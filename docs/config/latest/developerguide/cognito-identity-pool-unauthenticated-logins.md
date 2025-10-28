# cognito-identity-pool-unauthenticated-logins

Checks if Amazon Cognito identity pools disallow unauthenticated logins. The rule is NON_COMPLIANT if configuration.AllowUnauthenticatedIdentities is true.

**Identifier:** COGNITO_IDENTITY_POOL_UNAUTHENTICATED_LOGINS

**Resource Types:** AWS::Cognito::IdentityPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
