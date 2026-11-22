

# `AWSSupportRemediator-EnableRdsCopyTagsToSnapshot`

**Description**

Enables the `CopyTagsToSnapshot` setting on an Amazon Relational Database Service (Amazon RDS) DB instance or DB cluster.

When enabled, Amazon RDS copies tags from the source resource to any snapshots created from it.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM controls [Aurora DB clusters should be configured to copy tags to DB snapshots](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-16) and [RDS DB instances should be configured to copy tags to snapshots](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-17).

If the Amazon RDS DB instance or DB cluster does not exist or `CopyTagsToSnapshot` is already enabled, the automation completes successfully without making changes.

To disable `CopyTagsToSnapshot` after enabling, modify the Amazon RDS DB instance or DB cluster with `CopyTagsToSnapshot` set to `false`.

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

1. **validateDB** - Validates that the Amazon RDS DB instance or DB cluster exists and determines whether `CopyTagsToSnapshot` is already enabled.

1. **branchOnChangeRequired** - Branches on whether a change is required and routes to `updateDBInstance` or `updateDBCluster` based on the Amazon RDS resource type.

1. **updateDBInstance** - Enables `CopyTagsToSnapshot` on the Amazon RDS DB instance.

1. **updateDBCluster** - Enables `CopyTagsToSnapshot` on the Amazon RDS DB cluster.

**Outputs**
+ validateDB.ChangeRequired: Indicates whether the automation must enable `CopyTagsToSnapshot` on the Amazon RDS DB instance or DB cluster.
+ validateDB.DBIdentifier: The identifier of the Amazon RDS DB instance or DB cluster.
+ validateDB.DBType: The type of the Amazon RDS resource (`db` or `cluster`).
+ validateDB.ValidationMessage: A message describing the validation result.