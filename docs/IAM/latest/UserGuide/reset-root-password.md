# Reset a lost or forgotten root user password

When you first created your AWS account, you provided an email address and password.
These are your AWS account root user credentials. If you forget your root user password, you can reset the
password from the AWS Management Console.

AWS accounts managed using AWS Organizations may have [centralized root access](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management") enabled for member
accounts. These member accounts do not have root user credentials, can't sign in as a root user, and
are prevented from recovering the root user password. Contact your administrator if you need to
perform a task that requires root user credentials.

###### Important

**Having trouble signing in to AWS?** Make sure that
you're on the correct [AWS sign-in page](../../../signin/latest/userguide/console-sign-in-tutorials.md "../../../signin/latest/userguide/console-sign-in-tutorials.md")
for your type of user. If you are the AWS account root user (account owner), you can sign in to AWS
using the credentials that you set up when you created the AWS account. If you are an
IAM user, your account administrator can give you the credentials that you can use to sign
in to AWS. If you need to request support, do not use the feedback link on this page, as
the form is received by the AWS Documentation team, not Support. Instead, on the [Contact Us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") page choose **Still unable
to log into your AWS account** and then choose one of the available support
options.

###### To reset your root user password

1. Open the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and sign in using your root user credentials.

For instructions, see [Sign in to
the AWS Management Console as the root user](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md") in the _AWS Sign-In User
Guide_.

###### Note

If you are signed in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/")
with _IAM user_ credentials, then you must sign out
before you can reset the root user password. If you see the account-specific IAM user
sign-in page, choose **Sign-in using root account
credentials** near the bottom of the page. If necessary, provide your account
email address and choose **Next** to access the
**Root user sign in** page. 2. Choose **Forgot your password?**.

###### Note

If you are an IAM user, this option is not available. The **Forgot your
password?** option is only available for the root user account. IAM users must
ask their administrator to reset a forgotten password. For more information, see [I forgot my IAM user password for my AWS account](../../../signin/latest/userguide/troubleshooting-sign-in-issues.md#troubleshoot-forgot-iam-password "../../../signin/latest/userguide/troubleshooting-sign-in-issues.md#troubleshoot-forgot-iam-password"). If you sign in through
the AWS access portal, see [Resetting your
IAM Identity Center user password](../../../singlesignon/latest/userguide/resetpassword-accessportal.md "../../../singlesignon/latest/userguide/resetpassword-accessportal.md"). 3. Provide the email address that is associated with the account. Then provide the
CAPTCHA text and choose **Continue**. 4. Check the email that is associated with your AWS account for a message from
Amazon Web Services. The email will come from an address ending in `@verify.signin.aws`.
Follow the directions in the email. If you don't see the email in your account, check your
spam folder. If you no longer have access to the email, see [I don't have access to the email for my AWS account](../../../signin/latest/userguide/console-sign-in-troubleshooting.md#credentials-not-working-console "../../../signin/latest/userguide/console-sign-in-troubleshooting.md#credentials-not-working-console") in the
_AWS Sign-In User Guide_.
