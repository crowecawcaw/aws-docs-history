# Restore an Amazon Timestream table

When you restore a Amazon Timestream table, there are several options to configure, including
the new table name, the destination database, your storage allocation preferences (memory
and magnetic storage), and which role you’ll use to complete the restore job. You can also
choose an Amazon S3 bucket in which to store error logs. Magnetic storage writes are
asynchronous, so you may wish you log the errors.

Timestream data storage has two tiers: a memory store and a magnetic store. Memory store is
required, but you have the option of transferring your restored table to magnetic storage
after the specified memory time is finished. Memory store is optimized for high throughput
data writes and fast point-in-time queries. The magnetic store is optimized for lower
throughput late-arrival data writes, long-term data storage, and fast analytical
queries.

When you restore a Timestream table, you determine how long you want the table to remain in
each storage tier. Using the console or API, you can set the storage time for both. Note
that the storage is linear and sequential. Timestream will store your restored table in memory
storage first, then automatically transition it to magnetic storage when the memory storage
time has been reached.

###### Note

The magnetic store retention period must be equal or greater than the original
retention period (shown at the top-right of the console), or data will be lost.

_Example:_ You set the memory store allocation to hold data for one
week and set the magnetic store allocation to hold the same data for one year. When the data
in the memory store becomes a week old, it is automatically moved to the magnetic store. It
is then retained in the magnetic store for a year. At the end of that time, it is deleted
from Timestream and from AWS Backup.

## To restore a Amazon Timestream table using the AWS Backup console

You can restore Timestream tables in the AWS Backup console that were created by AWS Backup.

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources** and the
   Amazon Timestream resource ID that you want to restore.
3. On the **Resource details** page, a list of recovery points for
   the selected resource ID is shown. To restore a resource, in the
   **Backups** pane, choose the radio button next to the recovery
   point ID of the resource. In the upper-right corner of the pane, choose
   **Restore**.
4. Specify your new table configuration settings, including:
   1. **New table name**, consisting of 2 to 256 characters
      (letters, numbers, dashes, periods, and underscores).
   2. **Destination database**, chosen from the drop down
      menu.

5. **Storage allocation**: Set the amount of time the restored table
   will first reside in [memory storage](../../../timestream/latest/developerguide/storage.md "../../../timestream/latest/developerguide/storage.md"), and set
   the amount of time the restored table will then reside in [magnetic storage](../../../timestream/latest/developerguide/storage.md "../../../timestream/latest/developerguide/storage.md"). Memory
   storage can be set to hours, days, weeks, or months. Magnetic storage can be set to
   days, weeks, months, or years.
6. _(Optional)_ **Enable magnetic storage
   writes**: You have the option of allowing magnetic storage writes. With
   this option checked, late-arriving data, which is data with a timestamp outside the
   memory storage retention period, will be written directly into the magnetic
   store.
7. _(Optional)_
   **Amazon S3 error logs location**: You can specify an S3 location in which
   your error logs will be stored. Browse your S3 files or copy and paste the S3 file
   path.

###### Note

If you choose to specify an S3 error log location, the role you use for this
restore must have permission to write to an S3 bucket or it must contain a policy
with that permission. 8. Choose the IAM role to be passed to perform restores. You can use the default IAM
role or specify a different one. 9. Click **Restore backup**.

Your restore jobs will be visible under protected resources. You can see the current
status of your restore job by clicking the refresh button or CTRL-R.

## To restore a Amazon Timestream table using API, CLI, or SDK

Use [`StartRestoreJob` to restore a Timestream table via API.](API_StartRestoreJob.md "API_StartRestoreJob.md").

To restore a Timestream using the AWS CLI, use the operation `start-restore-job.`
and specify the following metadata:

```
TableName: string;
DestinationDatabase: string;
MemoryStoreRetentionPeriodInHours: value: number unit: 'hours' | 'days' | 'weeks' | 'months'
MagneticStoreRetentionPeriodInDays: value: number unit: 'days' | 'weeks' | 'months' | 'years'
EnableMagneticStoreWrites?: boolean;
aws:backup:request-id
```

Here is an example template:

```
aws backup start-restore-job \
--recovery-point-arn "arn:aws:backup:us-west-2:`accountnumber`:recovery-point:1a2b3cde-f405-6789-012g-3456hi789012_beta" \
--iam-role-arn "arn:aws:iam::`accountnumber`:role/`rolename`" \
--metadata 'TableName=`tablename`,DatabaseName=`databasename`,MagneticStoreRetentionPeriodInDays=1,MemoryStoreRetentionPeriodInHours=1,MagneticStoreWriteProperties="{\"EnableMagneticStoreWrites\":true,\"MagneticStoreRejectedDataLocation\":{\"S3Configuration\":{\"BucketName\":\"`bucketname`\",\"EncryptionOption\":\"SSE_S3\"}}}"' \
--region us-west-2 \
--endpoint-url `url`
```

You can also use [`DescribeRestoreJob`](API_DescribeRestoreJob.md "API_DescribeRestoreJob.md") to assist with restore information.

In the AWS CLI, use the operation `describe-restore-job` and use the
following metadata:

```
TableName: string;
DestinationDatabase: string;
MemoryStoreRetentionPeriodInHours: value: number unit: 'hours' | 'days' | 'weeks' | 'months'
MagneticStoreRetentionPeriodInDays: value: number unit: 'days' | 'weeks' | 'months' | 'years'
EnableMagneticStoreWrites?: boolean;
```

Here is an example template:

```
aws backup describe-restore-job \
--restore-job-id `restore job ID` \
--region `awsregion` \
--endpoint-url `url`
```
