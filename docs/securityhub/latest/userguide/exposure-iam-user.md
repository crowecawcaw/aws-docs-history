# Remediating exposures for IAM users

AWS Security Hub can generate exposure findings for AWS Identity and Access Management (IAM) users.

On the Security Hub console, the IAM user involved in an exposure finding and its identifying information are listed in
the **Resources** section of the finding details. Programmatically, you can retrieve resource
details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it.
Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential,
follow these recommended remediation steps to help mitigate the risk. The remediation topics are
divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down
its severity level by addressing just one remediation topic. Your approach to risk remediation
depends on your organizational requirements and workloads.

###### Note

The remediation guidance provided in this topic might require additional consultation in other AWS resources.

IAM best practices recommend that you create IAM roles or use federation with an identity provider to access AWS
using temporary credentials instead of creating individual IAM users. If that is an option for your organization and
use case, switch to roles or federation instead of using IAM users. For more information, see
[IAM users](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") in the _IAM User Guide_.

###### Contents

- [Misconfiguration traits for IAM users](exposure-iam-user.md#iam-user-misconfiguration "exposure-iam-user.md#iam-user-misconfiguration")

  - [The IAM user does not have MFA enabled](exposure-iam-user.md#user-mfa-disabled "exposure-iam-user.md#user-mfa-disabled")
  - [The AWS account for the IAM user has weak password policies](exposure-iam-user.md#weak-password-policies "exposure-iam-user.md#weak-password-policies")
  - [The IAM user has unrotated access keys](exposure-iam-user.md#unrotated-access-keys "exposure-iam-user.md#unrotated-access-keys")
  - [The IAM user has a policy that allows unrestricted access to KMS key decryption](exposure-iam-user.md#unrestricted-kms-decryption-allowed "exposure-iam-user.md#unrestricted-kms-decryption-allowed")

- [Unused access traits for IAM users](exposure-iam-user.md#iam-user-unused-access "exposure-iam-user.md#iam-user-unused-access")
- [Impact traits for IAM users](exposure-iam-user.md#iam-user-impact "exposure-iam-user.md#iam-user-impact")

  - [Has full control privileged executor path](exposure-iam-user.md#has-full-control-privileged-executor-path "exposure-iam-user.md#has-full-control-privileged-executor-path")
  - [Has direct policy escalation path](exposure-iam-user.md#has-direct-policy-escalation-path "exposure-iam-user.md#has-direct-policy-escalation-path")
  - [Has trust policy hijack path](exposure-iam-user.md#has-trust-policy-hijack-path "exposure-iam-user.md#has-trust-policy-hijack-path")
  - [Has data ransomware path](exposure-iam-user.md#has-data-ransomware-path "exposure-iam-user.md#has-data-ransomware-path")
  - [Has remove restriction path](exposure-iam-user.md#has-remove-restriction-path "exposure-iam-user.md#has-remove-restriction-path")
  - [Has pass role create executor path](exposure-iam-user.md#has-pass-role-create-executor-path "exposure-iam-user.md#has-pass-role-create-executor-path")
  - [Has swap role existing executor path](exposure-iam-user.md#has-swap-role-existing-executor-path "exposure-iam-user.md#has-swap-role-existing-executor-path")
  - [Has role chain escalation path](exposure-iam-user.md#has-role-chain-escalation-path "exposure-iam-user.md#has-role-chain-escalation-path")
  - [Has inject code privileged executor path](exposure-iam-user.md#has-inject-code-privileged-executor-path "exposure-iam-user.md#has-inject-code-privileged-executor-path")
  - [Has disable audit trail path](exposure-iam-user.md#has-disable-audit-trail-path "exposure-iam-user.md#has-disable-audit-trail-path")
  - [Has access existing executor path](exposure-iam-user.md#has-access-existing-executor-path "exposure-iam-user.md#has-access-existing-executor-path")
  - [Has credential minting path](exposure-iam-user.md#has-credential-minting-path "exposure-iam-user.md#has-credential-minting-path")
  - [Has pass role data access path](exposure-iam-user.md#has-pass-role-data-access-path "exposure-iam-user.md#has-pass-role-data-access-path")
  - [Has pass role task hijack path](exposure-iam-user.md#has-pass-role-task-hijack-path "exposure-iam-user.md#has-pass-role-task-hijack-path")
  - [Has single hop data access path](exposure-iam-user.md#has-single-hop-data-access-path "exposure-iam-user.md#has-single-hop-data-access-path")
  - [Has capability advancing path](exposure-iam-user.md#has-capability-advancing-path "exposure-iam-user.md#has-capability-advancing-path")

## Misconfiguration traits for IAM users

Here are misconfiguration traits for IAM users and suggested remediation steps.

### The IAM user does not have MFA enabled

Multi-factor authentication (MFA) adds an extra layer of protection on top of a user name and password.
When MFA is enabled and an IAM user signs in to an AWS website, they are prompted for their user name, password, and an authentication code from their AWS MFA device.
The authenticating principal must possess a device that emits a time-sensitive key and must have knowledge of a credential.
Without MFA, if a user’s password is compromised, an attacker gains full access to the user’s AWS permissions.
Following standard security principles, enable MFA for all accounts and users that have AWS Management Console access.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Review MFA types

AWS supports the following [MFA types](../../../IAM/latest/UserGuide/id_credentials_mfa.md#id_credentials_mfa-types "../../../IAM/latest/UserGuide/id_credentials_mfa.md#id_credentials_mfa-types"):

- Passkeys and security keys
- Virtual authenticator applications
- Hardware TOTP tokens

Although authentication with a physical device typically provides more stringent security protection, using any type of MFA is more secure than having MFA disabled.

###### Enable MFA

To enable the MFA type that suits your requirements, see [AWS multi-factor authentication in IAM](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the _IAM User Guide_.
Follow the steps for the specific MFA type you want to implement. For organizations managing many users, you may want to enforce MFA usage by requiring MFA to access sensitive resources.

### The AWS account for the IAM user has weak password policies

Password policies help protect against unauthorized access by enforcing minimum complexity requirements for IAM user passwords.
Without strong password policies, there’s an increased risk that user accounts could be compromised through password guessing or brute force attacks.
Following standard security principles, implement a strong password policy to ensure users create complex passwords that are difficult to guess.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Configure a strong password policy

Go to the IAM dashboard and navigate to Account settings.
Review the current password policy settings for your account, including minimum length, character types required, and password expiration settings.

At a minimum, follow these best practices when setting your password policy:

- Require at least one uppercase character.
- Require at least one lowercase character.
- Require at least one symbol.
- Require at least one number.
- Require at least eight characters.

###### Additional security considerations

Consider these additional security measures in addition to a strong password policy:

- MFA adds an additional security layer by requiring an additional form of authentication.
  This helps prevent unauthorized access even if credentials are compromised.
- Setting up condition elements to restrict when and how administrative permissions can be used based on factors like source IP or MFA age.

### The IAM user has unrotated access keys

Access keys consist of an access key ID and a secret access key that enable programmatic access to AWS resources.
When access keys remain unchanged for extended periods of time, they increase the risk of unauthorized access if they are compromised.
Following security best practices, rotate access keys every 90 days to minimize the window of opportunity for attackers to use compromised credentials.

###### Remediation: Rotate access keys

In the exposure finding, open the resource.
This opens the user details window.
To rotate access keys, see [Manage access keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey") in the _IAM User Guide_.

### The IAM user has a policy that allows unrestricted access to KMS key decryption

AWS KMS enables you to create and manage cryptographic keys that are used to protect your data.
IAM policies that allow unrestricted AWS KMS decryption permissions (for example, `kms:Decrypt` or `kms:ReEncryptFrom`) on all KMS keys can lead to unauthorized data access if an IAM user’s credentials are compromised.
If an attacker gains access to these credentials, they could potentially decrypt any encrypted data in your environment, which could include sensitive data.
Following security best practices, implement least privilege by limiting AWS KMS decryption permissions to only specific keys that users need for their job functions.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Implement least-privilege access

In the exposure finding, open the resource. This opens the IAM Policy window. Look for permissions in KMS that allow kms:Decrypt or `kms:ReEncryptFrom` or `KMS:*` with a resource specification of `"*"`.

Update the policy to restrict AWS KMS decryption permissions to only the specific keys needed. Modify the policy to replace the `"*"` resource with the specific ARNs of required AWS KMS keys.

###### Secure configuration considerations

Consider adding conditions to further restrict when these permissions can be used.
For example, you can limit decryption operations to specific VPC endpoints or source IP ranges.
You can also configure key policies to further restrict who can use specific KMS keys.

## Unused access traits for IAM users

When an IAM user has unused permissions, access keys, or passwords, Security Hub may include these as contextual traits in exposure findings for that user. These traits are generated by the service-managed IAM Access Analyzer and provide additional context about the user's security posture. Unused access traits are not the primary cause of the exposure finding, but they indicate that the user has more permissions than needed, which increases the potential impact if the user's credentials are compromised.

For unused permissions specifically, you can generate a least-privilege policy recommendation that shows you a scoped-down replacement policy. For more information, see [Generating policy recommendations for unused access findings](unused-access-recommendations.md "unused-access-recommendations.md").

## Impact traits for IAM users

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the
effective permissions of the AWS Identity and Access Management principal associated with the IAM user
to determine the downstream resources an attacker could reach if the IAM user
is compromised. Each impact trait identifies a specific privilege escalation pattern.
To reduce your blast radius, review the permission paths described in each trait and
remove any unnecessary privileges.

Following standard security principles, grant least
privilege by providing only the permissions required to perform a task. Replace broad
policies with scoped-down policies that grant only the specific actions and
resources needed. To identify unused permissions to remove, use IAM Access Analyzer to
generate recommendations based on access history. For more information, see [Findings for external
and unused access](../../../IAM/latest/UserGuide/access-analyzer-findings.md "../../../IAM/latest/UserGuide/access-analyzer-findings.md") and [Apply
least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the
_IAM User Guide_.

### Has full control privileged executor path

The associated principal can pass a role to and inject code into a compute resource that already has elevated permissions. This allows the principal to gain full control over the executor and perform any action that the executor's role permits.

### Has direct policy escalation path

The associated principal can directly modify IAM policies to grant itself additional permissions, escalating its own privileges without intermediate resources.

### Has trust policy hijack path

The associated principal can modify the trust policy of an IAM role to allow itself to assume that role, gaining the role's permissions.

### Has data ransomware path

The associated principal can encrypt or delete data in a way that could be used for ransomware, such as encrypting Amazon S3 objects with a customer-managed AWS KMS key and then modifying the key policy.

### Has remove restriction path

The associated principal can remove security restrictions such as permission boundaries, service control policies, or resource-based policy deny statements, expanding what other principals or the resource itself can do.

### Has pass role create executor path

The associated principal can create a new compute resource (such as a Lambda function or Amazon EC2 instance) and pass it a privileged role, effectively laundering its own permissions through the new resource.

### Has swap role existing executor path

The associated principal can change the IAM role attached to an existing compute resource, replacing it with a more privileged role to escalate access.

### Has role chain escalation path

The associated principal can assume a sequence of roles, where each role in the chain has progressively broader permissions, ultimately reaching a highly privileged role.

### Has inject code privileged executor path

The associated principal can inject code into a running compute resource that has elevated permissions, executing arbitrary operations under that resource's privileged role.

### Has disable audit trail path

The associated principal can disable logging or monitoring services such as CloudTrail, effectively covering its tracks during or after an escalation.

### Has access existing executor path

The associated principal can invoke or connect to an existing compute resource and use its attached role to perform privileged actions.

### Has credential minting path

The associated principal can create new long-term credentials (such as access keys or login profiles) for other principals, establishing persistent access paths that survive password rotations or session expirations.

### Has pass role data access path

The associated principal can create a service resource and pass it a role that has access to sensitive data, gaining indirect access to that data through the new resource.

### Has pass role task hijack path

The associated principal can pass a role to a scheduled or event-driven task (such as a Lambda function triggered by an event), allowing it to execute arbitrary code with that role's permissions.

### Has single hop data access path

The associated principal can directly access sensitive data resources (such as Amazon S3 buckets or DynamoDB tables) through its existing permissions, without needing intermediate escalation steps.

### Has capability advancing path

The associated principal has a privilege escalation path that advances its overall capabilities beyond what its directly assigned permissions would suggest. This is a general classification for paths that do not match a more specific pattern.
