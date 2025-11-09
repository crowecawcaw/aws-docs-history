# Security Hub controls for AWS Certificate Manager

These AWS Security Hub controls evaluate the AWS Certificate Manager (ACM) service and resources. The controls
might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [ACM.1] Imported and ACM-issued certificates should be renewed after a specified time period

**Related requirements:** NIST.800-53.r5 SC-28(3),
NIST.800-53.r5 SC-7(16), NIST.800-171.r2 3.13.15, PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::ACM::Certificate`

**AWS Config rule:**
[acm-certificate-expiration-check](../../../config/latest/developerguide/acm-certificate-expiration-check.md "../../../config/latest/developerguide/acm-certificate-expiration-check.md")

**Schedule type:** Change triggered and periodic

**Parameters:**

| Parameter          | Description                                                     | Type    | Allowed custom values | Security Hub default value |
| ------------------ | --------------------------------------------------------------- | ------- | --------------------- | -------------------------- |
| `daysToExpiration` | Number of days within which the ACM certificate must be renewed | Integer | `14` to `365`         | `30`                       |

This control checks whether an AWS Certificate Manager (ACM) certificate is renewed within the specified time period. It checks both imported certificates and certificates provided by
ACM. The control fails if the certificate isn't renewed within the specified time period. Unless you provide a custom parameter value for the renewal
period, Security Hub uses a default value of 30 days.

ACM can automatically renew certificates that use DNS validation. For certificates that
use email validation, you must respond to a domain validation email. ACM doesn't
automatically renew certificates that you import. You must renew imported
certificates manually.

### Remediation

ACM provides managed renewal for your SSL/TLS certificates issued by Amazon. This means
that ACM either renews your certificates automatically (if you use DNS
validation), or it sends you email notices when the certificate expiration
approaches. These services are provided for both public and private ACM
certificates.

**For domains validated by email**

When a certificate is 45 days from expiration, ACM sends to the domain owner an email
for each domain name. To validate the domains and complete the renewal, you must respond to
the email notifications.

For more information, see [Renewal for domains validated by
email](../../../acm/latest/userguide/email-renewal-validation.md "../../../acm/latest/userguide/email-renewal-validation.md") in the _AWS Certificate Manager User Guide_.

**For domains validated by DNS**

ACM automatically renews certificates that use DNS validation. 60 days before the
expiration, ACM verifies that the certificate can be renewed.

If it cannot validate a domain name, then ACM sends a notification that manual
validation is required. It sends these notifications 45 days, 30 days, 7 days, and 1 day
before the expiration.

For more information, see [Renewal for domains validated by
DNS](../../../acm/latest/userguide/dns-renewal-validation.md "../../../acm/latest/userguide/dns-renewal-validation.md") in the _AWS Certificate Manager User Guide_.

## [ACM.2] RSA certificates managed by ACM should use a key length of at least 2,048 bits

**Related requirements:** PCI DSS v4.0.1/4.2.1

**Category:** Identify > Inventory > Inventory services

**Severity:** High

**Resource type:**
`AWS::ACM::Certificate`

**AWS Config rule:**
[acm-certificate-rsa-check](../../../config/latest/developerguide/acm-certificate-rsa-check.md "../../../config/latest/developerguide/acm-certificate-rsa-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether RSA certificates managed by AWS Certificate Manager use a key length of at least 2,048 bits. The control
fails if the key length is smaller than 2,048 bits.

The strength of encryption directly correlates with key size. We recommend key lengths of at least 2,048 bits to
protect your AWS resources as computing power becomes less expensive and servers become more advanced.

### Remediation

The minimum key length for RSA certificates issued by ACM is already 2,048 bits. For instructions on issuing
new RSA certificates with ACM, see [Issuing and managing certificates](../../../acm/latest/userguide/gs.md "../../../acm/latest/userguide/gs.md") in the _AWS Certificate Manager User Guide_.

While ACM allows you to import certificates with shorter key lengths, you must use keys of at least 2,048 bits to pass this
control. You can't change the key length after importing a certificate. Instead, you must delete certificates with a key length smaller than 2,048 bits.
For more information about importing certificates into ACM, see
[Prerequisites for importing certificates](../../../acm/latest/userguide/import-certificate-prerequisites.md "../../../acm/latest/userguide/import-certificate-prerequisites.md") in the _AWS Certificate Manager User Guide_.

## [ACM.3] ACM certificates should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::ACM::Certificate`

**AWS Config rule:** `tagged-acm-certificate` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an AWS Certificate Manager (ACM) certificate has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the certificate doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the certificate isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to an ACM certificate, see
[Tagging AWS Certificate Manager certificates](../../../acm/latest/userguide/tags.md "../../../acm/latest/userguide/tags.md") in the _AWS Certificate Manager User Guide_.
