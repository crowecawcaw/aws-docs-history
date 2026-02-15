# CWT support for CloudFront Functions

This section provides details on support for CBOR Web Tokens (CWT) in your CloudFront
Functions, which enables secure token-based authentication and authorization at CloudFront
Edge Locations. This support is provided as a module, accessible in your CloudFront
Function.

To use this module, create a CloudFront Function using JavaScript runtime 2.0 and include
the following statement in the first line of the function code:

```
import cf from 'cloudfront';
```

The methods associated to this module are accessible through (where \* is a wildcard representing the different functions present in the module):

```
cf.cwt.*
```

For more information, see [JavaScript runtime 2.0 features for
CloudFront Functions](functions-javascript-runtime-20.md "functions-javascript-runtime-20.md").

Currently, the module only support MAC0 structure with HS256 (HMAC-SHA256) algorithm with a limit of 1KB for the maximum token size.

## Token structure

This section covers the token structure that is expected by the CWT module. The module
expects the token to be correctly tagged and identifiable (e.g. COSE MAC0). Moreover, as
for the structure of the token, the module follows the standards set by [CBOR Object
Signing and Encryption (COSE) [RFC 8152]](https://datatracker.ietf.org/doc/html/rfc8152 "https://datatracker.ietf.org/doc/html/rfc8152").

```
( // CWT Tag (Tag value: 61) --- optional
    ( // COSE MAC0 Structure Tag (Tag value: 17) --- required
        [
            protectedHeaders,
            unprotectedHeaders,
            payload,
            tag,
        ]
    )
)
```

###### Example: CWT using the COSE MAC0 structure

```
61( // CWT tag
    17( // COSE_MAC0 tag
        [
            { // Protected Headers
                1: 4  // algorithm : HMAC-256-64
            },
            { // Unprotected Headers
                4: h'53796d6d6574726963323536' // kid : Symmetric key id
            },
            { // Payload
                1: "https://iss.example.com", // iss
                2: "exampleUser", // sub
                3: "https://aud.example.com", // aud
                4: 1444064944, // exp
                5: 1443944944, // nbf
                6: 1443944944, // iat
            },
            h'093101ef6d789200' // tag
        ]
    )
)
```

###### Note

The CWT tag is optional when generating tokens. However, the COSE structure
tag is required.

## validateToken() method

The function decodes and validates a CWT token using the specified key. If validation is successful, it returns the decoded CWT token. Otherwise, it throws an error. Please note that this function does no validation on the claim set.

### Request

```
cf.cwt.validateToken(token, handlerContext{key})
```

###### Parameters

**token (required)**

Encoded token for validation. This must be a JavaScript Buffer.

**handlerContext (Required)**

A JavaScript Object that stores context for the validateToken call. At
present, only the key property is supported.

**key (Required)**

Secret key for message digest computation. Can be provided either as a
string or JavaScript Buffer.

### Response

When the `validateToken()` method returns a successfully validated
token, the response from the function is a `CWTObject` in the following
format. Once decoded, all claim keys are represented as strings.

```
CWTObject {
    protectedHeaders,
    unprotectedHeaders,
    payload
}
```

### Example - Validate token with kid sent as part of the token

This example demonstrates CWT token validation, where the kid is extracted from the header. The kid is then passed into CloudFront Functions KeyValueStore to fetch the secret key used to validate the token.

```
import cf from 'cloudfront'

const CwtClaims = {
   iss: 1,
   aud: 3,
   exp: 4
}

async function handler(event) {
    try {
        let request = event.request;
        let encodedToken = request.headers['x-cwt-token'].value;
        let kid = request.headers['x-cwt-kid'].value;

        // Retrieve the secret key from the kvs
        let secretKey = await cf.kvs().get(kid);

        // Now you can use the secretKey to decode & validate the token.
        let tokenBuffer = Buffer.from(encodedToken, 'base64url');

        let handlerContext = {
           key: secretKey,
        }

        try {
            let cwtObj = cf.cwt.validateToken(tokenBuffer, handlerContext);

            // Check if token is expired
            const currentTime = Math.floor(Date.now() / 1000); // Current time in seconds
            if (cwtObj[CwtClaims.exp] && cwtObj[CwtClaims.exp] < currentTime) {
                return {
                    statusCode: 401,
                    statusDescription: 'Token expired'
                };
            }
        } catch (error) {
            return {
               statusCode: 401,
               statusDescription: 'Invalid token'
            };
         }
    } catch (error) {
        return {
            statusCode: 402,
            statusDescription: 'Token processing failed'
        };
     }
    return request;
}
```

## generateToken() method

This function generates a new CWT token using the provided payload and context settings.

### Request

```
cf.cwt.generateToken(generatorContext, payload)
```

###### Parameters

**generatorContext (Required)**

This a JavaScript Object that is used as the context for generating
the token and contains the following key value pairs:

**cwtTag (Optional)**

This value is a boolean, which if `true`
specifies the `cwtTag` should be added.

**coseTag (Required)**

Specifies the COSE tag type. Currently only supports
`MAC0`.

**key (Required)**

Secret key to compute message digest. This value can be
either a string or JavaScript `Buffer`.

**payload (Required)**

Token payload for encoding. The payload must be in
`CWTObject` format.

### Response

Returns a JavaScript Buffer containing the encoded token.

###### Example: Generate a CWT token

```
import cf from 'cloudfront';

const CwtClaims = {
    iss: 1,
    sub: 2,
    exp: 4
};

const CatClaims = {
    catu: 401,
    catnip: 402,
    catm: 403,
    catr: 404
};

const Catu = {
    host: 1,
    path: 2,
    ext: 3
};

const CatuMatchTypes = {
    prefix_match: 1,
    suffix_match: 2,
    exact_match: 3
};

const Catr = {
    renewal_method: 1,
    next_renewal_time: 2,
    max_uses: 3
};

async function handler(event) {
    try {
        const response = {
            statusCode: 200,
            statusDescription: 'OK',
            headers: {}
        };

        const commonAccessToken = {
            protected: {
                1: "5",
            },
            unprotected: {},
            payload: {
                [CwtClaims.iss]: "cloudfront-documentation",
                [CwtClaims.sub]: "cwt-support-on-cloudfront-functions",
                [CwtClaims.exp]: 1740000000,
                [CatClaims.catu]: {
                    [Catu.host]: {
                        [CatuMatchTypes.suffix_match]: ".cloudfront.net"
                    },
                    [Catu.path]: {
                        [CatuMatchTypes.prefix_match]: "/media/live-stream/cf-4k/"
                    },
                    [Catu.ext]: {
                        [CatuMatchTypes.exact_match]: [
                            ".m3u8",
                            ".ts",
                            ".mpd"
                        ]
                    }
                },
                [CatClaims.catnip]: [
                    "[IP_ADDRESS]",
                    "[IP_ADDRESS]"
                ],
                [CatClaims.catm]: [
                    "GET",
                    "HEAD"
                ],
                [CatClaims.catr]: {
                    [Catr.renewal_method]: "header_renewal",
                    [Catr.next_renewal_time]: 1750000000,
                    [Catr.max_uses]: 5
                }
            }
        };

        if (!request.headers['x-cwt-kid']) {
            throw new Error('Missing x-cwt-kid header');
        }

        const kid = request.headers['x-cwt-kid'].value;
        const secretKey = await cf.kvs().get(kid);

        if (!secretKey) {
            throw new Error('Secret key not found for provided kid');
        }

        try {
            const genContext = {
                cwtTag: true,
                coseTag: "MAC0",
                key: secretKey
            };

            const tokenBuffer = cf.cwt.generateToken(commonAccessToken, genContext);
            response.headers['x-generated-cwt-token'] = { value: tokenBuffer.toString('base64url') };

            return response;
        } catch (tokenError) {
            return {
                statusCode: 401,
                statusDescription: 'Could not generate the token'
            };
        }
    } catch (error) {
        return {
            statusCode: 402,
            statusDescription: 'Token processing failed'
        };
    }
}
```

###### Example: Refresh token based on some logic

```
import cf from 'cloudfront'

const CwtClaims = {
   iss: 1,
   aud: 3,
   exp: 4
}

async function handler(event) {
    try {
        let request = event.request;
        let encodedToken = request.headers['x-cwt-token'].value;
        let kid = request.headers['x-cwt-kid'].value;
        let secretKey = await cf.kvs().get(kid); // Retrieve the secret key from the kvs

        // Now you can use the secretKey to decode & validate the token.
        let tokenBuffer = Buffer.from(encodedToken, 'base64url');

        let handlerContext = {
           key: secretKey,
        }

        try {
            let cwtJSON = cf.cwt.validateToken(tokenBuffer, handlerContext);

            // Check if token is expired
            const currentTime = Math.floor(Date.now() / 1000); // Current time in seconds
            if (cwtJSON[CwtClaims.exp] && cwtJSON[CwtClaims.exp] < currentTime) {
                // We can regnerate the token and add 8 hours to the expiry time
                cwtJSON[CwtClaims.exp] = Math.floor(Date.now() / 1000) + (8 * 60 * 60);

                let genContext = {
                  coseTag: "MAC0",
                  key: secretKey
                }

                let newTokenBuffer = cf.cwt.generateToken(cwtJSON, genContext);
                 request.headers['x-cwt-regenerated-token'] = newTokenBuffer.toString('base64url');
            }
        } catch (error) {
            return {
               statusCode: 401,
               statusDescription: 'Invalid token'
            };
         }
    }
    catch (error) {
        return {
            statusCode: 402,
            statusDescription: 'Token processing failed'
        };
     }
    return request;
}
```
