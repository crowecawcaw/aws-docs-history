# acm-pca-root-ca-disabled

Checks if AWS Private Certificate Authority (AWS Private CA) has a root CA that is disabled. The rule is NON_COMPLIANT for root CAs with status that is not DISABLED.

**Identifier:** ACM_PCA_ROOT_CA_DISABLED

**Resource Types:** AWS::ACMPCA::CertificateAuthority

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

exemptedCAArns (Optional)
Type: CSV

Comma-separated list of Amazon Resource Names (ARN) of CA's that can be enabled. This value can be supplied for other CAs, like specific root CAs or intermediate CA's that can be enabled.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
