# User claims passing and signature verification in

Verified Access

After an AWS Verified Access instance authenticates a user successfully, it sends the user claims
received from the IdP to the Verified Access endpoint. The user claims are signed so that applications
can verify the signatures and also verify that the claims were sent by Verified Access. During this
process, the following HTTP header is added:

`x-amzn-ava-user-context`

This header contains the user claims in JSON web token (JWT) format. The JWT format
includes a header, payload, and signature that are base64 URL encoded. Verified Access uses ES384 (ECDSA
signature algorithm using SHA-384 hash algorithm) to generate the JWT signature.

Applications can use these claims for personalization or other user specific experiences. Application developers should educate themselves regarding the level of uniqueness and verification of each claim provided by the identity provider before use. In general, the `sub` claim is the best way to identify a given user.

###### Contents

- [JWT for OIDC user claims](#oidc-sample "#oidc-sample")
- [JWT for IAM Identity Center user claims](#IdC-sample "#IdC-sample")
- [Public keys](#public-keys "#public-keys")
- [Retrieving and decoding JWT](#sample-code "#sample-code")

## Example: Signed JWT for OIDC user claims

The following examples demonstrate what the header and payload for OIDC user claims
will look like in the JWT format.

Example header:

```
{
   "alg": "ES384",
   "kid": "12345678-1234-1234-1234-123456789012",
   "signer": "arn:aws:ec2:us-east-1:123456789012:verified-access-instance/vai-abc123xzy321a2b3c",
   "iss": "OIDC Issuer URL",
   "exp": "expiration" (120 secs)
}
```

Example payload:

```
{
   "sub": "xyzsubject",
   "email": "xxx@amazon.com",
   "email_verified": true,
   "groups": [
      "Engineering",
      "finance"
   ],
   "additional_user_context": {
      "aud": "xxx",
      "exp": 1000000000,
      "groups": [
         "group-id-1",
         "group-id-2"
      ],
      "iat": 1000000000,
      "iss": "https://oidc-tp.com/",
      "sub": "xyzsubject",
      "ver": "1.0"
   }
}
```

## Example: Signed JWT for IAM Identity Center user claims

The following examples demonstrate what the header and payload for IAM Identity Center user claims
will look like in the JWT format.

###### Note

For IAM Identity Center, only user information will be included in the claims.

Example header:

```
{
   "alg": "ES384",
   "kid": "12345678-1234-1234-1234-123456789012",
   "signer": "arn:aws:ec2:us-east-1:123456789012:verified-access-instance/vai-abc123xzy321a2b3c",
   "iss": "arn:aws:ec2:us-east-1:123456789012:verified-access-trust-provider/vatp-abc123xzy321a2b3c",
   "exp": "expiration" (120 secs)
}
```

Example payload:

```
{
    "user": {
        "user_id": "f478d4c8-a001-7064-6ea6-12423523",
        "user_name": "test-123",
        "email": {
            "address": "test@amazon.com",
            "verified": false
        }
    }
}
```

## Public keys

Because Verified Access instances do not encrypt user claims, we recommend that you configure
Verified Access endpoints to use HTTPS. If you configure your Verified Access endpoint to use HTTP, be sure to
restrict the traffic to the endpoint using security groups.

To ensure security, you must verify the signature before doing any authorization based
on the claims, and validate that the `signer` field in the JWT header contains
the expected Verified Access instance ARN.

To get the public key, get the key ID from the JWT header and use it to look up the
public key from the endpoint.

The endpoint for each AWS Region is as follows:

`https://public-keys.prod.verified-access.<region>.amazonaws.com/<key-id>`

## Example: Retrieving and decoding JWT

The following code example shows how to get the key ID, public key, and payload in
Python 3.9.

```
import jwt
import requests
import base64
import json

# Step 1: Validate the signer
expected_verified_access_instance_arn = 'arn:aws:ec2:`region-code`:`account-id`:verified-access-instance/`verified-access-instance-id`'

encoded_jwt = headers.dict['x-amzn-ava-user-context']
jwt_headers = encoded_jwt.split('.')[0]
decoded_jwt_headers = base64.b64decode(jwt_headers)
decoded_jwt_headers = decoded_jwt_headers.decode("utf-8")
decoded_json = json.loads(decoded_jwt_headers)
received_verified_access_instance_arn = decoded_json['signer']

assert expected_verified_access_instance_arn == received_verified_access_instance_arn, "Invalid Signer"

# Step 2: Get the key id from JWT headers (the kid field)
kid = decoded_json['kid']

# Step 3: Get the public key from regional endpoint
url = 'https://public-keys.prod.verified-access.' + region + '.amazonaws.com/' + kid
req = requests.get(url)
pub_key = req.text

# Step 4: Get the payload
payload = jwt.decode(encoded_jwt, pub_key, algorithms=['ES384'])
```
