# cognito-user-pool-advanced-security-enabled

Checks if an Amazon Cognito user pool has advanced security enabled for standard authentication. The rule is NON\_COMPLIANT if advanced security is not enabled. Optionally, you can specify an advanced security mode for the rule to check.

**Identifier:** COGNITO\_USER\_POOL\_ADVANCED\_SECURITY\_ENABLED

**Resource Types:** AWS::Cognito::UserPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

SecurityMode (Optional)
Type: String

String value of the advanced security mode for the rule to check. If provided, the rule is NON\_COMPLIANT if the advanced security mode for user pools does not match this parameter value. Valid values are AUDIT and ENFORCED

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
