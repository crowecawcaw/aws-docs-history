

# `AWSSupportRemediator-EnableDynamoDbDeletionProtection`

**Description**

Enables deletion protection for an Amazon DynamoDB table by calling the `UpdateTable` API with `DeletionProtectionEnabled` set to `true`.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [DynamoDB tables should have deletion protection enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-6).

If the DynamoDB table does not exist or deletion protection is already enabled, the automation completes successfully without making changes.

The automation modifies only the specified DynamoDB table and does not affect its data, indexes, or replicas. To revert the change, disable deletion protection on the DynamoDB table by calling `UpdateTable` with `DeletionProtectionEnabled` set to `false`.

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
+ `dynamodb:DescribeTable`
+ `dynamodb:UpdateTable`

**Document Steps**

1. **validateTable** - Validates that the DynamoDB table exists and checks whether deletion protection is already enabled.

1. **branchOnChangeRequired** - Branches on whether deletion protection needs to be enabled on the DynamoDB table.

1. **updateTable** - Enables deletion protection on the DynamoDB table by calling the `UpdateTable` API with `DeletionProtectionEnabled` set to `true`.

**Outputs**
+ validateTable.TableName: The name of the DynamoDB table.
+ validateTable.ChangeRequired: Whether deletion protection needs to be enabled on the DynamoDB table.
+ validateTable.InitialDeletionProtection: The initial deletion protection setting of the DynamoDB table.
+ validateTable.ValidationMessage: A message describing the validation result.