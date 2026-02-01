Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading data from a local file setup and workflow

You can load data from a local file into an existing or new table.

## Administrator setup to load data from a local file

Your query editor v2 administrator must specify the common Amazon S3 bucket in the **Account settings** window.
The account users must be configured with the proper permissions.

- Required IAM permissions – the users of load from local file must have
  `s3:ListBucket`, `s3:GetBucketLocation`,
  `s3:putObject`, `s3:getObject`, and
  `s3:deleteObject` permissions. The
  `optional-prefix` can be specified to limit
  query editor v2 related use of this bucket to objects with this prefix. You might use
  this option when using this same Amazon S3 bucket for uses other than query editor v2. For
  more information about buckets and prefixes, see [Managing user access to specific folders](../../../AmazonS3/latest/userguide/example-bucket-policies.md#example-bucket-policies-folders "../../../AmazonS3/latest/userguide/example-bucket-policies.md#example-bucket-policies-folders") in the
  _Amazon Simple Storage Service User Guide_. To make sure that cross user data
  access is not allowed, we recommend that the query editor v2 administrator use an
  Amazon S3 bucket policy to restrict object access based on
  `aws:userid`. The following example allows Amazon S3 permissions
  to a `<staging-bucket-name>` with read/write
  access only to Amazon S3 objects with the `aws:userid` as a
  prefix.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`<staging-bucket-name>`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`<staging-bucket-name>[/<optional-prefix>]`/${aws:userid}/*"
 ]
 }
 ]
}`

```

- Data separation – we recommend that users not have access to each other's data (even
  briefly). Load from a local file uses the staging Amazon S3 bucket set up by the
  query editor v2 administrator. Configure the bucket policy for the staging bucket to
  provide data separation between users. The following example shows a bucket
  policy that separates data between users of the
  `<staging-bucket-name>`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {"Sid": "userIdPolicy",
 "Effect": "Deny",
 "Principal": "*",
 "Action": ["s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"],
 "NotResource": [
 "arn:aws:s3:::`<staging-bucket-name>[/<optional-prefix>]`/${aws:userid}/*"
 ]
 }
 ]
}`

```

## Loading data from a local file

###### To load local file data into an existing table

Your query editor v2 administrator must specify the common Amazon S3 bucket in the
**Account settings** window. query editor v2 automatically uploads
the local file to a common Amazon S3 bucket used by your account, and then uses the
COPY command to load data. The COPY command generated and run by the query editor v2 load
local file window supports many of the parameters available to the COPY command
syntax to copy from Amazon S3. For information about the COPY command and its options
used to load data from Amazon S3, see [COPY from
Amazon S3](../dg/copy-parameters-data-source-s3.md "../dg/copy-parameters-data-source-s3.md") in the _Amazon Redshift Database Developer Guide_.

1. Confirm that the table is already created in the database where you want to load data.
2. Confirm that you are connected to the target database in the tree-view panel of query editor v2.
   You can create a connection using the context menu (right-click) to the cluster or workgroup where the data will be loaded.
3. Choose
   ![Load](images/qev2-upload.png)**Load data**.
4. For **Data source**, choose **Load from local file**.
5. Choose **Browse** to find the file that contains the data to **Load file**.
   By default, files with extension `.csv`, `.avro` `.parquet`, and `.orc` are shown,
   but you can choose other file types. The maximum file size is 100 MB.
6. Choose the **File format** for the file to be uploaded. The supported data
   formats are CSV, JSON, DELIMITER, FIXEDWIDTH, SHAPEFILE, AVRO, PARQUET, and
   ORC. Depending on the specified file format, you can choose the respective **File options**.
   You can also select **Data is encrypted** if the data is encrypted and enter the Amazon Resource Name (ARN) of the KMS key
   used to encrypt the data.

If you choose CSV or DELIMITER, you can also choose the **Delimiter character** and whether to
**Ignore header rows** if the specified number of rows are actually column names and not data to load. 7. (Optional) The **Advanced settings** support various **Data conversion parameters** and
**Load operations**. Enter this information as needed for your file.

For more information about data conversion and data load parameters, see
[Data
conversion parameters](../dg/copy-parameters-data-conversion.md "../dg/copy-parameters-data-conversion.md") and [Data load
operations](../dg/copy-parameters-data-load.md "../dg/copy-parameters-data-load.md") in the _Amazon Redshift Database Developer Guide_. 8. Choose **Next**. 9. Choose **Load existing table**. 10. Confirm or choose the location of the **Target table** including **Cluster or workgroup**, **Database**, **Schema**,
and **Table** name where the data is loaded. 11. (Optional) You can choose column names to enter in **Column mapping** to map
columns in the order of the input data file. 12. Choose **Load data** to start the data load.

When the load completes, a message is displayed whether the load was successful or not.
If successful, you can now use SQL to select data from
the loaded table. When there is an error, query the system view
STL_LOAD_ERRORS to get more details. For information about COPY command
errors, see [STL_LOAD_ERRORS](../dg/r_STL_LOAD_ERRORS.md "../dg/r_STL_LOAD_ERRORS.md")
in the _Amazon Redshift Database Developer Guide_.

The COPY command template that was used to load data appears in your **Query history**.
This COPY command template shows some of the parameters used, but it can't be run directly in an editor tab.
For more information about query history, see
[Viewing query and tab history](query-editor-v2-history.md "query-editor-v2-history.md").

When you load data into a new table, query editor v2 first creates the table in the database, then loads the data as separate actions in the same workflow.

###### To load local file data into a new table

Your query editor v2 administrator must specify the common Amazon S3 bucket in the **Account settings** window.
The local file is automatically uploaded to a common Amazon S3 bucket used by your account, and then the COPY command is used by query editor v2 to load data.
The COPY command generated and run by the query editor v2 load local file window supports many of the parameters available to the COPY command syntax to copy from Amazon S3.
For information about the COPY command and its options used to load data from Amazon S3, see
[COPY from Amazon S3](../dg/copy-parameters-data-source-s3.md "../dg/copy-parameters-data-source-s3.md") in the _Amazon Redshift Database Developer Guide_.

1. Confirm that you are connected to the target database in the tree-view panel of query editor v2.
   You can create a connection using the context menu (right-click) to the cluster or workgroup where the data will be loaded.
2. Choose
   ![Load](images/qev2-upload.png)**Load data**.
3. For **Data source**, choose **Load from local file**.
4. Choose **Browse** to find the file that contains the data to **Load file**.
   By default, files with extension `.csv`, `.avro` `.parquet`, and `.orc` are shown,
   but you can choose other file types. The maximum file size is 100 MB.
5. Choose the **File format** for the file to be uploaded. The supported data
   formats are CSV, JSON, DELIMITER, FIXEDWIDTH, SHAPEFILE, AVRO, PARQUET, and
   ORC. Depending on the specified file format, you can choose the respective **File options**.
   You can also select **Data is encrypted** if the data is encrypted and enter the Amazon Resource Name (ARN) of the KMS key
   used to encrypt the data.

If you choose CSV or DELIMITER, you can also choose the **Delimiter character** and whether to
**Ignore header rows** if the specified number of rows are actually column names and not data to load. 6. (Optional) The **Advanced settings** support various **Data conversion parameters** and
**Load operations**. Enter this information as needed for your file.

For more information about data conversion and data load parameters, see
[Data
conversion parameters](../dg/copy-parameters-data-conversion.md "../dg/copy-parameters-data-conversion.md") and [Data load
operations](../dg/copy-parameters-data-load.md "../dg/copy-parameters-data-load.md") in the _Amazon Redshift Database Developer Guide_. 7. Choose **Next**. 8. Choose **Load new table**. 9. Confirm or choose the location of the **Target table** including **Cluster or workgroup**, **Database**, and **Schema**
where the data is loaded.
Enter a **Table** name to be created. 10. Choose **Create table** to create the table using the definition shown.

A review summary of the table definition is displayed. The table is
created in the database. To later delete the table, run a DROP TABLE SQL
command. For more information, see [DROP TABLE](../dg/r_DROP_TABLE.md "../dg/r_DROP_TABLE.md") in the
_Amazon Redshift Database Developer Guide_. 11. Choose **Load data** to start the data load.

When the load completes, a message displays indicating whether the load
was successful or not. If successful, you can now use SQL to select data
from the loaded table. When there is an error, query the system view
STL_LOAD_ERRORS to get more details. For information about COPY command
errors, see [STL_LOAD_ERRORS](../dg/r_STL_LOAD_ERRORS.md "../dg/r_STL_LOAD_ERRORS.md")
in the _Amazon Redshift Database Developer Guide_.

The COPY command template that was used to load data appears in your **Query history**.
This COPY command template shows some of the parameters used, but it can't be run directly in an editor tab.
For more information about query history, see
[Viewing query and tab history](query-editor-v2-history.md "query-editor-v2-history.md").
