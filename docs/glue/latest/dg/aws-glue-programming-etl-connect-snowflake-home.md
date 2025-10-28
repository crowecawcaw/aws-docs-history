# Snowflake connections

You can use AWS Glue for Spark to read from and write to tables in Snowflake in AWS Glue 4.0 and later versions.
You can read from Snowflake with a SQL query. You can connect to Snowflake using a user and password.
You can refer to Snowflake credentials stored in AWS Secrets Manager through the AWS Glue Data Catalog.
Data Catalog Snowflake credentials for AWS Glue for Spark are stored separately from Data Catalog Snowflake credentials for
crawlers. You must choose a `SNOWFLAKE`
type connection and not a `JDBC` type connection configured to connect to Snowflake.

For more information about Snowflake, see the [Snowflake
website](https://www.snowflake.com/ "https://www.snowflake.com/"). For more information about Snowflake on AWS, see [Snowflake Data Warehouse on
Amazon Web Services](https://aws.amazon.com/financial-services/partner-solutions/snowflake/ "https://aws.amazon.com/financial-services/partner-solutions/snowflake/").

## Configuring Snowflake connections

There are no AWS prerequisites to connecting to Snowflake databases available through the internet.

Optionally, you can perform the following configuration to manage your connection credentials with AWS Glue.

###### To manage your connection credentials with AWS Glue

1. In Snowflake, generate a user, `snowflakeUser` and password, `snowflakePassword`.
2. In AWS Secrets Manager, create a secret using your Snowflake credentials.
   To create a secret in Secrets Manager, follow the tutorial available in
   [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md#create_secret_cli "../../../secretsmanager/latest/userguide/create_secret.md#create_secret_cli") in the AWS Secrets Manager documentation.
   After creating the secret, keep the Secret name, `secretName` for the next step.
   - When selecting **Key/value pairs**, create a pair for
     `snowflakeUser` with the key `USERNAME`.
   - When selecting **Key/value pairs**, create a pair for
     `snowflakePassword` with the key `PASSWORD`.
   - When selecting **Key/value pairs**, you can provide your Snowflake
     warehouse with the key `sfWarehouse`.
   - When selecting **Key/value pairs**, you can provide additional Snowflake connection properties using their corresponding Spark property names as keys. Supported properties include:
     - `sfDatabase` - Snowflake database name
     - `sfSchema` - Snowflake schema name
     - `sfRole` - Snowflake role name
     - `pem_private_key` - Private key for key-pair authentication

3. In the AWS Glue Data Catalog, create a connection by choosing **Connections**, then **Create connection**. Following the steps in the connection wizard
   to complete the process:
   - When selecting a **Data source**, select Snowflake, then choose **Next**.
   - Enter the connection details such as host and port. When entering the host **Snowflake URL**, provide the URL of your Snowflake instance.
     The URL will typically use a hostname in the form ``account_identifier`.snowflakecomputing.com`.
     However, the URL format may vary depending on your Snowflake account type (for example, AWS, Azure, or Snowflake-hosted).
   - When selecting the IAM service role, choose from the drop-down menu. This is the IAM role from your account that will be used to access AWS Secrets Manager and assign IP
     if VPC is specified.
   - When selecting an **AWS Secret**, provide `secretName`.

4. In the next step in the wizard, set properties for your Snowflake connection.
5. In the final step in the wizard, review your settings and then complete the process to create your connection.

In the following situations, you may require the following:

- For Snowflake hosted on AWS in an Amazon VPC
  - You will need appropriate Amazon VPC configuration for Snowflake. For more information on how
    to configure your Amazon VPC, consult [AWS PrivateLink
    & Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink "https://docs.snowflake.com/en/user-guide/admin-security-privatelink") in the Snowflake documentation.
  - You will need appropriate Amazon VPC configuration for AWS Glue. [Configuring interface VPC endpoints (AWS PrivateLink) for AWS Glue
    (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
  - You will need to create a AWS Glue Data Catalog connection that provides Amazon VPC connection
    information (in addition to the id of an AWS Secrets Manager secret that defines your Snowflake
    security credentials). Your URL will change when using AWS PrivateLink, as described in the
    Snowflake documentation linked in a previous item.
  - You will need your job configuration in include the Data Catalog connection as an **Additional network
    connection**.

## Reading from Snowflake tables

**Prerequisites:** A Snowflake table you would like to read from. You will
need the Snowflake table name, `tableName`. You will
need your Snowflake url `snowflakeUrl`, username
`snowflakeUser` and password `snowflakePassword`.
If your Snowflake user does not have a default namespace set,
you will need the Snowflake database name, `databaseName` and the schema name `schemaName`.
Additionally, if your Snowflake user does not have a default warehouse set, you will need a warehouse name
`warehouseName`.

For example:

**Additional Prerequisites:** Complete the steps _To
manage your connection credentials with AWS Glue_ to configure
`snowflakeUrl`, `snowflakeUsername` and
`snowflakePassword`. To review these steps, see [Configuring Snowflake connections](#aws-glue-programming-etl-connect-snowflake-configure "#aws-glue-programming-etl-connect-snowflake-configure"), the previous section. To select which
**Additional network connection** to connect with, we will use the
`connectionName` parameter.

```
snowflake_read = glueContext.create_dynamic_frame.from_options(
  connection_type="snowflake",
  connection_options={
        "connectionName": "`connectionName`",
        "dbtable": "`tableName`",
        "sfDatabase": "`databaseName`",
        "sfSchema": "`schemaName`",
        "sfWarehouse": "`warehouseName`",
    }
)
```

Additionally, you can use the `autopushdown` and `query` parameters to read a
portion of a Snowflake table. This can be substantially more efficient than filtering your results after
they have been loaded into Spark. Consider an example where all sales are stored in the same table,
but you only need to analyze sales from a certain store on holidays. If that information is stored in
the table, you could use predicate pushdown to retrieve the results as follows:

```
snowflake_node = glueContext.create_dynamic_frame.from_options(
    connection_type="snowflake",
    connection_options={
        "autopushdown": "on",
        "query": "select * from sales where store='1' and IsHoliday='TRUE'",
        "connectionName": "snowflake-glue-conn",
        "sfDatabase": "`databaseName`",
        "sfSchema": "`schemaName`",
        "sfWarehouse": "`warehouseName`",
    }
)
```

## Writing to Snowflake tables

**Prerequisites:** A Snowflake database you would like to write to. You will
need a current or desired table name, `tableName`. You will
need your Snowflake url `snowflakeUrl`, username
`snowflakeUser` and password `snowflakePassword`.
If your Snowflake user does not have a default namespace set,
you will need the Snowflake database name, `databaseName` and the schema name `schemaName`.
Additionally, if your Snowflake user does not have a default warehouse set, you will need a warehouse name
`warehouseName`.

For example:

**Additional Prerequisites:** Complete the steps _To manage your
connection credentials with AWS Glue_ to configure
`snowflakeUrl`, `snowflakeUsername` and
`snowflakePassword`. To review these steps, see [Configuring Snowflake connections](#aws-glue-programming-etl-connect-snowflake-configure "#aws-glue-programming-etl-connect-snowflake-configure"), the previous section. To select which
**Additional network connection** to connect with, we will use the
`connectionName` parameter.

```
glueContext.write_dynamic_frame.from_options(
    connection_type="snowflake",
    connection_options={
        "connectionName": "`connectionName`",
        "dbtable": "`tableName`",
        "sfDatabase": "`databaseName`",
        "sfSchema": "`schemaName`",
        "sfWarehouse": "`warehouseName`",
    },
)
```

## Snowflake connection option reference

The Snowflake connection type takes the following connection options:

You can retrieve some of the parameters in this section from a Data Catalog connection (`sfUrl`,
`sfUser`, `sfPassword`), in which case you are not required to provide them. You can
do this by providing the parameter `connectionName`.

You can retrieve connection parameters from AWS Secrets Manager secrets using the `secretId` parameter. When using Secrets Manager, the following Spark properties can be automatically retrieved if present in the secret:

- `sfUser` (using key `USERNAME` or `sfUser`)
- `sfPassword` (using key `PASSWORD` or `sfPassword`)
- `sfWarehouse` (using key `sfWarehouse`)
- `sfDatabase` (using key `sfDatabase`)
- `sfSchema` (using key `sfSchema`)
- `sfRole` (using key `sfRole`)
- `pem_private_key` (using key `pem_private_key`)

**Property Precedence Order:** When the same property is specified in multiple locations, AWS Glue uses the following precedence order (highest to lowest):

1. Explicitly provided connection options in your job code
2. Data Catalog connection properties
3. AWS Secrets Manager secret values (when `secretId` is specified)
4. Snowflake user defaults

The following parameters are used generally when connecting to Snowflake.

- `sfDatabase` — Required if a user default is not set in Snowflake. Used for Read/Write. The database to use for the session after connecting.
- `sfSchema` — Required if a user default is not set in Snowflake. Used for Read/Write. The schema to use for the session after connecting.
- `sfWarehouse` — Required if a user default is not set in Snowflake. Used for Read/Write. The default virtual warehouse to use for the session after connecting.
- `sfRole` — Required if a user default is not set in Snowflake. Used for Read/Write. The default security role to use for the session after connecting.
- `sfUrl` — (Required) Used for Read/Write. Specifies the hostname for your
  account in the following format: ``account_identifier`.snowflakecomputing.com`. For more information
  about account identifiers, see [Account Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier "https://docs.snowflake.com/en/user-guide/admin-account-identifier") in the Snowflake documentation.
- `sfUser` — (Required) Used for Read/Write. Login name for the Snowflake user.
- `sfPassword` — (Required unless `pem_private_key` provided) Used for Read/Write. Password for the Snowflake user.
- `dbtable` — Required when working with full tables. Used for Read/Write. The name of the table to be read or the table to which data is written. When reading, all columns and records are retrieved.
- `pem_private_key` — Used for Read/Write. An unencrypted b64-encoded private key
  string. The private key for the Snowflake user. It is common to copy this out of a PEM file. For more information, see [Key-pair authentication and key-pair
  rotation](https://docs.snowflake.com/en/user-guide/key-pair-auth "https://docs.snowflake.com/en/user-guide/key-pair-auth") in the Snowflake documentation.
- `query` — Required when reading with a query. Used for Read. The exact query (`SELECT` statement) to run

The following options are used to configure specific behaviors during the process of connecting to Snowflake.

- `preactions` — Used for Read/Write. Valid Values: Semicolon separated list of
  SQL statements as String. SQL statements run before data is transferred between AWS Glue and Snowflake.
  If a statement contains `%s`, the `%s` is replaced with the table name referenced for the operation.
- `postactions` — Used for Read/Write. SQL statements run after data is transferred between AWS Glue and Snowflake.
  If a statement contains `%s`, the `%s` is replaced with the table name referenced for the operation.
- `autopushdown` — Default: `"on"`. Valid Values: `"on"`,
  `"off"`. This parameter controls whether automatic query pushdown is enabled. If pushdown
  is enabled, then when a query is run on Spark, if part of the query can be "pushed down" to the
  Snowflake server, it is pushed down. This improves performance of some queries. For information
  about whether your query can be pushed down, consult [Pushdown](https://docs.snowflake.com/en/user-guide/spark-connector-use#pushdown "https://docs.snowflake.com/en/user-guide/spark-connector-use#pushdown") in the
  Snowflake documentation.

Additionally, some of the options available on the Snowflake Spark connector may be supported in AWS Glue. For more information
about options available on the Snowflake Spark connector, see [Setting Configuration Options for the Connector](https://docs.snowflake.com/en/user-guide/spark-connector-use#setting-configuration-options-for-the-connector "https://docs.snowflake.com/en/user-guide/spark-connector-use#setting-configuration-options-for-the-connector")
in the Snowflake documentation.

## Snowflake authentication methods

AWS Glue supports the following authentication methods for connecting to Snowflake:

- **Username and Password Authentication:** Provide `sfUser` and `sfPassword` parameters.
- **Key-Pair Authentication:** Provide `sfUser` and `pem_private_key` parameters. When using key-pair authentication, the `sfPassword` parameter is not required.

Both authentication methods are fully supported and can be configured using any combination of connection options, Data Catalog connections, or AWS Secrets Manager secrets.

## Snowflake connector limitations

Connecting to Snowflake with AWS Glue for Spark is subject to the following limitations.

- This connector does not support job bookmarks. For more information about job bookmarks, see [Tracking processed data using job bookmarks](monitor-continuations.md "monitor-continuations.md").
- This connector does not support Snowflake reads and writes through tables in the AWS Glue Data Catalog using
  the `create_dynamic_frame.from_catalog` and `write_dynamic_frame.from_catalog` methods.
- This connector supports username/password authentication and key-pair authentication. Other authentication methods (such as OAuth or SAML) are not currently supported.
- This connector is not supported within streaming jobs.
- This connector supports `SELECT` statement based queries when retrieving information (such as with the
  `query` parameter). Other kind of queries (such as `SHOW`, `DESC`,
  or DML statements) are not supported.
- Snowflake limits the size of query text (i.e. SQL statements) submitted through Snowflake clients
  to 1 MB per statement. For more details, see [Limits on Query Text
  Size](https://docs.snowflake.com/en/user-guide/query-size-limits "https://docs.snowflake.com/en/user-guide/query-size-limits").
