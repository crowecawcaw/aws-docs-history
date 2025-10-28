# Working with Amazon S3 Tables in the lakehouse architecture of Amazon SageMaker

[Amazon S3
Tables](../../../AmazonS3/latest/userguide/s3-tables.md "../../../AmazonS3/latest/userguide/s3-tables.md") provide S3 storage that's specifically optimized for analytics workloads,
improving query performance while reducing costs. The data in S3 Tables is stored in a new
bucket type: a _table bucket_, which stores tables as
subresources. S3 tables have built-in support for Apache Iceberg standard, which allows you to
easily query tabular data in Amazon S3 table buckets using popular query engines like Apache
Spark.

You can integrate Amazon S3 table buckets and tables with AWS Glue Data Catalog (Data Catalog), and register
the catalog as a Lake Formation data location from the Lake Formation console or using service APIs. When your
organization manages data in the Data Catalog, and register the data location with Lake Formation, you can
use Lake Formation to control access to your datasets.

You can apply Lake Formation permissions using tag-based access control and the named
resource method on the federated databases, and share them across multiple AWS accounts, AWS
Organizations, and organizational units (OUs). You can also share the federated databases
directly with IAM principals from another account.

For more information, see [Using Amazon S3 Tables with AWS
analytics services](../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md") in the Amazon Simple Storage Service User Guide.

## Enable Amazon S3 integration

Before creating Amazon S3 Tables in Amazon SageMaker Unified Studio, you must first enable the integration between Amazon S3 Tables and AWS analytics services.

###### Enable S3 integration

1. Navigate to the [Amazon S3 console](https://console.aws.amazon.com/s3 "https://console.aws.amazon.com/s3"). In the left navigation pane, choose **Table buckets**.
2. Choose **Create table bucket**.
3. On the **Create table bucket** page, enter a **Table bucket name** and select **Enable integration**.
4. Choose **Create table bucket**.
5. Amazon S3 displays confirmation when integration of your table buckets with the lakehouse architecture completes.

When you enable the integration, Amazon S3 takes the following actions on your behalf:

- Creates a new service role that gives Lake Formation access to all your tables and table buckets in your current Region. This allows Lake Formation to manage access, permissions, and governance for all current and future table buckets in that Region.
- Creates the `S3tablescatalog` in the AWS Glue Data Catalog in your current Region.

## Onboard S3 Tables in the lakehouse architecture

To provide access to S3 tables from Amazon SageMaker Unified Studio, you must grant permissions through Lake Formation.

###### Grant Lake Formation permissions

1. Navigate to the [Lake Formation console](http://console.aws.amazon.com/lakeformation "http://console.aws.amazon.com/lakeformation").
2. In the left navigation pane, choose **Catalogs** and choose **S3tablescatalog**.
3. From **S3tablescatalog**, under **Objects**, choose your newly created **table bucket**.
4. From the **Actions** menu, select **Grant**.
5. In **Grant permissions**, under IAM users and roles, select your Amazon SageMaker Unified Studio Project role.
6. To grant full access, under **Catalog Permissions > Grant**, select **Super user**.

## Integrate Amazon S3 tables with the lakehouse architecture using CLI

1. Register the S3 Tables catalog as a Lake Formation data location.

```
aws lakeformation register-resource \
  --resource-arn 'arn:aws:s3tables:us-east-1:123456789012:bucket/*' \
  --role-arn 'arn:aws:iam::123456789012:role/LakeFormationDataAccessRole' \
  --with-federation
  --with-privileged-access
```

2. Create a catalog.

```
aws glue create-catalog --cli-input-json file://input.json

'{
   "Name": `"s3tablescatalog"`,
   "CatalogInput" : {
      "FederatedCatalog": {
         "Identifier": "arn:aws:s3tables:us-east-1:123456789012:bucket/*",
         "ConnectionName": "aws:s3tables"
      },
      "CreateDatabaseDefaultPermissions": [],
      "CreateTableDefaultPermissions": []
   }
}'

```

## Creating S3 tables catalog in the lakehouse architecture

You can create Amazon S3 table buckets in the lakehouse architecture of Amazon SageMaker as a new data source within Amazon SageMaker Unified Studio. Amazon S3 Tables provide S3 storage optimized for analytics workloads. They include built-in Apache Iceberg support and features designed to continuously improve query performance and reduce storage costs for tables.

Data in S3 Tables is stored in table buckets, which are specialized buckets for storing tabular data. For additional details, see [Working with Amazon S3 Tables and table buckets](../../../AmazonS3/latest/userguide/s3-tables.md "../../../AmazonS3/latest/userguide/s3-tables.md").

To get started using S3 Tables in Amazon SageMaker Unified Studio, create a new Lakehouse catalog with S3 table bucket source.

###### Create S3 Tables catalog

1. Open the Amazon SageMaker console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") and use the Region selector in the top navigation bar to choose the appropriate AWS Region.
2. Select your Amazon SageMaker domain.
3. Select the project you want to create a table bucket in.
4. In the navigation menu select **Data**, then select **+** to add a new data source.
5. Select **Create Lakehouse catalog**.
6. In the add catalog menu, choose **Amazon S3 Tables** as the source.
7. Enter a name for the catalog, and a database name.
8. Choose **Create catalog**.

This creates the following resources in your account:

    * A new S3 Table bucket and the corresponding AWS Glue child catalog under the parent catalog `s3tablescatalog`.
    * A new database within that AWS Glue Data Catalog child catalog. The database name matches the database name you provided. In S3 tables, this is the table namespace.

9. Begin creating tables in your database and querying them using query editor or Jupyter notebook.

## Creating and querying Amazon S3 Tables

After setting up your Amazon S3 Tables integration and catalog, you can create databases, tables, and query data using SQL commands in Amazon SageMaker Unified Studio.

###### Create S3 Table and add data in the lakehouse architecture

1. Navigate to Amazon SageMaker Unified Studio, and select the project.
2. From the **Build** menu, select **Query Editor**, and ensure you have **Amazon Athena** selected in **Connections**.
3. Create a database using SQL.

```
CREATE DATABASE "s3tablescatalog/`amzn-s3-demo-bucket".YourDBName`;
```

4. Create an Amazon S3 table using SQL.

```
CREATE TABLE "s3tablescatalog/`amzn-s3-demo-bucket".YourDBName.YourTableName`;
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
INSERT INTO "s3tablescatalog/`amzn-s3-demo-bucket".YourDBName.YourTableName`
VALUES('Dr.','1381546','Joyce','Deaton','Joyce.Deaton@example.edu');
```

You can now use the following integrated analytics services with your Amazon S3 Tables:

- [Amazon Athena](../../../AmazonS3/latest/userguide/s3-tables-integrating-athena.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-athena.md") - create databases, tables, query and add data in Amazon S3 Tables.
- [Amazon Redshift](../../../AmazonS3/latest/userguide/s3-tables-integrating-redshift.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-redshift.md") - query data from Amazon S3 Tables.
- [Amazon EMR](../../../AmazonS3/latest/userguide/s3-tables-integrating-emr.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-emr.md") - create table, namespace, query and add data in Amazon S3 Tables.
- [AWS Glue](../../../AmazonS3/latest/userguide/s3-tables-integrating-glue.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-glue.md") - create table, namespace, query and add data in Amazon S3 Tables.
- [Lake Formation](../../../lake-formation/latest/dg/create-s3-tables-catalog.md "../../../lake-formation/latest/dg/create-s3-tables-catalog.md") - grant fine-grained permissions for Amazon S3 table catalogs, databases, tables, columns, and cells.
