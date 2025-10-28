# Azure SQL connections

You can use AWS Glue for Spark to read from and write to tables on Azure SQL Managed Instances in AWS Glue 4.0 and
later versions. You can define what to read from Azure SQL with a SQL query. You connect to Azure SQL using user
and password credentials stored in AWS Secrets Manager through a AWS Glue connection.

For more information about Azure SQL, consult the [Azure SQL documentation](https://azure.microsoft.com/en-us/products/azure-sql "https://azure.microsoft.com/en-us/products/azure-sql").

## Configuring Azure SQL connections

To connect to Azure SQL from AWS Glue, you will need to create and store your Azure SQL credentials
in a AWS Secrets Manager secret, then associate that secret with a Azure SQL AWS Glue connection.

###### To configure a connection to Azure SQL:

1.  In AWS Secrets Manager, create a secret using your Azure SQL credentials.
    To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
    After creating the secret, keep the Secret name, `secretName` for the next step.
    - When selecting **Key/value pairs**, create a pair for
      the key `user` with the value `azuresqlUsername`.
    - When selecting **Key/value pairs**, create a pair for
      the key `password` with the value `azuresqlPassword`.

2.  In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
    After creating the connection, keep the connection name, `connectionName`, for future use in AWS Glue.
    - When selecting a **Connection type**, select Azure SQL.
    - When providing **Azure SQL URL**, provide a JDBC endpoint URL.

    The URL must be in the following format:
    `jdbc:sqlserver://`databaseServerName`:`databasePort`;databaseName=`azuresqlDBname`;`.

    AWS Glue requires the following URL properties:

        + `databaseName` – A default database in Azure SQL to connect to.

    For more information about JDBC URLs for Azure SQL Managed Instances, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=azuresqldb-mi-current "https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=azuresqldb-mi-current").
    - When selecting an **AWS Secret**, provide `secretName`.

After creating a AWS Glue Azure SQL connection, you will need to perform the following steps before running your AWS Glue job:

- Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
- In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.

## Reading from Azure SQL tables

**Prerequisites:**

- A Azure SQL table you would like to read from. You will need identification information for the
  table, `databaseName` and `tableIdentifier`.

An Azure SQL table is identified by its database, schema and table name. You must provide
the database name and table name when connecting to Azure SQL. You also must provide the schema if
it is not the default, "public". Database is provided through a URL property in `connectionName`
, schema and table name through the `dbtable`.

- A AWS Glue Azure SQL connection configured to provide auth information. Complete the steps in the
  previous procedure, _To configure a connection to Azure SQL_ to
  configure your auth information. You will need the name of the AWS Glue connection,
  `connectionName`.

For example:

```
azuresql_read_table = glueContext.create_dynamic_frame.from_options(
    connection_type="azuresql",
    connection_options={
        "connectionName": "`connectionName`",
        "dbtable": "`tableIdentifier`"
    }
)
```

You can also provide a SELECT SQL query, to filter the results returned to your DynamicFrame. You will need to configure `query`.

For example:

```
azuresql_read_query = glueContext.create_dynamic_frame.from_options(
    connection_type="azuresql",
    connection_options={
        "connectionName": "`connectionName`",
        "query": "`query`"
    }
)
```

## Writing to Azure SQL tables

This example writes information from an existing DynamicFrame, `dynamicFrame` to
Azure SQL. If the table already has information, AWS Glue will append data from your DynamicFrame.

**Prerequisites:**

- A Azure SQL table you would like to write to. You will need identification information for the
  table, `databaseName` and `tableIdentifier`.

An Azure SQL table is identified by its database, schema and table name. You must provide
the database name and table name when connecting to Azure SQL. You also must provide the schema if
it is not the default, "public". Database is provided through a URL property in `connectionName`
, schema and table name through the `dbtable`.

- Azure SQL auth information. Complete the steps in the previous procedure, _To configure a connection to Azure SQL_ to configure your auth
  information. You will need the name of the AWS Glue connection,
  `connectionName`.

For example:

```
azuresql_write = glueContext.write_dynamic_frame.from_options(
    connection_type="azuresql",
    connection_options={
        "connectionName": "`connectionName`",
        "dbtable": "`tableIdentifier`"
    }
)
```

## Azure SQL connection option reference

- `connectionName` — Required. Used for Read/Write. The name of a AWS Glue Azure SQL
  connection configured to provide auth information to your connection method.
- `databaseName` — Used for Read/Write. Valid Values: Azure SQL database names. The name of the database in Azure SQL to connect to.
- `dbtable` — Required for writing, required for reading unless `query`
  is provided. Used for Read/Write. Valid Values: Names of Azure SQL tables, or period separated
  schema/table name combinations. Used to specify the table and schema that identify the table to
  connect to. The default schema is "public". If your table is in a non-default schema, provide this
  information in the form
  ``schemaName`.`tableName``.
- `query` — Used for Read. A Transact-SQL SELECT query defining what
  should be retrieved when reading from Azure SQL. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql?view=azuresqldb-mi-current "https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql?view=azuresqldb-mi-current").
