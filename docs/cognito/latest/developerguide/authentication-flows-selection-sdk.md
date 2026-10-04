

# Manage authentication methods in AWS SDKs
<a name="authentication-flows-selection-sdk"></a>

Users in Amazon Cognito user pools can sign in with a variety of initial sign-in options, or *factors*. For some factors, users can follow up with multi-factor authentication (MFA). These first factors include username and password, one-time password, passkey, and custom authentication. For more information, see [Authentication flows](amazon-cognito-user-pools-authentication-flow-methods.md). When your application has built-in UI components and imports an AWS SDK module, you must build application logic for authentication. You must choose one of two primary methods and from that method, the authentication mechanisms that you want to implement.

You can implement *client-based authentication* where your application, or client, declares the type of authentication up front. Your other option is *choice-based authentication*, where your app collects a username and requests the available authentication types for users. You can implement these models together in the same application or split between app clients, according to your requirements. Each method has features that are unique to it, for example custom authentication in client-based and passwordless authentication in choice-based.

In custom-built applications that perform authentication with AWS SDK implementation of the users pools API, you must structure your API requests to align with user pool configuration, app client configuration, and client-side preferences. An `InitiateAuth` session that begins with an `AuthFlow` of `USER_AUTH` begins choice-based authentication. Amazon Cognito responds to your API with a challenge of either a preferred authentication method or a list of choices. A session that begins with `AuthFlow` of `CUSTOM_AUTH` goes right into custom authentication with Lambda triggers.

Some authentication methods are fixed to one of the two flow types, and some methods are available in both.

**Topics**
+ [Choice-based authentication](#authentication-flows-selection-choice)
+ [Client-based authentication](#authentication-flows-selection-client)
+ [Step-up authentication with the USER\_AUTH flow](#cognito-user-pools-step-up-user-auth)

## Choice-based authentication
<a name="authentication-flows-selection-choice"></a>

Your application can request the following authentication methods in choice-based authentication. Declare these options in the `PREFERRED_CHALLENGE` parameter of [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html#CognitoUserPools-InitiateAuth-request-AuthParameters) or [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html#CognitoUserPools-AdminInitiateAuth-request-AuthParameters), or in the `ChallengeName` parameter of [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html#CognitoUserPools-RespondToAuthChallenge-request-ChallengeName) or [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html#CognitoUserPools-AdminRespondToAuthChallenge-request-ChallengeName).

**Important**  
Choice-based sign-in has two prerequisites. Your app client must activate the `ALLOW_USER_AUTH` authentication flow, and the passwordless and passkey methods (`EMAIL_OTP`, `SMS_OTP`, `WEB_AUTHN`) require a user pool on the **Essentials** or **Plus** [feature plan](cognito-sign-in-feature-plans.md)—they aren't available on the **Lite** tier. `PASSWORD` (including SRP) is available on all feature plans. If a choice-based method doesn't appear for your users, confirm both the app-client flow and the feature plan before troubleshooting further.

1. `EMAIL_OTP` and `SMS_OTP`

   [Passwordless sign-in with one-time passwords](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless)

1. `WEB_AUTHN`

   [Passwordless sign-in with WebAuthn passkeys](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey)

1. `PASSWORD`

   [Sign-in with persistent passwords](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-password)

   [Sign-in with persistent passwords and secure payload](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-srp)

   [MFA after sign-in](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-mfa)

To review these options in their API context, see `ChallengeName` in [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html#CognitoUserPools-RespondToAuthChallenge-request-ChallengeName).

Choice-based sign-in issues a challenge in response to your initial request. This challenge either verifies that a requested option is available, or provides a list of available choices. Your application can display these choices to users, who then enter credentials for their preferred sign-in method and proceed with authentication in challenge responses.

You have the following choice-based options in your authentication flow. All requests of this type require that your app first collect a username or retrieve it from a cache.

1. Request options with `AuthParameters` of `USERNAME` only. Amazon Cognito returns a `SELECT_CHALLENGE` challenge. From there, your application can prompt the user to select a challenge and return this response to your user pool.

1. Request a preferred challenge with `AuthParameters` of `PREFERRED_CHALLENGE` and the parameters of your preferred challenge, if any. For example, if you request a `PREFERRED_CHALLENGE` of `PASSWORD_SRP`, you must also include `SRP_A`. If your user, user pool, and app client are all configured for the preferred challenge, Amazon Cognito responds with the next step in that challenge, for example `PASSWORD_VERIFIER` in the `PASSWORD_SRP` flow or [CodeDeliveryDetails](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CodeDeliveryDetailsType.html) in the `EMAIL_OTP` and `SMS_OTP` flows. If the preferred challenge isn't available, Amazon Cognito responds with `SELECT_CHALLENGE` and a list of available challenges.

1. Sign users in first, then request their choice-based authentication options. A [GetUserAuthFactors](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserAuthFactors.html) request with the access token of a signed-in user returns their available choice-based authentication factors and their MFA settings. With this option, a user can sign in with username and password first, then activate a different form of authentication. You can also use this operation to check additional options for a user who has signed in with a preferred challenge.

To [configure your app client](authentication.md#authentication-implement) for choice-based authentication, add `ALLOW_USER_AUTH` to the allowed authentication flows. You must also choose the choice-based factors that you want to permit in your user pool configuration. The following process illustrates how to choose choice-based authentication factors.

------
#### [ Amazon Cognito console ]

**To configure choice-based authentication options in a user pool**

1. Sign in to AWS and navigate to the [Amazon Cognito user pools console](https://console.aws.amazon.com/cognito/v2/idp). Choose a user pool or create a new one.

1. In your user pool configuration, select the **Sign-in** menu. Locate **Options for choice-based sign-in** and choose **Edit**.

1. The **Password** option is always available. This includes the `PASSWORD` and `PASSWORD_SRP` flows. Select the **Additional choices** that you want to add to your users' options. You can add **Passkey** for `WEB_AUTHN`, **Email message one-time password** for `EMAIL_OTP`, and **SMS message one-time password** for `SMS_OTP`.

1. Choose **Save changes**.

------
#### [ API/SDK ]

The following partial [CreateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html) or [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html) request body configures all available options for choice-based authentication.

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

------

## Client-based authentication
<a name="authentication-flows-selection-client"></a>

Client-based authentication supports the following authentication flows. Declare these options in the `AuthFlow` parameter of [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html#CognitoUserPools-InitiateAuth-request-AuthFlow) or [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html#CognitoUserPools-AdminInitiateAuth-request-AuthFlow).

1. `USER_PASSWORD_AUTH` and `ADMIN_USER_PASSWORD_AUTH`

   [Sign-in with persistent passwords](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-password)

   [MFA after sign-in](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-mfa)

   This authentication flow is equivalent to `PASSWORD` in choice-based authentication.

1. `USER_SRP_AUTH`

   [Sign-in with persistent passwords and secure payload](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-srp)

   [MFA after sign-in](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-mfa)

   This authentication flow is equivalent to `PASSWORD_SRP` in choice-based authentication.

1. `REFRESH_TOKEN_AUTH`

   [Refresh tokens](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-refresh)

   This authentication flow is only available in client-based authentication.

1. `CUSTOM_AUTH`

   [Custom authentication](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-custom)

   This authentication flow is only available in client-based authentication.

With client-based authentication, Amazon Cognito assumes that you have determined how your user wants to authenticate before they begin authentication flows. The logic of determining the sign-in factor that a user wants to provide must be determined with default settings or custom prompts, then declared in the first request to your user pool. The `InitiateAuth` request declares a sign-in `AuthFlow` that directly corresponds to one of the listed options, for example `USER_SRP_AUTH`. With this declaration, the request also includes the parameters to begin authentication, for example `USERNAME`, `SECRET_HASH`, and `SRP_A`. Amazon Cognito might follow up this request with additional challenges like `PASSWORD_VERIFIER` for SRP or `SOFTWARE_TOKEN_MFA` for password sign-in with TOTP MFA.

To [configure your app client](authentication.md#authentication-implement) for client-based authentication, add any authentication flows other than `ALLOW_USER_AUTH` to the allowed authentication flows. Examples are `ALLOW_USER_PASSWORD_AUTH`, `ALLOW_CUSTOM_AUTH`, `ALLOW_REFRESH_TOKEN_AUTH`. To permit client-based authentication flows, no additional user pool configuration is required.

## Step-up authentication with the USER\_AUTH flow
<a name="cognito-user-pools-step-up-user-auth"></a>

You request step-up authentication in the existing `USER_AUTH` flow with the [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html) and [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html) operations. There are no new API operations. The corresponding server-side operations, [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html) and [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html), support the same step-up parameters and behavior, and `AdminInitiateAuth` can also optionally take an access token. This flow works both when a user has an existing ID token and when a user authenticates toward a target level for the first time. For more information about the flow, see [An example authentication session](authentication.md#amazon-cognito-user-pools-authentication-flow).

For more information about ACR levels and AMR values, see [Authentication levels with ACR and AMR claims](cognito-user-pools-step-up-authentication.md).

**Note**  
Step-up authentication requires the Essentials or Plus feature plan.

You pass the step-up parameters in the `AuthParameters` map of your `InitiateAuth` (or `AdminInitiateAuth`) request: the new `TARGET_ACR_VALUES` and `MAX_AGE`, together with the existing `USERNAME`, `ACCESS_TOKEN`, and `PREFERRED_CHALLENGE`. For the definition and constraints of each parameter, see [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html) and [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html) in the *Amazon Cognito user pools API Reference*.

The following table describes how Amazon Cognito responds to combinations of these parameters.


**USER\_AUTH step-up authentication behavior**  

| Parameters | Behavior | 
| --- | --- | 
| TARGET\_ACR\_VALUES and ACCESS\_TOKEN, with MAX\_AGE satisfied | Amazon Cognito steps the user up from the token's current factors to the highest-priority satisfiable level. | 
| TARGET\_ACR\_VALUES and ACCESS\_TOKEN, with MAX\_AGE not satisfied | Amazon Cognito authenticates the user from scratch toward the target level. | 
| TARGET\_ACR\_VALUES without ACCESS\_TOKEN | Amazon Cognito authenticates the user from scratch toward the target level. | 
| Neither parameter | The USER\_AUTH flow behaves as it does without step-up authentication. | 

Keep the following behavior in mind when you design a step-up authentication flow.
+ Step-up authentication is all-or-nothing. If reaching the target level requires multiple challenges, for example a password and a TOTP for level 4, and the user fails any challenge, the step-up attempt fails entirely. Amazon Cognito doesn't issue intermediate tokens.
+ If the presented token already meets or exceeds the requested level, Amazon Cognito returns an error instead of issuing a new token. This prevents applications from using step-up authentication as a token-refresh mechanism.
+ The user must already have the factors to satisfy a requested level. If the user has no factors configured to meet any requested target level, Amazon Cognito returns an error. Step-up authentication doesn't prompt the user to set up new factors.
+ MFA is a floor. If the MFA settings of the user or the user pool require MFA, initial sign-in still enforces and prompts that MFA challenge even when the target level is lower and wouldn't otherwise require MFA. MFA that threat protection (advanced security features) prompts for is also enforced on initial sign-in, even when the requested target ACR level wouldn't otherwise require MFA. `TARGET_ACR_VALUES` can't suppress a required MFA prompt. At most, the target can influence which of several enabled MFA factors Amazon Cognito prompts for. If a step-up request targets a lower level, for example level 1, for a user who is required to use MFA, Amazon Cognito silently enforces the required MFA. It steps the user up and doesn't return an error.

Requesting step-up authentication with `TARGET_ACR_VALUES` requires the Essentials or Plus feature plan. For more information, see [Feature plan requirements](cognito-user-pools-step-up-authentication.md#cognito-user-pools-step-up-authentication-tiers).