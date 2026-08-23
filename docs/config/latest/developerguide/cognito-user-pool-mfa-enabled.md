# cognito-user-pool-mfa-enabled

Checks if Amazon Cognito user pools configured with a PASSWORD-only sign-in policy have Multi-Factor Authentication (MFA) enabled. This rule is NON\_COMPLIANT if the Cognito user pool configured with PASSWORD only sign in policy does not have MFA enabled.

**Identifier:** COGNITO\_USER\_POOL\_MFA\_ENABLED

**Resource Types:** AWS::Cognito::UserPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
