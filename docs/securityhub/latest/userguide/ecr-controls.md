# Security Hub CSPM controls for Amazon ECR

These Security Hub CSPM controls evaluate the Amazon Elastic Container Registry (Amazon ECR) service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [ECR.1] ECR private repositories should have image scanning configured

**Related requirements:** NIST.800-53.r5 RA-5, PCI DSS v4.0.1/6.2.3, PCI DSS v4.0.1/6.2.4

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** High

**Resource type:**
`AWS::ECR::Repository`

**AWS Config rule:**
[ecr-private-image-scanning-enabled](../../../config/latest/developerguide/ecr-private-image-scanning-enabled.md "../../../config/latest/developerguide/ecr-private-image-scanning-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether a private Amazon ECR repository has image scanning configured. The control fails if the private ECR
repository isn't configured for scan on push or continuous scanning.

ECR image scanning helps in identifying software vulnerabilities in your container images. Configuring image scanning on ECR repositories adds a layer of
verification for the integrity and safety of the images being stored.

### Remediation

To configure image scanning for an ECR repository, see [Image scanning](../../../AmazonECR/latest/userguide/image-scanning.md "../../../AmazonECR/latest/userguide/image-scanning.md")
in the _Amazon Elastic Container Registry User Guide_.

## [ECR.2] ECR private repositories should have tag immutability configured

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-8(1)

**Category:** Identify > Inventory > Tagging

**Severity:** Medium

**Resource type:**
`AWS::ECR::Repository`

**AWS Config rule:**
[ecr-private-tag-immutability-enabled](../../../config/latest/developerguide/ecr-private-tag-immutability-enabled.md "../../../config/latest/developerguide/ecr-private-tag-immutability-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a private ECR repository has tag immutability enabled. This control fails if a private ECR repository has tag
immutability disabled. This rule passes if tag immutability is enabled and has the value `IMMUTABLE`.

Amazon ECR Tag Immutability enables customers to rely on the descriptive tags of an image as a
reliable mechanism to track and uniquely identify images. An immutable tag is
static, which means each tag refers to a unique image. This improves reliability and
scalability as the use of a static tag will always result in the same image being
deployed. When configured, tag immutability prevents the tags from being overridden,
which reduces the attack surface.

### Remediation

To create a repository with immutable tags configured or to update the image tag mutability settings for an existing repository, see [Image tag mutability](../../../AmazonECR/latest/userguide/image-tag-mutability.md "../../../AmazonECR/latest/userguide/image-tag-mutability.md")
in the _Amazon Elastic Container Registry User Guide_.

## [ECR.3] ECR repositories should have at least one lifecycle policy configured

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Identify > Resource configuration

**Severity:** Medium

**Resource type:**
`AWS::ECR::Repository`

**AWS Config rule:**
[ecr-private-lifecycle-policy-configured](../../../config/latest/developerguide/ecr-private-lifecycle-policy-configured.md "../../../config/latest/developerguide/ecr-private-lifecycle-policy-configured.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon ECR repository has at least one lifecycle policy configured.
This control fails if an ECR repository does not have any lifecycle policies configured.

Amazon ECR lifecycle policies enable you to specify the lifecycle management of images in a repository. By configuring
lifecycle policies, you can automate the cleanup of unused images and the expiration of images based on age or count.
Automating these tasks can help you avoid unintentionally using outdated images in your repository.

### Remediation

To configure a lifecycle policy, see [Creating a lifecycle policy preview](../../../AmazonECR/latest/userguide/lpp_creation.md "../../../AmazonECR/latest/userguide/lpp_creation.md")
in the _Amazon Elastic Container Registry User Guide_.

## [ECR.4] ECR public repositories should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::ECR::PublicRepository`

**AWS Config rule:** `tagged-ecr-publicrepository` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon ECR public repository has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the public repository doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the public repository isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an ECR public repository, see [Tagging an Amazon ECR public repository](../../../AmazonECR/latest/public/ecr-public-using-tags.md "../../../AmazonECR/latest/public/ecr-public-using-tags.md") in the _Amazon Elastic Container Registry User Guide_.

## [ECR.5] ECR repositories should be encrypted with customer

managed AWS KMS keys

**Related requirements:** NIST.800-53.r5 SC-12(2),
NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5
SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 CA-9(1), NIST.800-53.r5 SI-7(6),
NIST.800-53.r5 AU-9

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::ECR::Repository`

**AWS Config rule:**
[ecr-repository-cmk-encryption-enabled](../../../config/latest/developerguide/ecr-repository-cmk-encryption-enabled.md "../../../config/latest/developerguide/ecr-repository-cmk-encryption-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter    | Description                                                                                                                                                                                             | Type                             | Allowed custom values                                                                                                         | Security Hub CSPM default value |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `kmsKeyArns` | A list of Amazon Resource Names (ARNs) of AWS KMS keys to<br>include in the evaluation. The control generates a<br>`FAILED` finding if an ECR repository isn't encrypted<br>with a KMS key in the list. | StringList (maximum of 10 items) | 1–10 ARNs of existing KMS keys. For example:<br>`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` | No default value                |

This control checks whether an Amazon ECR repository is encrypted at rest with a customer
managed AWS KMS key. The control fails if the ECR repository isn't encrypted with a
customer managed KMS key. You can optionally specify a list of KMS keys for the
control to include in the evaluation.

By default, Amazon ECR encrypts repository data with Amazon S3 managed keys (SSE-S3), using an
AES-256 algorithm. For additional control, you can configure Amazon ECR to encrypt the data
with an AWS KMS key (SSE-KMS or DSSE-KMS) instead. The KMS key can be: an
AWS managed key that Amazon ECR creates and manages for you and has the alias
`aws/ecr`, or a customer managed key that you create and manage in your
AWS account. With a customer managed KMS key, you have full control of the key. This
includes defining and maintaining the key policy, managing grants, rotating
cryptographic material, assigning tags, creating aliases, and enabling and disabling the
key.

###### Note

AWS KMS supports cross-account access to KMS keys. If an ECR repository is
encrypted with a KMS key that’s owned by another account, this control doesn’t
perform cross-account checks when it evaluates the repository. The control doesn’t
assess whether Amazon ECR can access and use the key when performing cryptographic
operations for the repository.

### Remediation

You can't change the encryption settings for an existing ECR repository. However,
you can specify different encryption settings for ECR repositories that you
subsequently create. Amazon ECR supports the use of different encryption settings for
individual repositories.

For more information about encryption options for ECR repositories, see [Encryption at
rest](../../../AmazonECR/latest/userguide/encryption-at-rest.md "../../../AmazonECR/latest/userguide/encryption-at-rest.md") in the _Amazon ECR User Guide_. For
more information about customer managed AWS KMS keys, see [AWS KMS keys](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the
_AWS Key Management Service Developer Guide_.
