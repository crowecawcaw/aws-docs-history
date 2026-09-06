

# Security Hub CSPM controls for AWS Identity and Access Management
<a name="iam-controls"></a>

These AWS Security Hub CSPM controls evaluate the AWS Identity and Access Management (IAM) service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [IAM.1] IAM policies should not allow full "\*" administrative privileges
<a name="iam-1"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/1.22, CIS AWS Foundations Benchmark v1.4.0/1.16, NIST.800-53.r5 AC-2, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-6(10), NIST.800-53.r5 AC-6(2), NIST.800-53.r5 AC-6(3), NIST.800-171.r2 3.1.4, PCI DSS v3.2.1/7.2.1

**Category:** Protect > Secure access management

**Severity:** High

**Resource type:** `AWS::IAM::Policy`

**AWS Config rule:** [`iam-policy-no-statements-with-admin-access`](https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-no-statements-with-admin-access.html)

**Schedule type:** Change triggered

**Parameters:**
+ `excludePermissionBoundaryPolicy: true` (not customizable)

This control checks whether the default version of IAM policies (also known as customer managed policies) has administrator access by including a statement with `"Effect": "Allow"` with `"Action": "*"` over `"Resource": "*"`. The control fails if you have IAM policies with such a statement.

The control only checks the customer managed policies that you create. It does not check inline and AWS managed policies.

IAM policies define a set of privileges that are granted to users, groups, or roles. Following standard security advice, AWS recommends that you grant least privilege, which means to grant only the permissions that are required to perform a task. When you provide full administrative privileges instead of the minimum set of permissions that the user needs, you expose the resources to potentially unwanted actions.

Instead of allowing full administrative privileges, determine what users need to do and then craft policies that let the users perform only those tasks. It is more secure to start with a minimum set of permissions and grant additional permissions as necessary. Do not start with permissions that are too lenient and then try to tighten them later.

You should remove IAM policies that have a statement with `"Effect": "Allow" `with `"Action": "*"` over `"Resource": "*"`.

**Note**  
AWS Config should be enabled in all Regions in which you use Security Hub CSPM. However, global resource recording can be enabled in a single Region. If you only record global resources in a single Region, then you can disable this control in all Regions except the Region where you record global resources.

### Remediation
<a name="iam-1-remediation"></a>

To modify your IAM policies so that they do not allow full "\*" administrative privileges, see [Editing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html) in the *IAM User Guide*.

## [IAM.2] IAM users should not have IAM policies attached
<a name="iam-2"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.14, CIS AWS Foundations Benchmark v3.0.0/1.15, CIS AWS Foundations Benchmark v1.2.0/1.16, NIST.800-53.r5 AC-2, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-6(3), NIST.800-171.r2 3.1.1, NIST.800-171.r2 3.1.2, NIST.800-171.r2 3.1.7, NIST.800-171.r2 3.3.9, NIST.800-171.r2 3.13.3, PCI DSS v3.2.1/7.2.1

**Category:** Protect > Secure access management

**Severity:** Low

**Resource type:** `AWS::IAM::User`

**AWS Config rule:** [`iam-user-no-policies-check`](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-no-policies-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether your IAM users have policies attached. The control fails if your IAM users have policies attached. Instead, IAM users must inherit permissions from IAM groups or assume a role.

By default, IAM users, groups, and roles have no access to AWS resources. IAM policies grant privileges to users, groups, or roles. We recommend that you apply IAM policies directly to groups and roles but not to users. Assigning privileges at the group or role level reduces the complexity of access management as the number of users grows. Reducing access management complexity might in turn reduce the opportunity for a principal to inadvertently receive or retain excessive privileges. 

**Note**  
AWS Config should be enabled in all Regions in which you use Security Hub CSPM. However, global resource recording can be enabled in a single Region. If you only record global resources in a single Region, you can disable this control in all Regions except the Region where you record global resources.

### Remediation
<a name="iam-2-remediation"></a>

To resolve this issue, [create an IAM group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html), and attach the policy to the group. Then, [add the users to the group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_add-remove-users.html). The policy is applied to each user in the group. To remove a policy attached directly to a user, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

## [IAM.3] IAM users' access keys should be rotated every 90 days or less
<a name="iam-3"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.13, CIS AWS Foundations Benchmark v3.0.0/1.14, CIS AWS Foundations Benchmark v1.4.0/1.14, CIS AWS Foundations Benchmark v1.2.0/1.4, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-2(3), NIST.800-53.r5 AC-3(15), PCI DSS v4.0.1/8.3.9, PCI DSS v4.0.1/8.6.3

**Category:** Protect > Secure access management

**Severity:** Medium 

**Resource type:** `AWS::IAM::User`

**AWS Config rule:** [`access-keys-rotated`](https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html)

**Schedule type:** Periodic

**Parameters:**
+ `maxAccessKeyAge`: `90` (not customizable)

This control checks whether the active access keys are rotated within 90 days.

We highly recommend that you do not generate and remove all access keys in your account. Instead, the recommended best practice is to either create one or more IAM roles or to use [federation](https://aws.amazon.com/identity/federation/) through AWS IAM Identity Center. You can use these methods to allow your users to access the AWS Management Console and AWS CLI.

Each approach has its use cases. Federation is generally better for enterprises that have an existing central directory or plan to need more than the current limit on IAM users. Applications that run outside of an AWS environment need access keys for programmatic access to AWS resources.

However, if the resources that need programmatic access run inside AWS, the best practice is to use IAM roles. Roles allow you to grant a resource access without hardcoding an access key ID and secret access key into the configuration.

To learn more about protecting your access keys and account, see [Best practices for managing AWS access keys](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html) in the *AWS General Reference*. Also see the blog post [Guidelines for protecting your AWS account while using programmatic access](https://aws.amazon.com/blogs/security/guidelines-for-protecting-your-aws-account-while-using-programmatic-access/).

If you already have an access key, Security Hub CSPM recommends that you rotate the access keys every 90 days. Rotating access keys reduces the chance that an access key that is associated with a compromised or terminated account is used. It also ensures that data cannot be accessed with an old key that might have been lost, cracked, or stolen. Always update your applications after you rotate access keys. 

Access keys consist of an access key ID and a secret access key. They are used to sign programmatic requests that you make to AWS. Users need their own access keys to make programmatic calls to AWS from the AWS CLI, Tools for Windows PowerShell, the AWS SDKs, or direct HTTP calls using the API operations for individual AWS services.

If your organization uses AWS IAM Identity Center (IAM Identity Center), your users can sign in to Active Directory, a built-in IAM Identity Center directory, or [another identity provider (IdP) connected to IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html). They can then be mapped to an IAM role that enables them to run AWS CLI commands or call AWS API operations without the need for access keys. To learn more, see [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*.

**Note**  
AWS Config should be enabled in all Regions in which you use Security Hub CSPM. However, global resource recording can be enabled in a single Region. If you only record global resources in a single Region, then you can disable this control in all Regions except the Region where you record global resources.

### Remediation
<a name="iam-3-remediation"></a>

To rotate access keys that are older than 90 days, see [Rotating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the *IAM User Guide*. Follow the instructions for any user with an **Access key age** greater than 90 days.

## [IAM.4] IAM root user access key should not exist
<a name="iam-4"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.3, CIS AWS Foundations Benchmark v3.0.0/1.4, CIS AWS Foundations Benchmark v1.4.0/1.4, CIS AWS Foundations Benchmark v1.2.0/1.12, PCI DSS v3.2.1/2.1, PCI DSS v3.2.1/2.2, PCI DSS v3.2.1/7.2.1, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-6(10), NIST.800-53.r5 AC-6(2)

**Category:** Protect > Secure access management

**Severity:** Critical 

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-root-access-key-check`](https://docs.aws.amazon.com/config/latest/developerguide/iam-root-access-key-check.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether the root user access key is present. 

The root user is the most privileged user in an AWS account. AWS access keys provide programmatic access to a given account.

Security Hub CSPM recommends that you remove all access keys that are associated with the root user. This limits that vectors that can be used to compromise your account. It also encourages the creation and use of role-based accounts that are least privileged. 

### Remediation
<a name="iam-4-remediation"></a>

To delete the root user access key, see [Deleting access keys for the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_delete-key) in the *IAM User Guide*. To delete the root user access keys from an AWS account in AWS GovCloud (US), see [Deleting my AWS GovCloud (US) account root user access keys](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-account-root-user.html#delete-govcloud-root-access-key) in the *AWS GovCloud (US) User Guide*.

## [IAM.5] MFA should be enabled for all IAM users that have a console password
<a name="iam-5"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.9, CIS AWS Foundations Benchmark v3.0.0/1.10, CIS AWS Foundations Benchmark v1.4.0/1.10, CIS AWS Foundations Benchmark v1.2.0/1.2, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), NIST.800-53.r5 IA-2(1), NIST.800-53.r5 IA-2(2), NIST.800-53.r5 IA-2(6), NIST.800-53.r5 IA-2(8), PCI DSS v4.0.1/8.4.2

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:** `AWS::IAM::User`

**AWS Config rule:** [`mfa-enabled-for-iam-console-access`](https://docs.aws.amazon.com/config/latest/developerguide/mfa-enabled-for-iam-console-access.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether AWS multi-factor authentication (MFA) is enabled for all IAM users that use a console password.

Multi-factor authentication (MFA) adds an extra layer of protection on top of a user name and password. With MFA enabled, when a user signs in to an AWS website, they are prompted for their user name and password. In addition, they are prompted for an authentication code from their AWS MFA device.

We recommend that you enable MFA for all accounts that have a console password. MFA is designed to provide increased security for console access. The authenticating principal must possess a device that emits a time-sensitive key and must have knowledge of a credential.

**Note**  
AWS Config should be enabled in all Regions in which you use Security Hub CSPM. However, global resource recording can be enabled in a single Region. If you only record global resources in a single Region, then you can disable this control in all Regions except the Region where you record global resources.

### Remediation
<a name="iam-5-remediation"></a>

To add MFA for IAM users, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) in the *IAM User Guide*.

## [IAM.6] Hardware MFA should be enabled for the root user
<a name="iam-6"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.5, CIS AWS Foundations Benchmark v3.0.0/1.6, CIS AWS Foundations Benchmark v1.4.0/1.6, CIS AWS Foundations Benchmark v1.2.0/1.14, PCI DSS v3.2.1/8.3.1, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), NIST.800-53.r5 IA-2(1), NIST.800-53.r5 IA-2(2), NIST.800-53.r5 IA-2(6), NIST.800-53.r5 IA-2(8), PCI DSS v4.0.1/8.4.2

**Category:** Protect > Secure access management

**Severity:** Critical

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`root-account-hardware-mfa-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/root-account-hardware-mfa-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether your AWS account is enabled to use a hardware multi-factor authentication (MFA) device to sign in with root user credentials. The control fails if hardware MFA isn't enabled or virtual MFA devices are permitted for signing in with root user credentials.

Virtual MFA might not provide the same level of security as hardware MFA devices. We recommend that you use a virtual MFA device only while you wait for hardware purchase approval or for your hardware to arrive. To learn more, see [ Assign a virtual MFA device (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html) in the *IAM User Guide*.

**Note**  
Security Hub CSPM evaluates this control based on the presence of root user credentials (login profile) in an AWS account. The control generates `PASSED` findings in the following cases:  
Root user credentials are present in the account and hardware MFA is enabled for the root user.
Root user credentials aren’t present in the account.
The control generates a `FAILED` finding if root user credentials are present in the account and hardware MFA is not enabled for the root user.

### Remediation
<a name="iam-6-remediation"></a>

For information about enabling hardware MFA for the root user, see [Multi-factor authentication for an AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html) in the *IAM User Guide*.

## [IAM.7] Password policies for IAM users should have strong configurations
<a name="iam-7"></a>

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-2(3), NIST.800-53.r5 AC-3(15), NIST.800-53.r5 IA-5(1), NIST.800-171.r2 3.5.2, NIST.800-171.r2 3.5.7, NIST.800-171.r2 3.5.8, PCI DSS v4.0.1/8.3.6, PCI DSS v4.0.1/8.3.7, PCI DSS v4.0.1/8.3.9, PCI DSS v4.0.1/8.3.10.1, PCI DSS v4.0.1/8.6.3

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `RequireUppercaseCharacters` | Require at least one uppercase character in password | Boolean | `true` or `false` | `true` | 
| `RequireLowercaseCharacters` | Require at least one lowercase character in password | Boolean | `true` or `false` | `true` | 
| `RequireSymbols` | Require at least one symbol in password | Boolean | `true` or `false` | `true` | 
| `RequireNumbers` | Require at least one number in password | Boolean | `true` or `false` | `true` | 
| `MinimumPasswordLength` | Minimum number of characters in the password | Integer | `8` to `128` | `8` | 
| `PasswordReusePrevention` | Number of password rotations before an old password can be reused | Integer | `12` to `24` | No default value | 
| `MaxPasswordAge` | Number of days before password expiration | Integer | `1` to `90` | No default value | 

This control checks whether the account password policy for IAM users uses strong configurations. The control fails if the password policy doesn't use strong configurations. Unless you provide custom parameter values, Security Hub CSPM uses the default values mentioned in the preceding table. The `PasswordReusePrevention` and `MaxPasswordAge` parameters have no default value, so if you exclude these parameters, Security Hub CSPM ignores number of password rotations and password age when evaluating this control.

To access the AWS Management Console, IAM users need passwords. As a best practice, Security Hub CSPM highly recommends that instead of creating IAM users, you use federation. Federation allows users to use their existing corporate credentials to log into the AWS Management Console. Use AWS IAM Identity Center (IAM Identity Center) to create or federate the user, and then assume an IAM role into an account.

To learn more about identity providers and federation, see [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) in the *IAM User Guide*. To learn more about IAM Identity Center, see the [*AWS IAM Identity Center User Guide*](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

 If you need to use IAM users, Security Hub CSPM recommends that you enforce the creation of strong user passwords. You can set a password policy on your AWS account to specify complexity requirements and mandatory rotation periods for passwords. When you create or change a password policy, most of the password policy settings are enforced the next time users change their passwords. Some of the settings are enforced immediately.

### Remediation
<a name="iam-7-remediation"></a>

To update your password policy, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *IAM User Guide*.

## [IAM.8] Unused IAM user credentials should be removed
<a name="iam-8"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/1.3, NIST.800-53.r5 AC-2, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-2(3), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6, NIST.800-171.r2 3.1.2, PCI DSS v3.2.1/8.1.4, PCI DSS v4.0.1/8.2.6

**Category:** Protect > Secure access management 

**Severity:** Medium 

**Resource type:** `AWS::IAM::User`

**AWS Config rule:** [`iam-user-unused-credentials-check`](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-unused-credentials-check.html)

**Schedule type:** Periodic

**Parameters:**
+ `maxCredentialUsageAge`: `90` (not customizable)

This control checks whether your IAM users have passwords or active access keys that have not been used for 90 days.

IAM users can access AWS resources using different types of credentials, such as passwords or access keys. 

Security Hub CSPM recommends that you remove or deactivate all credentials that were unused for 90 days or more. Disabling or removing unnecessary credentials reduces the window of opportunity for credentials associated with a compromised or abandoned account to be used.

**Note**  
AWS Config should be enabled in all Regions in which you use Security Hub CSPM. However, global resource recording can be enabled in a single Region. If you only record global resources in a single Region, then you can disable this control in all Regions except the Region where you record global resources.

### Remediation
<a name="iam-8-remediation"></a>

When you view user information in the IAM console, there are columns for **Access key age**, **Password age**, and **Last activity**. If the value in any of these columns is greater than 90 days, make the credentials for those users inactive.

You can also use [credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html#getting-credential-reports-console) to monitor users and identify those with no activity for 90 or more days. You can download credential reports in `.csv` format from the IAM console.

After you identify the inactive accounts or unused credentials, deactivate them. For instructions, see [Creating, changing, or deleting an IAM user password (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html#id_credentials_passwords_admin-change-user_console) in the *IAM User Guide*.

## [IAM.9] MFA should be enabled for the root user
<a name="iam-9"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.4, PCI DSS v3.2.1/8.3.1, PCI DSS v4.0.1/8.4.2, CIS AWS Foundations Benchmark v3.0.0/1.5, CIS AWS Foundations Benchmark v1.4.0/1.5, CIS AWS Foundations Benchmark v1.2.0/1.13, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), NIST.800-53.r5 IA-2(1), NIST.800-53.r5 IA-2(2), NIST.800-53.r5 IA-2(6), NIST.800-53.r5 IA-2(8)

**Category:** Protect > Secure access management 

**Severity:** Critical

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`root-account-mfa-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/root-account-mfa-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether multi-factor authentication (MFA) is enabled for the IAM root user of an AWS account to sign in to the AWS Management Console. The control fails if MFA isn't enabled for the root user of the account.

The IAM root user of an AWS account has complete access to all the services and resources in the account. If MFA is enabled, the user must enter a username, a password, and an authentication code from their AWS MFA device in order to sign in to the AWS Management Console. MFA adds an extra layer of protection on top of a username and password.

This control generates `PASSED` findings in the following cases:
+ Root user credentials are present in the account and MFA is enabled for the root user.
+ Root user credentials aren’t present in the account.

The control generates `FAILED` findings if root user credentials are present in the account and MFA isn’t enabled for the root user.

### Remediation
<a name="iam-9-remediation"></a>

For information about enabling MFA for the root user of an AWS account, see [Multi-factor authentication for the AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html) in the *AWS Identity and Access Management User Guide*.

## [IAM.10] Password policies for IAM users should have strong configurations
<a name="iam-10"></a>

**Related requirements:** NIST.800-171.r2 3.5.2, NIST.800-171.r2 3.5.7, NIST.800-171.r2 3.5.8, PCI DSS v3.2.1/8.1.4, PCI DSS v3.2.1/8.2.3, PCI DSS v3.2.1/8.2.4, PCI DSS v3.2.1/8.2.5

**Category:** Protect > Secure access management 

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether the account password policy for IAM users uses the following minimum PCI DSS configurations.
+ `RequireUppercaseCharacters` – Require at least one uppercase character in password. (Default = `true`)
+ `RequireLowercaseCharacters` – Require at least one lowercase character in password. (Default = `true`)
+ `RequireNumbers` – Require at least one number in password. (Default = `true`)
+ `MinimumPasswordLength` – Password minimum length. (Default = 7 or longer)
+ `PasswordReusePrevention` – Number of passwords before allowing reuse. (Default = 4)
+ `MaxPasswordAge` – Number of days before password expiration. (Default = 90)

**Note**  
On May 30, 2025, Security Hub CSPM removed this control from the PCI DSS v4.0.1 standard. PCI DSS v4.0.1 now requires passwords to have a minimum of 8 characters. This control continues to apply to the PCI DSS v3.2.1 standard, which has different password requirements.  
To evaluate account password policies against PCI DSS v4.0.1 requirements, you can use the [IAM.7 control](#iam-7). This control requires passwords to have a minimum of 8 characters. It also supports custom values for password length and other parameters. The IAM.7 control is part of the PCI DSS v4.0.1 standard in Security Hub CSPM.

### Remediation
<a name="iam-10-remediation"></a>

To update your password policy to use the recommended configuration, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *IAM User Guide*.

## [IAM.11] Ensure IAM password policy requires at least one uppercase letter
<a name="iam-11"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/1.5, NIST.800-171.r2 3.5.7, PCI DSS v4.0.1/8.3.6, PCI DSS v4.0.1/8.6.3

**Category:** Protect > Secure access management 

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)

**Schedule type:** Periodic

**Parameters:** None

Password policies, in part, enforce password complexity requirements. Use IAM password policies to ensure that passwords use different character sets.

CIS recommends that the password policy require at least one uppercase letter. Setting a password complexity policy increases account resiliency against brute force login attempts.

### Remediation
<a name="iam-11-remediation"></a>

To change your password policy, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *IAM User Guide*. For **Password strength**, select **Require at least one uppercase letter from the Latin alphabet (A–Z)**.

## [IAM.12] Ensure IAM password policy requires at least one lowercase letter
<a name="iam-12"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/1.6, NIST.800-171.r2 3.5.7, PCI DSS v4.0.1/8.3.6, PCI DSS v4.0.1/8.6.3

**Category:** Protect > Secure access management 

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)

**Schedule type:** Periodic

**Parameters:** None

Password policies, in part, enforce password complexity requirements. Use IAM password policies to ensure that passwords use different character sets. CIS recommends that the password policy require at least one lowercase letter. Setting a password complexity policy increases account resiliency against brute force login attempts.

### Remediation
<a name="iam-12-remediation"></a>

To change your password policy, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *IAM User Guide*. For **Password strength**, select **Require at least one lowercase letter from the Latin alphabet (A–Z)**.

## [IAM.13] Ensure IAM password policy requires at least one symbol
<a name="iam-13"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/1.7, NIST.800-171.r2 3.5.7

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)

**Schedule type:** Periodic

**Parameters:** None

Password policies, in part, enforce password complexity requirements. Use IAM password policies to ensure that passwords use different character sets.

CIS recommends that the password policy require at least one symbol. Setting a password complexity policy increases account resiliency against brute force login attempts.

### Remediation
<a name="iam-13-remediation"></a>

To change your password policy, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *IAM User Guide*. For **Password strength**, select **Require at least one nonalphanumeric character**.

## [IAM.14] Ensure IAM password policy requires at least one number
<a name="iam-14"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/1.8, NIST.800-171.r2 3.5.7, PCI DSS v4.0.1/8.3.6, PCI DSS v4.0.1/8.6.3

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)

**Schedule type:** Periodic

**Parameters:** None

Password policies, in part, enforce password complexity requirements. Use IAM password policies to ensure that passwords use different character sets.

CIS recommends that the password policy require at least one number. Setting a password complexity policy increases account resiliency against brute force login attempts.

### Remediation
<a name="iam-14-remediation"></a>

To change your password policy, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *IAM User Guide*. For **Password strength**, select **Require at least one number**.

## [IAM.15] Ensure IAM password policy requires minimum password length of 14 or greater
<a name="iam-15"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.7, CIS AWS Foundations Benchmark v3.0.0/1.8, CIS AWS Foundations Benchmark v1.4.0/1.8, CIS AWS Foundations Benchmark v1.2.0/1.9, NIST.800-171.r2 3.5.7

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)

**Schedule type:** Periodic

**Parameters:** None

Password policies, in part, enforce password complexity requirements. Use IAM password policies to ensure that passwords are at least a given length.

CIS recommends that the password policy require a minimum password length of 14 characters. Setting a password complexity policy increases account resiliency against brute force login attempts.

### Remediation
<a name="iam-15-remediation"></a>

To change your password policy, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *IAM User Guide*. For **Password minimum length**, enter **14** or a larger number.

## [IAM.16] Ensure IAM password policy prevents password reuse
<a name="iam-16"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.8, CIS AWS Foundations Benchmark v3.0.0/1.9, CIS AWS Foundations Benchmark v1.4.0/1.9, CIS AWS Foundations Benchmark v1.2.0/1.10, NIST.800-171.r2 3.5.8, PCI DSS v4.0.1/8.3.7

**Category:** Protect > Secure access management

**Severity:** Low

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether the number of passwords to remember is set to 24. The control fails if the value is not 24.

IAM password policies can prevent the reuse of a given password by the same user.

CIS recommends that the password policy prevent the reuse of passwords. Preventing password reuse increases account resiliency against brute force login attempts.

### Remediation
<a name="iam-16-remediation"></a>

To change your password policy, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *IAM User Guide*. For **Prevent password reuse**, enter **24**.

## [IAM.17] Ensure IAM password policy expires passwords within 90 days or less
<a name="iam-17"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/1.11, PCI DSS v4.0.1/8.3.9, PCI DSS v4.0.1/8.3.10.1

**Category:** Protect > Secure access management

**Severity:** Low

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-password-policy`](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)

**Schedule type:** Periodic

**Parameters:** None

IAM password policies can require passwords to be rotated or expired after a given number of days.

CIS recommends that the password policy expire passwords after 90 days or less. Reducing the password lifetime increases account resiliency against brute force login attempts. Requiring regular password changes also helps in the following scenarios:
+ Passwords can be stolen or compromised without your knowledge. This can happen via a system compromise, software vulnerability, or internal threat.
+ Certain corporate and government web filters or proxy servers can intercept and record traffic even if it's encrypted.
+ Many people use the same password for many systems such as work, email, and personal.
+ Compromised end-user workstations might have a keystroke logger.

### Remediation
<a name="iam-17-remediation"></a>

To change your password policy, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *IAM User Guide*. For **Turn on password expiration**, enter **90** or a smaller number.

## [IAM.18] Ensure a support role has been created to manage incidents with AWS Support
<a name="iam-18"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.16, CIS AWS Foundations Benchmark v3.0.0/1.17, CIS AWS Foundations Benchmark v1.4.0/1.17, CIS AWS Foundations Benchmark v1.2.0/1.20, NIST.800-171.r2 3.1.2, PCI DSS v4.0.1/12.10.3

**Category:** Protect > Secure access management

**Severity:** Low

**Resource type:** `AWS::::Account`

**AWS Config rule:** [`iam-policy-in-use`](https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-in-use.html)

**Schedule type:** Periodic

**Parameters:**
+ `policyARN`: `arn:{{partition}}:iam::aws:policy/AWSSupportAccess` (not customizable)
+ `policyUsageType`: `ANY` (not customizable)

AWS provides a support center that can be used for incident notification and response, as well as technical support and customer services.

Create an IAM role to allow authorized users to manage incidents with AWS Support. By implementing least privilege for access control, an IAM role will require an appropriate IAM policy to allow support center access in order to manage incidents with Support.

**Note**  
AWS Config should be enabled in all Regions in which you use Security Hub CSPM. However, global resource recording can be enabled in a single Region. If you only record global resources in a single Region, then you can disable this control in all Regions except the Region where you record global resources.

### Remediation
<a name="iam-18-remediation"></a>

To remediate this issue, create a role to allow authorized users to manage Support incidents.

**To create the role to use for Support access**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the IAM navigation pane, choose **Roles**, then choose **Create role**.

1. For **Role type**, choose the **Another AWS account**.

1. For **Account ID**, enter the AWS account ID of the AWS account to which you want to grant access to your resources.

   If the users or groups that will assume this role are in the same account, then enter the local account number.
**Note**  
The administrator of the specified account can grant permission to assume this role to any user in that account. To do this, the administrator attaches a policy to the user or a group that grants permission for the `sts:AssumeRole` action. In that policy, the resource must be the role ARN.

1. Choose **Next: Permissions**.

1. Search for the managed policy `AWSSupportAccess`.

1. Select the check box for the `AWSSupportAccess` managed policy.

1. Choose **Next: Tags**.

1. (Optional) To add metadata to the role, attach tags as key-value pairs.

   For more information about using tags in IAM, see [Tagging IAM users and roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

1. Choose **Next: Review**.

1. For **Role name**, enter a name for your role.

   Role names must be unique within your AWS account. They are not case sensitive.

1. (Optional) For **Role description**, enter a description for the new role.

1. Review the role, then choose **Create role**.

## [IAM.19] MFA should be enabled for all IAM users
<a name="iam-19"></a>

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), NIST.800-53.r5 IA-2(1), NIST.800-53.r5 IA-2(2), NIST.800-53.r5 IA-2(6), NIST.800-53.r5 IA-2(8), NIST.800-171.r2 3.3.8, NIST.800-171.r2 3.5.3, NIST.800-171.r2 3.5.4, NIST.800-171.r2 3.7.5, PCI DSS v3.2.1/8.3.1, PCI DSS v4.0.1/8.4.2, 

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:** `AWS::IAM::User`

**AWS Config rule:** [`iam-user-mfa-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-mfa-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether the IAM users have multi-factor authentication (MFA) enabled.

**Note**  
AWS Config should be enabled in all Regions in which you use Security Hub CSPM. However, global resource recording can be enabled in a single Region. If you only record global resources in a single Region, then you can disable this control in all Regions except the Region where you record global resources.

### Remediation
<a name="iam-19-remediation"></a>

To add MFA for IAM users, see [Enabling MFA devices for users in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable.html) in the *IAM User Guide*.

## [IAM.20] Avoid the use of the root user
<a name="iam-20"></a>

**Important**  
Security Hub CSPM retired this control in April 2024. For more information, see [Change log for Security Hub CSPM controls](controls-change-log.md).

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/1.1

**Category:** Protect > Secure access management

**Severity:** Low

**Resource type:** `AWS::IAM::User`

**AWS Config rule:** `use-of-root-account-test` (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an AWS account has restrictions on the usage of the root user. The control evaluates the following resources:
+ Amazon Simple Notification Service (Amazon SNS) topics
+ AWS CloudTrail trails
+ Metric filters associated with the CloudTrail trails
+ Amazon CloudWatch alarms based on the filters

This check results in a `FAILED` finding if one or more of the following statements is true:
+ No CloudTrail trails exist in the account.
+ A CloudTrail trail is enabled, but not configured with at-least one multi-Region trail that includes read and write management events.
+ A CloudTrail trail is enabled, but not associated with a CloudWatch Logs log group.
+ The exact metric filter prescribed by the Center for Internet Security (CIS) is not used. The prescribed metric filter is `'{$.userIdentity.type="Root" && $.userIdentity.invokedBy NOT EXISTS && $.eventType !="AwsServiceEvent"}'`.
+ No CloudWatch alarms based on the metric filter exist in the account.
+ CloudWatch alarms configured to send notification to the associated SNS topic don't trigger based on the alarm condition.
+ The SNS topic doesn't comply with the [constraints for sending a message to an SNS topic](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html).
+ The SNS topic doesn't have at least one subscriber.

This check results in a control status of `NO_DATA` if one or more of the following statements is true:
+ A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
+ A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.

This check results in a control status of `WARNING` if one or more of the following statements is true:
+ The current account doesn't own the SNS topic referenced in the CloudWatch alarm.
+ The current account doesn't have access to the SNS topic when invoking the `ListSubscriptionsByTopic` SNS API.

**Note**  
We recommend using organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of NO\_DATA for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.

As a best practice, use your root user credentials only when required to [ perform account and service management tasks](https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html). Apply IAM policies directly to groups and roles but not to users. For instructions on setting up an administrator for daily use, see [ Creating your first IAM admin user and group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*.

### Remediation
<a name="iam-20-remediation"></a>

The steps to remediate this issue include setting up an Amazon SNS topic, a CloudTrail trail, a metric filter, and an alarm for the metric filter.

**To create an Amazon SNS topic**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. Create an Amazon SNS topic that receives all CIS alarms.

   Create at least one subscriber to the topic. For more information, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*.

Next, set up an active CloudTrail that applies to all Regions. To do so, follow the remediation steps in [[CloudTrail.1] CloudTrail should be enabled and configured with at least one multi-Region trail that includes read and write management events](cloudtrail-controls.md#cloudtrail-1).

Make a note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group.

Finally, create the metric filter and alarm.

**To create a metric filter and alarm**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Log groups**.

1. Select the check box for the CloudWatch Logs log group that is associated with the CloudTrail trail that you created.

1. From **Actions**, choose **Create Metric Filter**.

1. Under **Define pattern**, do the following:

   1. Copy the following pattern and then paste it into the **Filter Pattern** field.

      ```
      {$.userIdentity.type="Root" && $.userIdentity.invokedBy NOT EXISTS && $.eventType !="AwsServiceEvent"}
      ```

   1. Choose **Next**.

1. Under **Assign Metric**, do the following:

   1. In **Filter name**, enter a name for your metric filter.

   1. For **Metric Namespace**, enter **LogMetrics**.

      If you use the same namespace for all of your CIS log metric filters, then all CIS Benchmark metrics are grouped together.

   1. For **Metric Name**, enter a name for the metric. Remember the name of the metric. You will need to select the metric when you create the alarm.

   1. For **Metric value**, enter **1**.

   1. Choose **Next**.

1. Under **Review and create**, verify the information that you provided for the new metric filter. Then, choose **Create metric filter**.

1. In the navigation pane, choose **Log groups**, and then choose the filter you created under **Metric filters**.

1. Select the check box for the filter. Choose **Create alarm**.

1. Under **Specify metric and conditions**, do the following:

   1. Under **Conditions**, for **Threshold**, choose **Static**.

   1. For **Define the alarm condition**, choose **Greater/Equal**.

   1. For **Define the threshold value**, enter **1**.

   1. Choose **Next**.

1. Under **Configure actions**, do the following:

   1. Under **Alarm state trigger**, choose **In alarm**.

   1. Under **Select an SNS topic**, choose **Select an existing SNS topic**.

   1. For **Send a notification to**, enter the name of the SNS topic that you created in the previous procedure.

   1. Choose **Next**.

1. Under **Add name and description**, enter a **Name** and **Description** for the alarm, such as **CIS-1.1-RootAccountUsage**. Then choose **Next**.

1. Under **Preview and create**, review the alarm configuration. Then choose **Create alarm**.

## [IAM.21] IAM customer managed policies that you create should not allow wildcard actions for services
<a name="iam-21"></a>

**Related requirements:** NIST.800-53.r5 AC-2, NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-6(10), NIST.800-53.r5 AC-6(2), NIST.800-53.r5 AC-6(3), NIST.800-171.r2 3.1.1, NIST.800-171.r2 3.1.2, NIST.800-171.r2 3.1.5, NIST.800-171.r2 3.1.7, NIST.800-171.r2 3.3.8, NIST.800-171.r2 3.3.9, NIST.800-171.r2 3.13.3, NIST.800-171.r2 3.13.4

**Category:** Detect > Secure access management 

**Severity:** Low

**Resource type:** `AWS::IAM::Policy`

**AWS Config rule:** [`iam-policy-no-statements-with-full-access`](https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-no-statements-with-full-access.html)

**Schedule type:** Change triggered

**Parameters:**
+ `excludePermissionBoundaryPolicy`: `True` (not customizable)

This control checks whether the IAM identity-based policies that you create have Allow statements that use the \* wildcard to grant permissions for all actions on any service. The control fails if any policy statement includes `"Effect": "Allow"` with `"Action": "Service:*"`. 

For example, the following statement in a policy results in a failed finding.

```
"Statement": [
{
  "Sid": "EC2-Wildcard",
  "Effect": "Allow",
  "Action": "ec2:*",
  "Resource": "*"
}
```

The control also fails if you use `"Effect": "Allow"` with `"NotAction": "{{service}}:*"`. In that case, the `NotAction` element provides access to all of the actions in an AWS service, except for the actions specified in `NotAction`.

This control only applies to customer managed IAM policies. It does not apply to IAM policies that are managed by AWS.

When you assign permissions to AWS services, it is important to scope the allowed IAM actions in your IAM policies. You should restrict IAM actions to only those actions that are needed. This helps you to provision least privilege permissions. Overly permissive policies might lead to privilege escalation if the policies are attached to an IAM principal that might not require the permission.

In some cases, you might want to allow IAM actions that have a similar prefix, such as `DescribeFlowLogs` and `DescribeAvailabilityZones`. In these authorized cases, you can add a suffixed wildcard to the common prefix. For example, `ec2:Describe*`.

This control passes if you use a prefixed IAM action with a suffixed wildcard. For example, the following statement in a policy results in a passed finding.

```
"Statement": [
{
  "Sid": "EC2-Wildcard",
  "Effect": "Allow",
  "Action": "ec2:Describe*",
  "Resource": "*"
}
```

When you group related IAM actions in this way, you can also avoid exceeding the IAM policy size limits.

**Note**  
AWS Config should be enabled in all Regions in which you use Security Hub CSPM. However, global resource recording can be enabled in a single Region. If you only record global resources in a single Region, then you can disable this control in all Regions except the Region where you record global resources.

### Remediation
<a name="iam-21-remediation"></a>

To remediate this issue, update your IAM policies so that they do not allow full "\*" administrative privileges. For details about how to edit an IAM policy, see [Editing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html) in the *IAM User Guide*.

## [IAM.22] IAM user credentials unused for 45 days should be removed
<a name="iam-22"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.11, CIS AWS Foundations Benchmark v3.0.0/1.12, CIS AWS Foundations Benchmark v1.4.0/1.12, NIST.800-171.r2 3.1.2

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:** `AWS::IAM::User`

**AWS Config rule: **[`iam-user-unused-credentials-check`](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-unused-credentials-check.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether your IAM users have passwords or active access keys that have not been used for 45 days or more. To do so, it checks whether the `maxCredentialUsageAge` parameter of the AWS Config rule is equal to 45 or more.

Users can access AWS resources using different types of credentials, such as passwords or access keys.

CIS recommends that you remove or deactivate all credentials that have been unused for 45 days or more. Disabling or removing unnecessary credentials reduces the window of opportunity for credentials associated with a compromised or abandoned account to be used.

The AWS Config rule for this control uses the [`GetCredentialReport`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetCredentialReport.html) and [`GenerateCredentialReport`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateCredentialReport.html) API operations, which are only updated every four hours. Changes to IAM users can take up to four hours to be visible to this control.

**Note**  
AWS Config should be enabled in all Regions in which you use Security Hub CSPM. However, you can enable recording of global resources in a single Region. If you only record global resources in a single Region, then you can disable this control in all Regions except the Region where you record global resources.

### Remediation
<a name="iam-22-remediation"></a>

When you view user information in the IAM console, there are columns for **Access key age**, **Password age**, and **Last activity**. If the value in any of these columns is greater than 45 days, make the credentials for those users inactive.

You can also use [credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html#getting-credential-reports-console) to monitor users and identify those with no activity for 45 or more days. You can download credential reports in `.csv` format from the IAM console.

After you identify the inactive accounts or unused credentials, deactivate them. For instructions, see [Creating, changing, or deleting an IAM user password (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html#id_credentials_passwords_admin-change-user_console) in the *IAM User Guide*.

## [IAM.23] IAM Access Analyzer analyzers should be tagged
<a name="iam-23"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::AccessAnalyzer::Analyzer`

**AWS Config rule: ** `tagged-accessanalyzer-analyzer` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an analyzer managed by AWS Identity and Access Management Access Analyzer (IAM Access Analyzer) has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the analyzer doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the analyzer isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="iam-23-remediation"></a>

To add tags to an analyzer, see [TagResource](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_TagResource.html) in the *AWS IAM Access Analyzer API Reference*.

## [IAM.24] IAM roles should be tagged
<a name="iam-24"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::IAM::Role`

**AWS Config rule: ** `tagged-iam-role` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an AWS Identity and Access Management (IAM) role has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the role doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the role isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="iam-24-remediation"></a>

To add tags to an IAM role, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

## [IAM.25] IAM users should be tagged
<a name="iam-25"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::IAM::User`

**AWS Config rule: ** `tagged-iam-user` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an AWS Identity and Access Management (IAM) user has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the user doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the user isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="iam-25-remediation"></a>

To add tags to an IAM user, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

## [IAM.26] Expired SSL/TLS certificates managed in IAM should be removed
<a name="iam-26"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.18, CIS AWS Foundations Benchmark v3.0.0/1.19

**Category:** Identify > Compliance

**Severity:** Medium

**Resource type:** `AWS::IAM::ServerCertificate`

**AWS Config rule: **[`iam-server-certificate-expiration-check`](https://docs.aws.amazon.com/config/latest/developerguide/iam-server-certificate-expiration-check.html)

**Schedule type:** Periodic

**Parameters:** None

This controls checks whether an active SSL/TLS server certificate that is managed in IAM has expired. The control fails if the expired SSL/TLS server certificate isn't removed.

To enable HTTPS connections to your website or application in AWS, you need an SSL/TLS server certificate. You can use IAM or AWS Certificate Manager (ACM) to store and deploy server certificates. Use IAM as a certificate manager only when you must support HTTPS connections in an AWS Region that isn't supported by ACM. IAM securely encrypts your private keys and stores the encrypted version in IAM SSL certificate storage. IAM supports deploying server certificates in all Regions, but you must obtain your certificate from an external provider for use with AWS. You can't upload an ACM certificate to IAM. Additionally, you can't manage your certificates from the IAM console. Removing expired SSL/TLS certificates eliminates the risk that an invalid certificate is deployed accidentally to a resource, which can damage the credibility of the underlying application or website.

### Remediation
<a name="iam-26-remediation"></a>

To remove a server certificate from IAM, see [Managing server certificates in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html) in the *IAM User Guide*.

## [IAM.27] IAM identities should not have the AWSCloudShellFullAccess policy attached
<a name="iam-27"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.21, CIS AWS Foundations Benchmark v3.0.0/1.22

**Category:** Protect > Secure access management > Secure IAM policies

**Severity:** Medium

**Resource type:** `AWS::IAM::Role`, `AWS::IAM::User`, `AWS::IAM::Group`

**AWS Config rule: **[`iam-policy-blacklisted-check`](https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-blacklisted-check.html)

**Schedule type:** Change triggered

**Parameters:**
+ "policyArns": "arn:aws:iam::aws:policy/AWSCloudShellFullAccess,arn:aws-cn:iam::aws:policy/AWSCloudShellFullAccess, arn:aws-us-gov:iam::aws:policy/AWSCloudShellFullAccess"

This control checks whether an IAM identity (user, role, or group) has the AWS managed policy `AWSCloudShellFullAccess` attached. The control fails if an IAM identity has the `AWSCloudShellFullAccess` policy attached.

AWS CloudShell provides a convenient way to run CLI commands against AWS services. The AWS managed policy `AWSCloudShellFullAccess` provides full access to CloudShell, which allows file upload and download capability between a user's local system and the CloudShell environment. Within the CloudShell environment, a user has sudo permissions, and can access the internet. As a result, atttaching this managed policy to an IAM identity gives them the ability to install file transfer software and move data from CloudShell to external internet servers. We recommend following the principle of least privilege and attaching narrower permissions to your IAM identities.

### Remediation
<a name="iam-27-remediation"></a>

To detach the `AWSCloudShellFullAccess` policy from an IAM identity, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

## [IAM.28] IAM Access Analyzer external access analyzer should be enabled
<a name="iam-28"></a>

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/1.19, CIS AWS Foundations Benchmark v3.0.0/1.20

**Category:** Detect > Detection services > Privileged usage monitoring

**Severity:** High

**Resource type:** `AWS::AccessAnalyzer::Analyzer`

**AWS Config rule: **[`iam-external-access-analyzer-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/iam-external-access-analyzer-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an AWS account has an IAM Access Analyzer external access analyzer enabled. The control fails if the account doesn't have an external access analyzer enabled in your currently selected AWS Region.

IAM Access Analyzer external access analyzers help identify resources, such as Amazon Simple Storage Service (Amazon S3) buckets or IAM roles, that are shared with an external entity. This helps you avoid unintended access to your resources and data. IAM Access Analyzer is Regional and must be enabled in each Region. To identify resources that are shared with external principals, an access analyzer uses logic-based reasoning to analyze resource-based policies in your AWS environment. When you create an external access analyzer, you can create and enable it for your entire organization or individual accounts.

**Note**  
If an account is part of an organization in AWS Organizations, this control doesn't factor external access analyzers that specify the organization as the zone of trust and are enabled for the organization in the current Region. If your organization uses this type of configuration, consider disabling this control for individual member accounts in your organization in the Region.

### Remediation
<a name="iam-28-remediation"></a>

For information about enabling an external access analyzer in a specific Region, see [Getting started with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html) in the *IAM User Guide*. You must enable an analyzer in each Region in which you want to monitor access to your resources.