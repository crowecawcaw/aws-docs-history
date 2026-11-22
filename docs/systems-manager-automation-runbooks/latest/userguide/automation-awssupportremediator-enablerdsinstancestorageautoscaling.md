

# `AWSSupportRemediator-EnableRdsInstanceStorageAutoScaling`

**Description**

Enables storage autoscaling for an Amazon Relational Database Service (Amazon RDS) DB instance by setting the `MaxAllocatedStorage` parameter.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon RDS DB instances have storage autoscaling turned off](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-rds-db-instance-storage-autoscaling-off).

If the Amazon RDS DB instance does not exist or storage autoscaling is already enabled, the automation completes successfully without making changes.

The Amazon RDS DB instance must be in `available` status. If the DB instance is in any other status, the automation fails.

Enabling storage autoscaling might increase storage costs. Amazon RDS automatically scales storage up to the configured maximum. For more information about pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/).

The maximum storage threshold must be at least 10% more than the current allocated storage. We recommend setting it to at least 26% more. For more information, see [Managing capacity automatically with Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.Autoscaling.html).

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

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon RDS DB instance.
+ MaxAllocatedStorageIncreasePercentage

  Type: Integer

  Description: (Optional) The percentage increase over the current allocated storage to set as the maximum allocated storage. The value must be between 10 and 100.

  Default: 26

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBInstances`
+ `rds:ModifyDBInstance`

**Document Steps**

1. **validateDB** - Validates that the Amazon RDS DB instance exists, is in `available` status, and does not already have storage autoscaling enabled.

1. **branchOnChangeRequired** - Branches on whether storage autoscaling needs to be enabled.

1. **updateDBInstance** - Enables storage autoscaling for the Amazon RDS DB instance by setting the maximum allocated storage.

**Outputs**
+ validateDB.ChangeRequired: Whether a change is required.
+ validateDB.ValidationMessage: The reason when no change is required.
+ validateDB.DBIdentifier: The identifier of the Amazon RDS DB instance.
+ validateDB.MaxAllocatedStorage: The maximum allocated storage value set for the DB instance.