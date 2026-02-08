# Slack

Slack can be configured as an AgentCore Identity credential provider for outbound resource
access. This allows your agents to authenticate users through Slack's OAuth2 service
and obtain access tokens for Slack API resources.

## Outbound

**Step 1**

Use the following procedure to set up a Slack OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a Slack OAuth2 application

1. Create a Slack application, enter an app name, and choose the development
   workspace where the app will be built.
2. Choose the **OAuth & Permissions** section and set
   the following as the redirect URL for the application:
   - `https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback`

3. Copy the client ID and client secret that Slack issues for your
   application. You will need them for configuring the provider in
   AgentCore Identity.

For more details, refer to Slack's documentation [Sign in with
Slack](https://docs.slack.dev/authentication/sign-in-with-slack/ "https://docs.slack.dev/authentication/sign-in-with-slack/").

**Step 2**

To configure the outbound Slack resource provider, use the following:

```
{
        "name": "NAME",
        "credentialProviderVendor": "SlackOauth2",
        "oauth2ProviderConfigInput": {
            "slackOauth2ProviderConfig": {
                "clientId": "`your-client-id`",
                "clientSecret": "`your-client-secret`"
            }
        }
    }
```
