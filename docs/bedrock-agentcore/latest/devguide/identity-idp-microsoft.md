# Microsoft

Microsoft Entra ID can be configured as an identity provider for accessing
AgentCore Gateway and Runtime, or an AgentCore Identity credential provider for outbound resource
access. This allows your agents to authenticate and authorize agent users with Microsoft
Entra ID as the identity provider and authorization server, or your agents to obtain
credentials to access resources authorized by Microsoft Entra ID.

## Inbound

To add Microsoft Entra ID as an identity provider and authorization server for
accessing AgentCore Gateway and Runtime, you must:

- Configure discovery URL for your Microsoft Entra ID Tenant. This helps
  AgentCore Identity get the metadata related to your OAuth authorization server and token
  verification keys.
- Enter valid `aud` claims for the token. This helps validate the
  tokens coming from your IDP and allows access for tokens that contain the
  expected claims.

You can configure these as part of configuration of Gateway and Runtime inbound
configuration.

Before configuring Microsoft Entra ID as your identity provider, we recommend
completing the basic setup steps outlined in [Integrate with Google Drive using
OAuth2](identity-getting-started-google.md "identity-getting-started-google.md"). This ensures your development
environment and SDK are properly configured before adding identity provider
integration.

We support Microsoft Entra ID for v1.0 and v2.0 Access and ID tokens that do not
have any custom claims. You can determine which token versions your entra
application is issuing by parsing the JWT and looking at the `ver`
claim.

###### Note

**Multi-tenant application requirement:**
AgentCore currently supports only multi-tenant Microsoft Entra applications.
Single-tenant applications are not supported at this time. When configuring your
Microsoft Entra application, ensure that it is set up as a multi-tenant
application to work with AgentCore identity services.

For all token types, in your custom authorizer:

- **Discovery URL**: Discovery URL should be
  one of the following:
  - For v1.0 tokens use:
    `https://login.microsoftonline.com/`tenantId`/.well-known/openid-configuration`
  - For v2.0 tokens use:
    `https://login.microsoftonline.com/`tenantId`/v2.0/.well-known/openid-configuration`

- **Allowed audiences**: `aud`
  should be the Application Id.

### Configurations

specific for v1.0 Access Tokens

When fetching the token from Microsoft Entra:

- Include in authorization URL a scope like
  ``entra-application-id`/.default`
  alongside any other scopes your application might require. This allows
  Microsoft to know that you intend to use the access token against
  resources other than Microsoft's Graph API and will result in a token
  that can be validated by AgentCore Identity.

### Configurations

Specific for v2.0 AccessTokens

On Microsoft Entra:

- While configuring the application, go to the Application Manifest and
  add `accessTokenAcceptedVersion=2`.
- On the application, expose an API. The application ID URI and scopes
  can be whatever is necessary for your application; but, the scope must
  be included in the authorization URL when retrieving the access
  token.

### Configurations Specific for

v1.0 and v2.0 Id Tokens

On Microsoft Entra:

- While configuring the application, Enable ID Token Issuance in
  Application Registration.
- Include mandatory `openid` scope while calling the
  authorize and token endpoint for Microsoft Entra Id during Ingress
  Flows.

## Outbound

To configure the outbound Microsoft resource provider, use the following:

```
{
        "name": "NAME",
        "credentialProviderVendor": "MicrosoftOAuth2",
        "oauth2ProviderConfigInput": {
            "microsoftOauth2ProviderConfig": {
                "clientId": "`your-client-id`",
                "clientSecret": "`your-client-secret`",
                "tenantId": "`your-microsoft-entra-tenant`"
            }
        }
    }
```
