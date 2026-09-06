

# Amazon Athena Redshift connector
<a name="connectors-redshift"></a>

The Amazon Athena Redshift connector enables Amazon Athena to access your Amazon Redshift and Amazon Redshift Serverless databases, including Redshift Serverless views. You can connect to either service using the JDBC connection string configuration settings described on this page.

This connector can be registered with Glue Data Catalog as a federated catalog. It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

## Prerequisites
<a name="connectors-redshift-prerequisites"></a>
+ Deploy the connector to your AWS account using the Athena console or the AWS Serverless Application Repository. For more information, see [Create a data source connection](connect-to-a-data-source.md) or [Use the AWS Serverless Application Repository to deploy a data source connector](connect-data-source-serverless-app-repo.md).

## Limitations
<a name="connectors-redshift-limitations"></a>
+ Write DDL operations are not supported.
+ In a multiplexer setup, the spill bucket and prefix are shared across all database instances.
+ Any relevant Lambda limits. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) in the *AWS Lambda Developer Guide*.
+ Because Redshift does not support external partitions, all data specified by a query is retrieved every time.
+ Like Redshift, Athena treats trailing spaces in Redshift `CHAR` types as semantically insignificant for length and comparison purposes. Note that this applies only to `CHAR` but not to `VARCHAR` types. Athena ignores trailing spaces for the `CHAR` type, but treats them as significant for the `VARCHAR` type.

## Terms
<a name="connectors-redshift-terms"></a>

The following terms relate to the Redshift connector.
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
<a name="connectors-redshift-parameters"></a>

Use the parameters in this section to configure the Redshift connector.

### AWS Glue Data Catalog federated connectors
<a name="redshift-gc"></a>

We recommend that you configure a Redshift connector by using a Glue connections object. To do this, set the `glue_connection` environment variable of the Amazon Redshift connector Lambda to the name of the Glue connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type REDSHIFT
```

**Lambda environment properties**

The following Lambda environment properties apply only when you use the connector with a Lambda function in your account.

**glue\_connection** – Specifies the name of the Glue connection associated with the federated connector. 

**Note**  
All connectors that use a AWS Glue Data Catalog federated connection must use AWS Secrets Manager to store credentials.
The Redshift connector created using a AWS Glue Data Catalog federated connection does not support the use of a multiplexing handler.
The Redshift connector created using a AWS Glue Data Catalog federated connection only supports `ConnectionSchemaVersion` 2.

### Athena data catalog federated connectors
<a name="redshift-legacy"></a>

**Note**  
Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created without an associated Glue connection. Use the following parameters only when you [manually deploy](connect-data-source-serverless-app-repo.md) an earlier version of an Athena data source connector or when the `glue_connection` environment property is not specified.

**Lambda environment properties**
+ **spill\_bucket** – Specifies the Amazon S3 bucket for data that exceeds Lambda function limits.
+ **spill\_prefix** – (Optional) Defaults to a subfolder in the specified `spill_bucket` called `athena-federation-spill`. We recommend that you configure an Amazon S3 [storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) on this location to delete spills older than a predetermined number of days or hours.
+ **spill\_put\_request\_headers** – (Optional) A JSON encoded map of request headers and values for the Amazon S3 `putObject` request that is used for spilling (for example, `{"x-amz-server-side-encryption" : "AES256"}`). For other possible headers, see [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) in the *Amazon Simple Storage Service API Reference*.
+ **kms\_key\_id** – (Optional) By default, any data that is spilled to Amazon S3 is encrypted using the AES-GCM authenticated encryption mode and a randomly generated key. To have your Lambda function use stronger encryption keys generated by KMS like `a7e63k4b-8loc-40db-a2a1-4d0en2cd8331`, you can specify a KMS key ID.
+ **disable\_spill\_encryption** – (Optional) When set to `True`, disables spill encryption. Defaults to `False` so that data that is spilled to S3 is encrypted using AES-GCM – either using a randomly generated key or KMS to generate keys. Disabling spill encryption can improve performance, especially if your spill location uses [server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html).
+ **disable\_glue** – (Optional) If present and set to true, the connector does not attempt to retrieve supplemental metadata from AWS Glue.
+ **glue\_catalog** – (Optional) Use this option to specify a [cross-account AWS Glue catalog](data-sources-glue-cross-account.md). By default, the connector attempts to get metadata from its own AWS Glue account.

#### Connection string
<a name="connectors-redshift-connection-string"></a>

Use a JDBC connection string in the following format to connect to a database instance.

```
redshift://${{{jdbc_connection_string}}}
```

#### Using a multiplexing handler
<a name="connectors-redshift-using-a-multiplexing-handler"></a>

You can use a multiplexer to connect to multiple database instances with a single Lambda function. Requests are routed by catalog name. Use the following classes in Lambda.



| Handler | Class | 
| --- | --- | 
| Composite handler | RedshiftMuxCompositeHandler | 
| Metadata handler | RedshiftMuxMetadataHandler | 
| Record handler | RedshiftMuxRecordHandler | 

##### Multiplexing handler parameters
<a name="connectors-redshift-multiplexing-handler-parameters"></a>



| Parameter | Description | 
| --- | --- | 
| ${{catalog}}\_connection\_string | Required. A database instance connection string. Prefix the environment variable with the name of the catalog used in Athena. For example, if the catalog registered with Athena is myredshiftcatalog, then the environment variable name is myredshiftcatalog\_connection\_string. | 
| default | Required. The default connection string. This string is used when the catalog is lambda:${{{AWS\_LAMBDA\_FUNCTION\_NAME}}}. | 

The following example properties are for a Redshift MUX Lambda function that supports two database instances: `redshift1` (the default), and `redshift2`.



| Property | Value | 
| --- | --- | 
| default | redshift://jdbc:redshift://redshift1.host:5439/dev?user=sample2&password=sample2 | 
| redshift\_catalog1\_connection\_string | redshift://jdbc:redshift://redshift1.host:3306/default?${Test/RDS/Redshift1} | 
| redshift\_catalog2\_connection\_string | redshift://jdbc:redshift://redshift2.host:3333/default?user=sample2&password=sample2 | 

##### Providing credentials
<a name="connectors-redshift-providing-credentials"></a>

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
The following string has the secret name ${Test/RDS/ `Redshift1`}.

```
redshift://jdbc:redshift://redshift1.host:3306/default?...&${Test/RDS/Redshift1}&...
```

The connector uses the secret name to retrieve secrets and provide the user name and password, as in the following example.

```
redshift://jdbc:redshift://redshift1.host:3306/default?...&user=sample2&password=sample2&...
```

Currently, the Redshift connector recognizes the `user` and `password` JDBC properties.

## Data type support
<a name="connectors-redshift-data-type-support"></a>

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

## Partitions and splits
<a name="connectors-redshift-partitions-and-splits"></a>

Redshift does not support external partitions. For information about performance related issues, see [Performance](#connectors-redshift-performance).

## Performance
<a name="connectors-redshift-performance"></a>

The Athena Redshift connector performs predicate pushdown to decrease the data scanned by the query. `LIMIT` clauses, `ORDER BY` clauses, simple predicates, and complex expressions are pushed down to the connector to reduce the amount of data scanned and decrease query execution run time. However, selecting a subset of columns sometimes results in a longer query execution runtime. Amazon Redshift is particularly susceptible to query execution slowdown when you run multiple queries concurrently.

### LIMIT clauses
<a name="connectors-redshift-performance-limit-clauses"></a>

A `LIMIT N` statement reduces the data scanned by the query. With `LIMIT N` pushdown, the connector returns only `N` rows to Athena.

### Top N queries
<a name="connectors-redshift-performance-top-n-queries"></a>

A top `N` query specifies an ordering of the result set and a limit on the number of rows returned. You can use this type of query to determine the top `N` max values or top `N` min values for your datasets. With top `N` pushdown, the connector returns only `N` ordered rows to Athena.

### Predicates
<a name="connectors-redshift-performance-predicates"></a>

A predicate is an expression in the `WHERE` clause of a SQL query that evaluates to a Boolean value and filters rows based on multiple conditions. The Athena Redshift connector can combine these expressions and push them directly to Redshift for enhanced functionality and to reduce the amount of data scanned.

The following Athena Redshift connector operators support predicate pushdown:
+ **Boolean: **AND, OR, NOT
+ **Equality: **EQUAL, NOT\_EQUAL, LESS\_THAN, LESS\_THAN\_OR\_EQUAL, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL, IS\_DISTINCT\_FROM, NULL\_IF, IS\_NULL
+ **Arithmetic: **ADD, SUBTRACT, MULTIPLY, DIVIDE, MODULUS, NEGATE
+ **Other: **LIKE\_PATTERN, IN

### Combined pushdown example
<a name="connectors-redshift-performance-pushdown-example"></a>

For enhanced querying capabilities, combine the pushdown types, as in the following example:

```
SELECT * 
FROM my_table 
WHERE col_a > 10 
    AND ((col_a + col_b) > (col_c % col_d)) 
    AND (col_e IN ('val1', 'val2', 'val3') OR col_f LIKE '%pattern%') 
ORDER BY col_a DESC 
LIMIT 10;
```

For an article on using predicate pushdown to improve performance in federated queries, including Amazon Redshift, see [Improve federated queries with predicate pushdown in Amazon Athena](https://aws.amazon.com/blogs/big-data/improve-federated-queries-with-predicate-pushdown-in-amazon-athena/) in the *AWS Big Data Blog*.

## Passthrough queries
<a name="connectors-redshift-passthrough-queries"></a>

The Redshift connector supports [passthrough queries](federated-query-passthrough.md). Passthrough queries use a table function to push your full query down to the data source for execution.

To use passthrough queries with Redshift, you can use the following syntax:

```
SELECT * FROM TABLE(
        system.query(
            query => '{{query string}}'
        ))
```

The following example query pushes down a query to a data source in Redshift. The query selects all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        system.query(
            query => 'SELECT * FROM customer LIMIT 10'
        ))
```

## Additional resources
<a name="connectors-redshift-additional-resources"></a>

For the latest JDBC driver version information, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-redshift/pom.xml) file for the Redshift connector on GitHub.com.

For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-redshift) on GitHub.com.