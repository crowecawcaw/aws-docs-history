For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Using UNLOAD to export query results to S3 from Timestream for LiveAnalytics

Amazon Timestream for LiveAnalytics now enables you to export your query results to Amazon S3 in a cost-effective and
secure way using the `UNLOAD` statement. Using the `UNLOAD` statement,
you can now export time series data to selected S3 buckets in either Apache Parquet or Comma
Separated Values (CSV) format, which provides flexibility to store, combine, and analyze
your time series data with other services. The `UNLOAD` statement allows you to
export the data in a compressed manner, which reduces the data transferred and storage space
required. `UNLOAD` also supports partitioning based on selected attributes when
exporting the data, improving performance and reducing the processing time of downstream
services accessing the data. In addition, you can use Amazon S3 managed keys (SSE-S3) or AWS
Key Management Service (AWS KMS) managed keys (SSE-KMS) to encrypt your exported
data.

## Benefits of UNLOAD from Timestream for LiveAnalytics

The key benefits of using the `UNLOAD` statement are as follows.

- **Operational ease** – With the
  `UNLOAD` statement, you can export gigabytes of data in a single
  query request in either Apache Parquet or CSV format, providing flexibility to
  select the best suited format for your downstream processing needs and making it
  easier to build data lakes.
- **Secure and Cost effective** –
  `UNLOAD` statement provides the capability to export your data to
  an S3 bucket in a compressed manner and to encrypt (SSE-KMS or SSE_S3) your data
  using customer managed keys, reducing the data storage costs and protecting
  against unauthorized access.
- **Performance** – Using the
  `UNLOAD` statement, you can partition the data when exporting to
  an S3 bucket. Partitioning the data enables downstream services to process the
  data in parallel, reducing their processing time. In addition, downstream
  services can process only the data they need, reducing the processing resources
  required and thereby costs associated.

## Use cases for UNLOAD from Timestream for LiveAnalytics

You can use the `UNLOAD` statement to write data to your S3 bucket to the
following.

- **Build Data Warehouse** – You can export
  gigabytes of query results into S3 bucket and more easily add time series data
  into your data lake. You can use services such as Amazon Athena and Amazon
  Redshift to combine your time series data with other relevant data to derive
  complex business insights.
- **Build AI and ML data pipelines** – The
  `UNLOAD` statement enables you to easily build data pipelines for
  your machine learning models that access time series data, making it easier to
  use time series data with services such as Amazon SageMaker and Amazon
  EMR.
- **Simplify ETL Processing** – Exporting
  data into S3 buckets can simplify the process of performing Extract, Transform,
  Load (ETL) operations on the data, enabling you to seamlessly use third-party
  tools or AWS services such as AWS Glue to process and transform the data.
