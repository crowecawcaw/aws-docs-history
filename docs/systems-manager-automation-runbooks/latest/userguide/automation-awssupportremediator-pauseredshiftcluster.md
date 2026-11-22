

# `AWSSupportRemediator-PauseRedshiftCluster`

**Description**

Pauses an Amazon Redshift cluster after validating that it meets AWS Trusted Advisor idle criteria (no connections in the last 7 days and less than 5% CPU utilization for 99% of the last 7 days).

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Underutilized Amazon Redshift Clusters](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#underutilized-amazon-redshift-clusters).

If the cluster does not exist, is already paused, is pausing, is being deleted, or is creating a final snapshot, the automation completes successfully without making changes.

If `CreateSnapshot` is set to true, the automation creates a manual snapshot tagged with `CreatedBy: AWSRemediator` before pausing the cluster. The snapshot remains in the account after the automation completes. Manual snapshots incur Amazon Redshift storage charges until they are deleted. For more information about pricing, see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/).

To resume the cluster after pausing, use the Amazon Redshift console or the `ResumeCluster` API action.

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
+ ClusterIdentifier

  Type: String

  Description: (Required) The identifier of the Amazon Redshift cluster.
+ CreateSnapshot

  Type: Boolean

  Description: (Optional) Whether to create a snapshot before pausing the cluster. If set to false, a recent backup must already exist or the pause operation fails.

  Default: True

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudwatch:GetMetricStatistics`
+ `redshift:CreateClusterSnapshot`
+ `redshift:DescribeClusterSnapshots`
+ `redshift:DescribeClusters`
+ `redshift:PauseCluster`

**Document Steps**

1. **validateInput** - Validates that the Amazon Redshift cluster exists, checks its current status, and verifies idle criteria for available clusters.

1. **branchOnValidation** - Branches on whether the cluster needs to be paused and whether a snapshot should be created first.

1. **createClusterSnapshot** - Creates a manual snapshot of the Amazon Redshift cluster tagged with `CreatedBy: AWSRemediator`.

1. **waitForSnapshotCreation** - Waits for the snapshot to become available.

1. **pauseCluster** - Pauses the Amazon Redshift cluster.

1. **waitForPauseCompletion** - Waits for the cluster to reach the paused state.

**Outputs**
+ validateInput.InitialResourceState: The initial status of the Amazon Redshift cluster.
+ validateInput.FinalResourceState: The expected final status of the Amazon Redshift cluster.
+ validateInput.ValidationMessage: A message describing the validation result.
+ createClusterSnapshot.SnapshotIdentifier: The identifier of the snapshot created before pausing.