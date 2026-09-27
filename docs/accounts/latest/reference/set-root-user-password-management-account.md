

# Set a root user password for your management account
<a name="set-root-user-password-management-account"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

After you've activated advanced features, your management account now uses a root email address for account recovery. While you can still recover access to your AWS Builder ID using [self-service options to recover access](https://docs.aws.amazon.com/signin/latest/userguide/recover-builder-id.html), you now recover access to your management account with root user credentials. To access the root user, you need to create a root user password. In addition, we recommend that you turn on multi-factor authentication (MFA) to enhance the security of your root user.

**To set a root user password**

1. Open the [AWS Management Console](https://console.aws.amazon.com/) and choose **Sign in using root user email**.

1. For **Email address**, enter the root user email address.

   This is the email address you set for the management account when you activated advanced features.

1. Choose **Forgot your password?**.

   The password reset process is also how you set your root user password after you activate advanced features.

1. Enter the email address that is associated with the account.

1. Provide the CAPTCHA text and choose **I'm not a robot**.

1. Check the email that is associated with your AWS account for a message from Amazon Web Services. The email will come from an address ending in `@verify.signin.aws`. Follow the directions in the email to set a root user password. If you don't see the email in your account, check your spam folder. If you no longer have access to the email, see [I don't have access to the email for my AWS account](https://docs.aws.amazon.com/signin/latest/userguide/troubleshooting-sign-in-issues.html#credentials-not-working-console) in the *AWS Sign-In User Guide*.

Once you've set the root user password, you can recover access to your account. Next, follow the guidance in [Multi-factor authentication for AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html) to turn on MFA for your root credentials.

Only use the root user to recover your account or when necessary to perform [tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks). For daily work, sign in with your identity source, such as AWS Builder ID.