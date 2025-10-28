# Notion

Notion can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Notion's OAuth2
service and obtain access tokens for Notion API resources.

## Outbound

**Step 1**

Use the following procedure to set up a Notion OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Notion OAuth2 application

1. Open [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations "https://www.notion.so/my-integrations").
2. Choose **+ New integration**.
3. Choose **Public integration**.
4. Provide a name for your integration.
5. Choose **Submit**.
6. On the integration details page, open the **OAuth Domain &
   URIs** section and add the following as a redirect URI:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

7. Record the OAuth client ID and OAuth client secret as you'll need this
   information to configure the Notion resource provider in AgentCore Identity.

For more details, refer to [Notion's authorization
documentation](https://developers.notion.com/docs/authorization "https://developers.notion.com/docs/authorization").

**Step 2**

To configure Notion as an outbound resource provider, use the following:

```
{
  "name": "Notion",
  "credentialProviderVendor": "NotionOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```
