# Understand federated table name qualifiers

Athena uses the following terms to refer to hierarchies of data objects:

- Data source – a group of databases
- Database – a group of tables
- Table – data organized as a group of rows or
  columns
  Sometimes these objects are also referred to with alternate but equivalent names such as
  the following:

- A data source is sometimes referred to as a _catalog_.
- A database is sometimes referred to as a _schema_.

## Terms in federated data sources

When you query federated data sources, note that the underlying data source might not
use the same terminology as Athena. Keep this distinction in mind when you write your
federated queries. The following sections describe how data object terms in Athena
correspond to those in federated data sources.

### Amazon Redshift

An Amazon Redshift _database_ is a group of Redshift
_schemas_ that contains a group of Redshift
_tables_.

| Athena                       | Redshift                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| Redshift data source         | A Redshift connector Lambda function configured to point to a<br>Redshift `database`. |
| `data_source.database.table` | `database.schema.table`                                                               |

Example query

```
SELECT * FROM
`Athena_Redshift_connector_data_source`.`Redshift_schema_name`.`Redshift_table_name`
```

For more information about this connector, see [Amazon Athena Redshift connector](connectors-redshift.md "connectors-redshift.md").

### Cloudera Hive

An Cloudera Hive _server_ or _cluster_ is a group of Cloudera Hive _databases_ that contains a group of Cloudera Hive
_tables_.

| Athena                       | Hive                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| Cloudera Hive data source    | Cloudera Hive connector Lambda function configured to point to a<br>Cloudera Hive `server`. |
| `data_source.database.table` | `server.database.table`                                                                     |

Example query

```
SELECT * FROM
`Athena_Cloudera_Hive_connector_data_source`.`Cloudera_Hive_database_name`.`Cloudera_Hive_table_name`
```

For more information about this connector, see [Amazon Athena Cloudera Hive connector](connectors-cloudera-hive.md "connectors-cloudera-hive.md").

### Cloudera Impala

An Impala _server_ or _cluster_ is a group of Impala _databases_ that contains a group of Impala _tables_.

| Athena                       | Impala                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------ |
| Impala data source           | Impala connector Lambda function configured to point to an Impala<br>`server`. |
| `data_source.database.table` | `server.database.table`                                                        |

Example query

```
SELECT * FROM
`Athena_Impala_connector_data_source`.`Impala_database_name`.`Impala_table_name`
```

For more information about this connector, see [Amazon Athena Cloudera Impala connector](connectors-cloudera-impala.md "connectors-cloudera-impala.md").

### MySQL

A MySQL _server_ is a group of MySQL _databases_ that contains a group of MySQL _tables_.

| Athena                       | MySQL                                                                       |
| ---------------------------- | --------------------------------------------------------------------------- |
| MySQL data source            | MySQL connector Lambda function configured to point to a MySQL<br>`server`. |
| `data_source.database.table` | `server.database.table`                                                     |

Example query

```
SELECT * FROM
`Athena_MySQL_connector_data source`.`MySQL_database_name`.`MySQL_table_name`
```

For more information about this connector, see [Amazon Athena MySQL connector](connectors-mysql.md "connectors-mysql.md").

### Oracle

An Oracle _server_ (or _database_) is a group of Oracle _schemas_ that contains a group of Oracle _tables_.

| Athena                       | Oracle                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------ |
| Oracle data source           | Oracle connector Lambda function configured to point to an Oracle<br>`server`. |
| `data_source.database.table` | `server.schema.table`                                                          |

Example query

```
SELECT * FROM
`Athena_Oracle_connector_data_source`.`Oracle_schema_name`.`Oracle_table_name`
```

For more information about this connector, see [Amazon Athena Oracle connector](connectors-oracle.md "connectors-oracle.md").

### Postgres

A Postgres _server_ (or _cluster_) is a group of Postgres _databases_. A Postgres _database_ is
a group of Postgres _schemas_ that contains a group
of Postgres _tables_.

| Athena                       | Postgres                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------ |
| Postgres data source         | Postgres connector Lambda function configured to point to a<br>Postgres `server` and `database`. |
| `data_source.database.table` | `server.database.schema.table`                                                                   |

Example query

```
SELECT * FROM
`Athena_Postgres_connector_data_source`.`Postgres_schema_name`.`Postgres_table_name`
```

For more information about this connector, see [Amazon Athena PostgreSQL connector](connectors-postgresql.md "connectors-postgresql.md").
