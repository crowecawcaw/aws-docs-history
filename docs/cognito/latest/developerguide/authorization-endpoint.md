# The redirect and authorization

endpoint

The `/oauth2/authorize` endpoint is a redirection endpoint that
supports two redirect destinations. If you include an `identity_provider`
or `idp_identifier` parameter in the URL, it silently redirects your user
to the sign-in page for that identity provider (IdP). Otherwise, it redirects to the
[Login endpoint](login-endpoint.md "login-endpoint.md") with the same
URL parameters that you included in your request.

The authorize endpoint redirects either to managed login or to an IdP sign-in
page. The destination of a user session at this endpoint is a webpage that your user
must interact with directly in their browser.

To use the authorize endpoint, invoke your user's browser at
`/oauth2/authorize` with parameters that provide your user pool with
information about the following user pool details.

- The app client that you want to sign in to.
- The callback URL that you want to end up at.
- The OAuth 2.0 scopes that you want to request in your user's access
  token.
- Optionally, the third-party IdP that you want to use to sign in.
  You can also supply `state` and `nonce` parameters that
  Amazon Cognito uses to validate incoming claims.

## GET `/oauth2/authorize`

The `/oauth2/authorize` endpoint only supports `HTTPS
 GET`. Your app typically initiates this request in your user's
browser. You can only make requests to the `/oauth2/authorize`
endpoint over HTTPS.

You can learn more about the definition of the authorization endpoint in the
OpenID Connect (OIDC) standard at [Authorization Endpoint](http://openid.net/specs/openid-connect-core-1_0.html#ImplicitAuthorizationEndpoint "http://openid.net/specs/openid-connect-core-1_0.html#ImplicitAuthorizationEndpoint").

### Request

parameters

**`response_type`**

Required.

The response type. Must be `code` or
`token`.

A successful request with a `response_type` of
`code` returns an authorization code grant. An
authorization code grant is a `code` parameter that
Amazon Cognito appends to your redirect URL. Your app can exchange the
code with the [Token endpoint](token-endpoint.md "token-endpoint.md") for access, ID, and refresh
tokens. As a security best practice, and to receive refresh
tokens for your users, use an authorization code grant in your
app.

A successful request with a `response_type` of
`token` returns an implicit grant. An implicit
grant is an ID and access token that Amazon Cognito appends to your
redirect URL. An implicit grant is less secure because it
exposes tokens and potential identifying information to users.
You can deactivate support for implicit grants in the
configuration of your app client.

**`client_id`**

Required.

The app client ID.

The value of `client_id` must be the ID of an app
client in the user pool where you make the request. Your app
client must support sign-in by Amazon Cognito local users or at least one
third-party IdP.

**`redirect_uri`**

Required.

The URL where the authentication server redirects the browser
after Amazon Cognito authorizes the user.

A redirect uniform resource identifier (URI) must have the
following attributes:

- It must be an absolute URI.
- You must have pre-registered the URI with a
  client.
- It can't include a fragment component.

See [OAuth 2.0 - Redirection Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2 "https://tools.ietf.org/html/rfc6749#section-3.1.2").

Amazon Cognito requires that your redirect URI use HTTPS, except for
`http://localhost`, which you can set as a
callback URL for testing purposes.

Amazon Cognito also supports app callback URLs such as
`myapp://example`.

**`state`**

Optional, recommended.

When your app adds a _state_
parameter to a request, Amazon Cognito returns its value to your app when
the `/oauth2/authorize` endpoint redirects your
user.

Add this value to your requests to guard against [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery "https://en.wikipedia.org/wiki/Cross-site_request_forgery") attacks.

You can't set the value of a `state` parameter to a
URL-encoded JSON string. To pass a string that matches this
format in a `state` parameter, encode the string to
base64, then decode it in your app.

**`identity_provider`**

Optional.

Add this parameter to bypass managed login and redirect your
user to a provider sign-in page. The value of the _identity_provider_ parameter is the
name of the identity provider (IdP) as it appears in your user
pool.

- For social providers, you can use the _identity_provider_ values
  `Facebook`, `Google`,
  `LoginWithAmazon`, and
  `SignInWithApple`.
- For Amazon Cognito user pools, use the value
  `COGNITO`.
- For SAML 2.0 and OpenID Connect (OIDC)
  identity providers (IdPs), use the name that you
  assigned to the IdP in your user pool.

**`idp_identifier`**

Optional.

Add this parameter to redirect to a provider with an
alternative name for the _identity_provider_ name. You can enter
identifiers for your SAML 2.0 and OIDC IdPs from the
**Social and external providers** menu of
the Amazon Cognito console.

**`scope`**

Optional.

Can be a combination of any system-reserved scopes or custom
scopes that are associated with a client. Scopes must be
separated by spaces. System reserved scopes are
`openid`, `email`, `phone`,
`profile`, and
`aws.cognito.signin.user.admin`. Any scope used
must be associated with the client, or it will be ignored at
runtime.

If the client doesn't request any scopes, the authentication
server uses all scopes that are associated with the
client.

An ID token is only returned if `openid` scope is
requested. The access token can be only used against Amazon Cognito user
pools if `aws.cognito.signin.user.admin` scope is
requested. The `phone`, `email`, and
`profile` scopes can only be requested if
`openid` scope is also requested. These scopes
dictate the claims that go inside the ID token.

**`code_challenge_method`**

Optional.

The hashing protocol that you used to generate the challenge.
The [PKCE
RFC](https://tools.ietf.org/html/rfc7636 "https://tools.ietf.org/html/rfc7636") defines two methods, S256 and plain; however,
Amazon Cognito authentication server supports only S256.

**`code_challenge`**

Optional.

The proof of key code exchange (PKCE) challenge that you
generated from the `code_verifier`. For more
information, see [Using PKCE in authorization code
grants](using-pkce-in-authorization-code.md "using-pkce-in-authorization-code.md").

Required only when you specify a
`code_challenge_method` parameter.

**`nonce`**

Optional.

A random value that you can add to the request. The nonce
value that you provide is included in the ID token that Amazon Cognito
issues. To guard against replay attacks, your app can inspect
the `nonce` claim in the ID token and compare it to
the one you generated. For more information about the
`nonce` claim, see [ID token validation](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation "https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation") in the _OpenID Connect standard_.

**`lang`**

Optional.

The language that you want to display user-interactive pages
in. Managed login pages can be localized, but hosted UI
(classic) pages can't. For more information, see [Managed login localization](cognito-user-pools-managed-login.md#managed-login-localization "cognito-user-pools-managed-login.md#managed-login-localization").

**`login_hint`**

Optional.

A username prompt that you want to pass to the authorization
server. You can collect a username, email address or phone
number from your user and allow the destination provider to
pre-populate the user's sign-in name. When you submit a
`login_hint` parameter and no
`idp_identifier` or
`identity_provider` parameters to the
`oauth2/authorize` endpoint, managed login fills
the username field with your hint value. You can also pass this
parameter to the [Login endpoint](login-endpoint.md "login-endpoint.md") and automatically fill the
username value.

When your authorization request invokes a redirect to OIDC
IdPs or Google, Amazon Cognito adds a `login_hint` parameter
to the request to that third-party authorizer. You can't forward
login hints to SAML, Apple, Login With Amazon, or Facebook
(Meta) IdPs.

**`prompt`**

Optional.

An OIDC parameter that controls authentication behavior for
existing sessions. Available in the managed login branding
version only, not in the classic hosted UI. For more information
from the OIDC specification, see [Authentication request](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest "https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest"). The values
`none` and `login` have an effect on
user pool authentication behavior.

Amazon Cognito forwards all values of `prompt` except
`none` to your IdPs when users select
authentication with third-party providers. This is true when the
URL that users access includes an `identity_provider`
or `idp_identifier` parameter, or when the
authorization server redirects them to the [Login endpoint](login-endpoint.md "login-endpoint.md")
and they select and IdP from the available buttons.

###### Prompt parameter values

`prompt=none`

Amazon Cognito silently continues authentication for users
who have a valid authenticated session. With this
prompt, users can silently authenticate between
different app clients in your user pool. If the user
is not already authenticated, the authorization
server returns a `login_required`
error.

`prompt=login`

Amazon Cognito requires users to re-authenticate even if
they have an existing session. Send this value when
you want to verify the user's identity again.
Authenticated users who have an existing session can
return to sign-in without invalidating that session.
When a user who has an existing session signs in
again, Amazon Cognito assigns them a new session cookie. This
parameter can also be forwarded to your IdPs. IdPs
that accept this parameter also request a new
authentication attempt from the user.

`prompt=select_account`

This value has no effect on local sign-in and must
be submitted in requests that redirect to IdPs. When
included in your authorization request, this
parameter adds `prompt=select_account` to
the URL path for the IdP redirect destination. When
IdPs support this parameter, they request that users
select the account that they want to log in
with.

`prompt=consent`

This value has no effect on local sign-in and must
be submitted in requests that redirect to IdPs. When
included in your authorization request, this
parameter adds `prompt=consent` to the
URL path for the IdP redirect destination. When IdPs
support this parameter, they request user consent
before they redirect back to your user pool.

When you omit the `prompt` parameter from your
request, managed login follows the default behavior: users must
sign in unless their browser has a valid managed login session
cookie. You can combine multiple values for `prompt`
with a space-character delimiter, for example `prompt=login
 consent`.

**`resource`**

Optional.

The identifier of a resource that you want to bind to the
access token in the `aud` claim. When you include
this parameter, Amazon Cognito validates that the value is a URL and sets
the audience of the resulting access token to the requested
resource. You can request a user pool [resource server](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md") with an identifier in a URL format,
or a URL of your choosing. Values for this parameter must begin
with `https://`, `http://localhost`, or a
custom URL scheme like `myapp://`.

Resource binding is defined in [RFC 8707](https://www.rfc-editor.org/rfc/rfc8707.html "https://www.rfc-editor.org/rfc/rfc8707.html"). For more information about resource servers and resource binding, see [Resource binding](cognito-user-pools-define-resource-servers.md#cognito-user-pools-resource-binding "cognito-user-pools-define-resource-servers.md#cognito-user-pools-resource-binding").

## Example: authorization code

grant

This is an example request for an authorization code grant.

The following request initiates a session to retrieve an authorization code
that your user passes to your app at the `redirect_uri` destination.
This session requests scopes for user attributes and for access to Amazon Cognito
self-service API operations.

```
GET https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/authorize?
response_type=code&
client_id=`1example23456789`&
redirect_uri=https://`www.example.com`&
state=`abcdefg`&
scope=openid+profile+aws.cognito.signin.user.admin

```

The Amazon Cognito authentication server redirects back to your app with the
authorization code and state. The authorization code is valid for five
minutes.

```
HTTP/1.1 302 Found
Location: https://`www.example.com`?code=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111&state=`abcdefg`

```

## Example:

authorization code grant with PKCE

This example flow performs an authorization code grant with [PKCE](using-pkce-in-authorization-code.md#using-pkce-in-authorization-code.title "using-pkce-in-authorization-code.md#using-pkce-in-authorization-code.title").

This request adds a `code_challenge` parameter. To complete the
exchange of a code for a token, you must include the `code_verifier`
parameter in your request to the `/oauth2/token` endpoint.

```
GET https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/authorize?
response_type=code&
client_id=`1example23456789`&
redirect_uri=`https://www.example.com`&
state=`abcdefg`&
scope=aws.cognito.signin.user.admin&
code_challenge_method=S256&
code_challenge=`a1b2c3d4...`

```

The authorization server redirects back to your application with the
authorization code and state. Your application processes the authorization code
and exchanges it for tokens.

```
HTTP/1.1 302 Found
Location: `https://www.example.com`?code=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111&state=`abcdefg`

```

## Example: require

re-authentication with `prompt=login`

The following request adds a `prompt=login` parameter that requires
the user to authenticate again, even if they have an existing session.

```
GET https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/authorize?
response_type=code&
client_id=`1example23456789`&
redirect_uri=`https://www.example.com`&
state=`abcdefg`&
scope=`openid+profile+aws.cognito.signin.user.admin`&
prompt=login
```

The authorization server redirects to the [login
endpoint](login-endpoint.md "login-endpoint.md"), requiring re-authentication.

```
HTTP/1.1 302 Found Location: https://`mydomain.auth.us-east-1.amazoncognito.com`/login?response_type=code&client_id=`1example23456789`&redirect_uri=`https://www.example.com`&state=`abcdefg`&scope=`openid+profile+aws.cognito.signin.user.admin`&prompt=login
```

## Example: silent

authentication with `prompt=none`

The following request adds a `prompt=none` parameter that silently
checks if the user has a valid session.

```
GET https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/authorize?
response_type=code&
client_id=`1example23456789`&
redirect_uri=`https://www.example.com`&
state=`abcdefg`&
scope=`openid+profile+aws.cognito.signin.user.admin`&
prompt=none
```

When no valid session exists, the authorization server returns an error to the
redirect URI

```
HTTP/1.1 302 Found Location: https://`www.example.com`?error=login_required&state=`abcdefg`
```

When a valid session exists, the authorization server returns an authorization
code.

```
HTTP/1.1 302 Found Location: https://`www.example.com`?code=`AUTHORIZATION_CODE`&state=`abcdefg`
```

## Example: authorization code grant with resource binding

The following request adds a `resource` parameter to bind the
access token to a specific resource server. The resulting access token creates
the conditions for the target API to validate that it is the intended audience
of the authenticated user's request.

```
GET https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/authorize?
response_type=`code`&
client_id=`1example23456789`&
redirect_uri=`https://www.example.com`&
state=`abcdefg`&
scope=`solar-system-data-api.example.com/asteroids.add`&
resource=`https://solar-system-data-api.example.com`
```

The authorization server returns an authorization code that results in an
access token with an `aud` claim of
`https://solar-system-data-api.example.com`.

```
HTTP/1.1 302 Found Location: https://`www.example.com`?code=`AUTHORIZATION_CODE`&state=`abcdefg`
```

## Example: Token

(implicit) grant without `openid` scope

This example flow generates an implicit grant and returns JWTs directly to the
user's session.

The request is for an implicit grant from your authorization server. It
requests scopes in the access token that authorize user profile self-service
operations.

```
GET https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/authorize?
response_type=token&
client_id=`1example23456789`&
redirect_uri=`https://www.example.com`&
state=`abcdefg`&
scope=aws.cognito.signin.user.admin

```

The authorization server redirects back to your application with an access
token only. Because `openid` scope was not requested, Amazon Cognito doesn't
return an ID token. Also, Amazon Cognito doesn't return a refresh token in this
flow.

```
HTTP/1.1 302 Found
Location: `https://example.com/callback`#access_token=`eyJra456defEXAMPLE`&token_type=bearer&expires_in=`3600`&state=STATE

```

## Example: Token (implicit)

grant with `openid` scope

This example flow generates an implicit grant and returns tokens to the user's
browser.

The request is for an implicit grant from your authorization server. It
requests scopes in the access token that authorize access to user attributes and
self-service operations.

```
GET
https://mydomain.auth.us-east-1.amazoncognito.com/oauth2/authorize?
response_type=token&
client_id=`1example23456789`&
redirect_uri=`https://www.example.com`&
state=`abcdefg`&
scope=aws.cognito.signin.user.admin+openid+profile

```

The authorization server redirects back to your application with access token
and ID token (because `openid` scope was included):

```
HTTP/1.1 302 Found
Location: `https://www.example.com`#id_token=`eyJra67890EXAMPLE`&access_token=`eyJra12345EXAMPLE`&token_type=bearer&expires_in=`3600`&state=`abcdefg`

```

## Examples of negative responses

Amazon Cognito might deny your request. Negative requests come with an HTTP error code
and a description that you can use to correct your request parameters. The
following are examples of negative responses.

- If `client_id` and `redirect_uri` are valid, but
  the request parameters aren't formatted correctly, the authentication
  server redirects the error to the client's `redirect_uri` and
  appends an error message in a URL parameter. The following are examples
  of incorrect formatting.

      + The request doesn't include a `response_type`
       parameter.
      + The authorization request provided a
       `code_challenge` parameter, but not a
       `code_challenge_method` parameter.
      + The value of the `code_challenge_method` parameter
       isn't `S256`.

  The following is the response to an example request with incorrect
  formatting.

```
HTTP 1.1 302 Found Location: https://client_redirect_uri?error=invalid_request
```

- If the client requests `code` or `token` in
  `response_type`, but doesn't have permission for these
  requests, the Amazon Cognito authorization server returns
  `unauthorized_client` to client's
  `redirect_uri`, as follows:

```
HTTP 1.1 302 Found Location: https://client_redirect_uri?error=unauthorized_client
```

- If the client requests scope that is unknown, malformed, or not
  valid, the Amazon Cognito authorization server returns `invalid_scope`
  to the client's `redirect_uri`, as follows:

```
HTTP 1.1 302 Found Location: https://client_redirect_uri?error=invalid_scope
```

- If there is any unexpected error in the server, the authentication
  server returns `server_error` to the client's
  `redirect_uri`. Because the HTTP 500 error doesn't get
  sent to the client, the error doesn't display in the user's browser. The
  authorization server returns the following error.

```
HTTP 1.1 302 Found Location: https://client_redirect_uri?error=server_error
```

- When Amazon Cognito authenticates through federation to third-party IdPs, Amazon Cognito
  might experience connection issues, such as the following:
  - If a connection timeout occurs while requesting token from the
    IdP, the authentication server redirects the error to the
    client’s `redirect_uri` as follows:

  ```
  HTTP 1.1 302 Found Location: https://client_redirect_uri?error=invalid_request&error_description=Timeout+occurred+in+calling+IdP+token+endpoint
  ```

  - If a connection timeout occurs while calling the
    `jwks_uri` endpoint for ID token validation, the
    authentication server redirects with an error to the client’s
    `redirect_uri` as follows:

  ```
  HTTP 1.1 302 Found Location: https://client_redirect_uri?error=invalid_request&error_description=error_description=Timeout+in+calling+jwks+uri
  ```

- When authenticating by federating to third-party IdPs, the providers
  may return error responses. This can be due to configuration errors or
  other reasons, such as the following:
  - If an error response is received from other providers, the
    authentication server redirects the error to the client’s
    `redirect_uri` as follows:

  ```
  HTTP 1.1 302 Found Location: https://client_redirect_uri?error=invalid_request&error_description=[IdP name]+Error+-+[status code]+error getting token
  ```

  - If an error response is received from Google, the
    authentication server redirects the error to the client’s
    `redirect_uri` as follows:

  ```
  HTTP 1.1 302 Found Location: https://client_redirect_uri?error=invalid_request&error_description=Google+Error+-+[status code]+[Google-provided error code]
  ```

- When Amazon Cognito encounters an communication exception when it connects to
  an external IdP, the authentication server redirects with an error to
  the client's `redirect_uri` with either of the following
  messages:
  - ```
    HTTP 1.1 302 Found Location: https://client_redirect_uri?error=invalid_request&error_description=Connection+reset
    ```

  ````
  + ```
  HTTP 1.1 302 Found Location: https://client_redirect_uri?error=invalid_request&error_description=Read+timed+out
  ````
