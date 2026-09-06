

# Working with Amazon OpenSearch Service direct queries
<a name="direct-query"></a>

Use Amazon OpenSearch Service direct query to analyze data in Amazon CloudWatch Logs, Amazon S3, Amazon Security Lake, and Amazon Managed Service for Prometheus without building ingestion pipelines. This zero-ETL integration lets you query data in place using PromQL, PPL, or SQL, and explore it in **Discover**.

To get started with Amazon Managed Service for Prometheus, CloudWatch Logs, or Security Lake, configure your data source in the [AWS Management Console](https://console.aws.amazon.com/aos/home#opensearch/data-sources). For Amazon S3, use domain connections and create tables with SQL in Query Workbench. CloudWatch Logs and Security Lake use preconfigured data sources and schema. For Amazon S3 and Security Lake, data is cataloged using AWS Glue Data Catalog tables—Amazon S3 requires you to create these tables manually, while Security Lake configures them automatically as part of the ingestion process.