# Amazon Athena Cloudera Hive connector

The Amazon Athena connector for Cloudera Hive enables Athena to run SQL queries on the [Cloudera Hive](https://www.cloudera.com/products/open-source/apache-hadoop/apache-hive.html "https://www.cloudera.com/products/open-source/apache-hadoop/apache-hive.html") Hadoop distribution. The connector transforms your Athena SQL
queries to their equivalent HiveQL syntax.

This connector does not use Glue Connections to centralize configuration properties in Glue. Connection configuration is done through Lambda.

## Prerequisites

- Deploy the connector to your AWS account using the Athena console or the AWS Serverless Application Repository. For more information, see [Create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md") or [Use the AWS Serverless Application Repository to deploy a data
  source connector](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md").
- Set up a VPC and a security group before you use this connector. For more
  information, see [Create a VPC for a data source connector or
  AWS Glue connection](athena-connectors-vpc-creation.md "athena-connectors-vpc-creation.md").

## Limitations

- Write DDL operations are not supported.
- In a multiplexer setup, the spill bucket and prefix are shared across all
  database instances.
- Any relevant Lambda limits. For more information, see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md") in the _AWS Lambda Developer Guide_.

## Terms

The following terms relate to the Cloudera Hive connector.

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

Use the parameters in this section to configure the Cloudera Hive connector.

We recommend that you configure a Cloudera Hive connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the Cloudera Hive connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type CLOUDERAHIVE
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
- The Cloudera Hive connector created using Glue connections does not support the use of a multiplexing handler.
- The Cloudera Hive connector created using Glue connections only supports `ConnectionSchemaVersion` 2.

#### Connection

string

Use a JDBC connection string in the following format to connect to a database
instance.

```
hive://${`jdbc_connection_string`}
```

#### Using a multiplexing

handler

You can use a multiplexer to connect to multiple database instances with a single
Lambda function. Requests are routed by catalog name. Use the following classes in
Lambda.

| Handler           | Class                     |
| ----------------- | ------------------------- |
| Composite handler | `HiveMuxCompositeHandler` |
| Metadata handler  | `HiveMuxMetadataHandler`  |
| Record handler    | `HiveMuxRecordHandler`    |

##### Multiplexing handler parameters

| Parameter                      | Description                                                                                                                                                                                                                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$`catalog`_connection_string` | Required. A database instance connection string. Prefix the<br>environment variable with the name of the catalog used in Athena. For example,<br>if the catalog registered with Athena is<br>`myhivecatalog`, then the environment<br>variable name is<br>`myhivecatalog_connection_string`. |
| `default`                      | Required. The default connection string. This string is used<br>when the catalog is<br>`lambda:${``AWS_LAMBDA_FUNCTION_NAME``}`.                                                                                                                                                             |

The following example properties are for a Hive MUX Lambda function
that supports two database instances: `hive1` (the
default), and `hive2`.

| Property                           | Value                                                           |
| ---------------------------------- | --------------------------------------------------------------- |
| `default`                          | `hive://jdbc:hive2://hive1:10000/default;${Test/RDS/hive1}`     |
| `hive2_catalog1_connection_string` | `hive://jdbc:hive2://hive1:10000/default;${Test/RDS/hive1}`     |
| `hive2_catalog2_connection_string` | `hive://jdbc:hive2://hive2:10000/default;UID=sample&PWD=sample` |

##### Providing

credentials

To provide a user name and password for your database in your JDBC connection
string, the Cloudera Hive connector requires a secret from AWS Secrets Manager. To use the Athena
Federated Query feature with AWS Secrets Manager, the VPC connected to your Lambda
function should have [internet access](https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/ "https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/") or a [VPC
endpoint](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md") to connect to Secrets Manager.

Put the name of a secret in AWS Secrets Manager in your JDBC connection
string. The connector replaces the secret name with the
`username` and `password` values from
Secrets Manager.

###### Example connection string with secret name

The following string has the secret name
`${Test/RDS/hive1}`.

```
hive://jdbc:hive2://hive1:10000/default;...&${Test/RDS/hive1}&...
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
hive://jdbc:hive2://hive1:10000/default;...&UID=sample2&PWD=sample2&...
```

Currently, the Cloudera Hive connector recognizes the `UID` and
`PWD` JDBC properties.

#### Using a single

connection handler

You can use the following single connection metadata and record handlers to
connect to a single Cloudera Hive instance.

| Handler type      | Class                  |
| ----------------- | ---------------------- |
| Composite handler | `HiveCompositeHandler` |
| Metadata handler  | `HiveMetadataHandler`  |
| Record handler    | `HiveRecordHandler`    |

##### Single connection handler parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `default` | Required. The default connection string. |

The single connection handlers support one database instance and must provide a
`default` connection string parameter. All other connection
strings are ignored.

The following example property is for a single Cloudera Hive instance supported by a Lambda function.

| Property | Value                                                              |
| -------- | ------------------------------------------------------------------ |
| default  | `hive://jdbc:hive2://hive1:10000/default;secret=${Test/RDS/hive1}` |

#### Spill parameters

The Lambda SDK can spill data to Amazon S3. All database instances accessed by the same
Lambda function spill to the same location.

| Parameter                   | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `spill_bucket`              | Required. Spill bucket name.                                                                                                                                                                                                                                                                                                                                                                           |
| `spill_prefix`              | Required. Spill bucket key<br>prefix.                                                                                                                                                                                                                                                                                                                                                                  |
| `spill_put_request_headers` | (Optional) A JSON encoded map of request headers and values for<br>the Amazon S3 `putObject` request that is used for spilling<br>(for example, `{"x-amz-server-side-encryption" :<br>"AES256"}`). For other possible headers, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md")<br>in the _Amazon Simple Storage Service API Reference_. |

## Data type support

The following table shows the corresponding data types for JDBC, Cloudera Hive, and
Arrow.

| JDBC       | Cloudera Hive  | Arrow     |
| ---------- | -------------- | --------- |
| Boolean    | Boolean        | Bit       |
| Integer    | TINYINT        | Tiny      |
| Short      | SMALLINT       | Smallint  |
| Integer    | INT            | Int       |
| Long       | BIGINT         | Bigint    |
| float      | float4         | Float4    |
| Double     | float8         | Float8    |
| Date       | date           | DateDay   |
| Timestamp  | timestamp      | DateMilli |
| String     | VARCHAR        | Varchar   |
| Bytes      | bytes          | Varbinary |
| BigDecimal | Decimal        | Decimal   |
| ARRAY      | N/A (see note) | List      |

###### Note

Currently, Cloudera Hive does not support the aggregate types `ARRAY`,
`MAP`, `STRUCT`, or `UNIONTYPE`. Columns of
aggregate types are treated as `VARCHAR` columns in SQL.

## Partitions and

splits

Partitions are used to determine how to generate splits for the connector. Athena constructs a synthetic column of type `varchar` that represents the partitioning scheme for the table to help the connector generate splits. The connector does not modify the actual table definition.

## Performance

Cloudera Hive supports static partitions. The Athena Cloudera Hive connector can
retrieve data from these partitions in parallel. If you want to query very large
datasets with uniform partition distribution, static partitioning is highly
recommended. The Cloudera Hive connector is resilient to throttling due to concurrency.

The Athena Cloudera Hive connector performs predicate pushdown to decrease the data scanned by the query. `LIMIT` clauses, simple predicates, and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time.

### LIMIT

clauses

A `LIMIT N` statement reduces the data scanned by the query. With
`LIMIT N` pushdown, the connector returns only `N` rows to
Athena.

### Predicates

A predicate is an expression in the `WHERE` clause of a SQL query that
evaluates to a Boolean value and filters rows based on multiple conditions. The
Athena Cloudera Hive connector can combine these expressions and push them directly to
Cloudera Hive for enhanced functionality and to reduce the amount of data scanned.

The following Athena Cloudera Hive connector operators support predicate
pushdown:

- Boolean: AND, OR, NOT
- Equality: EQUAL, NOT_EQUAL, LESS_THAN,
  LESS_THAN_OR_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_NULL
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

The Cloudera Hive connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md"). Passthrough
queries use a table function to push your full query down to the data source for
execution.

To use passthrough queries with Cloudera Hive, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '`query string`'
        ))
```

The following example query pushes down a query to a data source in Cloudera Hive. The query
selects all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer LIMIT 10'
        ))
```

## License information

By using this connector, you acknowledge the inclusion of third party components, a list
of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-cloudera-hive/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-cloudera-hive/pom.xml") file for this connector, and agree to the terms in the respective third
party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-cloudera-hive/LICENSE.txt "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-cloudera-hive/LICENSE.txt") file on GitHub.com.

## Additional resources

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-cloudera-hive/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-cloudera-hive/pom.xml") file for the Cloudera Hive connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-cloudera-hive "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-cloudera-hive") on GitHub.com.
