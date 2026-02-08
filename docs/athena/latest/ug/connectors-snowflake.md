# Amazon Athena Snowflake connector

The Amazon Athena connector for [Snowflake](https://www.snowflake.com/ "https://www.snowflake.com/")
enables Amazon Athena to run SQL queries on data stored in your Snowflake SQL database or RDS
instances using JDBC.

This connector can be registered with Glue Data Catalog as a federated catalog.
It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

## Prerequisites

Deploy the connector to your AWS account using the Athena console or the `CreateDataCatalog` API operation. For more information, see [Create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md").

## Limitations

- Write DDL operations are not supported.
- In a multiplexer setup, the spill bucket and prefix are shared across all
  database instances.
- Any relevant Lambda limits. For more information, see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md") in the _AWS Lambda Developer Guide_.
- Only legacy connections support multiplexer setup.
- Currently, Snowflake views with single split are supported.
- In Snowflake, object names are case-sensitive. Athena accepts mixed case in DDL and DML queries, but by default
  [lower cases](tables-databases-columns-names.md#table-names-and-table-column-names-in-ate-must-be-lowercase "tables-databases-columns-names.md#table-names-and-table-column-names-in-ate-must-be-lowercase")
  the object names when it executes the query. The Snowflake connector supports only
  lower case when Glue Catalog/Lake Formation are used. When the Athena Catalog is used, customers can
  control the casing behavior using the `casing_mode` Lambda environment variable whose possible values
  are listed in the [Parameters](#connectors-snowflake-parameters "#connectors-snowflake-parameters")
  section (for example, `key=casing_mode, value = CASE_INSENSITIVE_SEARCH`).

## Terms

The following terms relate to the Snowflake connector.

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

Use the parameters in this section to configure the Snowflake connector.

We recommend that you configure a Snowflake connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the Snowflake connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type SNOWFLAKE
```

**Lambda environment properties**

- glue_connection – Specifies the name of the Glue connection associated with the federated connector.
- **casing_mode** – (Optional) Specifies
  how to handle casing for schema and table names. The
  `casing_mode` parameter uses the following values to specify
  the behavior of casing:
  - **NONE** – Do not change case
    of the given schema and table names (run the query as is against Snowflake).
    This is the default value when **casing_mode**
    is not specified.
  - **UPPER** –
    Upper case all given schema and table names in the query before running it against
    Snowflake.
  - **LOWER** –
    Lower case all given schema and table names in the query before running it against
    Snowflake.
  - **CASE_INSENSITIVE_SEARCH** –
    Perform case insensitive searches against schema and tables names in Snowflake. For
    example, you can use this mode when you have a query like `SELECT * FROM EMPLOYEE`
    and Snowflake contains a table called `Employee`. However, in the presence
    of name collisions, such as having a table called `EMPLOYEE` and another
    table called `Employee` in Snowflake, the query will fail.

###### Note

- The Snowflake connector created using Glue connections does not support the use of a multiplexing handler.
- The Snowflake connector created using Glue connections only supports `ConnectionSchemaVersion` 2.
  **Storing credentials**

All connectors that use Glue connections must use AWS Secrets Manager to store
credentials. For more information, see [Authenticate with Snowflake](connectors-snowflake-authentication.md "connectors-snowflake-authentication.md").

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created without an associated Glue connection. Use the following parameters only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector or when the
`glue_connection` environment property is not
specified.

**Lambda environment properties**

- default – The JDBC connection string to use to connect to the Snowflake database instance. For example, `snowflake://${jdbc_connection_string}`
- catalog_connection_string – Used by the Multiplexing handler (not supported when using a glue connection). A database instance connection string. Prefix the environment variable with the name of the catalog used in Athena. For example, if the catalog registered with Athena is mysnowflakecatalog, then the environment variable name is mysnowflakecatalog_connection_string.
- **casing_mode** – (Optional) Specifies
  how to handle casing for schema and table names. The
  `casing_mode` parameter uses the following values to specify
  the behavior of casing:
  - **NONE** – Do not change case
    of the given schema and table names (run the query as is against Snowflake).
    This is the default value when **casing_mode**
    is not specified.
  - **UPPER** –
    Upper case all given schema and table names in the query before running it against
    Snowflake.
  - **LOWER** –
    Lower case all given schema and table names in the query before running it against
    Snowflake.
  - **CASE_INSENSITIVE_SEARCH** –
    Perform case insensitive searches against schema and tables names in Snowflake. For
    example, you can use this mode when you have a query like `SELECT * FROM EMPLOYEE`
    and Snowflake contains a table called `Employee`. However, in the presence
    of name collisions, such as having a table called `EMPLOYEE` and another
    table called `Employee` in Snowflake, the query will fail.

- spill_bucket – Specifies the Amazon S3 bucket
  for data that exceeds Lambda function limits.
- spill_prefix – (Optional) Defaults to a
  subfolder in the specified `spill_bucket` called
  `athena-federation-spill`. We recommend that you
  configure an Amazon S3 [storage
  lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") on this location to delete spills older than a
  predetermined number of days or hours.
- spill_put_request_headers – (Optional) A
  JSON encoded map of request headers and values for the Amazon S3
  `putObject` request that is used for spilling (for example,
  `{"x-amz-server-side-encryption" : "AES256"}`). For other
  possible headers, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") in the
  _Amazon Simple Storage Service API Reference_.
- kms_key_id – (Optional) By default, any
  data that is spilled to Amazon S3 is encrypted using the AES-GCM authenticated
  encryption mode and a randomly generated key. To have your Lambda function use
  stronger encryption keys generated by KMS like
  `a7e63k4b-8loc-40db-a2a1-4d0en2cd8331`, you can specify a KMS key
  ID.
- disable_spill_encryption – (Optional)
  When set to `True`, disables spill encryption. Defaults to
  `False` so that data that is spilled to S3 is encrypted using
  AES-GCM – either using a randomly generated key or KMS to generate keys.
  Disabling spill encryption can improve performance, especially if your spill
  location uses [server-side
  encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md").

#### Connection string

Use a JDBC connection string in the following format to connect to a database
instance.

```
snowflake://${`jdbc_connection_string`}
```

#### Using a

multiplexing handler

You can use a multiplexer to connect to multiple database instances with a single
Lambda function. Requests are routed by catalog name. Use the following classes in
Lambda.

| Handler           | Class                          |
| ----------------- | ------------------------------ |
| Composite handler | `SnowflakeMuxCompositeHandler` |
| Metadata handler  | `SnowflakeMuxMetadataHandler`  |
| Record handler    | `SnowflakeMuxRecordHandler`    |

##### Multiplexing handler parameters

| Parameter                      | Description                                                                                                                                                                                                                                                                                            |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `$`catalog`_connection_string` | Required. A database instance connection string. Prefix the<br>environment variable with the name of the catalog used in Athena. For example,<br>if the catalog registered with Athena is<br>`mysnowflakecatalog`, then the environment<br>variable name is<br>`mysnowflakecatalog_connection_string`. |
| `default`                      | Required. The default connection string. This string is used<br>when the catalog is<br>`lambda:${``AWS_LAMBDA_FUNCTION_NAME``}`.                                                                                                                                                                       |

The following example properties are for a Snowflake MUX Lambda function
that supports two database instances: `snowflake1` (the
default), and `snowflake2`.

| Property                               | Value                                                                                                                            |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `default`                              | `snowflake://jdbc:snowflake://snowflake1.host:port/?warehouse=warehousename&db=db1&schema=schema1&${Test/RDS/Snowflake1}`        |
| `snowflake_catalog1_connection_string` | `snowflake://jdbc:snowflake://snowflake1.host:port/?warehouse=warehousename&db=db1&schema=schema1${Test/RDS/Snowflake1}`         |
| `snowflake_catalog2_connection_string` | `snowflake://jdbc:snowflake://snowflake2.host:port/?warehouse=warehousename&db=db1&schema=schema1&user=sample2&password=sample2` |

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
`${Test/RDS/Snowflake1}`.

```
snowflake://jdbc:snowflake://snowflake1.host:port/?warehouse=warehousename&db=db1&schema=schema1${Test/RDS/Snowflake1}&...
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
snowflake://jdbc:snowflake://snowflake1.host:port/warehouse=warehousename&db=db1&schema=schema1&user=sample2&password=sample2&...
```

Currently, Snowflake recognizes the `user` and `password`
JDBC properties. It also accepts the user name and password in the format
`username``/``password`
without the keys `user` or `password`.

#### Using a

single connection handler

You can use the following single connection metadata and record handlers to
connect to a single Snowflake instance.

| Handler type      | Class                       |
| ----------------- | --------------------------- |
| Composite handler | `SnowflakeCompositeHandler` |
| Metadata handler  | `SnowflakeMetadataHandler`  |
| Record handler    | `SnowflakeRecordHandler`    |

##### Single connection handler parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `default` | Required. The default connection string. |

The single connection handlers support one database instance and must provide a
`default` connection string parameter. All other connection
strings are ignored.

The following example property is for a single Snowflake instance supported by a Lambda function.

| Property  | Value                                                                           |
| --------- | ------------------------------------------------------------------------------- |
| `default` | `snowflake://jdbc:snowflake://snowflake1.host:port/?secret=Test/RDS/Snowflake1` |

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

## Data type

conversions

In addition to the JDBC to Arrow conversions, the connector performs certain other
conversions to make the Snowflake source and Athena data types compatible. These
conversions help ensure that queries get executed successfully. The following table
shows these conversions.

| Source data type (Snowflake) | Converted data type (Athena) |
| ---------------------------- | ---------------------------- |
| TIMESTAMP                    | TIMESTAMPMILLI               |
| DATE                         | TIMESTAMPMILLI               |
| INTEGER                      | INT                          |
| DECIMAL                      | BIGINT                       |
| TIMESTAMP_NTZ                | TIMESTAMPMILLI               |

All other unsupported data types are converted to `VARCHAR`.

## Partitions and

splits

Partitions are used to determine how to generate splits for the connector. Athena constructs a synthetic column of type `varchar` that represents the partitioning scheme for the table to help the connector generate splits. The connector does not modify the actual table definition.

To create this synthetic column and the partitions, Athena requires a primary key to be
defined. However, because Snowflake does not enforce primary key constraints, you must
enforce uniqueness yourself. Failure to do so causes Athena to default to a single
split.

## Performance

For optimal performance, use filters in queries whenever possible. In addition, we
highly recommend native partitioning to retrieve huge datasets that have uniform
partition distribution. Selecting a subset of columns significantly speeds up query runtime and reduces data scanned. The Snowflake connector is resilient to throttling due to concurrency.

The Athena Snowflake connector performs predicate pushdown to decrease the data scanned by the query. `LIMIT` clauses, simple predicates, and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time.

### LIMIT

clauses

A `LIMIT N` statement reduces the data scanned by the query. With
`LIMIT N` pushdown, the connector returns only `N` rows to
Athena.

### Predicates

A predicate is an expression in the `WHERE` clause of a SQL query that
evaluates to a Boolean value and filters rows based on multiple conditions. The
Athena Snowflake connector can combine these expressions and push them directly to
Snowflake for enhanced functionality and to reduce the amount of data scanned.

The following Athena Snowflake connector operators support predicate
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

The Snowflake connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md"). Passthrough
queries use a table function to push your full query down to the data source for
execution.

To use passthrough queries with Snowflake, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '`query string`'
        ))
```

The following example query pushes down a query to a data source in Snowflake. The query
selects all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer LIMIT 10'
        ))
```

## License information

By using this connector, you acknowledge the inclusion of third party components, a list
of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-snowflake/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-snowflake/pom.xml") file for this connector, and agree to the terms in the respective third
party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-snowflake/LICENSE.txt "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-snowflake/LICENSE.txt") file on GitHub.com.

## Additional resources

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-snowflake/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-snowflake/pom.xml") file for the Snowflake connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-snowflake "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-snowflake") on GitHub.com.
