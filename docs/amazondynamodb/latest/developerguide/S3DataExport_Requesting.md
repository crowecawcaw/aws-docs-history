# Requesting a table export in DynamoDB

DynamoDB table exports allow you to export table data to an Amazon S3 bucket, enabling you to
perform analytics and complex queries on your data using other AWS services such as Athena,
AWS Glue, Amazon SageMaker AI, Amazon EMR, and AWS Lake Formation. You can request a table export using the AWS Management Console,
the AWS CLI, or the DynamoDB API.

###### Note

Requester pays Amazon S3 buckets aren't supported.

DynamoDB supports both full export and incremental export:

- With **full exports**, you can export a full snapshot
  of your table from any point in time within the point-in-time recovery (PITR) window
  to your Amazon S3 bucket.
- With **incremental exports**, you can export data
  from your DynamoDB table that was changed, updated, or deleted between a specified time
  period, within your PITR window, to your Amazon S3 bucket.

###### Topics

- [Prerequisites](#S3DataExport_Requesting_Permissions "#S3DataExport_Requesting_Permissions")
- [Requesting an export using the
  AWS Management Console](#S3DataExport_Requesting_Console "#S3DataExport_Requesting_Console")
- [Getting details about past
  exports in the AWS Management Console](#S3DataExport_Requesting_Console_Details "#S3DataExport_Requesting_Console_Details")
- [Requesting an export using the AWS CLI and
  AWS SDKs](#S3DataExport_Requesting_CLI "#S3DataExport_Requesting_CLI")
- [Getting details about past exports
  using the AWS CLI and AWS SDKs](#S3DataExport_Requesting_CLI_Details "#S3DataExport_Requesting_CLI_Details")

## Prerequisites

**Enable PITR**

To use the export to S3 feature, you must enable PITR on your table. For details about how to enable PITR, see [Point-in-time
recovery](PointInTimeRecovery_Howitworks.md "PointInTimeRecovery_Howitworks.md"). If you request an export for a table that doesn't have PITR enabled, your request will fail with an exception message: “An error occurred (PointInTimeRecoveryUnavailableException) when calling the `ExportTableToPointInTime` operation: Point in time recovery is not enabled for table 'my-dynamodb-table”. You can only request and export from a point in time that is within your configured PITR `RecoveryPeriodInDays`.

**Set up S3 permissions**

You can export your table data to any Amazon S3 bucket you have permission to write to. The
destination bucket doesn't need to be in the same AWS Region or have the same owner as
the source table owner. Your AWS Identity and Access Management (IAM) policy needs to allow you to be able to
perform S3 actions (`s3:AbortMultipartUpload`, `s3:PutObject`, and
`s3:PutObjectAcl`) and the DynamoDB export action
(`dynamodb:ExportTableToPointInTime`). Here's an example of a sample
policy that will grant your user permissions to perform exports to an S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDynamoDBExportAction",
 "Effect": "Allow",
 "Action": "dynamodb:ExportTableToPointInTime",
 "Resource": "arn:aws:dynamodb:us-east-1:`111122223333`:table/my-table"
 },
 {
 "Sid": "AllowS3BucketWrites",
 "Effect": "Allow",
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 }
 ]
}`

```

If you need to write to an Amazon S3 bucket that is in another account or you don't have
permissions to write to, the Amazon S3 bucket owner must add a bucket policy to allow you to
export from DynamoDB to that bucket. Here's an example policy on the target Amazon S3
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ExampleStatement",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:user/Dave"
 },
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
 }
 ]
}`

```

Revoking these permissions while an export is in progress will result in partial
files.

###### Note

If the table or bucket you're exporting to is encrypted with customer managed keys, that
KMS key's policies must give DynamoDB permission to use it. This permission is given
through the IAM User/Role that triggers the export job. For more information on
encryption including best practices, see [How DynamoDB uses
AWS KMS](../../../kms/latest/developerguide/services-dynamodb.md "../../../kms/latest/developerguide/services-dynamodb.md") and [Using a custom KMS key](encryption.md#managed-key-customer-managed "encryption.md#managed-key-customer-managed").

## Requesting an export using the

AWS Management Console

The following example demonstrates how to use the DynamoDB console to export an existing
table named `MusicCollection`.

###### Note

This procedure assumes that you have enabled point-in-time recovery. To enable it
for the `MusicCollection` table, on the table's
**Overview** tab, in the **Table details**
section, choose **Enable** for **Point-in-time
recovery**.

###### To request a table export

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. In the navigation pane on the left side of the console, choose
   **Exports to S3**.
3. Select the **Export to S3** button.
4. Choose a source table and destination S3 bucket. If the destination bucket is
   owned by your account, you can use the **Browse S3** button
   to find it. Otherwise, enter the URL of the bucket using the
   `s3://`bucketname`/`prefix`
format.` the `prefix` is an optional folder to
   help keep your destination bucket organized.
5. Choose **Full export** or **Incremental export**. A **full
   export** outputs the full table snapshot of your table as it was at
   the point in time you specify. An **incremental export** outputs the changes made to your table during the specified export
   period. Your output is compacted so it only contains the final state of the item
   from the export period. The item will only appear once in the export even if it
   has multiple updates within the same export period.

Full export

    1. Select the point in time you want to export the full table
     snapshot from. This can be any point in time within the PITR
     window. Alternatively, you can select **Current time** to export the latest
     snapshot.
    2. For **Exported file format**,
     choose between **DynamoDB JSON**
     and **Amazon Ion**. By default,
     your table will be exported in DynamoDB JSON format from the
     latest restorable time in the point in time recovery window
     and encrypted using an Amazon S3 key (SSE-S3). You can
     change these export settings if necessary.


    ###### Note

    If you choose to encrypt your export using a key
     protected by AWS Key Management Service (AWS KMS), the key must be in the
     same Region as the destination S3 bucket.

Incremental export

    1. Select the **Export period**
     you want to export the incremental data for. Pick a start
     time within the PITR window. The export period duration must
     be at least 15 minutes and be no longer than 24 hours. The
     export period's start time is inclusive and the end time is
     exclusive.
    2. Choose between **Absolute
     mode** or **Relative
     mode**.


    	1. **Absolute mode**
    	 will export incremental data for the time period you
    	 specify.
    	2. **Relative mode**
    	 will export incremental data for an export period
    	 that is relative to your export job submission
    	 time.
    3. For **Exported file format**,
     choose between **DynamoDB JSON**
     and **Amazon Ion**. By default,
     your table will be exported in DynamoDB JSON format from the
     latest restorable time in the point in time recovery window
     and encrypted using an Amazon S3 key (SSE-S3). You can change
     these export settings if necessary.


    ###### Note

    If you choose to encrypt your export using a key
     protected by AWS Key Management Service (AWS KMS), the key must be in the
     same Region as the destination S3 bucket.
    4. For **Export view type**,
     select either **New and old
     images** or **New images
     only**. New image provides the latest state of
     the item. Old image provides the state of the item right
     before the specified “start date and time”. The default
     setting is **New and old
     images**. For more information on new images
     and old images, see [Incremental export output](S3DataExport.md#incremental-export-output "S3DataExport.md#incremental-export-output").

6. Choose **Export** to begin.

Exported data isn't transactionally consistent. Your transaction operations can be
torn between two export outputs. A subset of items can be modified by a transaction
operation reflected in the export, while another subset of modifications in the same
transaction isn't reflected in the same export request. However, exports are eventually
consistent. If a transaction is torn during an export, you'll have the remaining
transaction in your next contiguous export, without duplicates. The time periods used
for exports are based on an internal system clock and can vary by one minute of your
application’s local clock.

## Getting details about past

exports in the AWS Management Console

You can find information about export tasks you've run in the past by choosing the
**Exports to S3** section in the navigation sidebar. This section
contains a list of all exports you've created in the past 90 days. Select the ARN of a
task listed in the **Exports** tab to retrieve information about that
export, including any advanced configuration settings you chose. Note that although
export task metadata expires after 90 days and jobs older than that are no longer found
in this list, the objects in your S3 bucket remain as long as their bucket policies
allow. DynamoDB never deletes any of the objects it creates in your S3 bucket during an
export.

## Requesting an export using the AWS CLI and

AWS SDKs

The following examples show how to export an existing table to an S3 bucket.

###### Note

This procedure assumes that you have enabled point-in-time recovery. To enable it
for the `MusicCollection` table, run the following command.

```
aws dynamodb update-continuous-backups \
    --table-name MusicCollection \
    --point-in-time-recovery-specification PointInTimeRecoveryEnabled=True
```

**Full export**

AWS CLI

###### Note

If requesting a cross-account table export, make sure to include the
`--s3-bucket-owner` option.

```
aws dynamodb export-table-to-point-in-time \
  --table-arn arn:aws:dynamodb:us-west-2:111122223333:table/MusicCollection \
  --s3-bucket ddb-export-musiccollection-9012345678 \
  --s3-prefix 2020-Nov \
  --export-format DYNAMODB_JSON \
  --export-time 1604632434 \
  --s3-bucket-owner 9012345678 \
  --s3-sse-algorithm AES256
```

Python

```
import boto3
from datetime import datetime

client = boto3.client('dynamodb')

client.export_table_to_point_in_time(
    TableArn='arn:aws:dynamodb:us-east-1:111122223333:table/TABLE',
    ExportTime=datetime(2023, 9, 20, 12, 0, 0),
    S3Bucket='bucket',
    S3Prefix='prefix',
    S3SseAlgorithm='AES256',
    ExportFormat='DYNAMODB_JSON'
)
```

Java

```
DynamoDbClient client = DynamoDbClient.create();

client.exportTableToPointInTime(b -> b
    .tableArn("arn:aws:dynamodb:us-east-1:111122223333:table/TABLE")
    .exportTime(Instant.parse("2023-09-20T12:00:00Z"))
    .s3Bucket("bucket")
    .s3Prefix("prefix")
    .s3SseAlgorithm(S3SseAlgorithm.AES256)
    .exportFormat(ExportFormat.DYNAMODB_JSON));
```

.NET

```
var client = new AmazonDynamoDBClient();

await client.ExportTableToPointInTimeAsync(new ExportTableToPointInTimeRequest
{
    TableArn = "arn:aws:dynamodb:us-east-1:111122223333:table/TABLE",
    ExportTime = new DateTime(2023, 9, 20, 12, 0, 0, DateTimeKind.Utc),
    S3Bucket = "bucket",
    S3Prefix = "prefix",
    S3SseAlgorithm = S3SseAlgorithm.AES256,
    ExportFormat = ExportFormat.DYNAMODB_JSON
});
```

JavaScript

```
import { DynamoDBClient, ExportTableToPointInTimeCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient();

await client.send(new ExportTableToPointInTimeCommand({
    TableArn: "arn:aws:dynamodb:us-east-1:111122223333:table/TABLE",
    ExportTime: new Date("2023-09-20T12:00:00Z"),
    S3Bucket: "bucket",
    S3Prefix: "prefix",
    S3SseAlgorithm: "AES256",
    ExportFormat: "DYNAMODB_JSON"
}));
```

Go

```
cfg, _ := config.LoadDefaultConfig(context.TODO())
client := dynamodb.NewFromConfig(cfg)

exportTime := time.Date(2023, 9, 20, 12, 0, 0, 0, time.UTC)
client.ExportTableToPointInTime(context.TODO(), &dynamodb.ExportTableToPointInTimeInput{
    TableArn:       aws.String("arn:aws:dynamodb:us-east-1:111122223333:table/TABLE"),
    ExportTime:     &exportTime,
    S3Bucket:       aws.String("bucket"),
    S3Prefix:       aws.String("prefix"),
    S3SseAlgorithm: types.S3SseAlgorithmAes256,
    ExportFormat:   types.ExportFormatDynamodbJson,
})
```

**Incremental export**

AWS CLI

```
aws dynamodb export-table-to-point-in-time \
  --table-arn arn:aws:dynamodb:REGION:ACCOUNT:table/TABLENAME \
  --s3-bucket BUCKET --s3-prefix PREFIX \
  --incremental-export-specification ExportFromTime=1693569600,ExportToTime=1693656000,ExportViewType=NEW_AND_OLD_IMAGES \
  --export-type INCREMENTAL_EXPORT
```

Python

```
import boto3
from datetime import datetime

client = boto3.client('dynamodb')

client.export_table_to_point_in_time(
    TableArn='arn:aws:dynamodb:us-east-1:111122223333:table/TABLE',
    IncrementalExportSpecification={
      'ExportFromTime': datetime(2023, 9, 20, 12, 0, 0),
      'ExportToTime': datetime(2023, 9, 20, 13, 0, 0),
      'ExportViewType': 'NEW_AND_OLD_IMAGES'
    },
    ExportType='INCREMENTAL_EXPORT',
    S3Bucket='bucket',
    S3Prefix='prefix',
    S3SseAlgorithm='AES256',
    ExportFormat='DYNAMODB_JSON'
)
```

Java

```
DynamoDbClient client = DynamoDbClient.create();

client.exportTableToPointInTime(b -> b
    .tableArn("arn:aws:dynamodb:us-east-1:111122223333:table/TABLE")
    .exportType(ExportType.INCREMENTAL_EXPORT)
    .incrementalExportSpecification(i -> i
        .exportFromTime(Instant.parse("2023-09-20T12:00:00Z"))
        .exportToTime(Instant.parse("2023-09-20T13:00:00Z"))
        .exportViewType(ExportViewType.NEW_AND_OLD_IMAGES))
    .s3Bucket("bucket")
    .s3Prefix("prefix")
    .s3SseAlgorithm(S3SseAlgorithm.AES256)
    .exportFormat(ExportFormat.DYNAMODB_JSON));
```

.NET

```
var client = new AmazonDynamoDBClient();

await client.ExportTableToPointInTimeAsync(new ExportTableToPointInTimeRequest
{
    TableArn = "arn:aws:dynamodb:us-east-1:111122223333:table/TABLE",
    ExportType = ExportType.INCREMENTAL_EXPORT,
    IncrementalExportSpecification = new IncrementalExportSpecification
    {
        ExportFromTime = new DateTime(2023, 9, 20, 12, 0, 0, DateTimeKind.Utc),
        ExportToTime = new DateTime(2023, 9, 20, 13, 0, 0, DateTimeKind.Utc),
        ExportViewType = ExportViewType.NEW_AND_OLD_IMAGES
    },
    S3Bucket = "bucket",
    S3Prefix = "prefix",
    S3SseAlgorithm = S3SseAlgorithm.AES256,
    ExportFormat = ExportFormat.DYNAMODB_JSON
});
```

JavaScript

```
import { DynamoDBClient, ExportTableToPointInTimeCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient();

await client.send(new ExportTableToPointInTimeCommand({
    TableArn: "arn:aws:dynamodb:us-east-1:111122223333:table/TABLE",
    ExportType: "INCREMENTAL_EXPORT",
    IncrementalExportSpecification: {
        ExportFromTime: new Date("2023-09-20T12:00:00Z"),
        ExportToTime: new Date("2023-09-20T13:00:00Z"),
        ExportViewType: "NEW_AND_OLD_IMAGES"
    },
    S3Bucket: "bucket",
    S3Prefix: "prefix",
    S3SseAlgorithm: "AES256",
    ExportFormat: "DYNAMODB_JSON"
}));
```

Go

```
cfg, _ := config.LoadDefaultConfig(context.TODO())
client := dynamodb.NewFromConfig(cfg)

fromTime := time.Date(2023, 9, 20, 12, 0, 0, 0, time.UTC)
toTime := time.Date(2023, 9, 20, 13, 0, 0, 0, time.UTC)
client.ExportTableToPointInTime(context.TODO(), &dynamodb.ExportTableToPointInTimeInput{
    TableArn:   aws.String("arn:aws:dynamodb:us-east-1:111122223333:table/TABLE"),
    ExportType: types.ExportTypeIncrementalExport,
    IncrementalExportSpecification: &types.IncrementalExportSpecification{
        ExportFromTime: &fromTime,
        ExportToTime:   &toTime,
        ExportViewType: types.ExportViewTypeNewAndOldImages,
    },
    S3Bucket:       aws.String("bucket"),
    S3Prefix:       aws.String("prefix"),
    S3SseAlgorithm: types.S3SseAlgorithmAes256,
    ExportFormat:   types.ExportFormatDynamodbJson,
})
```

###### Note

If you choose to encrypt your export using a key protected by AWS Key Management Service (AWS KMS),
the key must be in the same Region as the destination S3 bucket.

## Getting details about past exports

using the AWS CLI and AWS SDKs

You can find information about export requests you've run in the past by using the
`list-exports` command. This command returns a list of all exports you've
created in the past 90 days. Note that although export task metadata expires after 90
days and jobs older than that are no longer returned by the `list-exports`
command, the objects in your S3 bucket remain as long as their bucket policies allow.
DynamoDB never deletes any of the objects it creates in your S3 bucket during an
export.

Exports have a status of `PENDING` until they either succeed or fail. If
they succeed, the status changes to `COMPLETED`. If they fail, the status
changes to `FAILED` with a `failure_message` and
`failure_reason`.

**List exports**

AWS CLI

```
aws dynamodb list-exports \
    --table-arn arn:aws:dynamodb:us-east-1:111122223333:table/ProductCatalog
```

Python

```
import boto3

client = boto3.client('dynamodb')

print(
  client.list_exports(
     TableArn='arn:aws:dynamodb:us-east-1:111122223333:table/TABLE',
  )
)
```

Java

```
DynamoDbClient client = DynamoDbClient.create();

ListExportsResponse response = client.listExports(b -> b
    .tableArn("arn:aws:dynamodb:us-east-1:111122223333:table/TABLE"));

response.exportSummaries().forEach(System.out::println);
```

.NET

```
var client = new AmazonDynamoDBClient();

var response = await client.ListExportsAsync(new ListExportsRequest
{
    TableArn = "arn:aws:dynamodb:us-east-1:111122223333:table/TABLE"
});

response.ExportSummaries.ForEach(Console.WriteLine);
```

JavaScript

```
import { DynamoDBClient, ListExportsCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient();

const response = await client.send(new ListExportsCommand({
    TableArn: "arn:aws:dynamodb:us-east-1:111122223333:table/TABLE"
}));

console.log(response.ExportSummaries);
```

Go

```
cfg, _ := config.LoadDefaultConfig(context.TODO())
client := dynamodb.NewFromConfig(cfg)

response, _ := client.ListExports(context.TODO(), &dynamodb.ListExportsInput{
    TableArn: aws.String("arn:aws:dynamodb:us-east-1:111122223333:table/TABLE"),
})

fmt.Println(response.ExportSummaries)
```

**Describe export**

AWS CLI

```
aws dynamodb describe-export \
    --export-arn arn:aws:dynamodb:us-east-1:111122223333:table/ProductCatalog/export/01695353076000-a1b2c3d4
```

Python

```
import boto3

client = boto3.client('dynamodb')

print(
  client.describe_export(
     ExportArn='arn:aws:dynamodb:us-east-1:111122223333:table/TABLE/export/01695353076000-06e2188f',
  )['ExportDescription']
)
```

Java

```
DynamoDbClient client = DynamoDbClient.create();

DescribeExportResponse response = client.describeExport(b -> b
    .exportArn("arn:aws:dynamodb:us-east-1:111122223333:table/TABLE/export/01695353076000-06e2188f"));

System.out.println(response.exportDescription());
```

.NET

```
var client = new AmazonDynamoDBClient();

var response = await client.DescribeExportAsync(new DescribeExportRequest
{
    ExportArn = "arn:aws:dynamodb:us-east-1:111122223333:table/TABLE/export/01695353076000-06e2188f"
});

Console.WriteLine(response.ExportDescription);
```

JavaScript

```
import { DynamoDBClient, DescribeExportCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient();

const response = await client.send(new DescribeExportCommand({
    ExportArn: "arn:aws:dynamodb:us-east-1:111122223333:table/TABLE/export/01695353076000-06e2188f"
}));

console.log(response.ExportDescription);
```

Go

```
cfg, _ := config.LoadDefaultConfig(context.TODO())
client := dynamodb.NewFromConfig(cfg)

response, _ := client.DescribeExport(context.TODO(), &dynamodb.DescribeExportInput{
    ExportArn: aws.String("arn:aws:dynamodb:us-east-1:111122223333:table/TABLE/export/01695353076000-06e2188f"),
})

fmt.Println(response.ExportDescription)
```
