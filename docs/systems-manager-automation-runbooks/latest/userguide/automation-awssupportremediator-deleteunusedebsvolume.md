

# `AWSSupportRemediator-DeleteUnusedEbsVolume`

**Description**

Deletes an Amazon Elastic Block Store (Amazon EBS) volume that is in an available (unattached) state and has been idle for a specified period.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Underutilized Amazon EBS Volumes](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#underutilized-amazon-ebs-volumes) and AWS Compute Optimizer [Idle Amazon EBS volume](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).

If the volume does not exist or is already being deleted, the automation completes successfully without making changes. If the volume is attached or in an error state, the automation fails. If the volume has any read or write activity during the specified idle period, the automation fails, because it deletes only unused volumes.

When `CreateSnapshot` is set to `true`, the automation creates a backup snapshot before deleting the volume. If snapshot creation fails, the automation stops to prevent data loss. If the snapshot fails to complete, the automation deletes the snapshot and stops. If snapshot cleanup fails, the orphaned snapshot ID is available in the automation output for manual cleanup.

**Data loss risk**  
Deleting an Amazon EBS volume is irreversible. To recover the data, restore from the backup snapshot created by this automation.

Deleting the volume stops any associated Amazon EBS volume charges. If a backup snapshot is created, standard Amazon EBS snapshot charges apply. For more information about pricing, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/).

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ VolumeId

  Type: String

  Description: (Required) The ID of the Amazon EBS volume.
+ CreateSnapshot

  Type: Boolean

  Description: (Optional) Whether to create a backup snapshot before deletion.

  Default: True
+ MinimumUnattachedDays

  Type: Integer

  Description: (Optional) The minimum number of days the Amazon EBS volume must be unattached before deletion, up to 62 days. If set to 0, the volume is deleted without checking idle status.

  Default: 7

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudwatch:GetMetricData`
+ `ec2:CreateSnapshot`
+ `ec2:CreateTags`
+ `ec2:DeleteSnapshot`
+ `ec2:DeleteVolume`
+ `ec2:DescribeSnapshots`
+ `ec2:DescribeVolumeStatus`
+ `ec2:DescribeVolumes`

**Document Steps**

1. **validateAndCreateEbsSnapshot** - Validates that the Amazon EBS volume exists, is in an available state, and has been idle for the specified period. Creates a backup snapshot if `CreateSnapshot` is set to `true`.

1. **branchOnChangeRequired** - Branches on whether the volume meets deletion criteria.

1. **branchOnCreateSnapshot** - Branches on whether a snapshot needs to be created before deletion.

1. **waitForSnapshotCompleted** - Waits for the backup snapshot to reach the completed state.

1. **cleanBackupSnapshotsOnFailure** - Deletes the backup snapshot if the snapshot fails to complete.

1. **deleteEBSVolume** - Deletes the Amazon EBS volume.

1. **verifyEbsVolumeDeletion** - Verifies that the Amazon EBS volume is deleted.

**Outputs**
+ validateAndCreateEbsSnapshot.ChangeRequired: Whether the volume meets deletion criteria.
+ validateAndCreateEbsSnapshot.ValidationMessage: A message describing the validation result.
+ validateAndCreateEbsSnapshot.SnapshotId: The ID of the backup snapshot, if created.