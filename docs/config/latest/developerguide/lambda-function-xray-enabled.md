# lambda-function-xray-enabled

Checks if AWS X-Ray is enabled on AWS Lambda functions.The rule is NON_COMPLIANT if X-Ray tracing is disabled for a Lambda function.

**Identifier:** LAMBDA_FUNCTION_XRAY_ENABLED

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
