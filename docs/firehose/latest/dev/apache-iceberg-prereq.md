# Prerequisites to use Apache Iceberg Tables as a

destination

Choose from the following options to complete the required prerequisites.

###### Topics

- [Prerequisites to deliver to Iceberg
  Tables in Amazon S3](#iceberg-tables-prerequisites "#iceberg-tables-prerequisites")
- [Prerequisites to deliver to Amazon S3
  Tables](#s3-tables-prerequisites "#s3-tables-prerequisites")

## Prerequisites to deliver to Iceberg

Tables in Amazon S3

Before you begin, complete the following prerequisites.

- **Create an Amazon S3 bucket** – You must
  create an Amazon S3 bucket to add metadata file path during tables creation. For more
  information, see [Create an S3
  bucket](../../../AmazonS3/latest/userguide/creating-bucket.md "../../../AmazonS3/latest/userguide/creating-bucket.md").
- **Create an IAM role with required permissions**
  – Firehose needs an IAM role with specific permissions to access AWS Glue
  tables and write data to Amazon S3. The same role is used to grant AWS Glue access
  to Amazon S3 buckets. You need this IAM role when you create an Iceberg Table and
  a Firehose stream. For more information, see [Grant Firehose access to Amazon S3 Tables](controlling-access.md#using-s3-tables "controlling-access.md#using-s3-tables").
- **Create Apache Iceberg Tables** – If you
  are configuring unique keys in the Firehose stream for updates and deletes, Firehose
  validates if the table and unique keys exist as a part of stream creation. For
  this scenario, you must create tables before creating the Firehose stream. You can
  use AWS Glue to create Apache Iceberg Tables. For more information, see [Creating
  Apache Iceberg tables](../../../glue/latest/dg/populate-otf.md#creating-iceberg-tables "../../../glue/latest/dg/populate-otf.md#creating-iceberg-tables"). If you are not configuring unique keys in the
  Firehose stream, then you don't require to create Iceberg tables before creating a
  Firehose stream.

###### Note

Firehose supports the following table version and format for Apache Iceberg
tables.

    + **Table format version** –
     Firehose only supports [V2 table
     format](https://iceberg.apache.org/spec/#version-2 "https://iceberg.apache.org/spec/#version-2"). Do not create tables in V1 format, else you
     get an error and data is delivered to the S3 error bucket
     instead.
    + **Data storage format** –
     Firehose writes data to Apache Iceberg Tables in Parquet format.
    + **Row level operation** –
     Firehose supports the Merge-on-Read (MOR) mode of writing data to
     Apache Iceberg Tables.

## Prerequisites to deliver to Amazon S3

Tables

To deliver data to Amazon S3 table buckets, complete the following
prerequisites.

- Create an S3 Table bucket, namespace, tables in the table bucket, and
  other integration steps outlined in [Getting started with Amazon S3 Tables](../../../AmazonS3/latest/userguide/s3-tables-getting-started.md "../../../AmazonS3/latest/userguide/s3-tables-getting-started.md"). Column names must be
  lowercase because of the limitations imposed by the S3 Tables catalog
  integration, as specified in [S3 tables catalog integration limitations](../../../lake-formation/latest/dg/notes-s3-catalog.md "../../../lake-formation/latest/dg/notes-s3-catalog.md").
- **Create an IAM role with required permissions** –
  Firehose needs an IAM role with specific permissions to access AWS Glue tables and
  write data to tables in an Amazon S3 table bucket. To write to tables in an S3
  table bucket, you must also provide the IAM role with the required
  permissions in AWS Lake Formation. You configure this IAM role
  when you create a Firehose stream. For more information, see [Grant Firehose access to Amazon S3 Tables](controlling-access.md#using-s3-tablesusing-iam-iceberg "controlling-access.md#using-s3-tablesusing-iam-iceberg").
- **Configure AWS Lake Formation permissions**
  – AWS Lake Formation manages access to your table
  resources. Lake Formation uses its own [permissions model](../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md#grant-permissions-tables "../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md#grant-permissions-tables") that enables fine-grained access control for
  Data Catalog resources.

For step-by-step integration, refer to the blog [Build a data lake for streaming data with Amazon S3 Tables and Amazon Data Firehose](https://aws.amazon.com/blogs/storage/build-a-data-lake-for-streaming-data-with-amazon-s3-tables-and-amazon-data-firehose/ "https://aws.amazon.com/blogs/storage/build-a-data-lake-for-streaming-data-with-amazon-s3-tables-and-amazon-data-firehose/").
For additional information, also refer to [Using Amazon S3 Tables with AWS analytics services](../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md").
