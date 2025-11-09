# Connecting to the Data Catalog using AWS Glue Iceberg REST endpoint

AWS Glue's Iceberg REST endpoint supports API operations specified in the Apache Iceberg REST specification.
Using an Iceberg REST client, you can connect your application running on an analytics engine to the REST catalog hosted in the Data Catalog.

The endpoint supports both Apache Iceberg table specifications - v1 and v2, defaulting to
v2. When using the Iceberg table v1 specification, you must specify v1 in the API call. Using
the API operation, you can access Iceberg tables stored in both Amazon S3 object storage and Amazon S3
Table storage.

**Endpoint configuration**

You can access the AWS Glue Iceberg REST catalog using the service endpoint. Refer to
the [AWS Glue
service endpoints reference guide](../../../general/latest/gr/glue.md#glue_region "../../../general/latest/gr/glue.md#glue_region") for the region-specific endpoint. For example,
when connecting to AWS Glue in the us-east-1 Region, you need to configure the endpoint URI property
as follows:

```
Endpoint : https://glue.us-east-1.amazonaws.com/iceberg
```

**Additional configuration properties** – When using
Iceberg client to connect an analytics engine like Spark to the service endpoint, you are
required to specify the following application configuration properties:

```
catalog_name = "mydatacatalog"
aws_account_id = "123456789012"
aws_region = "us-east-1"
spark = SparkSession.builder \
    ... \
    .config("spark.sql.defaultCatalog", catalog_name) \
    .config(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog") \
    .config(f"spark.sql.catalog.{catalog_name}.type", "rest") \
    .config(f"spark.sql.catalog.{catalog_name}.uri", "https://glue.{aws_region}.amazonaws.com/iceberg") \
    .config(f"spark.sql.catalog.{catalog_name}.warehouse", "{aws_account_id}") \
    .config(f"spark.sql.catalog.{catalog_name}.rest.sigv4-enabled", "true") \
    .config(f"spark.sql.catalog.{catalog_name}.rest.signing-name", "glue") \
    .config("spark.sql.extensions","org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .getOrCreate()

```

AWS Glue Iceberg endpoint `https://glue.`us-east-1`.amazonaws.com/iceberg` supports
supports the following Iceberg REST APIs:

- GetConfig
- ListNamespaces
- CreateNamespace
- LoadNamespaceMetadata
- UpdateNamespaceProperties
- DeleteNamespace
- ListTables
- CreateTable
- LoadTable
- TableExists
- UpdateTable
- DeleteTable

## Prefix and catalog path parameters

Iceberg REST catalog APIs have a free-form prefix in their request URLs. For example, the
`ListNamespaces` API call uses the `GET/v1/{prefix}/namespaces` URL
format. AWS Glue prefix always follows the `/catalogs/{catalog}` structure to
ensure that the REST path aligns the AWS Glue multi-catalog hierarchy. The
`{catalog}` path parameter can be derived based on the following rules:

| **Access pattern**                               | **Glue catalog ID Style**   | **Prefix Style**            | **Example default catalog ID** | **Example REST route**                                   |
| ------------------------------------------------ | --------------------------- | --------------------------- | ------------------------------ | -------------------------------------------------------- |
| Access the default catalog in current account    | not required                | :                           | not applicable                 | GET /v1/catalogs/:/namespaces                            |
| Access the default catalog in a specific account | accountID                   | accountID                   | 111122223333                   | GET /v1/catalogs/111122223333/namespaces                 |
| Access a nested catalog in current account       | catalog1/catalog2           | catalog1/catalog2           | rmscatalog1:db1                | GET /v1/catalogs/rmscatalog1:db1/namespaces              |
| Access a nested catalog in a specific account    | accountId:catalog1/catalog2 | accountId:catalog1/catalog2 | 123456789012/rmscatalog1:db1   | GET /v1/catalogs/123456789012:rmscatalog1:db1/namespaces |

This catalog ID to prefix mapping is required only when you directly call the REST APIs.
When you are working with the AWS Glue Iceberg REST catalog APIs through an engine, you need to
specify the AWS Glue catalog ID in the `warehouse` parameter for your Iceberg REST
catalog API setting or in the `glue.id` parameter for your AWS Glue extensions API
setting. For example, see how you can use it with EMR Spark in [Use an Iceberg cluster with Spark](../../../emr/latest/ReleaseGuide/emr-iceberg-use-spark-cluster.md "../../../emr/latest/ReleaseGuide/emr-iceberg-use-spark-cluster.md").

## Namespace path parameter

Namespaces in Iceberg REST catalog APIs path can have multiple levels. However, AWS Glue
only supports single-level namespaces. To access a namespace in a multi-level catalog
hierarchy, you can connect to a multi-level catalog above the namespace to reference the
namespace. This allows any query engine that supports the 3-part notation of
`catalog.namespace.table` to access objects in AWS Glue’s multi-level catalog hierarchy without
compatibility issues compared to using the multi-level namespace.
