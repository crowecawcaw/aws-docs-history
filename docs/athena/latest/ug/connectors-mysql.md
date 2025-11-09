# Amazon Athena MySQL connector

The Amazon Athena Lambda MySQL connector enables Amazon Athena to access MySQL databases.

This connector can be registered with Glue Data Catalog as a federated catalog.
It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

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
- Because Athena converts queries to lower case, MySQL table names must be in
  lower case. For example, Athena queries against a table named
  `myTable` will fail.
- If you migrate your MySQL connections to Glue Catalog and Lake Formation, only the lowercase table and
  column names will be recognized.

## Terms

The following terms relate to the MySQL connector.

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

Use the parameters in this section to configure the MySQL connector.

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

We recommend that you configure a MySQL connector by using a Glue connections
object.

To do this, set the `glue_connection` environment variable of the
MySQL connector Lambda to the name of the Glue connection to use.

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type MYSQL
```

**Lambda environment properties**

glue_connection – Specifies the name of the Glue connection associated with the federated connector.

###### Note

- All connectors that use Glue connections must use AWS Secrets Manager to store credentials.
- The MySQL connector created using Glue connections does not support the use of a multiplexing handler.
- The MySQL connector created using Glue connections only supports `ConnectionSchemaVersion` 2.
  The parameter names and definitions listed below are for Athena data source connectors created without an associated Glue connection. Use the following parameters only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector or when the
  `glue_connection` environment property is not
  specified.

#### Connection string

Use a JDBC connection string in the following format to connect to a database
instance.

```
mysql://${`jdbc_connection_string`}
```

###### Note

If you receive the error **`java.sql.SQLException: Zero date value
 prohibited`** when doing a `SELECT` query on a MySQL
table, add the following parameter to your connection string:

```
zeroDateTimeBehavior=convertToNull
```

For more information, see [Error 'Zero date value prohibited' while trying to select from MySQL
table](https://github.com/awslabs/aws-athena-query-federation/issues/760 "https://github.com/awslabs/aws-athena-query-federation/issues/760") on GitHub.com.

#### Using a multiplexing

handler

You can use a multiplexer to connect to multiple database instances with a single
Lambda function. Requests are routed by catalog name. Use the following classes in
Lambda.

| Handler           | Class                      |
| ----------------- | -------------------------- |
| Composite handler | `MySqlMuxCompositeHandler` |
| Metadata handler  | `MySqlMuxMetadataHandler`  |
| Record handler    | `MySqlMuxRecordHandler`    |

##### Multiplexing

handler parameters

| Parameter                      | Description                                                                                                                                                                                                                                                                                    |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$`catalog`_connection_string` | Required. A database instance connection string. Prefix the<br>environment variable with the name of the catalog used in Athena. For example,<br>if the catalog registered with Athena is<br>`mymysqlcatalog`, then the environment<br>variable name is<br>`mymysqlcatalog_connection_string`. |
| `default`                      | Required. The default connection string. This string is used<br>when the catalog is<br>`lambda:${``AWS_LAMBDA_FUNCTION_NAME``}`.                                                                                                                                                               |

The following example properties are for a MySql MUX Lambda function
that supports two database instances: `mysql1` (the
default), and `mysql2`.

| Property                           | Value                                                                         |
| ---------------------------------- | ----------------------------------------------------------------------------- |
| `default`                          | `mysql://jdbc:mysql://mysql2.host:3333/default?`user=sample2&password=sample2 |
| `mysql_catalog1_connection_string` | `mysql://jdbc:mysql://mysql1.host:3306/default?${Test/RDS/MySql1}`            |
| `mysql_catalog2_connection_string` | `mysql://jdbc:mysql://mysql2.host:3333/default?`user=sample2&password=sample2 |

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
`${Test/RDS/MySql1}`.

```
mysql://jdbc:mysql://mysql1.host:3306/default?...&${Test/RDS/MySql1}&...
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
mysql://jdbc:mysql://mysql1host:3306/default?...&user=sample2&password=sample2&...
```

Currently, the MySQL connector recognizes the `user` and
`password` JDBC properties.

#### Using a single

connection handler

You can use the following single connection metadata and record handlers to
connect to a single MySQL instance.

| Handler type      | Class                   |
| ----------------- | ----------------------- |
| Composite handler | `MySqlCompositeHandler` |
| Metadata handler  | `MySqlMetadataHandler`  |
| Record handler    | `MySqlRecordHandler`    |

##### Single

connection handler parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `default` | Required. The default connection string. |

The single connection handlers support one database instance and must provide a
`default` connection string parameter. All other connection
strings are ignored.

The following example property is for a single MySQL instance supported by a Lambda function.

| Property  | Value                                                     |
| --------- | --------------------------------------------------------- |
| `default` | `mysql://mysql1.host:3306/default?secret=Test/RDS/`MySql1 |

#### Spill parameters

The Lambda SDK can spill data to Amazon S3. All database instances accessed by the same
Lambda function spill to the same location.

| Parameter                   | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `spill_bucket`              | Required. Spill bucket name.                                                                                                                                                                                                                                                                                                                                                                           |
| `spill_prefix`              | Required. Spill bucket key<br>prefix.                                                                                                                                                                                                                                                                                                                                                                  |
| `spill_put_request_headers` | (Optional) A JSON encoded map of request headers and values for<br>the Amazon S3 `putObject` request that is used for spilling<br>(for example, `{"x-amz-server-side-encryption" :<br>"AES256"}`). For other possible headers, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md")<br>in the _Amazon Simple Storage Service API Reference_. |

## Data type support

The following table shows the corresponding data types for JDBC and Arrow.

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

## Partitions and splits

Partitions are used to determine how to generate splits for the connector. Athena constructs a synthetic column of type `varchar` that represents the partitioning scheme for the table to help the connector generate splits. The connector does not modify the actual table definition.

## Performance

MySQL supports native partitions. The Athena MySQL connector can
retrieve data from these partitions in parallel. If you want to query very large
datasets with uniform partition distribution, native partitioning is highly
recommended.

The Athena MySQL connector performs predicate pushdown to decrease the data scanned by the query. `LIMIT` clauses, simple predicates, and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time.

### LIMIT

clauses

A `LIMIT N` statement reduces the data scanned by the query. With
`LIMIT N` pushdown, the connector returns only `N` rows to
Athena.

### Predicates

A predicate is an expression in the `WHERE` clause of a SQL query that
evaluates to a Boolean value and filters rows based on multiple conditions. The
Athena MySQL connector can combine these expressions and push them directly to
MySQL for enhanced functionality and to reduce the amount of data scanned.

The following Athena MySQL connector operators support predicate
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

For an article on using predicate pushdown to improve performance in federated
queries, including MySQL, see [Improve federated queries with predicate pushdown in Amazon Athena](https://aws.amazon.com/blogs/big-data/improve-federated-queries-with-predicate-pushdown-in-amazon-athena/ "https://aws.amazon.com/blogs/big-data/improve-federated-queries-with-predicate-pushdown-in-amazon-athena/") in the
_AWS Big Data Blog_.

## Passthrough

queries

The MySQL connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md"). Passthrough
queries use a table function to push your full query down to the data source for
execution.

To use passthrough queries with MySQL, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '`query string`'
        ))
```

The following example query pushes down a query to a data source in MySQL. The query
selects all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer LIMIT 10'
        ))
```

## License information

By using this connector, you acknowledge the inclusion of third party components, a list
of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-mysql/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-mysql/pom.xml") file for this connector, and agree to the terms in the respective third
party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-mysql/LICENSE.txt "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-mysql/LICENSE.txt") file on GitHub.com.

## Additional resources

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-mysql/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-mysql/pom.xml") file for the MySQL connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-mysql "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-mysql") on GitHub.com.
