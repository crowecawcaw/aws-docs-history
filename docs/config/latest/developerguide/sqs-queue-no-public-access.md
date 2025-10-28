# sqs-queue-no-public-access

Checks if the SQS queue access policy allows public access. The rule is NON_COMPLIANT if the SQS queue access policy allows public access.

###### Note

To be considered non-public, an SQS policy must grant access only to fixed values. This means values that don't contain a wildcard or the following IAM policy element: [Variables](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-using-variables "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-using-variables").

**Identifier:** SQS_QUEUE_NO_PUBLIC_ACCESS

**Resource Types:** AWS::SQS::Queue

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
