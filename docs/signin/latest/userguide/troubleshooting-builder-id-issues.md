# Troubleshooting AWS Builder ID issues

Use the information here to help you troubleshoot issues you might have with your
AWS Builder ID.

###### Topics

- [My email is already in use](#email-in-use-aws_builder_id "#email-in-use-aws_builder_id")
- [I can't complete email
  verification](#email-verification-aws_builder_id "#email-verification-aws_builder_id")
- [I can’t sign in with Google](#sign-in-google-builder_id "#sign-in-google-builder_id")
- [I received a sign in error when I attempted
  to sign up for a Builder ID using continue with Google](#switch-account-builder_id "#switch-account-builder_id")
- [I can’t create a Hodgkin account](#create-account-hodgkin "#create-account-hodgkin")
- [I receive an error that states 'It’s not
  you, it’s us' when I try to sign in with my AWS Builder ID](#error-sign-in-aws_builder_id "#error-sign-in-aws_builder_id")
- [I forgot my password](#forgot-password-aws_builder_id "#forgot-password-aws_builder_id")
- [I can't set a new password](#reset-not-working-aws_builder_id "#reset-not-working-aws_builder_id")
- [My password isn’t working](#password-not-working-aws_builder_id "#password-not-working-aws_builder_id")
- [My password isn't working
  and I can no longer access emails sent to my AWS Builder ID email address](#password-email-not-working-aws_builder_id "#password-email-not-working-aws_builder_id")
- [I can't enable MFA](#enable-mfa-aws_builder_id "#enable-mfa-aws_builder_id")
- [I can't add an authenticator app as a MFA
  device](#add-mfa-aws_builder_id "#add-mfa-aws_builder_id")
- [I can't remove an MFA device](#remove-mfa-aws_builder_id "#remove-mfa-aws_builder_id")
- [I get the message 'An unexpected error has
  occurred' when I try to register or sign in with an authenticator app](#syncing-mfa-aws_builder_id "#syncing-mfa-aws_builder_id")
- [I get the message 'It's not you, it's us' when
  trying to sign in to AWS Builder ID](#its-not-you-its-us "#its-not-you-its-us")
- [Sign out doesn't sign me out
  completely](#sign-out-completely-aws_builder_id "#sign-out-completely-aws_builder_id")
- [I'm still looking to solve my problem](#last-help-aws_builder_id "#last-help-aws_builder_id")

## My email is already in use

If the email that you entered is already in use and you recognize it as your own, then
you may already have signed up for an AWS Builder ID. Try signing in using that email
address. If you don't remember your password, see [I forgot my password](#forgot-password-aws_builder_id "#forgot-password-aws_builder_id").

## I can't complete email

verification

If you signed up for AWS Builder ID but have not received your verification email,
complete the following troubleshoot tasks.

1. Check your spam, junk, and deleted items folder.

###### Note

This verification email comes from either the address [no-reply@signin.aws](mailto:no-reply@signin.aws "mailto:no-reply@signin.aws") or [no-reply@login.awsapps.com](mailto:no-reply@login.awsapps.com "mailto:no-reply@login.awsapps.com"). We recommend that you configure
your mail system so that it accepts emails from these sender email addresses
and does not handle them as junk or spam. 2. Choose **Resend code**, refresh your inbox, and check your
spam, junk, and deleted items folders again. 3. If you still don't see your verification email, double-check your AWS Builder ID
email address for typos. If you entered the wrong email address, sign up again
with an email address that you own.

## I can’t sign in with Google

If you have an existing Builder ID profile with the same email address as your Google
account, use your AWS Builder ID password to sign in to your account. If you don't remember
your password, see [I forgot my password](#forgot-password-aws_builder_id "#forgot-password-aws_builder_id").

For help signing in with your Google password, see [Can't sign in
to your Google Account](https://support.google.com/accounts/troubleshooter/2402620?hl=en "https://support.google.com/accounts/troubleshooter/2402620?hl=en").

## I received a sign in error when I attempted

to sign up for a Builder ID using continue with Google

This means that you either have an existing Builder ID using the same email address as
your Google account, or that the email address associated with your Google account is
not verified. In either case, please try to sign up again entering your email address
and providing a password.

## I can’t create a Hodgkin account

If your email is already associated with an AWS account, you may not be able to
create a Hodgkin account for one of the following reasons:

- **Your email is already associated with an AWS account**.
  Continue to the AWS Management Console to sign in and set up the Hodgkin application.
- **Your email address is already associated with an account that has
  been closed**. Use a different email to create your Hodgkin
  account.

For help with troubleshooting account issues, see [Troubleshoot your
AWS account](../../../accounts/latest/reference/troubleshooting.md "../../../accounts/latest/reference/troubleshooting.md") in the _AWS Account Management Reference Guide_.

## I receive an error that states 'It’s not

you, it’s us' when I try to sign in with my AWS Builder ID

If you receive this error message when you try to sign in, there might be an issue
with your local settings or email address.

- Verify the date and time settings on the device you’re using to sign in. We
  recommend that you allow the date and time to be set automatically. If that’s
  not available, we recommend syncing your date and time to a known [Network Time
  Protocol (NTP)](https://en.wikipedia.org/wiki/Network_Time_Protocol "https://en.wikipedia.org/wiki/Network_Time_Protocol") server.
- Review your email address for formatting errors. The following issues will
  return an error when trying to sign in with your AWS Builder ID.
  - Space in an email address
  - Forward slash (/) in an email address
  - Two periods (.) in an email address
  - Two ampersands (@) in an email address
  - Comma (,) at the end of an email address
  - Bracket (]) at the end of an email address

## I forgot my password

###### To reset your forgotten password

1. On the **Sign in with AWS Builder ID** page, enter the email you
   used to create your AWS Builder ID in **Email address**. Choose
   **Next**.
2. Choose **Forgot password?**. We send a link to the email
   address associated with your AWS Builder ID where you can reset your password.
3. Follow the instructions in the email.

## I can't set a new password

For your security, you must follow these requirements whenever you set or change your
password:

- Passwords are case-sensitive.
- Passwords
  must be between 8 and 64 characters in length.
- Passwords must contain at least one character from each of the following four
  categories:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Non-alphanumeric characters
    (~!@#$%^management portal\*\_-+=`|\(){}[]:;"'<>,.?/)

- The last three passwords can't be reused.
- Passwords that are publicly known through a data set leaked from a third party
  can't be used.

## My password isn’t working

If you remember your password, but it isn't working when you sign in with AWS Builder ID,
make sure that:

- Caps lock is off.
- You're not using an older password.
- You're using your AWS Builder ID password and not one for an AWS account.

If you verify that your password is up-to-date and entered correctly, but it still
doesn't work, follow the instructions in [I forgot my password](#forgot-password-aws_builder_id "#forgot-password-aws_builder_id") to reset your password.

## My password isn't working

and I can no longer access emails sent to my AWS Builder ID email address

If you can still sign in to your AWS Builder ID, use the **Profile** page
to update your AWS Builder ID email to your new email address. After you complete email
verification, you are able to sign in to AWS and receive communications at your new
email address.

If you used a work or college email address, and have left the company or school and
can’t receive any emails sent to that address, reach out to the administrator of that
email system. They might be able to forward your email to a new address, grant you
temporary access, or share content from your mailbox.

## I can't enable MFA

To enable MFA, add one or more MFA devices to your profile by following the steps in
[Manage AWS Builder ID multi-factor authentication (MFA)](mfa-builder-id.md "mfa-builder-id.md").

## I can't add an authenticator app as a MFA

device

If you find that you can't add another MFA device, you may have reached the limit of
MFA devices that you can register in that application. Try removing an unused MFA device
or using a different authenticator app.

## I can't remove an MFA device

If you intend to disable MFA, then proceed with removing your MFA device by following
the steps in [Delete your MFA device](mfa-builder-id.md#delete-mfa-aws_builder_id "mfa-builder-id.md#delete-mfa-aws_builder_id"). However, if you want to keep MFA
enabled, you should add another MFA device before attempting to delete an existing MFA
device. For more information about adding another MFA device, see [Manage AWS Builder ID multi-factor authentication (MFA)](mfa-builder-id.md "mfa-builder-id.md").

## I get the message 'An unexpected error has

occurred' when I try to register or sign in with an authenticator app

A time-based one-time password (TOTP) system, such as the one used by AWS Builder ID in
combination with a code-based authenticator app, relies on time synchronization between
the client and the server. Ensure that the device where your authenticator app is
installed is correctly synchronized to a reliable time source, or manually set the time
on your device to match a reliable source, such as [NIST](https://www.time.gov/ "https://www.time.gov/") or other local/regional equivalents.

## I get the message 'It's not you, it's us' when

trying to sign in to AWS Builder ID

Verify the date and time settings on the device you're using to sign in. We recommend
that you set the date and time to be set automatically. If that's not available, we
recommend syncing your date and time to a known Network Time Protocol (NTP)
server.

## Sign out doesn't sign me out

completely

The system is designed to sign out immediately, but full sign out may take up to an
hour.

###### Note

When using **Continue with Google**, deleting active Builder ID
sessions will not log you out of your Google account.

## I'm still looking to solve my problem

You can fill out the [Support
Feedback form](https://support.aws.amazon.com/#/contacts/aws-account-support/ "https://support.aws.amazon.com/#/contacts/aws-account-support/"). In the **Request information** section,
under **How can we help you**, include that you’re using AWS Builder ID.
Provide as much detail as possible so that we can most efficiently address your
issue.
