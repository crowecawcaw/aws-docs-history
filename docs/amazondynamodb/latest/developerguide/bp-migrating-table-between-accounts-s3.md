

# Migrate a table using export to S3 and import from S3
<a name="bp-migrating-table-between-accounts-s3"></a>

**Prerequisites**
+ You must enable Point-in-Time Recovery (PITR) for your table in order to perform the export to S3. For more information, see [Enable point-in-time recovery in DynamoDB](PointInTimeRecovery_Howitworks.md).
+ Valid IAM permissions to perform the export. For more information, see [Requesting a table export in DynamoDB](S3DataExport_Requesting.md).
+ Valid IAM permissions sufficient to perform the import. For more information, see [Requesting a table import in DynamoDB](S3DataImport.Requesting.md).

**Pricing information**

AWS charges for PITR (based on the size of the table and how long PITR is enabled for). If you don't need PITR except for the export, you can turn it off after the export concludes. AWS also charges for requests made against S3, for storing the exported data in S3 and for importing (based on the uncompressed size of the imported data).

For more information about DynamoDB pricing, see [DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/).

**Note**  
 There are limits on the size and number of objects when importing from S3 to DynamoDB. For more information, see [Import quotas](S3DataImport.Validation.md#S3DataImport.Validation.limits).

## Requesting a table export to Amazon S3
<a name="bp-migrating-table-between-accounts-s3-table-export"></a>

1. Sign in to the AWS Management Console and open the DynamoDB console.

1. In the navigation pane on the left side of the console, choose **Exports to S3**.

1. Choose a source table and destination S3 bucket. Enter the URL of the destination account bucket using the `s3://bucketname/prefix` format. `/prefix` is an optional folder to help keep your destination bucket organized.

1. Choose **Full export**. A full export outputs the full table snapshot of your table, at the point in time you specify.

   1. Select **Current time** to export the latest full table snapshot.

   1. For **Exported file format**, choose between DynamoDB JSON and Amazon Ion. The default option is DynamoDB JSON.

1. Choose **Export** to begin the export.

1. Small table exports should complete in a few minutes, but tables in the terabyte range can take more than an hour.

## Requesting a table import from Amazon S3
<a name="bp-migrating-table-between-accounts-s3-table-import"></a>

1. Sign in to the AWS Management Console and open the DynamoDB console.

1. In the navigation pane on the left side of the console, choose **Import from S3**.

1. On the page that appears, select **Import from S3**.

1. Enter the Amazon S3 source URL. You can also find it by using the **Browse S3** button. The expected path is of the format `s3://bucket/prefix/AWSDynamoDB/<XXXXXXXX-XXXXXX>/data/`.

1. Specify if you are the S3 bucket owner.

1. Under **Import file compression**, select **GZIP** to match the export.

1. Under **Import file format**, select **DynamoDB JSON** to match the export.

1. Select **Next**. For **Specify table details**, choose the options for the new table that will be created to store your data.

1. Select **Next**. For **Configure table settings**, customize any additional table settings if applicable.

1. Select **Next** again to review your import options, then choose **Import** to begin the import task. You see your new table listed under **Imports from S3** with the status **Importing**. You cannot access your table during this time. Small imports should complete in a few minutes, but tables in the terabyte range can take more than an hour.

1. After the import completes, the status shows as **Active**, and you can start using the table.

## Keeping tables in sync during migration
<a name="bp-migrating-table-between-accounts-s3-table-sync"></a>

If you can pause write operations on the source table for the duration of the migration, then the source and output should match up exactly after the migration. If you can't pause write operations, the target table would normally be a bit behind the source after the migration. To catch up the source table, you can use streaming (DynamoDB Streams or Kinesis Data Streams for DynamoDB) to replay the writes that happened in the source table since the backup or export. 

You should start reading the stream records prior to the timestamp when you exported the source table to S3. For example, if the export to S3 occurred at 2:00 PM and the import to the target table was concluded at 11:00 PM, you should initiate the DynamoDB stream reading at 1:58 PM. The streaming options for change data capture table summarizes the features of each streaming model.

Using DynamoDB Streams with Lambda offers a streamlined approach for synchronizing data between the source and target DynamoDB tables. You can use a Lambda function to replay each write in the target table.

**Note**  
Items are kept in the DynamoDB Streams for 24 hours, so you should plan to complete your backup and restore or export and import within that window.