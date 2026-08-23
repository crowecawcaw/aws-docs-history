# kms-key-policy-no-public-access

Checks if the AWS KMS key policy allows public access. The rule is NON\_COMPLIANT if the KMS key policy allows public access to the KMS key.

###### Note

To be considered non-public, a KMS key policy must grant access only to fixed values. This means values that don't contain a wildcard or the following IAM policy element: [Variables](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-using-variables "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-using-variables").

**Identifier:** KMS\_KEY\_POLICY\_NO\_PUBLIC\_ACCESS

**Resource Types:** AWS::KMS::Key

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
