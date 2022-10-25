# -*- coding: utf-8 -*-
# Unit tests for the Endpoint class.
#
#  Mocked API responses are declared as static test fixtures for now.  This is a brittle approach, as any schema changes
#  in those calls will not be reflected here unless manually updated.  Long term, we'll want to generate these fixtures
#  dynamically from a shared schema, like swagger.  Additionally, some of the patching of methods is a tad cumbersome.
#  We'll want to consider a less verbose approach for patching in the future (decorators).

import os
import pytest

from copy import deepcopy
from typing import Dict, Any
from unittest.mock import patch

from client.verta.verta.endpoint import Endpoint
from client.verta.verta._internal_utils._utils import Connection, Configuration
from client.verta.verta.credentials import EmailCredentials

#---------------------------------------------------------------------------------------------------------------------
# TEST FIXTURES
#---------------------------------------------------------------------------------------------------------------------
# This section contains the test fixtures required for testing the Endpoint class,

@pytest.fixture
@patch.dict(os.environ, {'VERTA_EMAIL': 'test_email@verta.ai', 'VERTA_DEV_KEY':'123test1232dev1232key123'})
def mock_conn() -> Connection:
    """ Return a mocked object of the _internal_utils._utils.Connection class for use in tests """
    return Connection(
        scheme='https',
        socket='test_socket',
        credentials=EmailCredentials.load_from_os_env()
    )

@pytest.fixture
def mock_config() -> Configuration:
    """ Return a mocked object of the _internal_utils._utils.Configuration class for use in tests """
    return Configuration(use_git=False, debug=False)

@pytest.fixture
def mock_endpoint(mock_conn, mock_config) -> Endpoint:
    """ Use the mocked elements above to generate  an object of the Endpoint class for use in tests """
    return Endpoint(conn=mock_conn, conf=mock_config, workspace=456, id=123)

#---------------------------------------------------------------------------------------------------------------------
# GLOBAL VARIABLES
#---------------------------------------------------------------------------------------------------------------------
# A few helpful variables and some big, ugly simulated responses from the back-end API called by these methods.  See
# note at top of file about the long term strategy for generating those types of test fixtures dynamically.

VERTA_CLASS: str= 'client.verta.verta.endpoint.Endpoint.'  # patch() requires the complete path to the module being
                # patched.  This variable just avoids clutter caused by the length of paths for the client.
WORKSPACE_ID: int = 456  # Maintain a consistent value across all tests
DEPLOYMENT_ID: int = 123  # Maintain a consistent value across all tests

# Expected response from the _get_json_by_id method as of 2022-10-24
GET_JSON_BY_ID_RESPONSE: Dict[str, Any] = {
    "creator_request": {
        "custom_permission": {
            "collaborator_type": "READ_ONLY"
        },
        "description": "test_description",
        "path": "/test_path",
        "resource_visibility": "PRIVATE",
        "visibility": "PRIVATE"
    },
    "date_created": "2022-10-20T00:00:00.000Z",
    "date_updated": "2022-10-20T00:00:00.000Z",
    "full_url": "https://test_socket/api/v1/predict/test_path",
    "id": DEPLOYMENT_ID,
    "owner_id": "test_owner",
    "workspace_id": WORKSPACE_ID
}

# Expected response from the get_status method as of 2022-10-24
GET_STATUS_RESPONSE: Dict[str, Any] = {
    "components": [
        {
            "build_id": 0,
            "message": "test_message",
            "ratio": 0,
            "status": "active"
        }
    ],
    "creator_request": {
        "autocreate_token": True,
        "enable_prediction_authz": False,
        "enable_prediction_tokens": True,
        "name": "test_name"
    },
    "date_created": "2022-10-20T00:00:00.000Z",
    "date_updated": "2022-10-20T00:00:00.000Z",
    "id": DEPLOYMENT_ID,
    "status": "active"
}

# Expected response from the get_access_token method as of 2022-10-24
GET_ACCESS_TOKEN_RESPONSE: str =  '123-test-456-token-789'
#---------------------------------------------------------------------------------------------------------------------
# UNIT TESTS
#---------------------------------------------------------------------------------------------------------------------

@patch(f'{VERTA_CLASS}get_status', return_value=GET_STATUS_RESPONSE)
@patch(f'{VERTA_CLASS}_get_json_by_id', return_value=GET_JSON_BY_ID_RESPONSE)
@patch(f'{VERTA_CLASS}get_access_token', return_value=GET_ACCESS_TOKEN_RESPONSE)
def test_get_deployed_model_call_get_status(mock_get_status,
                                            mock_get_json_by_id,
                                            mock_get_access_token,
                                            mock_endpoint,
                                            mock_conn) -> None:
    """ Verify that get_deployed_model calls the methods it should with the expected params """
    mock_endpoint.get_deployed_model()
    mock_get_status.assert_called_once()
    mock_get_json_by_id.assert_called_once_with(mock_conn, WORKSPACE_ID, DEPLOYMENT_ID)
    mock_get_access_token.assert_called_once()


@patch(f'{VERTA_CLASS}get_status', return_value=GET_STATUS_RESPONSE)
@patch(f'{VERTA_CLASS}_get_json_by_id', return_value=GET_JSON_BY_ID_RESPONSE)
@patch(f'{VERTA_CLASS}get_access_token', return_value=GET_ACCESS_TOKEN_RESPONSE)
def test_get_deployed_model_with_full_url(mock_get_status,  # pass in patched methods in order
                                          mock_get_json_by_id,
                                          mock_get_access_token,
                                          mock_endpoint) -> None:
    """ Verify that the get_deployed_model method returns the correct value for the full_url when it is returned
       by the get_json_by_id method.  The 'full_url' key was added to the schema of the response 10/2022.
    """
    deployed_model = mock_endpoint.get_deployed_model()
    assert deployed_model.prediction_url == 'https://test_socket/api/v1/predict/test_path'


GET_JSON_BY_ID_RESPONSE_MISSING_URL: Dict[str, Any] = deepcopy(GET_JSON_BY_ID_RESPONSE)
GET_JSON_BY_ID_RESPONSE_MISSING_URL.pop('full_url')  # Remove the full url key and value from the dict.
@patch(f'{VERTA_CLASS}get_status', return_value=GET_STATUS_RESPONSE)
@patch(f'{VERTA_CLASS}_get_json_by_id', return_value=GET_JSON_BY_ID_RESPONSE_MISSING_URL)
@patch(f'{VERTA_CLASS}get_access_token', return_value=GET_ACCESS_TOKEN_RESPONSE)
def test_get_deployed_model_missing_full_url(mock_get_status,  # pass in patched methods in order
                                             mock_get_json_by_id,
                                             mock_get_access_token,
                                             mock_endpoint) -> None:
    """ Verify that the get_deployed_model method returns the correct value for the full_url when it is returned
       by the get_json_by_id method.  The 'full_url' key was added to the schema of the response 10/2022.
    """
    deployed_model = mock_endpoint.get_deployed_model()
    assert deployed_model.prediction_url == 'https://test_socket/api/v1/predict/test_path'