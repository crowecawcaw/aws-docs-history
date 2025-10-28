# Accessing tables using the Amazon S3 Tables Iceberg REST endpoint

You can connect your Iceberg REST client to the Amazon S3 Tables Iceberg REST endpoint and make REST API calls to create, update, or query tables in S3 table buckets. The endpoint implements a set of standardized Iceberg REST APIs specified in the [Apache Iceberg REST Catalog Open API specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml "https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml") . The endpoint works by translating Iceberg REST API operations into corresponding S3 Tables operations.

###### Note

Amazon S3 Tables Iceberg REST endpoint can be used to access tables in AWS Partner Network (APN) catalog implementations or custom catalog implementations. It can also be used if you only need basic read/write access to a single table bucket. For other access scenarios we recommend using the AWS Glue Iceberg REST endpoint to connect to tables, which provides unified table management, centralized governance, and fine-grained access control. For more information, see [Accessing Amazon S3 tables using the AWS Glue Iceberg REST endpoint](s3-tables-integrating-glue-endpoint.md "s3-tables-integrating-glue-endpoint.md")

## Configuring the endpoint

You connect to the Amazon S3 Tables Iceberg REST endpoint using the service endpoint. S3 Tables Iceberg REST endpoints have the following format:

```
https://s3tables.<REGION>.amazonaws.com/iceberg
```

Refer to [S3 Tables AWS Regions and endpoints](s3-tables-regions-quotas.md#s3-tables-regions "s3-tables-regions-quotas.md#s3-tables-regions") for the Region-specific endpoints.

###### Catalog configuration properties

When using an Iceberg client to connect an analytics engine to the service endpoint, you must specify the following configuration properties when you initialize the catalog. Replace the `placeholder values` with the information for your Region and table bucket.

- The region-specific endpoint as the endpoint URI: `https://s3tables.<REGION>.amazonaws.com/iceberg`
- Your table bucket ARN as the warehouse location: `arn:aws:s3tables:<region>:<accountID>:bucket/<bucketname>`
- Sigv4 properties for authentication. The SigV4 signing name for the service endpoint requests is: `s3tables`

The following examples show you how to configure different clients to use the Amazon S3 Tables Iceberg REST endpoint.

PyIceberg
To use the Amazon S3 Tables Iceberg REST endpoint with PyIceberg, specify the following application configuration properties:

```
rest_catalog = load_catalog(
  catalog_name,
  **{
    "type": "rest",
    "warehouse":"arn:aws:s3tables:`<Region>:<accountID>`:bucket/`<bucketname>`",
    "uri": "https://s3tables.`<Region>`.amazonaws.com/iceberg",
    "rest.sigv4-enabled": "true",
    "rest.signing-name": "s3tables",
    "rest.signing-region": "`<Region>`"
  }
)
```

Apache Spark
To use the Amazon S3 Tables Iceberg REST endpoint with Spark, specify the following application configuration properties, replacing the `placeholder values` with the information for your Region and table bucket.

```
spark-shell \
  --packages "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.4.1,software.amazon.awssdk:bundle:2.20.160,software.amazon.awssdk:url-connection-client:2.20.160" \
  --master "local[*]" \
  --conf "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions" \
  --conf "spark.sql.defaultCatalog=spark_catalog" \
   --conf "spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkCatalog" \
  --conf "spark.sql.catalog.spark_catalog.type=rest" \
  --conf "spark.sql.catalog.spark_catalog.uri=https://s3tables.`<Region>`.amazonaws.com/iceberg" \
  --conf "spark.sql.catalog.spark_catalog.warehouse=arn:aws:s3tables:`<Region>:<accountID>`:bucket/`<bucketname>`" \
  --conf "spark.sql.catalog.spark_catalog.rest.sigv4-enabled=true" \
  --conf "spark.sql.catalog.spark_catalog.rest.signing-name=s3tables" \
  --conf "spark.sql.catalog.spark_catalog.rest.signing-region=`<Region>`" \
  --conf "spark.sql.catalog.spark_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO" \
  --conf "spark.hadoop.fs.s3a.aws.credentials.provider=org.apache.hadoop.fs.s3a.SimpleAWSCredentialProvider" \
  --conf "spark.sql.catalog.spark_catalog.rest-metrics-reporting-enabled=false"
```

## Authenticating and authorizing access to the endpoint

API requests to the S3 Tables service endpoints are authenticated using AWS Signature Version 4 (SigV4). See [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") to learn more about AWS SigV4.

The SigV4 signing name for Amazon S3 Tables Iceberg REST endpoint requests is: `s3tables`

Requests to the Amazon S3 Tables Iceberg REST endpoint are authorized using `s3tables` IAM actions corresponding to the REST API operations. These permissions can be defined in either IAM identity-based policies or resource-based policies attached to tables and table buckets. For more information, see [Access management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md").

You can track requests made to your tables through the REST endpoint with AWS CloudTrail. Requests will be logged as their corresponding S3 IAM action. For example, a `LoadTable` API will generate a management event for the `GetTableMetadataLocation` operation and a data event for the `GetTableData` operation. For more information, see [Logging with AWS CloudTrail for S3 Tables](s3-tables-logging.md "s3-tables-logging.md").

## Prefix and path parameters

Iceberg REST catalog APIs have a free-form prefix in their request URLs. For example, the `ListNamespaces` API call uses the `GET/v1/{prefix}/namespaces` URL format. For S3 Tables the REST path `{prefix}` is always your url-encoded table bucket ARN.

For example, for the following table bucket ARN:
`arn:aws:s3tables:`us-east-1`:111122223333:bucket/`bucketname``
 the prefix would be: 
 `arn%3Aaws%3As3tables%3A`us-east-1`%3A`111122223333`%3Abucket%2F`bucketname``

### Namespace path parameter

Namespaces in an Iceberg REST catalog API path can have multiple levels. However, S3 Tables only supports single-level namespaces. To access a namespace in a multi-level catalog hierarchy, you can connect to a multi-level catalog above the namespace when referencing the namespace. This allows any query engine that supports the 3-part notation of `catalog.namespace.table` to access objects in S3 Tables’ catalog hierarchy without compatibility issues compared to using the multi-level namespace.

## Supported Iceberg REST API operations

The following table contains the supported Iceberg REST APIs and how they correspond to S3 Tables actions.

| Iceberg REST operation  | REST path                                                   | S3 Tables IAM action                                                                     | CloudTrail EventName                                                               |
| ----------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `getConfig`             | `GET /v1/config`                                            | `s3tables:GetTableBucket`                                                                | `s3tables:GetTableBucket`                                                          |
| `listNamespaces`        | `GET /v1/{prefix}/namespaces`                               | `s3tables:ListNamespaces`                                                                | `s3tables:ListNamespaces`                                                          |
| `createNamespace`       | `POST /v1/{prefix}/namespaces`                              | `s3tables:CreateNamespace`                                                               | `s3tables:CreateNamespace`                                                         |
| `loadNamespaceMetadata` | `GET /v1/{prefix}/namespaces/{namespace}`                   | `s3tables:GetNamespace`                                                                  | `s3tables:GetNamespace`                                                            |
| `dropNamespace`         | `DELETE /v1/{prefix}/namespaces/{namespace}`                | `s3tables:DeleteNamespace`                                                               | `s3tables:DeleteNamespace`                                                         |
| `listTables`            | `GET /v1/{prefix}/namespaces/{namespace}/tables`            | `s3tables:ListTables`                                                                    | `s3tables:ListTables`                                                              |
| `createTable`           | `POST /v1/{prefix}/namespaces/{namespace}/tables`           | `s3tables:CreateTable`, `s3tables:PutTableData`                                          | `s3tables:CreateTable`, `s3tables:PutObject`                                       |
| `loadTable`             | `GET /v1/{prefix}/namespaces/{namespace}/tables/{table}`    | `s3tables:GetTableMetadataLocation`, `s3tables:GetTableData`                             | `s3tables:GetTableMetadataLocation`, `s3tables:GetObject`                          |
| `updateTable`           | `POST /v1/{prefix}/namespaces/{namespace}/tables/{table}`   | `s3tables:UpdateTableMetadataLocation`, `s3tables:PutTableData`, `s3tables:GetTableData` | `s3tables:UpdateTableMetadataLocation`, `s3tables:PutObject`, `s3tables:GetObject` |
| `dropTable`             | `DELETE /v1/{prefix}/namespaces/{namespace}/tables/{table}` | `s3tables:DeleteTable`                                                                   | `s3tables:DeleteTable`                                                             |
| `renameTable`           | `POST /v1/{prefix}/tables/rename`                           | `s3tables:RenameTable`                                                                   | `s3tables:RenameTable`                                                             |
| `tableExists`           | `HEAD /v1/{prefix}/namespaces/{namespace}/tables/{table}`   | `s3tables:GetTable`                                                                      | `s3tables:GetTable`                                                                |
| `namespaceExists`       | `HEAD /v1/{prefix}/namespaces/{namespace}`                  | `s3tables:GetNamespace`                                                                  | `s3tables:GetNamespace`                                                            | ## Considerations and limitations Following are considerations and limitations when using the Amazon S3 Tables Iceberg REST endpoint. ###### **Considerations** <br>• **CreateTable API behavior** – The `stage-create` option is not supported for this operation, and results in a `400 Bad Request` error. This means you cannot create a table from query results using `CREATE TABLE AS SELECT` (CTAS). <br>• **DeleteTable API behavior** – You can only drop tables with purge enabled. Dropping tables with `purge=false` is not supported and results in a `400 Bad Request` error. Some versions of Spark always set this flag to false even when running `DROP TABLE PURGE` commands. You can try with `DROP TABLE PURGE` or use the S3 Tables [DeleteTable](../API/API_s3TableBuckets_DeleteTable.md "../API/API_s3TableBuckets_DeleteTable.md") operation to delete a table. <br>• The endpoint only supports standard table metadata operations. For table maintenance, such as snapshot management and compaction, use S3 Tables maintenance API operations. For more information, see [S3 Tables maintenance](s3-tables-maintenance-overview.md "s3-tables-maintenance-overview.md"). ###### **Limitations** <br>• Multilevel namespaces are not supported. <br>• OAuth-based authentication is not supported. <br>• Only the `owner` property is supported for namespaces. <br>• View-related APIs defined in the [Apache Iceberg REST Open API specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml "https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml") are not supported. <br>• Running operations on a table with a `metadata.json` file over 5MB is not supported, and will return a `400 Bad Request` error. To control the size of your `metadata.json` files use table maintenance operations. For more information, see [S3 Tables maintenance](s3-tables-maintenance-overview.md "s3-tables-maintenance-overview.md"). |
