

# Edge-only APIs for use with AWS IoT SiteWise edge devices
<a name="edge-local-apis"></a>

In addition to the AWS IoT SiteWise APIs that are available on the edge, there are edge-specific ones. Those edge-specifc APIs are described below.

## Authenticate
<a name="edge-local-apis-authenticate"></a>

Gets the credentials from the SiteWise Edge gateway. You'll need to add local users or connect to your system using LDAP or a Linux user pool. For more information about adding users, see [LDAP](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-gateways-ggv2.html#opshub-app) or [Linux user pool](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-gateways-ggv2.html#opshub-app).

### Request syntax
<a name="authenticate-request-syntax"></a>

```
POST /authenticate HTTP/1.1
Content-type: application/json
{
  "username": "string",
  "password": "string",
  "authMechanism": "string"
}
```

### URI request Parameters
<a name="authenticate-request-parameters"></a>

The request does not use any URI parameters.

### Request body
<a name="authenticate-request-body"></a>

The request accepts the following data in JSON format.

**username**  
The username used to validate the request call.  
Type: String  
Required: Yes

**password**  
The password of the user requesting credentials.  
Type: String  
Required: Yes

**authMechanism**  
The authentication method to validate this user in the host.  
Type: String  
Valid values: `ldap`, `linux`, `winnt`  
Required: Yes

### Response syntax
<a name="authenticate-response-syntax"></a>

```
HTTP/1.1 200
Content-type: application/json
{
  "accessKeyId": "string",
  "secretAccessKey": "string",
  "sessionToken": "string",
  "region": "edge"
}
```

### Response elements
<a name="authenticate-response-elements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format.

**accessKeyId**  
The access key ID that identifies the temporary security credentials.  
Length Constraints: Minimum length of 16. Maximum length of 128.  
Pattern: `[\w]*`

**secretAccessKey**  
The secret access key that can be used to sign requests.  
Type: String

**sessionToken**  
The token that users must pass to the service API to use the temporary credentials.  
Type: String

**region**  
The region you are targeting for API calls.  
Type: CONSTANT - `edge`

### Errors
<a name="authenticate-errors"></a>

**IllegalArgumentException**  
The request was rejected because the provided body document was malformed. The error message describes the specific error.  
HTTP Status Code: 400

**AccessDeniedException**  
The user doesn't have valid credentials based on the current Identity Provider. The error message describes the authentication Mechanism.  
HTTP Status Code: 403

**TooManyRequestsException**  
The request has reached it's limit of authentication attempts. The error message contains the quantity of time to wait until new attempts of authentication are made.  
HTTP Status Code: 429