

# Control access to REST APIs using JWT authorizers

A JWT authorizer validates JSON Web Tokens (JWTs) that clients send with API requests. API Gateway performs the validation in the gateway, so you do not run a function to validate tokens. You declare the issuers that you trust, the audiences that you accept from each issuer, the signing algorithms that you allow, and any additional claims that a token must carry. Each method can then require its own authorization scopes.

JWT authorizers work with any identity provider that supports [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html) and [OAuth 2.0](https://oauth.net/2/), including Amazon Cognito user pools. For a user pool, the issuer is `https://cognito-idp.{{region}}.amazonaws.com/{{user-pool-id}}`. You can use a JWT authorizer on Regional, edge-optimized, and private REST APIs. The identity provider's OIDC discovery document, which it publishes at `/.well-known/openid-configuration`, and its key set must be reachable from the public internet, including for private APIs.

If you need custom authorization logic, such as checking claims that a JWT authorizer can't evaluate, use a Lambda authorizer. For more information, see [Use API Gateway Lambda authorizers](apigateway-use-lambda-authorizer.md).

## How a JWT authorizer validates a request
<a name="rest-api-jwt-authorizer.evaluation"></a>

API Gateway uses the following steps to authorize a request to a method that uses a JWT authorizer:

1. API Gateway reads the token from the request header that you configure as the identity source.

1. API Gateway finds the issuer configuration whose `issuer` matches the token's `iss` claim. API Gateway rejects a token from an issuer that you did not configure.

1. API Gateway verifies the token signature against the issuer's public signing keys. API Gateway finds those keys through the issuer's OIDC discovery document. For more information, see [Signing keys and troubleshooting JWT authorizers](rest-api-jwt-authorizer-keys.md).

1. API Gateway checks the `aud` claim against the audiences that you configure. For an Amazon Cognito access token, API Gateway checks the `client_id` claim instead. API Gateway also checks the `exp`, `nbf`, and `iat` claims against the current time. API Gateway allows 60 seconds of clock skew when it checks these time claims.

1. API Gateway evaluates any additional claim rules that you configure for the issuer.

1. If the method requires authorization scopes, API Gateway checks that the token's `scope` or `scp` claim contains at least one of them.

1. API Gateway makes the token's claims available to your integration in `$context.authorizer.claims`. For more information, see [Pass JWT claims to your integration](rest-api-jwt-authorizer-claims.md).

If any step fails, API Gateway rejects the request. A missing, malformed, expired, or untrusted token receives a `401 Unauthorized` response. A valid token that lacks a required scope or fails an additional claim rule receives a `403 Forbidden` response. API Gateway does not pass a rejected request to the integration.

## Supported signing algorithms
<a name="rest-api-jwt-authorizer.algorithms"></a>

A JWT authorizer supports the RS256, RS384, RS512, ES256, ES384, and ES512 signing algorithms. You set the algorithms that you allow in the `defaultAlgorithms` field, which is required. API Gateway rejects a token that is signed with an HMAC algorithm, such as HS256, and a token that uses `alg: none`.

## Choosing between JWT, Amazon Cognito, and Lambda authorizers
<a name="rest-api-jwt-authorizer.choosing"></a>

All three authorizer types control who can invoke your REST API methods. The following table compares them to help you choose.


| Authorizer type | When to use it | 
| --- | --- | 
| JWT authorizer | Use a JWT authorizer to validate tokens from one or more OIDC or OAuth 2.0 identity providers, including Amazon Cognito user pools. A single JWT authorizer can trust several issuers, each with its own audiences and claim rules. | 
| Amazon Cognito user pool authorizer | Use an Amazon Cognito user pool authorizer when your users are in Amazon Cognito user pools and you want to accept tokens from any app client in those pools without listing each client ID. | 
| Lambda authorizer | Use a Lambda authorizer when authorization needs custom logic or credentials that aren't JWTs. | 

**Topics**
+ [How a JWT authorizer validates a request](#rest-api-jwt-authorizer.evaluation)
+ [Supported signing algorithms](#rest-api-jwt-authorizer.algorithms)
+ [Choosing between JWT, Amazon Cognito, and Lambda authorizers](#rest-api-jwt-authorizer.choosing)
+ [Create a JWT authorizer for a REST API](rest-api-jwt-authorizer-create.md)
+ [Attach a JWT authorizer to methods and require scopes](rest-api-jwt-authorizer-methods.md)
+ [Update a JWT authorizer](rest-api-jwt-authorizer-update.md)
+ [Pass JWT claims to your integration](rest-api-jwt-authorizer-claims.md)
+ [Signing keys and troubleshooting JWT authorizers](rest-api-jwt-authorizer-keys.md)