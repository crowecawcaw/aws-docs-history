

# `AWSSupportRemediator-CreateEbsSnapshot`

**Description**

Creates a snapshot for a specified Amazon Elastic Block Store (Amazon EBS) volume.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon EBS Snapshots](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-ebs-snapshots).

If the Amazon EBS volume does not exist or a recent snapshot was created within the specified time range, the automation completes successfully without making changes.

If the snapshot fails to complete and the automation cannot clean it up, it might remain in your account. Use the automation output `createSnapshot.SnapshotId` to find the snapshot ID.

Creating a snapshot incurs Amazon EBS snapshot storage costs. For more information about pricing, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/).

**Important considerations**  
You are responsible for reviewing automation actions before they run.
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

  Description: (Required) The ID of the Amazon EBS volume to create a snapshot for.
+ MaxSnapshotAge

  Type: String

  Description: (Optional) The time range in days to check if a recent snapshot was created. The automation does not create a new snapshot if a snapshot was created within this time range.

  Default: 7

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:CreateSnapshot`
+ `ec2:DeleteSnapshot`
+ `ec2:DescribeSnapshots`
+ `ec2:DescribeVolumes`

**Document Steps**

1. **validateVolume** - Validates whether the Amazon EBS volume exists and checks if a recent snapshot was created within the specified time range.

1. **branchOnChangeRequired** - Branches based on whether a new snapshot needs to be created.

1. **createSnapshot** - Creates a snapshot for the specified Amazon EBS volume.

1. **waitForSnapshotCompleted** - Waits for the snapshot to reach the completed state. If the snapshot fails, proceeds to clean up the failed snapshot.

1. **cleanupFailedSnapshot** - Deletes the snapshot if it fails to complete. If cleanup fails, the snapshot might remain in your account. Use the automation output `createSnapshot.SnapshotId` to find the snapshot ID.

**Outputs**
+ validateVolume.ChangeRequired: Whether a change is required.
+ validateVolume.ValidationMessage: The reason when no change is required.
+ createSnapshot.SnapshotId: The ID of the Amazon EBS snapshot created.