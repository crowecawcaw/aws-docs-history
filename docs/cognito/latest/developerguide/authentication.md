

# Authentication with Amazon Cognito user pools
<a name="authentication"></a>

Amazon Cognito includes several methods to authenticate your users. Users can sign in with passwords and WebAuthn passkeys. Amazon Cognito can send them a one-time password in an email or SMS message. You can implement Lambda functions that orchestrate your own sequence of challenges and responses. These are *authentication flows*. In authentication flows, users provide a secret and Amazon Cognito verifies the secret, then issues JSON web tokens (JWTs) for applications to process with OIDC libraries. In this chapter, we'll talk about how to configure your user pools and app clients for various authentication flows in various application environments. You'll learn about options for the use of the hosted sign-in pages of managed login, and for building your own logic and front end in an AWS SDK.

All user pools, whether you have a domain or not, can authenticate users in the user pools API. If you add a domain to your user pool, you can use the [user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-userpools-server-contract-reference.html). The user pools API supports a variety of authorization models and request flows for API requests.

To verify the identity of users, Amazon Cognito supports authentication flows that incorporate challenge types in addition to passwords like email and SMS message one-time passwords and passkeys.

**Topics**
+ [Application-specific settings with app clients](user-pool-settings-client-apps.md)
+ [Implement authentication flows](#authentication-implement)
+ [Things to know about authentication with user pools](#authentication-flow-things-to-know)
+ [An example authentication session](#amazon-cognito-user-pools-authentication-flow)
+ [Configure authentication methods for managed login](authentication-flows-selection-managedlogin.md)
+ [Manage authentication methods in AWS SDKs](authentication-flows-selection-sdk.md)
+ [Authentication flows](amazon-cognito-user-pools-authentication-flow-methods.md)
+ [Authorization models for API and SDK authentication](authentication-flows-public-server-side.md)
+ [User pool sign-in with third party identity providers](cognito-user-pools-identity-federation.md)

## Implement authentication flows
<a name="authentication-implement"></a>

Whether you're implementing [managed login](authentication-flows-selection-managedlogin.md) or a [custom-built application front end](authentication-flows-selection-sdk.md) with an AWS SDK for authentication, you must configure your app client for the types of authentication that you want to implement. The following information describes setup for authentication flows in your [app clients](user-pool-settings-client-apps.md) and your application.

------
#### [ App client supported flows ]

You can configure supported flows for your app clients in the Amazon Cognito console or with the API in an AWS SDK. After you configure your app client to support these flows, you can deploy them in your application.

The following procedure configures available authentication flows for an app client with the Amazon Cognito console.

**To configure an app client for authentication flows (console)**

1. Sign in to AWS and navigate to the [Amazon Cognito user pools console](https://console.aws.amazon.com/cognito/v2/idp). Choose a user pool or create a new one.

1. In your user pool configuration, select the **App clients** menu. Choose an app client or create a new one.

1. Under **App client information**, select **Edit**.

1. Under **App client flows**, choose the authentication flows that you want to support.

**To configure an app client for authentication flows (API/SDK)**  
To configure available authentication flows for an app client with the Amazon Cognito API, set the value of `ExplicitAuthFlows` in a [CreateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html#CognitoUserPools-CreateUserPoolClient-request-ExplicitAuthFlows) or [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html#CognitoUserPools-UpdateUserPoolClient-request-ExplicitAuthFlows) request. The following is an example that provisions secure remote password (SRP) and choice-based authentication to a client.

```
"ExplicitAuthFlows": [ 
   "ALLOW_USER_AUTH",
   "ALLOW_USER_SRP_AUTH
]
```

When you configure app client supported flows, you can specify the following options and API values.


**App client flow support**  

| Authentication flow | Compatibility | Console | API  | 
| --- | --- | --- | --- | 
| [Choice-based authentication](authentication-flows-selection-sdk.md#authentication-flows-selection-choice) | Server-side, client-side | Select an authentication type at sign-in | ALLOW\_USER\_AUTH | 
| [Sign-in with persistent passwords](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-password) | Client-side | Sign in with username and password | ALLOW\_USER\_PASSWORD\_AUTH | 
| [Sign-in with persistent passwords and secure payload](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-srp) | Server-side, client-side | Sign in with secure remote password (SRP) | ALLOW\_USER\_SRP\_AUTH | 
| [Refresh tokens](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-refresh) | Server-side, client-side | Get new user tokens from existing authenticated sessions | ALLOW\_REFRESH\_TOKEN\_AUTH | 
| [Server-side authentication](authentication-flows-public-server-side.md#amazon-cognito-user-pools-server-side-authentication-flow) | Server-side | Sign in with server-side administrative credentials | ALLOW\_ADMIN\_USER\_PASSWORD\_AUTH | 
| [Custom authentication](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-custom) | Server-side and client-side custom-built applications. Not compatible with managed login. | Sign in with custom authentication flows from Lambda triggers | ALLOW\_CUSTOM\_AUTH | 

------
#### [ Implement flows in your application ]

Managed login automatically makes your configured authentication options available in your sign-pages. In custom-built applications, start authentication with a declaration of the initial flow.
+ To choose from a list of flow options for a user, declare [choice-based authentication](authentication-flows-selection-sdk.md#authentication-flows-selection-choice) with the `USER_AUTH` flow. This flow has available authentication methods that aren't available in client-based authentication flows, for example [passkey](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey) and [passwordless](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless) authentication.
+ To choose your authentication flow up front, declare [client-based authentication](authentication-flows-selection-sdk.md#authentication-flows-selection-client) with any other flow that's available in your app client.

When you sign users in, the body of your [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html#CognitoUserPools-InitiateAuth-request-AuthFlow) or [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html#CognitoUserPools-AdminInitiateAuth-request-AuthFlow) request must include an `AuthFlow` parameter.

Choice-based authentication:

```
"AuthFlow": "USER_AUTH"
```

Client-based authentication with SRP:

```
"AuthFlow": "USER_SRP_AUTH"
```

------

## Things to know about authentication with user pools
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

**Topics**
+ [Authentication session flow duration](#authentication-flow-session-duration)
+ [Lockout behavior for failed sign-in attempts](#authentication-flow-lockout-behavior)

### Authentication session flow duration
<a name="authentication-flow-session-duration"></a>

Depending on the features of your user pool, you can end up responding to several challenges to `InitiateAuth` and `RespondToAuthChallenge` before your app retrieves tokens from Amazon Cognito. Amazon Cognito includes a session string in the response to each request. To combine your API requests into an authentication flow, include the session string from the response to the previous request in each subsequent request. By default, your users have three minutes to complete each challenge before the session string expires. To adjust this period, change your app client **Authentication flow session duration**. The following procedure describes how to change this setting in your app client configuration.

**Note**  
**Authentication flow session duration** settings apply to authentication with the Amazon Cognito user pools API. Managed login sets session duration to 3 minutes for multi-factor authentication and 8 minutes for password-reset codes.

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

### Lockout behavior for failed sign-in attempts
<a name="authentication-flow-lockout-behavior"></a>

After five failed sign-in attempts with a user's password, regardless of whether those are requested with unauthenticated or IAM-authorized API operations, Amazon Cognito locks out your user for one second. The lockout duration then doubles after each additional one failed attempt, up to a maximum of approximately 15 minutes.

Attempts made during a lockout period generate a `Password attempts exceeded` exception, and don't affect the duration of subsequent lockout periods. For a cumulative number of failed sign-in attempts *n*, not including `Password attempts exceeded` exceptions, Amazon Cognito locks out your user for *2^(n-5)* seconds. To reset the lockout to its *n=0* initial state, your user must either sign in successfully after a lockout period expires, or not initiate any sign-in attempts for 15 consecutive minutes at any time after a lockout. This behavior is subject to change. This behavior doesn't apply to custom challenges unless they also perform password-based authentication.

## An example authentication session
<a name="amazon-cognito-user-pools-authentication-flow"></a>

The following diagram and step-by-step guide illustrate a typical scenario where a user signs in to an application. The example application presents a user with several sign-in options. They select one by entering their credentials, provide an additional authentication factor, and sign in.

![A flowchart that shows an application that prompts a user for input and signs them in with an AWS SDK.](http://docs.aws.amazon.com/cognito/latest/developerguide/images/authentication-api-userauth.png)


Picture an application with a sign-in page where users can sign in with a username and password, request a one-time code in an email message, or choose a fingerprint option.

1. **Sign-in prompt**: Your application shows a home screen with a *Log in* button.

1. **Request sign-in**: The user selects *Log in*. From a cookie or a cache, your application retrieves their username, or prompts them to enter it.

1. **Request options**: Your application requests the user's sign-in options with an `InitiateAuth` API request with the `USER_AUTH` flow, requesting the available sign-in methods for the user.

1. **Send sign-in options**: Amazon Cognito responds with `PASSWORD`, `EMAIL_OTP`, and `WEB_AUTHN`. The response includes a session identifier for you to replay back in the next response.

1. **Display options**: Your application shows UI elements for the user to enter their username and password, get a one-time code, or scan their fingerprint.

1. **Choose option/Enter credentials**: The user enters their username and password.

1. **Initiate authentication**: Your application provides the user's sign-in information with a `RespondToAuthChallenge` API request that confirms username-password sign-in and provides the username and the password.

1. **Validate credentials**: Amazon Cognito confirms the user's credentials.

1. **Additional challenge**: The user has multi-factor authentication configured with an authenticator app. Amazon Cognito returns a `SOFTWARE_TOKEN_MFA` challenge.

1. **Challenge prompt**: Your application displays a form requesting a time-based one-time password (TOTP) from the user's authenticator app.

1. **Answer challenge**: The user submits the TOTP.

1. **Respond to challenge**: In another `RespondToAuthChallenge` request, your application provides the user's TOTP.

1. **Validate challenge response**: Amazon Cognito confirms the user's code and determines that your user pool is configured to issue no additional challenges to the current user.

1. **Issue tokens**: Amazon Cognito returns ID, access, and refresh JSON web tokens (JWTs). The user's initial authentication is complete.

1. **Store tokens**: Your application caches the user's tokens so that it can reference user data, authorize access to resources, and update tokens when they expire.

1. **Render authorized content**: Your application makes a determination of the user's access to resources based on their identity and roles, and delivers application content.

1. **Access content**: The user is signed in and begins using the application.

1. **Request content with expired token**: Later, the user requests a resource that requires authorization. The user's cached token has expired.

1. **Refresh tokens**: Your application makes an `InitiateAuth` request with the user's saved refresh token.

1. **Issue tokens**: Amazon Cognito returns new ID and access JWTs. The user's session is securely refreshed without additional prompts for credentials.

You can use [AWS Lambda triggers](cognito-user-pools-working-with-lambda-triggers.md) to customize the way users authenticate. These triggers issue and verify their own challenges as part of the authentication flow.

You can also use the admin authentication flow for secure backend servers. You can use the [user migration authentication flow](cognito-user-pools-using-import-tool.md) to make user migration possible without the requirement that your users to reset their passwords.