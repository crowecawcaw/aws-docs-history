# Amazon Athena Oracle connector

The Amazon Athena connector for Oracle enables Amazon Athena to run SQL queries on data stored in
Oracle running on-premises or on Amazon EC2 or Amazon RDS. You can also use the connector to query
data on [Oracle
exadata](https://www.oracle.com/engineered-systems/exadata/ "https://www.oracle.com/engineered-systems/exadata/").

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
- Only version 12.1.0.2 Oracle Databases are supported.
- If the Oracle connector does not use a Glue connection, the database, table,
  and column names will be converted to upper case by the connector.

If the Oracle connector uses a Glue connection, the database, table, and
column names will not default to upper case by the connector. To change this casing behavior,
change the Lambda by environment variable `casing_mode` to
`upper` or `lower` as needed.

An Oracle connector using Glue connection does not support the use of a Multiplexing handler.

- When you use the Oracle `NUMBER` without Precision and Scale
  defined, Athena treats this as `BIGINT`. To get the required decimal
  places in Athena, specify `default_scale=<`number of decimal
  places`>` in your Lambda environment variables.

## Terms

The following terms relate to the Oracle connector.

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

Use the parameters in this section to configure the Oracle connector.

We recommend that you configure a Oracle connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the Oracle connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type ORACLE
```

**Lambda environment properties**

- glue_connection – Specifies the name of the Glue connection associated with the federated connector.
- is_fips_enabled – (Optional) Set to true when FIPS mode is enabled. The default is false.
- **casing_mode** – (Optional) Specifies
  how to handle casing for schema and table names. The
  `casing_mode` parameter uses the following values to specify
  the behavior of casing:
  - **lower** – Lower case all
    given schema and table names. This is the default for connectors
    that have an associated glue connection.
  - **upper** – Upper case all
    given schema and table names. This is the default for connectors
    that do not have an associated glue connection.
  - **case_insensitive_search** –
    Perform case insensitive searches against schema and tables names in
    Oracle. Use this value if your query contains schema or table names
    that do not match the default casing for your connector.

###### Note

- All connectors that use Glue connections must use AWS Secrets Manager to store credentials.
- The Oracle connector created using Glue connections does not support the use of a multiplexing handler.
- The Oracle connector created using Glue connections only supports `ConnectionSchemaVersion` 2.

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created without an associated Glue connection. Use the following parameters only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector or when the
`glue_connection` environment property is not
specified.

**Lambda environment properties**

- default – The JDBC connection string to use to connect to the Oracle database instance. For example, `oracle://${jdbc_connection_string}`
- catalog_connection_string – Used by the Multiplexing handler (not supported when using a glue connection). A database instance connection string. Prefix the environment variable with the name of the catalog used in Athena. For example, if the catalog registered with Athena is myoraclecatalog, then the environment variable name is myoraclecatalog_connection_string.
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
- is_fips_enabled – (Optional) Set to true when FIPS mode is enabled. The default is false.
- **casing_mode** – (Optional) Specifies
  how to handle casing for schema and table names. The
  `casing_mode` parameter uses the following values to specify
  the behavior of casing:
  - **lower** – Lower case all
    given schema and table names. This is the default for connectors
    that have an associated glue connection.
  - **upper** – Upper case all
    given schema and table names. This is the default for connectors
    that do not have an associated glue connection.
  - **case_insensitive_search** –
    Perform case insensitive searches against schema and tables names in
    Oracle. Use this value if your query contains schema or table names
    that do not match the default casing for your connector.

#### Connection string

Use a JDBC connection string in the following format to connect to a database
instance.

```
oracle://${`jdbc_connection_string`}
```

###### Note

If your password contains special characters (for example,
`some.password`), enclose your password in double quotes when you
pass it to the connection string (for example, `"some.password"`).
Failure to do so can result in an **`Invalid Oracle URL
 specified`** error.

#### Using a single

connection handler

You can use the following single connection metadata and record handlers to
connect to a single Oracle instance.

| Handler type      | Class                    |
| ----------------- | ------------------------ |
| Composite handler | `OracleCompositeHandler` |
| Metadata handler  | `OracleMetadataHandler`  |
| Record handler    | `OracleRecordHandler`    |

##### Single

connection handler parameters

| Parameter       | Description                                                                   |
| --------------- | ----------------------------------------------------------------------------- |
| `default`       | Required. The default connection string.                                      |
| `IsFIPSEnabled` | Optional. Set to `true` when FIPS mode is enabled.<br>The default is `false`. |

The single connection handlers support one database instance and must provide
a `default` connection string parameter. All other connection strings
are ignored.

The connector supports SSL based connections to Amazon RDS instances. Support is
limited to the Transport Layer Security (TLS) protocol and to authentication of
the server by the client. Mutual authentication it is not supported in Amazon RDS.
The second row in the table below shows the syntax for using SSL.

The following example property is for a single Oracle instance supported by a Lambda function.

| Property  | Value                                                                                                                                                                    |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `default` | `oracle://jdbc:oracle:thin:${Test/RDS/Oracle}@//hostname:port/servicename`                                                                                               |
|           | `oracle://jdbc:oracle:thin:${Test/RDS/Oracle}@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCPS)<br>(HOST=<HOST_NAME>)(PORT=))(CONNECT_DATA=(SID=))(SECURITY=(SSL_SERVER_CERT_DN=)))` |

#### Providing

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

###### Note

If your password contains special characters (for example,
`some.password`), enclose your password in double quotes when
you store it in Secrets Manager (for example, `"some.password"`). Failure
to do so can result in an **`Invalid Oracle URL
 specified`** error.

###### Example connection string with secret name

The following string has the secret name
`${Test/RDS/Oracle}`.

```
oracle://jdbc:oracle:thin:${Test/RDS/Oracle}@//hostname:port/servicename
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
oracle://jdbc:oracle:thin:username/password@//hostname:port/servicename
```

Currently, the Oracle connector recognizes the `UID` and
`PWD` JDBC properties.

#### Using a

multiplexing handler

You can use a multiplexer to connect to multiple database instances with a single
Lambda function. Requests are routed by catalog name. Use the following classes in
Lambda.

| Handler           | Class                       |
| ----------------- | --------------------------- |
| Composite handler | `OracleMuxCompositeHandler` |
| Metadata handler  | `OracleMuxMetadataHandler`  |
| Record handler    | `OracleMuxRecordHandler`    |

##### Multiplexing

handler parameters

| Parameter                      | Description                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `$`catalog`_connection_string` | Required. A database instance connection string. Prefix the<br>environment variable with the name of the catalog used in Athena. For example,<br>if the catalog registered with Athena is<br>`myoraclecatalog`, then the environment<br>variable name is<br>`myoraclecatalog_connection_string`. |
| `default`                      | Required. The default connection string. This string is used<br>when the catalog is<br>`lambda:${``AWS_LAMBDA_FUNCTION_NAME``}`.                                                                                                                                                                 |

The following example properties are for a Oracle MUX Lambda function
that supports two database instances: `oracle1` (the
default), and `oracle2`.

| Property                            | Value                                                                               |
| ----------------------------------- | ----------------------------------------------------------------------------------- |
| `default`                           | `oracle://jdbc:oracle:thin:${Test/RDS/Oracle1}@//oracle1.hostname:port/servicename` |
| `oracle_catalog1_connection_string` | `oracle://jdbc:oracle:thin:${Test/RDS/Oracle1}@//oracle1.hostname:port/servicename` |
| `oracle_catalog2_connection_string` | `oracle://jdbc:oracle:thin:${Test/RDS/Oracle2}@//oracle2.hostname:port/servicename` |

## Data type support

The following table shows the corresponding data types for JDBC, Oracle, and
Arrow.

| JDBC       | Oracle         | Arrow     |
| ---------- | -------------- | --------- |
| Boolean    | boolean        | Bit       |
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

## Partitions and splits

Partitions are used to determine how to generate splits for the connector. Athena constructs a synthetic column of type `varchar` that represents the partitioning scheme for the table to help the connector generate splits. The connector does not modify the actual table definition.

## Performance

Oracle supports native partitions. The Athena Oracle connector can
retrieve data from these partitions in parallel. If you want to query very large
datasets with uniform partition distribution, native partitioning is highly
recommended. Selecting a subset of columns significantly speeds up query runtime and reduces data scanned. The Oracle connector is resilient to throttling due to concurrency.
However, query runtimes tend to be long.

The Athena Oracle connector performs predicate pushdown to decrease the data scanned by the query. Simple predicates and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time.

### Predicates

A predicate is an expression in the `WHERE` clause of a SQL query that
evaluates to a Boolean value and filters rows based on multiple conditions. The
Athena Oracle connector can combine these expressions and push them directly to
Oracle for enhanced functionality and to reduce the amount of data scanned.

The following Athena Oracle connector operators support predicate
pushdown:

- Boolean: AND, OR, NOT
- Equality: EQUAL, NOT_EQUAL, LESS_THAN,
  LESS_THAN_OR_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_NULL
- Arithmetic: ADD, SUBTRACT, MULTIPLY,
  DIVIDE, NEGATE
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

The Oracle connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md"). Passthrough
queries use a table function to push your full query down to the data source for
execution.

To use passthrough queries with Oracle, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '`query string`'
        ))
```

The following example query pushes down a query to a data source in Oracle. The query
selects all columns in the `customer` table.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer'
        ))
```

## License information

By using this connector, you acknowledge the inclusion of third party components, a list
of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-oracle/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-oracle/pom.xml") file for this connector, and agree to the terms in the respective third
party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-oracle/LICENSE.txt "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-oracle/LICENSE.txt") file on GitHub.com.

## Additional resources

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-oracle/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-oracle/pom.xml") file for the Oracle connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-oracle "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-oracle") on GitHub.com.
