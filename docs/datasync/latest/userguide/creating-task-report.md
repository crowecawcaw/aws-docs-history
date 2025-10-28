# Creating your DataSync task reports

AWS DataSync task reports can be only a summary of your task execution or a set of
detailed reports about what DataSync attempts to transfer, skip, verify, and delete.

## Prerequisites

Before you can create a task report, you must do the following.

###### Topics

- [Create an S3 bucket for your task reports](#setting-up-task-report-create-bucket "#setting-up-task-report-create-bucket")
- [Allow DataSync to upload task reports to your S3
  bucket](#task-report-access "#task-report-access")

### Create an S3 bucket for your task reports

If you don't already have one, [create an S3
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") where DataSync can upload your task report. Reports are stored in
the S3 Standard storage class.

We recommend the following for this bucket:

- If you're planning to transfer data to an S3 bucket, don't use the same bucket for your task report if you [disable the Keep deleted files option](configure-metadata.md "configure-metadata.md"). Otherwise, DataSync will delete any previous task reports each time you execute a task since those reports don't exist in your source location.
- To avoid a complex access permissions setup, make sure that your task
  report bucket is in the same AWS account and Region as your DataSync transfer
  task.

### Allow DataSync to upload task reports to your S3

bucket

You must configure an AWS Identity and Access Management (IAM) role that allows DataSync to upload a task
report to your S3 bucket.

In the DataSync console, you can create an IAM role that in most cases
automatically includes the permissions to upload a task report to your bucket. Keep
in mind that this automatically generated role might not meet your needs from a
least-privilege standpoint. This role also won't work if your bucket is encrypted
with a customer managed AWS Key Management Service (AWS KMS) key (SSE-KMS). In these cases, you can
create the role manually as long as the role does at least the following:

- [Prevents the cross-service confused deputy problem](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md") in the
  role's trusted entity.

The following full example shows how you can use the
`aws:SourceArn` and `aws:SourceAccount` global
condition context keys to prevent the confused deputy problem with DataSync.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "datasync.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:datasync:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

- Allows DataSync to upload a task report to your S3 bucket.

The following example does this by including the `s3:PutObject`
action only for a specific prefix (`reports/`) in your
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Action": [
 "s3:PutObject"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::`your-task-reports-bucket`/reports/*"
 }]
}`

```

- If your S3 bucket is encrypted with a customer managed SSE-KMS key, the
  [key's
  policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md") must include the IAM role that DataSync uses to access the
  bucket.

For more information, see [Accessing S3 buckets using
server-side encryption](create-s3-location.md#create-s3-location-encryption "create-s3-location.md#create-s3-location-encryption").

## Creating a summary only task

report

You can configure a task report that includes a [summary only](task-reports.md#task-report-types-summary "task-reports.md#task-report-types-summary") when creating your DataSync
task, starting your task, or updating your task.

The following steps show how to configure a summary only task report when creating a
task.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and
   then choose **Create task**.
3. Configure your task's source and destination locations.

For more information, see [Where can I transfer my data with
AWS DataSync?](working-with-locations.md "working-with-locations.md") 4. Scroll down to the **Task report** section. For
**Report type**, choose **Summary
only**. 5. For **S3 bucket for reports**, choose an S3 bucket
where you want DataSync to upload your task report.

###### Tip

If you're planning to transfer data to an S3 bucket, don't use the same bucket for your task report if you [disable the Keep deleted files option](configure-metadata.md "configure-metadata.md"). Otherwise, DataSync will delete any previous task reports each time you execute a task since those reports don't exist in your source location. 6. For **Folder**, enter a prefix to use for your task
report when DataSync uploads the report to your S3 bucket (for example,
`reports/`).

Make sure to include the appropriate delimiter character at the end of
your prefix. This character is usually a forward slash (`/`).
For more information, see [Organizing
objects by using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the _Amazon S3 User Guide_. 7. For **IAM role**, do one of the following:

    * Choose **Autogenerate** to have DataSync
     automatically create an IAM role with the permissions that are
     required to access the S3 bucket.


    If DataSync previously created an IAM role for this S3 bucket,
     that role is chosen by default.
    * Choose a custom IAM role that you created.


    In some cases, you might need to create the role yourself. For
     more information, see [Allow DataSync to upload task reports to your S3
     bucket](#task-report-access "#task-report-access").


    ###### Important

    If your S3 bucket is encrypted with a customer managed
     SSE-KMS key, the key's policy must include the IAM role
     that DataSync uses to access the bucket.

    For more information, see [Accessing S3 buckets using
     server-side encryption](create-s3-location.md#create-s3-location-encryption "create-s3-location.md#create-s3-location-encryption").

8. Finish creating your task, and then [start the
   task](run-task.md "run-task.md") to begin transferring your data.
   When your transfer is complete, you can [view your
   task report](task-report-viewing.md "task-report-viewing.md").

1. Copy the following `create-task` AWS Command Line Interface (AWS CLI)
   command:

```
aws datasync create-task \
  --source-location-arn arn:aws:datasync:`us-east-1`:`123456789012`:location/loc-`12345678abcdefgh` \
  --destination-location-arn arn:aws:datasync:`us-east-1`:`123456789012`:location/loc-`abcdefgh12345678` \
  --task-report-config '{
    "Destination":{
      "S3":{
        "Subdirectory":"`reports/`",
        "S3BucketArn":"arn:aws:s3:::`your-task-reports-bucket`",
        "BucketAccessRoleArn":"arn:aws:iam::`123456789012`:role/`bucket-iam-role`"
        }
    },
    "OutputType":"SUMMARY_ONLY"
  }'
```

2. For the `--source-location-arn` parameter, specify the
   Amazon Resource Name (ARN) of the source location in your transfer.
   Replace `us-east-1` with the
   appropriate AWS Region, replace
   `123456789012` with the
   appropriate AWS account number, and replace
   `12345678abcdefgh` with
   the appropriate source location ID.
3. For the `--destination-location-arn` parameter, specify the
   ARN of the destination location in your transfer. Replace
   `us-east-1` with the
   appropriate AWS Region, replace
   `123456789012` with the
   appropriate AWS account number, and replace
   `abcdefgh12345678` with
   the appropriate destination location ID.
4. For the `--task-report-config` parameter, do the
   following:
   - `Subdirectory` – Replace
     `reports/` with
     the prefix in your S3 bucket where you want DataSync to upload your
     task reports.

   Make sure to include the appropriate delimiter character at
   the end of your prefix. This character is usually a forward
   slash (`/`). For more information, see [Organizing objects by using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the
   _Amazon S3 User Guide_.
   - `S3BucketArn` – Specify the ARN of the S3
     bucket where you want to upload your task report.

   ###### Tip

   If you're planning to transfer data to an S3 bucket, don't use the same bucket for your task report if you [disable the Keep deleted files option](configure-metadata.md "configure-metadata.md"). Otherwise, DataSync will delete any previous task reports each time you execute a task since those reports don't exist in your source location.
   - `BucketAccessRoleArn` – Specify the IAM
     role that allows DataSync to upload a task report to your S3
     bucket.

   For more information, see [Allow DataSync to upload task reports to your S3
   bucket](#task-report-access "#task-report-access").

   ###### Important

   If your S3 bucket is encrypted with a customer managed
   SSE-KMS key, the key's policy must include the IAM role
   that DataSync uses to access the bucket.

   For more information, see [Accessing S3 buckets using
   server-side encryption](create-s3-location.md#create-s3-location-encryption "create-s3-location.md#create-s3-location-encryption").
   - `OutputType` – Specify
     `SUMMARY_ONLY`.

   For more information, see [Summary only task reports](task-reports.md#task-report-types-summary "task-reports.md#task-report-types-summary").

5. Run the `create-task` command to create your task.

You get a response like the following that shows you the ARN of the
task that you created. You will need this ARN to run the
`start-task-execution` command.

```
{
    "TaskArn": "arn:aws:datasync:us-east-1:123456789012:task/task-12345678abcdefgh"
}
```

6. Copy the following `start-task-execution` command.

```
aws datasync-task-report start-task-execution \
  --task-arn arn:aws:datasync:`us-east-1`:`123456789012`:task/task-`12345678abcdefgh`
```

7. For the `--task-arn` parameter, specify the ARN of the task
   that you're starting. Use the ARN that you received from running the
   `create-task` command.
8. Run the `start-task-execution` command.
   When your transfer is complete, you can [view your
   task report](task-report-viewing.md "task-report-viewing.md").

## Creating a standard task report

You can configure a [standard task
report](task-reports.md#task-report-types-standard "task-reports.md#task-report-types-standard") when creating your DataSync task, starting your task, or updating your
task.

The following steps show how to configure a standard task report when creating a
task.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and
   then choose **Create task**.
3. Configure your task's source and destination locations.

For more information, see [Where can I transfer my data with
AWS DataSync?](working-with-locations.md "working-with-locations.md") 4. Scroll down to the **Task report** section. For
**Report type**, choose **Standard
report**. 5. For **Report level**, choose one of the
following:

    * **Errors only** – Your task report
     includes only issues with what DataSync tried to transfer, skip,
     verify, and delete.
    * **Successes and errors** – Your task
     report includes what DataSync successfully transferred, skipped,
     verified, and deleted and what it didn't.
    * **Custom** – Allows you to choose
     whether you want to see errors only or successes and errors for
     specific aspects of your task report.


    For example, you can choose **Successes and
     errors** for the transferred files list but
     **Errors only** for the rest of the
     report.

6. If you're transferring to an S3 bucket that uses object versioning,
   keep **Include Amazon S3 object versions** selected if
   you want your report to include the new version for each transferred
   object.
7. For **S3 bucket for reports**, choose an S3 bucket
   where you want DataSync to upload your task report.

###### Tip

If you're planning to transfer data to an S3 bucket, don't use the same bucket for your task report if you [disable the Keep deleted files option](configure-metadata.md "configure-metadata.md"). Otherwise, DataSync will delete any previous task reports each time you execute a task since those reports don't exist in your source location. 8. For **Folder**, enter a prefix to use for your task
report when DataSync uploads the report to your S3 bucket (for example,
`reports/`). Make sure to include the
appropriate delimiter character at the end of your prefix. This
character is usually a forward slash (`/`). For more
information, see [Organizing
objects by using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the _Amazon S3 User Guide_. 9. For **IAM role**, do one of the following:

    * Choose **Autogenerate** to have DataSync
     automatically create an IAM role with the permissions that are
     required to access the S3 bucket.


    If DataSync previously created an IAM role for this S3 bucket,
     that role is chosen by default.
    * Choose a custom IAM role that you created.


    In some cases, you might need to create the role yourself. For
     more information, see [Allow DataSync to upload task reports to your S3
     bucket](#task-report-access "#task-report-access").


    ###### Important

    If your S3 bucket is encrypted with a customer managed
     SSE-KMS key, the key's policy must include the IAM role
     that DataSync uses to access the bucket.

    For more information, see [Accessing S3 buckets using
     server-side encryption](create-s3-location.md#create-s3-location-encryption "create-s3-location.md#create-s3-location-encryption").

10. Finish creating your task and [start the
    task](run-task.md "run-task.md") to begin transferring your data.
    When your transfer is complete, you can [view your
    task report](task-report-viewing.md "task-report-viewing.md").

1. Copy the following `create-task` command:

```
aws datasync create-task \
  --source-location-arn arn:aws:datasync:`us-east-1`:`123456789012`:location/loc-`12345678abcdefgh` \
  --destination-location-arn arn:aws:datasync:`us-east-1`:`123456789012`:location/loc-`abcdefgh12345678` \
  --task-report-config '{
    "Destination":{
      "S3":{
        "Subdirectory":"`reports/`",
        "S3BucketArn":"arn:aws:s3:::`your-task-reports-bucket`",
        "BucketAccessRoleArn":"arn:aws:iam::`123456789012`:role/`bucket-iam-role`"
        }
    },
    "OutputType":"STANDARD",
    "ReportLevel":"`level-of-detail`",
    "ObjectVersionIds":"`include-or-not`"
  }'
```

2. For the `--source-location-arn` parameter, specify the ARN
   of the source location in your transfer. Replace
   `us-east-1` with the
   appropriate AWS Region, replace
   `123456789012` with the
   appropriate AWS account number, and replace
   `12345678abcdefgh` with
   the appropriate source location ID.
3. For the `--destination-location-arn` parameter, specify the
   ARN of the destination location in your transfer. Replace
   `us-east-1` with the
   appropriate AWS Region, replace
   `123456789012` with the
   appropriate AWS account number, and replace
   `abcdefgh12345678` with
   the appropriate destination location ID.
4. For the `--task-report-config` parameter, do the
   following:
   - `Subdirectory` – Replace
     `reports/` with
     the prefix in your S3 bucket where you want DataSync to upload your
     task reports. Make sure to include the appropriate delimiter
     character at the end of your prefix. This character is usually a
     forward slash (`/`). For more information, see [Organizing objects by using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the
     _Amazon S3 User Guide_.
   - `S3BucketArn` – Specify the ARN of the S3
     bucket where you want to upload your task report.

   ###### Tip

   If you're planning to transfer data to an S3 bucket, don't use the same bucket for your task report if you [disable the Keep deleted files option](configure-metadata.md "configure-metadata.md"). Otherwise, DataSync will delete any previous task reports each time you execute a task since those reports don't exist in your source location.
   - `BucketAccessRoleArn` – Specify the IAM
     role that allows DataSync to upload a task report to your S3
     bucket.

   For more information, see [Allow DataSync to upload task reports to your S3
   bucket](#task-report-access "#task-report-access").

   ###### Important

   If your S3 bucket is encrypted with a customer managed
   SSE-KMS key, the key's policy must include the IAM role
   that DataSync uses to access the bucket.

   For more information, see [Accessing S3 buckets using
   server-side encryption](create-s3-location.md#create-s3-location-encryption "create-s3-location.md#create-s3-location-encryption").
   - `OutputType` – Specify `STANDARD`
     report.

   For more information, see [Standard task reports](task-reports.md#task-report-types-standard "task-reports.md#task-report-types-standard")Types of task reports.
   - (Optional) `ReportLevel` – Specify whether
     you want `ERRORS_ONLY` (the default) or
     `SUCCESSES_AND_ERRORS` in your report.
   - (Optional) `ObjectVersionIds` – If you're
     transferring to an S3 bucket that uses object versioning,
     specify `NONE` if you don't want to include the new
     version for each transferred object in the report.

   By default, this option is set to `INCLUDE`.
   - (Optional) `Overrides` – Customize the
     `ReportLevel` of a particular aspect of your
     report.

   For example, you might want to see
   `SUCCESSES_AND_ERRORS` for the list of what DataSync
   deletes in your destination location, but you want
   `ERRORS_ONLY` for everything else. In this
   example, you would add the following `Overrides`
   option to the `--task-report-config`
   parameter:

   ```
   "Overrides":{
     "Deleted":{
       "ReportLevel":"SUCCESSES_AND_ERRORS"
     }
   }
   ```

   If you don't use `Overrides`, your entire report
   uses the `ReportLevel` that you specify.

5. Run the `create-task` command to create your task.

You get a response like the following that shows you the ARN of the
task that you created. You will need this ARN to run the
`start-task-execution` command.

```
{
    "TaskArn": "arn:aws:datasync:us-east-1:123456789012:task/task-12345678abcdefgh"
}
```

6. Copy the following `start-task-execution` command.

```
aws datasync-task-report start-task-execution \
  --task-arn arn:aws:datasync:`us-east-1`:`123456789012`:task/task-`12345678abcdefgh`
```

7. For the `--task-arn` parameter, specify the ARN of the task
   you're running. Use the ARN that you received from running the
   `create-task` command.
8. Run the `start-task-execution` command.
   When your transfer is complete, you can [view your
   task report](task-report-viewing.md "task-report-viewing.md").
