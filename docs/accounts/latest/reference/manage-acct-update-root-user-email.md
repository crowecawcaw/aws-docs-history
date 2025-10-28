# Update the root user

email address

There are various business reasons why you might need to update the root user email address of
your AWS account. For example, security and administrative resilience. This topic walks
you through the process of updating your root user email
address for both
standalone and member accounts.

###### Note

Changes to an AWS account can take up to four hours to propagate everywhere.

You can update the root user
email differently, depending on
whether or not the accounts are standalone, or part of an organization:

- **Standalone AWS accounts** – For
  AWS accounts not associated with an organization, you can update the root user email
  using the AWS Management Console. To learn how to do this, see [Update the root user
  email for a standalone
  AWS account](#root-user-email-standalone "#root-user-email-standalone").
- **AWS accounts within an organization** –
  For member accounts that are part of an AWS organization, a user in the management
  account or delegated admin account can centrally update the root user email of the
  member account from the AWS Organizations console, or programmatically via the AWS CLI
  & SDKs. To learn how to do this, see [Update
  the root user email for any AWS account in your organization](#root-user-email-orgs "#root-user-email-orgs").

###### Topics

- [Update the root user
  email for a standalone
  AWS account](#root-user-email-standalone "#root-user-email-standalone")
- [Update the root user
  email for any
  AWS account in your organization](#root-user-email-orgs "#root-user-email-orgs")

## Update the root user

email for a standalone
AWS account

To edit the root user email address for a standalone AWS account, perform the steps
in the following procedure.

AWS Management Console

###### Note

You must sign in as the AWS account root user, which requires no additional
IAM permissions. You can't perform these steps as an IAM user or
role.

1. Use your AWS account's email address and password to sign in to
   the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as your AWS account root user.
2. In the upper right corner of the console, choose your account name
   or number and then choose **Account**.
3. On the [**Account** page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account"), next to
   **Account details**, choose
   **Actions** and then select **Update
   email address and password**.
4. On the **Account Details** page, next to
   **Email address** choose
   **Edit**.
5. On the **Edit Account Email** page, fill out the
   fields for **New email address**, **Confirm
   new email address**, and confirm your current
   **Password**. Then, choose **Save and
   continue**. A verification code is sent to your new
   email address from `no-reply@verify.signin.aws`.
6. On the **Edit Account Email** page, under
   **Verification code**, enter the code you
   received from your email, and then choose **Confirm
   updates**.

###### Note

It can take up to 5 minutes for the verification code to
arrive. If you don’t see the email in your inbox, check your
spam and junk folders.

AWS CLI & SDKsThis task isn't supported in the AWS CLI or by an API operation from
one of the AWS SDKs. You can perform this task only by using the AWS Management Console.

## Update the root user

email for any
AWS account in your organization

To edit the root user email address for any member account in your organization using
the AWS Organizations console, perform the steps in the following procedure.

###### Note

Before you update the root user email address for a member account, we recommend
that you understand the impact of this operation. For more information, see [Updating the root user email address for a member account with AWS Organizations](../../../organizations/latest/userguide/orgs_manage_accounts_update_primary_email.md "../../../organizations/latest/userguide/orgs_manage_accounts_update_primary_email.md")
in the _AWS Organizations User Guide_.

You can also update the root user email address for a member account directly from the
[**Account**
page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account") in the AWS Management Console after signing in as the root user. For step-by-step
instructions, follow the steps provided in [Update the root user
email for a standalone
AWS account](#root-user-email-standalone "#root-user-email-standalone").

AWS Management Console

###### Notes

- To perform this procedure from the management account or a
  delegated admin account in an organization against member
  accounts, you must [enable trusted access for the Account Management
  service](../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account "../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account").
- You can't use this procedure to access an account in a
  different organization from the one you're using to call the
  operation.

###### To update the root user email

address for a member account using the AWS Organizations
console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, or
   sign in as the root user ([not recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management
   account.
2. On the **AWS accounts** page, choose the member
   account for which you want to update the root user email address.
3. In the **Account details** section, choose the
   **Actions** button, and then choose
   **Update email address**.
4. Under **Email**, enter the new
   email address for the root user, and then choose
   **Save**. This sends a one-time password (OTP)
   to the new email address.

###### Note

If you need to close this page in the Organizations console
while you wait for the code, you can return and finish the OTP
process within 24 hours from when the code was sent. To do this,
while on the **Account details** page, choose
the **Actions** button, and then choose
**Complete email update**. 5. Under **Verification code**, enter
the code that was sent to the new email address in the previous
step, and then choose **Confirm**. This commits the
update to the root user for the account.

AWS CLI & SDKs
You can retrieve, or update the **_root user_** email address
(also referred to as the primary email address) by using the following AWS CLI
commands or their AWS SDK equivalent operations:

- [GetPrimaryEmail](API_GetPrimaryEmail.md "API_GetPrimaryEmail.md")
- [StartPrimaryEmailUpdate](API_StartPrimaryEmailUpdate.md "API_StartPrimaryEmailUpdate.md")
- [AcceptPrimaryEmailUpdate](API_AcceptPrimaryEmailUpdate.md "API_AcceptPrimaryEmailUpdate.md")

###### Notes

- To perform these operations from the management account or a
  delegated admin account in an organization against member
  accounts, you must [enable trusted access for the Account Management
  service](../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account "../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account").
- You can't access an account in a different organization from
  the one you're using to call the operation.

###### Minimum permissions

For each operation, you must have the permission that maps to that
operation:

- `account:GetPrimaryEmail`
- `account:StartPrimaryEmailUpdate`
- `account:AcceptPrimaryEmailUpdate`
  If you use these individual permissions, you can grant some users the
  ability to only read the root user email
  address information, and grant others the ability to both
  read and write.

To complete the root user email address process, you must use the
primary email APIs together in the order they are shown in the examples
below.

###### Example `GetPrimaryEmail`

The following example retrieves the root user email
address from the specified member account in an
organization. The credentials used must be from either the
organization's management account, or from the Account Management's
delegated admin account.

```
`$` `aws account get-primary-email --account-id 123456789012`
```

###### Example `StartPrimaryEmailUpdate`

The following example starts the root user email
address update process, identifies the new email address,
and sends a one-time password (OTP) to the new email address for the
specified member account in an organization. The credentials used must
be from either the organization's management account, or from the
Account Management's delegated admin account.

```
`$` `aws account start-primary-email-update --account-id 123456789012 --primary-email john@examplecorp.com`
```

###### Example `AcceptPrimaryEmailUpdate`

The following example accepts the OTP code and sets the new email
address to the specified member account in an organization. The
credentials used must be from either the organization's management
account, or from the Account Management's delegated admin
account.

```
`$` `aws account accept-primary-email-update --account-id 123456789012 --otp 12345678 --primary-email john@examplecorp.com`
```
