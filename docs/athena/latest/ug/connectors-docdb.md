# Amazon Athena DocumentDB connector

The Amazon Athena DocumentDB connector enables Athena to communicate with your DocumentDB instances
so that you can query your DocumentDB data with SQL. The connector also works with any
endpoint that is compatible with MongoDB.

Unlike traditional relational data stores, Amazon DocumentDB collections do not have set schema.
DocumentDB does not have a metadata store. Each entry in a DocumentDB collection can have
different fields and data types.

The DocumentDB connector supports two mechanisms for generating table schema information:
basic schema inference and AWS Glue Data Catalog metadata.

Schema inference is the default. This option scans a small number of documents in your
collection, forms a union of all fields, and coerces fields that have non-overlapping data
types. This option works well for collections that have mostly uniform entries.

For collections with a greater variety of data types, the connector supports retrieving
metadata from the AWS Glue Data Catalog. If the connector sees a AWS Glue database and table that match
your DocumentDB database and collection names, it gets its schema information from the
corresponding AWS Glue table. When you create your AWS Glue table, we recommend that you make it a
superset of all fields that you might want to access from your DocumentDB collection.

If you have Lake Formation enabled in your account, the IAM role for your Athena federated Lambda connector that you deployed in the AWS Serverless Application Repository must have read access in Lake Formation to the AWS Glue Data Catalog.

This connector can be registered with Glue Data Catalog as a federated catalog.
It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

## Prerequisites

- Deploy the connector to your AWS account using the Athena console or the AWS Serverless Application Repository. For more information, see [Create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md") or [Use the AWS Serverless Application Repository to deploy a data
  source connector](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md").

## Parameters

Use the parameters in this section to configure the DocumentDB connector.

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created prior to December 3, 2024. These can differ from their corresponding [AWS Glue connection properties](../../../glue/latest/dg/connection-properties.md "../../../glue/latest/dg/connection-properties.md"). Starting December 3, 2024, use the parameters below only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector.

We recommend that you configure a DocumentDB connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the DocumentDB connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type DOCUMENTDB
```

**Lambda environment properties**

- glue_connection – Specifies the name of the Glue connection associated with the federated connector.

###### Note

- All connectors that use Glue connections must use AWS Secrets Manager to store credentials.
- The DocumentDB connector created using Glue connections does not support the use of a multiplexing handler.
- The DocumentDB connector created using Glue connections only supports `ConnectionSchemaVersion` 2.

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
- disable_glue – (Optional) If present and set to true, the connector does not attempt to retrieve supplemental metadata from AWS Glue.
- glue_catalog – (Optional) Use this
  option to specify a [cross-account AWS Glue
  catalog](data-sources-glue-cross-account.md "data-sources-glue-cross-account.md"). By default, the connector attempts to get metadata from its
  own AWS Glue account.
- default_docdb – If present, specifies a
  DocumentDB connection string to use when no catalog-specific environment variable
  exists.
- disable_projection_and_casing –
  (Optional) Disables projection and casing. Use if you want to query Amazon DocumentDB
  tables that use case sensitive column names. The
  `disable_projection_and_casing` parameter uses the following
  values to specify the behavior of casing and column mapping:
  - false – This is the default
    setting. Projection is enabled, and the connector expects all column
    names to be in lower case.
  - true – Disables projection and
    casing. When using the `disable_projection_and_casing`
    parameter, keep in mind the following points:
    - Use of the parameter can result in higher bandwidth usage.
      Additionally, if your Lambda function is not in the same
      AWS Region as your data source, you will incur higher standard
      AWS cross-region transfer costs as a result of the higher
      bandwidth usage. For more information about cross-region
      transfer costs, see [AWS Data Transfer Charges for Server and Serverless
      Architectures](https://aws.amazon.com/blogs/apn/aws-data-transfer-charges-for-server-and-serverless-architectures/ "https://aws.amazon.com/blogs/apn/aws-data-transfer-charges-for-server-and-serverless-architectures/") in the AWS Partner Network
      Blog.
    - Because a larger number of bytes is transferred and because
      the larger number of bytes requires a higher deserialization
      time, overall latency can increase.

- enable_case_insensitive_match –
  (Optional) When `true`, performs case insensitive searches against
  schema and table names in Amazon DocumentDB. The default is `false`. Use if
  your query contains uppercase schema or table names.

#### Specifying

connection strings

You can provide one or more properties that define the DocumentDB connection details
for the DocumentDB instances that you use with the connector. To do this, set a Lambda
environment variable that corresponds to the catalog name that you want to use in
Athena. For example, suppose you want to use the following queries to query two
different DocumentDB instances from Athena:

```
SELECT * FROM "docdb_instance_1".database.table
```

```
SELECT * FROM "docdb_instance_2".database.table
```

Before you can use these two SQL statements, you must add two environment
variables to your Lambda function: `docdb_instance_1` and
`docdb_instance_2`. The value for each should be a
DocumentDB connection string in the following format:

```
mongodb://:@:/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0
```

##### Using secrets

You can optionally use AWS Secrets Manager for part or all of the value for your
connection string details. To use the Athena Federated Query feature with Secrets Manager, the VPC
connected to your Lambda function should have [internet access](https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/ "https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/") or a [VPC
endpoint](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md") to connect to Secrets Manager.

If you use the syntax `${my_secret}` to put the name of a secret
from Secrets Manager in your connection string, the connector replaces
`${my_secret}` with its plain text value from Secrets Manager exactly.
Secrets should be stored as a plain text secret with value
``<username>`:`<password>``.
Secrets stored as
`{username:`<username>`,password:`<password>`}`
will not be passed to the connection string properly.

Secrets can also be used for the entire connection string entirely, and the
username and password can be defined within the secret.

For example, suppose you set the Lambda environment variable for
`docdb_instance_1` to the following value:

```
mongodb://${docdb_instance_1_creds}@myhostname.com:123/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0
```

The Athena Query Federation SDK automatically attempts to retrieve a secret named `docdb_instance_1_creds` from Secrets Manager and inject that
value in place of `${docdb_instance_1_creds}`.
Any part of the connection string that is enclosed by the `${
 }` character combination is interpreted as a secret from Secrets Manager. If
you specify a secret name that the connector cannot find in Secrets Manager, the connector
does not replace the text.

## Retrieving supplemental metadata

To retrieve supplemental metadata, follow these steps to configure your Glue database and table.

### Set up the Glue database

1. Create a Glue database with the same name as your DocumentDB collection.
2. In the Location URI field, enter `docdb-metadata-flag`.

### Configure the Glue table

Add the following parameters to your Glue table:

- `docdb-metadata-flag = true`
- `columnMapping = apple=APPLE`

In this example, `apple` represents the lowercase column name in Glue, and `APPLE` represents the actual case-sensitive column name in your DocumentDB collection.

### Verify metadata retrieval

1. Run your query.
2. Check the Lambda function's CloudWatch logs for successful metadata retrieval. A successful retrieval will show the following log entry:

```
doGetTable: Retrieved schema for table[TableName{schemaName=test, tableName=profiles}] from AWS Glue.
```

###### Note

If your table already has a `columnMapping` field configured, you only need to add the `docdb-metadata-flag = true` parameter to the table properties.

## Setting

up databases and tables in AWS Glue

Because the connector's built-in schema inference capability scans a limited number of
documents and supports only a subset of data types, you might want to use AWS Glue for
metadata instead.

To enable an AWS Glue table for use with Amazon DocumentDB, you must have a AWS Glue database and
table for the DocumentDB database and collection that you want to supply supplemental
metadata for.

###### To use an AWS Glue table for supplemental metadata

1. Use the AWS Glue console to create an AWS Glue database that has the same name as
   your Amazon DocumentDB database name.
2. Set the URI property of the database to include docdb-metadata-flag.
3. (Optional) Add the sourceTable table property.
   This property defines the source table name in Amazon DocumentDB. Use this property if
   your AWS Glue table has a different name from the table name in Amazon DocumentDB.
   Differences in naming rules between AWS Glue and Amazon DocumentDB can make this necessary.
   For example, capital letters are not permitted in AWS Glue table names, but they
   are permitted in Amazon DocumentDB table names.
4. (Optional) Add the columnMapping table
   property. This property defines column name mappings. Use this property if AWS Glue
   column naming rules prevent you from creating an AWS Glue table that has the same
   column names as those in your Amazon DocumentDB table. This can be useful because capital
   letters are permitted in Amazon DocumentDB column names but are not permitted in AWS Glue
   column names.

The `columnMapping` property value is expected to be a set of
mappings in the format `col1=Col1,col2=Col2`.

###### Note

Column mapping applies only to top level column names and not to nested
fields.

After you add the AWS Glue `columnMapping` table property, you can
remove the `disable_projection_and_casing` Lambda environment
variable. 5. Make sure that you use the data types appropriate for AWS Glue as listed in this document.

## Data type support

This section lists the data types that the DocumentDB connector uses for schema
inference, and the data types when AWS Glue metadata is used.

### Schema inference data

types

The schema inference feature of the DocumentDB connector attempts to infer values as
belonging to one of the following data types. The table shows the corresponding data
types for Amazon DocumentDB, Java, and Apache Arrow.

| Apache Arrow | Java or DocDB |
| ------------ | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VARCHAR      | String        |
| INT          | Integer       |
| BIGINT       | Long          |
| BIT          | Boolean       |
| FLOAT4       | Float         |
| FLOAT8       | Double        |
| TIMESTAMPSEC | Date          |
| VARCHAR      | ObjectId      |
| LIST         | List          |
| STRUCT       | Document      | ### AWS Glue data types If you use AWS Glue for supplemental metadata, you can configure the following data types. The table shows the corresponding data types for AWS Glue and Apache Arrow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| AWS Glue     | Apache Arrow  |
| ---          | ---           |
| int          | INT           |
| bigint       | BIGINT        |
| double       | FLOAT8        |
| float        | FLOAT4        |
| boolean      | BIT           |
| binary       | VARBINARY     |
| string       | VARCHAR       |
| List         | LIST          |
| Struct       | STRUCT        | ## Required Permissions For full details on the IAM policies that this connector requires, review the `Policies` section of the [athena-docdb.yaml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-docdb/athena-docdb.yaml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-docdb/athena-docdb.yaml") file. The following list summarizes the required permissions. <br>• Amazon S3 write access – The connector requires write access to a location in Amazon S3 in order to spill results from large queries. <br>• Athena GetQueryExecution – The connector uses this permission to fast-fail when the upstream Athena query has terminated. <br>• AWS Glue Data Catalog – The DocumentDB connector requires read only access to the AWS Glue Data Catalog to obtain schema information. <br>• CloudWatch Logs – The connector requires access to CloudWatch Logs for storing logs. <br>• AWS Secrets Manager read access – If you choose to store DocumentDB endpoint details in Secrets Manager, you must grant the connector access to those secrets. <br>• VPC access – The connector requires the ability to attach and detach interfaces to your VPC so that it can connect to it and communicate with your DocumentDB instances. ## Performance The Athena Amazon DocumentDB connector does not currently support parallel scans but attempts to push down predicates as part of its DocumentDB queries, and predicates against indexes on your DocumentDB collection result in significantly less data scanned. The Lambda function performs projection pushdown to decrease the data scanned by the query. However, selecting a subset of columns sometimes results in a longer query execution runtime. `LIMIT` clauses reduce the amount of data scanned, but if you don't provide a predicate, you should expect `SELECT` queries with a `LIMIT` clause to scan at least 16 MB of data. ## Passthrough queries The Athena Amazon DocumentDB connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md") and is NoSQL based. For information about querying Amazon DocumentDB, see [Querying](../../../documentdb/latest/developerguide/querying.md "../../../documentdb/latest/developerguide/querying.md") in the _Amazon DocumentDB Developer Guide_. To use passthrough queries with Amazon DocumentDB, use the following syntax: ``SELECT * FROM TABLE( system.query( database => '`database_name`', collection => '`collection_name`', filter => '{`query_syntax`}' ))`` The following example queries the `example` database within the `TPCDS` collection, filtering on all books with the title _Bill of Rights_. `SELECT * FROM TABLE( system.query( database => 'example', collection => 'tpcds', filter => '{title: "Bill of Rights"}' ))` ## Additional resources <br>• For an article on using [Amazon Athena Federated Query](federated-queries.md "federated-queries.md") to connect a MongoDB database to [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/") to build dashboards and visualizations, see [Visualize MongoDB data from Quick Suite using Amazon Athena Federated Query](https://aws.amazon.com/blogs/big-data/visualize-mongodb-data-from-amazon-quicksight-using-amazon-athena-federated-query/ "https://aws.amazon.com/blogs/big-data/visualize-mongodb-data-from-amazon-quicksight-using-amazon-athena-federated-query/") in the _AWS Big Data Blog_. <br>• For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-docdb "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-docdb") on GitHub.com. |
