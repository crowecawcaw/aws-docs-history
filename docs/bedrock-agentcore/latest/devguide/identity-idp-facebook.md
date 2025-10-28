# Facebook

Facebook can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Facebook's OAuth2
service and obtain access tokens for Facebook API resources.

## Outbound

**Step 1**

Use the following procedure to set up a Facebook OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Facebook OAuth2 application

1. Create a [developer account with Facebook](https://developers.facebook.com/docs/facebook-login "https://developers.facebook.com/docs/facebook-login").
2. [Sign in](https://developers.facebook.com/ "https://developers.facebook.com/") with your
   Facebook credentials.
3. From the **My Apps** menu, choose **Create New
   App**.

###### Note

If you don't have an existing Facebook app, you will see a different
option. Choose **Create App**. 4. On the **Create an app** page, choose a use case for your
app, and then choose **Next**. 5. Enter a name for your Facebook app and choose **Create
App**. 6. On the left navigation bar, choose **App Settings**, and
then choose **Basic**. 7. Record the **App ID** and the **App
Secret**. You will use them for configuring the Facebook
provider in AgentCore Identity. 8. Choose **+ Add platform** from the bottom of the
page. 9. On the **Select Platform** screen, select your platforms,
and then choose **Next**. 10. Choose **Save changes**. 11. For **App Domains**, enter the domain of your application
and
`bedrock-agentcore.`region`.amazonaws.com`. 12. Choose **Save changes**. 13. From the navigation bar, choose **Products**, and then
choose **Configure** from **Facebook
Login**. 14. From the **Facebook Login**
**Configure** menu, choose
**Settings**. 15. Enter the following redirect URL into **Valid OAuth Redirect
URIs**:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

16. Choose **Save changes**.

**Step 2**

To configure Facebook as an outbound resource provider, use the following:

```
{
  "name": "Facebook",
  "credentialProviderVendor": "FacebookOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`"
    }
  }
}
```
