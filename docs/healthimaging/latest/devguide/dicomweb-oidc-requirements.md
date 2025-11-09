# Set up an AWS Lambda authorizer for OIDC authentication

This guide assumes you have already configured your Identity Provider (IdP) of choice to provide access tokens
compatible with the requirements of the HealthImaging OIDC authentication feature.

## 1. Configure IAM Roles for DICOMWeb API Access

Before configuring the Lambda authorizer, create IAM roles for HealthImaging to assume when processing DICOMWeb API requests.
The authorizer Lambda function returns one of these roles ARN after successful token verification, allowing HealthImaging to execute
the requests with appropriate permissions.

1. Create IAM policies defining the desired DICOMWeb API privileges. Refer to the "[Using DICOMweb](using-dicomweb.md "using-dicomweb.md")" section of the HealthImaging documentation for
   available permissions.
2. Create IAM roles that:
   - Attach these policies
   - Include a trust relationship allowing the AWS HealthImaging service principal (`medical-imaging.amazonaws.com`)
     to assume these roles.

Here is an example of a policy allowing associated roles to access to HealthImaging DICOMWeb read-only API:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "MedicalImagingDicomWebOperations",
            "Effect": "Allow",
            "Action": [
                "medical-imaging:SearchDICOMInstances",
                "medical-imaging:GetImageSetMetadata",
                "medical-imaging:GetDICOMSeriesMetadata",
                "medical-imaging:SearchDICOMStudies",
                "medical-imaging:GetDICOMBulkdata",
                "medical-imaging:SearchDICOMSeries",
                "medical-imaging:GetDICOMInstanceMetadata",
                "medical-imaging:GetDICOMInstance",
                "medical-imaging:GetDICOMInstanceFrames"
            ],
            "Resource": "arn:aws:medical-imaging:{`Region`}:{`Account`}:datastore/{`DatastoreId`}"
        }
    ]
}
```

Here is an example of the trust relationship policy that should be associated to the role(s):

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "OIDCRoleFederation",
            "Effect": "Allow",
            "Principal": {
                "Service": "medical-imaging.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

The Lambda authorizer you'll create in the next step can evaluate the token claims and return the ARN of the
appropriate role. AWS HealthImaging will then impersonate this role to execute the DICOMWeb API request with the corresponding
permissions.

For example:

- A token with "admin" claims might return an ARN for a role with full access
- A token with "reader" claims might return an ARN for a role with read-only access
- A token with "department_A" claims might return an ARN for a role specific to that department's access
  level

This mechanism allows you to map your IdP's authorization model to specific AWS HealthImaging permissions through IAM
roles.

## 2. Create and Configure Lambda Authorizer Function

Create a Lambda function that will verify the JWT token and return the appropriate IAM role ARN based on the
token claims evaluation. This function is invoked by the health imaging service and passed an event that contains the
HealthImaging datastore Id, the DICOMWeb operation, and the access token found in the HTTP request:

```
{
  "datastoreId": "{`datastore id`}",
  "operation": "{`Healthimaging API name e.g. GetDICOMInstance`}",
  "bearerToken": "{`access token`}"
}
```

The Lambda authorizer function must return a JSON response with the following structure:

```
{
  "isTokenValid": {true or false},
  "roleArn": "{role arn or empty string meaning to deny the request explicitly}"
}
```

You can refer to the implementation example for more information.

###### Note

Because the DICOMWeb request is only answered after the access token is verified by the lambda authorizer, it
is important that the execution of this function be as fast as possible to provide with the best DICOMWeb API response
time.

For the HealthImaging service to be authorized to invoke the lambda authorizer function, it must have a resource policy that allows
HealthImaging service to invoke it. This resource policy can be created in the permission menu of the lambda configuration tab or
Using AWS CLI:

```
aws lambda add-permission \
    --function-name YourAuthorizerFunctionName \
    --statement-id HealthImagingInvoke \
    --action lambda:InvokeFunction \
    --principal medical-imaging.amazonaws.com
```

This resource policy allows the HealthImaging service to invoke your Lambda authorizer when authenticating DICOMWeb API
requests.

###### Note

The lambda resource policy can be updated later on with an "ArnLike" condition matching the ARN of a specific HealthImaging
datastore.

Here is an example of lambda resource policy:

```
{
  "Version": "2012-10-17",
  "Id": "default",
  "Statement": [
    {
      "Sid": "LambaAuthorizer-HealthImagingInvokePermission",
      "Effect": "Allow",
      "Principal": {
        "Service": "medical-imaging.amazonaws.com"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:{`Region`}:{`Account`}::function:{`LambdaAuthorizerFunctionName`}",
      "Condition": {
        "ArnLike": {
          "AWS:SourceArn": "arn:aws:medical-imaging:{`Region`}:{`Account`}:datastore/{`DatastoreId`}"
        }
      }
    }
  ]
}
```

## 3. Create a New Datastore with OIDC Authentication

To enable OIDC authentication, you must create a new datastore using the AWS CLI with the parameter
"lambda-authorizer-arn". OIDC Authentication cannot be enabled on existing datastores without contacting AWS
Support.

Here's an example of how to create a new datastore with OIDC authentication enabled:

```
aws medical-imaging create-datastore \
    --datastore-name `YourDatastoreName` \
    --lambda-authorizer-arn YourAuthorizerFunctionArn
```

You can check if a specific datastore has OIDC authentication feature enabled by using the AWS CLI
get-datastore command, and verifying if the attribute "lambdaAuthorizerArn" is present:

```
aws medical-imaging get-datastore --datastore-id `YourDatastoreId`
```

```
{
    "datastoreProperties": {
        "datastoreId": `YourdatastoreId`,
        "datastoreName": `YourDatastoreName,`
        "datastoreStatus": "ACTIVE",
        "lambdaAuthorizerArn": `YourAuthorizerFunctionArn,`
        "datastoreArn": `YourDatastoreArn,`
        "createdAt": "2025-09-30T14:16:04.015000-05:00",
        "updatedAt": "2025-09-30T14:16:04.015000-05:00"
    }
}
```

###### Note

The execution role for the AWS CLI datastore creation command must have appropriate permissions to
invoke the Lambda authorizer function. This mitigates privilege escalation attacks where malicious users could
execute unauthorized Lambda functions through the datastore authorizer configuration.

## Exception Codes

In case of authentication failure HealthImaging returns the following HTTP error response codes and body messages:

| Condition                                                                   | AHI response                                              |
| --------------------------------------------------------------------------- | --------------------------------------------------------- |
| Lambda Authorizer does not exist or is invalid                              | \*_424_<br>• Authorizer Misconfiguration                  |
| Authorizer terminated due to execution failure                              | \*_424_<br>• Authorizer Failed                            |
| Any other unmapped authorizer error                                         | \*_424_<br>• Authorizer Failed                            |
| Authorizer returned invalid/ill-formed response                             | \*_424_<br>• Authorizer Misconfiguration                  |
| Authorizer ran more than 1s                                                 | \*_408_<br>• Authorizer Timeout                           |
| Token is expired or otherwise invalid                                       | \*_403_<br>• Invalid or Expired Token                     |
| AHI can't federate the returned IAM Role due to authorizer misconfiguration | \*_424_<br>• Authorizer Misconfiguration                  |
| Authorizer returned an empty Role                                           | \*_403_<br>• Access Denied                                |
| Returned Role is not callable (assume-role/trust misconfig)                 | \*_424_<br>• Authorizer Misconfiguration                  |
| Request rate exceeds DICOMweb Gateway limits                                | \*_429_<br>• Too many requests                            |
| Datastore, Return Role, or Authorizer Cross Account/Cross Region            | \*_424_<br>• Authorizer Cross Account/Cross Region Access |

## Implementation Example

This Python example demonstrates a lambda authorizer function that verifies AWS Cognito access tokens from HealthImaging
events and returns an IAM role ARN with appropriate DICOMWeb privileges.

The Lambda authorizer implements two caching mechanisms to reduce external calls and response latency. The JWKS
(JSON Web Key Set) is fetched once every hour and stored in the function's temporary folder, allowing subsequent function
invocations to read it locally instead of fetching from the public network. You will also notice that a token_cache dictionary
object is instantiated in the global context of this Lambda function. Global variables are shared by all invocations that
reuse the same warmed Lambda context. Thanks to this, successfully verified tokens can be stored in this dictionary and looked
up quickly during the next execution of this same Lambda function. The caching method represents a generalist approach that
could fit access tokens issued from most identity providers. For an AWS Cognito specific caching option, refer to [Managing User pool](../../../cognito/latest/developerguide/managing-users.md "../../../cognito/latest/developerguide/managing-users.md")
section and [caching section](../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-caching-tokens.md "../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-caching-tokens.md") of [AWS Cognito documentation](../../../cognito/latest/developerguide/what-is-amazon-cognito.md "../../../cognito/latest/developerguide/what-is-amazon-cognito.md").

```
import json
import os
import time
import logging
from jose import jwk, jwt
from jose.exceptions import ExpiredSignatureError, JWTClaimsError, JWTError
import requests
import tempfile

# Configure logging
logger = logging.getLogger()
log_level = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logger.setLevel(getattr(logging, log_level, logging.WARNING))

# Global token cache with TTL
token_cache = {}

# JWKS cache file path
JWKS_CACHE_FILE = os.path.join(tempfile.gettempdir(), 'jwks.json')
JWKS_CACHE_TTL = 3600  # 1 hour

# Load environment variables once
USER_POOL_ID = os.environ['USER_POOL_ID']
CLIENT_ID = os.environ['CLIENT_ID']
ROLE_ARN = os.environ.get('AHIDICOMWEB_READONLY_ROLE_ARN', '')

def cleanup_expired_tokens():
    """Remove expired tokens from cache"""
    now = int(time.time())
    expired_keys = [token for token, data in token_cache.items() if now > data['cache_expiry']]
    for token in expired_keys:
        del token_cache[token]

def get_cached_jwks():
    """Get JWKS from cache file if valid, otherwise return None """
    try:
        if os.path.exists(JWKS_CACHE_FILE):
            # Check if cache file is still valid
            cache_age = time.time() - os.path.getmtime(JWKS_CACHE_FILE)
            if cache_age < JWKS_CACHE_TTL:
                with open(JWKS_CACHE_FILE, 'r') as f:
                    jwks = json.load(f)
                    logger.debug(f'Using cached JWKS (age: {int(cache_age)}s)')
                    return jwks
            else:
                logger.debug(f'JWKS cache expired (age: {int(cache_age)}s)')
    except Exception as e:
        logger.debug(f'Error reading JWKS cache: {e}')

    return None

def cache_jwks(jwks):
    """Cache JWKS to file"""
    try:
        with open(JWKS_CACHE_FILE, 'w') as f:
            json.dump(jwks, f)
        logger.debug('JWKS cached successfully')
    except Exception as e:
        logger.debug(f'Error caching JWKS: {e}')

def fetch_jwks(jwks_url):
    """Fetch JWKS from URL and cache it"""
    logger.debug('Fetching JWKS from URL')
    jwks = requests.get(jwks_url, timeout=10).json()
    # Convert to dict for faster lookups
    jwks['keys_by_kid'] = {key['kid']: key for key in jwks['keys']}
    cache_jwks(jwks)
    return jwks

def is_token_cached(token):
    if token not in token_cache:
        return None

    cached = token_cache[token]
    now = int(time.time())

    if now > cached['cache_expiry']:
        del token_cache[token]
        return None

    return cached

def cache_token(token, payload):
    now = int(time.time())
    token_exp = payload.get('exp')
    cache_expiry = min(now + 60, token_exp)  # 1 minute or token expiry, whichever is sooner

    token_cache[token] = {
        'payload': payload,
        'cache_expiry': cache_expiry,
        'role_arn': ROLE_ARN
    }

def handler(event, context):
    cleanup_expired_tokens() # start be removing expired tokens from the cache
    try:
        # Extract token from bearerToken or authorizationToken field
        token = event.get('bearerToken')
        if not token:
            raise Exception('No token provided')

        # Check cache first
        cached = is_token_cached(token)
        if cached:
            logger.debug('Token found in cache, skipping verification')
            return {
                'isTokenValid': True,
                'roleArn': cached['role_arn']
            }

        # Get Cognito configuration
        region = context.invoked_function_arn.split(':')[3]

        # Get JWKS (cached or fresh)
        jwks_url = f'https://cognito-idp.{region}.amazonaws.com/{USER_POOL_ID}/.well-known/jwks.json'
        jwks = get_cached_jwks()
        if not jwks:
            jwks = fetch_jwks(jwks_url)

        # Decode token header to get kid
        headers = jwt.get_unverified_headers(token)
        kid = headers['kid']

        # Find the correct key
        key = None
        for jwk_key in jwks['keys']:
            if jwk_key['kid'] == kid:
                key = jwk_key
                break

        if not key:
            # Key not found - try refreshing JWKS in case of key rotation
            logger.debug('Key not found in cached JWKS, fetching fresh JWKS')
            jwks = fetch_jwks(jwks_url)
            for jwk_key in jwks['keys']:
                if jwk_key['kid'] == kid:
                    key = jwk_key
                    break

        if not key:
            raise Exception('Public key not found')

        # Construct the public key
        public_key = jwk.construct(key)

        # Verify and decode the token (includes expiry validation)
        payload = jwt.decode(
            token,
            public_key,
            algorithms=['RS256'],
            audience=CLIENT_ID,
            issuer=f'https://cognito-idp.{region}.amazonaws.com/{USER_POOL_ID}'
        )

        logger.debug('Token validated successfully')
        logger.debug('User: %s', payload.get('username', 'unknown'))

        # Cache the validated token
        cache_token(token, payload)

        # Return authorization response
        return {
            'isTokenValid': True,
            'roleArn': ROLE_ARN
        }

    except ExpiredSignatureError:
        logger.debug('Token expired')
        return {
            'isTokenValid': False,
            'roleArn': ''
        }
    except JWTClaimsError:
        logger.debug('Invalid token claims')
        return {
            'isTokenValid': False,
            'roleArn': ''
        }
    except JWTError as e:
        logger.debug('JWT validation error: %s', e)
        return {
            'isTokenValid': False,
            'roleArn': ''
        }
    except Exception as e:
        logger.debug('Authorization failed: %s', e)
        return {
            'isTokenValid': False,
            'roleArn': ''
        }
```
