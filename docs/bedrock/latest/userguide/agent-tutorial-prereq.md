# Prerequisites

Before you begin this tutorial, make sure you have the following:

- AWS account with the following managed policies:
  - [AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess")
  - [AWSLambda_FullAccess](../../../lambda/latest/dg/security-iam-awsmanpol.md#lambda-security-iam-awsmanpol-AWSLambda_FullAccess "../../../lambda/latest/dg/security-iam-awsmanpol.md#lambda-security-iam-awsmanpol-AWSLambda_FullAccess")
  - [IAMFullAccess](aws-managed-policy/latest/reference/IAMFullAccess.md "aws-managed-policy/latest/reference/IAMFullAccess.md")

###### Important

These permissions allow you to run this tutorial and other, unrelated, tasks. In
production environments be sure to assign only those permissions
that your users need to run your application.

- Basic understanding of IAM roles and permissions ([IAM User
  Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md"))
- Familiarity with AWS Lambda functions ([Lambda Developer Guide](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md"))
