

# `AWSSupportRemediator-EnableRdsDeletionProtection`

**Description**

Enables deletion protection for an Amazon Relational Database Service (Amazon RDS) DB instance or Amazon RDS DB cluster.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM controls [RDS DB instances should have deletion protection enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-8) and [RDS clusters should have deletion protection enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-7).

If the Amazon RDS DB instance or DB cluster does not exist or deletion protection is already enabled, the automation completes successfully without making changes.

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
+ DBIdentifierArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon RDS DB instance or DB cluster.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBClusters`
+ `rds:DescribeDBInstances`
+ `rds:ModifyDBCluster`
+ `rds:ModifyDBInstance`

**Document Steps**

1. **validateDb** - Validates whether the Amazon RDS DB instance or DB cluster exists and whether deletion protection is already enabled.

1. **branchOnChangeRequired** - Branches on whether deletion protection needs to be enabled.

1. **branchOnDbType** - Branches on whether the resource is a DB instance or DB cluster.

1. **enableInstanceDeletionProtection** - Enables deletion protection for the Amazon RDS DB instance.

1. **enableClusterDeletionProtection** - Enables deletion protection for the Amazon RDS DB cluster.

**Outputs**
+ validateDb.DBIdentifier: The identifier of the Amazon RDS DB instance or DB cluster.
+ validateDb.ChangeRequired: Whether deletion protection needs to be enabled.
+ validateDb.InitialDeletionProtection: The initial deletion protection setting.
+ validateDb.ValidationMessage: The reason for the result.