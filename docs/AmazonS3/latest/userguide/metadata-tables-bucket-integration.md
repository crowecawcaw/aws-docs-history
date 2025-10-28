# Querying metadata tables with AWS analytics

services

You can query your S3 managed metadata tables with AWS analytics services such as Amazon Athena,
Amazon Redshift, and Amazon EMR.

Before you can run queries, you must first [integrate the
AWS managed S3 table buckets](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md") in your AWS account and Region with AWS analytics
services.

## Querying metadata tables with

Amazon Athena

After you [integrate your AWS managed S3 table
buckets](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md") with AWS analytics services, you can start querying your metadata tables in Athena.
In your queries, do the following:

- Specify your catalog as `s3tablescatalog/aws-s3` and your database as
  `b_`general_purpose_bucket_name`` (which is typically the
  namespace for your metadata tables).

- Make sure to surround your metadata table namespace names in quotation marks (`"`)
  or backticks (```), otherwise the query might not work.

For more information, see [Querying Amazon S3 tables with
Athena](s3-tables-integrating-athena.md "s3-tables-integrating-athena.md").

You can also run queries in Athena from the Amazon S3 console.

The following procedure uses the Amazon S3 console to access the Athena query editor so that you can
query a table with Amazon Athena.

###### To query a metadata table

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. On the **General purpose buckets** tab, choose the bucket that contains
   the metadata configuration for the metadata table that you want to query.
4. On the bucket details page, choose the **Metadata** tab.
5. Choose **Query table with Athena**, and then choose one of the sample
   queries for journal or inventory tables.
6. The Amazon Athena console opens and the Athena query editor appears with a sample query loaded
   for you. Modify this query as needed for your use case.

In the query editor, the **Catalog** field should be populated with
**s3tablescatalog/aws-s3**. The
**Database** field should be populated with the namespace where your table
is stored (for example,
**b\_`general-purpose-bucket-name`**).

###### Note

If you don't see these values in the **Catalog** and
**Database** fields, make sure that you've integrated your AWS managed
table bucket with AWS analytics services in this Region. For more information, see [Integrating Amazon S3 Tables with AWS analytics
services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md"). 7. To run the query, choose **Run**.

###### Note

    * If you receive the error **`"Insufficient permissions to execute the query.
     Principal does not have any privilege on specified resource"`** when you try
     to run a query in Athena, you must be granted the necessary Lake Formation permissions on the
     table. For more information, see [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table").


    Also make sure that you have the appropriate AWS Identity and Access Management (IAM) permissions to query
     metadata tables. For more information, see [Permissions for querying metadata
     tables](metadata-tables-bucket-query-permissions.md "metadata-tables-bucket-query-permissions.md").
    * If you receive the error **`"Iceberg cannot access the requested
     resource"`** when you try to run the query, go to the AWS Lake Formation console and
     make sure that you've granted yourself permissions on the table bucket catalog and
     database (namespace) that you created. Don't specify a table when granting these
     permissions. For more information, see [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table").

## Querying metadata tables with

Amazon Redshift

After you [integrate your AWS managed S3 table
buckets](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md") with AWS analytics services, do the following:

- [Create a
  resource link](s3-tables-integrating-aws.md#database-link-tables "s3-tables-integrating-aws.md#database-link-tables") to your metadata table namespace (typically
  `b_`general_purpose_bucket_name``).
- Make sure to surround your metadata table namespace names in quotation marks (`"`)
  or backticks (```), otherwise the query might not work.

After that's done, you can start querying your metadata tables in the Amazon Redshift console. For more
information, see [Accessing Amazon S3 tables with
Amazon Redshift](s3-tables-integrating-redshift.md "s3-tables-integrating-redshift.md").

## Querying metadata tables with

Amazon EMR

To query your metadata tables by using Amazon EMR, you create an Amazon EMR cluster configured for
Apache Iceberg and connect to your metadata tables using Apache Spark.
You can set this up by integrating your AWS managed S3 table buckets with AWS analytics services
or using the open-source Amazon S3 Tables Catalog for Iceberg client catalog.

###### Note

When using Apache Spark on Amazon EMR or other third-party engines to query your
metadata tables, we recommend that you use the Amazon S3 Tables Iceberg REST endpoint.
Your query might not run successfully if you don't use this endpoint. For more information, see
[Accessing tables using the Amazon S3 Tables Iceberg REST endpoint](s3-tables-integrating-open-source.md "s3-tables-integrating-open-source.md").

For more information, see [Accessing Amazon S3 tables with
Amazon EMR](s3-tables-integrating-emr.md "s3-tables-integrating-emr.md").
