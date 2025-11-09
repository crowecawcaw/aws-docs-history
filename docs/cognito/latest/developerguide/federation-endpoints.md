# Identity provider and relying party

endpoints

_Federation endpoints_ are user pool endpoints serve
a purpose for one of the authentication standards used by user pools. They include SAML
ACS URLs, OIDC discovery endpoints, and service endpoints for user pool roles both as
identity provider and relying party. Federation endpoints initiate authentication flows,
receive proof of authentication from IdPs, and issue tokens to clients. They interact
with IdPs, applications, and administrators, but not with users.

The full-page topics after this page have details about the OAuth 2.0 and OIDC
provider endpoints that become available when you add a domain to your user pool. The
following chart is a list of all federation endpoints.

Examples of [user pool domains](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md")
are:

1. Prefix domain: `mydomain.auth.us-east-1.amazoncognito.com`
2. Custom domain: `auth.example.com`

| User pool federation endpoints                                                                     | Endpoint URL                                                                                                                                                                                                                                                   | Description                                                                                                                                                                   | How it's accessed |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| https://`Your user pool<br>domain`/oauth2/authorize                                                | Redirects a user to either managed login or to sign in with their<br>IdP.                                                                                                                                                                                      | Invoked in customer browser to begin user authentication. See [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md").                                    |
| https://`Your user pool<br>domain`/oauth2/token                                                    | Returns tokens based on an authorization code or client credentials<br>request.                                                                                                                                                                                | Requested by app to retrieve tokens. See [Token endpoint](token-endpoint.md "token-endpoint.md").                                                                             |
| https://`Your user pool<br>domain`/oauth2/userInfo                                                 | Returns user attributes based on OAuth 2.0 scopes and user identity<br>in an access token.                                                                                                                                                                     | Requested by app to retrieve user profile. See [userInfo endpoint](userinfo-endpoint.md "userinfo-endpoint.md").                                                              |
| https://`Your user pool<br>domain`/oauth2/revoke                                                   | Revokes a refresh token and the associated access tokens.                                                                                                                                                                                                      | Requested by app to revoke a token. See [Revoke endpoint](revocation-endpoint.md "revocation-endpoint.md").                                                                   |
| https://cognito-idp.`Region`.amazonaws.com/`your<br>user pool ID`/.well-known/openid-configuration | A directory of the OIDC architecture of your user pool.[1](#cognito-federation-oidc-discovery-note "#cognito-federation-oidc-discovery-note")                                                                                                                  | Requested by app to locate user pool issuer metadata.                                                                                                                         |
| https://cognito-idp.`Region`.amazonaws.com/`your<br>user pool ID`/.well-known/jwks.json            | Public keys that you can use to validate Amazon Cognito tokens.[2](#cognito-federation-oidc-jwks-note "#cognito-federation-oidc-jwks-note")                                                                                                                    | Requested by app to verify JWTs.                                                                                                                                              |
| https://`Your user pool<br>domain`/oauth2/idpresponse                                              | Social identity providers must redirect your users to this endpoint<br>with an authorization code. Amazon Cognito redeems the code for a token when it<br>authenticates your federated user.                                                                   | Redirected from OIDC IdP sign-in as the IdP client callback<br>URL.                                                                                                           |
| https://`Your user pool<br>domain`/saml2/idpresponse                                               | The Assertion Consumer Response (ACS) URL for integration with SAML<br>2.0 identity providers.                                                                                                                                                                 | Redirected from SAML 2.0 IdP as the ACS URL, or the origination point<br>for IdP-initiated sign-in[3](#cognito-federation-idp-init-note "#cognito-federation-idp-init-note"). |
| https://`Your user pool<br>domain`/saml2/logout                                                    | The [Single<br>Logout](cognito-user-pools-saml-idp-sign-out.md#cognito-user-pools-saml-idp-sign-out.title "cognito-user-pools-saml-idp-sign-out.md#cognito-user-pools-saml-idp-sign-out.title") (SLO) URL for integration with SAML 2.0 identity<br>providers. | Redirected from SAML 2.0 IdP as the single logout (SLO) URL. Accepts<br>POST binding only.                                                                                    |

1 The `openid-configuration` document might be updated at any time with additional information that keeps the endpoint compliant with the OIDC and OAuth2 specifications.

2The `jwks.json` JSON file might be updated at any time to with new public token signing keys.

3 For more information about IdP-initiated SAML
sign-in, see [Implement IdP-initiated SAML sign-in](cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-SAML-session-initiation-idp-initiation "cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-SAML-session-initiation-idp-initiation").

For more information on the OpenID Connect and OAuth standards, see [OpenID Connect
1.0](http://openid.net/specs/openid-connect-core-1_0.html "http://openid.net/specs/openid-connect-core-1_0.html") and [OAuth
2.0](https://tools.ietf.org/html/rfc6749 "https://tools.ietf.org/html/rfc6749").

###### Topics

- [The redirect and authorization
  endpoint](authorization-endpoint.md "authorization-endpoint.md")
- [The token issuer endpoint](token-endpoint.md "token-endpoint.md")
- [The user attributes endpoint](userinfo-endpoint.md "userinfo-endpoint.md")
- [The token revocation endpoint](revocation-endpoint.md "revocation-endpoint.md")
- [The IdP SAML assertion
  endpoint](saml2-idpresponse-endpoint.md "saml2-idpresponse-endpoint.md")
