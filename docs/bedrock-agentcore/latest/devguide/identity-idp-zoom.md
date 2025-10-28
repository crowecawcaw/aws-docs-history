# Zoom

Zoom can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Zoom's OAuth2
service and obtain access tokens for Zoom API resources.

## Outbound

###### Note

You can only configure a Zoom OAuth2 application as either a user federation
or M2M OAuth2 client but not both.

**Step 1**

Use the following procedure to set up a Zoom OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Zoom OAuth2 application

1. Sign in to the Zoom App Marketplace.
2. Choose **Develop** > **Build
   App**.
3. For a user federation app, select **General app** and
   choose **Create**.
   - On the app details page, add a name for your application and
     select how your application will be managed.
   - In the **OAuth Information** section, for both
     the OAuth Redirect URL and OAuth Allow Lists sections, use the
     following as the redirect URL for the application:

   ```
   https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
   ```

4. For a M2M app, select **Server to Server OAuth App** and
   choose **Create**.
   - Add a name for your application.
   - On the app details page, choose **Scopes** and
     add the necessary scopes for your application.
   - Open **Information** and provide a company name,
     and developer contact information.

5. Record the client ID and client secret that have been generated for your
   application. You'll need these values to configure the Zoom credential
   provider in AgentCore Identity.

For more details, refer to [Zoom's integration
documentation](https://developers.zoom.us/docs/integrations/create/ "https://developers.zoom.us/docs/integrations/create/").

**Step 2**

To configure Zoom as an outbound resource provider, use the following:

```
{
  "name": "Zoom",
  "credentialProviderVendor": "ZoomOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```
