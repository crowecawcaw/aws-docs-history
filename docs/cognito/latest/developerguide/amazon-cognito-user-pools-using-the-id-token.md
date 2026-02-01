# Understanding the identity (ID)

token

The ID token is a [JSON Web Token
(JWT)](https://tools.ietf.org/html/rfc7519 "https://tools.ietf.org/html/rfc7519") that contains claims about the identity of the authenticated user, such as
`name`, `email`, and `phone_number`. You can use this
identity information inside your application. The ID token can also be used to authenticate
users to your resource servers or server applications. You can also use an ID token outside of
the application with your web API operations. In those cases, you must verify the signature of
the ID token before you can trust any claims inside the ID token. See [Verifying JSON web
tokens](amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md "amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md").

You can set the ID token expiration to any value between 5 minutes and 1 day. You can set
this value per app client.

###### Important

When your user signs in with managed login, Amazon Cognito sets session cookies that are valid
for 1 hour. If you use managed login for authentication in your application, and specify a
minimum duration of less than 1 hour for your access and ID tokens, your users will still
have a valid session until the cookie expires. If the user has tokens that expire during the
one-hour session, the user can refresh their tokens without the need to
reauthenticate.

## ID Token Header

The header contains two pieces of information: the key ID (`kid`), and the
algorithm (`alg`).

```
{
"kid" : "1234example=",
"alg" : "RS256"
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

## ID token default payload

This is a example payload from an ID token. It contains claims about the authenticated
user. For more information about OpenID Connect (OIDC) standard claims, see the list of
[OIDC
standard claims](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims "http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims"). You can add claims of your own design with a [Pre token generation Lambda
trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md").

```
`<header>`.{
    "sub": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "cognito:groups": [
        "test-group-a",
        "test-group-b",
        "test-group-c"
    ],
    "email_verified": true,
    "cognito:preferred_role": "arn:aws:iam::111122223333:role/my-test-role",
    "iss": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_example",
    "cognito:username": "my-test-user",
    "middle_name": "Jane",
    "nonce": "abcdefg",
    "origin_jti": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "cognito:roles": [
        "arn:aws:iam::111122223333:role/my-test-role"
    ],
    "aud": "xxxxxxxxxxxxexample",
    "identities": [
        {
            "userId": "amzn1.account.EXAMPLE",
            "providerName": "LoginWithAmazon",
            "providerType": "LoginWithAmazon",
            "issuer": null,
            "primary": "true",
            "dateCreated": "1642699117273"
        }
    ],
    "event_id": "64f513be-32db-42b0-b78e-b02127b4f463",
    "token_use": "id",
    "auth_time": 1676312777,
    "exp": 1676316377,
    "iat": 1676312777,
    "jti": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "email": "my-test-user@example.com"
}
.`<token signature>`
```

**`sub`**

A unique identifier ([UUID](cognito-terms.md#terms-uuid "cognito-terms.md#terms-uuid")), or subject, for the
authenticated user. The username might not be unique in your user pool. The
`sub` claim is the best way to identify a given user.

**`cognito:groups`**

An array of the names of user pool groups that have your user as a member. Groups
can be an identifier that you present to your app, or they can generate a request for
a preferred IAM role from an identity pool.

**`cognito:preferred_role`**

The ARN of the IAM role that you associated with your user's highest-priority
user pool group. For more information about how your user pool selects this role
claim, see [Assigning precedence values to
groups](cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups "cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups").

**`iss`**

The identity provider that issued the token. The claim has the following
format.

`https://cognito-idp.`<Region>`.amazonaws.com/`<your
 user pool ID>``

**`cognito:username`**

The username of your user in your user pool.

**`nonce`**

The `nonce` claim comes from a parameter of the same name that you can
add to requests to your OAuth 2.0 `authorize` endpoint. When you add the
parameter, the `nonce` claim is included in the ID token that Amazon Cognito issues,
and you can use it to guard against replay attacks. If you do not provide a
`nonce` value in your request, Amazon Cognito automatically generates and
validates a nonce when you authenticate through a third-party identity provider, then
adds it as a `nonce` claim to the ID token. The implementation of the
`nonce` claim in Amazon Cognito is based on [OIDC
standards](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation "https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation").

**`origin_jti`**

A token-revocation identifier associated with your user's refresh token. Amazon Cognito
references the `origin_jti` claim when it checks if you revoked your user's
token with the [Revoke endpoint](revocation-endpoint.md "revocation-endpoint.md") or the [RevokeToken](../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md") API operation. When you revoke a token, Amazon Cognito invalidates all
access and ID tokens with the same `origin_jti` value.

**`cognito:roles`**

An array of the names of the IAM roles associated with your user's groups. Every
user pool group can have one IAM role associated with it. This array represents all
IAM roles for your user's groups, regardless of precedence. For more information, see
[Adding groups to a user pool](cognito-user-pools-user-groups.md "cognito-user-pools-user-groups.md").

**`aud`**

The user pool app client that authenticated your user. Amazon Cognito renders the same
value in the access token `client_id` claim.

**`identities`**

The contents of the user's `identities` attribute. The attribute
contains information about each third-party identity provider profile that you've
linked to a user, either by federated sign-in or by [linking a
federated user to a local profile](cognito-user-pools-identity-federation-consolidate-users.md "cognito-user-pools-identity-federation-consolidate-users.md"). This information contains their provider
name, their provider unique ID, and other metadata.

**`token_use`**

The intended purpose of the token. In an ID token, its value is
`id`.

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

The ID token can contain OIDC standard claims that are defined in [OIDC standard
claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims "https://openid.net/specs/openid-connect-core-1_0.html#Claims"). The ID token can also contain custom attributes that you define in your
user pool. Amazon Cognito writes custom attribute values to the ID token as strings regardless of
attribute type.

###### Note

User pool custom attributes are always prefixed with `custom:`.

## ID Token Signature

The signature of the ID token is calculated based on the header and payload of the JWT
token. Before you accept the claims in any ID token that your app receives, verify the
signature of the token. For more information, see Verifying a JSON Web Token. [Verifying JSON web
tokens](amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md "amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md").
