# Querying metadata tables with

open-source query engines

You can query your S3 managed metadata tables by using open-source query engines, such as
Apache Spark. When using Apache Spark on Amazon EMR or other third-party
engines to query your metadata tables, we recommend that you use the Amazon S3 Tables Iceberg
REST endpoint. Your query might not run successfully if you don't use this endpoint. For more
information, see [Accessing tables using the Amazon S3 Tables Iceberg REST endpoint](s3-tables-integrating-open-source.md "s3-tables-integrating-open-source.md").
