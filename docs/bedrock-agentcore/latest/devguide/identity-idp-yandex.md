# Yandex

Yandex can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Yandex's OAuth2
service and obtain access tokens for Yandex API resources.

## Outbound

**Step 1**

Use the following procedure to set up a Yandex OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Yandex OAuth2 application

1. Open the developer console for Yandex at [https://oauth.yandex.com/](https://oauth.yandex.com/ "https://oauth.yandex.com/").
2. Choose **Create app**.
3. Provide a name for your application.
4. For platforms, select **Web services**.
5. Choose **Save and Continue**.
6. Select the permissions necessary for your application and then choose
   **Save and Continue**.
7. Configure the following as the redirect URI for the application:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

8. Choose **Save and Continue**.
9. Once the client has been created, note the client ID and client secret
   assigned to your application as you'll need them for configuring the Yandex
   provider in AgentCore Identity.

For more details, refer to [Yandex's
OAuth documentation](https://yandex.com/dev/id/doc/en/ "https://yandex.com/dev/id/doc/en/").

**Step 2**

To configure Yandex as an outbound resource provider, use the following:

```
{
  "name": "Yandex",
  "credentialProviderVendor": "YandexOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```
