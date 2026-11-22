

# Application-specific settings with app clients

A user pool app client is a configuration within a user pool that interacts with one mobile or web application that authenticates with Amazon Cognito. App clients can call authenticated and unauthenticated API operations, and read or modify some or all of your users' attributes. Your app must identify itself to the app client in operations to register, sign in, and handle forgotten passwords. These API requests must include self-identification with an app client ID, and authorization with an optional client secret. You must secure any app client IDs or secrets so that only authorized client apps can call these unauthenticated operations. Additionally, if you configure your app to sign authenticated API requests with AWS credentials, you must secure your credentials against user inspection.

You can create multiple apps for a user pool. An app client might be linked to the code platform of an app, or a separate tenant in your user pool. For example, you might create an app for a server-side application and a different Android app. Each app has its own app client ID.

You can apply settings for the following user pool features at the app client level:

1. [Analytics](cognito-user-pools-pinpoint-integration.md)

1. [Managed login](cognito-user-pools-managed-login.md) IdPs, grant types, callback URLs, and customization

1. [Resource servers and custom scopes](cognito-user-pools-define-resource-servers.md)

1. [Threat protection](cognito-user-pool-settings-threat-protection.md)

1. [Attribute read and write permissions](user-pool-settings-attributes.md#user-pool-settings-attribute-permissions-and-scopes)

1. [Token expiration and revocation](amazon-cognito-user-pools-using-tokens-with-identity-providers.md)

1. [Authentication flows](authentication.md#amazon-cognito-user-pools-authentication-flow)

## App client types
<a name="user-pool-settings-client-app-client-types"></a>

When you create an app client in Amazon Cognito, you can pre-populate options based on the standard OAuth client types **public client** and **confidential client**. Configure a **confidential client** with a **client secret**. For more information about client types, see [IETF RFC 6749 \#2.1](https://datatracker.ietf.org/doc/html/rfc6749#section-2.1).

**Public client**  
A public client runs in a browser or on a mobile device. Because it does not have trusted server-side resources, it does not have a client secret.

**Confidential client**  
A confidential client has server-side resources that can be trusted with a **client secret** for unauthenticated API operations. The app might run as a daemon or shell script on your back-end server.

**Client secret**  
A client secret, or client password, is a fixed string that your app must use in all API requests to the app client. Your app client must have a client secret to perform `client_credentials` grants. For more information, see [IETF RFC 6749 \#2.3.1](https://datatracker.ietf.org/doc/html/rfc6749#section-2.3.1).  
Each app client can have up to two secrets at a time, enabling secret rotation without downtime. When you create an app client, you can either let Amazon Cognito generate a secret value or provide your own custom secret value. You can't change secrets after you create an app. You can add a second secret with the [AddUserPoolClientSecret](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AddUserPoolClientSecret.html) API operation to rotate secrets. When you add a secret, you can either let Amazon Cognito generate a secret value or provide your own custom secret value. To delete a secret, use the [DeleteUserPoolClientSecret](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClientSecret.html) API operation. You cannot delete the only secret associated with an app client. You can also delete an app to block access from apps that use that app client ID.  
For a Cognito-generated client secret, you can have Amazon Cognito manage it in AWS Secrets Manager. You don't have to handle the raw secret value yourself. Amazon Cognito stores and rotates the secret in Secrets Manager. Your app retrieves the current value from Secrets Manager at runtime. Standard Secrets Manager charges apply. For more information, see [Managing app client secrets with AWS Secrets Manager](#user-pool-settings-client-apps-asm-managed-secrets).
The Amazon Cognito console creates app clients with client secrets when you select the **Traditional web application** and **Machine-to-machine application** options for application type. Choose one of these options to generate a client secret, or create the client programmatically with [CreateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html) and set `GenerateSecret` to `true`.
You can't change whether an app client has a client secret after you create the app client. The [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html) operation can't add or remove a client secret. To change this configuration, create a new app client. You don't need to recreate the user pool, and your other app clients aren't affected.

You can use a confidential client, and a client secret, with a public app. Use an Amazon CloudFront proxy to add a `SECRET_HASH` in transit. For more information, see [Protect public clients for Amazon Cognito by using an Amazon CloudFront proxy](https://aws.amazon.com/blogs/security/protect-public-clients-for-amazon-cognito-by-using-an-amazon-cloudfront-proxy/) on the AWS blog.

### Managing app client secrets with AWS Secrets Manager
<a name="user-pool-settings-client-apps-asm-managed-secrets"></a>

For an app client with a generated client secret, you can have Amazon Cognito manage the secret in AWS Secrets Manager. Amazon Cognito stores the secret as a [managed secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html), which is a secret that an AWS service creates and manages for you. Amazon Cognito creates, rotates, and deletes the secret. Secrets Manager starts each rotation on a schedule, and Amazon Cognito performs the rotation with no downtime. Your app reads the current value from Secrets Manager when it needs the secret.

Amazon Cognito doesn't return the raw secret value in API responses for a managed secret.

**Important**  
Storing and rotating app client secrets in Secrets Manager incurs standard Secrets Manager charges. For more information about pricing, see [AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing/).

**Important**  
The following rules apply to managed client secrets.  
You can't provide your own custom secret value and set `PublishSecretsInAWSSecretsManager` to `true` in the same request. Doing so fails with an `InvalidInputException`.
You can't call [AddUserPoolClientSecret](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AddUserPoolClientSecret.html) or [DeleteUserPoolClientSecret](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClientSecret.html) for a managed client. These operations fail with an `InvalidInputException`, because Amazon Cognito manages secret rotation for you.
You can't recover the Secrets Manager secret after you delete a managed app client. Amazon Cognito deletes the secret right away, with no recovery window.

Use the following options to manage your app client's secret:

**Turn on managed secrets**  
To have Amazon Cognito publish the client secret to Secrets Manager, set `PublishSecretsInAWSSecretsManager` to `true`. You can set this parameter when you create a client with [CreateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html) (together with `GenerateSecret` set to `true`), or when you update a client that already has a generated secret with [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html).  
In API requests, this parameter defaults to `false`. If you don't set `PublishSecretsInAWSSecretsManager`, Amazon Cognito doesn't manage the secret in Secrets Manager and returns the plaintext `ClientSecret` value as before. In the Amazon Cognito console, the **Store secret in AWS Secrets Manager - recommended** option is turned on by default when you create an app client with a generated client secret.  
When managed secrets are turned on, the response contains a `ClientSecretArn` instead of the plaintext `ClientSecret` value. `ClientSecretArn` is the Amazon Resource Name (ARN) of the secret in Secrets Manager. An app client can have up to two secrets at a time for rotation. Secrets Manager stores both of them in the same secret, so a managed client has a single `ClientSecretArn`.  
When you turn on managed secrets for an existing app client, Amazon Cognito copies the client's secrets into Secrets Manager. Amazon Cognito then starts the first rotation right away. If the client has one secret, that secret keeps working until the next rotation, which is 7 days later by default. If the client has two secrets, the first rotation deletes the older one.  
Before you turn on managed secrets for an existing app client, make sure that your app uses the newer secret. Then update your app to read the secret from Secrets Manager before the next rotation.

**Retrieve the secret value**  
[DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html) returns the `ClientSecretArn` for a managed client and doesn't return the raw secret value. To read the current secret, retrieve it from Secrets Manager by its ARN with the [GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) operation. The following JSON object shows the contents of `SecretString`:  

```json
{
  "userPoolId": "us-east-1_EXAMPLE",
  "userPoolClientId": "1example23456789",
  "clientSecretValue": "example-client-secret"
}
```
Use the value of `clientSecretValue` as the app client secret. The `userPoolId` and `userPoolClientId` values identify the user pool and app client that the secret belongs to. For more information, see [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the *AWS Secrets Manager User Guide*.

**Rotate the secret**  
By default, Amazon Cognito rotates a managed client secret every 7 days. The first rotation starts as soon as you turn on managed secrets. Rotation has no downtime and requires no Lambda function of your own.  
To use a different schedule, change the rotation schedule of the secret in Secrets Manager. For more information, see [Managed rotation for AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html) in the *AWS Secrets Manager User Guide*.  
Each rotation adds a new secret and makes it the current value in Secrets Manager. The previous secret keeps working until the next rotation, when Amazon Cognito deletes it. A secret value that your app reads stays valid for one to two rotation intervals, depending on when in the rotation cycle your app reads it. With the default schedule, the value stays valid for 7 to 14 days.  
Read the secret from Secrets Manager when your app starts, and refresh any cached copy more often than the secret rotates. If Amazon Cognito can't verify the secret in an authentication request, read the secret from Secrets Manager again and retry the request.

**Encrypt the secret with your own KMS key**  
By default, Secrets Manager encrypts the managed secret with the Secrets Manager AWS managed key (`aws/secretsmanager`). This is true even if you encrypt your user pool with a customer managed key. To control the key that encrypts the secret, for example to apply your own key policy or grants, you can re-encrypt the secret with a customer managed AWS KMS key that you own. This key protects only the copy of the secret in Secrets Manager, which your application reads. Amazon Cognito keeps its own copy of the secret with the rest of your user pool data, so changing the Secrets Manager key doesn't change how Amazon Cognito verifies the secret. For more information about how Amazon Cognito encrypts user pool data, see [Data protection in Amazon Cognito](data-protection.md).  
Amazon Cognito uses the key through the Amazon Cognito service-linked role (`AWSServiceRoleForAmazonCognitoIdp`) when it rotates or replicates the secret, not with your credentials. Authorize that role in the *key policy* of your KMS key, not through an IAM policy on the role. Amazon Cognito creates the service-linked role in your account when you turn on managed secrets, so turn on managed secrets before you update the key policy.  
The key policy needs a statement for the Amazon Cognito service-linked role and a statement for each application role that reads the secret. The service-linked role needs its permissions to rotate the secret and to replicate it to replica Regions. Your application's role needs `kms:Decrypt` because Secrets Manager decrypts the secret with your application's credentials when your application calls [GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html). The following example key policy contains both statements and a statement that lets your account administer the key. Replace the example account ID, Region, and role name with your own values.  

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Allow administrators to manage the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:{{aws}}:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "AllowCognitoToUseKeyForManagedClientSecret",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:{{aws}}:iam::{{111122223333}}:role/aws-service-role/cognito-idp.amazonaws.com/AWSServiceRoleForAmazonCognitoIdp"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "secretsmanager.{{us-east-1}}.amazonaws.com"
                },
                "StringLike": {
                    "kms:EncryptionContext:SecretARN": "arn:{{aws}}:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:cognito-idp!*"
                }
            }
        },
        {
            "Sid": "AllowApplicationToDecryptManagedClientSecret",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:{{aws}}:iam::{{111122223333}}:role/{{MyApplicationRole}}"
            },
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "secretsmanager.{{us-east-1}}.amazonaws.com"
                },
                "StringLike": {
                    "kms:EncryptionContext:SecretARN": "arn:{{aws}}:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:cognito-idp!*"
                }
            }
        }
    ]
}
```
If your key already has a key policy, add the two Amazon Cognito statements to it. Don't remove the statements that give your account access to the key.  
Without the application statement, your application's `GetSecretValue` call fails with an `AccessDeniedException` error, even if the application has `secretsmanager:GetSecretValue` permission.  
After the key policy is in place, call the Secrets Manager [UpdateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecret.html) operation and pass your key in the `KmsKeyId` parameter. Secrets Manager encrypts later secret versions with the key that you set, including the versions that managed rotation creates.  
If the key becomes unavailable, for example because you disable it, delete it, or remove a statement from its key policy, then retrieving the secret from Secrets Manager and managed rotation both fail until you restore access. During that time, an app that doesn't already have the secret can't get it from Secrets Manager, so it can't authenticate with Amazon Cognito.

**Use managed secrets with multi-Region replication**  
If your user pool has replicas in other AWS Regions, Amazon Cognito replicates the managed secret to each replica Region with Secrets Manager replication. Your apps in a replica Region can read the replica of the secret from Secrets Manager in that Region. For more information about replica user pools, see [Multi-Region replication for user pools](user-pool-multi-region.md).  
Secrets Manager encrypts each replica with the AWS managed key (`aws/secretsmanager`) in the replica Region, even if the primary secret uses a customer managed KMS key. If the primary secret uses a customer managed KMS key, its key policy must allow the Amazon Cognito service-linked role to use `kms:Decrypt`, as in the example key policy. Otherwise, Secrets Manager can't replicate new secret versions, and the replicas keep an old secret value that stops working after later rotations.

**Turn off managed secrets**  
To stop managing the secret in Secrets Manager, set `PublishSecretsInAWSSecretsManager` to `false` on [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html). Amazon Cognito migrates the secret value back into Amazon Cognito, returns the plaintext `ClientSecret` again, and deletes the secret in Secrets Manager right away, with no recovery window. After that, your apps can't read the secret from Secrets Manager. Get the secret with [DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html) and update your apps to use it.

**Note**  
To retrieve the current secret, you need `secretsmanager:GetSecretValue` permission for the secret. If the secret uses a customer managed KMS key, you also need `kms:Decrypt` permission for the key.

**Note**  
Managing the client secret in Secrets Manager is independent of refresh token rotation. Managed secret storage applies to the app client's static secret. Refresh token rotation applies to your users' per-session refresh tokens. You can turn on both features. When your app client refreshes tokens under rotation, it still supplies its client secret as usual. Managing that secret in Secrets Manager doesn't change the refresh request.

## JSON web tokens
<a name="user-pool-settings-client-app-token-types"></a>

Amazon Cognito app clients can issue JSON web tokens (JWTs) of the following types.

**Identity (ID) token**  
A verifiable statement that your user is authenticated from your user pool. OpenID Connect (OIDC) added the [ID token specification](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) to the access and refresh token standards defined by OAuth 2.0. The ID token contains identity information, like user attributes, that your app can use to create a user profile and provision resources. See [Understanding the identity (ID) token](amazon-cognito-user-pools-using-the-id-token.md) for more information.

**Access token**  
A verifiable statement of your user's access rights. The access token contains [scopes](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3), a feature of OIDC and OAuth 2.0. Your app can present scopes to back-end resources and prove that your user pool authorized a user or machine to access data from an API, or their own user data. An access token with *custom scopes*, often from an M2M client-credentials grant, authorizes access to a resource server. See [Understanding the access token](amazon-cognito-user-pools-using-the-access-token.md) for more information.

**Refresh token**  
An encrypted statement of initial authentication that your app can present to your user pool when your user's tokens expire. A refresh-token request returns new, unexpired access and ID tokens. See [Refresh tokens](amazon-cognito-user-pools-using-the-refresh-token.md) for more information.

You can set the expiration of these tokens for each app client from the **App clients** menu of your user pool in the [Amazon Cognito console](https://console.aws.amazon.com/cognito/v2/idp/user-pools).

## App client terms
<a name="cognito-user-pools-app-idp-settings-about"></a>

The following terms are available properties of app clients in the Amazon Cognito console.

**Allowed callback URLs**  
A callback URL indicates where the user is redirected after a successful sign-in. Choose at least one callback URL. The callback URL must:  
+ Be an absolute URI.
+ Be pre-registered with a client.
+ Not include a fragment component.
See [OAuth 2.0 - redirection endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).  
Amazon Cognito requires `HTTPS` over `HTTP` except for `http://localhost`, `http://127.0.0.1`, and `http://[::1]` for testing purposes only.  
For loopback hosts, Amazon Cognito accepts any port at runtime. This exception applies only to `localhost`, `127.0.0.1`, and `[::1]`. When a registered callback URL points to one of these hosts, Amazon Cognito accepts a runtime `redirect_uri` on that host with any port. A port in the registered URL doesn't restrict the runtime port: if you register `http://localhost:3000/redirect`, Amazon Cognito also accepts `http://localhost:124/redirect` at runtime. This behavior supports clients that run locally and bind a port at runtime. It applies to app clients, CIMD clients, and dynamic client registration clients. Other hosts require an exact match to a registered callback URL.  
App callback URLs such as `myapp://example` are also supported.

**Allowed sign out URLs**  
A sign-out URL indicates where your user is to be redirected after signing out.

**Attribute read and write permissions**  
Your user pool might have many customers, each with their own app client and IdPs. You can configure your app client to have read and write access to only those user attributes that are relevant to the app. In cases like machine-to-machine (M2M) authorization, you can grant access to none of your user attributes.  

**Considerations for attribute read and write permissions configuration**
+ When you create an app client and don't customize attribute read and write permissions, Amazon Cognito grants read and write permissions to all user pool attributes.
+ You can grant write access to immutable [custom attributes](user-pool-settings-attributes.md#user-pool-settings-custom-attributes.title). Your app client can write values to immutable attributes when you create or sign up a user. After this, you can't write values to any immutable custom attributes for the user.
+ App clients must have write access to required attributes in your user pool. The Amazon Cognito console automatically sets required attributes as writeable.
+ You can't permit an app client to have write access to `email_verified` or `phone_number_verified`. A user pool administrator can modify these values. A user can only change the value of these attributes through [attribute verification](signing-up-users-in-your-app.md#allowing-users-to-sign-up-and-confirm-themselves.title).

**Authentication flows**  
The methods that your app client allows for sign-in. Your app can support authentication with username and password, email and SMS message OTPs, passkey authenticators, custom authentication with Lambda triggers, and token refresh. As a best security practice, use SRP authentication for username and password authentication in custom-built applications.

**Custom scopes**  
A custom scope is one that you define for your own resource server in the **Resource Servers**. The format is {{resource-server-identifier}}/{{scope}}. See [Scopes, M2M, and resource servers](cognito-user-pools-define-resource-servers.md).

**Default redirect URI**  
Replaces the `redirect_uri` parameter in authentication requests for users with third-party IdPs. Configure this app client setting with the `DefaultRedirectURI` parameter of a [CreateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html) or [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html) API request. This URL must also be a member of the `CallbackURLs` for your app client. Amazon Cognito redirects authenticated sessions to this URL when:  

1. Your app client has one [identity provider](#app-client-terms-identity-provider) assigned and multiple [callback URLs](#app-client-terms-callback-urls) defined. Your user pool redirects authentication requests to the [authorization server](authorization-endpoint.md) to the default redirect URI when they don't include a `redirect_uri` parameter.

1. Your app client has one [identity provider](#app-client-terms-identity-provider) assigned and one [callback URLs](#app-client-terms-callback-urls) defined. In this scenario it's not necessary to define a default callback URL. Requests that don't include a `redirect_uri` parameter redirect to the one available callback URL.

**Identity providers**  
You can choose some or all of your user pool external identity providers (IdPs) to authenticate your users. Your app client can also authenticate only local users in your user pool. When you add an IdP to your app client, you can generate authorization links to the IdP and display it on your managed login sign-in page. You can assign multiple IdPs, but you must assign at least one. For more information on using external IdPs, see [User pool sign-in with third party identity providers](cognito-user-pools-identity-federation.md).

**OpenID Connect scopes**  
Choose one or more of the following `OAuth` scopes to specify the access privileges that can be requested for access tokens.  
+ The `openid` scope declares that you want to retrieve an ID token and a user's unique ID. It also requests all or some user attributes, depending on additional scopes in the request. Amazon Cognito doesn't return an ID token unless you request the `openid` scope. The `openid` scope authorizes structural ID token claims like expiration and key ID, and determines the user attributes that you receive in a response from the [userInfo endpoint](userinfo-endpoint.md).
  + When `openid` is the only scope that you request, Amazon Cognito populates the ID token with all user attributes that the current app client can read. The `userInfo` response to an access token with this scope alone returns all user attributes.
  + When you request `openid` with other scopes like `phone`, `email`, or `profile`, the ID token and `userInfo` return the user's unique ID and the attributes defined by the additional scopes.
+ The `phone` scope grants access to the `phone_number` and `phone_number_verified` claims. This scope can only be requested with the `openid` scope.
+ The `email` scope grants access to the `email` and `email_verified` claims. This scope can only be requested with the `openid` scope.
+ The `aws.cognito.signin.user.admin` scope grants access to [Amazon Cognito user pools API operations](authentication-flows-public-server-side.md#user-pools-API-operations) that require access tokens, such as [UpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.html) and [VerifyUserAttribute](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifyUserAttribute.html).
+ The `profile` scope grants access to all user attributes that are readable by the client. This scope can only be requested with the `openid` scope.
For more information about scopes, see the list of [standard OIDC scopes](http://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims).

**OAuth grant types**  
An OAuth grant is a method of authentication that retrieves user-pool tokens. Amazon Cognito supports the following types of grants. To integrate these OAuth grants in your app, you must add a domain to your user pool.  
**Authorization code grant**  
The authorization code grant generates a code that your app can exchange for user pool tokens with the [Token endpoint](token-endpoint.md). When you exchange an authorization code, your app receives ID, access, and refresh tokens. This OAuth flow, like the implicit grant, happens in your users' browsers. An authorization code grant is the most secure grant that Amazon Cognito offers, because tokens aren't visible in your users' sessions. Instead, your app generates the request that returns tokens and can cache them in protected storage. For more information, see *Authorization code* in [IETF RFC 6749 \#1.3.1](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1)
As a best security practice in public-client apps, activate only the authorization-code grant OAuth flow, and implement Proof Key for Code Exchange (PKCE) to restrict token exchange. With PKCE, a client can only exchange an authorization code when they have provided the token endpoint with the same secret that was presented in the original authentication request. For more information on PKCE, see [IETF RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636).
**Implicit grant**  
The implicit grant delivers an access and ID token, but not refresh token, to your user's browser session directly from the [Authorize endpoint](authorization-endpoint.md). An implicit grant removes the requirement for a separate request to the token endpoint, but isn't compatible with PKCE and doesn't return refresh tokens. This grant accommodates testing scenarios and app architecture that can't complete authorization-code grants. For more information, see *Implicit grant* in [IETF RFC 6749 \#1.3.2](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.2). You can activate both the authorization-code grant and the implicit grant in an app client, and then use each grant as needed.
**Client credentials grant**  
The client credentials grant is for machine-to-machine (M2M) communications. Authorization-code and implicit grants issue tokens to authenticated human users. Client credentials grant scope-based authorization from a non-interactive system to an API. Your app can request client credentials directly from the token endpoint and receive an access token. For more information, see *Client Credentials* in [IETF RFC 6749 \#1.3.4](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.4). You can only activate client-credentials grants in app clients that have a client secret and that don't support authorization-code or implicit grants. As an alternative that requires no user pool domain, an app client with a client secret and the `ALLOW_CLIENT_TOKEN_AUTH` authentication flow can obtain M2M access tokens with the [GetClientToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetClientToken.html) API operation.
Because you don't invoke the client credentials flow as a user, this grant can only add *custom* scopes to access tokens. A custom scope is one that you define for your own resource server. Default scopes like `openid` and `profile` don't apply to nonhuman users.  
Because ID tokens are a validation of user attributes, they aren't relevant to M2M communication, and a client credentials grant doesn't issue them. See [Scopes, M2M, and resource servers](cognito-user-pools-define-resource-servers.md).
Client credentials grants add costs to your AWS bill. For more information, see [Amazon Cognito Pricing](https://aws.amazon.com/cognito/pricing).

## Creating an app client
<a name="cognito-user-pools-app-idp-settings-console-create"></a>

Applications can also register their own app clients with dynamic client registration. For more information, see [Dynamic client registration](cognito-user-pools-dynamic-client-registration.md).

------
#### [ AWS Management Console ]

**To create an app client (console)**

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home). If prompted, enter your AWS credentials.

1. Choose **User Pools**.

1. Choose an existing user pool from the list, or create a user pool. Both options prompt you to configure an app client with application-specific settings.

1. Choose an **Application type** that reflects your application architecture.
**Important**  
Your **Application type** selection also sets defaults for other app client settings, including whether Amazon Cognito generates a client secret. The **Traditional web application** and **Machine-to-machine application** types generate a client secret. For more information, see [App client types](#user-pool-settings-client-app-client-types).

1. **Name your application** with a friendly identifier.

1. Enter a **Return URL**.

1. Choose **Create app client**. You can change advanced options after you create your app client.

1. Amazon Cognito returns you to app client details. To access example code for your application, select a platform from the **Quick setup guide** tab.

------
#### [ AWS CLI ]

```
aws cognito-idp create-user-pool-client --user-pool-id {{MyUserPoolID}} --client-name {{myApp}}
```

**Note**  
Use JSON format for callback and logout URLs to prevent the CLI from treating them as remote parameter files:  

```
--callback-urls "["{{https://example.com}}"]"
--logout-urls "["{{https://example.com}}"]"
```

See the AWS CLI command reference for more information: [create-user-pool-client](https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/create-user-pool-client.html)

------
#### [ Amazon Cognito user pools API ]

Generate a [CreateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html) API request. You must specify a value for all parameters that you don't want set to a default value.

------

## Updating a user pool app client (AWS CLI and AWS API)
<a name="cognito-user-pools-app-idp-settings-cli-api-update-user-pool-client"></a>

At the AWS CLI, enter the following command:

```
aws cognito-idp update-user-pool-client --user-pool-id  "{{MyUserPoolID}}" --client-id "{{MyAppClientID}}" --allowed-o-auth-flows-user-pool-client --allowed-o-auth-flows "code" "implicit" --allowed-o-auth-scopes "openid" --callback-urls "["{{https://example.com}}"]" --supported-identity-providers "["MySAMLIdP", "LoginWithAmazon"]"
```

If the command is successful, the AWS CLI returns a confirmation:

```json
{
    "UserPoolClient": {
        "ClientId": "{{MyClientID}}",
        "SupportedIdentityProviders": [
            "LoginWithAmazon",
            "MySAMLIdP"
        ],
        "CallbackURLs": [
            "{{https://example.com}}"
        ],
        "AllowedOAuthScopes": [
            "openid"
        ],
        "ClientName": "Example",
        "AllowedOAuthFlows": [
            "implicit",
            "code"
        ],
        "RefreshTokenValidity": 30,
        "AuthSessionValidity": 3,
        "CreationDate": 1524628110.29,
        "AllowedOAuthFlowsUserPoolClient": true,
        "UserPoolId": "{{MyUserPoolID}}",
        "LastModifiedDate": 1530055177.553
    }
}
```

See the AWS CLI command reference for more information: [update-user-pool-client](https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/update-user-pool-client.html).

AWS API: [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html)

## Getting information about a user pool app client (AWS CLI and AWS API)
<a name="cognito-user-pools-app-idp-settings-cli-api-describe-user-pool-client"></a>

```
aws cognito-idp describe-user-pool-client --user-pool-id {{MyUserPoolID}} --client-id {{MyClientID}}
```

See the AWS CLI command reference for more information: [describe-user-pool-client](https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/describe-user-pool-client.html).

AWS API: [DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html)

## Listing all app client information in a user pool (AWS CLI and AWS API)
<a name="cognito-user-pools-app-idp-settings-cli-api-list-user-pool-clients"></a>

```
aws cognito-idp list-user-pool-clients --user-pool-id "{{MyUserPoolID}}" --max-results 3
```

See the AWS CLI command reference for more information: [list-user-pool-clients](https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/list-user-pool-clients.html).

AWS API: [ListUserPoolClients](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClients.html)

## Deleting a user pool app client (AWS CLI and AWS API)
<a name="cognito-user-pools-app-idp-settings-cli-api-delete-user-pool-client"></a>

```
aws cognito-idp delete-user-pool-client --user-pool-id "{{MyUserPoolID}}" --client-id "{{MyAppClientID}}"
```

See the AWS CLI command reference for more information: [delete-user-pool-client](https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/delete-user-pool-client.html)

AWS API: [DeleteUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClient.html)