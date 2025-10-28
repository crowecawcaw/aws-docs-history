# Passwords, account recovery, and password

policies

All users who sign in to a user pool, even [federated
users](cognito-terms.md#terms-federateduser "cognito-terms.md#terms-federateduser"), have passwords assigned to their user profiles. [Local users](cognito-terms.md#terms-localuser "cognito-terms.md#terms-localuser") and [linked users](cognito-terms.md#terms-linkeduser "cognito-terms.md#terms-linkeduser") must provide a
password when they sign in. Federated users don't use user pool passwords, but sign in with
their identity provider (IdP). You can permit users to reset their own passwords, reset or
change passwords as an administrator, and [set
policies](#user-pool-settings-policies "#user-pool-settings-policies") for password complexity and history.

Amazon Cognito doesn't store user passwords in plaintext. Instead, it stores a hash of each user's
password with a user-specific salt. Because of this, you can't retrieve existing passwords from
the user profiles in your user pools. As a best practice, don't store plaintext user passwords
anywhere. Perform password resets when users forget their passwords.

## Password reset and recovery

Users forget their passwords. You might want them to be able to reset their password
themselves, or you might want to require that an administrator resets their password for them.
Amazon Cognito user pools have options for both models. This part of the guide covers the user pool
settings and the API operations for password reset.

The [ForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md") API operation and the managed login option **Forgot your
password?** send users a code that, when they confirm that they have the correct
code, gives them an opportunity to set a new password with [ConfirmForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.md"). This is the self-service password-recovery model.

###### Recovery of unverified users

You can send recovery messages to users who have verified their email address or phone
number. If they don't have a confirmed recovery email or phone, a user pool administrator
can mark their email address or phone number verified. Edit the user's **User
attributes** in the Amazon Cognito console and select the checkbox next to **Mark
phone number as verified** or **Mark email address as
verified**. You can also set `email_verified` or
`phone_number_verified` to true in an [AdminUpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md") request. For new users, the [ResendConfirmationCode](../../../cognito-user-identity-pools/latest/APIReference/API_ResendConfirmationCode.md "../../../cognito-user-identity-pools/latest/APIReference/API_ResendConfirmationCode.md") API operation sends a new code to their email address or
phone number and they can complete self-service confirmation and verification.

###### Reset passwords as an administrator

The [AdminSetUserPassword](../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.md") and [AdminResetUserPassword](../../../cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.md") API operations are the administrator-inititated methods of
password reset. `AdminSetUserPassword` sets a temporary or permanent password,
and `AdminResetUserPassword` sends users a password-reset code in the same way as
`ForgotPassword`.

### Configure password reset

and recovery

Amazon Cognito automatically selects your account-recovery options from the required attributes
and sign-in options that you choose when you create a user pool in the console. You can
modify these default settings.

A user's preferred MFA method influences the methods they can use to recover their
password. Users whose preferred MFA is by email message can't receive a password-reset
code by email. Users whose preferred MFA is by SMS message can't receive a
password-reset code by SMS.

Your [password recovery](#user-pool-password-reset-and-recovery "#user-pool-password-reset-and-recovery")
settings must provide an alternative option when users aren't eligible for your
preferred password-reset method. For example, your recovery mechanisms might have email
as first priority and email MFA might be an option in your user pool. In this case, add
SMS-message account recovery as a second option or use administrative API operations to
reset passwords for those users.

Amazon Cognito replies to password-reset requests from users who don't have a valid
recovery method with an `InvalidParameterException` error response.

###### Note

Users can't receive MFA and password reset codes at the same email address or phone
number. If they use one-time passwords (OTPs) from email messages for MFA, they must use SMS
messages for account recovery. If they use OTPs from SMS messages for MFA, they must use
email messages for account recovery. In user pools with MFA, users might be unable to
complete self-service password recovery if they have attributes for their email address
but no phone number, or their phone number but no email address.

To prevent the state where users can't reset their passwords in user pools with this
configuration, set the `email` and `phone_number`
[attributes as required](user-pool-settings-attributes.md "user-pool-settings-attributes.md"). As an
alternative, you can set up processes that always collect and set those attributes when
users sign up or when your administrators create user profiles. When users have both
attributes, Amazon Cognito automatically sends password-reset codes to the destination that is
_not_ the user's MFA factor.

The following procedure configures self-service account recovery in a user pool.

Configure self-service password reset (API/SDK)
The `AccountRecoverySetting` parameter is the user pool parameter that
sets the methods that users can use to recover their password in [ForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md") API requests or when they select **Forgot
password?** in managed login. `ForgotPassword` sends a recovery
code to a verified email or a verified phone number. The recovery code is valid for
one hour. When you specify an [AccountRecoverySetting](../../../cognito-user-identity-pools/latest/APIReference/API_AccountRecoverySettingType.md "../../../cognito-user-identity-pools/latest/APIReference/API_AccountRecoverySettingType.md") for your user pool, Amazon Cognito chooses the code delivery
destination based on the priority that you set.

When you define `AccountRecoverySetting` and a user has SMS MFA
configured, SMS cannot be used as an account recovery mechanism. The priority for this
setting is determined with `1` being of the highest priority. Amazon Cognito sends a
verification to only one of the specified methods. The following example
`AccountRecoverySetting` sets email addresses as the primary destination
for account-recovery codes, falling back to SMS message if the user doesn't have an
email address attribute.

```
"AccountRecoverySetting": {
   "RecoveryMechanisms": [
      {
         "Name": "verified_email",
         "Priority": 1
      },
      {
         "Name": "verified_phone_number",
         "Priority": 2
      }
   ]
}
```

The value `admin_only` turns off self-service account recovery, instead
requiring users to contact their administrator for password reset. You cannot use
`admin_only` with any other account recovery mechanism. The following
e

```
"AccountRecoverySetting": {
   "RecoveryMechanisms": [
      {
         "Name": "admin_only",
         "Priority": 1
      }
   ]
}
```

If you do not specify `AccountRecoverySetting`, Amazon Cognito sends the
recovery code to a verified phone number first, and to a verified email address if
users don't have a phone number attribute.

For more information about `AccountRecoverySetting`, see [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") and [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md").

Configure self-service password reset (console)
Configure account-recovery and password-reset options from the
**Sign-in** menu of your user pool.

###### To set up user account recovery

1. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
2. Choose **User Pools**.
3. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
4. Choose the **Sign-in** menu. Locate **User account
   recovery** and choose **Edit**
5. To permit users to reset their own passwords, choose **Enable
   self-service account recovery**.
6. Configure the delivery method for the password-recovery codes that your user
   pool sends to users. Under **Delivery method for user account recovery
   messages**, select an available option. As a best practice, choose an
   option that has a secondary method for sending messages, for example
   **Email if available, otherwise SMS**. With a secondary
   delivery method, Amazon Cognito can send codes to users in a way that requires them to use
   a different medium for password reset than for MFA.
7. Select **Save changes**.

### Forgot password behavior

In a given hour, we allow between 5 and 20 attempts for a user to request or enter a
password reset code as part of forgot-password and confirm-forgot-password actions. The
exact value depends on the risk parameters associated with the requests. Please note that
this behavior is subject to change.

## Adding user pool password requirements

Strong, complex passwords are a security best practice for your user pool. Especially in
applications that are open to the internet, weak passwords can expose your users' credentials
to systems that guess passwords and try to access your data. The more complex a password is,
the more difficult it is to guess. Amazon Cognito has additional tools for security-conscious
administrators, like [threat
protection](cognito-user-pool-settings-threat-protection.md#cognito-user-pool-settings-threat-protection.title "cognito-user-pool-settings-threat-protection.md#cognito-user-pool-settings-threat-protection.title") and [AWS WAF web ACLs](user-pool-waf.md#user-pool-waf.title "user-pool-waf.md#user-pool-waf.title"), but
your password policy is a central element of the security of your user directory.

Passwords for local users in Amazon Cognito user pools don't automatically expire. As a best practice, log
the time, date, and metadata of user password resets in an external system. With an external
log of password age, your application or a Lambda trigger can look up a user's password age and
require a reset after a given period.

You can configure your user pool to require a minimum password complexity that conforms to
your security standards. Complex passwords have a minimum length of at least eight characters.
They also include a mix of uppercase, numeric, and special characters.

With the Essentials or Plus feature tiers, you can also set a policy for password reuse.
You can prevent a user from resetting their password to a new password that matches their
current password or any of up to 23 additional previous passwords, for a maximum total of 24.

###### To set a user pool password policy

1. Create a user pool and navigate to the **Configure security
   requirements** step, or access an existing user pool and navigate to the
   **Authentication methods** menu.
2. Navigate to **Password policy**.
3. Choose a **Password policy mode**. **Cognito
   defaults** configures your user pool with the recommended minimum settings. You
   can also choose a **Custom** password policy.
4. Set a **Password minimum length**. All users must sign up or be
   created with a password whose length is greater than or equal to this value. You can set
   this minimum value as high as 99, but your users can set passwords up to 256 characters
   long.
5. Configure password complexity rules under **Password requirements**.
   Choose the character types–numbers, special characters, uppercase letters, and
   lowercase letters–that you want to require at least one of in each user's
   password.

You can require at least one of the following characters in passwords. After Amazon Cognito
verifies that passwords contain the minimum required characters, your users' passwords can
contain additional characters of any type up to the maximum password length.

    * Uppercase and lowercase [basic latin](https://en.wikipedia.org/wiki/ISO_basic_Latin_alphabet "https://en.wikipedia.org/wiki/ISO_basic_Latin_alphabet")
     letters
    * Numbers
    * The following special characters.



    ```
    ^ $ * . [ ] { } ( ) ? " ! @ # % & / \ , > < ' : ; | _ ~ ` = + -
    ```
    * Non-leading, non-trailing space characters.

6. Set a value for **Temporary passwords set by administrators expire
   in**. After this period has passed, a new user that you created in the Amazon Cognito
   console or with `AdminCreateUser` can't sign in and set a new password. After
   they sign in with their temporary password, their user accounts never expire. To update
   the password duration in the Amazon Cognito user pools API, set a value for [TemporaryPasswordValidityDays](../../../cognito-user-identity-pools/latest/APIReference/API_PasswordPolicyType.md#CognitoUserPools-Type-PasswordPolicyType-TemporaryPasswordValidityDays "../../../cognito-user-identity-pools/latest/APIReference/API_PasswordPolicyType.md#CognitoUserPools-Type-PasswordPolicyType-TemporaryPasswordValidityDays") in your [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") or [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API request.
7. Set a value for **Prevent use of previous passwords**, if available.
   To use this feature, choose the Essentials or Plus [feature tier](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md") in your user pool. The value
   of this parameter is the number of previous passwords that a new password is prevented
   from matching when a user resets their password.

To reset access for an expired user account, do one of the following:

- Send a new temporary password and reset the expiration period with an [AdminCreateUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.md") API request that has
  `MessageAction` set to `RESEND`.
- Delete the user profile and create a new one.
- Generate a new confirmation code in an [AdminResetUserPassword](../../../cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.md") API request.
