

# `AWSSupportRemediator-EnableRedshiftClusterEnhancedVpcRouting`

**Description**

Enables enhanced VPC routing on an Amazon Redshift cluster by calling the Amazon Redshift [ModifyCluster](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyCluster.html) API to set `EnhancedVpcRouting` to `true`.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Redshift clusters should use enhanced VPC routing](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-7).

If the Amazon Redshift cluster does not exist or already has enhanced VPC routing enabled, the automation completes successfully without making changes.

After the runbook enables enhanced VPC routing, Amazon Redshift routes all COPY and UNLOAD traffic through the cluster's Amazon Virtual Private Cloud (Amazon VPC). Your Amazon VPC must have network paths to Amazon Simple Storage Service (Amazon S3) and any other services that your COPY and UNLOAD statements use. Without these network paths, COPY and UNLOAD operations might fail after the runbook enables enhanced VPC routing. For more information, see [Enhanced VPC routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Management Guide.

To disable enhanced VPC routing after enabling it, call the Amazon Redshift `ModifyCluster` API to set `EnhancedVpcRouting` to `false`.

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

  Description: (Required) The unique identifier of the Amazon Redshift cluster on which to enable enhanced VPC routing.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `redshift:DescribeClusters`
+ `redshift:ModifyCluster`

**Document Steps**

1. **validateCluster** - Checks whether the specified Amazon Redshift cluster exists and whether it already has enhanced VPC routing enabled. Returns no change required when the cluster does not exist or already has enhanced VPC routing enabled.

1. **branchOnChangeRequired** - Branches on whether the runbook needs to enable enhanced VPC routing. Continues to `modifyCluster` when `validateCluster.ChangeRequired` is `true`. Otherwise, ends the automation successfully.

1. **modifyCluster** - Calls the Amazon Redshift `ModifyCluster` API to set `EnhancedVpcRouting` to `true` on the cluster.

1. **waitForEnhancedVpcRoutingEnabled** - Waits for the cluster's `EnhancedVpcRouting` property to become `true` after `modifyCluster` runs. On timeout, continues to `assertEnhancedVPCRouting`, which fails with a clear terminal error.

1. **assertEnhancedVPCRouting** - Asserts that the cluster's `EnhancedVpcRouting` property is `true`, ensuring the automation reports success only after observing the change.

**Outputs**
+ validateCluster.ChangeRequired: Indicates whether the runbook needs to enable enhanced VPC routing. `false` when the Amazon Redshift cluster does not exist or already has enhanced VPC routing enabled.
+ validateCluster.ValidationMessage: Explains why the runbook takes no action, or `N/A` when the runbook enables enhanced VPC routing.