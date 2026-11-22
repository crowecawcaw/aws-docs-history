

# Exchanging tokens for downstream services

Token exchange is an OAuth 2.0 extension, defined in [RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html) on the RFC Editor website, that trades an existing token for a new token. With Amazon Cognito user pools, when your service receives a request from a user, it can exchange the user's token for a new token. The new token is narrowed in scope and bound to the audience of a specific downstream service. Your service doesn't forward the user's original token, which might be broader than the downstream service needs or intended for a different audience.

Amazon Cognito performs token exchange with the [GetDerivedToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetDerivedToken.html) API operation. You can call `GetDerivedToken` directly with the AWS SDK, or through the [Token endpoint](token-endpoint.md) with a token-exchange grant. Token exchange is well suited to service-to-service and agent-based scenarios where one service acts on a user's behalf when it calls another.

## How token exchange works
<a name="cognito-user-pools-token-exchange-about"></a>

In a token exchange, your application presents a *subject token* – the existing token that represents the user – and Amazon Cognito returns a new *issued token* for a downstream service. You can optionally present an *actor token* that represents the service that performs the exchange. The issued token is a standard Amazon Cognito access token or ID token that the downstream service validates the same way it validates any user pool token.

Token exchange is a feature of user pools on the Essentials or Plus feature plan. For more information about feature plans, see [User pool feature plans](cognito-sign-in-feature-plans.md).

### When to use token exchange
<a name="cognito-user-pools-token-exchange-when"></a>

Use token exchange when your service must call a downstream service on a user's behalf and you want the downstream call to carry a token that is appropriately scoped and audience-bound, rather than the user's original token. Common scenarios include the following.
+ **Service-to-service delegation** – A service receives a request from a user and must call a backend service with a token that is narrowed to only the access that the backend requires.
+ **Agent-based access** – An agent or intermediary acts on a user's behalf and the downstream service must be able to distinguish a request that the user made directly from a request that an agent made for the user.
+ **Audience binding** – You want to issue a token that targets a specific resource server rather than a general-purpose token.

### Impersonation and delegation
<a name="cognito-user-pools-token-exchange-impersonation-delegation"></a>

Token exchange supports two semantics. You choose between them on each request by whether you include an actor token.

**Impersonation**  
When you don't include an actor token, Amazon Cognito issues a token that represents the user acting directly, with no `act` claim. A downstream service can't distinguish the request from one that you made as the user directly.

**Delegation**  
When you include an actor token, Amazon Cognito issues a token that carries an `act` (actor) claim, as defined in RFC 8693. The `act` claim identifies the intermediary that is acting on the user's behalf and contains identity claims only. A downstream service can inspect the `act` claim to apply policies specific to the intermediary. It can also record in audit logs that an intermediary, not you acting as the user directly, made the request.

To learn where the `act` claim appears in an access token, see [Access token default payload](amazon-cognito-user-pools-using-the-access-token.md#user-pool-access-token-payload).

### Security model
<a name="cognito-user-pools-token-exchange-security"></a>

Token exchange is designed so that an exchanged token can never grant more access than the user's original token, and can't outlive the credential that it was derived from.

**Down-scoping only**  
The scopes in the issued token are the intersection of three sets: the scopes you request, the scopes in the subject token, and the scopes the app client is allowed to issue. Token exchange can never add a scope that the subject token didn't already carry. For example, if you request scopes A and B but the subject token carries only A, the issued token includes only A.

**No refresh token**  
A token exchange never issues a refresh token. The issued token is short lived and expires on its own, so an exchanged token can't be used to mint new tokens after the original credential is no longer valid.

**Subject token validation**  
Amazon Cognito validates the subject token's signature and expiration, and checks it for revocation, for example from a global sign-out. The user that the subject token represents must be enabled and confirmed.

**Audience and resource**  
You can bind the issued token to a single audience and a single resource. Amazon Cognito validates each against a registered resource server in your user pool.

**Note**  
Amazon Cognito doesn't currently issue or evaluate the RFC 8693 `may_act` claim, which an original token issuer would use to declare in advance which actors can act on a subject's behalf.

### Accepted subject and actor tokens
<a name="cognito-user-pools-token-exchange-token-sources"></a>

A subject token or actor token can be a token that Amazon Cognito issued, or a token from an external identity provider (IdP) that is already registered on your user pool, either OIDC or SAML 2.0. When you present a token from a registered external IdP, you also provide the name of the provider so that Amazon Cognito validates the token against the correct provider configuration.

A subject or actor that you resolve through a registered external IdP must already exist as a linked user in your user pool. Token exchange doesn't create a new user. If no linked user exists, the exchange fails. Amazon Cognito issues access tokens and ID tokens as output. It can't issue SAML tokens.

### Related token methods
<a name="cognito-user-pools-token-exchange-related"></a>

Token exchange derives a user token for a downstream service. It is distinct from machine-to-machine (M2M) authorization, which authorizes an application rather than a user. For M2M access tokens from a client credentials grant or the `GetClientToken` operation, see [Machine-to-machine (M2M) authorization](cognito-user-pools-define-resource-servers.md#cognito-user-pools-define-resource-servers-about-m2m). Because token exchange issues no refresh token, plan your token caching accordingly. For more information, see [Managing user pool token expiration and caching](amazon-cognito-user-pools-using-tokens-caching-tokens.md).

## Configure and perform a token exchange
<a name="cognito-user-pools-token-exchange-configure"></a>

To perform a token exchange, complete the following steps.

1. Configure an app client with the token-exchange authentication flows that match the semantics you want: `ALLOW_TOKEN_EXCHANGE_IMPERSONATION`, `ALLOW_TOKEN_EXCHANGE_DELEGATION`, or both.

1. Call `GetDerivedToken` through the token endpoint or with the AWS SDK.

1. Amazon Cognito returns the issued token for the downstream service.

### Prerequisites
<a name="cognito-user-pools-token-exchange-prerequisites"></a>
+ Your user pool is on the Essentials or Plus feature plan.
+ Your app client has the token-exchange authentication flows that match the semantics you want: `ALLOW_TOKEN_EXCHANGE_IMPERSONATION` for impersonation, `ALLOW_TOKEN_EXCHANGE_DELEGATION` for delegation, or both. For more information about app client authentication flows, see [Application-specific settings with app clients](user-pool-settings-client-apps.md).
+ Token exchange is enabled for your account. If the feature isn't enabled, the operation returns an `OperationNotEnabledException`.
+ Any audience or resource value that you request corresponds to a resource server that is registered in your user pool. For more information, see [Scopes, M2M, and resource servers](cognito-user-pools-define-resource-servers.md).
+ To exchange a token from a registered external IdP, the IdP is registered on your user pool, the subject or actor is already a linked user, and you supply the provider name with the token.
+ To exchange a token through the token endpoint, your user pool has a domain. To call `GetDerivedToken` with the SDK, no domain is required.

### Exchange a token with the token endpoint
<a name="cognito-user-pools-token-exchange-endpoint"></a>

To exchange a token at the [Token endpoint](token-endpoint.md), make an HTTP POST request to `/oauth2/token` with a `Content-Type` of `application/x-www-form-urlencoded`. Authenticate your app client in the same way as other token-endpoint grants, with `client_secret_basic` or `client_secret_post`. Set `grant_type` to the token-exchange grant `urn:ietf:params:oauth:grant-type:token-exchange`. The token-type parameters use the RFC 8693 URN values, for example `urn:ietf:params:oauth:token-type:access_token`.

```http
POST /oauth2/token HTTP/1.1
Host: {{example-domain.auth.us-west-2.amazoncognito.com}}
Content-Type: application/x-www-form-urlencoded
Authorization: Basic {{Base64Encoded(client_id:client_secret)}}

grant_type=urn:ietf:params:oauth:grant-type:token-exchange&
subject_token={{eyJra456defEXAMPLE}}&
subject_token_type=urn:ietf:params:oauth:token-type:access_token&
audience={{solar-system-data}}&
scope={{solar-system-data/asteroids.add}}
```

The preceding request uses the following parameters.

**grant\_type**  
The token-exchange grant URN, `urn:ietf:params:oauth:grant-type:token-exchange`.

**subject\_token**  
The existing token that represents the user, which Amazon Cognito exchanges for the issued token.

**subject\_token\_type**  
The RFC 8693 token-type URN of the subject token, for example `urn:ietf:params:oauth:token-type:access_token`.

**audience**  
The resource server that the issued token targets.

**scope**  
The scopes that you request for the issued token, down-scoped from the subject token.

To perform delegation, add the `actor_token` and `actor_token_type` parameters. For a subject or actor token from a registered external IdP, add `subject_token_provider_name` or `actor_token_provider_name`. These two provider-name parameters are Amazon Cognito extensions and aren't part of RFC 8693. For the full list of request parameters, see [GetDerivedToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetDerivedToken.html) in the *Amazon Cognito user pools API Reference*.

### Exchange a token with the AWS SDK
<a name="cognito-user-pools-token-exchange-sdk"></a>

To exchange a token with the SDK, call the `GetDerivedToken` operation. The request requires `ClientId`, `SubjectToken`, and `SubjectTokenType`. A confidential app client also supplies `ClientSecret`. To perform delegation, include `ActorToken` and `ActorTokenType`. The following example requests an impersonation exchange of an access token.

```json
{
    "ClientId": "{{1example23456789}}",
    "ClientSecret": "{{exampleClientSecret123EXAMPLE}}",
    "SubjectToken": "{{eyJra456defEXAMPLE}}",
    "SubjectTokenType": "ACCESS_TOKEN",
    "Audiences": [ "{{solar-system-data}}" ],
    "Scopes": [ "{{solar-system-data/asteroids.add}}" ]
}
```

The preceding request uses the following fields.

**ClientId**  
The ID of the app client that performs the exchange.

**ClientSecret**  
The client secret, required for a confidential app client.

**SubjectToken**  
The existing token that represents the user.

**SubjectTokenType**  
The type of the subject token, for example `ACCESS_TOKEN`.

**Audiences**  
The resource servers that the issued token targets.

**Scopes**  
The scopes that you request for the issued token.

For the complete request and response contract, see [GetDerivedToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetDerivedToken.html) in the *Amazon Cognito user pools API Reference*. For a delegation example, see [Example token exchanges](#cognito-user-pools-token-exchange-examples).

### Customize the exchanged token with a Lambda trigger
<a name="cognito-user-pools-token-exchange-lambda"></a>

Token exchange invokes the pre token generation Lambda trigger if you have configured one for your user pool. The trigger runs with a `triggerSource` of `TokenGeneration_TokenExchange`, which your function can check to apply logic that is specific to token exchange. Your function can add, suppress, or override claims, suppress scopes, or deny the exchange by returning an error. Your function can't add scopes. Amazon Cognito removes any scope that isn't in the exchange's requested or default scope set. The function receives the resolved user's attributes. It doesn't receive the raw subject or actor token strings. For more information, see [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md).

### Example token exchanges
<a name="cognito-user-pools-token-exchange-examples"></a>

The following examples show the output of an impersonation exchange and a delegation exchange.

An impersonation exchange returns a token that represents the user and has no `act` claim. The following is a `/oauth2/token` response.

```json
{
    "access_token": "{{eyJra456defEXAMPLE}}",
    "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
    "token_type": "Bearer",
    "expires_in": 3600
}
```

A delegation exchange returns a token whose decoded payload includes an `act` claim that identifies the intermediary. The following shows the decoded payload of an issued access token:

```json
{
    "sub": "{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
    "token_use": "access",
    "scope": "{{solar-system-data/asteroids.add}}",
    "aud": "{{solar-system-data}}",
    "act": {
        "sub": "{{service-a-client-id}}"
    },
    "exp": 1735689600,
    "iat": 1735686000
}
```