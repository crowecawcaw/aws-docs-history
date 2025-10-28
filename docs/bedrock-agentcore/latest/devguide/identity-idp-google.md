# Google

Google can be configured as an AgentCore Identity credential provider for outbound resource
access. This allows your agents to authenticate users through Google's OAuth2 service
and obtain access tokens for Google API resources.

## Outbound

**Step 1**

Use the following procedure to set up a Google OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Google OAuth2 application

1. Create a [developer
   account with Google](https://developers.google.com/identity "https://developers.google.com/identity").
2. Sign in to the [Google Cloud
   Platform console](https://console.cloud.google.com/home/dashboard "https://console.cloud.google.com/home/dashboard").
3. From the top navigation bar, choose **Select a project**.
   If you already have a project in the Google platform, this menu displays
   your default project instead.
4. Choose **NEW PROJECT**.
5. Enter a name for your product and then choose
   **CREATE**.
6. On the left navigation bar, choose **APIs and Services**,
   and then choose **OAuth consent screen**.
7. Enter the app information, an **App domain**,
   **Authorized domains**, and **Developer contact
   information**. Your **Authorized domains**
   must include
   `bedrock-agentcore.`region`.amazonaws.com`.
   Choose **SAVE AND CONTINUE**.
8. Under **Scopes**, choose **Add or remove
   scopes**, and then choose the scopes necessary for your
   application.
9. Expand the left navigation bar again, choose **APIs and
   Services**, and then choose
   **Credentials**.
10. Choose **CREATE CREDENTIALS**, and then choose
    **OAuth client ID**.
11. Choose an **Application type** and give your client a
    **Name**.
12. Under **Authorized redirect URIs**, choose **ADD
    URI**. Enter the following:
    - `https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback`

13. Choose **CREATE**.
14. Securely store the values that Google displays under **Your client
    ID** and **Your client secret**. Provide these
    values to AgentCore Identity when you add a Google credential provider.

**Step 2**

To configure the outbound Google resource provider, use the following:

```
{
        "name": "NAME",
        "credentialProviderVendor": "GoogleOauth2",
        "oauth2ProviderConfigInput": {
            "GoogleOauth2ProviderConfigInput": {
                "clientId": "`your-client-id`",
                "clientSecret": "`your-client-secret`",
            }
        },
    }
```
