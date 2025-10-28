# The user attributes endpoint

Where OIDC issues ID tokens that contain user attributes, OAuth 2.0 implements the
`/oauth2/userInfo` endpoint. An authenticated user or client receives
an access token with a `scopes` claim. This claim determines the
attributes that the authorization server should return. When an application presents
an access token to the `userInfo` endpoint, the authorization server
returns a response body that contains the user attributes that are within the
boundaries set by the access token scopes. Your application can retrieve information
about a user from the `userInfo` endpoint as long as it holds a valid
access token with at least an `openid` scope claim.

The `userInfo` endpoint is an OpenID Connect (OIDC) [userInfo
endpoint](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo "https://openid.net/specs/openid-connect-core-1_0.html#UserInfo"). It responds with user attributes when service providers
present access tokens that your [token endpoint](token-endpoint.md "token-endpoint.md")
issued. The scopes in your user's access token define the user attributes that the
userInfo endpoint returns in its response. The `openid` scope must be one
of the access token claims.

Amazon Cognito issues access tokens in response to user pools API requests like [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md"). Because they don't contain any scopes,
the userInfo endpoint doesn't accept these access tokens. Instead,
you must present access tokens from your token endpoint.

Your OAuth 2.0 third-party identity provider (IdP) also hosts a
userInfo endpoint. When your user authenticates with that IdP,
Amazon Cognito silently exchanges an authorization code with the IdP `token`
endpoint. Your user pool passes the IdP access token to authorize retrieval of user
information from the IdP `userInfo` endpoint.

The scopes in a user's access token are determined by the `scopes`
request parameter in authentication requests, or the scopes that the [pre token generation Lambda
trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md") adds. You can decode access tokens and examine `scope`
claims to see the access-control scopes that they contain. The following are some
scope combinations that influence the data returned from the `userInfo`
endpoint. The reserved Amazon Cognito scope `aws.cognito.signin.user.admin` has no
effect on the data returned from this endpoint.

###### Example scopes in access token and their effect on the `userInfo`

response

**`openid`**

Returns a response with all user attributes that the app client can
read.

**`openid profile`**

Returns the user attributes `name`,
`family_name`, `given_name`,
`middle_name`, `nickname`,
`preferred_username`, `profile`,
`picture`, `website`, `gender`,
`birthdate`, `zoneinfo`, `locale`,
and `updated_at`. Also returns [custom
attributes](user-pool-settings-attributes.md#user-pool-settings-custom-attributes "user-pool-settings-attributes.md#user-pool-settings-custom-attributes"). In app clients that don't have read access to
each attribute, the response to this scope is all of the attributes
within the specification that your app client does have read access
to.

**`openid email`**

Returns basic profile information and the `email` and
`email_verified` attributes.

**`openid phone`**

Returns basic profile information and the `phone_number`
and `phone_number_verified` attributes.

## GET /oauth2/userInfo

Your application generates requests to this endpoint directly, not through a
browser.

For more information, see [UserInfo Endpoint](http://openid.net/specs/openid-connect-core-1_0.html#UserInfo "http://openid.net/specs/openid-connect-core-1_0.html#UserInfo") in the OpenID Connect (OIDC)
specification.

###### Topics

- [Request parameters in
  header](#get-userinfo-request-header-parameters "#get-userinfo-request-header-parameters")
- [Example – request](#get-userinfo-positive-exchanging-authorization-code-for-userinfo-sample-request "#get-userinfo-positive-exchanging-authorization-code-for-userinfo-sample-request")
- [Example – positive
  response](#get-userinfo-response-sample "#get-userinfo-response-sample")
- [Example negative responses](#get-userinfo-negative "#get-userinfo-negative")

## Request parameters in

header

**`Authorization: Bearer
 `<access_token>``**

Pass the access token in the authorization header field.

Required.

## Example – request

```
GET /oauth2/userInfo HTTP/1.1
Content-Type: application/x-amz-json-1.1
Authorization: Bearer eyJra12345EXAMPLE
User-Agent: `[User agent]`
Accept: */*
Host: auth.example.com
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

## Example – positive

response

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Content-Length: `[Integer]`
Date: `[Timestamp]`
x-amz-cognito-request-id: `[UUID]`
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
X-Frame-Options: DENY
Server: Server
Connection: keep-alive
{
    "sub": "`[UUID]`",
    "email_verified": "true",
    "custom:mycustom1": "CustomValue",
    "phone_number_verified": "true",
    "phone_number": "+12065551212",
    "email": "bob@example.com",
    "username": "bob"
}
```

For a list of OIDC claims, see [Standard Claims](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims "http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims"). Currently, Amazon Cognito returns the values for
`email_verified` and `phone_number_verified` as
strings.

## Example negative responses

### Example – bad

request

```
HTTP/1.1 400 Bad Request
WWW-Authenticate: error="invalid_request",
error_description="Bad OAuth2 request at UserInfo Endpoint"
```

**`invalid_request`**

The request is missing a required parameter, it includes an
unsupported parameter value, or it is otherwise
malformed.

### Example – bad

token

```
HTTP/1.1 401 Unauthorized
WWW-Authenticate: error="invalid_token",
error_description="Access token is expired, disabled, or deleted, or the user has globally signed out."
```

**`invalid_token`**

The access token is expired, revoked, malformed, or it's
invalid.
