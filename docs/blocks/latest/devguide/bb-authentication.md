

# Authentication
<a name="bb-authentication"></a>

This section covers Blocks for user identity and session management, from simple username/password to federated OIDC providers.

## Choosing an authentication Block
<a name="_choosing_an_authentication_block"></a>


| Block | Best for | Avoid when | 
| --- | --- | --- | 
|  `AuthBasic`  | Prototypes, internal tools, MVPs with simple username/password auth | You need social login, MFA, or enterprise federation | 
|  `AuthCognito`  | Production apps needing social sign-in, MFA, SAML, passkeys, OAuth/OIDC | You only need simple credential-based auth (higher setup complexity) | 
|  `AuthOIDC`  | Social login with Google, GitHub, Okta, or any OIDC-compliant provider | You need full user management (signup, password reset) — use AuthCognito instead | 

## AuthBasic
<a name="bb-auth-basic"></a>

Username/password authentication with JWT sessions. Handles user signup, signin, signout, password hashing (bcrypt), HTTP-only cookie sessions, and optional email-confirmed signup. Provides a `createApi()` method that generates the auth API endpoints needed by the Authenticator UI component.

Locally, AuthBasic stores user records in memory. On AWS, it provisions a DynamoDB table for user records and issues JWTs for session management. Best for prototypes, internal tools, and MVPs where you need simple credential-based auth.

For more information, see [bb-auth-basic on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-auth-basic).

## AuthOIDC
<a name="bb-auth-oidc"></a>

OIDC sign-in with Google, GitHub, Okta, Auth0, Microsoft Entra, or any OIDC-compliant provider. Configure one or more providers with their client credentials and AuthOIDC handles the OAuth redirect flow, token exchange, and session management automatically.

Locally, AuthOIDC simulates the OAuth flow for development. On AWS, it runs a real OAuth redirect flow with session cookies. Best for applications that need social login or enterprise SSO without the complexity of Cognito.

For more information, see [bb-auth-oidc on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-auth-oidc).

## AuthCognito
<a name="bb-auth-cognito"></a>

Production-grade authentication powered by Amazon Cognito. Supports social sign-in, MFA (SMS, TOTP, email OTP), user pool groups, SAML federation, passkeys, and account recovery. Same auth interface as AuthBasic (`requireAuth`, `getCurrentUser`, `createApi`) so you can swap providers without changing application code.

Locally, AuthCognito simulates auth flows. On AWS, it provisions a Cognito User Pool with your configured options. Best for production applications that need enterprise-grade auth features.

For more information, see [bb-auth-cognito on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-auth-cognito).