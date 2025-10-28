# Understanding the access

token

The user pool access token contains claims about the authenticated user, a list of the
user's groups, and a list of scopes. The purpose of the access token is to authorize API
operations. Your user pool accepts access tokens to authorize user self-service operations.
For example, you can use the access token to grant your user access to add, change, or delete
user attributes.

With [OAuth 2.0
scopes](https://www.rfc-editor.org/rfc/rfc6749#section-3.3 "https://www.rfc-editor.org/rfc/rfc6749#section-3.3") in an access token, derived from the custom scopes that you add to your user
pool, you can authorize your user to retrieve information from an API. For example, Amazon API Gateway
supports authorization with Amazon Cognito access tokens. You can populate a REST API authorizer with
information from your user pool, or use Amazon Cognito as a JSON Web Token (JWT) authorizer for an HTTP
API. To generate an access token with custom scopes, you must request it through your user
pool [public
endpoints](cognito-userpools-server-contract-reference.md "cognito-userpools-server-contract-reference.md").

With the Essentials or Plus [feature
plan](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md"), you can also implement a pre token generation Lambda trigger that adds scopes to
your access tokens at runtime. For more information, see [Pre token generation Lambda
trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md").

A user's access token with the `openid` scope is permission to request more
information about your user's attributes from the [userInfo endpoint](userinfo-endpoint.md "userinfo-endpoint.md"). The amount of information from the `userInfo`
endpoint derives from the additional scopes in the access token: for example,
`profile` for all user data, `email` for their email address.

A user's access token with the `aws.cognito.signin.user.admin` scope is
permission to read and write user attributes, list authentication factors, configure
multi-factor authentication (MFA) preferences, and manage remembered devices. The level of
access to attributes that your access token grants to this scope matches the attribute
read/write permissions you assign to your app client.

The access token is a [JSON Web Token
(JWT)](https://www.rfc-editor.org/rfc/rfc7519 "https://www.rfc-editor.org/rfc/rfc7519"). The header for the access token has the same structure as the ID token. Amazon Cognito
signs access tokens with a different key from the key that signs ID tokens. The value of an
access key ID (`kid`) claim won't match the value of the `kid` claim in
an ID token from the same user session. In your app code, verify ID tokens and access tokens
independently. Don't trust the claims in an access token until you verify the signature. For
more information, see [Verifying JSON web
tokens](amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md "amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md"). You can set the access
token expiration to any value between 5 minutes and 1 day. You can set this value per app
client.

###### Important

For access and ID tokens, don't specify a minimum less than an hour if you use managed
login. Managed login sets browsers cookies that are valid for one hour. If you configure an
access token duration of less than an hour, this has no effect on the validity of the
managed login cookie and users' ability to reauthenticate without additional credentials for
one hour after initial sign-in.

## Access token header

The header contains two pieces of information: the key ID (`kid`), and the
algorithm (`alg`).

```
{
"kid" : "1234example="
"alg" : "RS256",
}
```

**`kid`**

The key ID. Its value indicates the key that was used to secure the JSON Web
Signature (JWS) of the token. You can view your user pool signing key IDs at the
`jwks_uri` endpoint.

For more information about the `kid` parameter, see the [Key
identifier (kid) header parameter](https://tools.ietf.org/html/draft-ietf-jose-json-web-key-41#section-4.5 "https://tools.ietf.org/html/draft-ietf-jose-json-web-key-41#section-4.5").

**`alg`**

The cryptographic algorithm that Amazon Cognito used to secure the access token. User pools
use an RS256 cryptographic algorithm, which is an RSA signature with SHA-256.

For more information about the `alg` parameter, see [Algorithm (alg) header parameter](https://tools.ietf.org/html/draft-ietf-jose-json-web-key-41#section-4.4 "https://tools.ietf.org/html/draft-ietf-jose-json-web-key-41#section-4.4").

## Access token default payload

This is a sample payload from an access token. For more information, see [JWT claims](https://tools.ietf.org/html/rfc7519#section-4 "https://tools.ietf.org/html/rfc7519#section-4"). You can add claims
of your own design with a [Pre token generation Lambda
trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md").

```
`<header>`.
{
   "sub":"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
   "device_key": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
   "cognito:groups":[
      "testgroup"
   ],
   "iss":"https://cognito-idp.us-west-2.amazonaws.com/us-west-2_example",
   "version":2,
   "client_id":"xxxxxxxxxxxxexample",
   "aud": "https://api.example.com",
   "origin_jti":"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
   "event_id":"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
   "token_use":"access",
   "scope":"phone openid profile resourceserver.1/appclient2 email",
   "auth_time":1676313851,
   "exp":1676317451,
   "iat":1676313851,
   "jti":"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
   "username":"my-test-user"
}
.`<token signature>`
```

**`sub`**

A unique identifier ([UUID](cognito-terms.md#terms-uuid "cognito-terms.md#terms-uuid")), or subject, for the
authenticated user. The username might not be unique in your user pool. The
`sub` claim is the best way to identify a given user.

**`cognito:groups`**

An array of the names of user pool groups that have your user as a member.

**`iss`**

The identity provider that issued the token. The claim has the following
format.

`https://cognito-idp.`us-east-1`.amazonaws.com/`us-east-1_EXAMPLE``

**`client_id`**

The user pool app client that authenticated your user. Amazon Cognito renders the same
value in the ID token `aud` claim.

**aud**

The URL of the API that the access token is intended to authorize for. Present
only if your application requested a [resource binding](cognito-user-pools-define-resource-servers.md#cognito-user-pools-resource-binding "cognito-user-pools-define-resource-servers.md#cognito-user-pools-resource-binding") from your
authorization server.

**`origin_jti`**

A token-revocation identifier associated with your user's refresh token. Amazon Cognito
references the `origin_jti` claim when it checks if you revoked your user's
token with the [Revoke endpoint](revocation-endpoint.md "revocation-endpoint.md") or the [RevokeToken](../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md") API operation. When you revoke a token, Amazon Cognito no longer
validates access and ID tokens with the same `origin_jti` value.

**`token_use`**

The intended purpose of the token. In an access token, its value is
`access`.

**`scope`**

A list of OAuth 2.0 scopes issued to the signed-in user. Scopes define the access
that the token provides to external APIs, user self-service operations, and user data
on the `userInfo` endpoint. A token from the [Token endpoint](token-endpoint.md "token-endpoint.md") can contain any scopes
that your app client supports. A token from Amazon Cognito API sign-in only contains the scope
`aws.cognito.signin.user.admin`.

**`auth_time`**

The authentication time, in Unix time format, that your user completed
authentication.

**`exp`**

The expiration time, in Unix time format, that your user's token expires.

**`iat`**

The issued-at time, in Unix time format, that Amazon Cognito issued your user's
token.

**`jti`**

The unique identifier of the JWT.

**`username`**

The user's username in the user pool.

###### More resources

- [How
  to customize access tokens in Amazon Cognito user pools](https://aws.amazon.com/blogs/security/how-to-customize-access-tokens-in-amazon-cognito-user-pools/ "https://aws.amazon.com/blogs/security/how-to-customize-access-tokens-in-amazon-cognito-user-pools/")

## Access token signature

The signature of the access token, signed with the key advertised at the
`.well-known/jwks.json` endpoint, validates the integrity of the token header
and payload. When you use access tokens to authorize access to external APIs, always
configure your API authorizer to verify this signature against the key that signed it. For
more information, see [Verifying JSON web
tokens](amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md "amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md").
