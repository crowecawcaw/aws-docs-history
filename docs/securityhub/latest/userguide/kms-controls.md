# Security Hub CSPM controls for AWS KMS

These AWS Security Hub CSPM controls evaluate the AWS Key Management Service (AWS KMS) service and resources. The
controls might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [KMS.1] IAM customer managed policies should not allow decryption actions on all KMS keys

**Related requirements:** NIST.800-53.r5 AC-2, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-6(3)

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::IAM::Policy`

**AWS Config rule:**
[iam-customer-policy-blocked-kms-actions](../../../config/latest/developerguide/iam-customer-policy-blocked-kms-actions.md "../../../config/latest/developerguide/iam-customer-policy-blocked-kms-actions.md")

**Schedule type:** Change triggered

**Parameters:**

- `blockedActionsPatterns: kms:ReEncryptFrom, kms:Decrypt` (not customizable)
- `excludePermissionBoundaryPolicy`: `True` (not customizable)

Checks whether the default version of IAM customer managed policies allow principals to
use the AWS KMS decryption actions on all resources. The control fails if the policy is open
enough to allow `kms:Decrypt` or `kms:ReEncryptFrom` actions on all
KMS keys.

The control only checks KMS keys in the Resource element and doesn't take into account any conditionals in the
Condition element of a policy. In addition, the control evaluates both attached and unattached customer managed policies. It doesn't
check inline policies or AWS managed policies.

With AWS KMS, you control who can use your KMS keys and gain access to your encrypted data.
IAM policies define which actions an identity (user, group, or role) can perform on which
resources. Following security best practices, AWS recommends that you allow least privilege.
In other words, you should grant to identities only the `kms:Decrypt` or
`kms:ReEncryptFrom` permissions and only for the keys that are required to perform a
task. Otherwise, the user might use keys that are not appropriate for your data.

Instead of granting permissions for all keys, determine the minimum set of keys that users
need to access encrypted data. Then design policies that allow users to use only those keys. For
example, do not allow `kms:Decrypt` permission on all KMS keys. Instead, allow
`kms:Decrypt` only on keys in a particular Region for your account. By adopting the
principle of least privilege, you can reduce the risk of unintended disclosure of your
data.

### Remediation

To modify an IAM customer managed policy, see [Editing customer managed policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-managed-policy-console") in
the _IAM User Guide_. When editing your policy, for the `Resource` field,
provide the Amazon Resource Name (ARN) of the specific key or keys that you want to allow decryption actions on.

## [KMS.2] IAM principals should not have IAM inline policies that allow decryption actions on all KMS keys

**Related requirements:** NIST.800-53.r5 AC-2, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-6(3)

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**

- `AWS::IAM::Group`
- `AWS::IAM::Role`
- `AWS::IAM::User`

**AWS Config rule:**
[iam-inline-policy-blocked-kms-actions](../../../config/latest/developerguide/iam-inline-policy-blocked-kms-actions.md "../../../config/latest/developerguide/iam-inline-policy-blocked-kms-actions.md")

**Schedule type:** Change triggered

**Parameters:**

- `blockedActionsPatterns: kms:ReEncryptFrom, kms:Decrypt` (not customizable)

This control checks whether the inline policies that are embedded in your IAM identities
(role, user, or group) allow the AWS KMS decryption and re-encryption actions on all KMS keys. The control fails
if the policy is open enough to allow `kms:Decrypt` or
`kms:ReEncryptFrom` actions on all KMS keys.

The control only checks KMS keys in the Resource element and doesn't take into account any conditionals in the
Condition element of a policy.

With AWS KMS, you control who can use your KMS keys and gain access to your encrypted data.
IAM policies define which actions an identity (user, group, or role) can perform on which
resources. Following security best practices, AWS recommends that you allow least privilege.
In other words, you should grant to identities only the permissions they need and only for keys
that are required to perform a task. Otherwise, the user might use keys that are not appropriate
for your data.

Instead of granting permission for all keys, determine the minimum set of keys that users
need to access encrypted data. Then design policies that allow the users to use only those keys.
For example, do not allow `kms:Decrypt` permission on all KMS keys. Instead, allow
the permission only on specific keys in a specific Region for your account. By adopting the
principle of least privilege, you can reduce the risk of unintended disclosure of your
data.

### Remediation

To modify an IAM inline policy, see [Editing inline policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-inline-policy-console "../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-inline-policy-console") in
the _IAM User Guide_. When editing your policy, for the `Resource` field,
provide the Amazon Resource Name (ARN) of the specific key or keys that you want to allow decryption actions on.

## [KMS.3] AWS KMS keys should not be deleted unintentionally

**Related requirements:** NIST.800-53.r5 SC-12, NIST.800-53.r5 SC-12(2)

**Category:** Protect > Data protection > Data deletion
protection

**Severity:** Critical

**Resource type:**
`AWS::KMS::Key`

**AWS Config rule:** `kms-cmk-not-scheduled-for-deletion-2` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether KMS keys are scheduled for deletion. The control fails if a
KMS key is scheduled for deletion.

KMS keys cannot be recovered once deleted. Data encrypted under a KMS key is also
permanently unrecoverable if the KMS key is deleted. If meaningful data has been encrypted
under a KMS key scheduled for deletion, consider decrypting the data or re-encrypting the data
under a new KMS key unless you are intentionally performing a _cryptographic
erasure_.

When a KMS key is scheduled for deletion, a mandatory waiting period is enforced to allow
time to reverse the deletion, if it was scheduled in error. The default waiting period is 30
days, but it can be reduced to as short as 7 days when the KMS key is scheduled for deletion.
During the waiting period, the scheduled deletion can be canceled and the KMS key will not be
deleted.

For additional information regarding deleting KMS keys, see [Deleting KMS keys](../../../kms/latest/developerguide/deleting-keys.md "../../../kms/latest/developerguide/deleting-keys.md") in the _AWS Key Management Service Developer Guide_.

### Remediation

To cancel a scheduled KMS key deletion, see
**To cancel key deletion** under [Scheduling and canceling key deletion (console)](../../../kms/latest/developerguide/deleting-keys-scheduling-key-deletion.md#deleting-keys-scheduling-key-deletion-console "../../../kms/latest/developerguide/deleting-keys-scheduling-key-deletion.md#deleting-keys-scheduling-key-deletion-console") in the _AWS Key Management Service Developer Guide_.

## [KMS.4] AWS KMS key rotation should be enabled

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/3.6, CIS AWS Foundations Benchmark v3.0.0/3.6, CIS AWS Foundations Benchmark v1.4.0/3.8, CIS AWS Foundations Benchmark v1.2.0/2.8, NIST.800-53.r5 SC-12, NIST.800-53.r5 SC-12(2), NIST.800-53.r5 SC-28(3), PCI DSS v3.2.1/3.6.4, PCI DSS v4.0.1/3.7.4

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::KMS::Key`

**AWS Config rule:**
[cmk-backing-key-rotation-enabled](../../../config/latest/developerguide/cmk-backing-key-rotation-enabled.md "../../../config/latest/developerguide/cmk-backing-key-rotation-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

AWS KMS enables customers to rotate the backing key, which is key material stored in
AWS KMS and is tied to the key ID of the KMS key. It's the backing key that is used
to perform cryptographic operations such as encryption and decryption. Automated key
rotation currently retains all previous backing keys so that decryption of encrypted
data can take place transparently.

CIS recommends that you enable KMS key rotation. Rotating encryption keys helps
reduce the potential impact of a compromised key because data encrypted with a new
key can't be accessed with a previous key that might have been exposed.

### Remediation

To enable KMS key rotation, see [How to enable and disable automatic key rotation](../../../kms/latest/developerguide/rotate-keys.md#rotating-keys-enable-disable "../../../kms/latest/developerguide/rotate-keys.md#rotating-keys-enable-disable") in the _AWS Key Management Service Developer Guide_.

## [KMS.5] KMS keys should not be publicly accessible

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** Critical

**Resource type:**
`AWS::KMS::Key`

**AWS Config rule:**
[kms-key-policy-no-public-access](../../../config/latest/developerguide/kms-key-policy-no-public-access.md "../../../config/latest/developerguide/kms-key-policy-no-public-access.md")

**Schedule type:** Change triggered

**Parameters:** None

This controls checks whether an AWS KMS key is publicly accessible. The control
fails if the KMS key is publicly accessible.

Implementing least privilege access is fundamental to reducing security risk and the
impact of errors or malicious intent. If the key policy for an AWS KMS key allows
access from external accounts, third parties might be able to encrypt and decrypt data
by using the key. This could result in an internal or external threat exfiltrating data
from AWS services that use the key.

###### Note

This control also returns a `FAILED` finding for an AWS KMS key if
your configurations prevent AWS Config from recording the key policy in the Configuration
Item (CI) for the KMS key. For AWS Config to populate the key policy in the CI for the
KMS key, the [AWS Config
role](../../../config/latest/developerguide/gs-cli-prereq.md#gs-cli-create-iamrole "../../../config/latest/developerguide/gs-cli-prereq.md#gs-cli-create-iamrole") must have access to read the key policy by using the [GetKeyPolicy](../../../kms/latest/APIReference/API_GetKeyPolicy.md "../../../kms/latest/APIReference/API_GetKeyPolicy.md") API call. To resolve this type of `FAILED`
finding, check policies that can prevent the AWS Config role from having read access to
the key policy for the KMS key. For example, check the following:

- The key policy for the KMS key.
- [Service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") and [resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in AWS Organizations that apply to your
  account.
- Permissions for the AWS Config role, if you are not using the [AWS Config
  service-linked role](../../../config/latest/developerguide/using-service-linked-roles.md "../../../config/latest/developerguide/using-service-linked-roles.md").
  In addition, this control doesn't evaluate policy conditions that use wildcard
  characters or variables. To produce a `PASSED` finding, conditions in the
  key policy must only use fixed values, which are values that don't contain wildcard
  characters or policy variables. For information about policy variables, see [Variables and
  tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _AWS Identity and Access Management User
  Guide_.

### Remediation

For information about updating the key policy for an AWS KMS key, see [Key
policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md#key-policy-overview "../../../kms/latest/developerguide/key-policies.md#key-policy-overview") in the _AWS Key Management Service Developer Guide_.
