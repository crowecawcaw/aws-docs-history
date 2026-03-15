# acm-certificate-transparent-logging-enabled

Checks if AWS Certificate Manager certificates have certificate transparency logging enabled. The rule is NON_COMPLIANT if CertificateTransparencyLoggingPreference is explicitly set DISABLED.

**Identifier:** ACM_CERTIFICATE_TRANSPARENT_LOGGING_ENABLED

**Resource Types:** AWS::ACM::Certificate

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
