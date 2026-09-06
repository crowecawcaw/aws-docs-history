

# Troubleshooting our new AWS experience issues
<a name="troubleshooting-sign-in-new"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

This troubleshooting information is for issues related to signing in to our new AWS experience. When you use our new AWS experience, you have access to AWS Settings and project accounts. If you use IAM users, the IAM identity center, or federated identities, use [Troubleshooting AWS account sign-in issues](troubleshooting-sign-in-issues.md) to troubleshoot.

**Topics**
+ [AWS is telling me choose an account to access](#choose-account_sign_in_new)
+ [I receive an error that states 'It's not you, it's us' when I try to sign in](#error-sign-in_sign_in_new)
+ [I forgot my password](#forgot-password_sign_in_new)
+ [I can't set a new password](#reset-not-working_sign_in_new)
+ [My password isn't working](#password-not-working_sign_in_new)
+ [My password isn't working and I can no longer access emails sent to my sign in email address](#password-email-not-working_sign_in_new)
+ [I can't enable MFA](#enable-mfa_sign_in_new)
+ [I can't add an authenticator app as a MFA device](#add-mfa_sign_in_new)
+ [I can't remove an MFA device](#remove-mfa_sign_in_new)
+ [I get the message 'An unexpected error has occurred' when I try to register or sign in with an authenticator app](#syncing-mfa_sign_in_new)
+ [I get the message 'It's not you, it's us' when trying to sign in](#its-not-you-its-us_sign_in_new)
+ [Sign out doesn't sign me out completely](#sign-out-completely_sign_in_new)
+ [I'm still looking to solve my problem](#last-help_sign_in_new)

## AWS is telling me choose an account to access
<a name="choose-account_sign_in_new"></a>

If AWS provides a list of accounts to access, you have multiple active sessions on your browser. This could be an AWS Builder ID session or a session with a project or AWS account. Choose the account you want to access. To prevent this from happening in the future, sign out of all active sessions when you are done accessing them.

## I receive an error that states 'It's not you, it's us' when I try to sign in
<a name="error-sign-in_sign_in_new"></a>

If you receive this error message when you try to sign in, there might be an issue with your local settings or email address.
+ Verify the date and time settings on the device you're using to sign in. We recommend that you allow the date and time to be set automatically. If that's not available, we recommend syncing your date and time to a known [Network Time Protocol (NTP)](https://en.wikipedia.org/wiki/Network_Time_Protocol) server.
+ Review your email address for formatting errors. The following issues will return an error when trying to sign in:
  + Space in an email address
  + Forward slash (`/`) in an email address
  + Two periods (`.`) in an email address
  + Two ampersands (`@`) in an email address
  + Comma (`,`) at the end of an email address
  + Bracket (`]`) at the end of an email address

## I forgot my password
<a name="forgot-password_sign_in_new"></a>

If you forgot your password, you can reset it.

**To reset your forgotten password**

1. On Sign in to AWS, enter the email you used to sign in. Choose **Next**.

1. Choose **Forgot password?**.

1. For the security check, choose **Verify**. We send a link to the email address associated with your login where you can reset your password.

1. Follow the instructions in the email.

## I can't set a new password
<a name="reset-not-working_sign_in_new"></a>

For your security, you must follow these requirements whenever you set or change your password:
+ Passwords are case-sensitive.
+ Passwords must be between 8 and 64 characters in length.
+ Passwords must contain at least one character from each of the following four categories:
  + Lowercase letters (a-z)
  + Uppercase letters (A-Z)
  + Numbers (0-9)
  + Non-alphanumeric characters (\~\!@\#$%^management portal\*\_-\+=`\|\\(){}[]:;"'<>,.?/)
+ The last three passwords can't be reused.
+ Passwords that are publicly known through a data set leaked from a third party can't be used.

## My password isn't working
<a name="password-not-working_sign_in_new"></a>

If you remember your password, but it isn't working when you sign in, make sure that:
+ Caps lock is off.
+ You're not using an older password.

If you verify that your password is up-to-date and entered correctly, but it still doesn't work, follow the instructions in [I forgot my password](#forgot-password_sign_in_new) to reset your password.

## My password isn't working and I can no longer access emails sent to my sign in email address
<a name="password-email-not-working_sign_in_new"></a>

If you can still sign in to AWS Settings, use the **Profile** page to update your email to your new email address. After you complete email verification, you are able to sign in to AWS and receive communications at your new email address.

If you used a work or college email address, and have left the company or school and can't receive any emails sent to that address, reach out to the administrator of that email system. They might be able to forward your email to a new address, grant you temporary access, or share content from your mailbox.

## I can't enable MFA
<a name="enable-mfa_sign_in_new"></a>

To enable MFA, add one or more MFA devices to your profile by following the steps in [Register MFA devices](https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws-register-mfa-devices.html).

## I can't add an authenticator app as a MFA device
<a name="add-mfa_sign_in_new"></a>

If you find that you can't add another MFA device, you may have reached the limit of MFA devices that you can register in that application. Try removing an unused MFA device or using a different authenticator app.

## I can't remove an MFA device
<a name="remove-mfa_sign_in_new"></a>

If you intend to disable MFA, then proceed with removing your MFA device by following the steps in [Register MFA devices](https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws-register-mfa-devices.html). However, if you want to keep MFA enabled, you should add another MFA device before attempting to delete an existing MFA device.

## I get the message 'An unexpected error has occurred' when I try to register or sign in with an authenticator app
<a name="syncing-mfa_sign_in_new"></a>

A time-based one-time password (TOTP) system, such as the one used by sign in for our new AWS experience in combination with a code-based authenticator app, relies on time synchronization between the client and the server. Ensure that the device where your authenticator app is installed is correctly synchronized to a reliable time source, or manually set the time on your device to match a reliable source, such as [NIST](https://www.time.gov/) or other local/regional equivalents.

## I get the message 'It's not you, it's us' when trying to sign in
<a name="its-not-you-its-us_sign_in_new"></a>

Verify the date and time settings on the device you're using to sign in. We recommend that you set the date and time to be set automatically. If that's not available, we recommend syncing your date and time to a known Network Time Protocol (NTP) server.

## Sign out doesn't sign me out completely
<a name="sign-out-completely_sign_in_new"></a>

The system is designed to sign out immediately, but full sign out may take up to an hour.

**Note**  
When using a login like Google or Apple, deleting active sessions will not log you out of your account.

## I'm still looking to solve my problem
<a name="last-help_sign_in_new"></a>

You can fill out the [Support Feedback form](https://support.aws.amazon.com/#/contacts/aws-account-support/). In the **Request information** section, under **How can we help you**, include that you're using our new AWS experience. Provide as much detail as possible so that we can most efficiently address your issue.