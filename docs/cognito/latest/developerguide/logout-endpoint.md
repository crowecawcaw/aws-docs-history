# The managed login sign-out endpoint:

`/logout`

The `/logout` endpoint is a redirection endpoint. It signs out the user
and redirects either to an authorized sign-out URL for your app client, or to the
`/login` endpoint. The available parameters in a GET request to the
`/logout` endpoint are tailored to Amazon Cognito managed login use
cases.

The logout endpoint is a front-end web application for interactive user sessions
with your customers. Your app must invoke this and other managed login endpoints in
your users' browsers.

To redirect your user to managed login to sign in again, add a
`redirect_uri` parameter to your request. A `logout`
request with a `redirect_uri` parameter must also include parameters for
your subsequent request to the [Login endpoint](login-endpoint.md "login-endpoint.md"), like `client_id`,
`response_type`, and `scope`.

To redirect your user to a page that you choose, add **Allowed sign-out
URLs** to your app client. In your users' requests to the
`logout` endpoint, add `logout_uri` and
`client_id` parameters. If the value of `logout_uri` is
one of the **Allowed sign-out URLs** for your app client, Amazon Cognito
redirects users to that URL.

With single logout (SLO) for SAML 2.0 IdPs, Amazon Cognito first redirects your user to the
SLO endpoint you defined in your IdP configuration. After your IdP redirects your
user back to `saml2/logout`, Amazon Cognito responds with one more redirect to the
`redirect_uri` or `logout_uri` from your request. For more
information, see [Signing out SAML users with
single sign-out](cognito-user-pools-saml-idp-sign-out.md "cognito-user-pools-saml-idp-sign-out.md").

The logout endpoint doesn't sign users out of OIDC or social identity providers
(IdPs). To sign users out from their session with an external IdP, direct them to
the sign-out page for that provider.

## GET /logout

The `/logout` endpoint only supports `HTTPS GET`. The
user pool client typically makes this request through the system browser. The
browser is typically Custom Chrome Tab in Android or Safari View Control in
iOS.

### Request parameters

_client_id_

The app client ID for your app. To get an app client ID, you
must register the app in the user pool. For more information,
see [Application-specific settings with app
clients](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md").

Required.

_logout_uri_

Redirect your user to a custom sign-out page with a _logout_uri_ parameter. Set its value
to the app client **sign-out URL** where you
want to redirect your user after they sign out. Use _logout_uri_ only with a _client_id_ parameter. For more
information, see [Application-specific settings with app
clients](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md").

You can also use the _logout_uri_ parameter to redirect your user to
the sign-in page for another app client. Set the sign-in page
for the other app client as an **Allowed callback
URL** in your app client. In your request to the
`/logout` endpoint, set the value of the
_logout_uri_ parameter to
the URL-encoded sign-in page.

Amazon Cognito requires either a _logout_uri_ or a _redirect_uri_ parameter in your request to the
`/logout` endpoint. A _logout_uri_ parameter redirects your user to
another website. If both _logout_uri_ and _redirect_uri_ parameters are included in your
request to the `/logout` endpoint, Amazon Cognito will utilize
the _logout_uri_ parameter
exclusively, overriding the _redirect_uri_ parameter.

_`nonce`_

(Optional) A random value that you can add to the request. The
nonce value that you provide is included in the ID token that
Amazon Cognito issues. To guard against replay attacks, your app can
inspect the `nonce` claim in the ID token and compare
it to the one you generated. For more information about the
`nonce` claim, see [ID token validation](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation "https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation") in the _OpenID Connect standard_.

**redirect_uri**

Redirect your user to your sign-in page to authenticate with a
_redirect_uri_ parameter.
Set its value to the app client **Allowed callback
URL** where you want to redirect your user after
they sign in again. Add _client_id_, _scope_, _state_,
and _response_type_ parameters
that you want to pass to your `/login`
endpoint.

Amazon Cognito requires either a _logout_uri_ or a _redirect_uri_ parameter in your request to the
`/logout` endpoint. To redirect your user to your
`/login` endpoint to reauthenticate and pass
tokens to your app, add a _redirect_uri_ parameter. If both _logout_uri_ and _redirect_uri_ parameters are
included in your request to the `/logout` endpoint,
Amazon Cognito overrides the _redirect_uri_ parameter and processes the
_logout_uri_ parameter
exclusively.

_response_type_

The OAuth 2.0 response that you want to receive from Amazon Cognito
after your user signs in. `code` and
`token` are the valid values for the _response_type_ parameter.

Required if you use a _redirect_uri_ parameter.

_state_

When your application adds a _state_ parameter to a request, Amazon Cognito returns its
value to your app when the `/oauth2/logout` endpoint
redirects your user.

Add this value to your requests to guard against [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery "https://en.wikipedia.org/wiki/Cross-site_request_forgery") attacks.

You can't set the value of a `state` parameter to a
URL-encoded JSON string. To pass a string that matches this
format in a `state` parameter, encode the string to
base64, then decode it in your application.

Strongly recommended if you use a _redirect_uri_ parameter.

_scope_

The OAuth 2.0 scopes that you want to request from Amazon Cognito after
you sign them out with a _redirect_uri_ parameter. Amazon Cognito redirects your
user to the `/login` endpoint with the _scope_ parameter in your request to
the `/logout` endpoint.

Optional if you use a _redirect_uri_ parameter. If you don't include a
_scope_ parameter, Amazon Cognito
redirects your user to the `/login` endpoint with a
_scope_ parameter. When
Amazon Cognito redirects your user and automatically populates
`scope`, the parameter includes all authorized
scopes for your app client.

### Example requests

**Example – log out and redirect user to
client**

Amazon Cognito redirects user sessions to the URL in the value of
`logout_uri`, ignoring all other request parameters, when
requests include `logout_uri` and `client_id`. This
URL must be an authorized sign-out URL for the app client.

The following is an example request for sign-out and redirect to
`https://www.example.com/welcome`.

```
GET https://mydomain.auth.us-east-1.amazoncognito.com/logout?
  client_id=1example23456789&
  logout_uri=https%3A%2F%2Fwww.example.com%2Fwelcome
```

**Example – log out and prompt the user to sign
in as another user**

When requests omit `logout_uri` but otherwise provide the
parameters that make up a well-formed request to the authorize endpoint,
Amazon Cognito redirects users to managed login sign-in. The logout endpoint appends
the parameters in your original request to the redirect destination.

The additional parameters that you add to the logout request must be in
the list at [Request parameters](#get-logout-request-parameters "#get-logout-request-parameters"). For example, the logout
endpoint doesn't support automatic IdP redirect with
`identity_provider` or `idp_identifier`
parameters. The parameter `redirect_uri` in a request to the
logout endpoint is not a sign-out URL, but a post-sign-in URL that you want
to pass through to the authorize endpoint.

The following is an example request that signs a user out, redirects to
the sign-in page, and provides an authorization code to
`https://www.example.com` after sign-in.

```
GET https://mydomain.auth.us-east-1.amazoncognito.com/logout?
  response_type=code&
  client_id=1example23456789&
  redirect_uri=https%3A%2F%2Fwww.example.com&
  state=example-state-value&
  nonce=example-nonce-value&
  scope=openid+profile+aws.cognito.signin.user.admin
```
