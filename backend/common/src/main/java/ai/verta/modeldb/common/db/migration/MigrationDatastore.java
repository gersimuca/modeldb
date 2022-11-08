package ai.verta.modeldb.common.db.migration;

import ai.verta.modeldb.common.config.RdbConfig;
import java.sql.Connection;
import java.sql.SQLException;

public interface MigrationDatastore {
  /** Lock the database in order to perform migrations. */
  void lock() throws SQLException;

  void unlock() throws SQLException;

  static MigrationDatastore create(RdbConfig config, Connection connection) {
    if (config.isH2()) {
      return new H2MigrationDatastore();
    }

    if (config.isMssql()) {
      return new SqlServerMigrationDatabase(connection);
    }

    if (config.isMysql()) {
      return new MySqlMigrationDatabase(connection);
    }

    throw new UnsupportedOperationException(
        "Unknown datastore for config. Requested dialect: " + config.getRdbDialect());
  }
}
