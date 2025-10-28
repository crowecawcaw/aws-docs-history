# The IdP SAML assertion

endpoint

The `/saml2/idpresponse` receives SAML assertions. In
service-provider-initiated (SP-initiated) sign-in, your application doesn't interact
directly with this endpoint—your SAML 2.0 identity provider (IdP) redirects
your user here with their SAML response. For SP-initiated sign-in, configure your
IdP with the path to your `saml2/idpresponse` as the assertion consumer
service (ACS) URL. For more information about session initiation, see [SAML session initiation
in Amazon Cognito user pools](cognito-user-pools-SAML-session-initiation.md "cognito-user-pools-SAML-session-initiation.md").

In IdP-initiated sign-in, invoke requests to this endpoint in your application
after you sign in user with your SAML 2.0 provider. Your users sign in with your IdP
in their browser, then your application collects the SAML assertion and submits it
to this endpoint. You must submit SAML assertions in the body of a `HTTP
 POST` request over HTTPS. The body of your `POST` request must
be a `SAMLResponse` parameter and a `Relaystate` parameter.
For more information, see [Implement IdP-initiated SAML sign-in](cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-SAML-session-initiation-idp-initiation "cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-SAML-session-initiation-idp-initiation").

The `saml2/idpresponse` endpoint can accept SAML assertions of up to
100,000 characters in length.

## POST

`/saml2/idpresponse`

To use the `/saml2/idpresponse` endpoint in an IdP-initiated
sign-in, generate a POST request with parameters that provide your user pool
with information about your user's session.

- The app client that they want to sign in to.
- The callback URL that they want to end up at.
- The OAuth 2.0 scopes that they want to request in your user's access
  token.
- The IdP that initiated the sign-in request.

### IdP-initiated

request body parameters

_SAMLResponse_

A Base64-encoded SAML assertion from an IdP associated with a
valid app client and IdP configuration in your user pool.

_RelayState_

A `RelayState` parameter contains the request
parameters that you would otherwise pass to the
`oauth2/authorize` endpoint. For detailed
information about these parameters, see [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md").

_response_type_

The OAuth 2.0 grant type.

_client_id_

The app client ID.

_redirect_uri_

The URL where the authentication server redirects
the browser after Amazon Cognito authorizes the user.

_identity_provider_

The name of the identity provider where you want
to redirect your user.

_idp_identifier_

The identifier of the identity provider where you
want to redirect your user.

_scope_

The OAuth 2.0 scopes that you want your user to
request from the authorization server.

### Example requests

with positive responses

###### Example – POST request

The following request is for an authorization code grant for a user
from IdP `MySAMLIdP` in app client
`1example23456789`. The user redirects to
`https://www.example.com` with their authorization code,
which can be exchanged for tokens that include an access token with the
OAuth 2.0 scopes `openid`, `email`, and
`phone`.

```
POST /saml2/idpresponse HTTP/1.1
User-Agent: `USER_AGENT`
Accept: */*
Host: `example.auth.us-east-1.amazoncognito.com`
Content-Type: application/x-www-form-urlencoded

SAMLResponse=`[Base64-encoded SAML assertion]`&RelayState=identity_provider%3D`MySAMLIdP`%26client_id%3D`1example23456789`%26redirect_uri%3D`https%3A%2F%2Fwww.example.com`%26response_type%3D`code`%26scope%3D`email%2Bopenid%2Bphone`
```

###### Example – response

The following is the response to the previous request.

```
HTTP/1.1 302 Found
Date: Wed, 06 Dec 2023 00:15:29 GMT
Content-Length: 0
x-amz-cognito-request-id: 8aba6eb5-fb54-4bc6-9368-c3878434f0fb
Location: `https://www.example.com`?code=`[Authorization code]`
```
