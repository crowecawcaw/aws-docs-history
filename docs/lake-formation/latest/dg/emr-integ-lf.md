

# Using AWS Lake Formation with Amazon EMR
<a name="emr-integ-lf"></a>

 Amazon EMR is a flexible AWS managed cluster platform on which you can run any custom code on supported big data frameworks like Hadoop Map-Reduce, Spark, Hive, Presto, etc. Organizations also use Amazon EMR to run both batch and stream data processing applications across a highly distributed cluster. Using Apache Spark on Amazon EMR, you can run your data transformations and custom code on database and tables whose permissions are managed by Lake Formation.

There are three options for deploying Amazon EMR:
+ EMR on EC2
+  EMR Serverless 
+  Amazon EMR on EKS 

 For more information, see [Integrate Amazon EMR with Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lake-formation.html) or [Using EMR Serverless with AWS Lake Formation for fine-grained access control](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable.html) 

## Support for transactional table formats
<a name="tables-emr"></a>

 Amazon EMR releases 6.15.0 and higher include support for Lake Formation table, row, column, and cell-level access control permissions on [Apache Hudi ](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hudi.html), [Apache Iceberg](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg.html) and [Delta Lake](https://github.com/aws-samples/amazon-emr-with-delta-lake) table formats when you read and write data with Spark SQL. 

For limitations, see [Considerations for Amazon EMR with Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-limitations.html).


**Supported table formats**  

| Table format | Description and allowed operations | Lake Formation permissions supported in Amazon EMR | 
| --- | --- | --- | 
| Apache Hudi | A open table format used to simplify incremental data processing and data pipeline development.<br />For a list of supported operations, see [Apache Hudi and Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/hudi-with-lake-formation.html). | Amazon EMR supports table, row, column, and cell-level access control with Apache Hudi. | 
| Apache Iceberg | An open table format that manages large collections of files as tables.<br />For a list of supported operations, see [Apache Iceberg and Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/iceberg-with-lake-formation.html). | Amazon EMR supports table, row, column, and cell-level access control with Apache Iceberg. | 
| Linux Foundation Delta Lake | Delta Lake is an open-source project that helps implement modern data lake architectures commonly built on Amazon S3 or Hadoop Distributed File System (HDFS).<br />For a list of supported operations, see [Delta Lake and Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/delta-with-lake-formation.html). | Amazon EMR supports table, row, column, and cell-level access control with Delta Lake tables. | 

## Additional resources
<a name="add-resources-EMR"></a>

**User guide, blog posts, and workshops**
+ [ Integration with Amazon EMR using Runtime Roles](https://catalog.us-east-1.prod.workshops.aws/workshops/78572df7-d2ee-4f78-b698-7cafdb55135d/en-US/emr-runtimerole-integration)
+  [Get a quick start with Apache Hudi, Apache Iceberg, and Delta Lake with Amazon EMR on EKS](https://aws.amazon.com/blogs/big-data/get-a-quick-start-with-apache-hudi-apache-iceberg-and-delta-lake-with-amazon-emr-on-eks/)
+  [Using Delta Lake OSS with EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-delta-lake.html) 