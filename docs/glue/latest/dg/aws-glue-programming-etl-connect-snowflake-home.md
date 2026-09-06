

# Snowflake connections
<a name="aws-glue-programming-etl-connect-snowflake-home"></a>

You can use AWS Glue for Spark to read from and write to tables in Snowflake in AWS Glue 4.0 and later versions. You can read from Snowflake with a SQL query. You can connect to Snowflake using one of three methods - basic authentication (using username and password), OAuth authentication, or key-pair authentication. You can refer to Snowflake credentials stored in AWS Secrets Manager through the AWS Glue Data connections. Data connection Snowflake credentials for AWS Glue for Spark are stored separately from Data Catalog Snowflake credentials for crawlers. You must choose a `SNOWFLAKE` type connection and not a `JDBC` type connection configured to connect to Snowflake.

For more information about Snowflake, see the [Snowflake website](https://www.snowflake.com/). For more information about Snowflake on AWS, see [Snowflake Data Warehouse on Amazon Web Services](https://aws.amazon.com/financial-services/partner-solutions/snowflake/).

## Configuring Snowflake connections
<a name="aws-glue-programming-etl-connect-snowflake-configure"></a>

There are no AWS prerequisites to connecting to Snowflake databases available through the internet.

Optionally, you can perform the following configuration to manage your connection credentials with AWS Glue.

**To manage your connection credentials with AWS Glue**

1. In AWS Secrets Manager, create a secret using your Snowflake credentials. To create a secret in Secrets Manager, follow the tutorial available in [ Create an AWS Secrets Manager secret ](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html#create_secret_cli) in the AWS Secrets Manager documentation. After creating the secret, keep the Secret name, {{secretName}} for the next step. 
   + For OAuth authentication:
     + When selecting **Key/value pairs**, create a pair for {{snowflakeUser}} with the key `sfUser`
     + When selecting **Key/value pairs**, create a pair for {{OAUTH\_CLIENT\_SECRET}} with the key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET`
   + For Key-pair authentication:
     + When selecting **Key/value pairs**, create a pair for {{snowflakeUser}} with the key `sfUser`
     + When selecting **Key/value pairs**, create a pair for {{private key}} with the key `pem_private_key`
   + For basic authentication:
     + When selecting **Key/value pairs**, create a pair for {{snowflakeUser}} with the key `USERNAME`
     + When selecting **Key/value pairs**, create a pair for {{snowflakePassword}} with the key `PASSWORD`
   + When selecting **Key/value pairs**, you can provide your Snowflake warehouse with the key `sfWarehouse`.
   + When selecting **Key/value pairs**, you can provide additional Snowflake connection properties using their corresponding Spark property names as keys. Supported properties include:
     + `sfDatabase` - Snowflake database name
     + `sfSchema` - Snowflake schema name
     + `sfRole` - Snowflake role name

1. In the AWS Glue Studio Console, create a connection by choosing **Data Connections**, then **Create connection**. Following the steps in the connection wizard to complete the process: 
   + When selecting a **Data source**, select Snowflake, then choose **Next**.
   + Enter the connection details such as host and port. When entering the host **Snowflake URL**, provide the URL of your Snowflake instance. The URL will typically use a hostname in the form `{{account_identifier}}.snowflakecomputing.com`. However, the URL format may vary depending on your Snowflake account type (for example, AWS, Azure, or Snowflake-hosted).
   + When selecting the IAM service role, choose from the drop-down menu. This is the IAM role from your account that will be used to access AWS Secrets Manager and assign IP if VPC is specified.
   + When selecting an **AWS Secret**, provide {{secretName}}.

1. In the next step in the wizard, set properties for your Snowflake connection. 

1. In the final step in the wizard, review your settings and then complete the process to create your connection.

For Snowflake hosted on AWS in an Amazon VPC, you may require the following:
+ You will need appropriate Amazon VPC configuration for Snowflake. For more information on how to configure your Amazon VPC, consult [AWS PrivateLink & Snowflake ](https://docs.snowflake.com/en/user-guide/admin-security-privatelink) in the Snowflake documentation.
+ You will need appropriate Amazon VPC configuration for AWS Glue. [Configuring interface VPC endpoints (AWS PrivateLink) for AWS Glue (AWS PrivateLink)](vpc-interface-endpoints.md).
+ You will need to create a AWS Glue Data Catalog connection that provides Amazon VPC connection information (in addition to the id of an AWS Secrets Manager secret that defines your Snowflake security credentials). Your URL will change when using AWS PrivateLink, as described in the Snowflake documentation linked in a previous item.
+ You will need your job configuration in include the Data Catalog connection as an **Additional network connection**.

## Reading from Snowflake tables
<a name="aws-glue-programming-etl-connect-snowflake-read"></a>

**Prerequisites:** A Snowflake table you would like to read from. You will need the Snowflake table name, {{tableName}}. If your Snowflake user does not have a default namespace set, you will need the Snowflake database name, {{databaseName}} and the schema name {{schemaName}}. Additionally, if your Snowflake user does not have a default warehouse set, you will need a warehouse name {{warehouseName}}. To select which **Additional network connection** to connect with, the `connectionName` parameter will be used.

```
snowflake_read = glueContext.create_dynamic_frame.from_options(
  connection_type="snowflake",
  connection_options={
        "connectionName": "{{connectionName}}",
        "dbtable": "{{tableName}}",
        "sfDatabase": "{{databaseName}}",
        "sfSchema": "{{schemaName}}",
        "sfWarehouse": "{{warehouseName}}",
    }
)
```

 Additionally, you can use the `autopushdown` and `query` parameters to read a portion of a Snowflake table. This can be substantially more efficient than filtering your results after they have been loaded into Spark. Consider an example where all sales are stored in the same table, but you only need to analyze sales from a certain store on holidays. If that information is stored in the table, you could use predicate pushdown to retrieve the results as follows:

```
snowflake_node = glueContext.create_dynamic_frame.from_options(
    connection_type="snowflake",
    connection_options={
        "autopushdown": "on",
        "query": "select * from sales where store='1' and IsHoliday='TRUE'",
        "connectionName": "snowflake-glue-conn",
        "sfDatabase": "{{databaseName}}",
        "sfSchema": "{{schemaName}}",
        "sfWarehouse": "{{warehouseName}}",
    }
)
```

## Writing to Snowflake tables
<a name="aws-glue-programming-etl-connect-snowflake-write"></a>

**Prerequisites:** A Snowflake database you would like to write to. You will need a current or desired table name, {{tableName}}. If your Snowflake user does not have a default namespace set, you will need the Snowflake database name, {{databaseName}} and the schema name {{schemaName}}. Additionally, if your Snowflake user does not have a default warehouse set, you will need a warehouse name {{warehouseName}}. To select which **Additional network connection** to connect with, the `connectionName` parameter will be used.

```
glueContext.write_dynamic_frame.from_options(
    connection_type="snowflake",
    connection_options={
        "connectionName": "{{connectionName}}",
        "dbtable": "{{tableName}}",
        "sfDatabase": "{{databaseName}}",
        "sfSchema": "{{schemaName}}",
        "sfWarehouse": "{{warehouseName}}",
    },
)
```

## Snowflake connection option reference
<a name="aws-glue-programming-etl-connect-snowflake-reference"></a>

The Snowflake connection type takes the following connection options:

You can retrieve some of the parameters in this section from a AWS Glue connection (`sfUrl`, `sfUser`, `sfPassword`), in which case you are not required to provide them. You can do this by providing the parameter `connectionName`.

You can retrieve connection parameters from AWS Secrets Manager secrets using the `secretId` parameter. When using Secrets Manager, the following Spark properties can be automatically retrieved if present in the secret:
+ `sfUser` (using key `USERNAME` or `sfUser`)
+ `sfPassword` (using key `PASSWORD` or `sfPassword`, when using basic authentication)
+ `sfWarehouse` (using key `sfWarehouse`)
+ `sfDatabase` (using key `sfDatabase`)
+ `sfSchema` (using key `sfSchema`)
+ `sfRole` (using key `sfRole`)
+ `pem_private_key` (using key `pem_private_key`, when using key-pair authentication)
+ `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` (when using OAuth authentication)

**Property Precedence Order:** When the same property is specified in multiple locations, AWS Glue uses the following precedence order (highest to lowest):

1. Explicitly provided connection options in your job code

1. Glue connection properties

1. AWS Secrets Manager secret values (when `secretId` is specified)

1. Snowflake user defaults

The following parameters are used generally when connecting to Snowflake.
+ `sfDatabase` — Required if a user default is not set in Snowflake. Used for Read/Write. The database to use for the session after connecting.
+ `sfSchema` — Required if a user default is not set in Snowflake. Used for Read/Write. The schema to use for the session after connecting.
+ `sfWarehouse` — Required if a user default is not set in Snowflake. Used for Read/Write. The default virtual warehouse to use for the session after connecting.
+ `sfRole` — Required if a user default is not set in Snowflake. Used for Read/Write. The default security role to use for the session after connecting.
+ `sfUrl` — (Required) Used for Read/Write. Specifies the hostname for your account in the following format: `{{account_identifier}}.snowflakecomputing.com`. For more information about account identifiers, see [Account Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier) in the Snowflake documentation.
+ `sfUser` — (Required) Used for Read/Write. Login name for the Snowflake user.
+ `sfPassword` — (Required when using basic authnetication) Used for Read/Write. Password for the Snowflake user.
+ `dbtable` — Required when working with full tables. Used for Read/Write. The name of the table to be read or the table to which data is written. When reading, all columns and records are retrieved.
+ `pem_private_key` — (Required when using key-pair authentication) Used for Read/Write. An unencrypted b64-encoded private key string. The private key for the Snowflake user. It is common to copy this out of a PEM file. For more information, see [Key-pair authentication and key-pair rotation](https://docs.snowflake.com/en/user-guide/key-pair-auth) in the Snowflake documentation.
+ `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` — (Required when using OAuth Authentication) Used for both read and write operations. This value corresponds to the OAUTH\_CLIENT\_SECRET, which can be obtained from the Snowflake security integration configured to enable OAuth-based authentication for your account. For more details, refer to your Snowflake OAuth security integration setup documentation - [Configure Snowflake OAuth for custom clients](https://docs.snowflake.com/en/user-guide/oauth-custom).
+ `query` — Required when reading with a query. Used for Read. The exact query (`SELECT` statement) to run

The following options are used to configure specific behaviors during the process of connecting to Snowflake.
+ `preactions` — Used for Read/Write. Valid Values: Semicolon separated list of SQL statements as String. SQL statements run before data is transferred between AWS Glue and Snowflake. If a statement contains `%s`, the `%s` is replaced with the table name referenced for the operation.
+ `postactions` — Used for Read/Write. SQL statements run after data is transferred between AWS Glue and Snowflake. If a statement contains `%s`, the `%s` is replaced with the table name referenced for the operation.
+ `autopushdown` — Default: `"on"`. Valid Values: `"on"`, `"off"`. This parameter controls whether automatic query pushdown is enabled. If pushdown is enabled, then when a query is run on Spark, if part of the query can be "pushed down" to the Snowflake server, it is pushed down. This improves performance of some queries. For information about whether your query can be pushed down, consult [Pushdown](https://docs.snowflake.com/en/user-guide/spark-connector-use#pushdown) in the Snowflake documentation.

Additionally, some of the options available on the Snowflake Spark connector may be supported in AWS Glue. For more information about options available on the Snowflake Spark connector, see [Setting Configuration Options for the Connector](https://docs.snowflake.com/en/user-guide/spark-connector-use#setting-configuration-options-for-the-connector) in the Snowflake documentation. 

## Snowflake authentication methods
<a name="aws-glue-programming-etl-connect-snowflake-authentication"></a>

AWS Glue supports the following authentication methods for connecting to Snowflake:
+ **Basic authentication:** Provide `sfUser` and `sfPassword` parameters.
+ **Key-pair authentication:** Provide `sfUser` and `pem_private_key` parameters. When using key-pair authentication, the `sfPassword` parameter is not required.
+ **OAuth authentication:** The Snowflake Connector supports the AUTHORIZATION\_CODE grant type to request access to your Snowflake data. This grant type is referred to as “3-legged OAuth”, as it involves redirecting users to a third-party authorization server where they can authenticate and approve access. This method is used when creating a connection through the AWS Glue Console. 
  + **Prerequisite:** To use this authentication method, ensure the following setup is complete: 
    + **Configure Snowflake OAuth for a custom client** by following the official Snowflake documentation: [Configure Snowflake OAuth for custom clients.](https://docs.snowflake.com/en/user-guide/oauth-custom) 
    + **Set the correct redirect URI** when creating the Snowflake security integration. For example: If you are creating the connection in the DUB (eu-west-1) region, your redirect URI should be: `https://eu-west-1.console.aws.amazon.com/gluestudio/oauth` 
    + After creating the security integration, retain the following information for use when creating the Glue connection: 
      + OAUTH\_CLIENT\_ID: This value should be provided as User Managed Client Application Client ID on the Glue connection creation page.
      + OAUTH\_CLIENT\_SECRET: This value should be stored in the AWS Secret used for the connection, under the key USER\_MANAGED\_CLIENT\_APPLICATION\_CLIENT\_SECRET.
  + OAuth Scopes — (Optional) Defines the specific permissions or levels of access requested from the Snowflake account. For example, a scope might limit access to a particular resource or operation.
    + This value can be specified in the following format: `session:role:Snowflake_Role_Name`
    + Example: `session:role:ANALYST_ROLE`
  + Authorization Code URL — (Required) The endpoint where the user is redirected to log in and grant authorization.
    + Example: `https://host/oauth/authorize`
  + Authorization Token URL — (Required) The endpoint used to exchange the authorization code for an access token.
    + Example: `https://host/oauth/token-request`
  + User Managed Client Application Client Id — (Required) The unique identifier for your registered OAuth client application in Snowflake
  + AWS Secret — (Required) Refers to an AWS Secrets Manager secret containing the following key-value pairs:
    + sfUser - The Snowflake username
    + USER\_MANAGED\_CLIENT\_APPLICATION\_CLIENT\_SECRET - The client secret associated with the OAuth client application

All three authentication methods are fully supported and can be configured using any combination of connection options, Glue connections, or AWS Secrets Manager secrets.

## Snowflake connector limitations
<a name="aws-glue-programming-etl-connect-snowflake-limitations"></a>

Connecting to Snowflake with AWS Glue for Spark is subject to the following limitations. 
+ This connector does not support job bookmarks. For more information about job bookmarks, see [Tracking processed data using job bookmarks](monitor-continuations.md).
+ This connector does not support Snowflake reads and writes through tables in the AWS Glue Data Catalog using the `create_dynamic_frame.from_catalog` and `write_dynamic_frame.from_catalog` methods.
+ This connector supports basic authentication, key-pair authentication, and OAuth authentication. Other authentication methods (such as SAML) are not currently supported.
+ This connector is not supported within streaming jobs.
+ This connector supports `SELECT` statement based queries when retrieving information (such as with the `query` parameter). Other kind of queries (such as `SHOW`, `DESC`, or DML statements) are not supported.
+ Snowflake limits the size of query text (i.e. SQL statements) submitted through Snowflake clients to 1 MB per statement. For more details, see [Limits on Query Text Size](https://docs.snowflake.com/en/user-guide/query-size-limits).