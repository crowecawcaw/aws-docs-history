# acm-certificate-expiration-check

Checks if AWS Certificate Manager Certificates in your account are marked for expiration within the specified number of days.
Certificates provided by ACM are automatically renewed. ACM does not automatically renew certificates that you import.
The rule is NON_COMPLIANT if your certificates are about to expire.

**Identifier:** ACM_CERTIFICATE_EXPIRATION_CHECK

**Resource Types:** AWS::ACM::Certificate

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West, Asia Pacific (Osaka) Region

**Parameters:**

daysToExpiration (Optional)
Type: int
Default: 14

Specify the number of days before the rule flags the ACM Certificate as noncompliant.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
