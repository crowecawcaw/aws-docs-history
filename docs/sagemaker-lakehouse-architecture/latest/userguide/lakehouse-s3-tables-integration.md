# Amazon S3 tables integration

The lakehouse architecture unifies all your data across Amazon S3 data lakes, Amazon Redshift data warehouses, and
third-party data sources without having to copy data. Amazon S3 Tables delivers the first cloud
object store with built-in Apache Iceberg support. The lakehouse architecture integrates with Amazon S3 Tables
so you can access S3 Tables from AWS analytics services, such as Amazon Redshift, Athena, Amazon EMR,
AWS Glue, or Apache Iceberg-compatible engines (Apache Spark or PyIceberg).

The lakehouse architecture integration with Amazon S3 Tables helps you secure analytic workflows by
joining data from Amazon S3 Tables with sources, such as Amazon Redshift data warehouses,
third-party, and federated data sources (Amazon DynamoDB or PostgreSQL). The lakehouse architecture also
enables centralized management of fine-grained data access permissions for S3 Tables and
other data, and consistently applies them across all engines. To get started, complete the
steps in the following sections.

**Prerequisites** - complete all the steps in the [Getting started with the lakehouse architecture of Amazon SageMaker](lakehouse-get-started.md "lakehouse-get-started.md").

###### Enable Amazon S3 integration

1. Navigate to the [Amazon S3
   console](https://console.aws.amazon.com/s3 "https://console.aws.amazon.com/s3"). In the left navigation pane, choose **Table
   buckets**.
2. Choose **Create table bucket**.
3. On the **Create table bucket** page, enter a **Table bucket
   name** and select **Enable integration**.
4. Choose **Create table bucket**.
5. You will see confirmation when Amazon S3 completes integration of your table buckets with
   the lakehouse architecture.

###### Onboard S3 Tables in the lakehouse architecture

To provide access to S3 tables, complete the following steps:

1. Navigate to the [AWS Lake
   Formation](http://console.aws.amazon.com/lakeformation "http://console.aws.amazon.com/lakeformation") console.
2. In the left navigation pane, choose **Catalogs** and choose
   **S3tablescatalog**.
3. From **S3tablescatalog**, under **Objects**,
   choose the name of your newly created **table bucket**.
4. From the **Actions** menu, select
   **Grant**.
5. In the **Grant permissions**, under IAM users and roles, select
   your Amazon SageMaker Unified Studio Project role. To grant full access, under
   **Catalog Permissions > Grant**, select **Super
   user**.

###### Create S3 Table and add data in the lakehouse architecture

1. Navigate to Amazon SageMaker Unified Studio, and select the project.
2. From the **Build** menu, select **Query Editor**,
   and ensure you have **Athena** selected in
   **Connections**.
3. Create a database using SQL.

```

CREATE DATABASE "s3tablescatalog/<Your Bucket Name>".<YourDBName>;

```

4. Create an S3 table using SQL.

```

CREATE TABLE "s3tablescatalog/<Your Bucket Name>".<YourDBName>.<YourTableName>
( c_salutation string,
  c_login string,
  c_first_name string,
  c_last_name string,
  c_email_address string)
  TBLPROPERTIES (
  'table_type'='ICEBERG'  );

```

5. Add data using SQL.

```

INSERT INTO "s3tablescatalog/<Your Bucket Name>".<YourDBName>.<YourTableName>
 VALUES('Dr.','1381546','Joyce','Deaton','Joyce.Deaton@qhtrwert.edu');

```

You can now use the following integrated analytics services:

- [Amazon Athena](../../../AmazonS3/latest/userguide/s3-tables-integrating-athena.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-athena.md") - create databases, tables, query and add data in S3
  Tables.
- [Amazon Redshift](../../../AmazonS3/latest/userguide/s3-tables-integrating-redshift.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-redshift.md") - query data from S3 Tables.
- [Amazon EMR](../../../AmazonS3/latest/userguide/s3-tables-integrating-emr.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-emr.md") - create table, namespace, query and add data in S3 Tables.
- [AWS Glue](../../../AmazonS3/latest/userguide/s3-tables-integrating-glue.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-glue.md") - create table, namespace, query and add data in S3 Tables.
- [AWS Lake Formation](../../../lake-formation/latest/dg/create-s3-tables-catalog.md "../../../lake-formation/latest/dg/create-s3-tables-catalog.md") - grant fine-grained permissions for S3 table catalogs,
  databases, tables, columns, and cells.

###### Note

Access to S3 Tables with the lakehouse architecture is available in the [AWS Regions](../../../AmazonS3/latest/userguide/s3-tables-regions-quotas.md "../../../AmazonS3/latest/userguide/s3-tables-regions-quotas.md") where S3 Tables are available.
