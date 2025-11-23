# Remediating exposures for IAM users

AWS Security Hub can generate exposure findings for AWS Identity and Access Management (IAM) users.

On the Security Hub console, the IAM user involved in an exposure finding and its identifying information are listed in
the **Resources** section of the finding details. Programmatically, you can retrieve resource
details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub API.

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
using temporary credentials instead of creating individual IAM users. If that's an option for your organization and
use case, we recommend switching to roles or federation instead of using IAM users. For more information, see
[IAM users](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") in the _IAM User Guide_.

###### Contents

- [Misconfiguration traits for
  IAM users](exposure-iam-user.md#iam-user-misconfiguration "exposure-iam-user.md#iam-user-misconfiguration")
  - [The IAM user has a policy with administrative access](exposure-iam-user.md#administrative-access-policy "exposure-iam-user.md#administrative-access-policy")
  - [The IAM user does not have MFA enabled](exposure-iam-user.md#user-mfa-disabled "exposure-iam-user.md#user-mfa-disabled")
  - [The IAM user has a policy with administrative access to an AWS service](exposure-iam-user.md#service-admin-policy "exposure-iam-user.md#service-admin-policy")
  - [The AWS account for the IAM user has weak password policies](exposure-iam-user.md#weak-password-policies "exposure-iam-user.md#weak-password-policies")
  - [The IAM user has unused credentials](exposure-iam-user.md#unused-credentials "exposure-iam-user.md#unused-credentials")
  - [The IAM user has unrotated access keys](exposure-iam-user.md#unrotated-access-keys "exposure-iam-user.md#unrotated-access-keys")
  - [The IAM user has a policy that allows unrestricted access to KMS key decryption](exposure-iam-user.md#unrestricted-kms-decryption-allowed "exposure-iam-user.md#unrestricted-kms-decryption-allowed")

## Misconfiguration traits for

IAM users

Here are misconfiguration traits for IAM users and suggested remediation steps.

### The IAM user has a policy with administrative access

IAM policies grant a set of privileges to IAM users when accessing resources.
Administrative policies provide IAM users with broad permissions to AWS services and resources.
Providing full administrative privileges, instead of the minimum set of permissions that the user needs, can increase the scope of an attack if credentials are compromised.
Following standard security principles, AWS recommends that you grant least privileges, which means that you grant only the permissions required to perform a task.

1. **Review and identify administrative policies** –
   In the **Resource ID**, identify the IAM role name.
   Go to the IAM dashboard and select the identified role.
   Review the permissions policy attached to the IAM user.
   If the policy is an AWS managed policy, look for `AdministratorAccess` or `IAMFullAccess`.
   Otherwise, in the policy document, look for statements that have the statements `"Effect":` `"Allow"` with `"Action": "*"` over `"Resource": "*"`.
2. **Implement least privilege access** –
   Replace service administrative policies with those that grant only the specific permissions required for the user to function.
   For more information on security best practices for IAM policies, see [Apply least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _AWS Identity and Access Management User Guide_.
   To identify unnecessary permissions, you can use the IAM Access Analyzer to understand how to modify your policy based on access history.
   For more information, see [Findings for external and unused access](../../../IAM/latest/UserGuide/access-analyzer-findings.md "../../../IAM/latest/UserGuide/access-analyzer-findings.md") in the _AWS Identity and Access Management User Guide_.
3. **Secure configuration considerations** –
   If service administrative permissions are necessary for the instance, consider implementing these additional security controls to mitigate risk:
   - **Multi-factor authentication (MFA)** –
     MFA adds an additional security layer by requiring an additional form of authentication.
     This helps prevent unauthorized access even if credentials are compromised.
     For more information, see [Require multi-factor authentication (MFA)](../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users "../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users") in the _AWS Identity and Access Management User Guide_.
   - **IAM conditions** –
     Setting up condition elements allow you to restrict when and how administrative permissions can be used based on factors like source IP or MFA age.
     For more information, see [Use conditions in IAM policies](../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions "../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions") to further restrict access in the _AWS Identity and Access Management User Guide_.
   - **Permission boundaries** –
     Permission boundaries establish the maximum permissions a role can have, providing guardrails for roles with administrative access.
     For more information, see [Use permissions boundaries to delegate permissions management within an account](../../../IAM/latest/UserGuide/best-practices.md#bp-permissions-boundaries "../../../IAM/latest/UserGuide/best-practices.md#bp-permissions-boundaries") in the _AWS Identity and Access Management User Guide_.

### The IAM user does not have MFA enabled

Multi-factor authentication (MFA) adds an extra layer of protection on top of a user name and password.
When MFA is enabled and an IAM user signs in to an AWS website, they are prompted for their user name, password, and an authentication code from their AWS MFA device.
The authenticating principal must possess a device that emits a time-sensitive key and must have knowledge of a credential.
Without MFA, if a user’s password is compromised, an attacker gains full access to the user’s AWS permissions.
Following standard security principles, AWS recommends enabling MFA for all accounts and users that have AWS Management Console access.

###### Review MFA types

AWS supports the following [MFA types](../../../IAM/latest/UserGuide/id_credentials_mfa.md#id_credentials_mfa-types "../../../IAM/latest/UserGuide/id_credentials_mfa.md#id_credentials_mfa-types"):

- Passkeys and security keys
- Virtual authenticator applications
- Hardware TOTP tokens

Although authentication with a physical device typically provides more stringent security protection, using any type of MFA is more secure than having MFA disabled.

###### Enable MFA

To enable the MFA type that suits your requirements, see [AWS multi-factor authentication in IAM](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the _IAM User Guide_.
Follow the steps for the specific MFA type you want to implement. For organizations managing many users, you may want to enforce MFA usage by requiring MFA to access sensitive resources.

### The IAM user has a policy with administrative access to an AWS service

Service admin policies provide IAM users with permissions to perform all actions within a specific AWS service.
These policies typically include permissions that are not required for users to perform their job functions.
Providing an IAM user with service administrator privileges, instead of the minimum set of permissions needed, increases the scope of an attack if credentials are compromised.
Following standard security principles, AWS recommends that you grant least privileges, which means that you grant only the permissions required to perform a task.

###### Review and identify service admin policies

In the **Resource ID**, identify the IAM role name.
Go to the IAM dashboard and select the identified role.
Review the permissions policy attached to the IAM user.
If the policy is an AWS managed policy, look for `AdministratorAccess` or `IAMFullAccess`.
Otherwise, in the policy document, look for statements that have the statements "`Effect": "Allow" with "Action": "*" over "Resource": "*"`.

###### Implement least privilege access

Replace service administrative policies with those that grant only the specific permissions required for the user to function.

To identify unnecessary permissions, you can use the IAM Access Analyzer to understand how to modify your policy based on access history.

###### Secure configuration considerations

If service administrative permissions are necessary for the instance, consider implementing these additional security controls to mitigate exposure:

- MFA adds an additional security layer by requiring an additional form of authentication.
  This helps prevent unauthorized access even if credentials are compromised.
- Use condition elements to restrict when and how administrative permissions can be used based on factors like source IP or MFA age.
- Use permission boundaries to establish the maximum permissions a role can have, providing guardrails for roles with administrative access.

### The AWS account for the IAM user has weak password policies

Password policies help protect against unauthorized access by enforcing minimum complexity requirements for IAM user passwords.
Without strong password policies, there’s an increased risk that user accounts could be compromised through password guessing or brute force attacks.
Following standard security principles, AWS recommends implementing a strong password policy to ensure users create complex passwords that are difficult to guess.

###### Configure a strong password policy

Go to the IAM dashboard and navigate to Account settings.
Review the current password policy settings for your account, including minimum length, character types required, and password expiration settings.

At a minimum, AWS recommends following these best practices when setting your password policy:

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

### The IAM user has unused credentials

Unused credentials, including passwords and access keys that have remained inactive for 90 days or more pose a security risk to your AWS environment.
These unused credentials create potential attack vectors for attackers and increase your organization’s overall attack surface.
Following security best practices, AWS recommends deactivating or removing credentials that haven’t been used in 90 days or more to reduce your attack surface.

###### Deactivate or remove unused credentials

In the exposure finding, open the resource.
This will open the user details window.
Before taking action on unused credentials, assess the potential impact on your environment.
Removing credentials without proper assessment could disrupt background processes, scheduled jobs, and more.
Consider a brief deactivation period before permanent removal to verify the impact of removing the unused credentials.

Take the appropriate action based on the credential type:

- For unused console passwords, consider first changing the password and temporarily deactivating it.
  If no issues arise, proceed with permanent deactivation or deletion.
- For unused access keys, consider first deactivating the key.
  After confirming no systems are affected, proceed with permanent deactivation or deletion.
- For unused users, consider temporarily deactivating the user by attaching a restrictive policy before full deletion.

### The IAM user has unrotated access keys

Access keys consist of an access key ID and a secret access key that enable programmatic access to AWS resources.
When access keys remain unchanged for extended periods of time, they increase the risk of unauthorized access if they are compromised.
Following security best practices, AWS recommends rotating access keys every 90 days to minimize the window of opportunity for attackers to use compromised credentials.

###### Rotate access keys

In the exposure finding, open the resource.
This will open the user details window.
To rotate access keys, see [Manage access keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey") in the _IAM User Guide_.

### The IAM user has a policy that allows unrestricted access to KMS key decryption

AWS KMS enables you to create and manage cryptographic keys that are used to protect your data.
IAM policies that allow unrestricted AWS KMS decryption permissions (e.g., `kms:Decrypt` or `kms:ReEncryptFrom`) on all KMS keys can lead to unauthorized data access if an IAM user’s credentials are compromised.
If an attacker gains access to these credentials, they could potentially decrypt any encrypted data in your environment, which could include sensitive data.
Following security best practices, AWS recommends implementing least privilege by limiting AWS KMS decryption permissions to only specific keys that users need for their job functions.

###### Implement least-privilege access

In the exposure finding, open the resource.
This will open the IAM Policy window.
Look for permissions in KMS that allow kms:Decrypt or `kms:ReEncryptFrom` or `KMS:*` with a resource specification of `"*"`.
Update the policy to restrict AWS KMS decryption permissions to only the specific keys needed.
Modify the policy to replace the `"*"` resource with the specific ARNs of required AWS KMS keys.

###### Secure configuration considerations

Consider adding conditions to further restrict when these permissions can be used.
For example, you can limit decryption operations to specific VPC endpoints or source IP ranges.

You can also configure key policies to further restrict who can use specific KMS keys.
