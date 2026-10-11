

# cognito-user-pool-password-policy-check
<a name="cognito-user-pool-password-policy-check"></a>

Checks if the password policy for Amazon cognito user pool meets the specified requirements indicated in the parameters. The rule is NON\_COMPLIANT if the user pool password policy does not meet the specified requirements. 



**Identifier:** COGNITO\_USER\_POOL\_PASSWORD\_POLICY\_CHECK

**Resource Types:** AWS::Cognito::UserPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

minLength (Optional)Type: intDefault: 8  
Minimum length required for user pool password. Valid values are 6 to 99.

requireLowercase (Optional)Type: booleanDefault: True  
Whether to require at least one lowercase letter in password.

requireNumbers (Optional)Type: booleanDefault: True  
Whether to require at least one number in password.

requireSymbols (Optional)Type: booleanDefault: True  
Whether to require at least one symbol in password.

requireUppercase (Optional)Type: booleanDefault: True  
Whether to require at least one uppercase letter in password.

temporaryPasswordValidity (Optional)Type: intDefault: 7  
Number of days a temporary password remains valid. Valid values are 1 to 365.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d433c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).