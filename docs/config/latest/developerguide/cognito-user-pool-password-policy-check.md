# cognito-user-pool-password-policy-check

Checks if the password policy for Amazon cognito user pool meets the specified requirements indicated in the parameters. The rule is NON_COMPLIANT if the user pool password policy does not meet the specified requirements.

**Identifier:** COGNITO_USER_POOL_PASSWORD_POLICY_CHECK

**Resource Types:** AWS::Cognito::UserPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

requireSymbols (Optional)
Type: boolean
Default: True

Whether to require at least one symbol in password.

temporaryPasswordValidity (Optional)
Type: int
Default: 7

Number of days a temporary password remains valid.

minLength (Optional)
Type: int
Default: 8

Minimum length required for user pool password.

requireNumbers (Optional)
Type: boolean
Default: True

Whether to require at least one number in password.

requireUppercase (Optional)
Type: boolean
Default: True

Whether to require at least one uppercase letter in password.

requireLowercase (Optional)
Type: boolean
Default: True

Whether to require at least one lowercase letter in password.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
