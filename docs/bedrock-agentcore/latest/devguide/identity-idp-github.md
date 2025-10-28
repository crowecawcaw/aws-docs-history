# GitHub

GitHub can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through GitHub's OAuth2
service and obtain access tokens for GitHub API resources.

## Outbound

**Step 1**

Use the following procedure to set up a GitHub OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a GitHub OAuth2 application

1. Choose the profile picture of your github account and choose
   **Settings**.
2. Choose **Developer settings**.
3. Choose **OAuth Apps**.
4. On the OAuth2 apps page choose **New OAuth App**.
5. Enter the necessary details specific to your application. For
   authorization callback URL enter the following:
   - `https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback`

6. Choose **Register application** to create your Github
   OAuth app.
7. On Github's OAuth Apps page, go to your newly created provider.
8. Under the client secrets section, choose **Generate a new client
   secret**.
9. Make a note of the newly created client secret. You'll need this to
   configure your Github application with AgentCore Identity.

###### Note

Github only returns the full secret when it is created. If you lose
track of it you'll need to recreate the client secret to configure the
provider in AgentCore Identity.

For more details, refer to Github's documentation [Creating an OAuth app](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app "https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app").

**Step 2**

To configure the outbound GitHub resource provider, use the following:

```
{
        "name": "NAME",
        "credentialProviderVendor": "GithubOauth2",
        "oauth2ProviderConfigInput": {
            "GithubOauth2ProviderConfigInput": {
                "clientId": "`your-client-id`",
                "clientSecret": "`your-client-secret`",
            }
        },
    }
```
