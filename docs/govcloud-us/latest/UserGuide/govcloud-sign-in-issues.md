# Troubleshooting AWS GovCloud (US) sign-in or

account issues

Use the information here to help you troubleshoot sign-in and other AWS GovCloud (US)
account issues. For step-by-step directions to sign in to an AWS account, see
[Sign in as the root user](signing-into-govcloud.md#sign-in-root-user-govcloud "signing-into-govcloud.md#sign-in-root-user-govcloud")

If you are having trouble signing in to your [associated standard AWS account](getting-started-standard-account-linking.md "getting-started-standard-account-linking.md"), see [Troubleshooting sign-in issues](../../../signin/latest/userguide/troubleshooting-sign-in-issues.md "../../../signin/latest/userguide/troubleshooting-sign-in-issues.md") in the _AWS Sign-In User
Guide_ instead.

###### Note

For security purposes, AWS doesn't have access to view, provide, or change
your credentials.

###### Topics

- [My AWS GovCloud (US)
  credentials aren't working](#troubleshoot-my-credentials-are-not-working "#troubleshoot-my-credentials-are-not-working")
- [I need my AWS GovCloud (US)
  account ID or account alias](#troubleshoot-need-account-ID-alias "#troubleshoot-need-account-ID-alias")
- [I lost or forgot my
  AWS GovCloud (US) IAM user name or password](#troubleshoot-lost-iam-password "#troubleshoot-lost-iam-password")
- [I lost or forgot the access keys
  for my AWS GovCloud (US) IAM user name](#troubleshoot-lost-access-keys "#troubleshoot-lost-access-keys")
- [I lost or forgot
  the access keys for my AWS GovCloud (US) root user](#troubleshoot-lost-access-keys-govcloud-root "#troubleshoot-lost-access-keys-govcloud-root")
- [I forgot the
  root user password for my standard AWS account](#troubleshoot-forgot-root-standard-password "#troubleshoot-forgot-root-standard-password")
- [I don't know the email for
  my standard AWS account or AWS GovCloud (US) account](#troubleshoot-forgot-email-account "#troubleshoot-forgot-email-account")
- [I don't have access to the
  email for my standard AWS account or AWS GovCloud (US) account](#troubleshoot-no-access-to-email "#troubleshoot-no-access-to-email")
- [I need to change the credit
  card for my AWS GovCloud (US) account](#troubleshoot-update-credit-card "#troubleshoot-update-credit-card")
- [I need to report fraudulent
  AWS GovCloud (US) account activity](#troubleshoot-report-fraud "#troubleshoot-report-fraud")
- [I need to close my AWS GovCloud (US)
  account activity](#troubleshoot-close-account "#troubleshoot-close-account")

## My AWS GovCloud (US)

credentials aren't working

When you can't sign in to the AWS Management Console for AWS GovCloud (US), try to remember how
you previously accessed AWS.

**If you don't remember signing in using a password at
all**

You might have previously accessed AWS without using AWS credentials. This
is common for enterprise single sign-on through IAM Identity Center. Accessing AWS this way
means that you use your corporate credentials to access AWS accounts or
applications without entering your credentials.

- **AWS access portal** – If an administrator
  allows you to use credentials from outside AWS to access AWS, you
  need the URL for your portal. Check your email, browser favorites, or
  browser history for a URL that includes `awsapps.com/start`
  or `signin.aws/platform/login`.

For example, your custom URL might include an ID or a domain such as
`https://`d-1234567890`.awsapps.com/start`.
If you can't find your portal link, contact your administrator. Support
can't help you recover this information.

**If you remember signing in using a password**

You might be on the wrong page. Try signing in on a different page:

- **Root user sign-in page** – Signing in
  to the AWS Management Console for AWS GovCloud (US) as the root user is not supported. To
  learn more about the root user in AWS GovCloud (US), see [AWS GovCloud (US) account root user](govcloud-account-root-user.md "govcloud-account-root-user.md") in the _AWS GovCloud (US) User Guide_.
- **IAM user sign-in page** – If you or
  someone else created an IAM user within a single AWS GovCloud (US)
  account, you must know that account ID or alias. Enter your account ID
  or alias, user name, and password in to the [AWS Management Console for AWS GovCloud (US)](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"). To
  learn how to access the IAM user sign-in page, see [Sign in as the root user](signing-into-govcloud.md#sign-in-root-user-govcloud "signing-into-govcloud.md#sign-in-root-user-govcloud"). If you forgot your
  IAM user password, see [I lost or forgot my
  AWS GovCloud (US) IAM user name or password](#troubleshoot-lost-iam-password "#troubleshoot-lost-iam-password") for information on
  resetting your IAM user password. If you forgot your account number,
  search your email, browser favorites, or browser history for a URL that
  includes `signin.amazonaws-us-gov.com/`. Your account ID or
  alias will precede this URL, such as `account_alias_or_id.signin.amazonaws-us-gov.com`. The account
  ID can also follow the `account=` or `account%3D`
  text in the URL. If you can’t find your account ID or alias, see [I need my AWS GovCloud (US)
  account ID or account alias](#troubleshoot-need-account-ID-alias "#troubleshoot-need-account-ID-alias") .
- **AWS access portal** – If an administrator
  set up an AWS IAM Identity Center identity source for AWS, you must sign in using
  your user name and password. In this case, you need the URL for your
  portal. Check your email, secure password storage, browser favorites, or
  browser history for a URL that includes
  `start.us-gov-home.awsapps.com` or `s
signin-fips.amazonaws-us-gov.com/platform/login`. For example,
  your custom URL might include an ID or a domain such as
  `https://start.us-gov-home.awsapps.com/directory/d-1234567890`.
  If you can’t find your portal link, contact your administrator. Support
  can’t help you recover this information.

For more assistance on troubleshooting your sign-in issues, see [What
do I do if I'm having trouble signing in to or accessing my
AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/sign-in-account/ "https://aws.amazon.com/premiumsupport/knowledge-center/sign-in-account/")

## I need my AWS GovCloud (US)

account ID or account alias

If you are an IAM user and you are not signed in, you must ask your
administrator for the AWS account ID or AWS account alias. You need this
information, plus your IAM user name and password, to sign in to an
AWS account. To learn more about where to find your account ID and alias, see
[Your AWS GovCloud (US) account ID and its
alias](govcloud-account-ID-alias.md "govcloud-account-ID-alias.md") in the _AWS GovCloud (US) User Guide_.

###### Note

Support can’t help you recover this information.

## I lost or forgot my

AWS GovCloud (US) IAM user name or password

If you are an IAM user, your administrator provides your credentials. If you
forget your password, you must ask your administrator to reset your password. To
learn how an administrator can manage your password, see [Managing passwords for IAM users](../../../IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.md "../../../IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.md").

If you are an administrator of the AWS GovCloud (US) account and have forgot your
password to the AWS Management Console for AWS GovCloud (US), please contact another
administrator in the account to assist with restoring your access. If there are
no other users with administrative access to your account, you will need root
credentials for your AWS GovCloud (US) account to restore console access. To learn
how to restore administrative console access with the root user, see [AWS GovCloud (US) account root user](govcloud-account-root-user.md "govcloud-account-root-user.md") in the _AWS GovCloud (US) User Guide_.

## I lost or forgot the access keys

for my AWS GovCloud (US) IAM user name

If you are an IAM user and you forget your access keys, you will need new
access keys. If you have permission to create your own access keys, you can find
instructions for creating a new one at [Managing access keys (console)](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey"). If you do not have the required
permissions, you must ask your administrator to create new access keys. If you
are still using your old keys, ask your administrator not to delete the old
keys. To learn how an administrator can manage your access keys, see [Managing access
keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md").

You should follow the AWS [best
practice](../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials "../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials") of periodically changing your password and AWS access
keys. In AWS, you change access keys by rotating them. This means that you
create a new one, configure your applications to use the new key, and then
delete the old one. You are allowed to have two access key pairs active at the
same time for just this reason. For more information, see [Rotating access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey").

## I lost or forgot

the access keys for my AWS GovCloud (US) root user

If you forget your AWS GovCloud (US) account root access keys, you can request new
access keys, see [AWS GovCloud (US) account root user](govcloud-account-root-user.md "govcloud-account-root-user.md") in the _AWS GovCloud (US) User Guide_.

## I forgot the

root user password for my standard AWS account

If you are a root user and you have lost or forgot the password for your [associated standard AWS account](getting-started-standard-account-linking.md "getting-started-standard-account-linking.md"), you can reset your password. You
must know the email address used to create the associated standard AWS account
and you must have access to the email account. For more information, see [Resetting lost or forgotten passwords or access keys for AWS](../../../IAM/latest/UserGuide/id_credentials_access-keys_retrieve.md "../../../IAM/latest/UserGuide/id_credentials_access-keys_retrieve.md").

## I don't know the email for

my standard AWS account or AWS GovCloud (US) account

Your AWS GovCloud (US) account email address is the same as email address
configured in its [assocated standard AWS account](getting-started-standard-account-linking.md "getting-started-standard-account-linking.md"). Changing the standard
AWS account email will result in a change to the AWS GovCloud (US)) account
email.

If you are not sure of the email address associated with your AWS GovCloud (US)
account, [sign in to your
AWS GovCloud (US) account](sign-in-iam-govcloud.md "sign-in-iam-govcloud.md"). In the navigation bar, choose
**Support**, and then **Support Center**.
In the **Support Center** navigation pane, choose
**Your support cases** and open the most recently created
support case by choosing its **Case ID** or
**Subject**. In the **Case details**, look
for the email address listed in the **Opened by** field. If
your account email address has not changed since opening the case, this will be
your account email address.

###### Note

If you have never opened a support case or believe the email address has
since changed, [Create a support case for account and billing](../../../awssupport/latest/user/case-example.md "../../../awssupport/latest/user/case-example.md") and [resolve it](../../../awssupport/latest/user/monitoring-your-case.md#resolve-a-support-case "../../../awssupport/latest/user/monitoring-your-case.md#resolve-a-support-case") immediately. Review this cases **Open
by** field to see the associated account email.

If you can’t sign in to your AWS GovCloud (US) account to find your email address,
see [I don't have access to the email for my AWS account](../../../signin/latest/userguide/troubleshooting-sign-in-issues.md#troubleshoot-lost-email "../../../signin/latest/userguide/troubleshooting-sign-in-issues.md#troubleshoot-lost-email") in the AWS Sign-In
User Guide.

## I don't have access to the

email for my standard AWS account or AWS GovCloud (US) account

If you know the email address, but no longer have access to the email, see
[I don't have access to the email for my AWS account](../../../signin/latest/userguide/troubleshooting-sign-in-issues.md#troubleshoot-lost-email "../../../signin/latest/userguide/troubleshooting-sign-in-issues.md#troubleshoot-lost-email") in the
_AWS Sign-In User Guide_.

## I need to change the credit

card for my AWS GovCloud (US) account

To change the credit card for your AWS GovCloud (US) account, you must have access
to its [associated standard AWS account](getting-started-standard-account-linking.md "getting-started-standard-account-linking.md"). See [I need to change the credit card for my AWS account](../../../accounts/latest/reference/troubleshooting_other.md#troubleshoot-change-credit-card "../../../accounts/latest/reference/troubleshooting_other.md#troubleshoot-change-credit-card") in the
_AWS Account Management Reference Guide_.

## I need to report fraudulent

AWS GovCloud (US) account activity

If you suspect fraudulent activity using your AWS GovCloud (US) account and would
like to make a report, see [How do I report
abuse of AWS resources](https://aws.amazon.com/premiumsupport/knowledge-center/report-aws-abuse/ "https://aws.amazon.com/premiumsupport/knowledge-center/report-aws-abuse/").

## I need to close my AWS GovCloud (US)

account activity

See [Closing an
AWS GovCloud (US) account](Closing-govcloud-account.md "Closing-govcloud-account.md") in the _AWS GovCloud
(US) User Guide_.
