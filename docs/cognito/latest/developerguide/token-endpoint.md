# The token issuer endpoint

The OAuth 2.0 [token endpoint](https://www.rfc-editor.org/rfc/rfc6749#section-3.2 "https://www.rfc-editor.org/rfc/rfc6749#section-3.2") at `/oauth2/token` issues JSON web tokens
(JWTs) to applications that want to complete authorization-code and
client-credentials grant flows. These tokens are the end result of authentication
with a user pool. They contain information about the user (ID token), the user's
level of access (access token), and the user's entitlement to persist their
signed-in session (refresh token). OpenID Connect (OIDC) relying-party libraries
handle requests to and response payloads from this endpoint. Tokens provide
verifiable proof of authentication, profile information, and a mechanism for access
to back-end systems.

Your user pool OAuth 2.0 authorization server issues JSON web tokens (JWTs) from
the token endpoint to the following types of sessions:

1. Users who have completed a request for an authorization code grant.
   Successful redemption of a code returns ID, access, and refresh
   tokens.
2. Machine-to-machine (M2M) sessions that have completed a client-credentials
   grant. Successful authorization with the client secret returns an access
   token.
3. Users who have previously signed in and received refresh tokens. Refresh
   token authentication returns new ID and access tokens.

###### Note

Users who sign in with an authorization code grant in managed login or
through federation can always refresh their tokens from the token
endpoint. Users who sign in with the API operations
`InitiateAuth` and `AdminInitiateAuth` can
refresh their tokens with the token endpoint when [remembered
devices](amazon-cognito-user-pools-device-tracking.md "amazon-cognito-user-pools-device-tracking.md") is _not_ active in
your user pool. If remembered devices is active, refresh tokens with the
[relevant API or SDK
token-refresh operation](amazon-cognito-user-pools-using-the-refresh-token.md#using-the-refresh-token-api "amazon-cognito-user-pools-using-the-refresh-token.md#using-the-refresh-token-api") for your app client.
The token endpoint becomes publicly available when you add a domain to your user
pool. It accepts HTTP POST requests. For application security, use PKCE with your
authorization code sign-in events. PKCE verifies that the user passing an
authorization code is that same user who authenticated. For more information about
PKCE, see [IETF RFC
7636](https://datatracker.ietf.org/doc/html/rfc7636 "https://datatracker.ietf.org/doc/html/rfc7636").

You can learn more about the user pool app clients and their grant types, client
secrets, allowed scopes, and client IDs at [Application-specific settings with app
clients](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md"). You can learn more about M2M
authorization, client credentials grants, and authorization with access token scopes
at [Scopes, M2M, and resource
servers](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md").

To retrieve information about a user from their access token, pass it to your
[userInfo endpoint](userinfo-endpoint.md "userinfo-endpoint.md") or to a
[GetUser](../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md") API request. The access token must contain
the appropriate scopes for these requests,

## Format a POST request to the token endpoint

The `/oauth2/token` endpoint only supports `HTTPS POST`.
This endpoint is not user-interactive. Handle token requests with an [OpenID Connect (OIDC) library](https://openid.net/developers/certified-openid-connect-implementations/ "https://openid.net/developers/certified-openid-connect-implementations/") in your application.

The token endpoint supports `client_secret_basic` and
`client_secret_post` authentication. For more information about
the OIDC specification, see [Client Authentication](https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication "https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication"). For more information about the token
endpoint from the OpenID Connect specification, see [Token Endpoint](http://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint "http://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint").

### Request parameters in

header

You can pass the following parameters in the header of your request to the
token endpoint.

**`Authorization`**

If the client was issued a secret, the client can pass its
`client_id` and `client_secret` in the
authorization header as `client_secret_basic` HTTP
authorization. You can also include the `client_id`
and `client_secret` in the request body as
`client_secret_post` authorization.

The authorization header string is [Basic](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side "https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side")
`Base64Encode(client_id:client_secret)`. The
following example is an authorization header for app client
`djc98u3jiedmi283eu928` with client secret
`abcdef01234567890`, using the Base64-encoded
version of the string
`djc98u3jiedmi283eu928:abcdef01234567890`:

```
Authorization: Basic ZGpjOTh1M2ppZWRtaTI4M2V1OTI4OmFiY2RlZjAxMjM0NTY3ODkw
```

**`Content-Type`**

Set the value of this parameter to
`'application/x-www-form-urlencoded'`.

### Request parameters

in body

The following are parameters that you can request in
`x-www-form-urlencoded` format in the request body to the
token endpoint.

**`grant_type`**

_Required._

The type of OIDC grant that you want to request.

Must be `authorization_code` or
`refresh_token` or
`client_credentials`. You can request an access
token for a custom scope from the token endpoint under the
following conditions:

- You enabled the requested scope in your app client
  configuration.
- You configured your app client with a client
  secret.
- You enable client credentials grant in your app
  client.

###### Note

The token endpoint returns a refresh token only when the
`grant_type` is
`authorization_code`.

**`client_id`**

_Optional. Not required when you
provide the app client ID in the `Authorization`
header._

The ID of an app client in your user pool. Specify the same
app client that authenticated your user.

You must provide this parameter if the client is public and
does not have a secret, or with `client_secret` in
`client_secret_post` authorization.

**`client_secret`**

_Optional. Not required when you
provide the client secret in the `Authorization`
header and when the app client doesn't have a
secret._

The app client secret, if the app client has one, for
`client_secret_post` authorization.

**`scope`**

_Optional._

Can be a combination of any scopes that are associated with
your app client. Amazon Cognito ignores scopes in the request that aren't
allowed for the requested app client. If you don't provide this
request parameter, the authorization server returns an access
token `scope` claim with all authorization scopes
that you enabled in your app client configuration. You can
request any of the scopes allowed for the requested app client:
standard scopes, custom scopes from resource servers, and the
`aws.cognito.signin.user.admin` user self-service
scope.

**`redirect_uri`**

_Optional. Not required for
client-credentials grants._

Must be the same `redirect_uri` that was used to
get `authorization_code` in
`/oauth2/authorize`.

You must provide this parameter if `grant_type` is
`authorization_code`.

**`refresh_token`**

_Optional. Used only when the user
already has a refresh token and wishes to get new ID and
access tokens._

To generate new access and ID tokens for a user's session, set
the value of `refresh_token` to a valid refresh token
that the requested app client issued.

Returns a new refresh token with new ID and access token when
[refresh
token rotation](amazon-cognito-user-pools-using-the-refresh-token.md#using-the-refresh-token-rotation "amazon-cognito-user-pools-using-the-refresh-token.md#using-the-refresh-token-rotation") is active, otherwise returns only ID
and access tokens. If the original access token was [bound to an
API resource](cognito-user-pools-define-resource-servers.md#cognito-user-pools-resource-binding "cognito-user-pools-define-resource-servers.md#cognito-user-pools-resource-binding"), the new access token maintains the
requested API url in the `aud` claim.

**`code`**

_Optional. Only required in
authorization-code grants._

The authorization code from an authorization code grant. You
must provide this parameter if your authorization request
included a `grant_type` of
`authorization_code`.

**`aws_client_metadata`**

_Optional._

Information that you want to pass to the [Pre token generation Lambda
trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md") in [machine-to-machine (M2M)](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md") authorization flows. Your
application can collect context information about the session
and pass it in this parameter. When you pass
`aws_client_metadata` in URL-encoded JSON format,
Amazon Cognito includes it in the input event to your trigger Lambda
function. Your pre token trigger event version or global Lambda
trigger version must be configured for version three or later.
Although Amazon Cognito accepts requests to this endpoint in
authorization code and client credentials M2M flows, your user
pool only passes `aws_client_metadata` to the pre
token generation trigger from client credentials
requests.

**`code_verifier`**

Optional. Required only if you provided
`code_challenge_method` and
`code_challenge` parameters in your initial
authorization request.

The generated code verifier that your application calculated
the `code_challenge` from in an authorization code
grant request with [PKCE](using-pkce-in-authorization-code.md "using-pkce-in-authorization-code.md").

## Exchanging an authorization code for tokens

The following request successfully generates ID, access, and refresh tokens
after authentication with an authorization-code grant. The request passes the
client secret in `client_secret_basic` format in the
`Authorization` header.

```
POST https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/token&
Content-Type='application/x-www-form-urlencoded'&
Authorization=Basic `ZGpjOTh1M2ppZWRtaTI4M2V1OTI4OmFiY2RlZjAxMjM0NTY3ODkw`

grant_type=authorization_code&
client_id=`1example23456789`&
code=`AUTHORIZATION_CODE`&
redirect_uri=`com.myclientapp://myclient/redirect`
```

The response issues new ID, access, and refresh tokens to the user, with
additional metadata.

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "access_token": "`eyJra1example`",
    "id_token": "`eyJra2example`",
    "refresh_token": "`eyJj3example`",
    "token_type": "Bearer",
    "expires_in": `3600`
}
```

## Client credentials with basic authorization

The following request from an M2M application requests a client credentials
grant. Because client credentials requires a client secret, the request is
authorized with an `Authorization` header derived from the app client
ID and secret. The request results in an access token with the two requested
scopes. The request also includes client metadata that provides IP-address
information and a token issued to the user who this grant is on behalf of. Amazon Cognito
passes the client metadata to the pre token generation Lambda trigger.

```
POST https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/token >
Content-Type='application/x-www-form-urlencoded'&
Authorization=Basic `ZGpjOTh1M2ppZWRtaTI4M2V1OTI4OmFiY2RlZjAxMjM0NTY3ODkw`

grant_type=client_credentials&
client_id=`1example23456789`&
scope=`resourceServerIdentifier1`%2F`scope1`%20`resourceServerIdentifier2`%2F`scope2`&
&aws_client_metadata=`%7B%22onBehalfOfToken%22%3A%22eyJra789ghiEXAMPLE%22,%20%22ClientIpAddress%22%3A%22192.0.2.252%22%7D`
```

Amazon Cognito passes the following input event to the pre token generation Lambda
trigger.

```
{
    version: '3',
    triggerSource: 'TokenGeneration_ClientCredentials',
    region: '`us-east-1`',
    userPoolId: '`us-east-1_EXAMPLE`',
    userName: 'ClientCredentials',
    callerContext: {
        awsSdkVersion: '`aws-sdk-unknown-unknown`',
        clientId: '`1example23456789`'
    },
    request: {
        userAttributes: {},
        groupConfiguration: null,
        scopes: [
           'resourceServerIdentifier1/scope1',
           'resourceServerIdentifier2/scope2'
        ],
        clientMetadata: {
            'onBehalfOfToken': 'eyJra789ghiEXAMPLE',
            'ClientIpAddress': '192.0.2.252'
        }
    },
    response: { claimsAndScopeOverrideDetails: null }
}
```

The response returns an access token. Client credentials grants are for
machine-to-machine (M2M) authorization and only return access tokens.

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "access_token": "`eyJra1example`",
    "token_type": "Bearer",
    "expires_in": `3600`
}

```

## Client credentials with POST body authorization

The following client-credentials grant request includes the
`client_secret` parameter in the request body and doesn't include
an `Authorization` header. This request uses the
`client_secret_post` authorization syntax. The request results in
an access token with the requested scope. The request also includes client
metadata that provides IP-address information and a token issued to the user who
this grant is on behalf of. Amazon Cognito passes the client metadata to the pre token
generation Lambda trigger.

```
POST /oauth2/token HTTP/1.1
Content-Type: application/x-www-form-urlencoded
X-Amz-Target: AWSCognitoIdentityProviderService.Client credentials request
User-Agent: `USER_AGENT`
Accept: /
Accept-Encoding: gzip, deflate, br
Content-Length: 177
Referer: http://`auth.example.com`/oauth2/token
Host: `auth.example.com`
Connection: keep-alive

grant_type=client_credentials&
client_id=`1example23456789`&
scope=`my_resource_server_identifier%2Fmy_custom_scope&`
client_secret=`9example87654321`&
aws_client_metadata=`%7B%22onBehalfOfToken%22%3A%22eyJra789ghiEXAMPLE%22,%20%22ClientIpAddress%22%3A%22192.0.2.252%22%7D`
```

Amazon Cognito passes the following input event to the pre token generation Lambda
trigger.

```
{
    version: '3',
    triggerSource: 'TokenGeneration_ClientCredentials',
    region: '`us-east-1`',
    userPoolId: '`us-east-1_EXAMPLE`',
    userName: 'ClientCredentials',
    callerContext: {
        awsSdkVersion: '`aws-sdk-unknown-unknown`',
        clientId: '`1example23456789`'
    },
    request: {
        userAttributes: {},
        groupConfiguration: null,
        scopes: [
           'resourceServerIdentifier1/my_custom_scope'
        ],
        clientMetadata: {
            'onBehalfOfToken': 'eyJra789ghiEXAMPLE',
            'ClientIpAddress': '192.0.2.252'
        }
    },
    response: { claimsAndScopeOverrideDetails: null }
}
```

The response returns an access token. Client credentials grants are for
machine-to-machine (M2M) authorization and only return access tokens.

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Date: Tue, 05 Dec 2023 16:11:11 GMT
x-amz-cognito-request-id: 829f4fe2-a1ee-476e-b834-5cd85c03373b

{
    "access_token": "`eyJra12345EXAMPLE`",
    "expires_in": `3600`,
    "token_type": "Bearer"
}
```

## Authorization code grant with PKCE

The following example request completes an authorization request that included
`code_challenge_method` and `code_challenge`
parameters in an authorization code grant request with [PKCE](using-pkce-in-authorization-code.md "using-pkce-in-authorization-code.md").

```
POST https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/token
Content-Type='application/x-www-form-urlencoded'&
Authorization=Basic `ZGpjOTh1M2ppZWRtaTI4M2V1OTI4OmFiY2RlZjAxMjM0NTY3ODkw`

grant_type=authorization_code&
client_id=`1example23456789`&
code=`AUTHORIZATION_CODE`&
code_verifier=`CODE_VERIFIER`&
redirect_uri=`com.myclientapp://myclient/redirect`
```

The response returns ID, access, and refresh tokens from the successful PKCE
verification by the application.

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "access_token": "`eyJra1example`",
    "id_token": "`eyJra2example`",
    "refresh_token": "`eyJj3example`",
    "token_type": "Bearer",
    "expires_in": `3600`
}
```

## Token refresh without refresh token rotation

The following example requests provides a refresh token to an app client where
[refresh token
rotation](amazon-cognito-user-pools-using-the-refresh-token.md#using-the-refresh-token-rotation "amazon-cognito-user-pools-using-the-refresh-token.md#using-the-refresh-token-rotation") is inactive. Because the app client has a client secret, the
request provides an `Authorization` header.

```
POST https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/token >
Content-Type='application/x-www-form-urlencoded'&
Authorization=Basic `ZGpjOTh1M2ppZWRtaTI4M2V1OTI4OmFiY2RlZjAxMjM0NTY3ODkw`

grant_type=refresh_token&
client_id=`1example23456789`&
refresh_token=`eyJj3example`
```

The response returns new ID and access tokens.

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "access_token": "`eyJra1example`",
    "id_token": "`eyJra2example`",
    "token_type": "Bearer",
    "expires_in": `3600`}
```

## Token refresh with

refresh token rotation

The following example requests provides a refresh token to an app client where
[refresh token
rotation](amazon-cognito-user-pools-using-the-refresh-token.md#using-the-refresh-token-rotation "amazon-cognito-user-pools-using-the-refresh-token.md#using-the-refresh-token-rotation") is active. Because the app client has a client secret, the
request provides an `Authorization` header.

```
POST https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/token >
Content-Type='application/x-www-form-urlencoded'&
Authorization=Basic `ZGpjOTh1M2ppZWRtaTI4M2V1OTI4OmFiY2RlZjAxMjM0NTY3ODkw`

grant_type=refresh_token&
client_id=`1example23456789`&
refresh_token=`eyJj3example`
```

The response returns new ID, access, and refresh tokens.

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "access_token": "`eyJra1example`",
    "id_token": "`eyJra2example`",
    "refresh_token": "`eyJj4example`",
    "token_type": "Bearer",
    "expires_in": `3600`
}
```

## Examples of negative responses

Malformed requests generate errors from the token endpoint. The following is a
general map of the response body when token requests generate an error.

```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
"error":"invalid_request|invalid_client|invalid_grant|unauthorized_client|unsupported_grant_type"
}
```

**`invalid_request`**

The request is missing a required parameter, includes an
unsupported parameter value (other than
`unsupported_grant_type`), or is otherwise malformed.
For example, `grant_type` is `refresh_token`
but `refresh_token` is not included.

**`invalid_client`**

Client authentication failed. For example, when the client
includes `client_id` and `client_secret` in
the authorization header, but there's no such client with that
`client_id` and `client_secret`.

**`invalid_grant`**

Refresh token has been revoked.

Authorization code has been consumed already or does not exist.

App client doesn't have read access to all [attributes](user-pool-settings-attributes.md "user-pool-settings-attributes.md") in the requested scope. For example, your
app requests the `email` scope and your app client can
read the `email` attribute, but not
`email_verified`.

**`unauthorized_client`**

Client is not allowed for code grant flow or for refreshing
tokens.

**`unsupported_grant_type`**

Returned if `grant_type` is anything other than
`authorization_code` or `refresh_token` or
`client_credentials`.
