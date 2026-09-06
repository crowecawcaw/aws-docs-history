

# Prerequisites to use Apache Iceberg Tables as a destination
<a name="apache-iceberg-prereq"></a>

Choose from the following options to complete the required prerequisites.

**Topics**
+ [Prerequisites to deliver to Iceberg Tables in Amazon S3](#iceberg-tables-prerequisites)
+ [Prerequisites to deliver to Amazon S3 Tables](#s3-tables-prerequisites)

## Prerequisites to deliver to Iceberg Tables in Amazon S3
<a name="iceberg-tables-prerequisites"></a>

Before you begin, complete the following prerequisites.
+ **Create an Amazon S3 bucket** – You must create an Amazon S3 bucket to add metadata file path during tables creation. For more information, see [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
+ **Create an IAM role with required permissions** – Firehose needs an IAM role with specific permissions to access AWS Glue tables and write data to Amazon S3. The same role is used to grant AWS Glue access to Amazon S3 buckets. You need this IAM role when you create an Iceberg Table and a Firehose stream. For more information, see [Grant Firehose access to Amazon S3 Tables](controlling-access.md#using-s3-tables). 
+ **Create Apache Iceberg Tables** – If you are configuring unique keys in the Firehose stream for updates and deletes, Firehose validates if the table and unique keys exist as a part of stream creation. For this scenario, you must create tables before creating the Firehose stream. You can use AWS Glue to create Apache Iceberg Tables. For more information, see [Creating Apache Iceberg tables](https://docs.aws.amazon.com/glue/latest/dg/populate-otf.html#creating-iceberg-tables). If you are not configuring unique keys in the Firehose stream, then you don't require to create Iceberg tables before creating a Firehose stream. 
**Note**  
Firehose supports the following table version and format for Apache Iceberg tables.  
**Table format version** – Firehose only supports [V2 table format](https://iceberg.apache.org/spec/#version-2). Do not create tables in V1 format, else you get an error and data is delivered to the S3 error bucket instead. 
**Data storage format** – Firehose writes data to Apache Iceberg Tables in Parquet format. 
**Row level operation** – Firehose supports the Merge-on-Read (MOR) mode of writing data to Apache Iceberg Tables. 

## Prerequisites to deliver to Amazon S3 Tables
<a name="s3-tables-prerequisites"></a>

To deliver data to Amazon S3 table buckets, complete the following prerequisites.
+ Create an S3 Table bucket, namespace, tables in the table bucket, and other integration steps outlined in [Getting started with Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-getting-started.html). Column names must be lowercase because of the limitations imposed by the S3 Tables catalog integration, as specified in [S3 tables catalog integration limitations](https://docs.aws.amazon.com/lake-formation/latest/dg/notes-s3-catalog.html).
+ **Create an IAM role with required permissions** – Firehose needs an IAM role with specific permissions to access AWS AWS Glue tables and write data to tables in an Amazon S3 table bucket. To write to tables in an Amazon S3 table bucket, you must also provide the IAM role with the required permissions. The permissions required for Amazon S3 Tables catalog depend on the access control mode you use:
  + **IAM access control** – The Firehose delivery role needs IAM permissions directly on Amazon S3 Tables resources.
  + **Lake Formation access control** – The Firehose delivery role needs AWS AWS Lake Formation permissions for managing access to your table resources. AWS Lake Formation uses its own permissions model that enables fine-grained access control for Data Catalog resources.

  You configure this IAM role when you create a Firehose stream. For more information, see [Grant Firehose access to Amazon S3 Tables](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-s3-tables).

For step-by-step integration, refer to the blog [Build a data lake for streaming data with Amazon S3 Tables and Amazon Data Firehose](https://aws.amazon.com/blogs/storage/build-a-data-lake-for-streaming-data-with-amazon-s3-tables-and-amazon-data-firehose/). For additional information, also refer to [Using Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html). 