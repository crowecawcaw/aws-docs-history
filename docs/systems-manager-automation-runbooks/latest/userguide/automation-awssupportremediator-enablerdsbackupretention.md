

# `AWSSupportRemediator-EnableRdsBackupRetention`

**Description**

Enables automated backups for an Amazon Relational Database Service (Amazon RDS) DB instance by setting the backup retention period to a non-zero value (1-35 days).

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon RDS Backups](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-rds-backups).

If the DB instance does not exist, the backup retention period is already set to a non-zero value, or a pending change exists to enable backup retention, the automation completes successfully without making changes.

If `ApplyImmediately` is set to `true` and the DB instance has pending changes other than backup retention, the automation fails to prevent unintended application of those changes.

Enabling automated backups might increase storage costs. For more information about pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/).

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
+ DBInstanceIdentifier

  Type: String

  Description: (Required) The Amazon RDS DB instance identifier, not the Amazon Resource Name (ARN).
+ ApplyImmediately

  Type: Boolean

  Description: (Optional) Whether to apply the modifications in this request and any pending modifications as soon as possible. Choose `true` to apply the change immediately, or `false` to schedule the change on the next maintenance window. If set to `true` and the DB instance has pending changes other than backup retention, the automation fails.

  Default: False
+ BackupRetentionPeriod

  Type: Integer

  Description: (Optional) The number of days (1-35) to retain automated backups. Setting a non-zero value enables automated backups.

  Default: 7

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBInstances`
+ `rds:ModifyDBInstance`

**Document Steps**

1. **validateDB** - Validates whether the Amazon RDS DB instance exists, is in `available` status, and requires a backup retention period change.

1. **branchOnChangeRequired** - Branches on whether modification is needed.

1. **updateDBInstance** - Modifies the Amazon RDS DB instance to set the backup retention period to the specified value.

**Outputs**
+ validateDB.ChangeRequired: Whether the backup retention period needs to be changed.
+ validateDB.ValidationMessage: The reason when no change is required.
+ validateDB.InitialBackupRetentionPeriod: The backup retention period value before the automation runs.