# Dropbox

Dropbox can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Dropbox's OAuth2
service and obtain access tokens for Dropbox API resources.

###### Note

Dropbox does not support the M2M/Client Credentials flow.

## Outbound

**Step 1**

Use the following procedure to set up a Dropbox OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Dropbox OAuth2 application

1. Open the developer **App Console** for Dropbox.
2. Choose **Create app**.
3. Choose **Scoped access**.
4. For the access type, choose the access type appropriate for your
   application.
5. Provide a name for your application.
6. Choose **Create app**.
7. On the app overview page, open the OAuth2 section and add the following as
   a redirect URI:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

8. In the same section choose the dropdown below **Allow public
   clients (Implicit Grant & PKCE)** and choose
   **Disallow** in the options.
9. Record the app key and app secret as you'll need the information to
   configure the Dropbox resource provider in AgentCore Identity.
10. In the **Permissions** tab for the application, select
    the scopes that are needed for your application.

For more details, refer to [Dropbox's
OAuth implementation guide](https://developers.dropbox.com/oauth-guide#implementing-oauth "https://developers.dropbox.com/oauth-guide#implementing-oauth").

**Step 2**

To configure Dropbox as an outbound resource provider, use the following:

```
{
  "name": "DropBox",
  "credentialProviderVendor": "DropboxOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```
