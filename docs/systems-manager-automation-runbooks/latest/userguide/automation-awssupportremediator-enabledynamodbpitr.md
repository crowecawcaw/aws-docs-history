

# `AWSSupportRemediator-EnableDynamoDbPitr`

**Description**

Enables point-in-time recovery for an Amazon DynamoDB table.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon DynamoDB Point-in-time Recovery](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-dynamodb-table-point-in-time-recovery).

If the DynamoDB table does not exist or point-in-time recovery is already enabled, the automation completes successfully without making changes.

Enabling point-in-time recovery incurs additional DynamoDB backup costs. For more information about pricing, see [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/).

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
+ DynamoDBTableArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the DynamoDB table.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `dynamodb:DescribeContinuousBackups`
+ `dynamodb:UpdateContinuousBackups`

**Document Steps**

1. **validateTable** - Validates that the DynamoDB table exists and checks whether point-in-time recovery is already enabled.

1. **branchOnChangeRequired** - Branches on whether point-in-time recovery needs to be enabled.

1. **enablePitr** - Enables point-in-time recovery for the DynamoDB table.

**Outputs**
+ validateTable.TableName: The name of the DynamoDB table.
+ validateTable.ChangeRequired: Whether point-in-time recovery needs to be enabled.
+ validateTable.ValidationMessage: The reason for the validation result.