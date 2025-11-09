# Using AWS Lake Formation with Amazon EMR

Amazon EMR is a flexible AWS managed cluster platform on which you can run any custom
code on supported big data frameworks like Hadoop Map-Reduce, Spark, Hive, Presto, etc.
Organizations also use Amazon EMR to run both batch and stream data processing applications across
a highly distributed cluster. Using Apache Spark on Amazon EMR, you can run your data
transformations and custom code on database and tables whose permissions are managed by
Lake Formation.

There are three options for deploying Amazon EMR:

- EMR on EC2
- EMR Serverless
- Amazon EMR on EKS

For more information, see [Integrate Amazon EMR with Lake Formation](../../../emr/latest/ManagementGuide/emr-lake-formation.md "../../../emr/latest/ManagementGuide/emr-lake-formation.md")
or [Using EMR Serverless with AWS Lake Formation for fine-grained access control](../../../emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable.md "../../../emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable.md")

## Support for transactional table formats

Amazon EMR releases 6.15.0 and higher include support for Lake Formation table, row, column, and
cell-level access control permissions on [Apache Hudi](../../../emr/latest/ReleaseGuide/emr-hudi.md "../../../emr/latest/ReleaseGuide/emr-hudi.md") , [Apache Iceberg](../../../emr/latest/ReleaseGuide/emr-iceberg.md "../../../emr/latest/ReleaseGuide/emr-iceberg.md")
and [Delta
Lake](https://github.com/aws-samples/amazon-emr-with-delta-lake "https://github.com/aws-samples/amazon-emr-with-delta-lake") table formats when you read and write data with Spark SQL.

For limitations, see [Considerations for Amazon EMR with Lake Formation](../../../emr/latest/ManagementGuide/emr-lf-limitations.md "../../../emr/latest/ManagementGuide/emr-lf-limitations.md").

| Supported table formats     | Table format                                                                                                                                                                                                                                                                                                                                                                          | Description and allowed operations                                                            | Lake Formation permissions supported in Amazon EMR |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Apache Hudi                 | A open table format used to simplify incremental data processing and data<br>pipeline development.<br>For a list of supported operations, see [Apache Hudi and<br>Lake Formation](../../../emr/latest/ManagementGuide/hudi-with-lake-formation.md "../../../emr/latest/ManagementGuide/hudi-with-lake-formation.md").                                                                 | Amazon EMR supports table, row, column, and cell-level access control with Apache Hudi.       |
| Apache Iceberg              | An open table format that manages large collections of files as tables.<br>For a list of supported operations, see [Apache Iceberg<br>and Lake Formation](../../../emr/latest/ManagementGuide/iceberg-with-lake-formation.md "../../../emr/latest/ManagementGuide/iceberg-with-lake-formation.md").                                                                                   | Amazon EMR supports table, row, column, and cell-level access control with Apache Iceberg.    |
| Linux Foundation Delta Lake | Delta Lake is an open-source project that helps implement modern data lake<br>architectures commonly built on Amazon S3 or Hadoop Distributed File System (HDFS).<br>For a list of supported operations, see [Delta Lake and<br>Lake Formation](../../../emr/latest/ManagementGuide/delta-with-lake-formation.md "../../../emr/latest/ManagementGuide/delta-with-lake-formation.md"). | Amazon EMR supports table, row, column, and cell-level access control with Delta Lake tables. |

## Additional resources

###### User guide, blog posts, and workshops

- [Integration with Amazon EMR using Runtime Roles](https://catalog.us-east-1.prod.workshops.aws/workshops/78572df7-d2ee-4f78-b698-7cafdb55135d/en-US/emr-runtimerole-integration "https://catalog.us-east-1.prod.workshops.aws/workshops/78572df7-d2ee-4f78-b698-7cafdb55135d/en-US/emr-runtimerole-integration")
- [Get a quick start with Apache Hudi, Apache Iceberg, and Delta Lake with Amazon EMR on
  EKS](https://aws.amazon.com/blogs/big-data/get-a-quick-start-with-apache-hudi-apache-iceberg-and-delta-lake-with-amazon-emr-on-eks/ "https://aws.amazon.com/blogs/big-data/get-a-quick-start-with-apache-hudi-apache-iceberg-and-delta-lake-with-amazon-emr-on-eks/")
- [Using Delta Lake OSS with EMR Serverless](../../../emr/latest/EMR-Serverless-UserGuide/using-delta-lake.md "../../../emr/latest/EMR-Serverless-UserGuide/using-delta-lake.md")
