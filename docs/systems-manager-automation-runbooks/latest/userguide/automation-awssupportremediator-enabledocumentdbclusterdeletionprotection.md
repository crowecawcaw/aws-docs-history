

# `AWSSupportRemediator-EnableDocumentDbClusterDeletionProtection`

**Description**

Enables deletion protection for an Amazon DocumentDB cluster.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon DocumentDB clusters should have deletion protection enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-5).

If the Amazon DocumentDB cluster does not exist or deletion protection is already enabled, the automation completes successfully without making changes.

Amazon DocumentDB uses the Amazon Relational Database Service (Amazon RDS) API to modify cluster configuration. Enabling deletion protection does not interrupt cluster availability and takes effect immediately.

To disable deletion protection after enabling, modify the cluster configuration and set `DeletionProtection` to `false`.

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
+ DocDBClusterIdentifierArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon DocumentDB cluster for which to enable deletion protection.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBClusters`
+ `rds:ModifyDBCluster`

**Document Steps**

1. **validateDocDB** - Validates that the Amazon DocumentDB cluster exists and checks its current deletion protection setting.

1. **branchOnChangeRequired** - Branches on whether deletion protection needs to be enabled.

1. **enableDeletionProtection** - Enables deletion protection on the Amazon DocumentDB cluster.

**Outputs**
+ validateDocDB.ChangeRequired: Whether deletion protection needs to be enabled on the Amazon DocumentDB cluster.
+ validateDocDB.ValidationMessage: Information about the validation result.
+ validateDocDB.DBClusterIdentifier: The identifier of the Amazon DocumentDB cluster.
+ validateDocDB.InitialDeletionProtection: The initial deletion protection setting on the Amazon DocumentDB cluster.