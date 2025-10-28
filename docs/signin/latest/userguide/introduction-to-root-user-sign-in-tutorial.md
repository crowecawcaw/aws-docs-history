# Sign in to the AWS Management Console as the

root user

When you first create an AWS account, you begin with one sign-in identity that has complete access to all AWS services
and resources in the account. This identity is called the AWS account _root user_ and is accessed by
signing in with the email address and password that you used to create the account.

###### Important

We strongly recommend that you don't use the root user for your everyday tasks. Safeguard your root user credentials and use them to
perform the tasks that only the root user can perform. For the complete list of tasks that require you to sign in as the root user, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

## To sign in as the root user

You can sign in as the root user while you are already signed in to another identity in the
AWS Management Console. For details, see [Signing in to multiple accounts](../../../awsconsolehelpdocs/latest/gsg/multisession.md "../../../awsconsolehelpdocs/latest/gsg/multisession.md")
in the _AWS Management Console Getting Started Guide_.

AWS accounts managed using AWS Organizations may not have root user credentials, and you must contact
an administrator to perform root user actions in your member account. If you can't sign in as the
root user, see [Troubleshooting AWS account sign-in
issues](troubleshooting-sign-in-issues.md "troubleshooting-sign-in-issues.md").

######

1. Open the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").

###### Note

If you signed in previously as an **IAM user** using this browser,
your browser might display the IAM user sign-in page instead. Choose **Sign in
using root user email**. 2. Choose **Root user**. 3. Under **Root user email address**, enter the email address
associated with your root user. Then, select **Next**. 4. If you’re prompted to complete a security check, enter the characters presented to you to
continue. If you can't complete the security check, try listening to the audio or refreshing
the security check for a new set of characters.

###### Tip

Type the alphanumeric characters you see (or hear) in order without spaces. 5. Enter your password. 6. Authenticate with MFA. MFA is enforced by default on the root user. For root users of
standalone and member accounts, you must manually enable MFA, which is strongly recommended.
For more information, see [Multi-factor authentication for
AWS account root user](../../../IAM/latest/UserGuide/enable-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-mfa-for-root.md") in the _AWS Identity and Access Management User Guide_.

###### Tip

As a security best practice, we recommend removing all root user credentials from member
accounts in your AWS organization to help prevent unauthorized use. If you choose this
option, member accounts can't sign in as the root user, perform password recovery, or set up
MFA. In this case, only the management account administrator can perform a task that requires
root user credentials in a member account. For details, see [Centrally manage
root access for member accounts](../../../IAM/latest/UserGuide/id_root-user.md#id_root-user-access-management "../../../IAM/latest/UserGuide/id_root-user.md#id_root-user-access-management") in the _AWS Identity and Access Management User
Guide_. 7. Choose **Sign in**. The AWS Management Console appears.

After authentication the AWS Management Console opens to the Console Home page.

## Additional information

If you want more information about the AWS account root user, refer to the following
resources.

- For an overview of the root user, see [AWS account root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md").
- For details about using the root user, see [Using the AWS account root user](../../../accounts/latest/reference/root-user.md "../../../accounts/latest/reference/root-user.md").
- For step-by-step directions on how to reset your root user password, see [I forgot my root user password for my
  AWS account](troubleshooting-sign-in-issues.md#troubleshoot-forgot-root-password "troubleshooting-sign-in-issues.md#troubleshoot-forgot-root-password").
