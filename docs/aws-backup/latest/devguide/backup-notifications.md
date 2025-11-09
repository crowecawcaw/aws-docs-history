# Notification options with AWS Backup

There are two ways to receive notifications about AWS Backup:

- User Notifications can send notifications, including Amazon CloudWatch alarms, AWS Support,
  and other services' notifications.
- Amazon Simple Notification Service can notify you of AWS Backup events.

## User Notifications and AWS Backup

AWS Backup supports management of your backup notifications from the [User Notifications
console](https://console.aws.amazon.com/notifications/home?notifications#/notifications "https://console.aws.amazon.com/notifications/home?notifications#/notifications"). With [User Notifications](../../../notifications/latest/userguide/getting-started.md "../../../notifications/latest/userguide/getting-started.md"), you can view the progress of your backup, copy, and restore jobs
and changes to your backup policies, vaults, recovery points, and settings from the User
Notifications Notification Center.

Amazon CloudWatch, Amazon EventBridge alarms, and AWS Support case updates are among other types of
notifications you can manage from the console. Additionally, you can set up several delivery
options, including email, Amazon Q Developer in chat applications notifications, and AWS Console Mobile Application push notifications.

## Amazon SNS and AWS Backup events

AWS Backup takes advantage of the robust notifications delivered by Amazon Simple Notification Service (Amazon SNS). You
can configure Amazon SNS to notify you of AWS Backup events from the Amazon SNS console.

###### Limitations

- While the Amazon SNS service allows cross-account notifications, AWS Backup does not currently
  support this feature. You must specify your own AWS account ID and the resource ARN of
  your topic.
- AWS Backup supports Standard topics for SNS best-effort deduplication, but AWS Backup does not
  currently support SNS FIFO topics for Strict deduplication.

### Common use cases

- Set up notifications for failed backup jobs by following the steps in [How can I
  get notifications for AWS Backup jobs that failed?](https://repost.aws/knowledge-center/aws-backup-failed-job-notification "https://repost.aws/knowledge-center/aws-backup-failed-job-notification") from AWS Premium
  Support.
- Review sample Amazon SNS notification JSONs for completed, failed, and expired backup
  jobs in the Examples of events table below.

For more information about Amazon SNS generally, see [Getting Started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the
_Amazon Simple Notification Service Developer Guide_.

### AWS Backup notification APIs

After creating your topics using the Amazon SNS console or AWS Command Line Interface (AWS CLI), you can use
the following AWS Backup API operations to manage your backup notifications.

- [DeleteBackupVaultNotifications](API_DeleteBackupVaultNotifications.md "API_DeleteBackupVaultNotifications.md") — Deletes event
  notifications for the specified backup vault.
- [GetBackupVaultNotifications](API_GetBackupVaultNotifications.md "API_GetBackupVaultNotifications.md") — Lists all event
  notifications for the specified backup vault.
- [PutBackupVaultNotifications](API_PutBackupVaultNotifications.md "API_PutBackupVaultNotifications.md") — Turns on notifications
  for the specified topic and events.

AWS Backup supports the following events:

| Job type                | Event                            |
| ----------------------- | -------------------------------- | ------------------------------ | ------------------------------------ |
| Backup job              | `BACKUP_JOB_STARTED`             | `BACKUP_JOB_COMPLETED`         | <br>`CONTINUOUS_BACKUP_INTERRUPTED`  |
| Copy job                | `COPY_JOB_STARTED`               | `COPY_JOB_SUCCESSFUL`          | <br>`COPY_JOB_FAILED`                |
| Restore job             | `RESTORE_JOB_STARTED`            | `RESTORE_JOB_COMPLETED`        |
| Recovery point          | `RECOVERY_POINT_MODIFIED`        |
| Recovery point indexing | `RECOVERY_POINT_INDEX_COMPLETED` | `RECOVERY_POINT_INDEX_DELETED` | <br>`RECOVERY_POINT_INDEXING_FAILED` |

AWS Backup for S3 supports two additional events:

- `S3_BACKUP_OBJECT_FAILED` notifies you of any S3 object that AWS Backup
  failed to back up during a backup job.
- `S3_RESTORE_OBJECT_FAILED` notifies you of any S3 object that AWS Backup
  failed to restore during a restore job.

### Examples of events

###### Example: Backup job completed

```
{
    "Records": [{
        "EventSource": "aws:sns",
        "EventVersion": "1.0",
        "EventSubscriptionArn": "arn:aws:sns:...-a3802aa1ed45",
        "Sns": {
            "Type": "Notification",
            "MessageId": "12345678-abcd-123a-def0-abcd1a234567",
            "TopicArn": "arn:aws:sns:us-west-1:123456789012:backup-2sqs-sns-topic",
            "Subject": "Notification from AWS Backup",
            "Message": "An AWS Backup job was completed successfully. Recovery point ARN: arn:aws:ec2:us-west-1:123456789012:volume/vol-012f345df6789012d. Resource ARN : arn:aws:ec2:us-west-1:123456789012:volume/vol-012f345df6789012e. BackupJob ID : 1b2345b2-f22c-4dab-5eb6-bbc7890ed123",
            "Timestamp": "2019-08-02T18:46:02.788Z",
            ...
            "MessageAttributes": {
                "EventType": {"Type":"String","Value":"BACKUP_JOB"},
                "State": {"Type":"String","Value":"COMPLETED"},
                "AccountId": {"Type":"String","Value":"123456789012"},
                "Id": {"Type":"String","Value":"1b2345b2-f22c-4dab-5eb6-bbc7890ed123"},
                "StartTime": {"Type":"String","Value":"2019-09-02T13:48:52.226Z"}
            }
        }
    }]
}
```

###### Example: Backup job failed

```
{
    "Records": [{
        "EventSource": "aws:sns",
        "EventVersion": "1.0",
        "EventSubscriptionArn": "arn:aws:sns:...-a3802aa1ed45",
        "Sns": {
            "Type": "Notification",
            "MessageId": "12345678-abcd-123a-def0-abcd1a234567",
            "TopicArn": "arn:aws:sns:us-west-1:123456789012:backup-2sqs-sns-topic",
            "Subject": "Notification from AWS Backup",
            "Message": "An AWS Backup job failed. Resource ARN : arn:aws:ec2:us-west-1:123456789012:volume/vol-012f345df6789012e. BackupJob ID : 1b2345b2-f22c-4dab-5eb6-bbc7890ed123",
            "Timestamp": "2019-08-02T18:46:02.788Z",
            ...
            "MessageAttributes": {
                "EventType": {"Type":"String","Value":"BACKUP_JOB"},
                "State": {"Type":"String","Value":"FAILED"},
                "AccountId": {"Type":"String","Value":"123456789012"},
                "Id": {"Type":"String","Value":"1b2345b2-f22c-4dab-5eb6-bbc7890ed123"},
                "StartTime": {"Type":"String","Value":"2019-09-02T13:48:52.226Z"}
            }
        }
    }]
}
```

###### Example: Backup job could not complete during the backup window

```
{
    "Records": [{
        "EventSource": "aws:sns",
        "EventVersion": "1.0",
        "EventSubscriptionArn": "arn:aws:sns:...-a3802aa1ed45",
        "Sns": {
            "Type": "Notification",
            "MessageId": "12345678-abcd-123a-def0-abcd1a234567",
            "TopicArn": "arn:aws:sns:us-west-1:123456789012:backup-2sqs-sns-topic",
            "Subject": "Notification from AWS Backup",
            "Message": "An AWS Backup job failed to complete in time. Resource ARN : arn:aws:ec2:us-west-1:123456789012:volume/vol-012f345df6789012e. BackupJob ID : 1b2345b2-f22c-4dab-5eb6-bbc7890ed123",
            "Timestamp": "2019-08-02T18:46:02.788Z",
            ...
            "MessageAttributes" : {
              "EventType" : {"Type":"String","Value":"BACKUP_JOB"},
              "State" : {"Type":"String","Value":"EXPIRED"},
              "AccountId" : {"Type":"String","Value":"123456789012"},
              "Id" : {"Type":"String","Value":"1b2345b2-f22c-4dab-5eb6-bbc7890ed123"},
              "StartTime" : {"Type":"String","Value":"2019-09-02T13:48:52.226Z"}
            }
        }
    }]
}
```

###### Example: Recovery point indexing completed

```
{
    "Records": [{
        "EventSource": "aws:sns",
        "EventVersion": "1.0",
        "EventSubscriptionArn": "arn:aws:sns:...-a3802aa1ed45",
        "Sns": {
            "Type": "Notification",
            "MessageId": "12345678-abcd-123a-def0-abcd1a234567",
            "TopicArn": "arn:aws:sns:us-west-1:123456789012:backup-2sqs-sns-topic",
            "Subject": "Notification from AWS Backup",
            "Message": "An AWS Backup backup index job was completed. Indexed recovery point arn: arn:aws:backup:us-west-2:1112233445566:recovery-point:abcd1234-5678-abcd-9012-abcdef123456",
            "Timestamp": "2025-05-25T18:46:02.788Z",
            ...
            "MessageAttributes" : {
              "EventType" : {"Type":"String","Value":"RECOVERY_POINT_INDEXING_COMPLETED"},
              "AccountId" : {"Type":"String","Value":"123456789012"},
              "IndexStatus" : {"Type":"String","Value":"ACTIVE"},
              "IsIndexingContinuous" : {"Type":"String","Value":"false"},
               "RecoveryPointArn" : {"Type":"String","Value":"arn:aws:backup:us-west-2:1112233445566:recovery-point:abcd1234-5678-abcd-9012-abcdef123456"}
            }
        }
    }]
}
```

### AWS Backup notification command examples

You can use AWS CLI commands to subscribe to, list, and delete Amazon SNS notifications for
your AWS Backup events.

#### Example put backup vault

notification

The following command subscribes to an Amazon SNS topic for the specified backup vault
that notifies you when a restore job is started or completed, or when a recovery point
is modified.

```
aws backup put-backup-vault-notifications
    --backup-vault-name `myBackupVault`
    --sns-topic-arn arn:aws:sns:`region`:`account-id`:`myBackupTopic`
    --backup-vault-events RESTORE_JOB_STARTED RESTORE_JOB_COMPLETED RECOVERY_POINT_MODIFIED
```

#### Example get backup vault

notification

The following command lists all events currently subscribed to an Amazon SNS topic for
the specified backup vault.

```
aws backup get-backup-vault-notifications
    --backup-vault-name `myVault`
```

The sample output is as follows:

```
{
    "SNSTopicArn": "arn:aws:sns:region:account-id:myBackupTopic",
    "BackupVaultEvents": [
        "RESTORE_JOB_STARTED",
        "RESTORE_JOB_COMPLETED",
        "RECOVERY_POINT_MODIFIED"
    ],
    "BackupVaultName": "myVault",
    "BackupVaultArn": "arn:aws:backup:region:account-id:backup-vault:myVault"
}
```

#### Example delete backup vault

notification

The following command unsubscribes from an Amazon SNS topic for the specified backup
vault.

```
aws backup delete-backup-vault-notifications
    --backup-vault-name `myVault`
```

### Specifying AWS Backup as a

service principal

###### Note

To allow AWS Backup to publish SNS topics on your behalf, you must specify AWS Backup as a
service principal.

Include the following JSON in the access policy of the Amazon SNS topic that you use to
track AWS Backup events. You must specify the resource Amazon Resource Name (ARN) of your
topic.

```
{
      "Sid": "My-statement-id",
      "Effect": "Allow",
      "Principal": {
        "Service": "backup.amazonaws.com"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:`region`:`account-id`:`myTopic`"
}
```

For more information about specifying a service principal in an Amazon SNS access policy,
see [Allowing Any AWS Resource to Publish to a Topic](../../../sns/latest/dg/AccessPolicyLanguage_UseCases_Sns.md#AccessPolicyLanguage_UseCase4_Sns "../../../sns/latest/dg/AccessPolicyLanguage_UseCases_Sns.md#AccessPolicyLanguage_UseCase4_Sns") in the
_Amazon Simple Notification Service Developer Guide_.

###### Note

If your topic is encrypted, you must include additional permissions in your policy
to allow AWS Backup to publish to it. For more information about enabling services to publish
to encrypted topics, see [Enable
Compatibility between Event Sources from AWS Services and Encrypted Topics](../../../sns/latest/dg/sns-key-management.md#sns-what-permissions-for-sse "../../../sns/latest/dg/sns-key-management.md#sns-what-permissions-for-sse")
in the _Amazon Simple Notification Service Developer Guide_.
