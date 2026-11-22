

# `AWSSupportRemediator-UpdateRdsInstanceMinorVersionUpgrade`

**Description**

Enables or disables automatic minor version upgrades on an Amazon Relational Database Service (Amazon RDS) DB instance by setting the `AutoMinorVersionUpgrade` property to the value specified in the `AutoMinorVersionUpgrade` parameter.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [RDS automatic minor version upgrades should be enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-13).

If the DB instance does not exist, or the current `AutoMinorVersionUpgrade` value already matches the requested value, the automation completes successfully without making changes.

The Amazon RDS DB instance must be in the `available` state for the change to take effect.

When `AutoMinorVersionUpgrade` is enabled, Amazon RDS might apply minor version upgrades during the next scheduled maintenance window. This can briefly affect DB instance availability.

The runbook records the initial value of `AutoMinorVersionUpgrade` in the `validateDB.InitialAutoMinorVersionUpgrade` output. You can reverse the change by rerunning the runbook with the original value.

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
+ AutoMinorVersionUpgrade

  Type: Boolean

  Description: (Required) The target value for the `AutoMinorVersionUpgrade` setting on the Amazon RDS DB instance.
+ RDSInstanceArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon RDS DB instance.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBInstances`
+ `rds:ModifyDBInstance`

**Document Steps**

1. **validateDB** - Validates that the Amazon RDS DB instance exists and determines whether its current `AutoMinorVersionUpgrade` value differs from the requested value.

1. **branchOnChangeRequired** - Branches on whether the runbook needs to update `AutoMinorVersionUpgrade` on the Amazon RDS DB instance.

1. **updateDBInstance** - Updates the `AutoMinorVersionUpgrade` setting on the Amazon RDS DB instance to the requested value.

**Outputs**
+ validateDB.DBIdentifier: The Amazon RDS DB instance identifier parsed from the input ARN.
+ validateDB.ChangeRequired: Whether a change to `AutoMinorVersionUpgrade` is required.
+ validateDB.ValidationMessage: The reason for the validation result.
+ validateDB.InitialAutoMinorVersionUpgrade: The value of `AutoMinorVersionUpgrade` on the DB instance before the runbook runs.