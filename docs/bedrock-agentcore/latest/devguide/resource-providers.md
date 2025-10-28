# Configure credential provider

Resource credential providers in AgentCore Identity act as intelligent intermediaries that
manage the complex relationships between agents, identity providers, and resource
servers. Each provider encapsulates the specific endpoint configuration required for a
particular service or identity system. The service provides built-in providers for
popular services including Google, GitHub, Slack, and Salesforce, with authorization
server endpoints and provider-specific parameters pre-configured to reduce development
effort. AgentCore Identity supports custom configurations through configurable OAuth2 credential
providers that can be tailored to work with any OAuth2-compatible resource server. For
information about OAuth2 credential provider limits, see [AgentCore Identity Service Quotas](bedrock-agentcore-limits.md#identity-service-limits "bedrock-agentcore-limits.md#identity-service-limits").

Resource credential providers integrate deeply with the token vault to provide
seamless credential lifecycle management. When an agent requests access to a resource,
the provider handles the authentication flow, stores the resulting credentials in the
token vault, and provides the agent with the necessary access tokens.

## Creating an OAuth 2.0 credential

provider

Provider configurations in AgentCore Identity define the basic parameters needed for
credential management with different resources and authentication systems. The
following example demonstrates how to use the AgentCore SDK to configure an OAuth
2.0 credential provider to use with GitHub.

```
from bedrock_agentcore.services.identity import IdentityClient
identity_client = IdentityClient("us-east-1")
github_provider = identity_client.create_oauth2_credential_provider({
        "name": "github-provider",
        "credentialProviderVendor": "GithubOauth2",
        "oauth2ProviderConfigInput": {
            "githubOauth2ProviderConfig": {
                "clientId": "your-github-client-id",
                "clientSecret": "your-github-client-secret"
            }
        }
    })
```

## Creating an API key credential provider

For services that use API keys for authentication rather than OAuth, AgentCore Identity
will securely store and retrieve keys for your agents. The example below illustrates
using the AgentCore SDK to store an API key. For information about API key
credential provider limits, see [AgentCore Identity Service Quotas](bedrock-agentcore-limits.md#identity-service-limits "bedrock-agentcore-limits.md#identity-service-limits").

```
from bedrock_agentcore.services.identity import IdentityClient
identity_client= IdentityClient("us-east-1")
apikey_provider= identity_client.create_api_key_credential_provider({
        "name": "`your-service-name`",
        "apiKey": "`your-api-key`"
    })
```
