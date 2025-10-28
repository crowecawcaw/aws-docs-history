# Verifying JSON web

tokens

JSON web tokens (JWTs) can be decoded, read, and modified easily. A modified access token
creates a risk of privilege escalation. A modified ID token creates a risk of impersonation.
Your application trusts your user pool as a token issuer, but what if a user intercepts the
token in transit? You must ensure that your application is receiving the same token that Amazon Cognito
issued.

Amazon Cognito issues tokens that use some of the integrity and confidentiality features of the
OpenID Connect (OIDC) specification. User pool tokens indicate validity with objects like the
expiration time, issuer, and digital signature. The signature, the third and final segment of
the `.`-delimited JWT, is the key component of token validation. A malicious user
can modify a token, but if your application retrieves the public key and compares the
signature, it won't match. Any application that processes JWTs from OIDC authentication must
perform this verification operation with each sign-in.

On this page, we make some general and specific recommendations for verification of JWTs.
Application development spans a variety of programming languages and platforms. Because Amazon Cognito
implements OIDC sufficiently close to the public specification, any reputable JWT library in
your developer environment of choice can handle your verification requirements.

These steps describe verifying a user pool JSON Web Token (JWT).

###### Topics

- [Prerequisites](#amazon-cognito-user-pools-using-tokens-prerequisites "#amazon-cognito-user-pools-using-tokens-prerequisites")
- [Validate tokens with
  aws-jwt-verify](#amazon-cognito-user-pools-using-tokens-aws-jwt-verify "#amazon-cognito-user-pools-using-tokens-aws-jwt-verify")
- [Understanding and
  inspecting tokens](#amazon-cognito-user-pools-using-tokens-manually-inspect "#amazon-cognito-user-pools-using-tokens-manually-inspect")

## Prerequisites

Your library, SDK, or software framework might already handle the tasks in this section.
AWS SDKs provide tools for Amazon Cognito user pool token handling and management in your app.
AWS Amplify includes functions to retrieve and refresh Amazon Cognito tokens.

For more information, see the following pages.

- [Integrating Amazon Cognito authentication and authorization with
  web and mobile apps](cognito-integrate-apps.md "cognito-integrate-apps.md")
- [Code examples for Amazon Cognito
  Identity Provider using AWS SDKs](service_code_examples.md "service_code_examples.md")
- [Advanced workflows](https://docs.amplify.aws/lib/auth/advanced/q/platform/js/#retrieve-jwt-tokens "https://docs.amplify.aws/lib/auth/advanced/q/platform/js/#retrieve-jwt-tokens") in the _Amplify Dev
  Center_

Many libraries are available for decoding and verifying a JSON Web Token (JWT). If you
want to manually process tokens for server-side API processing, or if you are using other
programming languages, these libraries can help. See the [OpenID foundation list of libraries for working
with JWT tokens](http://openid.net/developers/jwt/ "http://openid.net/developers/jwt/").

## Validate tokens with

aws-jwt-verify

In a Node.js app, AWS recommends the [aws-jwt-verify
library](https://github.com/awslabs/aws-jwt-verify "https://github.com/awslabs/aws-jwt-verify") to validate the parameters in the token that your user passes to your app.
With `aws-jwt-verify`, you can populate a `CognitoJwtVerifier` with
the claim values that you want to verify for one or more user pools. Some of the values that
it can check include the following.

- That access or ID tokens aren't malformed or expired, and have a valid
  signature.
- That access tokens came from the [correct user pools and app clients](https://github.com/awslabs/aws-jwt-verify#verifying-jwts-from-amazon-cognito "https://github.com/awslabs/aws-jwt-verify#verifying-jwts-from-amazon-cognito").
- That access token claims contain the [correct OAuth 2.0
  scopes](https://github.com/awslabs/aws-jwt-verify#checking-scope "https://github.com/awslabs/aws-jwt-verify#checking-scope").
- That the keys that signed your access and ID tokens [match a signing key
  `kid` from the _JWKS URI_ of your user
  pools](https://github.com/awslabs/aws-jwt-verify#the-jwks-cache "https://github.com/awslabs/aws-jwt-verify#the-jwks-cache").

The JWKS URI contains public information about the private key that signed your
user's token. You can find the JWKS URI for your user pool at
`https://cognito-idp.`<Region>`.amazonaws.com/`<userPoolId>`/.well-known/jwks.json`.

For more information and example code that you can use in a Node.js app or a AWS Lambda
authorizer, see [aws-jwt-verify](https://github.com/awslabs/aws-jwt-verify "https://github.com/awslabs/aws-jwt-verify") on GitHub.

## Understanding and

inspecting tokens

Before you integrate token inspection with your app, consider how Amazon Cognito assembles JWTs.
Retrieve example tokens from your user pool. Decode and examine them in detail to understand
their characteristics, and determine what you want to verify and when. For example, you
might want to examine group membership in one scenario, and scopes in another.

The following sections describe a process to manually inspect Amazon Cognito JWTs as you prepare
your app.

### Confirm the structure of

the JWT

A JSON Web Token (JWT) includes three sections with a `.` (dot) delimiter
between them.

**Header**

The key ID, `kid`, and the RSA algorithm, `alg`, that
Amazon Cognito used to sign the token. Amazon Cognito signs tokens with an `alg` of
`RS256`. The `kid` is a truncated reference to a 2048-bit
RSA private signing key held by your user pool.

**Payload**

Token claims. In an ID token, the claims include user attributes and information
about the user pool, `iss`, and app client, `aud`. In an
access token, the payload includes scopes, group membership, your user pool as
`iss`, and your app client as `client_id`.

**Signature**

The signature isn't decodable base64url like the header and payload. It's an
RSA256 identifier derived from a signing key and parameters that you can observe at
your JWKS URI.

The header and payload are base64url-encoded JSON. You can identify them by the
opening characters `eyJ` that decode to the starting character `{`.
If your user presents a base64url-encoded JWT to your app and it's not in the format
`[JSON Header].[JSON Payload].[Signature]`, it's not a valid Amazon Cognito token and
you can discard it.

The following example application verifies user pool tokens with
`aws-jwt-verify`.

```
// cognito-verify.js
// Usage example: node cognito-verify.js eyJra789ghiEXAMPLE

const { CognitoJwtVerifier } = require('aws-jwt-verify');

// Replace with your Amazon Cognito user pool ID
const userPoolId = '`us-west-2_EXAMPLE`';

async function verifyJWT(token) {
  try {
    const verifier = CognitoJwtVerifier.create({
      userPoolId,
      tokenUse: '`access`', // or 'id' for ID tokens
      clientId: '`1example23456789`', // Optional, only if you need to verify the token audience
    });

    const payload = await verifier.verify(token);
    console.log('Decoded JWT:', payload);
  } catch (err) {
    console.error('Error verifying JWT:', err);
  }
}

// Example usage
if (process.argv.length < 3) {
  console.error('Please provide a JWT token as an argument.');
  process.exit(1);
}

const MyToken = process.argv[2];
verifyJWT(MyToken);
```

### Validate the JWT

The JWT signature is a hashed combination of the header and the payload. Amazon Cognito
generates two pairs of RSA cryptographic keys for each user pool. One private key signs
access tokens, and the other signs ID tokens.

###### To verify the signature of a JWT token

1. Decode the ID token.

The OpenID Foundation also [maintains a list of libraries for working with JWT tokens](http://openid.net/developers/jwt/ "http://openid.net/developers/jwt/").

You can also use AWS Lambda to decode user pool JWTs. For more information, see
[Decode and verify Amazon Cognito JWT tokens using AWS Lambda](https://github.com/awslabs/aws-support-tools/tree/master/Cognito/decode-verify-jwt "https://github.com/awslabs/aws-support-tools/tree/master/Cognito/decode-verify-jwt"). 2. Compare the local key ID (`kid`) to the public `kid`.

    1. Download and store the corresponding public JSON Web Key (JWK) for your user
     pool. It is available as part of a JSON Web Key Set (JWKS). You can locate it by
     constructing the following `jwks_uri` URI for your environment:



    ```
    https://cognito-idp.`<Region>`.amazonaws.com/`<userPoolId>`/.well-known/jwks.json
    ```

    For more information on JWK and JWK sets, see [JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517 "https://tools.ietf.org/html/rfc7517").


    ###### Note

    Amazon Cognito might rotate signing keys in your user pool. As a best practice, cache
     public keys in your app, using the `kid` as a cache key, and refresh
     the cache periodically. Compare the `kid` in the tokens that your app
     receives to your cache.

    If you receive a token with the correct issuer but a different
     `kid`, Amazon Cognito might have rotated the signing key. Refresh the cache
     from your user pool `jwks_uri` endpoint.


    This is a sample `jwks.json` file:



    ```
    {
    	"keys": [{
    		"kid": "1234example=",
    		"alg": "RS256",
    		"kty": "RSA",
    		"e": "AQAB",
    		"n": "1234567890",
    		"use": "sig"
    	}, {
    		"kid": "5678example=",
    		"alg": "RS256",
    		"kty": "RSA",
    		"e": "AQAB",
    		"n": "987654321",
    		"use": "sig"
    	}]
    }
    ```



    **Key ID (`kid`)**

    The `kid` is a hint that indicates which key was used to
     secure the JSON Web Signature (JWS) of the token.



    **Algorithm (`alg`)**

    The `alg` header parameter represents the cryptographic
     algorithm that is used to secure the ID token. User pools use an RS256
     cryptographic algorithm, which is an RSA signature with SHA-256. For more
     information on RSA, see [RSA
     cryptography](https://tools.ietf.org/html/rfc3447 "https://tools.ietf.org/html/rfc3447").



    **Key type (`kty`)**

    The `kty` parameter identifies the cryptographic algorithm
     family that is used with the key, such as "RSA" in this example.



    **RSA exponent (`e`)**

    The `e` parameter contains the exponent value for the RSA
     public key. It is represented as a Base64urlUInt-encoded value.



    **RSA modulus (`n`)**

    The `n` parameter contains the modulus value for the RSA
     public key. It is represented as a Base64urlUInt-encoded value.



    **Use (`use`)**

    The `use` parameter describes the intended use of the public
     key. For this example, the `use` value `sig`
     represents signature.
    2. Search the public JSON Web Key for a `kid` that matches the
     `kid` of your JWT.

### Verify the claims

###### To verify JWT claims

1. By one of the following methods, verify that the token hasn't expired.
   1. Decode the token and compare the `exp` claim to the current
      time.
   2. If your access token includes an `aws.cognito.signin.user.admin`
      claim, send a request to an API like [GetUser](../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md"). API requests that you [authorize with an access token](user-pools-API-operations.md#user-pool-apis-auth-unauth "user-pools-API-operations.md#user-pool-apis-auth-unauth") return an error if your token has
      expired.
   3. Present your access token in a request to the [userInfo endpoint](userinfo-endpoint.md "userinfo-endpoint.md"). Your request
      returns an error if your token has expired.

2. The `aud` claim in an ID token and the `client_id` claim in
   an access token should match the app client ID that was created in the Amazon Cognito user
   pool.
3. The issuer (`iss`) claim should match your user pool. For example, a
   user pool created in the `us-east-1` Region will have the following
   `iss` value:

`https://cognito-idp.us-east-1.amazonaws.com/`<userpoolID>``.
4. Check the `token_use` claim.

    * If you are only accepting the access token in your web API operations, its
     value must be `access`.
    * If you are only using the ID token, its value must be `id`.
    * If you are using both ID and access tokens, the `token_use` claim
     must be either `id` or `access`.

You can now trust the claims inside the token.
