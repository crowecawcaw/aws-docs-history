# OneLogin

OneLogin can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through OneLogin's OAuth2
service and obtain access tokens for OneLogin API resources.

## Outbound

**Step 1**

Use the following procedure to set up a OneLogin OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a OneLogin OAuth2 application

1. Open the OneLogin Administration panel.
2. Add a new app.
3. Search for OIDC and select the OpenId Connect app.
4. Choose a name for your application and choose **Save**.
5. On the page for the app, go to the **Configuration** tab and add the following as a redirect
   URI:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

6. Open the **SSO** tab and note the client ID
   and client secret as you'll need these to configure the OneLogin app in
   AgentCore Identity.
7. Change the Token endpoint authentication method to **POST**.
8. Choose **Save**.

**Step 2**

To configure OneLogin as an outbound resource provider use the following:

```
{
  "name": "OneLogin",
  "credentialProviderVendor": "OneLoginOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`",
      "authorizationEndpoint": "https://`your-tenant`.onelogin.com/oidc/2/auth",
      "tokenEndpoint": "https://`your-tenant`.onelogin.com/oidc/2/token",
      "issuer": "https://`your-tenant`.onelogin.com/oidc/2"
    }
  }
}
```
