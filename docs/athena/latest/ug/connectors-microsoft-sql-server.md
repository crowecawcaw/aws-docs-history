# Amazon Athena Microsoft SQL Server connector

The Amazon Athena connector for [Microsoft SQL
Server](https://docs.microsoft.com/en-us/sql/?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/?view=sql-server-ver15") enables Amazon Athena to run SQL queries on your data stored in Microsoft SQL
Server using JDBC.

This connector can be registered with Glue Data Catalog as a federated catalog.
It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

## Prerequisites

- Deploy the connector to your AWS account using the Athena console or the AWS Serverless Application Repository. For more information, see [Create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md") or [Use the AWS Serverless Application Repository to deploy a data source connector](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md").

## Limitations

- Write DDL operations are not supported.
- In a multiplexer setup, the spill bucket and prefix are shared across all
  database instances.
- Any relevant Lambda limits. For more information, see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md") in the _AWS Lambda Developer Guide_.
- In filter conditions, you must cast the `Date` and
  `Timestamp` data types to the appropriate data type.
- To search for negative values of type `Real` and
  `Float`, use the `<=` or `>=`
  operator.
- The `binary`, `varbinary`, `image`, and
  `rowversion` data types are not supported.

## Terms

The following terms relate to the SQL Server connector.

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

Use the parameters in this section to configure the SQL Server connector.

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created prior to December 3, 2024. These can differ from their corresponding [AWS Glue connection properties](../../../glue/latest/dg/connection-properties.md "../../../glue/latest/dg/connection-properties.md"). Starting December 3, 2024, use the parameters below only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector.

We recommend that you configure a SQL Server connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the SQL Server connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type SQLSERVER
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
- The SQL Server connector created using Glue connections does not support the use of a multiplexing handler.
- The SQL Server connector created using Glue connections only supports `ConnectionSchemaVersion` 2.

#### Connection string

Use a JDBC connection string in the following format to connect to a database
instance.

```
sqlserver://${`jdbc_connection_string`}
```

#### Using a multiplexing handler

You can use a multiplexer to connect to multiple database instances with a single
Lambda function. Requests are routed by catalog name. Use the following classes in
Lambda.

| Handler           | Class                          |
| ----------------- | ------------------------------ |
| Composite handler | `SqlServerMuxCompositeHandler` |
| Metadata handler  | `SqlServerMuxMetadataHandler`  |
| Record handler    | `SqlServerMuxRecordHandler`    |

##### Multiplexing handler parameters

| Parameter                      | Description                                                                                                                                                                                                                                                                                            |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `$`catalog`_connection_string` | Required. A database instance connection string. Prefix the<br>environment variable with the name of the catalog used in Athena. For example,<br>if the catalog registered with Athena is<br>`mysqlservercatalog`, then the environment<br>variable name is<br>`mysqlservercatalog_connection_string`. |
| `default`                      | Required. The default connection string. This string is used<br>when the catalog is<br>`lambda:${``AWS_LAMBDA_FUNCTION_NAME``}`.                                                                                                                                                                       |

The following example properties are for a SqlServer MUX Lambda function
that supports two database instances: `sqlserver1` (the
default), and `sqlserver2`.

| Property                               | Value                                                                                                        |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `default`                              | `sqlserver://jdbc:sqlserver://sqlserver1.`hostname`:`port`;databaseName=`<database_name>`;${`secret1_name`}` |
| `sqlserver_catalog1_connection_string` | `sqlserver://jdbc:sqlserver://sqlserver1.`hostname`:`port`;databaseName=`<database_name>`;${`secret1_name`}` |
| `sqlserver_catalog2_connection_string` | `sqlserver://jdbc:sqlserver://sqlserver2.`hostname`:`port`;databaseName=`<database_name>`;${`secret2_name`}` |

##### Providing credentials

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
`${secret_name}`.

```
sqlserver://jdbc:sqlserver://`hostname`:`port`;databaseName=`<database_name>`;${`secret_name`}
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
sqlserver://jdbc:sqlserver://`hostname`:`port`;databaseName=`<database_name>`;user=`<user>`;password=`<password>`
```

#### Using a single connection handler

You can use the following single connection metadata and record handlers to
connect to a single SQL Server instance.

| Handler type      | Class                       |
| ----------------- | --------------------------- |
| Composite handler | `SqlServerCompositeHandler` |
| Metadata handler  | `SqlServerMetadataHandler`  |
| Record handler    | `SqlServerRecordHandler`    |

##### Single connection handler parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `default` | Required. The default connection string. |

The single connection handlers support one database instance and must provide a
`default` connection string parameter. All other connection
strings are ignored.

The following example property is for a single SQL Server instance supported by a Lambda function.

| Property  | Value                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------ |
| `default` | `sqlserver://jdbc:sqlserver://`hostname`:`port`;databaseName=`<database_name>`;${`secret_name`}` |

#### Spill parameters

The Lambda SDK can spill data to Amazon S3. All database instances accessed by the same
Lambda function spill to the same location.

| Parameter                   | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `spill_bucket`              | Required. Spill bucket name.                                                                                                                                                                                                                                                                                                                                                                           |
| `spill_prefix`              | Required. Spill bucket key<br>prefix.                                                                                                                                                                                                                                                                                                                                                                  |
| `spill_put_request_headers` | (Optional) A JSON encoded map of request headers and values for<br>the Amazon S3 `putObject` request that is used for spilling<br>(for example, `{"x-amz-server-side-encryption" :<br>"AES256"}`). For other possible headers, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md")<br>in the _Amazon Simple Storage Service API Reference_. |

## Data type support

The following table shows the corresponding data types for SQL Server and Apache
Arrow.

| SQL Server      | Arrow             |
| --------------- | ----------------- |
| bit             | TINYINT           |
| tinyint         | SMALLINT          |
| smallint        | SMALLINT          |
| int             | INT               |
| bigint          | BIGINT            |
| decimal         | DECIMAL           |
| numeric         | FLOAT8            |
| smallmoney      | FLOAT8            |
| money           | DECIMAL           |
| float[24]       | FLOAT4            |
| float[53]       | FLOAT8            |
| real            | FLOAT4            |
| datetime        | Date(MILLISECOND) |
| datetime2       | Date(MILLISECOND) |
| smalldatetime   | Date(MILLISECOND) |
| date            | Date(DAY)         |
| time            | VARCHAR           |
| datetimeoffset  | Date(MILLISECOND) |
| char[n]         | VARCHAR           |
| varchar[n/max]  | VARCHAR           |
| nchar[n]        | VARCHAR           |
| nvarchar[n/max] | VARCHAR           |
| text            | VARCHAR           |
| ntext           | VARCHAR           |

## Partitions and splits

A partition is represented by a single partition column of type `varchar`.
In case of the SQL Server connector, a partition function determines how partitions are
applied on the table. The partition function and column name information are retrieved
from the SQL Server metadata table. A custom query then gets the partition. Splits are
created based upon the number of distinct partitions received.

## Performance

Selecting a subset of columns significantly speeds up query runtime and reduces data scanned. The SQL Server connector is resilient to throttling due to concurrency.

The Athena SQL Server connector performs predicate pushdown to decrease the data scanned by the query. Simple predicates and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time.

### Predicates

A predicate is an expression in the `WHERE` clause of a SQL query that
evaluates to a Boolean value and filters rows based on multiple conditions. The
Athena SQL Server connector can combine these expressions and push them directly to
SQL Server for enhanced functionality and to reduce the amount of data scanned.

The following Athena SQL Server connector operators support predicate
pushdown:

- Boolean: AND, OR, NOT
- Equality: EQUAL, NOT_EQUAL, LESS_THAN,
  LESS_THAN_OR_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_DISTINCT_FROM,
  NULL_IF, IS_NULL
- Arithmetic: ADD, SUBTRACT, MULTIPLY,
  DIVIDE, MODULUS, NEGATE
- Other: LIKE_PATTERN, IN

### Combined pushdown example

For enhanced querying capabilities, combine the pushdown types, as in the following example:

```
SELECT *
FROM my_table
WHERE col_a > 10
    AND ((col_a + col_b) > (col_c % col_d))
    AND (col_e IN ('val1', 'val2', 'val3') OR col_f LIKE '%pattern%');
```

## Passthrough queries

The SQL Server connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md"). Passthrough
queries use a table function to push your full query down to the data source for
execution.

To use passthrough queries with SQL Server, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '`query string`'
        ))
```

The following example query pushes down a query to a data source in SQL Server. The query
selects all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer LIMIT 10'
        ))
```

## License information

By using this connector, you acknowledge the inclusion of third party components, a list
of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-sqlserver/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-sqlserver/pom.xml") file for this connector, and agree to the terms in the respective third
party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-sqlserver/LICENSE.txt "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-sqlserver/LICENSE.txt") file on GitHub.com.

## Additional resources

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-sqlserver/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-sqlserver/pom.xml") file for the SQL Server connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-sqlserver "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-sqlserver") on GitHub.com.
