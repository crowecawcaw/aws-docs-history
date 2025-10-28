# `AWSConfigRemediation-EnableEncryptionOnDynamoDbTable`

**Description**

The `AWSConfigRemediation-EnableEncryptionOnDynamoDbTable` runbook encrypts an
Amazon DynamoDB (DynamoDB) table using the AWS Key Management Service (AWS KMS) customer managed key you specify for the
`KMSKeyId` parameter.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableEncryptionOnDynamoDbTable "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableEncryptionOnDynamoDbTable")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf.

- KMSKeyId

Type: String

Description: (Required) The ARN of the customer managed key you want to use to encrypt the
DynamoDB table you specify in the `TableName` parameter.

- TableName

Type: String

Description: (Required) The name of the DynamoDB table you want to encrypt.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `dynamodb:DescribeTable`
- `dynamodb:UpdateTable`

**Document Steps**

- `aws:executeAwsApi` - Encrypts the DynamoDB table you specify in the
  `TableName` parameter.
- `aws:waitForAwsResourceProperty` - Verifies the `Enabled`
  property for the DynamoDB table's `SSESpecification` is set to
  `true` .
- `aws:assertAwsResourceProperty` - Verifies the DynamoDB table is encrypted
  with the customer managed key specified in the `KMSKeyId` parameter.
