# Security Hub controls for AWS Private CA

These AWS Security Hub controls evaluate the AWS Private Certificate Authority (AWS Private CA) service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [PCA.1] AWS Private CA root certificate authority should be disabled

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** Low

**Resource type:**
`AWS::ACMPCA::CertificateAuthority`

**AWS Config rule:**
[`acm-pca-root-ca-disabled`](../../../config/latest/developerguide/acm-pca-root-ca-disabled.md "../../../config/latest/developerguide/acm-pca-root-ca-disabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks if AWS Private CA has a root certificate authority (CA) that is disabled. The control fails if the root CA
is enabled.

With AWS Private CA, you can create a CA hierarchy that includes a root CA and subordinate CAs. You should minimize the use of
the root CA for daily tasks, especially in production environments. The root CA should only be used to issue certificates for
intermediate CAs. This allows the root CA to be stored out of harm's way while the intermediate CAs perform the daily task of
issuing end-entity certificates.

### Remediation

To disable the root CA, see [Update CA status](../../../privateca/latest/userguide/console-update.md#console-update-status-steps "../../../privateca/latest/userguide/console-update.md#console-update-status-steps")
in the _AWS Private Certificate Authority User Guide_.

## [PCA.2] AWS Private CA certificate authorities should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::ACMPCA::CertificateAuthority`

**AWS Config rule:** `acmpca-certificate-authority-tagged`

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requiredKeyTags` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           | This control checks whether an AWS Private CA certificate authority has tags with the specific keys defined in the parameter `requiredKeyTags`. The control fails if the certificate authority doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredKeyTags`. If the parameter `requiredKeyTags` isn't provided, the control only checks for the existence of a tag key and fails if the certificate authority isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored. A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [Define permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. ###### Note Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Best practices and strategies](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the _Tagging AWS Resources and Tag Editor User Guide_. ### Remediation To add tags to an AWS Private CA authority, see [Add tags for your private CA](../../../privateca/latest/userguide/PcaCaTagging.md "../../../privateca/latest/userguide/PcaCaTagging.md") in the _AWS Private Certificate Authority User Guide_. |
