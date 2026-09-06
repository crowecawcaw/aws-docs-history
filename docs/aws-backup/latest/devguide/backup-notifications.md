

# Notification options with AWS Backup
<a name="backup-notifications"></a>

There are two ways to receive notifications about AWS Backup:
+ User Notifications can send notifications, including Amazon CloudWatch alarms, AWS Support, and other services' notifications.
+ Amazon Simple Notification Service can notify you of AWS Backup events.

## User Notifications and AWS Backup
<a name="aws-backup-uno"></a>

AWS Backup supports management of your backup notifications from the [User Notifications console](https://console.aws.amazon.com/notifications/home?notifications#/notifications). With [User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html), you can view the progress of your backup, copy, and restore jobs and changes to your backup policies, vaults, recovery points, and settings from the User Notifications Notification Center.

Amazon CloudWatch, Amazon EventBridge alarms, and AWS Support case updates are among other types of notifications you can manage from the console. Additionally, you can set up several delivery options, including email, Amazon Q Developer in chat applications notifications, and AWS Console Mobile Application push notifications.

## Amazon SNS and AWS Backup events
<a name="backup-notifications-section"></a>

AWS Backup takes advantage of the robust notifications delivered by Amazon Simple Notification Service (Amazon SNS). You can configure Amazon SNS to notify you of AWS Backup events from the Amazon SNS console.

**Limitations**
+ While the Amazon SNS service allows cross-account notifications, AWS Backup does not currently support this feature. You must specify your own AWS account ID and the resource ARN of your topic.
+ AWS Backup supports Standard topics for SNS best-effort deduplication, but AWS Backup does not currently support SNS FIFO topics for Strict deduplication.

### Common use cases
<a name="aws-backup-sns-console"></a>
+ Set up notifications for failed backup jobs by following the steps in [How can I get notifications for AWS Backup jobs that failed?](https://repost.aws/knowledge-center/aws-backup-failed-job-notification) from AWS Premium Support.
+ Review sample Amazon SNS notification JSONs for completed, failed, and expired backup jobs in the Examples of events table below.

For more information about Amazon SNS generally, see [Getting Started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the *Amazon Simple Notification Service Developer Guide*.

### AWS Backup notification APIs
<a name="aws-backup-sns-apis"></a>

After creating your topics using the Amazon SNS console or AWS Command Line Interface (AWS CLI), you can use the following AWS Backup API operations to manage your backup notifications.
+ [DeleteBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupVaultNotifications.html) — Deletes event notifications for the specified backup vault.
+ [GetBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetBackupVaultNotifications.html) — Lists all event notifications for the specified backup vault.
+ [PutBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_PutBackupVaultNotifications.html) — Turns on notifications for the specified topic and events.

AWS Backup supports the following events:


| Job type | Event | 
| --- | --- | 
| Backup job | BACKUP\_JOB\_STARTED \| BACKUP\_JOB\_COMPLETED \| BACKUP\_JOB\_SUCCESSFUL \| BACKUP\_JOB\_FAILED \| BACKUP\_JOB\_EXPIRED \| CONTINUOUS\_BACKUP\_INTERRUPTED | 
| Copy job | COPY\_JOB\_STARTED \| COPY\_JOB\_SUCCESSFUL \| COPY\_JOB\_FAILED | 
| Restore job | RESTORE\_JOB\_STARTED \| RESTORE\_JOB\_COMPLETED \| RESTORE\_JOB\_SUCCESSFUL \| RESTORE\_JOB\_FAILED | 
| Recovery point | RECOVERY\_POINT\_MODIFIED | 
| Recovery point indexing | RECOVERY\_POINT\_INDEX\_COMPLETED \| RECOVERY\_POINT\_INDEX\_DELETED \| RECOVERY\_POINT\_INDEXING\_FAILED | 
| Access point | ACCESS\_POINT\_AVAILABLE \| ACCESS\_POINT\_CREATION\_FAILED \| ACCESS\_POINT\_DELETED \| ACCESS\_POINT\_DELETION\_FAILED \| ACCESS\_POINT\_EXPIRED \| ACCESS\_POINT\_DISASSOCIATED | 

AWS Backup for S3 supports two additional events:
+ `S3_BACKUP_OBJECT_FAILED` notifies you of any S3 object that AWS Backup failed to back up during a backup job.
+ `S3_RESTORE_OBJECT_FAILED` notifies you of any S3 object that AWS Backup failed to restore during a restore job.

AWS Backup for EKS supports three additional events:
+ `EKS_BACKUP_OBJECT_FAILED` notifies you of any EKS objects that AWS Backup failed to back up during a backup job.
+ `EKS_RESTORE_OBJECT_FAILED` notifies you of any EKS objects that AWS Backup failed to restore during a restore job.
+ `EKS_RESTORE_OBJECT_SKIPPED` notifies you of any EKS objects that AWS Backup skipped during a restore job.

### Examples of events
<a name="sns-completed-backup-events"></a>



**Example: Backup job completed**  

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

**Example: Backup job failed**  

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

**Example: Backup job could not complete during the backup window**  

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

**Example: Recovery point indexing completed**  

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

**Example: EKS backup object failed**  

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
            "Message": "A Kubernetes resource failed to backup from your Amazon EKS Backup. Resource: example.resource.io/v1. EKS Cluster Name: eks-cluster-name. BackupJob ID: 1b2345b2-f22c-4dab-5eb6-bbc7890ed123",
            "Timestamp": "2025-05-25T18:46:02.788Z",
            ...
            "MessageAttributes" : {
              "eventType" : {"Type":"String","Value":"EKS_BACKUP_OBJECT_FAILED"},
              "backupJobId" : {"Type":"String","Value":"1b2345b2-f22c-4dab-5eb6-bbc7890ed123"},
              "clusterName" : {"Type":"String","Value":"eks-cluster-name"},
              "reason" : {"Type":"String","Value":"Example failure reason."},
              "resourceName" : {"Type":"String","Value":"example.resource.io/v1"}
            }
        }
    }]
}
```

**Example: EKS restore object failed**  

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
            "Message": "A Kubernetes resource failed to restore from your Amazon EKS Backup. Resource: apiextensions.k8s.io/v1/customresourcedefinitions. Resource Name: exampleresource. Destination EKS Cluster Name: eks-restore-target-cluster-name. RestoreJob ID: 1b2345b2-f22c-4dab-5eb6-bbc7890ed123",
            "Timestamp": "2025-05-25T18:46:02.788Z",
            ...
            "MessageAttributes" : {
              "eventType" : {"Type":"String","Value":"EKS_RESTORE_OBJECT_FAILED"},
              "clusterName" : {"Type":"String","Value":"eks-restore-target-cluster-name"},
              "parentRestoreJobId" : {"Type":"String","Value":"12345678-abcd-123a-def0-abcd1a234567"},
              "reason" : {"Type":"String","Value":"Example failure reason."},
              "resourceName" : {"Type":"String","Value":"exampleresourceio"},
              "resourceType" : {"Type":"String","Value":"apiextensions.k8s.io/v1/customresourcedefinitions"},
              "restoreJobId" : {"Type":"String","Value":"1b2345b2-f22c-4dab-5eb6-bbc7890ed123"}
            }
        }
    }]
}
```

**Example: EKS restore object skipped**  

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
            "Message": "A Kubernetes resource was skipped from restore from your Amazon EKS Backup. This Kubernetes resource already exists in your target EKS cluster. Resource: apiextensions.k8s.io/v1/customresourcedefinitions. Resource Name: exampleresource. Destination EKS Cluster Name: eks-restore-target-cluster-name. RestoreJob ID: 1b2345b2-f22c-4dab-5eb6-bbc7890ed123",
            "Timestamp": "2025-05-25T18:46:02.788Z",
            ...
            "MessageAttributes" : {
              "eventType" : {"Type":"String","Value":"EKS_RESTORE_OBJECT_SKIPPED"},
              "clusterName" : {"Type":"String","Value":"eks-restore-target-cluster-name"},
              "parentRestoreJobId" : {"Type":"String","Value":"12345678-abcd-123a-def0-abcd1a234567"},
              "reason" : {"Type":"String","Value":"Already exists."},
              "resourceName" : {"Type":"String","Value":"exampleresource"},
              "resourceType" : {"Type":"String","Value":"apiextensions.k8s.io/v1/customresourcedefinitions"},
              "restoreJobId" : {"Type":"String","Value":"1b2345b2-f22c-4dab-5eb6-bbc7890ed123"}
            }
        }
    }]
}
```

**Example: Access point available**  

```
{
    "Type": "Notification",
    "MessageId": "dd7579e6-47bb-51af-866c-1b36e07d9aaa",
    "TopicArn": "arn:aws:sns:us-east-1:123456789012:my-backup-topic",
    "Subject": "Notification from AWS Backup",
    "Message": "An AWS Backup access point was created successfully. Access point ARN: arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point. S3 access point ARN: arn:aws:s3:us-east-1:123456789012:accesspoint/my-access-point. Recovery point ARN: arn:aws:backup:us-east-1:123456789012:recovery-point:rp-1234567890abcdef0.",
    "Timestamp": "2026-07-28T12:00:26.426Z",
    "MessageAttributes": {
        "EventType": {"Type":"String","Value":"ACCESS_POINT_AVAILABLE"},
        "Status": {"Type":"String","Value":"AVAILABLE"},
        "AccountId": {"Type":"String","Value":"123456789012"},
        "AccessPointArn": {"Type":"String","Value":"arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point"},
        "CreationTime": {"Type":"String","Value":"2026-07-28T12:00:25.938846787Z"}
    }
}
```

**Example: Access point creation failed**  

```
{
    "Type": "Notification",
    "MessageId": "abcdef01-2345-6789-abcd-ef0123456789",
    "TopicArn": "arn:aws:sns:us-east-1:123456789012:my-backup-topic",
    "Subject": "Notification from AWS Backup",
    "Message": "An AWS Backup access point failed to create. Access point ARN: arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point. Recovery point ARN: arn:aws:backup:us-east-1:123456789012:recovery-point:rp-1234567890abcdef0.",
    "Timestamp": "2026-07-28T12:05:10.123Z",
    "MessageAttributes": {
        "EventType": {"Type":"String","Value":"ACCESS_POINT_CREATION_FAILED"},
        "Status": {"Type":"String","Value":"FAILED"},
        "AccountId": {"Type":"String","Value":"123456789012"},
        "AccessPointArn": {"Type":"String","Value":"arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point"},
        "CreationTime": {"Type":"String","Value":"2026-07-28T12:04:55.123456789Z"}
    }
}
```

**Example: Access point expired**  

```
{
    "Type": "Notification",
    "MessageId": "fedcba98-7654-3210-fedc-ba9876543210",
    "TopicArn": "arn:aws:sns:us-east-1:123456789012:my-backup-topic",
    "Subject": "Notification from AWS Backup",
    "Message": "An AWS Backup access point expired. Access point ARN: arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point. Recovery point ARN: arn:aws:backup:us-east-1:123456789012:recovery-point:rp-1234567890abcdef0.",
    "Timestamp": "2026-07-28T18:30:05.789Z",
    "MessageAttributes": {
        "EventType": {"Type":"String","Value":"ACCESS_POINT_EXPIRED"},
        "Status": {"Type":"String","Value":"EXPIRED"},
        "AccountId": {"Type":"String","Value":"123456789012"},
        "AccessPointArn": {"Type":"String","Value":"arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point"},
        "CreationTime": {"Type":"String","Value":"2026-07-28T12:00:25.938846787Z"}
    }
}
```

### AWS Backup notification command examples
<a name="sns-cli-commands"></a>

You can use AWS CLI commands to subscribe to, list, and delete Amazon SNS notifications for your AWS Backup events.

#### Example put backup vault notification
<a name="cli-put-vault-notification"></a>

The following command subscribes to an Amazon SNS topic for the specified backup vault that notifies you when a restore job is started or completed, or when a recovery point is modified.

```
aws backup put-backup-vault-notifications 
    --backup-vault-name {{myBackupVault}} 
    --sns-topic-arn arn:aws:sns:{{region}}:{{account-id}}:{{myBackupTopic}}
    --backup-vault-events RESTORE_JOB_STARTED RESTORE_JOB_COMPLETED RECOVERY_POINT_MODIFIED
```

#### Example get backup vault notification
<a name="w2aac32c15b9c13b7"></a>

The following command lists all events currently subscribed to an Amazon SNS topic for the specified backup vault.

```
aws backup get-backup-vault-notifications 
    --backup-vault-name {{myVault}}
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

#### Example delete backup vault notification
<a name="w2aac32c15b9c13b9"></a>

The following command unsubscribes from an Amazon SNS topic for the specified backup vault.

```
aws backup delete-backup-vault-notifications 
    --backup-vault-name {{myVault}}
```

### Specifying AWS Backup as a service principal
<a name="specifying-aws-backup-as-a-service-principal"></a>

**Note**  
To allow AWS Backup to publish SNS topics on your behalf, you must specify AWS Backup as a service principal.

Include the following JSON in the access policy of the Amazon SNS topic that you use to track AWS Backup events. You must specify the resource Amazon Resource Name (ARN) of your topic.

```
{
      "Sid": "My-statement-id",
      "Effect": "Allow",
      "Principal": {
        "Service": "backup.amazonaws.com"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:{{region}}:{{account-id}}:{{myTopic}}"
}
```

For more information about specifying a service principal in an Amazon SNS access policy, see [Allowing Any AWS Resource to Publish to a Topic](https://docs.aws.amazon.com/sns/latest/dg/AccessPolicyLanguage_UseCases_Sns.html#AccessPolicyLanguage_UseCase4_Sns) in the *Amazon Simple Notification Service Developer Guide*.

**Note**  
If your topic is encrypted, you must include additional permissions in your policy to allow AWS Backup to publish to it. For more information about enabling services to publish to encrypted topics, see [Enable Compatibility between Event Sources from AWS Services and Encrypted Topics](https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html#sns-what-permissions-for-sse) in the *Amazon Simple Notification Service Developer Guide*.