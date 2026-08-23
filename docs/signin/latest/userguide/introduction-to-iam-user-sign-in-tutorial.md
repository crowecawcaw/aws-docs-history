# Sign in to the AWS Management Console as an IAM user

An [IAM user](user-types-list.md#iam-user-type "user-types-list.md#iam-user-type") is an identity created within an AWS account that has permission to
interact with AWS resources. IAM users sign-in using their account ID or alias, their user
name, and a password. IAM user names are configured by your administrator. IAM user names can
be either friendly names, such as `Zhang`, or email addresses such as
`zhang@example.com`. IAM user names can't include spaces, but can
include upper and lower case letters, numbers, and the symbols `+ = , . @ _ -`.

This sign-in method is only supported for accounts created with Sign up for AWS (advanced). For more information, see [Compare sign-up options](../../../accounts/latest/reference/sign-up-for-aws.md "../../../accounts/latest/reference/sign-up-for-aws.md").

###### Tip

If your IAM user has multi-factor authentication (MFA) enabled, you must have access to
the authentication device. For details, see [Using MFA devices with your IAM sign-in
page](../../../IAM/latest/UserGuide/console_sign-in-mfa.md "../../../IAM/latest/UserGuide/console_sign-in-mfa.md").

## To sign in as an IAM user

You can sign in as an IAM user while you are already signed in to another identity in the
AWS Management Console. For details, see [Signing in to multiple accounts](../../../awsconsolehelpdocs/latest/gsg/multisession.md "../../../awsconsolehelpdocs/latest/gsg/multisession.md")
in the _AWS Management Console Getting Started Guide_.

1. Open the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. The main sign-in page appears. Enter the account ID (12 digits) or alias, your IAM user
   name, and password.

###### Note

You might not have to enter your account ID or alias if you've previously signed in as
the IAM user with your current browser or if you are using your account sign-in URL. 3. Choose **Sign in**. 4. If MFA is enabled for your IAM user, AWS requires you to confirm your identity with
an authenticator. For more information, see [Using multi-factor
authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md").

After authentication the AWS Management Console opens to the Console Home page.

### To sign in as an IAM user using our new AWS experience

If you signed up for AWS using our new AWS experience, you can sign in to the AWS Management Console
as an IAM user.

######

1. Open the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. Choose our new AWS experience.
3. Choose the **IAM user** icon.
4. Enter the account ID (12 digits) or alias, your IAM user name, and
   password.

###### Note

You might not have to enter your account ID or alias if you've previously signed in as
the IAM user with your current browser or if you are using your account sign-in URL. 5. Choose **Sign in**. 6. If MFA is enabled for your IAM user, AWS requires you to confirm your identity with
an authenticator. For more information, see [Using multi-factor
authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md").

### Additional information

If you want more information about IAM users, refer to the following resources.

- For an overview of IAM, see [What is Identity and Access
  Management?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md")
- For details about AWS account IDs, see [Your AWS account ID and its
  alias](../../../IAM/latest/UserGuide/console_account-alias.md "../../../IAM/latest/UserGuide/console_account-alias.md").
- For step-by-step directions on how to reset your IAM user password, see [I forgot my IAM user password for my AWS account](troubleshooting-sign-in-issues.md#troubleshoot-forgot-iam-password "troubleshooting-sign-in-issues.md#troubleshoot-forgot-iam-password").
