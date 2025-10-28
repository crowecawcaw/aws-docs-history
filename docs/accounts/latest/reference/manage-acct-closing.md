# Close an AWS account

If you no longer need your AWS account, you can close it at any time by following the
instructions in this section. After you've closed it, you can reopen it within 90 days from
the day you closed the account. The timespan between the day you closed the account and when AWS
permanently closes the account is referred to as the [post-closure period](#post-closure-period "#post-closure-period").

## What you need to know before closing your

account

Before closing your AWS account, you should consider the following:

- Closing your account will serve as your notice of termination of the AWS
  Customer Agreement for this account.
- You don't need to delete resources in your AWS account before closing
  it. However, we recommend you back up any resources or data that you want to
  keep. For instructions about how to back up a particular resource, see the
  appropriate [AWS
  documentation](../../../index.md "../../../index.md") for that service.
- You can reopen your account during the [post-closure period](#post-closure-period "#post-closure-period"). Charges for the services that remained in
  your account will restart if you reopen it. You also remain responsible for
  any unpaid invoices and outstanding [Reserved Instances](../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#Instance_Reservations "../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#Instance_Reservations") and [Savings Plans](../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#cb_savingsplans "../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#cb_savingsplans").
- You remain responsible for all outstanding fees and charges for the
  services consumed before account closure. You will receive an AWS bill the
  following month after closing your account. For example, if you closed your
  account on January 15, you will receive a bill at the beginning of February
  for usage incurred from January 1 through January 15. You will continue
  receiving invoices for [Reserved Instances](../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#Instance_Reservations "../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#Instance_Reservations") and [Savings Plans](../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#cb_savingsplans "../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#cb_savingsplans") after closing your account until they
  expire.
- You will no longer be able to access AWS services that were previously
  available in your account. However, you can sign-in and access a closed
  AWS account during the [post-closure
  period](#post-closure-period "#post-closure-period") only to view past billing information, access account
  settings, or contact [AWS Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home").
- You can't use the same email address that was registered to your
  AWS account at the time of its closure as the primary email of another
  AWS account. If you want to use the same email address for a different
  AWS account, we recommend updating it before closure. For more information, see [Update the root user
  email address](manage-acct-update-root-user-email.md "manage-acct-update-root-user-email.md").
- If you've [enabled multi-factor authentication (MFA)](../../../IAM/latest/UserGuide/id_credentials_mfa_enable-overview.md "../../../IAM/latest/UserGuide/id_credentials_mfa_enable-overview.md") on your AWS account
  root user, or configured an [MFA device on an
  IAM user](../../../IAM/latest/UserGuide/console_sign-in-mfa.md "../../../IAM/latest/UserGuide/console_sign-in-mfa.md"), MFA isn't removed automatically when you close the
  account. If you choose to leave MFA turned on during the 90 days [post-closure period](#post-closure-period "#post-closure-period"), keep the MFA
  device active until the post-closure period has expired in case you need to
  access the account during that time. Note, the hardware TOTP token devices
  cannot be associated with another user after the permanent closure of your
  account. If you would like to use the hardware TOTP token with another user
  later, you have the option to [deactivate
  the hardware MFA device](../../../IAM/latest/UserGuide/id_credentials_mfa_disable.md "../../../IAM/latest/UserGuide/id_credentials_mfa_disable.md") before closing the account. MFA devices
  for [IAM users](../../../IAM/latest/UserGuide/id_users_manage.md#id_users_deleting "../../../IAM/latest/UserGuide/id_users_manage.md#id_users_deleting") must be deleted by the account
  administrator.

**Additional considerations for member
accounts**

- When you close a member account, that account isn't removed from the
  organization until after the [post-closure period](#post-closure-period "#post-closure-period"). During the post-closure period, a closed
  member account still counts toward your quota of accounts in the
  organization. To avoid having the account count against the quota, see
  [Remove a member account from your organization](../../../organizations/latest/userguide/orgs_manage_accounts_remove-member-account.md "../../../organizations/latest/userguide/orgs_manage_accounts_remove-member-account.md") before closing
  it.
- You can only close 10% of member accounts within a rolling 30 day period.
  This quota is not bound by a calendar month, but starts when you close an
  account. Within 30 days of that initial account closure, you can't exceed
  the 10% account closure limit. The minimum account closure is 10 and the
  maximum account closure is 1000, even if 10% of accounts exceeds 1000. For
  more information about Organizations quotas, see [Quotas
  for AWS Organizations](../../../organizations/latest/userguide/orgs_reference_limits.md "../../../organizations/latest/userguide/orgs_reference_limits.md").
- If you use AWS Control Tower, you need to unmanage the member account
  before you attempt to close the account. See [Unmanage a
  member account](../../../controltower/latest/userguide/unmanage-account.md "../../../controltower/latest/userguide/unmanage-account.md") in the _AWS Control Tower User
  Guide_.

**Service specific considerations**

- AWS Marketplace subscriptions aren't automatically canceled on account closure. If
  you have any subscriptions, first [terminate all instances of your software](../../../marketplace/latest/buyerguide/buyer-getting-started.md#step-6-terminate-your-instance "../../../marketplace/latest/buyerguide/buyer-getting-started.md#step-6-terminate-your-instance") in the subscriptions.
  Then, go to the **[Manage subscriptions](https://aws.amazon.com/marketplace/library "https://aws.amazon.com/marketplace/library")** page of the AWS Marketplace console
  and cancel your subscriptions.
- After an account has been closed, AWS will send daily emails for up to
  five days before we suspend the domain. After the domain has been suspended,
  and depending on the domain’s registrar, we will either delete the domain
  within 30 days or release the domain to its registrar. For more information,
  see [My AWS account is closed or permanently closed, and my domain is
  registered with Route 53](../../../Route53/latest/DeveloperGuide/troubleshooting-account-closed.md "../../../Route53/latest/DeveloperGuide/troubleshooting-account-closed.md").
- AWS CloudTrail is a foundational security service. This means that trails
  created by users can continue to exist and deliver events even after an
  AWS account is closed, unless a user explicitly deletes the trails in
  their AWS account before closing it. For more information about how to
  request trail deletion after an AWS account has been closed, see [AWS account closure and trails](../../../awscloudtrail/latest/userguide/cloudtrail-account-closure.md "../../../awscloudtrail/latest/userguide/cloudtrail-account-closure.md") in the _CloudTrail User
  Guide_.

[Show moreShow less](# "#")

## How to close your account

You can close your AWS account using the following procedure. Note, that there is
different guidance provided in each tab depending on the type of account [standalone,
member, management, and AWS GovCloud (US)] you want to close.

If you experience any issues during the process of closing your account, see [Troubleshooting issues with AWS account
closure](troubleshooting_close-account.md "troubleshooting_close-account.md").

Standalone account
A standalone account is an individually managed account that is not part
of AWS Organizations.

###### To close a standalone account from the Accounts page

1. [Sign in to the AWS Management Console as the root user](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md") in the
   AWS account that you want to close. You can't close an account
   while signed in as an IAM user or role.
2. On the navigation bar in the upper-right corner, choose your
   account name or number, and then choose
   **Account**.
3. On the [**Account** page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account"), choose the
   **Close account** button.
4. Type your account ID (displayed at the top of the closure dialog
   box) to confirm that you have read and understand the account
   closure process.
5. Choose the **Close account** button to initiate
   the account closure process.
6. Within a few minutes, you should receive an email confirmation
   that your account has been closed.

###### Note

This task isn't supported in the AWS CLI or by an API operation from
one of the AWS SDKs. You can perform this task only by using the AWS Management Console.

Member account
A member account is an AWS account that is part of AWS Organizations.

###### To close a member account from the AWS Organizations console

1. Sign in to the [AWS Organizations
   console](https://console.aws.amazon.com/organizations "https://console.aws.amazon.com/organizations").
2. On the **AWS accounts** page, find and choose
   the name of the member account you want to close. You can navigate
   the OU hierarchy, or look at a flat list of accounts without the OU
   structure.
3. Choose **Close** next to the account name at the
   top of the page. This option is only available when an AWS
   organization is in [All features](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#feature-set "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#feature-set") mode.

###### Note

If your organization is using [Consolidated billing](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#feature-set-cb-only "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#feature-set-cb-only") mode, you won't be able to see
the **Close** button in the console. To close
an account in consolidated billing mode, sign in to the account
you want to close as the root user. On the
**Accounts** page, choose the
**Close account** button, enter your
account ID, and then choose the **Close
account** button. 4. Read and ensure that you understand the account closure
guidance. 5. Enter the member account ID, and then choose **Close
account** to initiate the account closure
process.

###### Note

Any member account that you close will display a
`CLOSED` label next to its account name in the
AWS Organizations console for up to 90 days after the original closure date.
After 90 days, the member account will no longer be displayed in the
AWS Organizations console.

**To close a member account from the Accounts
page**

Optionally, you can close an AWS member account directly from the [**Account**
page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account") in the AWS Management Console. For step-by-step guidance, follow the
instructions in the **Standalone account** tab.

**To close a member account using AWS CLI and
SDKs**

For instructions on how to close a member account using the AWS CLI and
SDKs, see [Closing a member account in your organization](../../../organizations/latest/userguide/orgs_manage_accounts_close.md "../../../organizations/latest/userguide/orgs_manage_accounts_close.md") in the
_AWS Organizations User Guide_.

Management account
A management account is an AWS account that acts as the parent or root
account for AWS Organizations.

###### Note

You cannot close a management account directly from the AWS Organizations
console.

###### To close a management account from the Accounts page

1. [Sign in to the AWS Management Console as the root user](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md") for the
   management account that you want to close. You can't close an
   account while signed in as an IAM user or role.
2. Verify that there are no active member accounts remaining in your
   organization. To do this, go to the [AWS Organizations console](https://console.aws.amazon.com/organizations "https://console.aws.amazon.com/organizations"), and make sure that
   all member accounts are showing `Closed` next to their
   account names. If you have a member account that is still active,
   you will need to follow the account closure guidance provided in the
   **Member account** tab before you can move to
   the next step.
3. On the navigation bar in the upper-right corner, choose your
   account name or number, and then choose
   **Account**.
4. On the [**Account** page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account"), choose the
   **Close account** button.
5. Type your account ID (displayed at the top of the closure dialog
   box) to confirm that you have read and understand the account
   closure process.
6. Choose the **Close account** button to initiate
   the account closure process.
7. Within a few minutes, you should receive an email confirmation
   that your account has been closed.

###### Note

This task isn't supported in the AWS CLI or by an API operation from
one of the AWS SDKs. You can perform this task only by using the AWS Management Console.

AWS GovCloud (US) account
An AWS GovCloud (US) account is always linked to a single standard
AWS account for billing and payment purposes.

**To close an AWS GovCloud (US) account**

If you have an AWS account that is linked to a AWS GovCloud (US) account,
you need to close the standard account before you close the AWS GovCloud (US)
account. For more details, including how to back-up data and avoid
unintended AWS GovCloud (US) charges, see [Closing an AWS GovCloud (US) account](../../../govcloud-us/latest/UserGuide/Closing-govcloud-account.md "../../../govcloud-us/latest/UserGuide/Closing-govcloud-account.md") in the _AWS GovCloud (US) User Guide_.

## What to expect after you close your

account

Immediately after you close your account, the following will occur:

- You will receive an email confirming the account closure to the root user’s email
  address. If you don’t receive this email within a few hours, see [Troubleshooting issues with AWS account
  closure](troubleshooting_close-account.md "troubleshooting_close-account.md").
- Any member account that you close will display a `CLOSED` label
  next to its account name in the AWS Organizations console for up to 90 days after the
  original closure date. After 90 days, the member account will no longer be
  displayed in the AWS Organizations console.
- If you have granted permissions to access services in your AWS account to
  other accounts, any access requests made from those accounts should fail after
  account closure. If you reopen your AWS account, other AWS accounts can
  again access your account's AWS services and resources if you granted the
  necessary permissions to them.

Account closure may not occur immediately across all Regions and services and can take several hours to complete.

### Post-closure period

The post-closure period refers to the length of time between the day you closed
your account and when AWS permanently closes your AWS account. The post-closure
period is 90 days. During the post-closure period, you can access your content and
AWS services only by reopening your account. After the post-closure period, AWS
permanently closes your AWS account, and you can no longer reopen it. AWS will
also delete content and resources in your account (except for CloudTrail trails). After an
account has been permanently closed, its [AWS account
ID](manage-acct-identifiers.md#awsaccountid "manage-acct-identifiers.md#awsaccountid") can never be reused.

### Reopening your AWS account

Your account will permanently close in 90 days, after which you will not be able
to reopen your account and AWS will delete the content remaining in your account.
To reopen your account before it is permanently closed, (1) you must contact [AWS Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") as soon as possible,
and (2) we must receive full payment of any outstanding balance, including providing
required information as specified on the invoice, within 60 days from the date of
account closure.

###### Note

Charges for the services that remained in your account will restart if you
reopen it.
