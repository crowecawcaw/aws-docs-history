

# `AWSSupportRemediator-DisablePublicAccessOnRedshiftCluster`

**Description**

Disables public accessibility on an Amazon Redshift cluster by setting the `PubliclyAccessible` attribute to `false`.

The runbook calls the Amazon Redshift `ModifyCluster` API, waits for the cluster to return to the `available` state, and asserts that `PubliclyAccessible` is `false` on completion.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon Redshift clusters should prohibit public access](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-1).

If the Amazon Redshift cluster does not exist or public access is already disabled, the automation completes successfully without making changes.

Disabling public access removes the cluster's public endpoint. Clients that connect over the internet lose connectivity. After the change, only clients reachable through the cluster's Amazon Virtual Private Cloud (Amazon VPC) can connect. The cluster briefly transitions out of the `available` state during the modification.

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

  Description: (Required) The unique identifier of the Amazon Redshift cluster.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `redshift:DescribeClusters`
+ `redshift:ModifyCluster`

**Document Steps**

1. **validateCluster** - Checks whether the specified Amazon Redshift cluster exists and whether its `PubliclyAccessible` attribute is already `false`. Returns no change required when the cluster does not exist or already has public access disabled.

1. **branchOnChangeRequired** - Branches on whether a change is required. Continues to `disableClusterPublicAccess` when `validateCluster.ChangeRequired` is `true`. Otherwise, ends the runbook successfully.

1. **disableClusterPublicAccess** - Calls the Amazon Redshift `ModifyCluster` API on the specified cluster with `PubliclyAccessible` set to `false`. The cluster transitions out of the `available` state during the modification.

1. **waitForClusterAvailability** - Waits until the Amazon Redshift cluster returns to the `available` state after the `ModifyCluster` call. This confirms that the cluster has applied the change before the runbook verifies the final state.

1. **assertFinalPublicAccessIsDisabled** - Asserts that the Amazon Redshift cluster's `PubliclyAccessible` attribute is `false` after the modification completes. The step fails if the cluster is still publicly accessible.

**Outputs**
+ validateCluster.ChangeRequired: Whether a change is required. `false` when the cluster does not exist or already has public access disabled.
+ validateCluster.ValidationMessage: A message describing why no change is required, or `N/A` when a change is required.