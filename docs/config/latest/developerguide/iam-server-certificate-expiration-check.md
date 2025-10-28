# iam-server-certificate-expiration-check

Checks if AWS IAM SSL/TLS server certificates stored in IAM are expired. The rule is NON_COMPLIANT if an IAM server certificate is expired.

**Identifier:** IAM_SERVER_CERTIFICATE_EXPIRATION_CHECK

**Resource Types:** AWS::IAM::ServerCertificate

**Trigger type:** Periodic

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
