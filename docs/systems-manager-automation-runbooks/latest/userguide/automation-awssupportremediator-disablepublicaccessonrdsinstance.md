

# `AWSSupportRemediator-DisablePublicAccessOnRdsInstance`

**Description**

Disables public access on an Amazon Relational Database Service (Amazon RDS) DB instance by setting the `PubliclyAccessible` attribute to `false`.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [RDS DB Instances should prohibit public access, as determined by the PubliclyAccessible configuration](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-2).

If the DB instance does not exist or public access is already disabled, the automation completes successfully without making changes.

Disabling public access terminates ongoing public network connections to the DB instance. This change affects applications that rely on reaching the DB instance from outside its Amazon Virtual Private Cloud (Amazon VPC).

To reverse this change, modify the DB instance and set `PubliclyAccessible` to `true`.

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

  Description: (Required) The identifier of the Amazon RDS DB instance.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBInstances`
+ `rds:ModifyDBInstance`

**Document Steps**

1. **validateDBInstance** - Validates that the Amazon RDS DB instance exists and checks whether it has public access enabled.

1. **branchOnChangeRequired** - Branches on whether the runbook needs to disable public access.

1. **disableDBInstancePublicAccess** - Disables public access on the Amazon RDS DB instance by setting `PubliclyAccessible` to `false`.

**Outputs**
+ validateDBInstance.ChangeRequired: Whether a change is required.
+ validateDBInstance.ValidationMessage: The reason for the validation result.