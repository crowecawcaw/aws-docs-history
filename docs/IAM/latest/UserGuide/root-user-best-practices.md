# Root user best practices for your

AWS account

When you first create an AWS account, you begin with a default set of credentials with
complete access to all AWS resources in your account. This identity is called the [AWS account
root user](id_root-user.md "id_root-user.md"). We strongly recommend you don’t access the AWS account root user unless you have
a [task that requires root user credentials](root-user-tasks.md#root-user-tasks "root-user-tasks.md#root-user-tasks"). You need to secure your root user credentials and
your account recovery mechanisms to help ensure you don’t expose your highly privileged
credentials for unauthorized use.

For multiple AWS accounts managed through AWS Organizations, we recommend removing root user
credentials from member accounts to help prevent unauthorized use. You can remove the root user
password, access keys, signing certificates, and deactivate and delete multi-factor
authentication (MFA). Member accounts can't sign in to their root user or perform password recovery
for their root user. For more information, see [Centrally manage root access for member
accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management").

Instead of accessing the root user, create an administrative user for everyday tasks.

- If you have a new AWS account, see [Setting up your AWS account](getting-started-account-iam.md "getting-started-account-iam.md").
- For multiple AWS accounts managed through AWS Organizations, see [Set
  up AWS account access for an IAM Identity Center administrative user](../../../singlesignon/latest/userguide/get-started-assign-account-access-admin-user.md "../../../singlesignon/latest/userguide/get-started-assign-account-access-admin-user.md").
  With your administrative user, you can then create additional identities for users that need
  access to resources in your AWS account. We strongly recommend you require users to
  authenticate with temporary credentials when accessing AWS.

- For a single, standalone AWS account, use [IAM roles](id_roles.md "id_roles.md") to create identities in your account with specific permissions. Roles
  are intended to be assumable by anyone who needs it. Also, a role does not have standard
  long-term credentials, such as a password or access keys, associated with it. Instead, when
  you assume a role, it provides you with temporary security credentials for your role
  session. Unlike IAM roles, [IAM users](id_users.md "id_users.md") have
  long-term credentials such as passwords and access keys. Where possible, [best
  practices](best-practices-use-cases.md "best-practices-use-cases.md") recommend relying on temporary credentials instead of creating IAM
  users who have long-term credentials such as passwords and access keys.
- For multiple AWS accounts managed through AWS Organizations, use IAM Identity Center workforce users. With
  IAM Identity Center, you can centrally manage users across your AWS accounts and permissions within
  those accounts. Manage your user identities with IAM Identity Center or from an external identity
  provider. For more information, see [What is AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the
  _AWS IAM Identity Center User Guide_.

###### Topics

- [Secure your root user credentials to prevent unauthorized
  use](#ru-bp-secure "#ru-bp-secure")
- [Use a strong root user password to help protect access](#ru-bp-password "#ru-bp-password")
- [Secure your root user sign-in with multi-factor authentication
  (MFA)](#ru-bp-mfa "#ru-bp-mfa")
- [Don't create access keys for the root user](#ru-bp-access "#ru-bp-access")
- [Use multi-person approval for root user sign-in wherever
  possible](#ru-bp-multi "#ru-bp-multi")
- [Use a group email address for root user credentials](#ru-bp-group "#ru-bp-group")
- [Restrict access to account recovery mechanisms](#ru-bp-recovery "#ru-bp-recovery")
- [Secure your AWS Organizations account root user credentials](#ru-bp-organizations "#ru-bp-organizations")
- [Monitor access and usage](#ru-bp-monitor "#ru-bp-monitor")

## Secure your root user credentials to prevent unauthorized

use

Secure your root user credentials and use them for only [the tasks that require them](root-user-tasks.md "root-user-tasks.md"). To help
prevent unauthorized use, don’t share your root user password, MFA, access keys, CloudFront key
pairs, or signing certificates with anyone, except those that have a strict business need to
access the root user.

Don't store the root user password with tools that depend on AWS services in an account
that is accessed using that same password. If you lose or forget your root user password, you
will not be able to access these tools. We recommend that you prioritize resiliency and
consider requiring two or more people to authorize access to the storage location. Access to
the password or its storage location should be logged and monitored.

## Use a strong root user password to help protect access

We recommend that you use a password that is strong and unique. Tools such as password
managers with strong password generation algorithms can help you achieve these goals. AWS
requires that your password meet the following conditions:

- It must have a minimum of 8 characters and a maximum of 128 characters.
- It must include a minimum of three of the following mix of character types: uppercase,
  lowercase, numbers, and ! @ # $ % ^ & \* () <> [] {} | \_+-= symbols.
- It must not be identical to your AWS account name or email address.

For more information, see [Change the password for the AWS account root user](root-user-password.md "root-user-password.md").

## Secure your root user sign-in with multi-factor authentication

(MFA)

Because a root user can perform privileged actions, it's crucial to add MFA for the root user as
a second authentication factor in addition to the email address and password as sign-in
credentials. You can register up to eight MFA devices of any combination of the currently
supported MFA types with your AWS account root user.

We strongly recommend enabling multiple MFA devices for your root user credentials to
provide additional flexibility and resiliency in your security strategy. All AWS account
types (standalone, management, and member accounts) require MFA to be configured for their
root user. Users must register MFA within 35 days of their first sign-in attempt to access the
AWS Management Console if MFA is not already enabled.

- FIDO Certified hardware security keys are provided by third-party providers. For more
  information, see [Enable a FIDO security key for
  the AWS account root user](enable-fido-mfa-for-root.md "enable-fido-mfa-for-root.md").
- A hardware device that generates a six-digit numeric code based on the time-based
  one-time password (TOTP) algorithm. For more information, see [Enable a hardware TOTP token for
  the AWS account root user](enable-hw-mfa-for-root.md "enable-hw-mfa-for-root.md").
- A virtual authenticator application that runs on a phone or other device and emulates
  a physical device. For more information, see [Enable a virtual MFA device for
  your AWS account root user](enable-virt-mfa-for-root.md "enable-virt-mfa-for-root.md").

## Don't create access keys for the root user

Access keys let you run commands in the AWS Command Line Interface (AWS CLI) or use API
operations from one of the AWS SDKs. We strongly recommend that you do not create access key
pairs for your root user because the root user has full access to all AWS services and resources
in the account, including billing information.

Since only a few tasks require the root user and you typically perform those tasks
infrequently, we recommend signing in to the AWS Management Console to perform root user tasks. Before
creating access keys, review the [Alternatives to
long-term access keys](security-creds-programmatic-access.md#security-creds-alternatives-to-long-term-access-keys "security-creds-programmatic-access.md#security-creds-alternatives-to-long-term-access-keys").

## Use multi-person approval for root user sign-in wherever

possible

Consider using multi-person approval to ensure that no one person can access both MFA and
password for the root user. Some companies add an additional layer of security by setting up one
group of administrators with access to the password, and another group of administrators with
access to MFA. One member from each group must come together to sign in as the root user.

## Use a group email address for root user credentials

Use an email address that is managed by your business and forwards received messages
directly to a group of users. If AWS must contact the owner of the account, this approach
reduces the risk of delays in responding, even if individuals are on vacation, out sick, or
have left the business. The email address used for the root user should not be used for other
purposes.

## Restrict access to account recovery mechanisms

Ensure you develop a process to manage root user credential recovery mechanisms in case you
need access to it during emergency such as takeover of your administrative account.

- Ensure you have access to your root user email inbox so that you can [reset a lost or
  forgotten root user password](reset-root-password.md "reset-root-password.md").
- If MFA for your AWS account root user is lost, damaged, or not working, you can sign in
  using another MFA registered to the same root user credentials. If you lost access to all
  your MFAs, you need both the phone number and the email used to register your account, to
  be up to date and accessible to recover your MFA. For details, see [Recovering a root user MFA device](id_credentials_mfa_lost-or-broken.md#root-mfa-lost-or-broken "id_credentials_mfa_lost-or-broken.md#root-mfa-lost-or-broken").
- If you choose not to store your root user password and MFA, then the phone number
  registered in your account can be used as an alternate way to recover root user credentials.
  Ensure you have access to the contact phone number, keep the phone number updated, and
  limit who has access to manage the phone number.

No one person should have access to both the email inbox and phone number since both are
verification channels to recover your root user password. It is important to have two groups of
individuals managing these channels. One group having access to your primary email address and
another group having access to the primary phone number to recover access to your account as
root user.

## Secure your AWS Organizations account root user credentials

As you move to a multi-account strategy with AWS Organizations, each of your AWS accounts has its
own root user credentials that you need to secure. The account you use to create your
organization is the **management account** and the rest of the
accounts in your organization are **member accounts**.

### Secure root user credentials for the management

account

AWS requires that you register MFA for the root user of your organization's management
account. MFA registration must be completed during the first sign-in attempt or within the
35-day grace period. If MFA is not enabled within this time, registration will be required
before you can access the AWS Management Console. For more information, see [Multi-factor authentication for AWS account root user](enable-mfa-for-root.md "enable-mfa-for-root.md").

### Secure root user credentials for member accounts

If you use AWS Organizations to manage multiple accounts, there are two strategies that you can
take to secure root user access in your AWS Organizations.

- Centralize root access and remove root user credentials from member accounts. Remove
  the root user credentials, access keys, signing certificates, and deactivate and delete
  multi-factor authentication (MFA). When this strategy is used, member accounts can't
  sign in to their root user or perform password recovery for their root user. For more
  information, see [Centrally manage root access for member
  accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management").
- Secure root user credentials of your AWS Organizations accounts with MFA to enhance account
  security. For more information, see [Multi-factor authentication for AWS account root user](enable-mfa-for-root.md "enable-mfa-for-root.md").

For details, see [Accessing member
accounts in your organization](../../../organizations/latest/userguide/orgs_manage_accounts_access.md "../../../organizations/latest/userguide/orgs_manage_accounts_access.md") in the _AWS Organizations User
Guide_.

### Set preventative security controls in AWS Organizations using a service

control policy (SCP)

If the member accounts in your organization have root user credentials enabled, you can
apply an SCP to restrict access to member account root user. Denying all root user actions in your
member accounts, except for certain root-only actions, helps prevent unauthorized access.
For details, see [Use an SCP to restrict what the root user in your member accounts can do](../../../organizations/latest/userguide/best-practices_member-acct.md#bp_member-acct_use-scp "../../../organizations/latest/userguide/best-practices_member-acct.md#bp_member-acct_use-scp").

## Monitor access and usage

We recommend you use your current tracking mechanisms to monitor, alert, and report the
sign in and use of root user credentials, including alerts that announce root user sign-in and
usage. The following services can help to ensure that root user credential usage is tracked and
perform security checks that can help prevent unauthorized use.

###### Note

CloudTrail logs different sign-in events for the root user and privileged root user sessions. These
privileged sessions allow tasks that require root user credentials to be performed in member
accounts in your organization. You can use the sign-in event to identify the actions taken
by the management account or a delegated administrator using [`sts:AssumeRoot`](../../../STS/latest/APIReference/API_AssumeRoot.md "../../../STS/latest/APIReference/API_AssumeRoot.md"). For
more information, see [Track privileged tasks in
CloudTrail](cloudtrail-track-privileged-tasks.md "cloudtrail-track-privileged-tasks.md").

- If you want to be notified about root user sign-in activity in your account, you can
  leverage Amazon CloudWatch to create an Events rule that detects when root user credentials are used
  and triggers a notification to your security administrator. For details, see [Monitor and
  notify on AWS account root user activity](https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity/ "https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity/").
- If you want to set up notifications to alert you of approved root user actions, you can
  leverage Amazon EventBridge along with Amazon SNS to write an EventBridge rule to track root user usage for the
  specific action and notify you using an Amazon SNS topic. For an example, see [Send a
  notification when an Amazon S3 object is created](../../../eventbridge/latest/userguide/eb-s3-object-created-tutorial.md "../../../eventbridge/latest/userguide/eb-s3-object-created-tutorial.md").
- If you already using GuardDuty as your threat detection service, you can [extend its capability](../../../guardduty/latest/ug/guardduty_finding-types-iam.md#policy-iam-rootcredentialusage "../../../guardduty/latest/ug/guardduty_finding-types-iam.md#policy-iam-rootcredentialusage") to notify you when root user credentials are being used in
  your account.

Alerts should include, but not be limited to, the email address for the root user. Have
procedures in place for how to respond to alerts so that personnel who receive a root user access
alert understand how to validate that root user access is expected, and how to escalate if they
believe that a security incident is in progress. For an example of how to configure alerts,
see [Monitor
and notify on AWS account root user activity](https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity/ "https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity/").

### Evaluate root user MFA compliance

The following services can help evaluate MFA compliance for root user credentials.

###### MFA-related rules return noncompliant if you follow the best practice of removing

root user credentials.

We recommend removing root user credentials from member accounts in your organization to
help prevent unauthorized use. After you remove root user credentials, including MFA, these
member accounts are evaluated as **not applicable**.

- AWS Config provides rules to monitor compliance with root user best practices. You can use
  AWS Config managed rules to help you [enforce MFA for
  root user credentials](../../../config/latest/developerguide/root-account-mfa-enabled.md "../../../config/latest/developerguide/root-account-mfa-enabled.md"). AWS Config can also [identify access keys
  for the root user](../../../config/latest/developerguide/iam-root-access-key-check.md "../../../config/latest/developerguide/iam-root-access-key-check.md").
- Security Hub provides you with a comprehensive view of your security state in AWS and
  helps you assess your AWS environment against security industry standards and best
  practices, such as having MFA on the root user and not having root user access keys. For
  details on the rules available, see [AWS Identity and Access Management controls](../../../securityhub/latest/userguide/iam-controls.md#iam-4 "../../../securityhub/latest/userguide/iam-controls.md#iam-4")
  in the _Security Hub User Guide_.
- Trusted Advisor provides a security check so you know if MFA isn't enabled on the root user
  account. For more information, see [MFA on Root
  Account](../../../awssupport/latest/user/security-checks.md#mfa-root-account "../../../awssupport/latest/user/security-checks.md#mfa-root-account") in the _AWS Support User Guide_.

If you need to report a security issue on your account, see [Report Suspicious Emails](https://aws.amazon.com/security/report-suspicious-emails/ "https://aws.amazon.com/security/report-suspicious-emails/") or [Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/ "https://aws.amazon.com/security/vulnerability-reporting/").
Alternatively, you can [Contact AWS](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") for
assistance and additional guidance.
