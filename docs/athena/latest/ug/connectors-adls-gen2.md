# Amazon Athena Azure Data Lake Storage (ADLS) Gen2

connector

The Amazon Athena connector for [Azure Data Lake Storage (ADLS) Gen2](https://docs.microsoft.com/en-us/azure/databricks/data/data-sources/azure/adls-gen2/ "https://docs.microsoft.com/en-us/azure/databricks/data/data-sources/azure/adls-gen2/") enables Amazon Athena to run SQL queries on
data stored on ADLS. Athena cannot access stored files in the data lake directly.

This connector can be registered with Glue Data Catalog as a federated catalog.
It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

- Workflow – The connector implements the JDBC
  interface, which uses the `com.microsoft.sqlserver.jdbc.SQLServerDriver`
  driver. The connector passes queries to the Azure Synapse engine, which then
  accesses the data lake.
- Data handling and S3 – Normally, the Lambda
  connector queries data directly without transfer to Amazon S3. However, when data
  returned by the Lambda function exceeds Lambda limits, the data is written to the Amazon S3
  spill bucket that you specify so that Athena can read the excess.
- AAD authentication – AAD can be used as an
  authentication method for the Azure Synapse connector. In order to use AAD, the JDBC
  connection string that the connector uses must contain the URL parameters
  `authentication=ActiveDirectoryServicePrincipal`,
  `AADSecurePrincipalId`, and `AADSecurePrincipalSecret`.
  These parameters can either be passed in directly or by Secrets Manager.

## Prerequisites

- Deploy the connector to your AWS account using the Athena console or the AWS Serverless Application Repository. For more information, see [Create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md") or [Use the AWS Serverless Application Repository to deploy a data
  source connector](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md").

## Limitations

- Write DDL operations are not supported.
- In a multiplexer setup, the spill bucket and prefix are shared across all
  database instances.
- Any relevant Lambda limits. For more information, see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md") in the _AWS Lambda Developer Guide_.
- Date and timestamp data types in filter conditions must be cast to appropriate
  data types.

## Terms

The following terms relate to the Azure Data Lake Storage Gen2 connector.

- Database instance – Any instance of a
  database deployed on premises, on Amazon EC2, or on Amazon RDS.
- Handler – A Lambda handler that accesses
  your database instance. A handler can be for metadata or for data
  records.
- Metadata handler – A Lambda handler that
  retrieves metadata from your database instance.
- Record handler – A Lambda handler that
  retrieves data records from your database instance.
- Composite handler – A Lambda handler that
  retrieves both metadata and data records from your database instance.
- Property or parameter – A database
  property used by handlers to extract database information. You configure these
  properties as Lambda environment variables.
- Connection String – A string of text
  used to establish a connection to a database instance.
- Catalog – A non-AWS Glue catalog registered
  with Athena that is a required prefix for the `connection_string`
  property.
- Multiplexing handler – A Lambda handler
  that can accept and use multiple database connections.

## Parameters

Use the parameters in this section to configure the Azure Data Lake Storage Gen2 connector.

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created prior to December 3, 2024. These can differ from their corresponding [AWS Glue connection properties](../../../glue/latest/dg/connection-properties.md "../../../glue/latest/dg/connection-properties.md"). Starting December 3, 2024, use the parameters below only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector.

We recommend that you configure a Azure Data Lake Storage Gen2 connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the Azure Data Lake Storage Gen2 connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type DATALAKEGEN2
```

**Lambda environment properties**

- glue_connection – Specifies the name of the Glue connection associated with the federated connector.
- **casing_mode** – (Optional) Specifies
  how to handle casing for schema and table names. The
  `casing_mode` parameter uses the following values to specify
  the behavior of casing:
  - **none** – Do not change case
    of the given schema and table names. This is the default for
    connectors that have an associated glue connection.
  - **upper** –
    Upper case all given schema and table names.
  - **lower** –
    Lower case all given schema and table names.

###### Note

- All connectors that use Glue connections must use AWS Secrets Manager to store credentials.
- The Azure Data Lake Storage Gen2 connector created using Glue connections does not support the use of a multiplexing handler.
- The Azure Data Lake Storage Gen2 connector created using Glue connections only supports `ConnectionSchemaVersion` 2.

#### Connection string

Use a JDBC connection string in the following format to connect to a database
instance.

```
datalakegentwo://${`jdbc_connection_string`}
```

#### Using a

multiplexing handler

You can use a multiplexer to connect to multiple database instances with a single
Lambda function. Requests are routed by catalog name. Use the following classes in
Lambda.

| Handler           | Class                             |
| ----------------- | --------------------------------- |
| Composite handler | `DataLakeGen2MuxCompositeHandler` |
| Metadata handler  | `DataLakeGen2MuxMetadataHandler`  |
| Record handler    | `DataLakeGen2MuxRecordHandler`    |

##### Multiplexing handler parameters

| Parameter                      | Description                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$`catalog`_connection_string` | Required. A database instance connection string. Prefix the<br>environment variable with the name of the catalog used in Athena. For example,<br>if the catalog registered with Athena is<br>`mydatalakegentwocatalog`, then the environment<br>variable name is<br>`mydatalakegentwocatalog_connection_string`. |
| `default`                      | Required. The default connection string. This string is used<br>when the catalog is<br>`lambda:${``AWS_LAMBDA_FUNCTION_NAME``}`.                                                                                                                                                                                 |

The following example properties are for a DataLakeGen2 MUX Lambda function
that supports two database instances: `datalakegentwo1` (the
default), and `datalakegentwo2`.

| Property                                    | Value                                                                                                            |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `default`                                   | `datalakegentwo://jdbc:sqlserver://adlsgentwo1.`hostname`:`port`;databaseName=`database_name`;${`secret1_name`}` |
| `datalakegentwo_catalog1_connection_string` | `datalakegentwo://jdbc:sqlserver://adlsgentwo1.`hostname`:`port`;databaseName=`database_name`;${`secret1_name`}` |
| `datalakegentwo_catalog2_connection_string` | `datalakegentwo://jdbc:sqlserver://adlsgentwo2.`hostname`:`port`;databaseName=`database_name`;${`secret2_name`}` |

##### Providing

credentials

To provide a user name and password for your database in your JDBC connection
string, you can use connection string properties or AWS Secrets Manager.

- Connection String – A user name
  and password can be specified as properties in the JDBC connection
  string.

###### Important

As a security best practice, don't use hardcoded credentials in your
environment variables or connection strings. For information about moving
your hardcoded secrets to AWS Secrets Manager, see [Move hardcoded
secrets to AWS Secrets Manager](../../../secretsmanager/latest/userguide/hardcoded.md "../../../secretsmanager/latest/userguide/hardcoded.md") in the
_AWS Secrets Manager User Guide_.

- AWS Secrets Manager – To use the Athena
  Federated Query feature with AWS Secrets Manager, the VPC connected to your Lambda
  function should have [internet access](https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/ "https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/") or a [VPC
  endpoint](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md") to connect to Secrets Manager.

You can put the name of a secret in AWS Secrets Manager in your JDBC connection
string. The connector replaces the secret name with the
`username` and `password` values from
Secrets Manager.

For Amazon RDS database instances, this support is tightly integrated. If
you use Amazon RDS, we highly recommend using AWS Secrets Manager and credential
rotation. If your database does not use Amazon RDS, store the credentials as
JSON in the following format:

```
{"username": "${username}", "password": "${password}"}
```

###### Example connection string with secret name

The following string has the secret name
`${secret1_name}`.

```
datalakegentwo://jdbc:sqlserver://`hostname`:`port`;databaseName=`database_name`;${secret1_name}
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
datalakegentwo://jdbc:sqlserver://`hostname`:`port`;databaseName=`database_name`;user=`user_name`;password=`password`
```

#### Using a

single connection handler

You can use the following single connection metadata and record handlers to
connect to a single Azure Data Lake Storage Gen2 instance.

| Handler type      | Class                          |
| ----------------- | ------------------------------ |
| Composite handler | `DataLakeGen2CompositeHandler` |
| Metadata handler  | `DataLakeGen2MetadataHandler`  |
| Record handler    | `DataLakeGen2RecordHandler`    |

##### Single connection handler parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `default` | Required. The default connection string. |

The single connection handlers support one database instance and must provide a
`default` connection string parameter. All other connection
strings are ignored.

The following example property is for a single Azure Data Lake Storage Gen2 instance supported by a Lambda function.

| Property  | Value                                                                                |
| --------- | ------------------------------------------------------------------------------------ |
| `default` | `datalakegentwo://jdbc:sqlserver://`hostname`:`port`;databaseName=;${`secret_name`}` |

#### Spill parameters

The Lambda SDK can spill data to Amazon S3. All database instances accessed by the same
Lambda function spill to the same location.

| Parameter                   | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `spill_bucket`              | Required. Spill bucket name.                                                                                                                                                                                                                                                                                                                                                                           |
| `spill_prefix`              | Required. Spill bucket key<br>prefix.                                                                                                                                                                                                                                                                                                                                                                  |
| `spill_put_request_headers` | (Optional) A JSON encoded map of request headers and values for<br>the Amazon S3 `putObject` request that is used for spilling<br>(for example, `{"x-amz-server-side-encryption" :<br>"AES256"}`). For other possible headers, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md")<br>in the _Amazon Simple Storage Service API Reference_. |

## Data type support

The following table shows the corresponding data types for ADLS Gen2 and Arrow.

| ADLS Gen2      | Arrow             |
| -------------- | ----------------- |
| bit            | TINYINT           |
| tinyint        | SMALLINT          |
| smallint       | SMALLINT          |
| int            | INT               |
| bigint         | BIGINT            |
| decimal        | DECIMAL           |
| numeric        | FLOAT8            |
| smallmoney     | FLOAT8            |
| money          | DECIMAL           |
| float[24]      | FLOAT4            |
| float[53]      | FLOAT8            |
| real           | FLOAT4            |
| datetime       | Date(MILLISECOND) |
| datetime2      | Date(MILLISECOND) |
| smalldatetime  | Date(MILLISECOND) |
| date           | Date(DAY)         |
| time           | VARCHAR           |
| datetimeoffset | Date(MILLISECOND) |
| char[n]        | VARCHAR           |
| varchar[n/max] | VARCHAR           |

## Partitions and

splits

Azure Data Lake Storage Gen2 uses Hadoop compatible Gen2 blob storage for storing data
files. The data from these files is queried from the Azure Synapse engine. The Azure
Synapse engine treats Gen2 data stored in file systems as external tables. The
partitions are implemented based on the type of data. If the data has already been
partitioned and distributed within the Gen 2 storage system, the connector retrieves the
data as single split.

## Performance

The Azure Data Lake Storage Gen2 connector shows slower query performance when running multiple queries at
once, and is subject to throttling.

The Athena Azure Data Lake Storage Gen2 connector performs predicate pushdown to decrease the data scanned by the query. Simple predicates and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time.

### Predicates

A predicate is an expression in the `WHERE` clause of a SQL query that
evaluates to a Boolean value and filters rows based on multiple conditions. The
Athena Azure Data Lake Storage Gen2 connector can combine these expressions and push them directly to
Azure Data Lake Storage Gen2 for enhanced functionality and to reduce the amount of data scanned.

The following Athena Azure Data Lake Storage Gen2 connector operators support predicate
pushdown:

- Boolean: AND, OR, NOT
- Equality: EQUAL, NOT_EQUAL, LESS_THAN,
  LESS_THAN_OR_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, NULL_IF,
  IS_NULL
- Arithmetic: ADD, SUBTRACT, MULTIPLY,
  DIVIDE, MODULUS, NEGATE
- Other: LIKE_PATTERN, IN

### Combined

pushdown example

For enhanced querying capabilities, combine the pushdown types, as in the following example:

```
SELECT *
FROM my_table
WHERE col_a > 10
    AND ((col_a + col_b) > (col_c % col_d))
    AND (col_e IN ('val1', 'val2', 'val3') OR col_f LIKE '%pattern%');
```

## Passthrough

queries

The Azure Data Lake Storage Gen2 connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md"). Passthrough
queries use a table function to push your full query down to the data source for
execution.

To use passthrough queries with Azure Data Lake Storage Gen2, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '`query string`'
        ))
```

The following example query pushes down a query to a data source in Azure Data Lake Storage Gen2. The query
selects all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer LIMIT 10'
        ))
```

## License information

By using this connector, you acknowledge the inclusion of third party components, a list
of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-datalakegen2/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-datalakegen2/pom.xml") file for this connector, and agree to the terms in the respective third
party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-datalakegen2/LICENSE.txt "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-datalakegen2/LICENSE.txt") file on GitHub.com.

## Additional resources

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-datalakegen2/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-datalakegen2/pom.xml") file for the Azure Data Lake Storage Gen2 connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-datalakegen2 "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-datalakegen2") on GitHub.com.
