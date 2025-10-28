# Manage authentication methods in AWS

SDKs

Users in Amazon Cognito user pools can sign in with a variety of initial sign-in options, or
_factors_. For some factors, users can follow up with
multi-factor authentication (MFA). These first factors include username and password, one-time
password, passkey, and custom authentication. For more information, see [Authentication
flows](amazon-cognito-user-pools-authentication-flow-methods.md "amazon-cognito-user-pools-authentication-flow-methods.md"). When your application has
built-in UI components and imports an AWS SDK module, you must build application logic for
authentication. You must choose one of two primary methods and from that method, the
authentication mechanisms that you want to implement.

You can implement _client-based authentication_ where
your application, or client, declares the type of authentication up front. Your other option
is _choice-based authentication_, where your app collects a
username and requests the available authentication types for users. You can implement these
models together in the same application or split between app clients, according to your
requirements. Each method has features that are unique to it, for example custom
authentication in client-based and passwordless authentication in choice-based.

In custom-built applications that perform authentication with AWS SDK implementation of
the users pools API, you must structure your API requests to align with user pool
configuration, app client configuration, and client-side preferences. An
`InitiateAuth` session that begins with an `AuthFlow` of
`USER_AUTH` begins choice-based authentication. Amazon Cognito responds to your API with a
challenge of either a preferred authentication method or a list of choices. A session that
begins with `AuthFlow` of `CUSTOM_AUTH` goes right into custom
authentication with Lambda triggers.

Some authentication methods are fixed to one of the two flow types, and some methods are
available in both.

###### Topics

- [Choice-based authentication](#authentication-flows-selection-choice "#authentication-flows-selection-choice")
- [Client-based authentication](#authentication-flows-selection-client "#authentication-flows-selection-client")

## Choice-based authentication

Your application can request the following authentication methods in choice-based
authentication. Declare these options in the `PREFERRED_CHALLENGE` parameter of
[InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-AuthParameters "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-AuthParameters") or [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md#CognitoUserPools-AdminInitiateAuth-request-AuthParameters "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md#CognitoUserPools-AdminInitiateAuth-request-AuthParameters"), or in the `ChallengeName` parameter of [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md#CognitoUserPools-RespondToAuthChallenge-request-ChallengeName "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md#CognitoUserPools-RespondToAuthChallenge-request-ChallengeName") or [AdminRespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md#CognitoUserPools-AdminRespondToAuthChallenge-request-ChallengeName "../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md#CognitoUserPools-AdminRespondToAuthChallenge-request-ChallengeName").

1. `EMAIL_OTP` and `SMS_OTP`

[Passwordless sign-in with one-time passwords](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless") 2. `WEB_AUTHN`

[Passwordless
sign-in with WebAuthn passkeys](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey") 3. `PASSWORD`

[Sign-in
with persistent passwords](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-password "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-password")

[Sign-in with
persistent passwords and secure payload](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-srp "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-srp")

[MFA after
sign-in](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-mfa "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-mfa")

To review these options in their API context, see `ChallengeName` in [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md#CognitoUserPools-RespondToAuthChallenge-request-ChallengeName "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md#CognitoUserPools-RespondToAuthChallenge-request-ChallengeName").

Choice-based sign-in issues a challenge in response to your initial request. This
challenge either verifies that a requested option is available, or provides a list of
available choices. Your application can display these choices to users, who then enter
credentials for their preferred sign-in method and proceed with authentication in challenge
responses.

You have the following choice-based options in your authentication flow. All requests of
this type require that your app first collect a username or retrieve it from a cache.

1. Request options with `AuthParameters` of `USERNAME` only.
   Amazon Cognito returns a `SELECT_CHALLENGE` challenge. From there, your application
   can prompt the user to select a challenge and return this response to your user
   pool.
2. Request a preferred challenge with `AuthParameters` of
   `PREFERRED_CHALLENGE` and the parameters of your preferred challenge, if
   any. For example, if you request a `PREFERRED_CHALLENGE` of
   `PASSWORD_SRP`, you must also include `SRP_A`. If your user,
   user pool, and app client are all configured for the preferred challenge, Amazon Cognito responds
   with the next step in that challenge, for example `PASSWORD_VERIFIER` in the
   `PASSWORD_SRP` flow or [CodeDeliveryDetails](../../../cognito-user-identity-pools/latest/APIReference/API_CodeDeliveryDetailsType.md "../../../cognito-user-identity-pools/latest/APIReference/API_CodeDeliveryDetailsType.md") in the `EMAIL_OTP` and `SMS_OTP`
   flows. If the preferred challenge isn't available, Amazon Cognito responds with
   `SELECT_CHALLENGE` and a list of available challenges.
3. Sign users in first, then request their choice-based authentication options. A
   [GetUserAuthFactors](../../../cognito-user-identity-pools/latest/APIReference/API_GetUserAuthFactors.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUserAuthFactors.md") request with the access token of a signed-in user returns
   their available choice-based authentication factors and their MFA settings. With this
   option, a user can sign in with username and password first, then activate a different
   form of authentication. You can also use this operation to check additional options for
   a user who has signed in with a preferred challenge.

To [configure your app client](authentication.md#authentication-implement "authentication.md#authentication-implement") for
choice-based authentication, add `ALLOW_USER_AUTH` to the allowed authentication
flows. You must also choose the choice-based factors that you want to permit in your user
pool configuration. The following process illustrates how to choose choice-based
authentication factors.

Amazon Cognito console

###### To configure choice-based authentication options in a user pool

1. Sign in to AWS and navigate to the [Amazon Cognito user pools console](https://console.aws.amazon.com/cognito/v2/idp "https://console.aws.amazon.com/cognito/v2/idp"). Choose a user pool or create a new
   one.
2. In your user pool configuration, select the **Sign-in** menu.
   Locate **Options for choice-based sign-in** and choose
   **Edit**.
3. The **Password** option is always available. This includes
   the `PASSWORD` and `PASSWORD_SRP` flows. Select the
   **Additional choices** that you want to add to your users'
   options. You can add **Passkey** for `WEB_AUTHN`,
   **Email message one-time password** for `EMAIL_OTP`,
   and **SMS message one-time password** for
   `SMS_OTP`.
4. Choose **Save changes**.

API/SDK
The following partial [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") or [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") request body configures all available options for
choice-based authentication.

```
"Policies": {
    "SignInPolicy": {
        "AllowedFirstAuthFactors": [
            "PASSWORD",
            "WEB_AUTHN",
            "EMAIL_OTP",
            "SMS_OTP"
        ]
    }
},
```

## Client-based authentication

Client-based authentication supports the following authentication flows. Declare these
options in the `AuthFlow` parameter of [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-AuthFlow "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-AuthFlow") or [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md#CognitoUserPools-AdminInitiateAuth-request-AuthFlow "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md#CognitoUserPools-AdminInitiateAuth-request-AuthFlow").

1. `USER_PASSWORD_AUTH` and `ADMIN_USER_PASSWORD_AUTH`

[Sign-in
with persistent passwords](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-password "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-password")

[MFA after
sign-in](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-mfa "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-mfa")

This authentication flow is equivalent to `PASSWORD` in choice-based
authentication. 2. `USER_SRP_AUTH`

[Sign-in with
persistent passwords and secure payload](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-srp "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-srp")

[MFA after
sign-in](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-mfa "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-mfa")

This authentication flow is equivalent to `PASSWORD_SRP` in choice-based
authentication. 3. `REFRESH_TOKEN_AUTH`

[Refresh
tokens](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-refresh "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-refresh")

This authentication flow is only available in client-based authentication. 4. `CUSTOM_AUTH`

[Custom
authentication](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-custom "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-custom")

This authentication flow is only available in client-based authentication.

With client-based authentication, Amazon Cognito assumes that you have determined how your user
wants to authenticate before they begin authentication flows. The logic of determining the
sign-in factor that a user wants to provide must be determined with default settings or
custom prompts, then declared in the first request to your user pool. The
`InitiateAuth` request declares a sign-in `AuthFlow` that directly
corresponds to one of the listed options, for example `USER_SRP_AUTH`. With this
declaration, the request also includes the parameters to begin authentication, for example
`USERNAME`, `SECRET_HASH`, and `SRP_A`. Amazon Cognito might
follow up this request with additional challenges like `PASSWORD_VERIFIER` for
SRP or `SOFTWARE_TOKEN_MFA` for password sign-in with TOTP MFA.

To [configure your app client](authentication.md#authentication-implement "authentication.md#authentication-implement") for
client-based authentication, add any authentication flows other than
`ALLOW_USER_AUTH` to the allowed authentication flows. Examples are
`ALLOW_USER_PASSWORD_AUTH`, `ALLOW_CUSTOM_AUTH`,
`ALLOW_REFRESH_TOKEN_AUTH`. To permit client-based authentication flows, no
additional user pool configuration is required.
