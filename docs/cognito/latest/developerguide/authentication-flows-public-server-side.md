

# Authorization models for API and SDK authentication
<a name="authentication-flows-public-server-side"></a>

When you're starting development of your application with user pools authentication, you must decide on the API authorization model that fits your application type. An authorization model is a system for providing authorization to make requests with the authentication components in the Amazon Cognito user pools API and SDK integrations. Amazon Cognito has three authorization models: IAM-authorized, public, and token-authorized.

With IAM-authorized requests, the authorization comes from a signature by a set of AWS IAM credentials in the `Authorization` header of a request. For server-side applications, this practice protects authentication operations with IAM authorization. With public (unauthenticated) authentication requests, no authorization is required. This is suitable for client-side applications distributed to users. With token-authorized operations, typically implemented in combination with public operations, the authorization comes from a session token or an access token included in the `Authorization` header of the request. Amazon Cognito authentication typically requires that you implement two or more API operations in order, and the API operations you use depend on the characteristics of your application. Public clients, where the application is distributed to users, use public operations, where requests for sign-in don't require authorization. Token-authorized operations continue the session of users in public applications. Server-side clients, where the application logic is hosted on a remote system, protect authentication operations with IAM authorization for sign-in requests. The API operation pairs that follow, and their corresponding SDK methods, map to the available authorization models.

Each public authentication operation has some form of server-side equivalent, for example [UpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.html) and [AdminUpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.html). While client-side operations are user-initiated and require confirmation, server-side operations assume the change was committed by a user pool administrator and changes take immediate effect. In this example, Amazon Cognito sends a message with a confirmation code to the user, and the user's access token authorizes a [VerifyUserAttribute](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifyUserAttribute.html) request that submits the code. The server-side application can immediately set the value of any attribute, although [special considerations apply](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.html#CognitoUserPools-AdminUpdateUserAttributes-request-UserAttributes) for changing the value of email addresses and phone numbers when they're used for sign-in.

To compare API authentication and see a full list of API operations and their authorization models, see [Understanding API, OIDC, and managed login pages authentication](#user-pools-API-operations).

------
#### [ Client-side (public) authentication ]

The following is a typical sequence of requests in a client-side application

1. The public [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html) operation submits primary credentials like a username and password.

1. The token-authorized [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html) operation submits a *session* token from the `InitiateAuth` response and the answer to a challenge, for example MFA. Session token authorization indicates requests that are part of not-yet-complete authentication cycles.

1. The token-authorized [ConfirmDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.html) operation submits an *access* token and performs the write operation of adding a remembered device to the user's profile. Access token authorization indicates requests that are for user self-service operations after they have completed authentication.

For more information, see [Client-side authentication options](#amazon-cognito-user-pools-client-side-authentication-flow) and [Understanding API, OIDC, and managed login pages authentication](#user-pools-API-operations).

------
#### [ Server-side authentication ]

The following is a typical sequence of requests from a server-side operation. Each request has an [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) authorization header signed with IAM machine credentials that were issued to the application server.

1. The [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html) operation submits primary credentials like a username and password.

1. [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html) operation submits the answer to a challenge, for example MFA.

1. The [AdminUpdateDeviceStatus](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateDeviceStatus.html) operation sets the device key from the `AdminInitiateAuth` [response](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html#API_AdminInitiateAuth_ResponseSyntax) as remembered.

For more information, see [Server-side authentication options](#amazon-cognito-user-pools-server-side-authentication-flow) and [Understanding API, OIDC, and managed login pages authentication](#user-pools-API-operations).

------

A user authenticates by answering successive challenges until authentication either fails or Amazon Cognito issues tokens to the user. You can repeat these steps with Amazon Cognito, in a process that includes different challenges, to support any custom authentication flow.

**Topics**
+ [Server-side authentication options](#amazon-cognito-user-pools-server-side-authentication-flow)
+ [Client-side authentication options](#amazon-cognito-user-pools-client-side-authentication-flow)
+ [Understanding API, OIDC, and managed login pages authentication](#user-pools-API-operations)
+ [List of API operations grouped by authorization model](#user-pool-apis-auth-unauth)

## Server-side authentication options
<a name="amazon-cognito-user-pools-server-side-authentication-flow"></a>

Web applications and other *server-side* applications implement authentication on a remote server that a client loads in a remote-display application like a browser or SSH session. Server-side applications typically have the following characteristics.
+ They're built in an application installed on a server in languages like Java, Ruby, or Node.js.
+ They connect to user pool [app clients](user-pool-settings-client-apps.md) that might have a client secret, called *confidential clients*.
+ They have access to AWS credentials.
+ They invoke [managed login](cognito-user-pools-managed-login.md) for authentication, or use IAM-authorized operations in the user pools API with an AWS SDK.
+ They serve internal customers and might serve public customers.

Server-side operations with the user pools API can use passwords, one-time passwords, or passkeys as the primary sign-in factor. For server-side apps, user pool authentication is similar to authentication for client-side apps, except for the following:
+ The server-side app makes an [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html) API request. This operation requires AWS credentials with permissions that include `cognito-idp:AdminInitiateAuth` and `cognito-idp:AdminRespondToAuthChallenge`. The operation returns the required challenge or authentication outcome.
+ When the application receives a challenge, it makes an [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html) API request. The `AdminRespondToAuthChallenge` API operation also requires AWS credentials.

For more information about signing Amazon Cognito API requests with AWS credentials, see [Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

In the `AdminInitiateAuth` response `ChallengeParameters`, the `USER_ID_FOR_SRP` attribute, if present, contains the user's actual username, not an alias (such as email address or phone number). In your call to `AdminRespondToAuthChallenge`, in the `ChallengeResponses`, you must pass this username in the `USERNAME` parameter. 

**Note**  
Because backend admin implementations use the admin authentication flow, the flow doesn't support remembered devices. When you have turned on device tracking, admin authentication succeeds, but any call to refresh the access token fails.

## Client-side authentication options
<a name="amazon-cognito-user-pools-client-side-authentication-flow"></a>

Mobile apps and other *client-side* application types are installed on users' devices and perform the logic of authentication and user interface locally. They typically have the following characteristics.
+ They're built in languages like React native, Flutter, and Swift and deploy to user devices.
+ They connect to user pool [app clients](user-pool-settings-client-apps.md) that don't have a client secret, called *public clients*.
+ They don't have access to AWS credentials that would authorize IAM-authorized API requests.
+ They invoke [managed login](cognito-user-pools-managed-login.md) for authentication, or use public and token-authorized operations in the user pools API with an AWS SDK.
+ They serve public customers and permit anyone to sign up and sign in.

Client-side operations with the user pools API can use passwords, one-time passwords, or passkeys as the primary sign-in factor. The following process works for user client-side apps that you create with [AWS Amplify](https://docs.amplify.aws/javascript/start/getting-started/) or the [AWS SDKs](https://aws.amazon.com/developer/tools/).

1. The user enters their username and password into the app.

1. The app calls the `InitiateAuth` operation with the user's username and Secure Remote Password (SRP) details.

   This API operation returns the authentication parameters.
**Note**  
The app generates SRP details with the Amazon Cognito SRP features that are built in to AWS SDKs.

1. The app calls the `RespondToAuthChallenge` operation. If the call succeeds, Amazon Cognito returns the user's tokens, and the authentication flow is complete.

   If Amazon Cognito requires another challenge, the call to `RespondToAuthChallenge` returns no tokens. Instead, the call returns a session.

1. If `RespondToAuthChallenge` returns a session, the app calls `RespondToAuthChallenge` again, this time with the session and the challenge response (for example, MFA code).

## Understanding API, OIDC, and managed login pages authentication
<a name="user-pools-API-operations"></a>

Amazon Cognito user pools are a combination of several authentication technologies. They are relying parties to external identity providers (IdPs). They are IdPs to applications that implement authentication with OpenID Connect (OIDC) SDKs. They provide authentication as issuers of JSON web tokens (JWTs) similar to OIDC authentication, but in API methods that are part of AWS SDKs. They can also be secure points of entry to your applications.

When you want to sign up, sign in, and manage users in your user pool, you have two options. 

1. Your *managed login pages* and the classic *hosted UI* include the [managed login user-interactive endpoints](managed-login-endpoints.md) and the [federation endpoints](federation-endpoints.md) that handle IdP and relying-party roles. They make up a package of public webpages that Amazon Cognito activates when you [choose a domain](cognito-user-pools-assign-domain.md) for your user pool. For a quick start with the authentication and authorization features of Amazon Cognito user pools, including pages for sign-up, sign-in, password management, and multi-factor authentication (MFA), use the built-in user interface of managed login.

   The other user pool endpoints facilitate authentication with third-party identity providers (IdPs). The services that they perform include the following.

   1. Service-provider callback endpoints for authenticated claims from your IdPs, like `saml2/idpresponse` and `oauth2/idpresponse`. When Amazon Cognito is an intermediate service provider (SP) between your app and your IdP, the callback endpoints represent the service.

   1. Endpoints that provide information about your environment, like `oauth2/userInfo` and `/.well-known/jwks.json`. Your app uses these endpoints when it verifies tokens or retrieves user profile data with OIDC or OAuth 2.0 developer libraries.

1. The [Amazon Cognito user pools API](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/Welcome.html) is a set of tools for your web or mobile app to authenticate users after it collects sign-in information in your own custom front end. User pools API authentication produces the following JSON web tokens.

   1. An identity token with verifiable attribute claims from your user.

   1. An access token that authorizes your user to create token-authorized API requests to an [AWS service endpoint](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html).
**Note**  
By default, access tokens from user pools API authentication only contain the `aws.cognito.signin.user.admin` scope. To generate an access token with additional scopes, for example to authorize a request to a third-party API, request scopes during authentication through your user pool endpoints or add custom scopes in a [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md). Access token customization adds costs to your AWS bill.

   1. A refresh token that authorizes requests for new ID and access tokens, and refreshes user identity and access-control properties.

You can link a federated user, who would normally sign in through the user pools endpoints, with a user whose profile is *local* to your user pool. A local user exists exclusively in your user pool directory without federation through an external IdP. If you link their federated identity to a local user in an [AdminLinkProviderForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.html) API request, they can sign in with the user pools API. For more information, see [Linking federated users to an existing user profile](cognito-user-pools-identity-federation-consolidate-users.md).

The Amazon Cognito user pools API is dual-purpose.

1. It creates and configures your Amazon Cognito user pools resources. For example, you can create user pools, add AWS Lambda triggers, and configure the user pool domain that hosts your managed login pages.

1. It performs sign-up, sign-in and other user operations for local and linked users.

**Example scenario with the Amazon Cognito user pools API**

1. Your user selects a "Create an account" button that you created in your app. They enter an email address and password.

1. Your app sends a [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html) API request and creates a new user in your user pool.

1. Your app prompts your user for an email confirmation code. Your users enters the code they received in an email message.

1. Your app sends a [ConfirmSignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.html) API request with the user's confirmation code.

1. Your app prompts your user for their username and password, and they enter their information.

1. Your app sends an [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html) API request and stores an ID token, access token, and refresh token. Your app calls OIDC libraries to manage your user's tokens and maintain a persistent session for that user.

In the Amazon Cognito user pools API, you can't sign in users who federate through an IdP. You must authenticate these users through your user pool endpoints. For more information about the user pool endpoints that include managed login, see [User pool endpoints and managed login reference](cognito-userpools-server-contract-reference.md).

Your federated users can start in managed login and select their IdP, or you can skip managed login and send your users directly to your IdP to sign in. When your API request to the [Authorize endpoint](authorization-endpoint.md) includes an IdP parameter, Amazon Cognito silently redirects your user to the IdP sign-in page.

**Example scenario with managed login pages**

1. Your user selects a "Create an account" button that you created in your app.

1. Managed login presents your user with a list of the social identity providers where you have registered developer credentials. Your user chooses Apple.

1. Your app initiates a request to the [Authorize endpoint](authorization-endpoint.md) with provider name `SignInWithApple`.

1. Your user's browser opens the Apple authentication page. Your user signs in and chooses to authorize Amazon Cognito to read their profile information.

1. Amazon Cognito confirms the Apple access token and queries your user's Apple profile.

1. Your user presents an Amazon Cognito authorization code to your app.

1. The OIDC library in your application exchanges the authorization code with the [Token endpoint](token-endpoint.md) and stores an ID token, access token, and refresh token issued by the user pool. Your app uses OIDC libraries to manage your user's tokens and maintain a persistent session for that user.

The user pools API and managed login pages support a variety of scenarios, described throughout this guide. The following sections examine how the user pools API further divides into classes that support your sign-up, sign-in, and resource-management requirements.

## List of API operations grouped by authorization model
<a name="user-pool-apis-auth-unauth"></a>

The Amazon Cognito user pools API, both a resource-management interface and a user-facing authentication and authorization interface, combines the authorization models that follow in its operations. Depending on the API operation, you might have to provide authorization with IAM credentials, an access token, a session token, a client secret, or a combination of these. For many user authentication and authorization operations, you have a choice of authenticated and unauthenticated versions of the request. Unauthenticated operations are best security practice for apps that you distribute to your users, like mobile apps; you don't need to include any secrets in your code.

You can only assign permissions in IAM policies for [IAM-authorized management operations](#user-pool-apis-auth-unauth-sigv4-management) and [IAM-authorized user operations](#user-pool-apis-auth-unauth-sigv4-user).

### IAM-authorized management operations
<a name="user-pool-apis-auth-unauth-sigv4-management"></a>

IAM-authorized management operations modify and view your user pool and app client configuration, like you would do in the AWS Management Console. 

For example, to modify your user pool in an [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html) API request, you must present AWS credentials and IAM permissions to update the resource.

To authorize these requests in the AWS Command Line Interface (AWS CLI) or an AWS SDK, configure your environment with environment variables or client configuration that adds IAM credentials to your request. For more information, see [Accessing AWS using your AWS credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) in the *AWS General Reference*. You can also send requests directly to the [service endpoints](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html) for the Amazon Cognito user pools API. You must authorize, or *sign*, these requests with AWS credentials that you embed in the header of your request. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html).


| IAM-authorized management operations | 
| --- |
| [AddCustomAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AddCustomAttributes.html) | 
| [CreateGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateGroup.html) | 
| [CreateIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html) | 
| [CreateResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateResourceServer.html) | 
| [CreateUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserImportJob.html) | 
| [CreateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html) | 
| [CreateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html) | 
| [CreateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.html) | 
| [DeleteGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteGroup.html) | 
| [DeleteIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteIdentityProvider.html) | 
| [DeleteResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteResourceServer.html) | 
| [DeleteUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPool.html) | 
| [DeleteUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClient.html) | 
| [DeleteUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolDomain.html) | 
| [DescribeIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.html) | 
| [DescribeResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeResourceServer.html) | 
| [DescribeRiskConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeRiskConfiguration.html) | 
| [DescribeUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserImportJob.html) | 
| [DescribeUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html) | 
| [DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html) | 
| [DescribeUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolDomain.html) | 
| [GetCSVHeader](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetCSVHeader.html) | 
| [GetGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetGroup.html) | 
| [GetIdentityProviderByIdentifier](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetIdentityProviderByIdentifier.html) | 
| [GetSigningCertificate](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetSigningCertificate.html) | 
| [GetUICustomization](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUICustomization.html) | 
| [GetUserPoolMfaConfig](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserPoolMfaConfig.html) | 
| [ListGroups](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListGroups.html) | 
| [ListIdentityProviders](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListIdentityProviders.html) | 
| [ListResourceServers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListResourceServers.html) | 
| [ListTagsForResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListTagsForResource.html) | 
| [ListUserImportJobs](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserImportJobs.html) | 
| [ListUserPoolClients](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClients.html) | 
| [ListUserPools](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPools.html) | 
| [ListUsers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsers.html) | 
| [ListUsersInGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsersInGroup.html) | 
| [SetRiskConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetRiskConfiguration.html) | 
| [SetUICustomization](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUICustomization.html) | 
| [SetUserPoolMfaConfig](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.html) | 
| [StartUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StartUserImportJob.html) | 
| [StopUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StopUserImportJob.html) | 
| [TagResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_TagResource.html) | 
| [UntagResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UntagResource.html) | 
| [UpdateGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateGroup.html) | 
| [UpdateIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.html) | 
| [UpdateResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateResourceServer.html) | 
| [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html) | 
| [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html) | 
| [UpdateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.html) | 

### IAM-authorized user operations
<a name="user-pool-apis-auth-unauth-sigv4-user"></a>

IAM-authorized user operations sign up, sign in, manage credentials for, modify, and view your users. 

For example, you can have a server-side application tier that backs a web front end. Your server-side app is an OAuth confidential client that you trust with privileged access to your Amazon Cognito resources. To register a user in the app, your server can include AWS credentials in an [AdminCreateUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.html) API request. For more information about OAuth client types, see [Client Types](https://www.rfc-editor.org/rfc/rfc6749#section-2.1) in *The OAuth 2.0 Authorization Framework*.

To authorize these requests in the AWS CLI or an AWS SDK, configure your server-side app environment with environment variables or client configuration that adds IAM credentials to your request. For more information, see [Accessing AWS using your AWS credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) in the *AWS General Reference*. You can also send requests directly to the [service endpoints](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html) for the Amazon Cognito user pools API. You must authorize, or *sign*, these requests with AWS credentials that you embed in the header of your request. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html).

If your app client has a client secret, you must provide both your IAM credentials and, depending on the operation, either the `SecretHash` parameter or the `SECRET_HASH` value in `AuthParameters`. For more information, see [Computing secret hash values](signing-up-users-in-your-app.md#cognito-user-pools-computing-secret-hash).


| IAM-authorized user operations | 
| --- |
| [AdminAddUserToGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminAddUserToGroup.html) | 
| [AdminConfirmSignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.html) | 
| [AdminCreateUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.html) | 
| [AdminDeleteSoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteSoftwareToken.html) | 
| [AdminDeleteUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteUser.html) | 
| [AdminDeleteUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteUserAttributes.html) | 
| [AdminDisableProviderForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDisableProviderForUser.html) | 
| [AdminDisableUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDisableUser.html) | 
| [AdminEnableUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminEnableUser.html) | 
| [AdminForgetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminForgetDevice.html) | 
| [AdminGetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.html) | 
| [AdminGetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.html) | 
| [AdminGetUserAuthFactors](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUserAuthFactors.html) | 
| [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html) | 
| [AdminLinkProviderForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.html) | 
| [AdminListDevices](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.html) | 
| [AdminListGroupsForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListGroupsForUser.html) | 
| [AdminListUserAuthEvents](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListUserAuthEvents.html) | 
| [AdminRemoveUserFromGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRemoveUserFromGroup.html) | 
| [AdminResetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.html) | 
| [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html) | 
| [AdminSetUserMFAPreference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserMFAPreference.html) | 
| [AdminSetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.html) | 
| [AdminSetUserSettings](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserSettings.html) | 
| [AdminUpdateAuthEventFeedback](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateAuthEventFeedback.html) | 
| [AdminUpdateDeviceStatus](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateDeviceStatus.html) | 
| [AdminUpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.html) | 
| [AdminUserGlobalSignOut](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.html) | 

### Unauthenticated user operations
<a name="user-pool-apis-auth-unauth-unauth"></a>

Unauthenticated user operations sign up, sign in, and initiate password resets for your users. Use unauthenticated, or *public*, API operations when you want anyone on the internet to sign up and sign in to your app.

For example, to register a user in your app, you can distribute an OAuth public client that doesn't provide any privileged access to secrets. You can register this user with the unauthenticated API operation [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html).

To send these requests in a public client that you developed with an AWS SDK, you don't need to configure any credentials. You can also send requests directly to the [service endpoints](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html) for the Amazon Cognito user pools API with no additional authorization.

If your app client has a client secret, you must provide, depending on the operation, either the `SecretHash` parameter or the `SECRET_HASH` value in `AuthParameters`. For more information, see [Computing secret hash values](signing-up-users-in-your-app.md#cognito-user-pools-computing-secret-hash).


| Unauthenticated user operations | 
| --- |
| [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html) | 
| [ConfirmSignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.html) | 
| [ResendConfirmationCode](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ResendConfirmationCode.html) | 
| [ForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.html) | 
| [ConfirmForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.html) | 
| [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html) | 

### Token-authorized user operations
<a name="user-pool-apis-auth-unauth-token-auth"></a>

Token-authorized user operations sign out, manage credentials for, modify, and view your users after they have signed in or begun the sign-in process. Use token-authorized API operations when you don't want to distribute secrets in your app, and you want to authorize requests with your user's own credentials. If your user has completed sign-in, you must authorize their token-authorized API request with an access token. If your user is in the middle of a sign-in process, you must authorize their token-authorized API request with a session token that Amazon Cognito returned in the response to the previous request.

For example, in a public client, you might want to update a user's profile in a way that restricts the write access to the user's own profile only. To make this update, your client can include the user's access token in a [UpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.html) API request.

To send these requests in a public client that you developed with an AWS SDK, you don't need to configure any credentials. Include an `AccessToken` or `Session` parameter in your request. You can also send requests directly to the [service endpoints](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html) for the Amazon Cognito user pools API. To authorize a request to a service endpoint, include the access or session token in the POST body of your request.

To sign an API request for a token-authorized operation, include the access token as an `Authorization` header in your request, in the format `Bearer {{<Base64-encoded access token>}}`.


| Token-authorized user operations | AccessToken | Session | 
| --- |--- |--- |
| [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html) |  | ✓ | 
| [ChangePassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ChangePassword.html) | ✓ |  | 
| [GetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUser.html) | ✓ |  | 
| [StartWebAuthnRegistration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StartWebAuthnRegistration.html) | ✓ |  | 
| [CompleteWebAuthnRegistration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CompleteWebAuthnRegistration.html) | ✓ |  | 
| [DeleteWebAuthnCredential](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteWebAuthnCredential.html) | ✓ |  | 
| [ListWebAuthnCredentials](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListWebAuthnCredentials.html) | ✓ |  | 
| [UpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.html) | ✓ |  | 
| [DeleteUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserAttributes.html) | ✓ |  | 
| [DeleteUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUser.html) | ✓ |  | 
| [ConfirmDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.html) | ✓ |  | 
| [ForgetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ForgetDevice.html) | ✓ |  | 
| [GetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetDevice.html) | ✓ |  | 
| [ListDevices](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListDevices.html) | ✓ |  | 
| [UpdateDeviceStatus](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateDeviceStatus.html) | ✓ |  | 
| [GetUserAttributeVerificationCode](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserAttributeVerificationCode.html) | ✓ |  | 
| [VerifyUserAttribute](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifyUserAttribute.html) | ✓ |  | 
| [SetUserSettings](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserSettings.html) | ✓ |  | 
| [SetUserMFAPreference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserMFAPreference.html) | ✓ |  | 
| [GlobalSignOut](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.html) | ✓ |  | 
| [UpdateAuthEventFeedback](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateAuthEventFeedback.html) |  | ✓ | 
| [AssociateSoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AssociateSoftwareToken.html) | ✓ | ✓ | 
| [VerifySoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifySoftwareToken.html) | ✓ | ✓ | 
| [RevokeToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RevokeToken.html)¹ |  |  | 
| [GetTokensFromRefreshToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.html)¹ |  |  | 

¹ `RevokeToken` and `GetTokensFromRefreshToken` take refresh tokens as the authorization parameter. The refresh token serves as the authorizing token, and as the target resource.