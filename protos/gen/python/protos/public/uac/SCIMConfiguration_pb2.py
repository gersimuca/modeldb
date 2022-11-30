# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uac/SCIMConfiguration.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..uac import UACService_pb2 as uac_dot_UACService__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uac/SCIMConfiguration.proto',
  package='ai.verta.uac',
  syntax='proto3',
  serialized_options=b'P\001Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uac',
  serialized_pb=b'\n\x1buac/SCIMConfiguration.proto\x12\x0c\x61i.verta.uac\x1a\x1cgoogle/api/annotations.proto\x1a\x14uac/UACService.proto\"[\n\x11SCIMConfiguration\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05token\x18\x02 \x01(\t\x12\x14\n\x0cmultiple_org\x18\x03 \x01(\x08\x12\x10\n\x08org_name\x18\x04 \x01(\t2\x87\x01\n\x18SCIMConfigurationService\x12k\n\x10getConfiguration\x12\x13.ai.verta.uac.Empty\x1a\x1f.ai.verta.uac.SCIMConfiguration\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/scim/getConfigurationB>P\x01Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uacb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,uac_dot_UACService__pb2.DESCRIPTOR,])




_SCIMCONFIGURATION = _descriptor.Descriptor(
  name='SCIMConfiguration',
  full_name='ai.verta.uac.SCIMConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='ai.verta.uac.SCIMConfiguration.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='ai.verta.uac.SCIMConfiguration.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiple_org', full_name='ai.verta.uac.SCIMConfiguration.multiple_org', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org_name', full_name='ai.verta.uac.SCIMConfiguration.org_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=188,
)

DESCRIPTOR.message_types_by_name['SCIMConfiguration'] = _SCIMCONFIGURATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SCIMConfiguration = _reflection.GeneratedProtocolMessageType('SCIMConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _SCIMCONFIGURATION,
  '__module__' : 'uac.SCIMConfiguration_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.SCIMConfiguration)
  })
_sym_db.RegisterMessage(SCIMConfiguration)


DESCRIPTOR._options = None

_SCIMCONFIGURATIONSERVICE = _descriptor.ServiceDescriptor(
  name='SCIMConfigurationService',
  full_name='ai.verta.uac.SCIMConfigurationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=191,
  serialized_end=326,
  methods=[
  _descriptor.MethodDescriptor(
    name='getConfiguration',
    full_name='ai.verta.uac.SCIMConfigurationService.getConfiguration',
    index=0,
    containing_service=None,
    input_type=uac_dot_UACService__pb2._EMPTY,
    output_type=_SCIMCONFIGURATION,
    serialized_options=b'\202\323\344\223\002\033\022\031/v1/scim/getConfiguration',
  ),
])
_sym_db.RegisterServiceDescriptor(_SCIMCONFIGURATIONSERVICE)

DESCRIPTOR.services_by_name['SCIMConfigurationService'] = _SCIMCONFIGURATIONSERVICE

# @@protoc_insertion_point(module_scope)
