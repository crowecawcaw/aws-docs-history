# User pool endpoints and

managed login reference

Amazon Cognito has two models of user pool authentication: with the user pools API and with the
OAuth 2.0 authorization server. Use the API when you want to retrieve OpenID Connect (OIDC)
tokens with an AWS SDK in your application back end. Use the authorization server when you
want to implement your user pool as an OIDC provider. The authorization server adds features
like [federated sign-in](cognito-user-pools-identity-federation.md "cognito-user-pools-identity-federation.md"), [API and M2M authorization with
access token scopes](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md"), and [managed
login](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md"). You can use the API and OIDC models each on their own or together,
configured at the user pool level or at the [app client](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md") level. This section is a reference for the implementation of the OIDC
model. For more information about the two authentication models, see [Understanding API, OIDC, and managed login pages
authentication](authentication-flows-public-server-side.md#user-pools-API-operations "authentication-flows-public-server-side.md#user-pools-API-operations").

Amazon Cognito activates the public webpages listed here when you assign a domain to your user
pool. Your domain serves as a central access point for all of your app clients. They include
managed login, where your users can sign up and sign in ([Login endpoint](login-endpoint.md "login-endpoint.md")), and sign out ([Logout endpoint](logout-endpoint.md "logout-endpoint.md")). For more information about these resources, see
[User pool managed login](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md").

These pages also include the public web resources that allow your user pool to communicate
with third-party SAML, OpenID Connect (OIDC) and OAuth 2.0 identity providers (IdPs). To
sign in a user with a federated identity provider, your users must initiate a request to the
interactive managed login [Login endpoint](login-endpoint.md "login-endpoint.md") or
the OIDC [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md").
The Authorize endpoint redirects your users either to your managed login pages or your IdP
sign-in page.

Your app can also sign in _local users_ with the [Amazon Cognito user pools API](../../../cognito-user-identity-pools/latest/APIReference/Welcome.md "../../../cognito-user-identity-pools/latest/APIReference/Welcome.md"). A local user exists exclusively in your user pool
directory without federation through an external IdP.

In addition to managed login, Amazon Cognito integrates with SDKs for Android, iOS, JavaScript, and
more. The SDKs provide tools to perform user pool API operations with Amazon Cognito API service
endpoints. For more information about service endpoints, see [Amazon Cognito Identity endpoints and
quotas](../../../general/latest/gr/cognito_identity.md "../../../general/latest/gr/cognito_identity.md").

###### Warning

Don't pin the end-entity or intermediate Transport Layer Security (TLS) certificates
for Amazon Cognito domains. AWS manages all certificates for all of your user pool endpoints
and prefix domains. The certificate authorities (CAs) in the chain of trust that
supports Amazon Cognito certificates dynamically rotate and renew. When you pin your app to an
intermediate or leaf certificate, your app can fail without notice when AWS rotates
certificates.

Instead, pin your application to all available [Amazon root certificates](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/"). For
more information, see best practices and recommendations at [Certificate pinning](../../../acm/latest/userguide/acm-bestpractices.md#best-practices-pinning "../../../acm/latest/userguide/acm-bestpractices.md#best-practices-pinning") in the _AWS Certificate Manager User Guide_.

###### Topics

- [User-interactive managed login and classic
  hosted UI endpoints](managed-login-endpoints.md "managed-login-endpoints.md")
- [Identity provider and relying party
  endpoints](federation-endpoints.md "federation-endpoints.md")
- [OAuth 2.0 grants](federation-endpoints-oauth-grants.md "federation-endpoints-oauth-grants.md")
- [Using PKCE in authorization code
  grants](using-pkce-in-authorization-code.md "using-pkce-in-authorization-code.md")
- [Managed login and federation error
  responses](federation-endpoint-idp-responses.md "federation-endpoint-idp-responses.md")
