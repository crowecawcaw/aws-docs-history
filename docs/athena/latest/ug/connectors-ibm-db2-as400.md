# Amazon Athena IBM Db2 AS/400 (Db2 iSeries)

connector

The Amazon Athena connector for Db2 AS/400 enables Amazon Athena to run SQL queries on your IBM
Db2 AS/400 (Db2 iSeries) databases using JDBC.

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
- Date and timestamp data types in filter conditions must be cast to appropriate
  data types.

## Terms

The following terms relate to the Db2 AS/400 connector.

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

Use the parameters in this section to configure the Db2 AS/400 connector.

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created prior to December 3, 2024. These can differ from their corresponding [AWS Glue connection properties](../../../glue/latest/dg/connection-properties.md "../../../glue/latest/dg/connection-properties.md"). Starting December 3, 2024, use the parameters below only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector.

We recommend that you configure a Db2 AS/400 connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the Db2 AS/400 connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type DB2AS400
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
- The Db2 AS/400 connector created using Glue connections does not support the use of a multiplexing handler.
- The Db2 AS/400 connector created using Glue connections only supports `ConnectionSchemaVersion` 2.

#### Connection

string

Use a JDBC connection string in the following format to connect to a database
instance.

```
db2as400://${`jdbc_connection_string`}
```

#### Using a

multiplexing handler

You can use a multiplexer to connect to multiple database instances with a single
Lambda function. Requests are routed by catalog name. Use the following classes in
Lambda.

| Handler           | Class                    |
| ----------------- | ------------------------ |
| Composite handler | `Db2MuxCompositeHandler` |
| Metadata handler  | `Db2MuxMetadataHandler`  |
| Record handler    | `Db2MuxRecordHandler`    |

##### Multiplexing handler parameters

| Parameter                      | Description                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$`catalog`_connection_string` | Required. A database instance connection string. Prefix the<br>environment variable with the name of the catalog used in Athena. For example,<br>if the catalog registered with Athena is<br>`mydb2as400catalog`, then the environment<br>variable name is<br>`mydb2as400catalog_connection_string`. |
| `default`                      | Required. The default connection string. This string is used<br>when the catalog is<br>`lambda:${``AWS_LAMBDA_FUNCTION_NAME``}`.                                                                                                                                                                     |

The following example properties are for a Db2 MUX Lambda function
that supports two database instances: `db2as4001` (the
default), and `db2as4002`.

| Property                              | Value                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `default`                             | `db2as400://jdbc:as400://`<ip_address>`;`<properties>`;:${`<secret<br>name>`};`                  |
| `db2as400_catalog1_connection_string` | `db2as400://jdbc:as400://db2as4001.`hostname/:${`secret1_name`}``                                |
| `db2as400_catalog2_connection_string` | `db2as400://jdbc:as400://db2as4002.``hostname/:${`secret2_name`}```                              |
| `db2as400_catalog3_connection_string` | `db2as400://jdbc:as400://`<ip_address>`;user=`<username>`;password=`<password>`;`<properties>`;` |

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
`${secret_name}`.

```
db2as400://jdbc:as400://`<ip_address>`;`<properties>`;:${`<secret_name>`};
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
db2as400://jdbc:as400://`<ip_address>`;user=`<username>`;password=`<password>`;`<properties>`;
```

#### Using a

single connection handler

You can use the following single connection metadata and record handlers to
connect to a single Db2 AS/400 instance.

| Handler type      | Class                 |
| ----------------- | --------------------- |
| Composite handler | `Db2CompositeHandler` |
| Metadata handler  | `Db2MetadataHandler`  |
| Record handler    | `Db2RecordHandler`    |

##### Single connection handler parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `default` | Required. The default connection string. |

The single connection handlers support one database instance and must provide a
`default` connection string parameter. All other connection
strings are ignored.

The following example property is for a single Db2 AS/400 instance supported by a Lambda function.

| Property  | Value                                                                        |
| --------- | ---------------------------------------------------------------------------- |
| `default` | `db2as400://jdbc:as400://`<ip_address>`;`<properties>`;:${`<secret_name>`};` |

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

| Db2 AS/400 | Arrow     |
| ---------- | --------- |
| CHAR       | VARCHAR   |
| VARCHAR    | VARCHAR   |
| DATE       | DATEDAY   |
| TIME       | VARCHAR   |
| TIMESTAMP  | DATEMILLI |
| DATETIME   | DATEMILLI |
| BOOLEAN    | BOOL      |
| SMALLINT   | SMALLINT  |
| INTEGER    | INT       |
| BIGINT     | BIGINT    |
| DECIMAL    | DECIMAL   |
| REAL       | FLOAT8    |
| DOUBLE     | FLOAT8    |
| DECFLOAT   | FLOAT8    |

## Partitions and

splits

A partition is represented by one or more partition columns of type
`varchar`. The Db2 AS/400 connector creates partitions using the following
organization schemes.

- Distribute by hash
- Partition by range
- Organize by dimensions

The connector retrieves partition details such as the number of partitions and column
name from one or more Db2 AS/400 metadata tables. Splits are created based upon the number
of partitions identified.

## Performance

For improved performance, use predicate pushdown to query from Athena, as in the
following examples.

```
SELECT * FROM "lambda:`<LAMBDA_NAME>`"."`<SCHEMA_NAME>`"."`<TABLE_NAME>`"
 WHERE integercol = 2147483647
```

```
SELECT * FROM "lambda: `<LAMBDA_NAME>`"."`<SCHEMA_NAME>`"."`<TABLE_NAME>`"
 WHERE timestampcol >= TIMESTAMP '2018-03-25 07:30:58.878'
```

## Passthrough

queries

The Db2 AS/400 connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md"). Passthrough
queries use a table function to push your full query down to the data source for
execution.

To use passthrough queries with Db2 AS/400, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '`query string`'
        ))
```

The following example query pushes down a query to a data source in Db2 AS/400. The query
selects all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer LIMIT 10'
        ))
```

## License information

By using this connector, you acknowledge the inclusion of third party components, a list
of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-db2-as400/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-db2-as400/pom.xml") file for this connector, and agree to the terms in the respective third
party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-db2-as400/LICENSE.txt "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-db2-as400/LICENSE.txt") file on GitHub.com.

## Additional resources

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-db2-as400/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-db2-as400/pom.xml") file for the Db2 AS/400 connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-db2-as400 "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-db2-as400") on GitHub.com.
