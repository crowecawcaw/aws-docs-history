

# Identity provider and relying party endpoints
<a name="federation-endpoints"></a>

*Federation endpoints* are user pool endpoints that serve a purpose for one of the authentication standards used by user pools. They include SAML ACS URLs, OIDC discovery endpoints, and service endpoints for user pool roles both as identity provider and relying party. Federation endpoints initiate authentication flows, receive proof of authentication from IdPs, and issue tokens to clients. They interact with IdPs, applications, and administrators, but not with users.

The full-page topics after this page have details about the OAuth 2.0 and OIDC provider endpoints that become available when you add a domain to your user pool. The following chart is a list of all federation endpoints.

Examples of [user pool domains](cognito-user-pools-assign-domain.md) are:

1. Prefix domain: `mydomain.auth.us-east-1.amazoncognito.com`

1. Custom domain: `auth.example.com`


**User pool federation endpoints**  

| Endpoint URL | Description | How it's accessed | 
| --- | --- | --- | 
| https://{{Your user pool domain}}/oauth2/authorize | Redirects a user to either managed login or to sign in with their IdP. | Invoked in customer browser to begin user authentication. See [Authorize endpoint](authorization-endpoint.md). | 
| https://{{Your user pool domain}}/oauth2/token | Returns tokens based on an authorization code or client credentials request. | Requested by app to retrieve tokens. See [Token endpoint](token-endpoint.md). | 
| https://{{Your user pool domain}}/oauth2/userInfo | Returns user attributes based on OAuth 2.0 scopes and user identity in an access token. | Requested by app to retrieve user profile. See [userInfo endpoint](userinfo-endpoint.md). | 
| https://{{Your user pool domain}}/oauth2/revoke | Revokes a refresh token and the associated access tokens. | Requested by app to revoke a token. See [Revoke endpoint](revocation-endpoint.md). | 
| https://cognito-idp.{{Region}}.amazonaws.com/{{your user pool ID}}/.well-known/openid-configuration | A directory of the OIDC architecture of your user pool.[1](#cognito-federation-oidc-discovery-note) | Requested by app to locate user pool issuer metadata. | 
| https://cognito-idp.{{Region}}.amazonaws.com/{{your user pool ID}}/.well-known/jwks.json | Public keys that you can use to validate Amazon Cognito tokens.[2](#cognito-federation-oidc-jwks-note) | Requested by app to verify JWTs. | 
| https://{{Your user pool domain}}/oauth2/idpresponse | Social identity providers must redirect your users to this endpoint with an authorization code. Amazon Cognito redeems the code for a token when it authenticates your federated user. | Redirected from OIDC IdP sign-in as the IdP client callback URL. | 
| https://{{Your user pool domain}}/saml2/idpresponse | The Assertion Consumer Response (ACS) URL for integration with SAML 2.0 identity providers. | Redirected from SAML 2.0 IdP as the ACS URL, or the origination point for IdP-initiated sign-in[3](#cognito-federation-idp-init-note). | 
| https://{{Your user pool domain}}/saml2/logout | The [Single Logout](cognito-user-pools-saml-idp-sign-out.md#cognito-user-pools-saml-idp-sign-out.title) (SLO) URL for integration with SAML 2.0 identity providers. | Redirected from SAML 2.0 IdP as the single logout (SLO) URL. Accepts POST binding only. | 

1 The `openid-configuration` document might be updated at any time with additional information that keeps the endpoint compliant with the OIDC and OAuth2 specifications.

2The `jwks.json` JSON file might be updated at any time to with new public token signing keys.

3 For more information about IdP-initiated SAML sign-in, see [Implement IdP-initiated SAML sign-in](cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-SAML-session-initiation-idp-initiation).

For more information on the OpenID Connect and OAuth standards, see [OpenID Connect 1.0](http://openid.net/specs/openid-connect-core-1_0.html) and [OAuth 2.0](https://tools.ietf.org/html/rfc6749).

## Amazon Cognito user pools as an OIDC issuer
<a name="user-pool-oidc-issuer"></a>

Amazon Cognito user pools function as OpenID Connect (OIDC) identity providers, serving as an issuer that application libraries can use for OIDC federation. Application libraries for OIDC federation can reference the two different paths as discussed below as an autodiscovery endpoint. This endpoint provides access to the JSON Web Key Set (JWKS) at `/.well-known/jwks.json` and OIDC discovery metadata at `/.well-known/openid-configuration`, where applications can discover the authorization, token, and userInfo endpoints.

Applications that support OIDC autodiscovery can automatically configure themselves by querying these well-known endpoints. For applications that don't support autodiscovery, you can hardcode your application with the specific OIDC endpoints that are listed in the previous section.User pool issuer types

**Original issuer**  
The current default issuer configuration for user pools. The issuer URL is hosted in the user pool's Region and provides OIDC endpoints specific to that Region.  
Original issuers take the format `https://cognito-idp.{{us-east-1}}.amazonaws.com/{{us-east-1_EXAMPLE}}`.

**Updated issuer**  
Recommended for all user pools, including for multi-Region replication. Updated issuers host the same JWKS content in multiple Regions, resulting in improved resilience and efficiency.  
Updated issuers take the format `https://issuer-cognito-idp.{{us-east-1}}.amazonaws.com/{{us-east-1_EXAMPLE}}`, where {{Region}} is the primary AWS Region of your user pool.  
The updated issuer type is not currently compatible with Application Load Balancer authentication with Amazon Cognito ([Authenticate users using an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html)) or Amazon API Gateway Amazon Cognito authorizers ([Control access to REST APIs using Amazon Cognito user pools as authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html)).

**Topics**
+ [Amazon Cognito user pools as an OIDC issuer](#user-pool-oidc-issuer)
+ [The redirect and authorization endpoint](authorization-endpoint.md)
+ [The token issuer endpoint](token-endpoint.md)
+ [The user attributes endpoint](userinfo-endpoint.md)
+ [The token revocation endpoint](revocation-endpoint.md)
+ [The IdP SAML assertion endpoint](saml2-idpresponse-endpoint.md)