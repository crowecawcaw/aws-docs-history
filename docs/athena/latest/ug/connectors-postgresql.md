# Amazon Athena PostgreSQL connector

The Amazon Athena PostgreSQL connector enables Athena to access your PostgreSQL
databases.

This connector can be registered with Glue Data Catalog as a federated catalog.
It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

## Prerequisites

- Deploy the connector to your AWS account using the Athena console or the AWS Serverless Application Repository. For more information, see [Create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md") or [Use the AWS Serverless Application Repository to deploy a data
  source connector](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md").

## Limitations

- Write DDL operations are not supported.
- In a multiplexer setup, the spill bucket and prefix are shared across all
  database instances.
- Any relevant Lambda limits. For more information, see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md") in the _AWS Lambda Developer Guide_.
- Like PostgreSQL, Athena treats trailing spaces in PostgreSQL `CHAR`
  types as semantically insignificant for length and comparison purposes. Note
  that this applies only to `CHAR` but not to `VARCHAR`
  types. Athena ignores trailing spaces for the `CHAR` type, but treats them as
  significant for the `VARCHAR` type.
- When you use the [citext](https://www.postgresql.org/docs/current/citext.html "https://www.postgresql.org/docs/current/citext.html")
  case-insensitive character string data type, PostgreSQL uses a case insensitive
  data comparison that is different from Athena. This difference creates a data
  discrepancy during SQL `JOIN` operations. To workaround this issue,
  use the PostgreSQL connector passthrough query feature. For more information, see
  the [passthrough
  queries](#connectors-postgres-passthrough-queries "#connectors-postgres-passthrough-queries") section later in this document.

## Terms

The following terms relate to the PostgreSQL connector.

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

Use the parameters in this section to configure the PostgreSQL connector.

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

We recommend that you configure a PostgreSQL connector by using a Glue connections
object.

To do this, set the `glue_connection` environment variable of the
PostgreSQL connector Lambda to the name of the Glue connection to use.

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type POSTGRESQL
```

**Lambda environment properties**

glue_connection – Specifies the name of the Glue connection associated with the federated connector.

###### Note

- All connectors that use Glue connections must use AWS Secrets Manager to store credentials.
- The PostgreSQL connector created using Glue connections does not support the use of a multiplexing handler.
- The PostgreSQL connector created using Glue connections only supports `ConnectionSchemaVersion` 2.
  The parameter names and definitions listed below are for Athena data source connectors created without an associated Glue connection. Use the following parameters only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector or when the
  `glue_connection` environment property is not
  specified.

#### Connection string

Use a JDBC connection string in the following format to connect to a database
instance.

```
postgres://${`jdbc_connection_string`}
```

#### Using a

multiplexing handler

You can use a multiplexer to connect to multiple database instances with a single
Lambda function. Requests are routed by catalog name. Use the following classes in
Lambda.

| Handler           | Class                           |
| ----------------- | ------------------------------- |
| Composite handler | `PostGreSqlMuxCompositeHandler` |
| Metadata handler  | `PostGreSqlMuxMetadataHandler`  |
| Record handler    | `PostGreSqlMuxRecordHandler`    |

##### Multiplexing handler parameters

| Parameter                      | Description                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$`catalog`_connection_string` | Required. A database instance connection string. Prefix the<br>environment variable with the name of the catalog used in Athena. For example,<br>if the catalog registered with Athena is<br>`mypostgrescatalog`, then the environment<br>variable name is<br>`mypostgrescatalog_connection_string`. |
| `default`                      | Required. The default connection string. This string is used<br>when the catalog is<br>`lambda:${``AWS_LAMBDA_FUNCTION_NAME``}`.                                                                                                                                                                     |

The following example properties are for a PostGreSql MUX Lambda function
that supports two database instances: `postgres1` (the
default), and `postgres2`.

| Property                              | Value                                                                                  |
| ------------------------------------- | -------------------------------------------------------------------------------------- |
| `default`                             | `postgres://jdbc:postgresql://postgres1.host:5432/default?${Test/RDS/PostGres1}`       |
| `postgres_catalog1_connection_string` | `postgres://jdbc:postgresql://postgres1.host:5432/default?${Test/RDS/PostGres1}`       |
| `postgres_catalog2_connection_string` | `postgres://jdbc:postgresql://postgres2.host:5432/default?user=sample&password=sample` |

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
`${Test/RDS/PostGres1}`.

```
postgres://jdbc:postgresql://postgres1.host:5432/default?...&${Test/RDS/PostGres1}&...
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
postgres://jdbc:postgresql://postgres1.host:5432/default?...&user=sample2&password=sample2&...
```

Currently, the PostgreSQL connector recognizes the `user` and
`password` JDBC properties.

##### Enabling SSL

To support SSL in your PostgreSQL connection, append the following to your
connection string:

```
&sslmode=verify-ca&sslfactory=org.postgresql.ssl.DefaultJavaSSLFactory
```

###### Example

The following example connection string does not use SSL.

```
postgres://jdbc:postgresql://example-asdf-aurora-postgres-endpoint:5432/asdf?user=someuser&password=somepassword
```

To enable SSL, modify the string as follows.

```
postgres://jdbc:postgresql://example-asdf-aurora-postgres-endpoint:5432/asdf?user=someuser&password=somepassword&sslmode=verify-ca&sslfactory=org.postgresql.ssl.DefaultJavaSSLFactory
```

#### Using a

single connection handler

You can use the following single connection metadata and record handlers to
connect to a single PostgreSQL instance.

| Handler type      | Class                        |
| ----------------- | ---------------------------- |
| Composite handler | `PostGreSqlCompositeHandler` |
| Metadata handler  | `PostGreSqlMetadataHandler`  |
| Record handler    | `PostGreSqlRecordHandler`    |

##### Single connection handler parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `default` | Required. The default connection string. |

The single connection handlers support one database instance and must provide a
`default` connection string parameter. All other connection
strings are ignored.

The following example property is for a single PostgreSQL instance supported by a Lambda function.

| Property  | Value                                                                                     |
| --------- | ----------------------------------------------------------------------------------------- |
| `default` | `postgres://jdbc:postgresql://postgres1.host:5432/default?secret=${Test/RDS/PostgreSQL1}` |

#### Spill parameters

The Lambda SDK can spill data to Amazon S3. All database instances accessed by the same
Lambda function spill to the same location.

| Parameter                   | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `spill_bucket`              | Required. Spill bucket name.                                                                                                                                                                                                                                                                                                                                                                           |
| `spill_prefix`              | Required. Spill bucket key<br>prefix.                                                                                                                                                                                                                                                                                                                                                                  |
| `spill_put_request_headers` | (Optional) A JSON encoded map of request headers and values for<br>the Amazon S3 `putObject` request that is used for spilling<br>(for example, `{"x-amz-server-side-encryption" :<br>"AES256"}`). For other possible headers, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md")<br>in the _Amazon Simple Storage Service API Reference_. |

## Data type support

The following table shows the corresponding data types for JDBC, PostGreSQL, and
Arrow.

| JDBC       | PostGreSQL     | Arrow     |
| ---------- | -------------- | --------- |
| Boolean    | Boolean        | Bit       |
| Integer    | N/A            | Tiny      |
| Short      | smallint       | Smallint  |
| Integer    | integer        | Int       |
| Long       | bigint         | Bigint    |
| float      | float4         | Float4    |
| Double     | float8         | Float8    |
| Date       | date           | DateDay   |
| Timestamp  | timestamp      | DateMilli |
| String     | text           | Varchar   |
| Bytes      | bytes          | Varbinary |
| BigDecimal | numeric(p,s)   | Decimal   |
| ARRAY      | N/A (see note) | List      |

###### Note

The `ARRAY` type is supported for the PostgreSQL connector with the
following constraints: Multidimensional arrays
(``<data_type>`[][]`or nested
 arrays) are not supported. Columns with unsupported`ARRAY` data-types
 are converted to an array of string elements
 (`array<varchar>`).

## Partitions and

splits

Partitions are used to determine how to generate splits for the connector. Athena constructs a synthetic column of type `varchar` that represents the partitioning scheme for the table to help the connector generate splits. The connector does not modify the actual table definition.

## Performance

PostgreSQL supports native partitions. The Athena PostgreSQL connector can
retrieve data from these partitions in parallel. If you want to query very large
datasets with uniform partition distribution, native partitioning is highly
recommended.

The Athena PostgreSQL connector performs predicate pushdown to decrease the data scanned by the query. `LIMIT` clauses, simple predicates, and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time. However, selecting a subset of columns sometimes results in a longer query execution runtime.

### LIMIT

clauses

A `LIMIT N` statement reduces the data scanned by the query. With
`LIMIT N` pushdown, the connector returns only `N` rows to
Athena.

### Predicates

A predicate is an expression in the `WHERE` clause of a SQL query that
evaluates to a Boolean value and filters rows based on multiple conditions. The
Athena PostgreSQL connector can combine these expressions and push them directly to
PostgreSQL for enhanced functionality and to reduce the amount of data scanned.

The following Athena PostgreSQL connector operators support predicate
pushdown:

- Boolean: AND, OR, NOT
- Equality: EQUAL, NOT_EQUAL, LESS_THAN,
  LESS_THAN_OR_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_DISTINCT_FROM,
  NULL_IF, IS_NULL
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
    AND (col_e IN ('val1', 'val2', 'val3') OR col_f LIKE '%pattern%')
LIMIT 10;
```

## Passthrough

queries

The PostgreSQL connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md"). Passthrough
queries use a table function to push your full query down to the data source for
execution.

To use passthrough queries with PostgreSQL, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '`query string`'
        ))
```

The following example query pushes down a query to a data source in PostgreSQL. The query
selects all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer LIMIT 10'
        ))
```

## Additional

resources

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-postgresql/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-postgresql/pom.xml") file for the PostgreSQL connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-postgresql "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-postgresql") on GitHub.com.
