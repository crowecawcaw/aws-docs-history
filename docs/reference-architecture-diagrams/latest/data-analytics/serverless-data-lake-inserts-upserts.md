

# Managing inserts and upserts in a serverless data lake
<a name="serverless-data-lake-inserts-upserts"></a>

Publication date: **June 15, 2021 ([Diagram history](diagram-history.md))**

This architecture shows how to use Apache Hudi running on Amazon EMR to process inserts and updates to datasets in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). You can build a cost-effective and scalable data lake that provisions on-demand analytics and creates persistent data marts.

## Managing inserts and upserts in a serverless data lake diagram
<a name="serverless-data-lake-inserts-upserts-diagram1"></a>

![Raw data lands in Amazon S3, AWS Glue catalogs it, and Amazon EMR runs inserts and upserts into processed Amazon S3 layers.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/serverless-data-lake-inserts-upserts.png)


The following steps describe the architecture:

1. Ingest data from source systems using batch, change data capture (CDC), or streaming into the raw layer in Amazon S3.

1. After the data persists in the raw data lake on Amazon S3, crawl the data and populate it in the [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) Data Catalog using a crawler.

1. Pull raw data into an Amazon EMR cluster and read it using Hive and Spark for cleaning and transformation.

1. Apache Hudi running on Amazon EMR reads the data using Spark APIs and performs inserts and upserts on the required datasets.

1. Persist the cleaned and transformed data back into the Amazon S3 processed and reportable buckets.

1. Consume the reportable data on demand using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) or load it into [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/). Different users, tools, and resources can consume this data.

1. Handle the complete data movement, spin on-demand Amazon EMR clusters for batch data, and load the data using workflow orchestration with [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/) (MWAA).

## Further reading
<a name="serverless-data-lake-inserts-upserts-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)