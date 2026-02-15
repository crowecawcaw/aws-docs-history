# Auth0 by Okta

Auth0 can be configured as an identity provider for accessing AgentCore Gateway and
Runtime, or an AgentCore Identity credential provider for outbound resource access. This
allows your agents to authenticate and authorize agent users with Auth0 as the identity
provider and authorization server, or your agents to obtain credentials to access
resources authorized by Auth0.

## Inbound

To add Auth0 as an identity provider and authorization server for accessing
AgentCore Gateway and Runtime, you must:

- Configure discovery URL from your IDP directory. This helps AgentCore Identity get the
  metadata related to your OAuth authorization server and token verification
  keys.
- Enter valid `aud` claims for the token. This helps validate the
  tokens coming from your IDP and allows access for tokens that contain expected
  claims.

Use the following procedure to set up Auth0 and obtain the necessary configuration
values for Gateway authentication.

###### To configure Auth0 for inbound authentication

1. Create an API in Auth0:
   1. Sign in to your Auth0 dashboard.
   2. Open **APIs** and choose **Create
      API**.
   3. Enter a name and identifier for your API (e.g.,
      "gateway-api").
   4. Select the signing algorithm (RS256 recommended).
   5. Choose **Create**.

2. Configure API scopes:
   1. In the API settings, go to the **Scopes**
      tab.
   2. Add scopes such as "invoke:gateway" and "read:gateway".

3. Create an application:
   1. Open **Applications** and choose **Create
      Application**.
   2. Select **Machine to Machine Application**.
   3. Select the API you created in step 1.
   4. Authorize the application for the scopes you created.
   5. Choose **Create**.

4. Record the client ID and client secret from the application settings.
   You'll need these values to configure the Auth0 provider in
   AgentCore Identity.
5. Construct the discovery URL for your Auth0 tenant:

```
https://`your-domain`/.well-known/openid-configuration
```

Where `your-domain` is your Auth0
tenant domain (e.g., "dev-example.us.auth0.com"). 6. Configure Inbound Auth with the following values:

    1. **Discovery URL**: The URL
     constructed in the previous step
    2. **Allowed audiences**: The API
     identifier you created in step 1

## Outbound

To configure Auth0 as an outbound resource provider, use the following:

```
{
  "name": "NAME",
  "credentialProviderVendor": "Auth0Oauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`",
      "authorizationEndpoint": "https://`your-auth0-tenant`.auth0.com/authorize",
      "tokenEndpoint": "https://`your-auth0-tenant`.auth0.com/oauth/token",
      "issuer": "https://`your-auth0-tenant`.auth0.com"
    }
  }
}
```
