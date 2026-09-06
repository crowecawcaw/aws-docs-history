

# acm-certificate-transparent-logging-enabled
<a name="acm-certificate-transparent-logging-enabled"></a>

Checks if AWS Certificate Manager certificates have certificate transparency logging enabled. The rule is NON\_COMPLIANT if CertificateTransparencyLoggingPreference is explicitly set DISABLED. 



**Identifier:** ACM\_CERTIFICATE\_TRANSPARENT\_LOGGING\_ENABLED

**Resource Types:** AWS::ACM::Certificate

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7c11c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).