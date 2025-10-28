# Viewing the activity of specific users in Amazon Q Developer

You can configure Amazon Q to collect user activity telemetry of individual Amazon Q Developer subscribers in your
organization and present that information in a report. The report gives you insights into how specific
users are using Amazon Q.

Amazon Q generates the report every day at midnight (00:00) Coordinated Universal Time (UTC), and saves
it in a CSV file at the following path:

`s3://`bucketName`/`prefix`/AWSLogs/`accountId`/QDeveloperLogs/by_user_analytic/`region`/`year`/`month`/`day`/00/`accountId`_by_user_analytic_`timestamp`.csv`

The CSV file is laid out as follows:

- Each row shows a user who interacted with Amazon Q that day.
- Each column shows a metric, as described in [User activity report metrics](user-activity-metrics.md "user-activity-metrics.md"). Metrics are calculated based on the user
  telemetry collected over the course of the day.
  If more than 1,000 users interact with Amazon Q during the day, Amazon Q splits the data into several CSV
  files containing 1,000 users each, and having suffixes of `part_1`,
  `part_2`, and so on.

###### Note

When you enable user activity reports, Amazon Q collects telemetry regardless of how a developer has
set the **Enable Amazon Q to send usage data to AWS** setting in their IDE. That
setting controls whether telemetry can be used by the _AWS corporation_, not
your organization. For more information about this setting, see [Opting out of sharing your client-side
telemetry](opt-out-IDE.md#opt-out-IDE-telemetry "opt-out-IDE.md#opt-out-IDE-telemetry").

Use the following instructions to enable user activity reports.

**Prerequisite**

Create an Amazon S3 bucket to hold the user activity report CSV file. The bucket must:

- Be in the AWS Region where the Amazon Q Developer profile was installed. This profile was
  installed when you subscribed IAM Identity Center workforce users to Amazon Q Developer Pro for the first time. For more
  information about this profile and the Regions where it's supported, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md "subscribe-understanding-profile.md"), and [Supported Regions for the Q Developer
  console and Q Developer profile](q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions "q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions").
- Be in the AWS account where users are subscribed. If users are subscribed in multiple
  AWS accounts, then you must create buckets in each of those accounts. Cross-account buckets
  are not supported.
- (Optional but recommended) Be different from the bucket you might be using for [prompt logging](q-admin-prompt-logging.md "q-admin-prompt-logging.md").
- Include a prefix, also known as a subfolder, where Amazon Q will save the CSV file. The CSV file
  cannot be saved in the root of the bucket.
- Have a bucket policy like the one that follows. Replace
  `bucketName`, `region`,
  `accountId`, and `prefix` with your own
  information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QDeveloperLogsWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "q.amazonaws.com"
 },
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucketName`/`prefix`/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:codewhisperer:`us-east-1`:`111122223333`:*"
 }
 }
 }
 ]
}`

```

If you're configuring SSE-KMS on the bucket, add the below policy on the KMS key:

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "q.amazonaws.com"
    },
    "Action": "kms:GenerateDataKey",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`accountId`"
        },
        "ArnLike": {
           "aws:SourceArn": "arn:aws:codewhisperer:`region`:`accountId`:*"
        }
    }
}
```

To learn about protecting the data in your Amazon S3 bucket, see [Protecting data with
encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") in the _Amazon Simple Storage Service User Guide_.

###### To enable user activity reports

1. Open the Amazon Q Developer console.

To use the Amazon Q Developer console, you must have the permissions defined in [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users"). 2. Choose **Settings**. 3. Under **Q Developer user activity reports**, choose
**Edit**. 4. Toggle **Collect granular metrics per user**. 5. Under **S3 location**, enter the Amazon S3 URI that you will use to hold the CSV
reports. Example: `s3://amzn-s3-demo-bucket/user-activity-reports/`
