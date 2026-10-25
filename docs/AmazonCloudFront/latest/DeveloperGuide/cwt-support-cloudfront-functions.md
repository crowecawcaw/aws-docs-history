

# CWT support for CloudFront Functions
<a name="cwt-support-cloudfront-functions"></a>

This section provides details on support for CBOR Web Tokens (CWT) in your CloudFront Functions, which enables secure token-based authentication and authorization at CloudFront Edge Locations. This support is provided as a module, accessible in your CloudFront Function. 

To use this module, create a CloudFront Function using JavaScript runtime 2.0 and include the following statement in the first line of the function code: 

```
import cf from 'cloudfront';
```

The methods associated with this module are accessible through (where \* is a wildcard representing the different functions present in the module):

```
cf.cwt.*
```

For more information, see [JavaScript runtime 2.0 features for CloudFront Functions](functions-javascript-runtime-20.md).

Currently, the module only supports MAC0 structure with HS256 (HMAC-SHA256) algorithm with a limit of 1 KB for the maximum token size.

## Token structure
<a name="token-structure"></a>

This section covers the token structure that is expected by the CWT module. The module expects the token to be correctly tagged and identifiable (for example COSE MAC0). For the token structure, the module follows the standards set by [CBOR Object Signing and Encryption (COSE) [RFC 8152]](https://datatracker.ietf.org/doc/html/rfc8152).

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

**Example : CWT using the COSE MAC0 structure**  

```
61( // CWT tag     
    17( // COSE_MAC0 tag       
        [         
            { // Protected Headers           
                1: 5  // algorithm         
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
            h'ac243fa30d37386146b4e559fdc56d28840c453e7caf58126e819cbc3c299b3a' // tag       
        ]     
    )   
)
```
The tag in this example is the HMAC-SHA256 of the token, computed with the example key `Symmetric256` from [RFC 8392](https://datatracker.ietf.org/doc/html/rfc8392).  
The CWT tag is optional when generating tokens. However, the COSE structure tag is required.

## validateToken() method
<a name="validatetoken-method"></a>

The function decodes and validates a CWT token using the specified key. If validation is successful, it returns the decoded CWT token. Otherwise, it throws an error.

**Important**  
`validateToken()` checks only the structure of the token and its tag. It doesn't check any claims, such as `exp`, `nbf`, or `aud`, or Common Access Token (CAT) claims, such as `catu`. Your function must check the claims that it relies on.

To check a `catu` query restriction, compare it with the unparsed query string, which `request.rawQueryString()` returns. For more information, see [`rawQueryString()` method](general-helper-methods.md#raw-query-string-method).

### Request
<a name="validatetoken-request"></a>

```
cf.cwt.validateToken(token, handlerContext)
```Parameters

**token (Required)**  
Encoded token for validation. This must be a JavaScript Buffer.

**handlerContext (Required)**  
A JavaScript Object that stores context for the validateToken call. At present, only the key property is supported.    
**key (Required)**  
Secret key for message digest computation. Can be provided either as a string or JavaScript Buffer. The bytes of a string are used as the key, so if you store the key base64-encoded, decode it first, for example with `Buffer.from(key, 'base64')`.

### Response
<a name="validatetoken-response"></a>

When the `validateToken()` method returns a successfully validated token, the response from the function is a JavaScript object in the following format. Once decoded, all claim keys are represented as strings of their numeric labels, such as `"4"` for `exp`.

```
{    
    protected,    
    unprotected,    
    payload
}
```

### Example - Validate token with kid sent in a request header
<a name="validatetoken-example"></a>

This example demonstrates CWT token validation, where the `kid` is read from the `x-cwt-kid` request header. The `kid` is then passed into CloudFront Functions KeyValueStore to fetch the secret key used to validate the token.

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
            if (cwtObj.payload[CwtClaims.exp] && cwtObj.payload[CwtClaims.exp] < currentTime) {
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
            statusCode: 500,
            statusDescription: 'Token processing failed'
        };
     }
    return request;
}
```

## generateToken() method
<a name="generatetoken-method"></a>

This function generates a new CWT token using the provided payload and context settings.

### Request
<a name="generatetoken-request"></a>

```
cf.cwt.generateToken(tokenContents, generatorContext)
```Parameters

**tokenContents (Required)**  
The contents of the token to encode, as a JavaScript object with exactly three properties: `protected`, `unprotected`, and `payload`. This is the same format as the object that `validateToken()` returns.

**generatorContext (Required)**  
This is a JavaScript Object that is used as the context for generating the token and contains the following key value pairs:    
**cwtTag (Optional)**  
This value is a boolean, which if `true` specifies the `cwtTag` should be added.  
**coseTag (Required)**  
Specifies the COSE tag type. Currently only supports `MAC0`.  
**key (Required)**  
Secret key to compute message digest. This value can be either a string or JavaScript `Buffer`.

### Response
<a name="generatetoken-response"></a>

Returns a JavaScript Buffer containing the encoded token.

**Example : Generate a token**  

```
import cf from 'cloudfront';

const CwtClaims = {
    iss: 1,
    sub: 2,
    exp: 4
};

const CatClaims = {
    catnip: 311,
    catu: 312,
    catm: 313,
    catr: 323
};

const Catu = {
    host: 1,
    path: 3,
    ext: 8
};

const CatuMatchTypes = {
    exact_match: 0,
    prefix_match: 1,
    suffix_match: 2
};

const Catr = {
    type: 0,
    expadd: 1,
    deadline: 2,
    header_name: 4
};

const CatrTypes = {
    automatic: 0,
    cookie: 1,
    header: 2,
    redirect: 3
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
                1: 5,
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
                    [Catr.type]: CatrTypes.header,
                    [Catr.expadd]: 3600,
                    [Catr.deadline]: 60,
                    [Catr.header_name]: "CTA-Common-Access-Token"
                }
            }
        };
        
        const request = event.request;
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
                statusCode: 500,
                statusDescription: 'Could not generate the token'
            };
        }
    } catch (error) {
        return {
            statusCode: 500,
            statusDescription: 'Token processing failed'
        };
    }
}
```

**Example : Refresh token based on some logic**  

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
            if (cwtJSON.payload[CwtClaims.exp] && cwtJSON.payload[CwtClaims.exp] < currentTime) {
                // We can regenerate the token and add 8 hours to the expiry time
                cwtJSON.payload[CwtClaims.exp] = Math.floor(Date.now() / 1000) + (8 * 60 * 60);
                                
                let genContext = {
                  coseTag: "MAC0",
                  key: secretKey
                }
                                
                let newTokenBuffer = cf.cwt.generateToken(cwtJSON, genContext);
                 request.headers['x-cwt-regenerated-token'] = { value: newTokenBuffer.toString('base64url') };
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
            statusCode: 500,
            statusDescription: 'Token processing failed'
        };
     }
    return request;
}
```