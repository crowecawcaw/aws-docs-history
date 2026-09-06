

# Protecting your data with on-demand replication
<a name="on-demand-replication"></a>

Amazon FSx for OpenZFS supports on-demand data replication, enabling you to transfer snapshots of data between file systems within and across AWS Regions and accounts. You can use on-demand data replication for a variety of tasks such as:
+ Synchronizing or distributing data to your development or test environments.
+ Establishing and maintaining read replicas to provide scale-out read performance.
+ Maintaining a passive standby file system for use in disaster recovery cases.

With on-demand data replication, Amazon FSx automatically establishes and maintains network connectivity between file systems to handle interruptions and resume data transfer as needed. Amazon FSx also encrypts data in transit and at rest and integrates with AWS RAM to authorize accesss to volumes for data replication across AWS accounts. For more information, see [Shareable AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-fsx) in the *AWS RAM User Guide*. 

On-demand data replication is available for all deployment types in AWS Regions where Amazon FSx for OpenZFS is available. For more information, see [Availability by AWS Region](available-aws-regions.md).

**Topics**
+ [Prerequisites for using on-demand data replication](#access-data-replication)
+ [Performance considerations for on-demand data replication](#on-demand-replication-performance)
+ [Using on-demand data replication](#how-to-use-data-replication)
+ [Monitoring progress of on-demand data replication](#how-to-monitor-data-replication)
+ [Setting up ongoing periodic data replication](ongoing-periodic-data-replication.md)

## Prerequisites for using on-demand data replication
<a name="access-data-replication"></a>

Before using on-demand data replication, make sure that you have met the following prerequisites.
+ Single-AZ 1 (non-HA and HA) file systems must have a provisioned throughput capacity of 256 MBps or above. It is also recommended that Single-AZ 1 (non-HA and HA) file systems have a provisioned SSD IOPS level of 6,000 or above.
+ Single-AZ 2 (non-HA and HA) and Multi-AZ (HA) file systems must have a provisioned throughput capacity of 160 MBps or above. It is also recommended that Single-AZ 2 (non-HA) and Multi-AZ (HA) file systems have a provisioned SSD IOPS level of 6,000 or above.
+ Users or roles must have permission to take the [CreateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateVolume.html) and [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) actions in an AWS account. You can control these permissions by using AWS Identity and Access Management (IAM) policies. For more information, see [Actions, resources, and condition keys for Amazon FSx](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfsx.html#amazonfsx-actions-as-permissions.html) in the *Service Authorization Reference*.
+ To replicate data across file systems in different AWS accounts, the source account must have, at minimum, permission to take the **fsx:PutResourcePolicy**, **fsx:GetResourcePolicy**, and **fsx:DeleteResourcePolicy** actions. The source account must also have permissions to share resources on AWS RAM. To grant these permissions, you can directly attach the [AmazonFSxFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonFSxFullAccess), [AmazonFSxConsoleFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonFSxConsoleFullAccess), and [AWSResourceAccessManagerFullAccess](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-managed-policies.html#security-iam-managed-policies-AWSResourceAccessManagerFullAccess) AWS managed policies to your IAM roles, groups, and users. The destination account must have the [AWSResourceAccessManagerResourceShareParticipantAccess](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-managed-policies.html#security-iam-managed-policies-AWSResourceAccessManagerResourceShareParticipantAccess) AWS managed policy attached to its IAM roles, groups, and users. 

## Performance considerations for on-demand data replication
<a name="on-demand-replication-performance"></a>

On-demand data replication shares provisioned throughput with other file system clients. To accommodate data replication activity without impacting other workloads, we recommend provisioning twice the level of throughput capacity that your workload normally needs. You can use Amazon CloudWatch metrics with FSx for OpenZFS to monitor your file system’s performance utilization and scale up your file system’s performance as needed to avoid slowing down your ongoing workloads. For more information, see [Using Amazon FSx for OpenZFS CloudWatch metrics](how_to_use_metrics.md).

## Using on-demand data replication
<a name="how-to-use-data-replication"></a>

On-demand data replication only transfers data from the indicated source snapshot, which does not include data from child volumes. To transfer data from child volumes, you must initiate additional data replication jobs using source snapshots from the child volumes.

Each file system can only be used as the source file system or the destination file system for one on-demand data replication task at a time. You must wait until the first on-demand replication task is completed or cancelled before initating another request. You can only have a maximum of twenty concurrent cross-file system replication jobs per account, per AWS Region.

### Replicating data across file systems on the same account
<a name="same-account-data-replication"></a>

You can create or update a replica volume across file systems that are on the same AWS account by using the Amazon FSx Console, API, or CLI.

#### To update a volume from a snapshot (Console)
<a name="update-volume-from-snapshot-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, choose **Volumes**, and then choose the volume that you would like to use as your destination volume.

1. For **Actions**, choose **Update volume with snapshot**. The **Copy snapshot and update volume** panel displays.

1. Choose the source region of the snapshot

1. Choose the snapshot that you would like to update the volume from.

1. For **Source snapshot copy strategy**, choose **Incremental copy** or **Full copy**. An incremental copy returns the destination volume to the most recent common ancestor that it shares with the source volume and then updates the destination volume, transferring only the data that is not already included in the most recent common ancestor. A full copy will remove any clones, snapshots, and intermediate data on the destination volume and transfer all of the data from the source volume. During incremental copy, your destination volume will be read-only. During full copy, your destination volume will be unmounted and automatically remounted after the transfer is completed.

1. If the destination volume has any **intermediate clones**, **dependent snapshots**, or **intermediate data**, select the checkboxes to delete them. If you are using incremental copy, you must delete all descendent data for the update to succeed.

1. Choose **Update** to update the volume.

#### To update a volume from a snapshot (CLI)
<a name="w2aac29c14c21b7b7b1"></a>
+ To update an FSx for OpenZFS volume with a snapshot, use the [copy-snapshot-and-update-volume](https://docs.aws.amazon.com/cli/latest/reference/fsx/copy-snapshot-and-update-volume.html) CLI command, or the equivalent [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) API command, and specify the following properties:
  + `--volume-id` – The ID of the volume that you would like to update.
  + `--source-snapshot-arn` – The ARN of the source snapshot.
  + `--options` – Any intermediate clones, dependent snapshots, or intermediate data that need to be deleted. Valid values are `DELETE_INTERMEDIATE_SNAPSHOTS`, `DELETE_CLONED_VOLUMES`, and `DELETE_INTERMEDIATE_DATA`.
  + `--copy-strategy` – Strategy used to copy data from the source volume. Value values are `FULL_COPY` and `INCREMENTAL_COPY`.

The following example shows how to update a volume with a snapshot using incremental copy and deleting all intermediate clones, dependent snapshots, and intermediate data.

```
aws fsx copy-snapshot-and-update-volume \
     --volume-id {{fsvol-1234567890abcdef0}} \
     --source-snapshot-arn {{arn:aws:fsx:555555555555:snapshot/fsvol-1234567890abcdef0/fsvolsnap-021345abcdef6789}}\
     --options {{DELETE_INTERMEDIATE_SNAPSHOTS DELETE_CLONED_VOLUMES DELETE_INTERMEDIATE_DATA}}\
     --copy-strategy {{INCREMENTAL_COPY}}
```

The example above returns the following response.

```
{
    "VolumeId": "fsvol-1234567890abcdef0",
    "Lifecycle": "AVAILABLE",
    "AdministrativeActions": [ 
    {
        "AdministrativeActionType": "VOLUME_UPDATE_WITH_SNAPSHOT",
        "FailureDetails": { 
            "Message": "string"
        },
        "ProgressPercent": 80,
        "RequestTime": 2023-11-03T09:26:55-07:00,
        "Status": "IN_PROGRESS",
        "TargetVolumeValues": { 
            "OpenZFSConfiguration": { 
            "RecordSizeKiB": 128, 
            "DataCompressionType": "ZSTD", 
            "DeleteIntermediateSnaphots": false, 
            "DeleteClonedVolumes": false, 
            "DeleteIntermediateData": true, 
            "SourceSnapshotARN": "arn:aws:fsx:us-east-1:854733241892:snapshot/fsvol-018a3d05b4d9fc768/fsvolsnap-03b43bd1942a51637", 
            "DestinationSnapshot": "fsvolsnap-0f753e290e20cc974" }"
        }
    }]    
}
```

### Replicating data across file systems on different AWS accounts using AWS RAM
<a name="cross-account-replication"></a>

FSx for OpenZFS integrates with AWS Resource Access Manager (RAM) to allow you to replicate data across file systems that are on different AWS accounts. In the AWS Resource Access Manager (RAM) console, the owner of the source account must first enable resource sharing, and then share the source FSx for OpenZFS volume with the destination account. For more information on enabling and creating a resource share, see [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) and [Creating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html) in the *AWS RAM User Guide*.

You will receive a shared resource invitation when the source volume has been shared with your account. Once you accept the invitation, all snapshots associated with the source volume will appear in the list of snapshots that you can replicate to a volume in the FSx for OpenZFS console. For more information, see [To update a volume from a snapshot (Console)](#update-volume-from-snapshot-console). After you’ve created a replica volume, you can continue to update it with any of the subsequent snapshots in the source volume, as long as the source volume continues to be shared.

## Monitoring progress of on-demand data replication
<a name="how-to-monitor-data-replication"></a>

You can monitor the progress of your data replication using the AWS Management Console on the **Volume details** page. When you initiate a replication task, the destination snapshot will enter the **CREATING** state. Once the data transfer is complete, the destination snapshot will become **AVAILABLE**.

You can also use the AWS CLI or Amazon FSx API to track more detailed progress of your replication by using the [describe-volumes](https://docs.aws.amazon.com/cli/latest/reference/fsx/describe-volumes.html) AWS CLI command or the [DescribeVolumes](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeVolumes.html) API operation. to display the `AdministrativeActions` for the destination volume. The `AdministrativeActions` array lists the 10 most recent update actions for each administrative action type. When you initiate an on-demand data replication, a `VOLUME_UPDATE_WITH_SNAPSHOT` action is generated. Progress will be reported using the `ProgressPercent` property.

The following example shows the response for an incremental copy on-demand data replication task.

```
{
    "VolumeId": "fsvol-1234567890abcdef0",
    "Lifecycle": "AVAILABLE",
    "AdministrativeActions": [ 
    {
        "AdministrativeActionType": "VOLUME_UPDATE_WITH_SNAPSHOT",
        "FailureDetails": { 
            "Message": "string"
        },
        "ProgressPercent": 80,
        "RequestTime": 2023-11-03T09:26:55-07:00,
        "Status": "IN_PROGRESS",
        "TotalTransferBytes": 107483152368,
        "RemainingTransferBytes": 0
        "TargetVolumeValues": {
            "OpenZFSConfiguration": {
                "SourceSnapshotARN": "stringarn:aws:fsx:555555555555:snapshot/fsvol-1234567890abcdef0/fsvolsnap-021345abcdef6789",
                "DestinationSnapshot": "fsvolsnap-021345abcdef6789"
            }
        }
    }]    
}
```

When Amazon FSx processes the request successfully, the status changes to `COMPLETED`. If the on-demand data replication task fails, the status changes to `FAILED`, and the `FailureDetails` property provides information about the failure.