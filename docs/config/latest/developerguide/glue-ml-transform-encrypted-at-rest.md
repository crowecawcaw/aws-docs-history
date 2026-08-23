# glue-ml-transform-encrypted-at-rest

Checks if an AWS Glue ML Transform has encryption at rest enabled. The rule is NON\_COMPLIANT if `MLUserDataEncryptionMode` is set to `DISABLED`.

**Identifier:** GLUE\_ML\_TRANSFORM\_ENCRYPTED\_AT\_REST

**Resource Types:** AWS::Glue::MLTransform

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
