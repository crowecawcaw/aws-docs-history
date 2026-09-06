

# Sign in to the AWS Management Console as an IAM user
<a name="introduction-to-iam-user-sign-in-tutorial"></a>

An [IAM user](https://docs.aws.amazon.com/signin/latest/userguide/user-types-list.html#iam-user-type) is an identity created within an AWS account that has permission to interact with AWS resources. IAM users sign-in using their account ID or alias, their user name, and a password. IAM user names are configured by your administrator. IAM user names can be either friendly names, such as {{Zhang}}, or email addresses such as {{zhang@example.com}}. IAM user names can't include spaces, but can include upper and lower case letters, numbers, and the symbols `+ = , . @ _ -`. 

This sign-in method is only supported for accounts created with Sign up for AWS (advanced). For more information, see [Compare sign-up options](https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws.html).

**Tip**  
 If your IAM user has multi-factor authentication (MFA) enabled, you must have access to the authentication device. For details, see [Using MFA devices with your IAM sign-in page](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_sign-in-mfa.html).

## To sign in as an IAM user
<a name="iam-user-sign-in-tutorial"></a>

You can sign in as an IAM user while you are already signed in to another identity in the AWS Management Console. For details, see [Signing in to multiple accounts](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/multisession.html) in the *AWS Management Console Getting Started Guide*.

1. Open the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/).

1. The main sign-in page appears. Enter the account ID (12 digits) or alias, your IAM user name, and password.
**Note**  
 You might not have to enter your account ID or alias if you've previously signed in as the IAM user with your current browser or if you are using your account sign-in URL. 

1. Choose **Sign in**. 

1. If MFA is enabled for your IAM user, AWS requires you to confirm your identity with an authenticator. For more information, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html).

After authentication the AWS Management Console opens to the Console Home page.

### To sign in as an IAM user using our new AWS experience
<a name="iam-user-sign-in-new-experience"></a>

If you signed up for AWS using our new AWS experience, you can sign in to the AWS Management Console as an IAM user.

1. Open the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/).

1. Choose our new AWS experience.

1. Choose the **IAM user** icon.

1. Enter the account ID (12 digits) or alias, your IAM user name, and password.
**Note**  
You might not have to enter your account ID or alias if you've previously signed in as the IAM user with your current browser or if you are using your account sign-in URL.

1. Choose **Sign in**.

1. If MFA is enabled for your IAM user, AWS requires you to confirm your identity with an authenticator. For more information, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html).

### Additional information
<a name="iam-user-sign-in-tutorial-more-info"></a>

If you want more information about IAM users, refer to the following resources.
+ For an overview of IAM, see [What is Identity and Access Management?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
+ For details about AWS account IDs, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html).
+ For step-by-step directions on how to reset your IAM user password, see [I forgot my IAM user password for my AWS account](troubleshooting-sign-in-issues.md#troubleshoot-forgot-iam-password). 