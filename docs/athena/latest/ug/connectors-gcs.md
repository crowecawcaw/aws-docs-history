# Amazon Athena Google Cloud Storage connector

The Amazon Athena Google Cloud Storage connector enables Amazon Athena to run queries on Parquet
and CSV files stored in a Google Cloud Storage (GCS) bucket. After you group one or more
Parquet or CSV files in an unpartitioned or partitioned folder in a GCS bucket, you can
organize them in an [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/") database table.

This connector can be registered with Glue Data Catalog as a federated catalog.
It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

If you have Lake Formation enabled in your account, the IAM role for your Athena federated Lambda connector that you deployed in the AWS Serverless Application Repository must have read access in Lake Formation to the AWS Glue Data Catalog.

For an article that shows how to use Athena to run queries on Parquet or CSV files in a GCS
bucket, see the AWS Big Data Blog post [Use
Amazon Athena to query data stored in Google Cloud Platform](https://aws.amazon.com/blogs/big-data/use-amazon-athena-to-query-data-stored-in-google-cloud-platform/ "https://aws.amazon.com/blogs/big-data/use-amazon-athena-to-query-data-stored-in-google-cloud-platform/").

## Prerequisites

- Set up an AWS Glue database and table that correspond to your bucket and folders
  in Google Cloud Storage. For the steps, see [Setting up
  databases and tables in AWS Glue](#connectors-gcs-setting-up-databases-and-tables-in-glue "#connectors-gcs-setting-up-databases-and-tables-in-glue")
  later in this document.
- Deploy the connector to your AWS account using the Athena console or the AWS Serverless Application Repository. For more information, see [Create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md") or [Use the AWS Serverless Application Repository to deploy a data
  source connector](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md").

## Limitations

- Write DDL operations are not supported.
- Any relevant Lambda limits. For more information, see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md") in the _AWS Lambda Developer Guide_.
- Currently, the connector supports only the `VARCHAR` type for
  partition columns (`string` or `varchar` in an AWS Glue table
  schema). Other partition field types raise errors when you query them in
  Athena.

## Terms

The following terms relate to the GCS connector.

- Handler – A Lambda handler that accesses
  your GCS bucket. A handler can be for metadata or for data
  records.
- Metadata handler – A Lambda handler that
  retrieves metadata from your GCS bucket.
- Record handler – A Lambda handler that
  retrieves data records from your GCS bucket.
- Composite handler – A Lambda handler that
  retrieves both metadata and data records from your GCS bucket.

## Supported file types

The GCS connector supports the Parquet and CSV file types.

###### Note

Make sure you do not place both CSV and Parquet files in the same GCS bucket or
path. Doing so can result in a runtime error when Parquet files are attempted to be
read as CSV or vice versa.

## Parameters

Use the parameters in this section to configure the GCS
connector.

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created prior to December 3, 2024. These can differ from their corresponding [AWS Glue connection properties](../../../glue/latest/dg/connection-properties.md "../../../glue/latest/dg/connection-properties.md"). Starting December 3, 2024, use the parameters below only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector.

We recommend that you configure a GCS connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the GCS connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type GOOGLECLOUDSTORAGE
```

**Lambda environment properties**

- glue_connection – Specifies the name of the Glue connection associated with the federated connector.

###### Note

- All connectors that use Glue connections must use AWS Secrets Manager to store credentials.
- The GCS connector created using Glue connections does not support the use of a multiplexing handler.
- The GCS connector created using Glue connections only supports `ConnectionSchemaVersion` 2.

- spill_bucket – Specifies the Amazon S3 bucket
  for data that exceeds Lambda function limits.
- spill_prefix – (Optional) Defaults to a
  subfolder in the specified `spill_bucket` called
  `athena-federation-spill`. We recommend that you
  configure an Amazon S3 [storage
  lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") on this location to delete spills older than a
  predetermined number of days or hours.
- spill_put_request_headers – (Optional) A
  JSON encoded map of request headers and values for the Amazon S3
  `putObject` request that is used for spilling (for example,
  `{"x-amz-server-side-encryption" : "AES256"}`). For other
  possible headers, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") in the
  _Amazon Simple Storage Service API Reference_.
- kms_key_id – (Optional) By default, any
  data that is spilled to Amazon S3 is encrypted using the AES-GCM authenticated
  encryption mode and a randomly generated key. To have your Lambda function use
  stronger encryption keys generated by KMS like
  `a7e63k4b-8loc-40db-a2a1-4d0en2cd8331`, you can specify a KMS key
  ID.
- disable_spill_encryption – (Optional)
  When set to `True`, disables spill encryption. Defaults to
  `False` so that data that is spilled to S3 is encrypted using
  AES-GCM – either using a randomly generated key or KMS to generate keys.
  Disabling spill encryption can improve performance, especially if your spill
  location uses [server-side
  encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md").
- secret_manager_gcp_creds_name – The name
  of the secret in AWS Secrets Manager that contains your GCS credentials in JSON format
  (for example, `GoogleCloudPlatformCredentials`).

## Setting up

databases and tables in AWS Glue

Because the built-in schema inference capability of the GCS connector is limited, we
recommend that you use AWS Glue for your metadata. The following procedures show how to
create a database and table in AWS Glue that you can access from Athena.

### Creating a database in

AWS Glue

You can use the AWS Glue console to create a database for use with the GCS
connector.

###### To create a database in AWS Glue

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. From the navigation pane, choose **Databases**.
3. Choose **Add database**.
4. For **Name**, enter a name for the database that you want
   to use with the GCS connector.
5. For **Location**, specify
   `google-cloud-storage-flag`. This location tells the GCS
   connector that the AWS Glue database contains tables for GCS data to be queried
   in Athena. The connector recognizes databases in Athena that have this flag
   and ignores databases that do not.
6. Choose **Create database**.

### Creating a table in

AWS Glue

Now you can create a table for the database. When you create an AWS Glue table to use
with the GCS connector, you must specify additional metadata.

###### To create a table in the AWS Glue console

1. In the AWS Glue console, from the navigation pane, choose
   **Tables**.
2. On the **Tables** page, choose **Add
   table**.
3. On the **Set table properties** page, enter the following
   information.
   - Name – A unique name for the
     table.
   - Database – Choose the AWS Glue
     database that you created for the GCS connector.
   - Include path – In the
     **Data store** section, for **Include
     path**, enter the URI location for GCS prefixed by
     `gs://` (for example,
     `gs://`gcs_table`/`data`/`).
     If you have one or more partition folders, don't include them in the
     path.

   ###### Note

   When you enter the non `s3://` table path, the
   AWS Glue console shows an error. You can ignore this error. The
   table will be created successfully.
   - Data format – For
     **Classification**, select
     **CSV** or **Parquet**.

4. Choose **Next.**
5. On the **Choose or define schema** page, defining a table
   schema is highly recommended, but not mandatory. If you do not define a
   schema, the GCS connector attempts to infer a schema for you.

Do one of the following:

    * If you want the GCS connector to attempt to infer a schema for
     you, choose **Next**, and then choose
     **Create**.
    * To define a schema yourself, follow the steps in the next
     section.

### Defining a table

schema in AWS Glue

Defining a table schema in AWS Glue requires more steps but gives you greater control
over the table creation process.

###### To define a schema for your table in AWS Glue

1. On the **Choose or define schema** page, choose
   **Add**.
2. Use the **Add schema entry** dialog box to provide a
   column name and data type.
3. To designate the column as a partition column, select the **Set as
   partition key** option.
4. Choose **Save** to save the column.
5. Choose **Add** to add another column.
6. When you are finished adding columns, choose
   **Next**.
7. On the **Review and create** page, review the table, and
   then choose **Create**.
8. If your schema contains partition information, follow the steps in the
   next section to add a partition pattern to the table's properties in
   AWS Glue.

### Adding a partition pattern to table properties in AWS Glue

If your GCS buckets have partitions, you must add the partition pattern to the
properties of the table in AWS Glue.

###### To add partition information to table properties AWS Glue

1. On the details page for the table that you created in AWS Glue, choose
   **Actions**, **Edit table**.
2. On the **Edit table** page, scroll down to the
   **Table properties** section.
3. Choose **Add** to add a partition key.
4. For **Key**, enter
   `partition.pattern`. This key defines the folder
   path pattern.
5. For **Value**, enter a folder path pattern like
   `StateName=${statename}/ZipCode=${zipcode}/`, where
   `statename` and `zipcode`
   enclosed by `${}` are partition column names. The GCS
   connector supports both Hive and non-Hive partition schemes.
6. When you are finished, choose **Save**.
7. To view the table properties that you just created, choose the
   **Advanced properties** tab.

At this point, you can navigate to the Athena console. The database and table that
you created in AWS Glue are available for querying in Athena.

## Data type support

The following tables show the supported data types for CSV and for Parquet.

### CSV

| **Nature of data**                                           | **Inferred Data Type**                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data looks like a number                                     | BIGINT                                                                    |
| Data looks like a string                                     | VARCHAR                                                                   |
| Data looks like a floating point (float, double, or decimal) | DOUBLE                                                                    |
| Data looks like a Date                                       | Timestamp                                                                 |
| Data that contains true/false values                         | BOOL                                                                      | ### Parquet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **PARQUET**                                                  | **Athena (Arrow)**                                                        |
| ---                                                          | ---                                                                       |
| BINARY                                                       | VARCHAR                                                                   |
| BOOLEAN                                                      | BOOL                                                                      |
| DOUBLE                                                       | DOUBLE                                                                    |
| ENUM                                                         | VARCHAR                                                                   |
| FIXED_LEN_BYTE_ARRAY                                         | DECIMAL                                                                   |
| FLOAT                                                        | FLOAT (32-bit)                                                            |
| INT32                                                        | 1. INT32 2. DATEDAY (when the Parquet column logical type is DATE)        |
| INT64                                                        | 1. INT64 2. TIMESTAMP (when the Parquet column logical type is TIMESTAMP) |
| INT96                                                        | Timestamp                                                                 |
| MAP                                                          | MAP                                                                       |
| STRUCT                                                       | STRUCT                                                                    |
| LIST                                                         | LIST                                                                      | ## Required Permissions For full details on the IAM policies that this connector requires, review the `Policies` section of the [athena-gcs.yaml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-gcs/athena-gcs.yaml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-gcs/athena-gcs.yaml") file. The following list summarizes the required permissions. <br>• Amazon S3 write access – The connector requires write access to a location in Amazon S3 in order to spill results from large queries. <br>• Athena GetQueryExecution – The connector uses this permission to fast-fail when the upstream Athena query has terminated. <br>• AWS Glue Data Catalog – The GCS connector requires read only access to the AWS Glue Data Catalog to obtain schema information. <br>• CloudWatch Logs – The connector requires access to CloudWatch Logs for storing logs. ## Performance When the table schema contains partition fields and the `partition.pattern` table property is configured correctly, you can include the partition field in the `WHERE` clause of your queries. For such queries, the GCS connector uses the partition columns to refine the GCS folder path and avoid scanning unneeded files in GCS folders. For Parquet datasets, selecting a subset of columns results in fewer data being scanned. This usually results in a shorter query execution runtime when column projection is applied. For CSV datasets, column projection is not supported and does not reduce the amount of data being scanned. `LIMIT` clauses reduce the amount of data scanned, but if you don't provide a predicate, you should expect `SELECT` queries with a `LIMIT` clause to scan at least 16 MB of data. The GCS connector scans more data for larger datasets than for smaller datasets, regardless of the `LIMIT` clause applied. For example, the query `SELECT * LIMIT 10000` scans more data for a larger underlying dataset than a smaller one. ### License information By using this connector, you acknowledge the inclusion of third party components, a list of which can be found in the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-gcs/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-gcs/pom.xml") file for this connector, and agree to the terms in the respective third party licenses provided in the [LICENSE.txt](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-gcs/LICENSE.txt "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-gcs/LICENSE.txt") file on GitHub.com. ### Additional resources For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-gcs "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-gcs") on GitHub.com. |
