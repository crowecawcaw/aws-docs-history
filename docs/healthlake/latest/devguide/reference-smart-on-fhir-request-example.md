# Making a FHIR REST API request on a

SMART-enabled HealthLake data store

You can make FHIR REST API requests on a SMART on FHIR-enabled HealthLake data store. The
following example shows a request from client application containing a JWT in the authorization
header and how Lambda should decode the response. After the client application request is
authorized and authenticated, it must receive a bearer token from the authorization server. Use
the bearer token in the authorization header when sending a FHIR REST API request on a
SMART on FHIR-enabled HealthLake data store.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`[ID]`
Authorization: Bearer `auth-server-provided-bearer-token`

```

Because a bearer token was found in the authorization header and no AWS IAM identity was
detected HealthLake invokes the Lambda function specified when the SMART on FHIR enabled HealthLake data
store was created. When the token is successfully decoded by your Lambda function, the following
example response is sent to HealthLake.

```
{
  "authPayload": {
    "iss": "https://`authorization-server-endpoint`/oauth2/`token`", # The issuer identifier of the authorization server
    "aud": "https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/", # Required, data store endpoint
    "iat": 1677115637,  # Identifies the time at which the token was issued
    "nbf": 1677115637,  # Required, the earliest time the JWT would be valid
    "exp": 1997877061,  # Required, the time at which the JWT is no longer valid
    "isAuthorized": "true",  # Required, boolean indicating the request has been authorized
    "uid": "100101",  # Unique identifier returned by the auth server
    "scope": "system/*.*" # Required, the scope of the request
  },
  "iamRoleARN": "`iam-role-arn`" #Required, IAM role to complete the request
}
```
