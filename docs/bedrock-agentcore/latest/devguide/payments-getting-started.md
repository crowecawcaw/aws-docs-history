# Get started with AgentCore payments

This guide walks you through setting up AgentCore payments and processing your first microtransaction. By the end, your agent will be able to access paid x402 endpoints autonomously.

## Prerequisites

Before you start, ensure you have:

- An AWS account with credentials configured. See [Getting started with the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- Python 3.10+ installed.
- Boto3 installed: `pip install boto3`
- The AgentCore SDK installed: `pip install bedrock-agentcore[strands-agents]`
- Credentials from at least one payment provider (Coinbase CDP or Stripe Privy). See [Prerequisites](payments-prerequisites.md "payments-prerequisites.md") for details.
- An AWS Region where AgentCore payments is available (us-east-1, us-west-2, eu-central-1, or ap-southeast-2). See [Supported AWS Regions](agentcore-regions.md "agentcore-regions.md").

## Steps

Follow these steps to set up payments and process your first transaction:

1. **Create a payment credential provider** — Store your Coinbase CDP or Stripe Privy credentials securely in AgentCore Identity. See [Creating a payment credential provider](resource-providers.md#payment-credential-provider "resource-providers.md#payment-credential-provider").
2. **Set up IAM roles** — Configure the required roles for administration, management, execution, and service operations. See [IAM roles for AgentCore payments](payments-iam-roles.md "payments-iam-roles.md").
3. **Create a Payment Manager and Connector** — Set up the top-level resource that coordinates payment operations and connect it to your payment provider. See [Create a Payment Manager and Connector](payments-create-manager.md "payments-create-manager.md").
4. **Create a payment instrument** — Provision an embedded crypto wallet for your agent. See [Create a payment instrument](payments-create-instrument.md "payments-create-instrument.md").
5. **Fund the wallet** — Redirect the end user to the wallet hub to top up and grant agent permissions. See [Funding the wallet](payments-how-it-works.md#payments-how-it-works-funding-wallet "payments-how-it-works.md#payments-how-it-works-funding-wallet").
6. **Create a payment session** — Establish a time-bounded session with optional spending limits. See [Create a payment session](payments-create-session.md "payments-create-session.md").
7. **Process a payment** — Call a paid endpoint and let AgentCore payments handle the x402 flow. See [Process a payment](payments-process-payment.md "payments-process-payment.md").

## Quick example with Strands SDK

The following example shows the minimal code to enable automatic payments in a Strands agent:

```
from strands import Agent
from strands_tools import http_request
from bedrock_agentcore.payments.integrations.config import AgentCorePaymentsPluginConfig
from bedrock_agentcore.payments.integrations.strands.plugin import AgentCorePaymentsPlugin

# Configure the payments plugin
config = AgentCorePaymentsPluginConfig(
    payment_manager_arn="arn:aws:bedrock-agentcore:us-west-2:123456789012:payment-manager/pm-abc123",
    user_id="test-user-123",
    payment_instrument_id="payment-instrument-xyz789",
    payment_session_id="payment-session-def456",
    region="us-west-2",
)

# Create agent with automatic payment handling
plugin = AgentCorePaymentsPlugin(config=config)
agent = Agent(
    system_prompt="You are a helpful assistant that can access paid APIs.",
    tools=[http_request],
    plugins=[plugin],
)

# The agent automatically handles 402 responses
agent("Access the premium endpoint at https://example.com/paid-api")
```

## Next steps

- [Connect to Coinbase x402 Bazaar](payments-connect-bazaar.md "payments-connect-bazaar.md") to discover 10,000+ paid MCP tools.
- [Integrate with Browser Tool](payments-browser.md "payments-browser.md") to access paywalled websites.
- [Enable observability](payments-observability.md "payments-observability.md") to monitor payment operations in CloudWatch.
