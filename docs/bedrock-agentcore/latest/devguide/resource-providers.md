# Configure credential provider

Resource credential providers in AgentCore Identity act as intelligent intermediaries that manage the complex relationships between agents, identity providers, and resource servers. Each provider encapsulates the specific endpoint configuration required for a particular service or identity system. The service provides built-in providers for popular services including Google, GitHub, Slack, and Salesforce, with authorization server endpoints and provider-specific parameters pre-configured to reduce development effort. AgentCore Identity supports custom configurations through configurable OAuth2 credential providers that can be tailored to work with any OAuth2-compatible resource server. For information about OAuth2 credential provider limits, see [AgentCore Identity Service Quotas](bedrock-agentcore-limits.md#identity-service-limits "bedrock-agentcore-limits.md#identity-service-limits").

Resource credential providers integrate deeply with the token vault to provide seamless credential lifecycle management. When an agent requests access to a resource, the provider handles the authentication flow, stores the resulting credentials in the token vault, and provides the agent with the necessary access tokens.

## Creating an OAuth 2.0 credential provider

Provider configurations in AgentCore Identity define the basic parameters needed for credential management with different resources and authentication systems.

If you are using the AgentCore CLI, you can create an OAuth 2.0 credential provider with the `agentcore add credential` command:

```
agentcore add credential --type oauth \
  --name github-provider \
  --discovery-url https://your-idp/.well-known/openid-configuration \
  --client-id your-github-client-id \
  --client-secret your-github-client-secret \
  --scopes repo,user
```

The CLI stores the credential configuration in `agentcore/agentcore.json` and saves sensitive values (client ID and client secret) to `agentcore/.env.local`.

Alternatively, you can bring your own secret by providing a reference to a client secret already stored in AWS Secrets Manager:

```
aws bedrock-agentcore-control create-oauth2-credential-provider \
  --name "github-provider" \
  --credential-provider-vendor "GithubOauth2" \
  --oauth2-provider-config-input '{
    "githubOauth2ProviderConfig": {
      "clientId": "your-github-client-id",
      "clientSecretSource": "EXTERNAL",
      "clientSecretConfig": {
        "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret",
        "jsonKey": "clientSecret"
      }
    }
  }' \
  --region us-east-1
```

Alternatively, you can use the AgentCore SDK to configure an OAuth 2.0 credential provider programmatically. The following example configures a provider for GitHub.

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

To configure on-behalf-of (OBO) token exchange on an OAuth 2.0 credential provider, add an `onBehalfOfTokenExchangeConfig` to the provider configuration. For supported modes, parameters, and examples, see [On-behalf-of token exchange](on-behalf-of-token-exchange.md "on-behalf-of-token-exchange.md").

To authenticate to a downstream token endpoint using a signed JWT client assertion backed by an AWS KMS key instead of a client secret, configure `PRIVATE_KEY_JWT` as the client authentication method. For setup instructions, signing algorithm options, and KMS key requirements, see [Private Key JWT](private-key-jwt.md "private-key-jwt.md").

## Creating an API key credential provider

For services that use API keys for authentication rather than OAuth, AgentCore Identity will securely store and retrieve keys for your agents. For information about API key credential provider limits, see [AgentCore Identity Service Quotas](bedrock-agentcore-limits.md#identity-service-limits "bedrock-agentcore-limits.md#identity-service-limits").

If you are using the AgentCore CLI, you can store an API key with a single command:

```
agentcore add credential --name your-service-name --api-key your-api-key
```

Alternatively, you can bring your own secret by providing a reference to an API key already stored in AWS Secrets Manager:

```
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name "your-service-name" \
  --api-key-secret-source EXTERNAL \
  --api-key-secret-config secretId=arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret,jsonKey=api_key \
  --region us-east-1
```

Alternatively, you can use the AgentCore SDK to store an API key programmatically:

```
from bedrock_agentcore.services.identity import IdentityClient
identity_client= IdentityClient("us-east-1")
apikey_provider= identity_client.create_api_key_credential_provider({
        "name": "your-service-name",
        "apiKey": "your-api-key"
    })
```

## Creating a payment credential provider

For services that use payment-processor credentials such as Coinbase CDP or Stripe Privy, AgentCore Identity securely stores the associated API keys, app secrets, and wallet/authorization secrets in Secrets Manager and surfaces only their ARNs to your agents. For information about payment credential provider limits, see [AgentCore Identity Service Quotas](bedrock-agentcore-limits.md#identity-service-limits "bedrock-agentcore-limits.md#identity-service-limits").

Payment credential providers currently support two vendors: `CoinbaseCDP` and `StripePrivy`. Supply exactly one configuration block under `providerConfigurationInput` that matches the `credentialProviderVendor` you choose. Alternatively, you can bring your own secret by providing a reference to a secret already stored in AWS Secrets Manager.

###### Example

AWS CLI
The following example creates a payment credential provider for Coinbase CDP:

```
aws bedrock-agentcore-control create-payment-credential-provider \
  --name "coinbase-provider" \
  --credential-provider-vendor CoinbaseCDP \
  --provider-configuration-input '{
    "coinbaseCdpConfiguration": {
      "apiKeyId": "your-coinbase-api-key-id",
      "apiKeySecret": "your-coinbase-api-key-secret",
      "walletSecret": "your-coinbase-wallet-secret"
    }
  }' \
  --region us-east-1
```

The following example creates a Coinbase CDP payment credential provider with secrets stored in AWS Secrets Manager:

```
aws bedrock-agentcore-control create-payment-credential-provider \
  --name "coinbase-provider" \
  --credential-provider-vendor "CoinbaseCDP" \
  --provider-configuration-input '{
    "coinbaseCdpConfiguration": {
      "apiKeyId": "your-coinbase-api-key-id",
      "apiKeySecretSource": "EXTERNAL",
      "apiKeySecretConfig": {
        "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-api-secret",
        "jsonKey": "apiKeySecret"
      },
      "walletSecretSource": "EXTERNAL",
      "walletSecretConfig": {
        "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-wallet-secret",
        "jsonKey": "walletSecret"
      }
    }
  }' \
  --region us-east-1
```

The following example creates a payment credential provider for Stripe Privy:

```
aws bedrock-agentcore-control create-payment-credential-provider \
  --name "stripe-privy-provider" \
  --credential-provider-vendor StripePrivy \
  --provider-configuration-input '{
    "stripePrivyConfiguration": {
      "appId": "your-stripe-privy-app-id",
      "appSecret": "your-stripe-privy-app-secret",
      "authorizationPrivateKey": "your-stripe-privy-authorization-private-key",
      "authorizationId": "your-stripe-privy-authorization-id"
    }
  }' \
  --region us-east-1
```

The following example creates a Stripe Privy payment credential provider with secrets stored in AWS Secrets Manager:

```
aws bedrock-agentcore-control create-payment-credential-provider \
  --name "stripe-privy-provider" \
  --credential-provider-vendor "StripePrivy" \
  --provider-configuration-input '{
    "stripePrivyConfiguration": {
      "appId": "your-stripe-privy-app-id",
      "appSecretSource": "EXTERNAL",
      "appSecretConfig": {
        "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-app-secret",
        "jsonKey": "appSecret"
      },
      "authorizationPrivateKeySource": "EXTERNAL",
      "authorizationPrivateKeyConfig": {
        "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-auth-key-secret",
        "jsonKey": "authorizationPrivateKey"
      },
      "authorizationId": "your-stripe-privy-authorization-id"
    }
  }' \
  --region us-east-1
```

AWS SDK
The following example configures a provider for Coinbase CDP:

```
import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-east-1")

coinbase_provider = client.create_payment_credential_provider(
    name="coinbase-provider",
    credentialProviderVendor="CoinbaseCDP",
    providerConfigurationInput={
        "coinbaseCdpConfiguration": {
            "apiKeyId": "your-coinbase-api-key-id",
            "apiKeySecret": "your-coinbase-api-key-secret",
            "walletSecret": "your-coinbase-wallet-secret"
        }
    }
)
```

The following example configures a Coinbase CDP provider with secrets stored in AWS Secrets Manager:

```
import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-east-1")

coinbase_provider = client.create_payment_credential_provider(
    name="coinbase-provider",
    credentialProviderVendor="CoinbaseCDP",
    providerConfigurationInput={
        "coinbaseCdpConfiguration": {
            "apiKeyId": "your-coinbase-api-key-id",
            "apiKeySecretSource": "EXTERNAL",
            "apiKeySecretConfig": {
                "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-api-secret",
                "jsonKey": "apiKeySecret"
            },
            "walletSecretSource": "EXTERNAL",
            "walletSecretConfig": {
                "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-wallet-secret",
                "jsonKey": "walletSecret"
            }
        }
    }
)
```

The following example configures a provider for Stripe Privy:

```
import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-east-1")

stripe_privy_provider = client.create_payment_credential_provider(
    name="stripe-privy-provider",
    credentialProviderVendor="StripePrivy",
    providerConfigurationInput={
        "stripePrivyConfiguration": {
            "appId": "your-stripe-privy-app-id",
            "appSecret": "your-stripe-privy-app-secret",
            "authorizationPrivateKey": "your-stripe-privy-authorization-private-key",
            "authorizationId": "your-stripe-privy-authorization-id"
        }
    }
)
```

The following example configures a Stripe Privy provider with secrets stored in AWS Secrets Manager:

```
import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-east-1")

stripe_privy_provider = client.create_payment_credential_provider(
    name="stripe-privy-provider",
    credentialProviderVendor="StripePrivy",
    providerConfigurationInput={
        "stripePrivyConfiguration": {
            "appId": "your-stripe-privy-app-id",
            "appSecretSource": "EXTERNAL",
            "appSecretConfig": {
                "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-app-secret",
                "jsonKey": "appSecret"
            },
            "authorizationPrivateKeySource": "EXTERNAL",
            "authorizationPrivateKeyConfig": {
                "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-auth-key-secret",
                "jsonKey": "authorizationPrivateKey"
            },
            "authorizationId": "your-stripe-privy-authorization-id"
        }
    }
)
```

AgentCore SDK
The following example configures a provider for Coinbase CDP:

```
from bedrock_agentcore.services.identity import IdentityClient

identity_client = IdentityClient("us-east-1")

coinbase_provider = identity_client.create_payment_credential_provider(
    name="coinbase-provider",
    credential_provider_vendor="CoinbaseCDP",
    provider_configuration_input={
        "coinbaseCdpConfiguration": {
            "apiKeyId": "your-coinbase-api-key-id",
            "apiKeySecret": "your-coinbase-api-key-secret",
            "walletSecret": "your-coinbase-wallet-secret"
        }
    }
)
```

The following example configures a Coinbase CDP provider with secrets stored in AWS Secrets Manager:

```
from bedrock_agentcore.services.identity import IdentityClient

identity_client = IdentityClient("us-east-1")

coinbase_provider = identity_client.create_payment_credential_provider(
    name="coinbase-provider",
    credential_provider_vendor="CoinbaseCDP",
    provider_configuration_input={
        "coinbaseCdpConfiguration": {
            "apiKeyId": "your-coinbase-api-key-id",
            "apiKeySecretSource": "EXTERNAL",
            "apiKeySecretConfig": {
                "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-api-secret",
                "jsonKey": "apiKeySecret"
            },
            "walletSecretSource": "EXTERNAL",
            "walletSecretConfig": {
                "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-wallet-secret",
                "jsonKey": "walletSecret"
            }
        }
    }
)
```

The following example configures a provider for Stripe Privy:

```
from bedrock_agentcore.services.identity import IdentityClient

identity_client = IdentityClient("us-east-1")

stripe_privy_provider = identity_client.create_payment_credential_provider(
    name="stripe-privy-provider",
    credential_provider_vendor="StripePrivy",
    provider_configuration_input={
        "stripePrivyConfiguration": {
            "appId": "your-stripe-privy-app-id",
            "appSecret": "your-stripe-privy-app-secret",
            "authorizationPrivateKey": "your-stripe-privy-authorization-private-key",
            "authorizationId": "your-stripe-privy-authorization-id"
        }
    }
)
```

The following example configures a Stripe Privy provider with secrets stored in AWS Secrets Manager:

```
from bedrock_agentcore.services.identity import IdentityClient

identity_client = IdentityClient("us-east-1")

stripe_privy_provider = identity_client.create_payment_credential_provider(
    name="stripe-privy-provider",
    credential_provider_vendor="StripePrivy",
    provider_configuration_input={
        "stripePrivyConfiguration": {
            "appId": "your-stripe-privy-app-id",
            "appSecretSource": "EXTERNAL",
            "appSecretConfig": {
                "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-app-secret",
                "jsonKey": "appSecret"
            },
            "authorizationPrivateKeySource": "EXTERNAL",
            "authorizationPrivateKeyConfig": {
                "secretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-auth-key-secret",
                "jsonKey": "authorizationPrivateKey"
            },
            "authorizationId": "your-stripe-privy-authorization-id"
        }
    }
)
```
