# ses-sending-tls-required

Checks if Amazon Simple Email Service (SES) Configuration Set has TLS encryption enforced for email delivery. The rule is NON_COMPLIANT if the TLS Policy is not set to 'REQUIRE' in the Configuration Set.

**Identifier:** SES_SENDING_TLS_REQUIRED

**Resource Types:** AWS::SES::ConfigurationSet

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
