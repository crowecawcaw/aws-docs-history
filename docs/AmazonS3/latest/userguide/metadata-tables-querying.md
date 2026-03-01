# Querying metadata tables

Your Amazon S3 Metadata tables are stored in an AWS managed S3 table bucket, which provides storage
that's optimized for tabular data. To query your metadata, you can integrate your table bucket with
Amazon SageMaker Lakehouse. This integration, which uses the AWS Glue Data Catalog and AWS Lake Formation, allows AWS analytics services to
automatically discover and access your table data.

After your table bucket is integrated with the AWS Glue Data Catalog, you can directly query your metadata
tables with AWS analytics services such as Amazon Athena, Amazon EMR, and Amazon Redshift. You can also create
interactive dashboards with your query data by using Amazon Quick.

For more information about integrating your AWS managed S3 table bucket with Amazon SageMaker Lakehouse, see [Integrating Amazon S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").

You can also query your metadata tables with Apache Spark, Apache Trino,
and any other application that supports the Apache Iceberg format by using the AWS Glue
Iceberg REST endpoint, Amazon S3 Tables Iceberg REST endpoint, or the Amazon S3
Tables Catalog for Apache Iceberg client catalog. For more information about accessing your
metadata tables, see [Accessing table data](s3-tables-access.md "s3-tables-access.md").

You can analyze your metadata tables with any query engine that supports the Apache
Iceberg format. For example, you can query your metadata tables to do the following:

- Discover storage usage patterns and trends
- Audit AWS Key Management Service (AWS KMS) encryption key usage across your objects
- Search for objects by user-defined metadata and object tags
- Understand object metadata changes over time
- Learn when objects are updated or deleted, including the AWS account ID or IP address that made
  the request
  You can also join S3 managed metadata tables and custom metadata tables, allowing you to query across
  multiple datasets.

## Query pricing considerations

Additional pricing applies for running queries on your metadata tables. For more information, see
pricing information for the query engine that you're using.

For information on making your queries more cost effective, see [Optimizing metadata table query performance](metadata-tables-optimizing-query-performance.md "metadata-tables-optimizing-query-performance.md").

###### Topics

- [Permissions for querying metadata tables](metadata-tables-bucket-query-permissions.md "metadata-tables-bucket-query-permissions.md")
- [Querying metadata tables with AWS analytics services](metadata-tables-bucket-integration.md "metadata-tables-bucket-integration.md")
- [Querying metadata tables with open-source query engines](metadata-tables-bucket-integration-open-source.md "metadata-tables-bucket-integration-open-source.md")
- [Optimizing metadata table query performance](metadata-tables-optimizing-query-performance.md "metadata-tables-optimizing-query-performance.md")
- [Example metadata table queries](metadata-tables-example-queries.md "metadata-tables-example-queries.md")
