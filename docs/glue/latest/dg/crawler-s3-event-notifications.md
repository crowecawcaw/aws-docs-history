# Accelerating crawls using Amazon S3 event notifications

Instead of listing the objects from an Amazon S3 or Data Catalog target, you can configure the crawler to use Amazon S3 events to find any changes. This feature improves the recrawl time by using Amazon S3 events to identify the changes between two crawls by listing all the files from the subfolder which triggered the event instead of listing the full Amazon S3 or Data Catalog target.

The first crawl lists all Amazon S3 objects from the target. After the first successful crawl, you can choose to recrawl manually or on a set schedule.
The crawler will list only the objects from those events instead of listing all objects.

When the target is a Data Catalog table, the crawler updates the existing tables in the Data Catalog with changes (for example, extra partitions in a table).

The advantages of moving to an Amazon S3 event based crawler are:

- A faster recrawl as the listing of all the objects from the target is not required, instead the listing of specific folders is done where objects are added or deleted.
- A reduction in the overall crawl cost as the listing of specific folders is done where objects are added or deleted.
  The Amazon S3 event crawl runs by consuming Amazon S3 events from the SQS queue based on the crawler schedule. There will be no cost if there are no events in the queue. Amazon S3 events can be configured to go directly to the SQS queue or in cases where multiple consumers need the same event, a combination of SNS and SQS. For more information, see [Setting up your account for Amazon S3 event notifications](#crawler-s3-event-notifications-setup "#crawler-s3-event-notifications-setup").

After creating and configuring the crawler in event mode, the first crawl runs in listing mode by performing full a listing of the Amazon S3 or Data Catalog target. The following log confirms the operation of the crawl by consuming Amazon S3 events after the first successful crawl: "The crawl is running by consuming Amazon S3 events."

After creating the Amazon S3 event crawl and updating the crawler properties which may impact the crawl, the crawl operates in list mode and the following log is added: "Crawl is not running in S3 event mode".

###### Note

The maximum number of messages to consume is 100,000 messages per crawl.

## Considerations and limitations

The following considerations and limitations apply when you configure a crawler to use Amazon S3 event notifications to find any changes.

- **Important behavior with deleted partitions**

When using Amazon S3 event crawlers with Data Catalog tables:

    + If you delete a partition using the `DeletePartition` API call,
     you must also delete all S3 objects under that partition, and select
     **All object removal events** when you configure
     your S3 event notifications. If deletion events are not configured, the
     crawler recreates the deleted partition during its next run.

- Only a single target is supported by the crawler, whether for Amazon S3 or Data Catalog targets.
- SQS on private VPC is not supported.
- Amazon S3 sampling is not supported.
- The crawler target should be a folder for an Amazon S3 target, or one or more AWS Glue Data Catalog tables for a Data Catalog target.
- The 'everything' path wildcard is not supported: s3://%
- For a Data Catalog target, all catalog tables should point to same Amazon S3 bucket for Amazon S3 event mode.
- For a Data Catalog target, a catalog table should not point to an Amazon S3 location in the Delta Lake format (containing \_symlink folders, or checking the catalog table's `InputFormat`).

###### Topics

- [Setting up your account for Amazon S3 event notifications](#crawler-s3-event-notifications-setup "#crawler-s3-event-notifications-setup")
- [Setting up a crawler for Amazon S3 event notifications for an Amazon S3 target](crawler-s3-event-notifications-setup-console-s3-target.md "crawler-s3-event-notifications-setup-console-s3-target.md")
- [Setting up a crawler for Amazon S3 event notifications for a Data Catalog table](crawler-s3-event-notifications-setup-console-catalog-target.md "crawler-s3-event-notifications-setup-console-catalog-target.md")

## Setting up your account for Amazon S3 event notifications

Complete the following setup tasks. Note the values in parenthesis reference the configurable settings from the script.

1. You need to set up event notifications for your Amazon S3 bucket.

For more information, see [Amazon S3 event notifications](../../../AmazonS3/latest/userguide/EventNotifications.md "../../../AmazonS3/latest/userguide/EventNotifications.md"). 2. To use the Amazon S3 event based crawler, you should enable event notification on
the Amazon S3 bucket with events filtered from the prefix which is the same as the S3
target and store in SQS. You can set up SQS and event notification through the
console by following the steps in [Walkthrough: Configuring a bucket for notifications](../../../AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.md "../../../AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.md"). 3. Add the following SQS policy to the role used by the crawler.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "sqs:DeleteMessage",
 "sqs:GetQueueUrl",
 "sqs:ListDeadLetterSourceQueues",
 "sqs:ReceiveMessage",
 "sqs:GetQueueAttributes",
 "sqs:ListQueueTags",
 "sqs:SetQueueAttributes",
 "sqs:PurgeQueue"
 ],
 "Resource": "arn:aws:sqs:us-east-1:`111122223333`:cfn-sqs-queue"
 }
 ]
}`

```
