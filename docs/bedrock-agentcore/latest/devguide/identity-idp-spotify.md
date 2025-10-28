# Spotify

Spotify can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Spotify's OAuth2
service and obtain access tokens for Spotify API resources.

## Outbound

**Step 1**

Use the following procedure to set up a Spotify OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Spotify OAuth2 application

1. Open the developer dashboard for Spotify.
2. Choose **Create an App**.
3. Provide a name and description for your application.
4. Use the following as the **Redirect URI** for your
   application:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

5. Select **Web API** for the API/SDKs that you intend to
   use for Spotify.
6. Choose **Save**.
7. On the application overview page, choose
   **Settings**.
8. On the **Basic Information** tab, record the client ID
   and client secret. You'll need these values for configuring the Spotify
   resource provider in AgentCore Identity.

**Step 2**

To configure Spotify as an outbound resource provider, use the following:

```
{
  "name": "Spotify",
  "credentialProviderVendor": "SpotifyOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```
