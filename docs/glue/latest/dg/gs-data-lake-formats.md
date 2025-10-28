#

Using Data Lake frameworks with AWS Glue Studio

##

Overview

Open source data lake frameworks simplify incremental data processing for files stored in data lakes built on
Amazon S3. AWS Glue 3.0 and later supports the following open-source data lake storage frameworks:

- Apache Hudi
- Linux Foundation Delta Lake
- Apache Iceberg

As of AWS Glue 4.0, AWS Glue provides native support for these frameworks so that you can read and
write data that you store in
Amazon S3 in a transactionally consistent manner. There's no need to install a separate connector or complete extra configuration
steps in order to use these frameworks in AWS Glue jobs.

Data Lake frameworks can be used as a source or a target within AWS Glue Studio through Spark Script Editor jobs.
For more information on using Apache Hudi, Apache Iceberg and Delta Lake see:
[Using data lake frameworks with AWS Glue ETL jobs](aws-glue-programming-etl-datalake-native-frameworks.md "aws-glue-programming-etl-datalake-native-frameworks.md").

## Creating open table formats from an AWS Glue Streaming source

AWS Glue streaming ETL jobs continuously consume data from streaming sources, clean and transform the data in-flight, and make it available for analysis in seconds.

AWS offers a broad selection of services to support your needs. A database replication service such as AWS Database Migration Service can replicate the data from your source systems to Amazon S3, which commonly hosts the storage layer of the data lake. Although it’s straightforward to apply updates on a relational database management system (RDBMS) that backs an online source application, it's difficult to apply this CDC process on your data lakes. The open-source data management frameworks simplify incremental data processing and data pipeline development, and are a good option to solve this problem.

For more information, see:

- [Create an Apache Hudi-based near-real-time transactional data lake using AWS Glue Streaming](https://aws.amazon.com/blogs/big-data/create-an-apache-hudi-based-near-real-time-transactional-data-lake-using-aws-dms-amazon-kinesis-aws-glue-streaming-etl-and-data-visualization-using-amazon-quicksight/ "https://aws.amazon.com/blogs/big-data/create-an-apache-hudi-based-near-real-time-transactional-data-lake-using-aws-dms-amazon-kinesis-aws-glue-streaming-etl-and-data-visualization-using-amazon-quicksight/")
- [Build a real-time GDPR-aligned Apache Iceberg data lake](https://aws.amazon.com/blogs/big-data/build-a-real-time-gdpr-aligned-apache-iceberg-data-lake/ "https://aws.amazon.com/blogs/big-data/build-a-real-time-gdpr-aligned-apache-iceberg-data-lake/")
