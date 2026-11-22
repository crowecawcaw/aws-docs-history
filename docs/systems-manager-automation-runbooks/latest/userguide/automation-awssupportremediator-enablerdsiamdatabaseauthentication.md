

# `AWSSupportRemediator-EnableRdsIamDatabaseAuthentication`

**Description**

Enables AWS Identity and Access Management (IAM) database authentication for an Amazon Relational Database Service (Amazon RDS) DB instance or cluster.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM controls [IAM authentication should be configured for RDS instances](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-10) and [IAM authentication should be configured for RDS clusters](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-12).

If the Amazon RDS DB instance or cluster does not exist or IAM database authentication is already enabled, the automation completes successfully without making changes.

If the Amazon RDS resource has other pending modifications and `ApplyImmediately` is set to true, the automation fails to avoid applying unrelated changes during a maintenance-sensitive window.

Enabling IAM database authentication does not replace or disable existing password-based authentication. Existing database users continue to authenticate using their current credentials.

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
+ ApplyImmediately

  Type: Boolean

  Description: (Required) Whether to apply the modification immediately or during the next maintenance window. Set to true to apply the change immediately, or false to schedule the change for the next maintenance window.
+ DBIdentifierArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon RDS DB instance or cluster.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBClusters`
+ `rds:DescribeDBInstances`
+ `rds:ModifyDBCluster`
+ `rds:ModifyDBInstance`

**Document Steps**

1. **validateDB** - Validates that the Amazon RDS DB instance or cluster exists and checks whether IAM database authentication is already enabled.

1. **branchOnChangeRequired** - Branches on whether IAM database authentication needs to be enabled and on whether the Amazon RDS resource is a DB instance or cluster.

1. **updateDBInstance** - Enables IAM database authentication on the Amazon RDS DB instance.

1. **updateDBCluster** - Enables IAM database authentication on the Amazon RDS cluster.

**Outputs**
+ validateDB.ChangeRequired: Whether IAM database authentication needs to be enabled.
+ validateDB.DBType: The type of Amazon RDS resource (`db` or `cluster`).
+ validateDB.ValidationMessage: Additional information about the validation result.
+ validateDB.DBIdentifier: The identifier of the Amazon RDS DB instance or cluster.