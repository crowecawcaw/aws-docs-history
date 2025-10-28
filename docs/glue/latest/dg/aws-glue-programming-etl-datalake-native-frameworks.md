# Using data lake

frameworks with AWS Glue ETL jobs

Open-source data lake frameworks simplify incremental data processing for files that you
store in data lakes built on Amazon S3. AWS Glue 3.0 and later supports the following
open-source data lake frameworks:

- Apache Hudi
- Linux Foundation Delta Lake
- Apache Iceberg
  We provide native support for these frameworks so that you can read and write data that
  you store in Amazon S3 in a transactionally consistent manner. There's no need to install a
  separate connector or complete extra configuration steps in order to use these frameworks in
  AWS Glue ETL jobs.

When you manage datasets through the AWS Glue Data Catalog, you can use AWS Glue methods to read and
write data lake tables with Spark DataFrames. You can also read and write Amazon S3
data using the Spark DataFrame API.

In this video, you can learn about the basics of how Apache Hudi, Apache Iceberg, and Delta Lake work. You'll see how to insert, update, and delete data in your data lake and how each of these frameworks works.

###### Topics

- [Limitations](aws-glue-programming-etl-datalake-native-frameworks-limitations.md "aws-glue-programming-etl-datalake-native-frameworks-limitations.md")
- [Using the Hudi framework in
  AWS Glue](aws-glue-programming-etl-format-hudi.md "aws-glue-programming-etl-format-hudi.md")
- [Using the Delta Lake framework
  in AWS Glue](aws-glue-programming-etl-format-delta-lake.md "aws-glue-programming-etl-format-delta-lake.md")
- [Using the Iceberg framework in
  AWS Glue](aws-glue-programming-etl-format-iceberg.md "aws-glue-programming-etl-format-iceberg.md")
