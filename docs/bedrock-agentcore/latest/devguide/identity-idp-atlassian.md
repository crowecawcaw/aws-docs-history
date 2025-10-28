# Atlassian

Atlassian can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Atlassian's
OAuth2 service and obtain access tokens for Atlassian API resources.

## Outbound

**Step 1**

Use the following procedure to set up an Atlassian OAuth2 application and obtain
the necessary client credentials for AgentCore Identity.

###### To configure an Atlassian OAuth2 application

1. Open Atlassian's developer console and register for a developer
   account.
2. Create a new application.
3. Select authorization and next to **OAuth 2.0
   (3LO)** select **Configure**.
4. Enter the following as a callback URL for the app:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

5. Choose **Save changes**.
6. Select **Permissions** and choose the
   permissions relevant to your application.

For more details, refer to [Atlassian's OAuth 2.0 (3LO) apps documentation](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/ "https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/").

**Step 2**

To configure Atlassian as an outbound resource provider, use the following:

```
{
   "name": "NAME",
   "credentialProviderVendor": "AtlassianOAuth2",
   "oauth2ProviderConfigInput": {
       "atlassianOauth2ProviderConfig": {
           "clientId": "`your-client-id`",
           "clientSecret": "`your-client-secret`"
       }
   }
}
```
