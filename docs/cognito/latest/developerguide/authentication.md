

# Authentication with Amazon Cognito user pools
<a name="authentication"></a>

Amazon Cognito includes several methods to authenticate your users. Users can sign in with passwords and WebAuthn passkeys. Amazon Cognito can send them a one-time password in an email or SMS message. You can implement Lambda functions that orchestrate your own sequence of challenges and responses. These are *authentication flows*. In authentication flows, users provide a secret and Amazon Cognito verifies the secret, then issues JSON web tokens (JWTs) for applications to process with OIDC libraries. In this chapter, we'll talk about how to configure your user pools and app clients for various authentication flows in various application environments. You'll learn about options for the use of the hosted sign-in pages of managed login, and for building your own logic and front end in an AWS SDK.

All user pools, whether you have a domain or not, can authenticate users in the user pools API. If you add a domain to your user pool, you can use the [user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-userpools-server-contract-reference.html). The user pools API supports a variety of authorization models and request flows for API requests.

To verify the identity of users, Amazon Cognito supports authentication flows that incorporate challenge types in addition to passwords like email and SMS message one-time passwords and passkeys.

Before you configure the details, choose the authentication approach that fits your application. The following decision aid summarizes the two entry points and, within a custom-built application, the two initial sign-in flows. Each option links to its detailed section.

**Do you want Amazon Cognito to host the sign-in pages, or build your own front end?**  
If you want the lowest-effort path, use [managed login](authentication-flows-selection-managedlogin.md). Amazon Cognito hosts the sign-in, sign-out, and password-reset pages, and your application processes the result with an OpenID Connect (OIDC) relying-party library. Managed login automatically presents the authentication methods that your user pool and app client configuration allow.  
If you want to build your own UI and control the sign-in logic, use an [AWS SDK](authentication-flows-selection-sdk.md). Your application calls the user pools API directly and you implement the challenge-response logic.

**In a custom-built application, do you collect the sign-in method from the user, or declare it up front?**  
Choose [choice-based authentication](authentication-flows-selection-sdk.md#authentication-flows-selection-choice) (the `USER_AUTH` flow) when you want to offer users a list of available sign-in methods and let them select one. This flow is the only way to offer [passwordless](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless) and [passkey](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey) sign-in.  
Choose [client-based authentication](authentication-flows-selection-sdk.md#authentication-flows-selection-client) when your application already knows how the user will sign in and declares the flow up front, for example `USER_SRP_AUTH`. Client-based authentication is the only way to use the [custom authentication](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-custom) and [refresh token](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-refresh) flows.

**Prerequisites for choice-based authentication**  
Choice-based authentication applies to both managed login and the AWS SDKs. To use it, add `ALLOW_USER_AUTH` to the allowed authentication flows of your app client. The passwordless and passkey methods additionally require a [managed login domain](managed-login-branding.md) and a [feature plan](cognito-sign-in-feature-plans.md) above the **Lite** tier (Essentials or Plus).

**Topics**
+ [Application-specific settings with app clients](user-pool-settings-client-apps.md)
+ [Implement authentication flows](authentication-implement.md)
+ [Things to know about authentication with user pools](authentication-flow-things-to-know.md)
+ [An example authentication session](#amazon-cognito-user-pools-authentication-flow)
+ [Configure authentication methods for managed login](authentication-flows-selection-managedlogin.md)
+ [Manage authentication methods in AWS SDKs](authentication-flows-selection-sdk.md)
+ [Authentication flows](amazon-cognito-user-pools-authentication-flow-methods.md)
+ [Authorization models for API and SDK authentication](authentication-flows-public-server-side.md)
+ [User pool sign-in with third party identity providers](cognito-user-pools-identity-federation.md)

## An example authentication session
<a name="amazon-cognito-user-pools-authentication-flow"></a>

The following diagram and step-by-step guide illustrate a typical scenario where a user signs in to an application. The example application presents a user with several sign-in options. They select one by entering their credentials, provide an additional authentication factor, and sign in.

![A flowchart that shows an application that prompts a user for input and signs them in with an AWS SDK.](https://docs.aws.amazon.com/cognito/latest/developerguide/images/authentication-api-userauth.png)


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