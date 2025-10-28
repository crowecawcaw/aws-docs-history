# Using PKCE in authorization code

grants

Amazon Cognito supports Proof Key for Code Exchange (PKCE) authentication in authorization code
grants. PKCE is an extension to the OAuth 2.0 authorization code grant
for public clients. PKCE guards against the redemption of intercepted authorization
codes.

## How Amazon Cognito uses PKCE

To start authentication with PKCE, your application must generate a unique string
value. This string is the code verifier, a secret value that Amazon Cognito uses to compare
the client requesting the initial authorization grant to the client exchanging the
authorization code for tokens.

Your app must apply an SHA256 hash to the code verifier string and encode the
result to base64. Pass the hashed string to the [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md") as a
`code_challenge` parameter in the request body. When your app
exchanges the authorization code for tokens, it must include the code verifier
string in plaintext as a `code_verifier` parameter in the request body to
the [Token endpoint](token-endpoint.md "token-endpoint.md"). Amazon Cognito performs
the same hash-and-encode operation on the code verifier. Amazon Cognito only returns ID,
access, and refresh tokens if it determines that the code verifier results in the
same code challenge that it received in the authorization request.

###### To implement Authorization Grant Flow with PKCE

1. Open the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list, or create a user pool. If you
   create a user pool, you will be prompted to set up an app client and
   configure managed login during the wizard.
   1. If you create a new user pool, set up an app client and configure
      managed login during the guided setup.
   2. If you configure an existing user pool, add a [domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md") and a
      [public app
      client](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md"), if you haven’t already.

4. Generate a random alphanumeric string, typically a universally unique
   identifier ([UUID](cognito-terms.md#terms-uuid "cognito-terms.md#terms-uuid")), to create a code
   challenge for the PKCE. This string is the value of the
   `code_verifier` parameter that you will submit in your
   request to the [Token endpoint](token-endpoint.md "token-endpoint.md").
5. Hash the `code_verifier` string with the SHA256 algorithm.
   Encode the result of the hashing operation to base64. This string is the
   value of the `code_challenge` parameter that you will submit in
   your request to the [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md").

The following Python example generates a
`code_verifier` and calculates the
`code_challenge`:

```
#!/usr/bin/env python3

import random
from base64 import urlsafe_b64encode
from hashlib import sha256
from string import ascii_letters
from string import digits

# use a cryptographically strong random number generator source
rand = random.SystemRandom()

code_verifier = ''.join(rand.choices(ascii_letters + digits, k=128))
code_verifier_hash = sha256(code_verifier.encode()).digest()
code_challenge = urlsafe_b64encode(code_verifier_hash).decode().rstrip('=')

print(f"code challenge: {code_challenge}")
print(f"code verifier: {code_verifier}")
```

The following is an example output from the Python
script:

```
code challenge: Eh0mg-OZv7BAyo-tdv_vYamx1boOYDulDklyXoMDtLg
code verifier: 9D-aW_iygXrgQcWJd0y0tNVMPSXSChIc2xceDhvYVdGLCBk-JWFTmBNjvKSdOrjTTYazOFbUmrFERrjWx6oKtK2b6z_x4_gHBDlr4K1mRFGyE8yA-05-_v7Dxf3EIYJH
```

6. Complete managed login sign-in with an authorization code grant request
   with PKCE. The following is an example URL:

```
https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/authorize?response_type=code&client_id=`1example23456789`&redirect_uri=`https://www.example.com`&code_challenge=`Eh0mg-OZv7BAyo-tdv_vYamx1boOYDulDklyXoMDtLg`&code_challenge_method=S256
```

7. Collect the authorization `code` and redeem it for tokens with
   the token endpoint. The following is an example request:

```
POST /oauth2/token HTTP/1.1
Host: `mydomain.auth.us-east-1.amazoncognito.com`
Content-Type: application/x-www-form-urlencoded
Content-Length: 296

redirect_uri=`https%3A%2F%2Fwww.example.com`&
client_id=`1example23456789`&
code=`7378f445-c87f-400c-855e-0297d072ff03`&
grant_type=authorization_code&
code_verifier=`9D-aW_iygXrgQcWJd0y0tNVMPSXSChIc2xceDhvYVdGLCBk-JWFTmBNjvKSdOrjTTYazOFbUmrFERrjWx6oKtK2b6z_x4_gHBDlr4K1mRFGyE8yA-05-_v7Dxf3EIYJH`
```

8. Review the response. It will contain ID, access, and refresh tokens. For
   more information about using Amazon Cognito user pool tokens, see [Understanding
   user pool JSON web tokens (JWTs)](amazon-cognito-user-pools-using-tokens-with-identity-providers.md "amazon-cognito-user-pools-using-tokens-with-identity-providers.md").
