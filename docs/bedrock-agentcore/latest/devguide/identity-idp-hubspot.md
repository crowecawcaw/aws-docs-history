# HubSpot

HubSpot can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through HubSpot's OAuth2
service and obtain access tokens for HubSpot API resources.

###### Note

HubSpot does not support the M2M/Client Credentials flow.

## Outbound

**Step 1**

Use the following procedure to set up a HubSpot OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a HubSpot OAuth2 application

1. Open the developer console for HubSpot.
2. In the main navigation bar, choose **Apps**.
3. Choose **Create App**.
4. Enter a name for your application.
5. Choose the **Auth** tab and enter the following as a
   Redirect URL:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

6. Configure any scopes that are required for your application.
7. Once your app has been created, go back to the **Auth**
   tab for your application.
8. Record the client ID and client secret, you'll need these when creating
   the HubSpot resource provider in AgentCore Identity.

For more details, refer to [HubSpot's OAuth quickstart guide](https://developers.hubspot.com/docs/apps/legacy-apps/authentication/oauth-quickstart-guide "https://developers.hubspot.com/docs/apps/legacy-apps/authentication/oauth-quickstart-guide").

**Step 2**

To configure HubSpot as an outbound resource provider, use the following:

```
{
  "name": "Hubspot",
  "credentialProviderVendor": "HubspotOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```

###### Note

When calling GetResourceOAuth2Token, the scopes must include
`oauth`.
