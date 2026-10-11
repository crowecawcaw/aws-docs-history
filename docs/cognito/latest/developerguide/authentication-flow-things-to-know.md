

# Things to know about authentication with user pools
<a name="authentication-flow-things-to-know"></a>

Consider the following information in the design of your authentication model with Amazon Cognito user pools.

**Authentication flows in managed login and the hosted UI**  
[Managed login](cognito-user-pools-managed-login.md) has more options for authentication than the classic hosted UI. For example, users can do passwordless and passkey authentication only in managed login.

**Custom authentication flows only available in AWS SDK authentication**  
You can't do *custom authentication flows*, or [custom authentication with Lambda triggers](user-pool-lambda-challenge.md), with managed login or the classic hosted UI. Custom authentication is available in [authentication with AWS SDKs](authentication-flows-selection-sdk.md).

**Managed login for external identity provider (IdP) sign-in**  
You can't sign users in through [third-party IdPs](cognito-user-pools-identity-federation.md) in [authentication with AWS SDKs](authentication-flows-selection-sdk.md). You must implement managed login or the classic hosted UI, redirect to IdPs, and then process the resulting authentication object with OIDC libraries in your application. For more information about managed login, see [User pool managed login](cognito-user-pools-managed-login.md).

**Passwordless authentication effect on other user features**  
Activation of passwordless sign-in with [one-time passwords](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless) or [passkeys](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey) in your user pool and app client has an effect on user creation and migration. When passwordless sign-in is active:  

1. Administrators can create users without passwords. The default invitation message template changes to no longer include the `{###}` password placeholder. For more information, see [Creating user accounts as administrator](how-to-create-user-accounts.md).

1. For SDK-based [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html) operations, users aren't required to supply a password when they sign up. Managed login and the hosted UI require a password in the sign-up page, even if passwordless authentication is permitted. For more information, see [Signing up and confirming user accounts](signing-up-users-in-your-app.md).

1. Users imported from a CSV file can sign in immediatelywith passwordless options, without a password reset, if their attributes include an email address or phone number for an available passwordless sign-in option. For more information, see [Importing users into user pools from a CSV file](cognito-user-pools-using-import-tool.md).

1. Passwordless authentication doesn't invoke the [user migration Lambda trigger](user-pool-lambda-migrate-user.md).

1. Users who sign in with a one-time password (OTP) first factor can't add a [multi-factor authentication (MFA)](user-pool-settings-mfa.md) factor to their session. Passkeys with user verification can satisfy MFA requirements when configured with `MULTI_FACTOR_WITH_USER_VERIFICATION`.

**Passkey relying party URLs can't be on the public suffix list**  
You can use domain names that you own, like `www.example.com`, as the relying party (RP) ID in your passkey configuration. This configuration is intended to support custom-built applications that run on domains that you own. The [public suffix list](https://publicsuffix.org/), or PSL, contains protected high-level domains. Amazon Cognito returns an error when you attempt to set your RP URL to a domain on the PSL.

## Authentication session flow duration
<a name="authentication-flow-session-duration"></a>

Depending on the features of your user pool, you can end up responding to several challenges to `InitiateAuth` and `RespondToAuthChallenge` before your app retrieves tokens from Amazon Cognito. Amazon Cognito includes a session string in the response to each request. To combine your API requests into an authentication flow, include the session string from the response to the previous request in each subsequent request. By default, your users have three minutes to complete each challenge before the session string expires. To adjust this period, change your app client **Authentication flow session duration**. The following procedure describes how to change this setting in your app client configuration.

**Note**  
**Authentication flow session duration** settings apply to authentication with the Amazon Cognito user pools API. Managed login sets session duration to 3 minutes for multi-factor authentication and 8 minutes for forced password change during end-user's first sign-in with temporary password.

------
#### [ Amazon Cognito console ]

**To configure app client authentication flow session duration (AWS Management Console)**

1. From the **App integration** tab in your user pool, select the name of your app client from the **App clients and analytics** container.

1. Choose **Edit** in the **App client information** container.

1. Change the value of **Authentication flow session duration** to the validity duration that you want, in minutes, for SMS and email MFA codes. This also changes the amount of time that any user has to complete any authentication challenge in your app client.

1. Choose **Save changes**.

------
#### [ User pools API ]

**To configure app client authentication flow session duration (Amazon Cognito API)**

1. Prepare an `UpdateUserPoolClient` request with your existing user pool settings from a `DescribeUserPoolClient` request. Your `UpdateUserPoolClient` request must include all existing app client properties.

1. Change the value of `AuthSessionValidity` to the validity duration that you want, in minutes, for SMS MFA codes. This also changes the amount of time that any user has to complete any authentication challenge in your app client.

------

For more information about app clients, see [Application-specific settings with app clients](user-pool-settings-client-apps.md).

## Lockout behavior for failed sign-in attempts
<a name="authentication-flow-lockout-behavior"></a>

After five failed sign-in attempts with a user's password, regardless of whether those are requested with unauthenticated or IAM-authorized API operations, Amazon Cognito locks out your user for one second. The lockout duration then doubles after each additional one failed attempt, up to a maximum of approximately 15 minutes.

Attempts made during a lockout period generate a `Password attempts exceeded` exception, and don't affect the duration of subsequent lockout periods. For a cumulative number of failed sign-in attempts *n*, not including `Password attempts exceeded` exceptions, Amazon Cognito locks out your user for *2^(n-5)* seconds. To reset the lockout to its *n=0* initial state, your user must either sign in successfully after a lockout period expires, or not initiate any sign-in attempts for 15 consecutive minutes at any time after a lockout. This behavior is subject to change. This behavior doesn't apply to custom challenges unless they also perform password-based authentication.