# Twitch

Twitch can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Twitch's OAuth2
service and obtain access tokens for Twitch API resources.

## Outbound

**Step 1**

Use the following procedure to set up a Twitch OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Twitch OAuth2 application

1. Sign in to the Twitch developer console.
2. Choose the **Applications** tab and then choose
   **Register your Application**.
3. Set a name for your application.
4. For the **OAuth Redirect URLs** field, use the
   following:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

5. Select the application category that is appropriate for the application
   you're developing (most likely this will be **Chat
   bot**).
6. Set **Client Type** as
   **Confidential**.
7. Choose **Create**.
8. On the application details page, record the client ID and client secret as
   you'll need this information for configuring the Twitch resource provider in
   AgentCore Identity.

For more details, refer to [Twitch's app
registration documentation](https://dev.twitch.tv/docs/authentication/register-app/ "https://dev.twitch.tv/docs/authentication/register-app/").

**Step 2**

To configure Twitch as an outbound resource provider, use the following:

```
{
  "name": "Twitch",
  "credentialProviderVendor": "TwitchOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```
