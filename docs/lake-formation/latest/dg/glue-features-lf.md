# Using AWS Lake Formation with AWS Glue

Data engineers and DevOps professionals use AWS Glue with Extract, Transform and Load
(ETL) with Apache Spark to perform transformations on their data sets in Amazon S3 and load the
transformed data into data lakes and data warehouses for analytics, machine learning, and
application development. With different teams accessing the same data set in Amazon S3, it is
imperative to grant and restrict permissions based on their roles.

AWS Lake Formation is built on AWS Glue, and the services interact in the following ways:

- Lake Formation and AWS Glue share the same Data Catalog.
- The following Lake Formation console features invoke the AWS Glue console:
  - Jobs – For more information, see [Adding
    Jobs](../../../glue/latest/dg/add-job.md "../../../glue/latest/dg/add-job.md") in the _AWS Glue Developer Guide_.
  - Crawlers – For more information, see [Cataloging Tables with a Crawler](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") in the
    _AWS Glue Developer Guide_.

- The workflows generated when you use a Lake Formation blueprint are AWS Glue workflows. You can view
  and manage these workflows in both the Lake Formation console and the AWS Glue console.
- Machine learning transforms are provided with Lake Formation and are built on AWS Glue API
  operations. You create and manage machine learning transforms on the AWS Glue console. For more
  information, see [Machine Learning
  Transforms](../../../glue/latest/dg/machine-learning.md "../../../glue/latest/dg/machine-learning.md") in the _AWS Glue Developer Guide_.
  You can use the Lake Formation fine-grained access control to manage your existing Data Catalog resources and Amazon S3 data locations.

###### Note

AWS Glue 5.0 or higher supports fine-grained access controls on Iceberg and Hive tables
that are backed by S3. This capability lets you configure table, row, column, and cell level
access controls for read queries within your AWS Glue for Apache Spark jobs.

## Support for transactional table types

Applying Lake Formation permissions allows you to secure your transactional data in your Amazon S3 based data lakes. The table below lists transactional table formats supported in AWS Glue and the Lake Formation permissions. Lake Formation enforces these permissions for AWS Glue operations.

| Supported table formats     | Table format                                                                                                                                                                                                                                                                                                                                                                        | Description and allowed operations                                                                                                                                                                                                                                                                                                     | Lake Formation permissions supported in AWS Glue |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Apache Hudi                 | A open table format used to simplify incremental data processing and data<br>pipeline development.<br>For examples, see [Using the Hudi framework in AWS Glue](../../../glue/latest/dg/aws-glue-programming-etl-format-hudi.md "../../../glue/latest/dg/aws-glue-programming-etl-format-hudi.md").                                                                                  | Table-level permissions are available for Hudi tables.<br>For more information, see [Limitations](../../../glue/latest/dg/security-lf-enable.md "../../../glue/latest/dg/security-lf-enable.md").                                                                                                                                      |
| Apache Iceberg              | An open table format that manages large collections of files as tables.<br>For examples, see [Using the Iceberg framework in AWS Glue](../../../glue/latest/dg/aws-glue-programming-etl-format-iceberg.md "../../../glue/latest/dg/aws-glue-programming-etl-format-iceberg.md").                                                                                                    | AWS Glue version 5.0 and higher lets you configure table, row, column, and cell<br>level access controls for read queries within your AWS Glue for Apache Spark jobs for<br>Iceberg tables.<br>For more information, see [Limitations](../../../glue/latest/dg/security-lf-enable.md "../../../glue/latest/dg/security-lf-enable.md"). |
| Linux Foundation Delta Lake | Delta Lake is an open-source project that helps implement modern data lake<br>architectures commonly built on Amazon S3 or Hadoop Distributed File System (HDFS).<br>For examples, see [Using the Delta Lake framework in AWS Glue](../../../glue/latest/dg/aws-glue-programming-etl-format-delta-lake.md "../../../glue/latest/dg/aws-glue-programming-etl-format-delta-lake.md"). | Table-level permissions are available for Delta Lake tables.<br>For more information, see [Limitations](../../../glue/latest/dg/security-lf-enable-considerations.md "../../../glue/latest/dg/security-lf-enable-considerations.md").                                                                                                  |

## Additional resources

###### Blog posts and repositories

- [Use the AWS Glue connector to read and write Apache Iceberg tables with ACID transactions and perform time travel](https://aws.amazon.com/blogs/big-data/use-the-aws-glue-connector-to-read-and-write-apache-iceberg-tables-with-acid-transactions-and-perform-time-travel/ "https://aws.amazon.com/blogs/big-data/use-the-aws-glue-connector-to-read-and-write-apache-iceberg-tables-with-acid-transactions-and-perform-time-travel/")
- [Writing to Apache Hudi tables using AWS Glue custom connector](https://aws.amazon.com/blogs/big-data/writing-to-apache-hudi-tables-using-aws-glue-connector/ "https://aws.amazon.com/blogs/big-data/writing-to-apache-hudi-tables-using-aws-glue-connector/")
- AWS repository of [Cloudformation template and pyspark code sample](https://github.com/aws-samples/aws-glue-streaming-etl-with-apache-hudi "https://github.com/aws-samples/aws-glue-streaming-etl-with-apache-hudi")
  to analyze streaming data using AWS Glue, Apache Hudi, and Amazon S3.
