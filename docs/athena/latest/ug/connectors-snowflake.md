

# Amazon Athena Snowflake connector
<a name="connectors-snowflake"></a>

The Amazon Athena connector for [Snowflake](https://www.snowflake.com/) enables Amazon Athena to run SQL queries on data stored in your Snowflake SQL database or RDS instances using JDBC.

This connector can be registered with Glue Data Catalog as a federated catalog. It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

## Prerequisites
<a name="connectors-snowflake-prerequisites"></a>

Deploy the connector to your AWS account using the Athena console or the `CreateDataCatalog` API operation. For more information, see [Create a data source connection](connect-to-a-data-source.md).

## Limitations
<a name="connectors-snowflake-limitations"></a>
+ Write DDL operations are not supported.
+ In a multiplexer setup, the spill bucket and prefix are shared across all database instances.
+ Any relevant Lambda limits. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) in the *AWS Lambda Developer Guide*.
+ Only Athena data catalog federated connectors support multiplexer setup. 
+ Currently, Snowflake views with single split are supported. 
+  In Snowflake, object names are case-sensitive. Athena accepts mixed case in DDL and DML queries, but by default [lower cases](https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html#table-names-and-table-column-names-in-ate-must-be-lowercase) the object names when it executes the query. The Snowflake connector supports only lower case when Glue Catalog/Lake Formation are used. When the Athena Catalog is used, customers can control the casing behavior using the `casing_mode` Lambda environment variable whose possible values are listed in the [Parameters](#connectors-snowflake-parameters) section (for example, `key=casing_mode, value = CASE_INSENSITIVE_SEARCH`). 

## Terms
<a name="connectors-snowflake-terms"></a>

The following terms relate to the Snowflake connector.
+ **Database instance** – Any instance of a database deployed on premises, on Amazon EC2, or on Amazon RDS.
+ **Handler** – A Lambda handler that accesses your database instance. A handler can be for metadata or for data records.
+ **Metadata handler** – A Lambda handler that retrieves metadata from your database instance.
+ **Record handler** – A Lambda handler that retrieves data records from your database instance.
+ **Composite handler** – A Lambda handler that retrieves both metadata and data records from your database instance.
+ **Property or parameter** – A database property used by handlers to extract database information. You configure these properties as Lambda environment variables.
+ **Connection String** – A string of text used to establish a connection to a database instance.
+ **Catalog** – A non-AWS Glue catalog registered with Athena that is a required prefix for the `connection_string` property.
+ **Multiplexing handler** – A Lambda handler that can accept and use multiple database connections.

## Parameters
<a name="connectors-snowflake-parameters"></a>

Use the parameters in this section to configure the Snowflake connector.

### AWS Glue Data Catalog federated connectors
<a name="snowflake-gc"></a>

We recommend that you configure a Snowflake connector by using a Glue connections object. To do this, set the `glue_connection` environment variable of the Snowflake connector Lambda to the name of the Glue connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type SNOWFLAKE
```

**Lambda environment properties**

The following Lambda environment properties apply only when you use the connector with a Lambda function in your account.
+ **glue\_connection** – Specifies the name of the Glue connection associated with the federated connector. 
+ **casing\_mode** – (Optional) Specifies how to handle casing for schema and table names. The `casing_mode` parameter uses the following values to specify the behavior of casing:
  + **NONE** – Do not change case of the given schema and table names (run the query as is against Snowflake). This is the default value when **casing\_mode** is not specified. 
  + **UPPER** – Upper case all given schema and table names in the query before running it against Snowflake.
  + **LOWER** – Lower case all given schema and table names in the query before running it against Snowflake.
  + **CASE\_INSENSITIVE\_SEARCH** – Perform case insensitive searches against schema and tables names in Snowflake. For example, you can use this mode when you have a query like `SELECT * FROM EMPLOYEE` and Snowflake contains a table called `Employee`. However, in the presence of name collisions, such as having a table called `EMPLOYEE` and another table called `Employee` in Snowflake, the query will fail.

**Note**  
The Snowflake connector created using a AWS Glue Data Catalog federated connection does not support the use of a multiplexing handler.
The Snowflake connector created using a AWS Glue Data Catalog federated connection only supports `ConnectionSchemaVersion` 2.

**Storing credentials**

All connectors that use a AWS Glue Data Catalog federated connection must use AWS Secrets Manager to store credentials. For more information, see [Authenticate with Snowflake](connectors-snowflake-authentication.md).

### Athena data catalog federated connectors
<a name="snowflake-legacy"></a>

**Note**  
Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created without an associated Glue connection. Use the following parameters only when you [manually deploy](connect-data-source-serverless-app-repo.md) an earlier version of an Athena data source connector or when the `glue_connection` environment property is not specified.

**Lambda environment properties**
+ **default** – The JDBC connection string to use to connect to the Snowflake database instance. For example, `snowflake://${jdbc_connection_string}`
+ **catalog\_connection\_string** – Used by the Multiplexing handler (not supported when using a glue connection). A database instance connection string. Prefix the environment variable with the name of the catalog used in Athena. For example, if the catalog registered with Athena is mysnowflakecatalog, then the environment variable name is mysnowflakecatalog\_connection\_string.
+ **casing\_mode** – (Optional) Specifies how to handle casing for schema and table names. The `casing_mode` parameter uses the following values to specify the behavior of casing:
  + **NONE** – Do not change case of the given schema and table names (run the query as is against Snowflake). This is the default value when **casing\_mode** is not specified. 
  + **UPPER** – Upper case all given schema and table names in the query before running it against Snowflake.
  + **LOWER** – Lower case all given schema and table names in the query before running it against Snowflake.
  + **CASE\_INSENSITIVE\_SEARCH** – Perform case insensitive searches against schema and tables names in Snowflake. For example, you can use this mode when you have a query like `SELECT * FROM EMPLOYEE` and Snowflake contains a table called `Employee`. However, in the presence of name collisions, such as having a table called `EMPLOYEE` and another table called `Employee` in Snowflake, the query will fail.
+ **spill\_bucket** – Specifies the Amazon S3 bucket for data that exceeds Lambda function limits.
+ **spill\_prefix** – (Optional) Defaults to a subfolder in the specified `spill_bucket` called `athena-federation-spill`. We recommend that you configure an Amazon S3 [storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) on this location to delete spills older than a predetermined number of days or hours.
+ **spill\_put\_request\_headers** – (Optional) A JSON encoded map of request headers and values for the Amazon S3 `putObject` request that is used for spilling (for example, `{"x-amz-server-side-encryption" : "AES256"}`). For other possible headers, see [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) in the *Amazon Simple Storage Service API Reference*.
+ **kms\_key\_id** – (Optional) By default, any data that is spilled to Amazon S3 is encrypted using the AES-GCM authenticated encryption mode and a randomly generated key. To have your Lambda function use stronger encryption keys generated by KMS like `a7e63k4b-8loc-40db-a2a1-4d0en2cd8331`, you can specify a KMS key ID.
+ **disable\_spill\_encryption** – (Optional) When set to `True`, disables spill encryption. Defaults to `False` so that data that is spilled to S3 is encrypted using AES-GCM – either using a randomly generated key or KMS to generate keys. Disabling spill encryption can improve performance, especially if your spill location uses [server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html).

#### Connection string
<a name="connectors-snowflake-connection-string"></a>

Use a JDBC connection string in the following format to connect to a database instance.

```
snowflake://${{{jdbc_connection_string}}}
```

#### Using a multiplexing handler
<a name="connectors-snowflake-using-a-multiplexing-handler"></a>

You can use a multiplexer to connect to multiple database instances with a single Lambda function. Requests are routed by catalog name. Use the following classes in Lambda.



| Handler | Class | 
| --- | --- | 
| Composite handler | SnowflakeMuxCompositeHandler | 
| Metadata handler | SnowflakeMuxMetadataHandler | 
| Record handler | SnowflakeMuxRecordHandler | 

##### Multiplexing handler parameters
<a name="connectors-snowflake-multiplexing-handler-parameters"></a>



| Parameter | Description | 
| --- | --- | 
| ${{catalog}}\_connection\_string | Required. A database instance connection string. Prefix the environment variable with the name of the catalog used in Athena. For example, if the catalog registered with Athena is mysnowflakecatalog, then the environment variable name is mysnowflakecatalog\_connection\_string. | 
| default | Required. The default connection string. This string is used when the catalog is lambda:${{{AWS\_LAMBDA\_FUNCTION\_NAME}}}. | 

The following example properties are for a Snowflake MUX Lambda function that supports two database instances: `snowflake1` (the default), and `snowflake2`.



| Property | Value | 
| --- | --- | 
| default | snowflake://jdbc:snowflake://snowflake1.host:port/?warehouse=warehousename&db=db1&schema=schema1&${Test/RDS/Snowflake1} | 
| snowflake\_catalog1\_connection\_string | snowflake://jdbc:snowflake://snowflake1.host:port/?warehouse=warehousename&db=db1&schema=schema1${Test/RDS/Snowflake1} | 
| snowflake\_catalog2\_connection\_string | snowflake://jdbc:snowflake://snowflake2.host:port/?warehouse=warehousename&db=db1&schema=schema1&user=sample2&password=sample2 | 

##### Providing credentials
<a name="connectors-snowflake-providing-credentials"></a>

To provide a user name and password for your database in your JDBC connection string, you can use connection string properties or AWS Secrets Manager.
+ **Connection String** – A user name and password can be specified as properties in the JDBC connection string.
**Important**  
As a security best practice, don't use hardcoded credentials in your environment variables or connection strings. For information about moving your hardcoded secrets to AWS Secrets Manager, see [Move hardcoded secrets to AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/hardcoded.html) in the *AWS Secrets Manager User Guide*.
+ **AWS Secrets Manager** – To use the Athena Federated Query feature with AWS Secrets Manager, the VPC connected to your Lambda function should have [internet access](https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/) or a [VPC endpoint](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html) to connect to Secrets Manager.

  You can put the name of a secret in AWS Secrets Manager in your JDBC connection string. The connector replaces the secret name with the `username` and `password` values from Secrets Manager.

  For Amazon RDS database instances, this support is tightly integrated. If you use Amazon RDS, we highly recommend using AWS Secrets Manager and credential rotation. If your database does not use Amazon RDS, store the credentials as JSON in the following format:

  ```
  {"username": "${username}", "password": "${password}"}
  ```

**Example connection string with secret name**  
The following string has the secret name `${Test/RDS/Snowflake1}`.

```
snowflake://jdbc:snowflake://snowflake1.host:port/?warehouse=warehousename&db=db1&schema=schema1${Test/RDS/Snowflake1}&... 
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
snowflake://jdbc:snowflake://snowflake1.host:port/warehouse=warehousename&db=db1&schema=schema1&user=sample2&password=sample2&... 
```

Currently, Snowflake recognizes the `user` and `password` JDBC properties. It also accepts the user name and password in the format {{username}}`/`{{password}} without the keys `user` or `password`.

#### Using a single connection handler
<a name="connectors-snowflake-using-a-single-connection-handler"></a>

You can use the following single connection metadata and record handlers to connect to a single Snowflake instance.



| Handler type | Class | 
| --- | --- | 
| Composite handler | SnowflakeCompositeHandler | 
| Metadata handler | SnowflakeMetadataHandler | 
| Record handler | SnowflakeRecordHandler | 

##### Single connection handler parameters
<a name="connectors-snowflake-single-connection-handler-parameters"></a>



| Parameter | Description | 
| --- | --- | 
| default | Required. The default connection string. | 

The single connection handlers support one database instance and must provide a `default` connection string parameter. All other connection strings are ignored.

The following example property is for a single Snowflake instance supported by a Lambda function.



| Property | Value | 
| --- | --- | 
| default | snowflake://jdbc:snowflake://snowflake1.host:port/?secret=Test/RDS/Snowflake1 | 

#### Spill parameters
<a name="connectors-snowflake-spill-parameters"></a>

The Lambda SDK can spill data to Amazon S3. All database instances accessed by the same Lambda function spill to the same location.



| Parameter | Description | 
| --- | --- | 
| spill\_bucket | Required. Spill bucket name. | 
| spill\_prefix | Required. Spill bucket key prefix. | 
| spill\_put\_request\_headers | (Optional) A JSON encoded map of request headers and values for the Amazon S3 putObject request that is used for spilling (for example, {"x-amz-server-side-encryption" : "AES256"}). For other possible headers, see [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) in the Amazon Simple Storage Service API Reference. | 

## Data type support
<a name="connectors-snowflake-data-type-support"></a>

The following table shows the corresponding data types for JDBC and Apache Arrow.



| JDBC | Arrow | 
| --- | --- | 
| Boolean | Bit | 
| Integer | Tiny | 
| Short | Smallint | 
| Integer | Int | 
| Long | Bigint | 
| float | Float4 | 
| Double | Float8 | 
| Date | DateDay | 
| Timestamp | DateMilli | 
| String | Varchar | 
| Bytes | Varbinary | 
| BigDecimal | Decimal | 
| ARRAY | List | 

## Data type conversions
<a name="connectors-snowflake-data-type-conversions"></a>

In addition to the JDBC to Arrow conversions, the connector performs certain other conversions to make the Snowflake source and Athena data types compatible. These conversions help ensure that queries get executed successfully. The following table shows these conversions.



| Source data type (Snowflake) | Converted data type (Athena) | 
| --- | --- | 
| TIMESTAMP | TIMESTAMPMILLI | 
| DATE | TIMESTAMPMILLI | 
| INTEGER | INT | 
| DECIMAL | BIGINT | 
| TIMESTAMP\_NTZ | TIMESTAMPMILLI | 

All other unsupported data types are converted to `VARCHAR`.

## Partitions and splits
<a name="connectors-snowflake-partitions-and-splits"></a>

Partitions are used to determine how to generate splits for the connector. Athena constructs a synthetic column of type `varchar` that represents the partitioning scheme for the table to help the connector generate splits. The connector does not modify the actual table definition.

To create this synthetic column and the partitions, Athena requires a primary key to be defined. However, because Snowflake does not enforce primary key constraints, you must enforce uniqueness yourself. Failure to do so causes Athena to default to a single split.

## Performance
<a name="connectors-snowflake-performance"></a>

For optimal performance, use filters in queries whenever possible. In addition, we highly recommend native partitioning to retrieve huge datasets that have uniform partition distribution. Selecting a subset of columns significantly speeds up query runtime and reduces data scanned. The Snowflake connector is resilient to throttling due to concurrency.

The Athena Snowflake connector performs predicate pushdown to decrease the data scanned by the query. `LIMIT` clauses, simple predicates, and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time.

### LIMIT clauses
<a name="connectors-snowflake-performance-limit-clauses"></a>

A `LIMIT N` statement reduces the data scanned by the query. With `LIMIT N` pushdown, the connector returns only `N` rows to Athena.

### Predicates
<a name="connectors-snowflake-performance-predicates"></a>

A predicate is an expression in the `WHERE` clause of a SQL query that evaluates to a Boolean value and filters rows based on multiple conditions. The Athena Snowflake connector can combine these expressions and push them directly to Snowflake for enhanced functionality and to reduce the amount of data scanned.

The following Athena Snowflake connector operators support predicate pushdown:
+ **Boolean: **AND, OR, NOT
+ **Equality: **EQUAL, NOT\_EQUAL, LESS\_THAN, LESS\_THAN\_OR\_EQUAL, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL, IS\_DISTINCT\_FROM, NULL\_IF, IS\_NULL
+ **Arithmetic: **ADD, SUBTRACT, MULTIPLY, DIVIDE, MODULUS, NEGATE
+ **Other: **LIKE\_PATTERN, IN

### Combined pushdown example
<a name="connectors-snowflake-performance-pushdown-example"></a>

For enhanced querying capabilities, combine the pushdown types, as in the following example:

```
SELECT * 
FROM my_table 
WHERE col_a > 10 
    AND ((col_a + col_b) > (col_c % col_d))
    AND (col_e IN ('val1', 'val2', 'val3') OR col_f LIKE '%pattern%') 
LIMIT 10;
```

## Passthrough queries
<a name="connectors-snowflake-passthrough-queries"></a>

The Snowflake connector supports [passthrough queries](federated-query-passthrough.md). Passthrough queries use a table function to push your full query down to the data source for execution.

To use passthrough queries with Snowflake, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '{{query string}}'
        ))
```

The following example query pushes down a query to a data source in Snowflake. The query selects all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer LIMIT 10'
        ))
```

## License information
<a name="connectors-snowflake-license-information"></a>

By using this connector, you acknowledge the inclusion of third party components, a list of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-snowflake/pom.xml) file for this connector, and agree to the terms in the respective third party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-snowflake/LICENSE.txt) file on GitHub.com.

## Additional resources
<a name="connectors-snowflake-additional-resources"></a>

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-snowflake/pom.xml) file for the Snowflake connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-snowflake) on GitHub.com.