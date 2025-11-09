# Amazon Athena Teradata connector

The Amazon Athena connector for Teradata enables Athena to run SQL queries on data stored in
your Teradata databases.

This connector does not use Glue Connections to centralize configuration properties in Glue. Connection configuration is done through Lambda.

## Prerequisites

- Deploy the connector to your AWS account using the Athena console or the AWS Serverless Application Repository. For more information, see [Create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md") or [Use the AWS Serverless Application Repository to deploy a data
  source connector](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md").

## Limitations

- Write DDL operations are not supported.
- In a multiplexer setup, the spill bucket and prefix are shared across all
  database instances.
- Any relevant Lambda limits. For more information, see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md") in the _AWS Lambda Developer Guide_.

## Terms

The following terms relate to the Teradata connector.

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

Use the parameters in this section to configure the Teradata connector.

We recommend that you configure a Teradata connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the Teradata connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type TERADATA
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
- The Teradata connector created using Glue connections does not support the use of a multiplexing handler.
- The Teradata connector created using Glue connections only supports `ConnectionSchemaVersion` 2.

#### Connection string

Use a JDBC connection string in the following format to connect to a database
instance.

```
teradata://${`jdbc_connection_string`}
```

#### Using a

multiplexing handler

You can use a multiplexer to connect to multiple database instances with a single
Lambda function. Requests are routed by catalog name. Use the following classes in
Lambda.

| Handler           | Class                         |
| ----------------- | ----------------------------- |
| Composite handler | `TeradataMuxCompositeHandler` |
| Metadata handler  | `TeradataMuxMetadataHandler`  |
| Record handler    | `TeradataMuxRecordHandler`    |

##### Multiplexing handler parameters

| Parameter                      | Description                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$`catalog`_connection_string` | Required. A database instance connection string. Prefix the<br>environment variable with the name of the catalog used in Athena. For example,<br>if the catalog registered with Athena is<br>`myteradatacatalog`, then the environment<br>variable name is<br>`myteradatacatalog_connection_string`. |
| `default`                      | Required. The default connection string. This string is used<br>when the catalog is<br>`lambda:${``AWS_LAMBDA_FUNCTION_NAME``}`.                                                                                                                                                                     |

The following example properties are for a Teradata MUX Lambda function
that supports two database instances: `teradata1` (the
default), and `teradata2`.

| Property                              | Value                                                                                                           |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `default`                             | `teradata://jdbc:teradata://teradata2.host/TMODE=ANSI,CHARSET=UTF8,DATABASE=TEST,user=sample2&password=sample2` |
| `teradata_catalog1_connection_string` | `teradata://jdbc:teradata://teradata1.host/TMODE=ANSI,CHARSET=UTF8,DATABASE=TEST,${Test/RDS/Teradata1}`         |
| `teradata_catalog2_connection_string` | `teradata://jdbc:teradata://teradata2.host/TMODE=ANSI,CHARSET=UTF8,DATABASE=TEST,user=sample2&password=sample2` |

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
`${Test/RDS/Teradata1}`.

```
teradata://jdbc:teradata1.host/TMODE=ANSI,CHARSET=UTF8,DATABASE=TEST,${Test/RDS/Teradata1}&...
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
teradata://jdbc:teradata://teradata1.host/TMODE=ANSI,CHARSET=UTF8,DATABASE=TEST,...&user=sample2&password=sample2&...
```

Currently, Teradata recognizes the `user` and `password`
JDBC properties. It also accepts the user name and password in the format
`username``/``password`
without the keys `user` or `password`.

#### Using a

single connection handler

You can use the following single connection metadata and record handlers to
connect to a single Teradata instance.

| Handler type      | Class                      |
| ----------------- | -------------------------- |
| Composite handler | `TeradataCompositeHandler` |
| Metadata handler  | `TeradataMetadataHandler`  |
| Record handler    | `TeradataRecordHandler`    |

##### Single connection handler parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `default` | Required. The default connection string. |

The single connection handlers support one database instance and must provide a
`default` connection string parameter. All other connection
strings are ignored.

The following example property is for a single Teradata instance supported by a Lambda function.

| Property  | Value                                                                                                       |
| --------- | ----------------------------------------------------------------------------------------------------------- |
| `default` | `teradata://jdbc:teradata://teradata1.host/TMODE=ANSI,CHARSET=UTF8,DATABASE=TEST,secret=Test/RDS/Teradata1` |

#### Spill parameters

The Lambda SDK can spill data to Amazon S3. All database instances accessed by the same
Lambda function spill to the same location.

| Parameter                   | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `spill_bucket`              | Required. Spill bucket name.                                                                                                                                                                                                                                                                                                                                                                           |
| `spill_prefix`              | Required. Spill bucket key<br>prefix.                                                                                                                                                                                                                                                                                                                                                                  |
| `spill_put_request_headers` | (Optional) A JSON encoded map of request headers and values for<br>the Amazon S3 `putObject` request that is used for spilling<br>(for example, `{"x-amz-server-side-encryption" :<br>"AES256"}`). For other possible headers, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md")<br>in the _Amazon Simple Storage Service API Reference_. |

## Data type support

The following table shows the corresponding data types for JDBC and Apache
Arrow.

| JDBC       | Arrow     |
| ---------- | --------- |
| Boolean    | Bit       |
| Integer    | Tiny      |
| Short      | Smallint  |
| Integer    | Int       |
| Long       | Bigint    |
| float      | Float4    |
| Double     | Float8    |
| Date       | DateDay   |
| Timestamp  | DateMilli |
| String     | Varchar   |
| Bytes      | Varbinary |
| BigDecimal | Decimal   |
| ARRAY      | List      |

## Partitions and

splits

A partition is represented by a single partition column of type `Integer`.
The column contains partition names of the partitions defined on a Teradata table. For a
table that does not have partition names, \* is returned, which is equivalent to a single
partition. A partition is equivalent to a split.

| Name      | Type    | Description                  |
| --------- | ------- | ---------------------------- |
| partition | Integer | Named partition in Teradata. |

## Performance

Teradata supports native partitions. The Athena Teradata connector can
retrieve data from these partitions in parallel. If you want to query very large
datasets with uniform partition distribution, native partitioning is highly
recommended. Selecting a subset of columns significantly slows down query runtime. The connector shows
some throttling due to concurrency.

The Athena Teradata connector performs predicate pushdown to decrease the data scanned by the query. Simple predicates and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time.

### Predicates

A predicate is an expression in the `WHERE` clause of a SQL query that
evaluates to a Boolean value and filters rows based on multiple conditions. The
Athena Teradata connector can combine these expressions and push them directly to
Teradata for enhanced functionality and to reduce the amount of data scanned.

The following Athena Teradata connector operators support predicate
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

The Teradata connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md"). Passthrough
queries use a table function to push your full query down to the data source for
execution.

To use passthrough queries with Teradata, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '`query string`'
        ))
```

The following example query pushes down a query to a data source in Teradata. The query
selects all columns in the `customer` table.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer'
        ))
```

## License information

By using this connector, you acknowledge the inclusion of third party components, a list
of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-teradata/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-teradata/pom.xml") file for this connector, and agree to the terms in the respective third
party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-teradata/LICENSE.txt "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-teradata/LICENSE.txt") file on GitHub.com.

## Additional resources

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-teradata/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-teradata/pom.xml") file for the Teradata connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-teradata "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-teradata") on GitHub.com.
