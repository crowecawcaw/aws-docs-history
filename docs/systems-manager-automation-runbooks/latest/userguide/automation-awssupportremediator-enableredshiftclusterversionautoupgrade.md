

# `AWSSupportRemediator-EnableRedshiftClusterVersionAutoUpgrade`

**Description**

Enables automatic major version upgrades on an Amazon Redshift cluster by calling the Amazon Redshift `ModifyCluster` API with `AllowVersionUpgrade` set to `true`.

After this runbook enables automatic major version upgrades, Amazon Redshift applies those upgrades to the cluster during the next maintenance window.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon Redshift should have automatic upgrades to major versions enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-6).

If the Amazon Redshift cluster does not exist or already has `AllowVersionUpgrade` enabled, the automation completes successfully without making changes.

Major version upgrades might introduce changes that affect compatibility with client applications. Test your applications with new Amazon Redshift major versions to understand the impact.

To disable automatic major version upgrades after enabling, call the Amazon Redshift `ModifyCluster` API on the cluster with `AllowVersionUpgrade` set to `false`. The `validateCluster.InitialAllowVersionUpgrade` output records the initial value before the automation runs, for rollback.

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

  Description: (Required) The unique identifier of the Amazon Redshift cluster on which to enable automatic major version upgrades.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `redshift:DescribeClusters`
+ `redshift:ModifyCluster`

**Document Steps**

1. **validateCluster** - Checks whether the specified Amazon Redshift cluster exists and already has `AllowVersionUpgrade` enabled. Returns no change required when the cluster does not exist or already has `AllowVersionUpgrade` enabled.

1. **branchOnChangeRequired** - Branches on whether a change is required. Continues to `setAllowVersionUpgradeToTrue` when `validateCluster.ChangeRequired` is `true`. Otherwise, ends the runbook successfully.

1. **setAllowVersionUpgradeToTrue** - Calls the Amazon Redshift `ModifyCluster` API on the specified cluster with `AllowVersionUpgrade` set to `true`.

**Outputs**
+ validateCluster.ChangeRequired: Whether a change is required. `false` when the cluster does not exist or already has `AllowVersionUpgrade` enabled.
+ validateCluster.InitialAllowVersionUpgrade: The initial `AllowVersionUpgrade` value for the Amazon Redshift cluster before the automation runs. `false` when the cluster does not exist.
+ validateCluster.ValidationMessage: A message describing why no change is required, or `N/A` when a change is required.