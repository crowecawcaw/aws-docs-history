# Connecting to the Data Catalog using AWS Glue Iceberg REST extension endpoint

AWS Glue Iceberg REST extension endpoint provides additional APIs, which are not present in
the Apache Iceberg REST specification, and provides server-side scan planning capabilities.
These additional APIs are used when you access tables stored in Amazon Redshift managed storage. The
endpoint is accessible from an application using Apache Iceberg AWS Glue Data Catalog extensions.

**Endpoint configuration** – A catalog with tables in
the Redshift managed storage is accessible using the service endpoint. Refer to the [AWS Glue service
endpoints reference guide](../../../general/latest/gr/glue.md#glue_region "../../../general/latest/gr/glue.md#glue_region") for the region-specific endpoint. For example, when
connecting to AWS Glue in the us-east-1 Region, you need to configure the endpoint URI property
as follows:

```
Endpoint : https://glue.us-east-1.amazonaws.com/extensions
```

```
catalog_name = "myredshiftcatalog"
aws_account_id = "123456789012"
aws_region = "us-east-1"
spark = SparkSession.builder \
    .config("spark.sql.defaultCatalog", catalog_name) \
    .config(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog") \
    .config(f"spark.sql.catalog.{catalog_name}.type", "glue") \
    .config(f"spark.sql.catalog.{catalog_name}.glue.id", "{123456789012}:redshiftnamespacecatalog/redshiftdb") \
    .config("spark.sql.extensions","org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .getOrCreate()

```
