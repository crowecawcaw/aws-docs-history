

# Understanding the identity (ID) token
<a name="amazon-cognito-user-pools-using-the-id-token"></a>

The ID token is a [JSON web token (JWT)](https://tools.ietf.org/html/rfc7519) that contains claims about the identity of the authenticated user, such as `name`, `email`, and `phone_number`. You can use this identity information inside your application. The ID token can also be used to authenticate users to your resource servers or server applications. You can also use an ID token outside of the application with your web API operations. In those cases, you must verify the signature of the ID token before you can trust any claims inside the ID token. See [Verifying JSON web tokens](amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md). 

You can set the ID token expiration to any value between 5 minutes and 1 day. You can set this value per app client.

The ID token includes the `acr` and `amr` claims, which describe the authentication level that the user satisfied and the methods that they completed. These claims are part of a capability that is rolling out gradually and might not yet be available to your user pool. For more information, see [ACR and AMR token claims](cognito-user-pools-step-up-authentication.md#cognito-user-pools-step-up-token-claims).

**Important**  
When your user signs in with managed login, Amazon Cognito sets session cookies that are valid for 1 hour. If you use managed login for authentication in your application, and specify a minimum duration of less than 1 hour for your access and ID tokens, your users will still have a valid session until the cookie expires. If the user has tokens that expire during the one-hour session, the user can refresh their tokens without the need to reauthenticate.

## ID token header
<a name="user-pool-id-token-header"></a>

The header contains two pieces of information: the key ID (`kid`), and the algorithm (`alg`).

```
{
"kid" : "1234example=",
"alg" : "RS256"
}
```

**`kid`**  
The key ID. Its value indicates the key that was used to secure the JSON Web Signature (JWS) of the token. You can view your user pool signing key IDs at the `jwks_uri` endpoint.  
For more information about the `kid` parameter, see the [Key identifier (kid) header parameter](https://tools.ietf.org/html/draft-ietf-jose-json-web-key-41#section-4.5).

**`alg`**  
The cryptographic algorithm that Amazon Cognito used to secure the access token. User pools use an RS256 cryptographic algorithm, which is an RSA signature with SHA-256.  
For more information about the `alg` parameter, see [Algorithm (alg) header parameter](https://tools.ietf.org/html/draft-ietf-jose-json-web-key-41#section-4.4).

## ID token default payload
<a name="user-pool-id-token-payload"></a>

This is an example payload from an ID token. It contains claims about the authenticated user. For more information about OpenID Connect (OIDC) standard claims, see the list of [OIDC standard claims](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims). You can add claims of your own design with a [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md).

This payload is representative, not exhaustive. The set of claims in a Amazon Cognito ID token grows over time as new features add new claims, so the claims that your tokens carry can differ from this example. Treat this example as a snapshot of common claims rather than a complete, fixed list, and read [How to parse this token safely](#user-pool-id-token-parse-safely) before you write code that parses Amazon Cognito tokens.

```
{{<header>}}.{
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
.{{<token signature>}}
```

**`sub`**  
A unique identifier ([UUID](cognito-terms.md#terms-uuid)), or subject, for the authenticated user. The username might not be unique in your user pool. The `sub` claim is the best way to identify a given user.  
Amazon Cognito generates `sub` in an Amazon Cognito-specific format that doesn't conform to a specific UUID format, including RFC UUID. You shouldn't strictly validate the format of `sub`. More generally, as described in [the guidance on parsing token claims safely](#user-pool-id-token-parse-safely), read each claim as the type that this page documents and don't impose a stricter format than the documentation states.

**`cognito:groups`**  
An array of strings. Each string is the name of a user pool group that has your user as a member. Groups can be an identifier that you present to your app, or they can generate a request for a preferred IAM role from an identity pool. This claim is always an array, even when the user belongs to a single group.

**`cognito:preferred_role`**  
The ARN of the IAM role that you associated with your user's highest-priority user pool group. For more information about how your user pool selects this role claim, see [Assigning precedence values to groups](cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups).

**`iss`**  
A single string. The issuer of the token. This claim identifies the user pool that generated the token. Your application should validate that this value matches your user pool's expected issuer URL. The claim has the following format.  
`https://cognito-idp.{{<Region>}}.amazonaws.com/{{<your user pool ID>}}`  
Your user pool can use an original or updated issuer. Updated issuers host the same JWKS content in multiple Regions, resulting in improved resilience and efficiency. For more information, see [Amazon Cognito user pools as an OIDC issuer](federation-endpoints.md#user-pool-oidc-issuer).

**`cognito:username`**  
The username of your user in your user pool.

**`nonce`**  
The `nonce` claim comes from a parameter of the same name that you can add to requests to your OAuth 2.0 `authorize` endpoint. When you add the parameter, the `nonce` claim is included in the ID token that Amazon Cognito issues, and you can use it to guard against replay attacks. If you do not provide a `nonce` value in your request, Amazon Cognito automatically generates and validates a nonce when you authenticate through a third-party identity provider, then adds it as a `nonce` claim to the ID token. The implementation of the `nonce` claim in Amazon Cognito is based on [OIDC standards](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation).

**`origin_jti`**  
A token-revocation identifier associated with your user's refresh token. Amazon Cognito references the `origin_jti` claim when it checks if you revoked your user's token with the [Revoke endpoint](revocation-endpoint.md) or the [RevokeToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RevokeToken.html) API operation. When you revoke a token, Amazon Cognito invalidates all access and ID tokens with the same `origin_jti` value.

**`cognito:roles`**  
An array of strings. Each string is the ARN of an IAM role associated with one of your user's groups. Every user pool group can have one IAM role associated with it. This array represents all IAM roles for your user's groups, regardless of precedence, and is always an array even when it contains a single role. For more information, see [Adding groups to a user pool](cognito-user-pools-user-groups.md).

**`aud`**  
A single string. The user pool app client that authenticated your user. Amazon Cognito renders the same value in the access token `client_id` claim.

**`identities`**  
An array of objects. Each object describes one third-party identity provider profile that you've linked to the user, either by federated sign-in or by [linking a federated user to a local profile](cognito-user-pools-identity-federation-consolidate-users.md). Each object contains the fields `userId` (the user's unique ID at the provider), `providerName`, `providerType`, `issuer`, `primary`, and `dateCreated`. All of these fields are strings, with two serialization details to parse carefully: `primary` is the string `"true"` or `"false"`, not a JSON boolean, and `dateCreated` is a string that holds Unix time in milliseconds (for example `"1642699117273"`), not a number. The `issuer` field can be `null`. This claim is always an array, even when the user has one linked identity.

**`token_use`**  
The intended purpose of the token. In an ID token, its value is `id`.

**`auth_time`**  
A number. The authentication time, in Unix time format, when your user completed authentication.

**`exp`**  
A number. The expiration time, in Unix time format, when your user's token expires.

**`iat`**  
A number. The issued-at time, in Unix time format, when Amazon Cognito issued your user's token.

**`jti`**  
The unique identifier of the JWT.

**`email`**  
A single string. The email address of your user, when the `email` attribute is present and readable by the app client.

The ID token can contain OIDC standard claims that are defined in [OIDC standard claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims). The ID token can also contain custom attributes that you define in your user pool. Amazon Cognito writes custom attribute values to the ID token as strings regardless of attribute type.

**Note**  
User pool custom attributes are always prefixed with `custom:`. 

### How to parse this token safely
<a name="user-pool-id-token-parse-safely"></a>

The claim set in a Amazon Cognito ID token is not fixed. The claims that a token carries vary with the authentication flow, the user's group membership, and the identity provider. They also depend on the features that are enabled on your user pool. The OpenID Connect specification requires only `iss`, `sub`, `aud`, `exp`, and `iat`, and these are present in every Amazon Cognito ID token. Amazon Cognito also always adds `token_use` with the value `id`, which you should verify to confirm that you received an ID token rather than an access token. Treat every other claim as optional and conditional on how the user authenticated.

The ID token is one of several Amazon Cognito token types, and the same parsing rules apply to all of them. For more information about parsing tokens safely, see [Parse user pool tokens safely](user-pool-parse-tokens-safely.md).

### Example ID tokens by scenario
<a name="user-pool-id-token-examples"></a>

The [ID token default payload](#user-pool-id-token-payload) combines many optional claims into a single example. In practice, the claims that a token carries depend on how the user signed in. The following examples show the claim combinations that Amazon Cognito emits for four common scenarios. Each example is a decoded payload, not a signed and serialized JWT: a real token is `header.payload.signature`, base64url-encoded and RS256-signed with your user pool's key. The `sub`, user pool ID, and timestamp values are illustrative placeholders.

#### Baseline authorization-code ID token
<a name="user-pool-id-token-example-baseline"></a>

The identity token that most applications consume after they exchange an authorization code at the token endpoint. The `token_use` value of `id` distinguishes it from an access token. The `nonce` claim is present because the client sent a `nonce` parameter in the authorization request to help prevent replay attacks.

```
{
    "sub": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
    "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_ExAmPlE",
    "aud": "6o7h8i9jexampleclientid",
    "cognito:username": "my-test-user",
    "email": "my-test-user@example.com",
    "email_verified": true,
    "origin_jti": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "token_use": "id",
    "auth_time": 1759345200,
    "iat": 1759345200,
    "exp": 1759348800,
    "jti": "11112222-3333-4444-5555-666677778888",
    "nonce": "n-0S6_WzA2Mj"
}
```

#### Group and role membership
<a name="user-pool-id-token-example-groups"></a>

Amazon Cognito adds the group and role authorization claims when the user belongs to one or more user pool groups. The `cognito:groups` and `cognito:roles` claims are arrays; read them as arrays even when they contain a single element. `cognito:preferred_role` is a single string.

```
{
    "sub": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
    "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_ExAmPlE",
    "aud": "6o7h8i9jexampleclientid",
    "cognito:username": "my-test-user",
    "cognito:groups": ["admins", "beta-testers"],
    "cognito:roles": ["arn:aws:iam::111122223333:role/my-test-role"],
    "cognito:preferred_role": "arn:aws:iam::111122223333:role/my-test-role",
    "origin_jti": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "token_use": "id",
    "auth_time": 1759345200,
    "iat": 1759345200,
    "exp": 1759348800,
    "jti": "11112222-3333-4444-5555-666677778888"
}
```

#### Federated sign-in
<a name="user-pool-id-token-example-federated"></a>

A user who signed in through an external identity provider, such as a social or SAML/OIDC provider, carries the `identities` claim, which describes the external provider link.

```
{
    "sub": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
    "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_ExAmPlE",
    "aud": "6o7h8i9jexampleclientid",
    "cognito:username": "LoginWithAmazon_amzn1.account.EXAMPLE",
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
    "origin_jti": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "token_use": "id",
    "auth_time": 1759345200,
    "iat": 1759345200,
    "exp": 1759348800,
    "jti": "11112222-3333-4444-5555-666677778888"
}
```

**Note**  
Inside each `identities` object, `primary` and `dateCreated` are serialized as strings (`"true"` and `"1642699117273"`), not as a JSON boolean and number. A comparison such as `identity.primary === true` silently evaluates to false. Read `primary` as the string `"true"` or `"false"`, and `dateCreated` as a string that holds Unix time in milliseconds.

#### Authentication strength (ACR and AMR)
<a name="user-pool-id-token-example-step-up"></a>

**Note**  
Authentication levels with ACR and AMR claims is rolling out gradually. This feature might not yet be available to your user pool. If the behavior described here isn't available, check back later as the rollout continues.

When your user pool reports the authentication level that the user reached, Amazon Cognito adds the `acr` and `amr` claims. The following token is from a user who authenticated with a password and a TOTP from an authenticator app, which is the highest level. Each token contains exactly one of the possible `acr` levels. For the fixed set of levels, the factor combinations that satisfy each one, and the complete list of `amr` values, see [Authentication levels with ACR and AMR claims](cognito-user-pools-step-up-authentication.md).

```
{
    "sub": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
    "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_ExAmPlE",
    "aud": "6o7h8i9jexampleclientid",
    "cognito:username": "my-test-user",
    "acr": "urn:cognito:loa:4",
    "amr": ["pwd", "otp", "mfa"],
    "origin_jti": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "token_use": "id",
    "auth_time": 1759345200,
    "iat": 1759345200,
    "exp": 1759348800,
    "jti": "11112222-3333-4444-5555-666677778888"
}
```

Requesting an authentication level requires the Essentials or Plus feature plan. The `acr` and `amr` claims are computed by Amazon Cognito and can't be modified by a pre token generation Lambda trigger. Translating the Amazon Cognito levels to another standard, such as NIST or eIDAS, is the responsibility of your application.

## ID token signature
<a name="user-pool-id-token-signature"></a>

The signature of the ID token is calculated based on the header and payload of the JWT token. Before you accept the claims in any ID token that your app receives, verify the signature of the token. For more information, see Verifying a JSON web token. [Verifying JSON web tokens](amazon-cognito-user-pools-using-tokens-verifying-a-jwt.md).