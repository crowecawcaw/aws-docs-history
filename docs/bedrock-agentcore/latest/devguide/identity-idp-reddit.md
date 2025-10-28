# Reddit

Reddit can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Reddit's OAuth2
service and obtain access tokens for Reddit API resources.

## Outbound

**Step 1**

Use the following procedure to set up a Reddit OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Reddit OAuth2 application

1. Open Reddit's developer console: [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps "https://www.reddit.com/prefs/apps").
2. Choose on **create an app**.
3. Select **web app** as the application type.
4. Configure the following as the redirect URI for the application:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

5. The client ID for the application is below the high-level summary of the
   application and the client secret is labelled **secret**.
   Note these values as you'll need it to configure the Reddit provider in
   AgentCore Identity.

For more details, refer to [Reddit's OAuth2
documentation](https://github.com/reddit-archive/reddit/wiki/oauth2 "https://github.com/reddit-archive/reddit/wiki/oauth2").

**Step 2**

To configure Reddit as an outbound resource provider, use the following:

```
{
  "name": "Reddit",
  "credentialProviderVendor": "RedditOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```
