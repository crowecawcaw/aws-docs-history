

# Implement authentication flows
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
   "ALLOW_USER_SRP_AUTH"
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

Managed login automatically makes your configured authentication options available in your sign-in pages. In custom-built applications, start authentication with a declaration of the initial flow.
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