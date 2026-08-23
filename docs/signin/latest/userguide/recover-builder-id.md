# Recover your AWS Builder ID

If you can't sign in to your AWS Builder ID, you can use the following self-service options to
recover access. The recovery option that you use depends on how you sign in and which
verification methods you set up.

Setting up a recovery email before you lose access improves your ability to recover your
AWS Builder ID. A recovery email provides an alternate way to verify your identity when you can't
access your primary email inbox. It also serves as the second verification factor when you
recover access after losing your MFA device. For more information, see [Add or change your recovery email](edit-details-builder-id.md#recovery-email-builder-id "edit-details-builder-id.md#recovery-email-builder-id").

###### Note

You can recover your AWS Builder ID only if you can complete the required identity
verification. If you can't complete self-service recovery, you can [Get help from Support](#recover-support-builder-id "#recover-support-builder-id").

## Find your recovery options

You can reach the AWS Builder ID recovery options in the following ways.

- **From the sign-in page** – On the sign-in
  page, choose **Trouble Signing In?**. On the **Builder
  ID recovery options** page, enter your AWS Builder ID email address, and
  then choose the recovery option that applies to you:

  - **Forgot password?** – Use this option if you
    sign in with an email address and password. For more information, see
    [Reset a forgotten password](#recover-password-builder-id "#recover-password-builder-id").
  - **Can't sign in with my social login?** – Use
    this option if you sign in with a social login, such as Google or Apple,
    and you can no longer access that account. For more information, see
    [Regain access when you can't use your social login](#recover-social-builder-id "#recover-social-builder-id").
  - **Need more help?** – Use this option to get
    help from Support when you can't complete self-service recovery. For more
    information, see [Get help from Support](#recover-support-builder-id "#recover-support-builder-id").

- **Inline during sign-in** – Some recovery
  options are offered directly in the sign-in flow when they apply. For example,
  if you can't complete multi-factor authentication (MFA), AWS Builder ID offers you
  the option to verify your identity another way. For more information, see [Recover access when you lose your MFA device](#recover-mfa-builder-id "#recover-mfa-builder-id").

## Reset a forgotten password

If you sign in with an email address and password and you forget your password, you
can reset it with a password reset link. AWS Builder ID sends the reset link to an email
inbox that you can access, which verifies your identity.

###### To reset your password using your primary email

1. On the sign-in page, choose **Trouble Signing In?**.
2. On the **Builder ID recovery options** page, enter your
   AWS Builder ID email address, and then choose **Forgot
   password?**.
3. Choose **Continue**. AWS Builder ID sends a password reset link to
   your primary email address.
4. Open the email from AWS, and then choose **Reset
   password**.
5. Enter and confirm your new password, and then choose
   **Continue**. You can now sign in with your new
   password.

If you can't access your primary email inbox but you set up a recovery email, you
can have the password reset link sent to your recovery email instead. For more
information, see [Add or change your recovery email](edit-details-builder-id.md#recovery-email-builder-id "edit-details-builder-id.md#recovery-email-builder-id").

###### To reset your password using your recovery email

1. On the sign-in page, choose **Trouble Signing In?**.
2. On the **Builder ID recovery options** page, enter your
   AWS Builder ID email address, and then choose **Forgot
   password?**.
3. Choose **Continue**. On the page that confirms the reset link
   was sent to your primary email, choose **Send to your recovery email
   instead**.
4. Open the email from AWS in your recovery email inbox, and then choose
   **Reset password**.
5. Enter and confirm your new password, and then choose
   **Continue**. You can now sign in with your new
   password.

###### Note

If you can't access your primary email inbox and you don't have a recovery email
set up, you can't reset your password through self-service or with assistance from
Support. We recommend that you set up a recovery email to avoid being permanently
locked out of your AWS Builder ID profile.

## Recover access when you lose your MFA device

If you set up multi-factor authentication (MFA) and you lose access to your MFA
device, you can regain access through self-service recovery. To protect your account,
self-service MFA recovery requires two verification factors: access to your primary
email inbox **and** access to your recovery email inbox.
For this reason, you must set up a recovery email to recover a lost MFA device
through self-service. For more information, see [Add or change your recovery email](edit-details-builder-id.md#recovery-email-builder-id "edit-details-builder-id.md#recovery-email-builder-id").

###### To recover access after losing your MFA device

1. Sign in to your AWS Builder ID with your password or social login.
2. When you're prompted for MFA and you can't complete the challenge, choose the
   option to verify your email addresses instead of MFA.
3. Enter the one-time password (OTP) sent to your primary email address, and then
   choose **Continue**.
4. Enter the OTP sent to your recovery email address, and then choose
   **Continue**.

After you verify both factors, AWS Builder ID grants you access to your account. You
don't need to set up MFA again during sign-in. To update your MFA devices, choose
**Security** in your AWS Builder ID profile. For more information,
see [Manage AWS Builder ID multi-factor authentication (MFA)](mfa-builder-id.md "mfa-builder-id.md").

###### Note

If you don't have access to your primary email inbox or you don't have a recovery
email set up, you can't recover a lost MFA device through self-service. To get help,
see [Get help from Support](#recover-support-builder-id "#recover-support-builder-id").

## Regain access when you can't use your social login

If you sign in with a social login (such as Google or
Apple) and you can no longer access that account, you can switch your
sign-in method to an email address and password. This switch is permanent. After you
switch, you sign in with your email address and password instead of your social
login.

###### Important

Switching your sign-in method from a social login to an email address and password
is permanent. You can't switch back to a social login afterward. AWS Builder ID preserves
your other settings, such as your recovery email and MFA devices.

To switch your sign-in method, you must verify your identity with a one-time password
(OTP) sent to your primary email address. If you set up a recovery email, you can use
that instead.

###### To switch from a social login to an email address and password

1. On the sign-in page, choose **Trouble Signing In?**.
2. On the **Builder ID recovery options** page, enter your
   AWS Builder ID email address, and then choose **Can't sign in with my
   social login?**.
3. Confirm that you want to switch your sign-in method.
4. Verify your identity:

   - Enter the OTP sent to your primary email address, and then choose
     **Continue**.
   - If you can't access your primary email inbox and you set up a recovery
     email, choose **Use your recovery email instead**, enter
     the OTP sent to your recovery email address, and then choose
     **Continue**.

5. Enter and confirm a password for your AWS Builder ID, and then choose
   **Continue**. You can now sign in with your email address
   and password.

###### Note

If you can't access your primary email inbox and you don't have a recovery email
set up, you can't switch your sign-in method through self-service or with assistance
from Support. We recommend that you set up a recovery email to avoid being permanently
locked out of your AWS Builder ID profile.

## Get help from Support

If you can't recover your AWS Builder ID through the self-service options, you can request
help from Support. On the **Builder ID recovery options** page, choose
**Need more help?** and follow the instructions to contact
Support.

To help verify your identity, provide as much detail as possible about your AWS Builder ID.
If Support can't verify that you own the AWS Builder ID, Support can't recover your
account.
