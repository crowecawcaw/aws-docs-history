

# `AWSSupportRemediator-EnableRdsMultiAz`

**Description**

Converts an Amazon Relational Database Service (Amazon RDS) DB instance to a Multi-AZ deployment.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon RDS Multi-AZ](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-rds-multi-az).

If the DB instance does not exist, is already a Multi-AZ deployment, or already has a pending Multi-AZ modification, the automation completes successfully without making changes.

The modification applies during the next maintenance window of the DB instance. Enabling Multi-AZ might increase costs due to the standby DB instance. For more information about pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/).

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

1. **validateDBInstance** - Validates whether the Amazon RDS DB instance exists and is already a Multi-AZ deployment.

1. **branchOnChangeRequired** - Branches on whether modification is needed.

1. **updateDBInstance** - Modifies the Amazon RDS DB instance to enable Multi-AZ deployment. The modification applies during the next maintenance window.

**Outputs**
+ validateDBInstance.ChangeRequired: Whether the DB instance requires modification.
+ validateDBInstance.ValidationMessage: A message describing the validation result.