# X

X can be configured as an AgentCore Identity credential provider for outbound resource
access. This allows your agents to authenticate users through X's OAuth2 service and
obtain access tokens for X API resources.

## Outbound

**Step 1**

Use the following procedure to set up a X OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure an X OAuth2 application

1. Open the X developer portal.
2. In the left navigation bar, choose **Project &
   Apps**.
3. Choose on the X project you've created for the application.
4. Under the **Apps** header choose **Add an App**.
5. Choose **Create new**.
6. Provide a name and description for your application.
7. In the left navigation bar, choose the application that was just
   generated.
8. On the app details page for your new app, choose **Edit** in the User Authentication settings.
9. Select the **App permissions** necessary for
   your application.
10. For **Type of App** select **Web App, Automated App or Bot**.
11. Under **App Info** enter the following as the
    callback URL:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

12. For **Website URL** enter the URL for your
    application.
13. Choose **Save**.
14. Under the **Keys and token** tab for your
    application, go to the **OAuth 2.0 Client ID and Client
    Secret**.
15. Choose **Generate** and note the client ID
    and secret that get generated as you'll need this information to configure
    the X resource provider in AgentCore Identity.

###### Note

X only displays the full client secret when it is generated, if you lose this
information you'll need to re-generate the client secret in the X developer
portal.

For more details, refer to [X's
OAuth 2.0 documentation](https://docs.x.com/fundamentals/authentication/oauth-2-0/overview "https://docs.x.com/fundamentals/authentication/oauth-2-0/overview").

**Step 2**

To configure X as an outbound resource provider, use the following:

```
{
  "name": "X",
  "credentialProviderVendor": "XOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```
