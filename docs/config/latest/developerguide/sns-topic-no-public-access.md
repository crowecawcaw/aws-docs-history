# sns-topic-no-public-access

Checks if the SNS topic access policy allows public access. The rule is NON\_COMPLIANT if the SNS topic access policy allows public access.

###### Note

To be considered non-public, an SNS policy must grant access only to fixed values. This means values that don't contain a wildcard or the following IAM policy element: [Variables](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-using-variables "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-using-variables").

**Identifier:** SNS\_TOPIC\_NO\_PUBLIC\_ACCESS

**Resource Types:** AWS::SNS::Topic

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
