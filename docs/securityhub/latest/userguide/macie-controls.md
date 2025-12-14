# Security Hub CSPM controls for Macie

These AWS Security Hub CSPM controls evaluate the Amazon Macie service.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Macie.1] Amazon Macie should be enabled

**Related requirements:** NIST.800-53.r5 CA-7,
NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 RA-5,
NIST.800-53.r5 SA-8(19),
NIST.800-53.r5 SI-4

**Category:** Detect > Detection services

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:**
[`macie-status-check`](../../../config/latest/developerguide/macie-status-check.md "../../../config/latest/developerguide/macie-status-check.md")

**Schedule type:** Periodic

This control checks whether Amazon Macie is enabled for an account. The control fails if Macie isn't enabled for the
account.

Amazon Macie discovers sensitive data using machine learning and pattern matching, provides visibility into data
security risks, and enables automated protection against those risks. Macie automatically and continually evaluates your
Amazon Simple Storage Service (Amazon S3) buckets for security and access control, and generates findings to notify you of potential issues with
the security or privacy of your Amazon S3 data. Macie also automates discovery and reporting of sensitive data, such as
personally identifiable information (PII), to provide you with a better understanding of the data that you store in
Amazon S3. To learn more, see the [_Amazon Macie User Guide_](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md").

### Remediation

To enable Macie, see [Enable Macie](../../../macie/latest/user/getting-started.md#enable-macie "../../../macie/latest/user/getting-started.md#enable-macie") in the _Amazon Macie User Guide_.

## [Macie.2] Macie automated sensitive data discovery should be enabled

**Related requirements:** NIST.800-53.r5 CA-7,
NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 RA-5,
NIST.800-53.r5 SA-8(19),
NIST.800-53.r5 SI-4

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::::Account`

**AWS Config rule:**
[`macie-auto-sensitive-data-discovery-check`](../../../config/latest/developerguide/macie-auto-sensitive-data-discovery-check.md "../../../config/latest/developerguide/macie-auto-sensitive-data-discovery-check.md")

**Schedule type:** Periodic

This control checks whether automated sensitive data discovery is enabled for an Amazon Macie administrator account.
The control fails if automated sensitive data discovery isn't enabled for a Macie administrator account. This control applies
only to administrator accounts.

Macie automates discovery and reporting of sensitive data, such as personally identifiable information (PII), in
Amazon Simple Storage Service (Amazon S3) buckets. With automated sensitive data discovery, Macie continually evaluates your bucket inventory and uses
sampling techniques to identify and select representative S3 objects from your buckets. Macie then analyzes the selected objects,
inspecting them for sensitive data. As the analyses progress, Macie updates statistics, inventory data, and other information that
it provides about your S3 data. Macie also generates findings to report sensitive data that it finds.

### Remediation

To create and configure automated sensitive data discovery jobs to analyze objects in S3 buckets, see [Configuring automated sensitive data discovery for your account](../../../macie/latest/user/discovery-asdd-account-manage.md "../../../macie/latest/user/discovery-asdd-account-manage.md") in the _Amazon Macie User Guide_.
