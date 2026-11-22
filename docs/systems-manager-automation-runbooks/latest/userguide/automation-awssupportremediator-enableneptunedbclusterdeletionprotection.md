

# `AWSSupportRemediator-EnableNeptuneDbClusterDeletionProtection`

**Description**

Enables deletion protection for an Amazon Neptune DB cluster.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Neptune DB clusters should have deletion protection enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-4).

If the Neptune DB cluster does not exist or deletion protection is already enabled, the automation completes successfully without making changes.

If the supplied cluster ARN does not belong to a Neptune DB cluster (for example, an Amazon Relational Database Service (Amazon RDS) DB cluster), the automation fails.

This automation modifies the Neptune DB cluster configuration through the Amazon Neptune API.

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
+ NeptuneClusterIdentifierArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Neptune DB cluster.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBClusters`
+ `rds:ModifyDBCluster`

**Document Steps**

1. **validateNeptuneCluster** - Verifies that the Amazon Neptune DB cluster exists, confirms its engine is Neptune, and reads the current deletion-protection state. If the cluster does not exist or deletion protection is already enabled, this step reports that no change is required. If the cluster engine is not Neptune, this step fails with an error.

1. **branchOnChangeRequired** - Branches on whether deletion protection requires an update.

1. **updateNeptuneCluster** - Enables deletion protection on the Neptune DB cluster.

**Outputs**
+ validateNeptuneCluster.DBClusterIdentifier: The identifier of the Neptune DB cluster.
+ validateNeptuneCluster.ChangeRequired: Whether deletion protection requires an update.
+ validateNeptuneCluster.InitialDeletionProtection: The initial deletion protection setting of the Neptune DB cluster.
+ validateNeptuneCluster.ValidationMessage: A message describing the validation result.