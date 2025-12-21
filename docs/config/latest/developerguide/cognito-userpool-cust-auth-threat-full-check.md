# cognito-userpool-cust-auth-threat-full-check

Checks if Amazon Cognito user pools have threat protection enabled with full-function enforcement mode for custom authentication. This rule is NON_COMPLIANT if threat protection for custom authentication is not set to full-function enforcement mode.

**Identifier:** COGNITO_USERPOOL_CUST_AUTH_THREAT_FULL_CHECK

**Resource Types:** AWS::Cognito::UserPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
