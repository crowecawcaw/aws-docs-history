# AgentCore payments quick start

This tutorial walks you through setting up AgentCore payments and processing your first microtransaction. By the end, your agent will pay for a resource using the x402 protocol on a test network.

You can set up payments in two ways:

- [Using the AgentCore Payments skill](#payments-getting-started-skill "#payments-getting-started-skill") — An automated setup experience that provisions all resources through a guided conversation with AI coding agents like Kiro, Claude Code, or Codex. The skill handles CLI commands, SDK scripts, and framework wiring for you.
- [Using CLI, SDK, or Boto3](#payments-getting-started-manual "#payments-getting-started-manual") — A step-by-step manual setup using the AgentCore CLI, AWS SDK, or AWS CLI directly.

## Using the AgentCore Payments skill

The AgentCore Payments skill automates the entire setup process through an interactive, guided experience. It provisions the following resources:

- **PaymentCredentialProvider** — Stores payment provider credentials in AgentCore Identity.
- **Payment Manager** — The top-level resource that coordinates payment operations.
- **Payment Connector** — Links the manager to your credentials via the AgentCore CLI.
- **Payment Instrument** — A crypto wallet that your agent uses to pay merchants on behalf of a user.
- **Payment Session** — A time-bounded context with spending limits.

The skill also wires payments into your agent with a framework-agnostic tool, so it works with Strands, LangGraph, OpenAI Agents SDK, or any Python framework.

### Prerequisites

Before starting, make sure you have:

- **AWS Account** with credentials configured (`aws configure`)
- **An AWS Region where AgentCore payments is available** — us-east-1, us-west-2, eu-central-1, or ap-southeast-2. See [Supported AWS Regions](agentcore-regions.md "agentcore-regions.md").
- **Node.js 20+** installed (the skill installs the AgentCore CLI automatically)
- **An agent that accesses a paid endpoint** — The skill enables your agent to pay for x402-protected APIs. For testing, you can use the sandbox endpoint `https://sandbox.node4all.com/v1/x402-test`.
- **The [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws "https://github.com/aws/agent-toolkit-for-aws")
  `aws-agents` plugin** installed in your AI coding agent:

###### Example

Claude Code

```
/plugin marketplace add aws/agent-toolkit-for-aws
/plugin install aws-agents@agent-toolkit-for-aws
```

Codex
The plugin is discovered automatically from the marketplace manifest. To add the marketplace, run the following command:

```
codex plugin marketplace add aws/agent-toolkit-for-aws
```

### Invoke the skill

The payments skill is part of the `agents-build` skill in the [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws "https://github.com/aws/agent-toolkit-for-aws"). To trigger it, describe your intent in your AI coding agent. For example:

- "Add payments to my agent using `agents-build` skill in `aws-agents` plugin"
- "Set up microtransactions for my agent using `agents-build` skill in `aws-agents` plugin"
- "I need to handle 402 Payment Required responses using `agents-build` skill in `aws-agents` plugin"
- "Wire my agent to pay for x402-protected APIs using `agents-build` skill in `aws-agents` plugin"

The skill detects payment-related intent and loads the payments workflow automatically.

### What the skill does

The skill runs an automated process that provisions your payment infrastructure end-to-end. The skill runs most steps automatically and pauses twice for your input:

1. Verifies or installs the AgentCore CLI and sets up the project
2. Creates the payment manager
3. **Pauses** — You run `agentcore add payment-connector` to enter your provider secrets (Coinbase CDP or Stripe Privy credentials)
4. Deploys resources to your AWS account (`agentcore deploy -y`)
5. Wires a framework-agnostic payment tool (`x402_payment_tool.py`) into your agent
6. Creates a per-user wallet (instrument) and budget-bounded session via the SDK
7. **Pauses** — You authorize the wallet (delegation) and fund it with testnet USDC from the [Circle faucet](https://faucet.circle.com/ "https://faucet.circle.com/") website
8. Sets environment variables and runs a test payment against a paid endpoint

Before running the connector command, obtain credentials from your provider:

- **Coinbase CDP** — API Key ID, API Key Secret, and Wallet Secret from the [Coinbase Developer Platform](https://portal.cdp.coinbase.com/ "https://portal.cdp.coinbase.com/") website (with Delegated signing enabled).
- **Stripe Privy** — App ID, App Secret, Authorization ID, and Authorization Private Key from the [Privy dashboard](https://dashboard.privy.io/ "https://dashboard.privy.io/") website.

A successful run shows the agent calling `x402_fetch`, detecting a `402`, settling payment via the AgentCore SDK, and the retry returning `200` with paid content.

## Using CLI, SDK, or Boto3

This section walks you through each step manually using the AgentCore CLI, AWS CLI, or AWS SDK (Boto3).

### Prerequisites

Before starting, make sure you have:

- **AWS Account** with credentials configured (`aws configure`)
- **Python 3.10+** installed
- **An AWS Region where AgentCore payments is available** — us-east-1, us-west-2, eu-central-1, or ap-southeast-2. See [Supported AWS Regions](agentcore-regions.md "agentcore-regions.md").

Install the required packages:

```
pip install boto3 bedrock-agentcore[strands-agents] strands-agents strands-agents-tools
```

Verify your credentials are configured:

```
aws sts get-caller-identity
```

###### Tip

If you have the AgentCore CLI v0.19.0 or later installed, you can use CLI commands as an alternative to the SDK in Steps 2, 3, 5, and 6. Each step below shows both options.

### Step 1: Obtain payment provider credentials

AgentCore payments connects to an external payment provider for wallet operations. You need credentials from one of the supported providers before proceeding.

###### Example

Coinbase CDP

1. Log in to the [Coinbase Developer Platform](https://docs.cdp.coinbase.com/api-reference/v2/authentication "https://docs.cdp.coinbase.com/api-reference/v2/authentication") and create or select a project.
2. Generate an API key and note the **API Key ID**, **API Key Secret**, and **Wallet Secret**.
3. Under **Project** > **Wallets** > **Non-custodial Wallet** > **Security**, enable **Delegated signing**.

You will use these three values in the next step:

| Credential       | Description                                                                           |
| ---------------- | ------------------------------------------------------------------------------------- |
| `API Key ID`     | Public identifier for your CDP project                                                |
| `API Key Secret` | Private secret for signing API requests                                               |
| `Wallet Secret`  | Secret for cryptographic wallet operations (deriving addresses, signing transactions) |

Privy

1. Create a **dedicated** Privy app at [dashboard.privy.io](https://dashboard.privy.io/ "https://dashboard.privy.io/"). Do not reuse apps that serve other purposes.
2. Copy the **App ID** and **App Secret** from your app settings.
3. Navigate to **Wallet Infrastructure** > **Authorization** and choose **New Key** to generate a P-256 key pair.
4. Strip the `wallet-auth:` prefix from the generated private key. Use only the raw base64 content.

You will use these four values in the next step:

| Credential                  | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| `App ID`                    | Your Privy application identifier                            |
| `App Secret`                | Secret for server-to-server Basic Auth                       |
| `Authorization ID`          | Public key identifier from the P-256 key pair                |
| `Authorization Private Key` | Private key (base64 only, without the `wallet-auth:` prefix) |

For full details including security best practices and credential rotation, see [Prerequisites](payments-prerequisites.md "payments-prerequisites.md").

### Step 2: Store credentials in AgentCore Identity

Store your payment provider credentials as a PaymentCredentialProvider. This keeps secrets in AWS Secrets Manager rather than in your application code.

###### Example

Coinbase CDP

```
import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

credential_provider = client.create_payment_credential_provider(
    name="my-coinbase-credentials",
    credentialProviderVendor="CoinbaseCDP",
    coinbaseCdpConfig={
        "apiKeyId": "<YOUR_CDP_API_KEY_ID>",
        "apiKeySecret": "<YOUR_CDP_API_KEY_SECRET>",
        "walletSecret": "<YOUR_CDP_WALLET_SECRET>"
    }
)
CREDENTIAL_PROVIDER_ARN = credential_provider["credentialProviderArn"]
print(f"Credential provider created: {CREDENTIAL_PROVIDER_ARN}")
```

Privy

```
import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

credential_provider = client.create_payment_credential_provider(
    name="my-privy-credentials",
    credentialProviderVendor="StripePrivy",
    stripePrivyConfig={
        "appId": "<YOUR_PRIVY_APP_ID>",
        "appSecret": "<YOUR_PRIVY_APP_SECRET>",
        "authorizationId": "<YOUR_PRIVY_AUTHORIZATION_ID>",
        "authorizationPrivateKey": "<YOUR_PRIVY_PRIVATE_KEY_BASE64>"
    }
)
CREDENTIAL_PROVIDER_ARN = credential_provider["credentialProviderArn"]
print(f"Credential provider created: {CREDENTIAL_PROVIDER_ARN}")
```

For the complete request and response schema, see [CreatePaymentCredentialProvider](../../../bedrock-agentcore-control/latest/APIReference/API_CreatePaymentCredentialProvider.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreatePaymentCredentialProvider.md") in the API Reference.

#### CLI alternative: Store credentials

With the AgentCore CLI, credential storage happens automatically when you add a payment connector (Step 3). Skip this step if you plan to use the CLI path.

### Step 3: Create a Payment Manager and Connector

A Payment Manager is the top-level resource that coordinates payment operations. A Payment Connector links the manager to your payment provider credentials. Before creating these resources, set up the required IAM roles as described in [IAM roles for AgentCore payments](payments-iam-roles.md "payments-iam-roles.md").

###### Example

AgentCore CLI
The CLI creates the credential provider, Payment Manager, and Payment Connector in one flow. From your AgentCore project directory, add a payment manager and connector together.

**Interactive wizard:**

```
agentcore add payment-manager
```

The wizard prompts for the manager name, pattern (interceptor), auto-payment toggle, and default spend limit. It then asks whether to add a connector and walks through provider selection and credential input.

**Non-interactive (Coinbase CDP):**

```
agentcore add payment-manager \
  --name my-payment-manager \
  --auto-payment \
  --default-spend-limit 5.00

agentcore add payment-connector \
  --manager my-payment-manager \
  --name my-coinbase-connector \
  --provider CoinbaseCDP \
  --api-key-id <YOUR_CDP_API_KEY_ID> \
  --api-key-secret <YOUR_CDP_API_KEY_SECRET> \
  --wallet-secret <YOUR_CDP_WALLET_SECRET>
```

**Non-interactive (Privy):**

```
agentcore add payment-manager \
  --name my-payment-manager \
  --auto-payment \
  --default-spend-limit 5.00

agentcore add payment-connector \
  --manager my-payment-manager \
  --name my-privy-connector \
  --provider StripePrivy \
  --app-id <YOUR_PRIVY_APP_ID> \
  --app-secret <YOUR_PRIVY_APP_SECRET> \
  --authorization-id <YOUR_PRIVY_AUTHORIZATION_ID> \
  --authorization-private-key <YOUR_PRIVY_PRIVATE_KEY_BASE64>
```

After adding, deploy to provision the payment infrastructure:

```
agentcore deploy
```

The deploy step creates IAM roles, stores credentials in AgentCore Identity, and provisions the Payment Manager and Connector. You will see "Creating payment infrastructure…​" in the output.

AWS CLI
Create the Payment Manager:

```
aws bedrock-agentcore-control create-payment-manager \
  --name "my-first-payment-manager" \
  --authorizer-type AWS_IAM \
  --role-arn "<YOUR_SERVICE_ROLE_ARN>" \
  --region us-west-2
```

After the manager reaches `READY` status, create a credential provider and connector. See [Create a Payment Manager and Connector](payments-create-manager.md "payments-create-manager.md") for the full AWS CLI workflow.

AWS SDK
First, create the Payment Manager (the same for both providers):

```
import time

manager = client.create_payment_manager(
    name="my-first-payment-manager",
    authorizerType="AWS_IAM",
    roleArn="<YOUR_SERVICE_ROLE_ARN>"
)
PAYMENT_MANAGER_ARN = manager["paymentManagerArn"]
print(f"Payment Manager created: {PAYMENT_MANAGER_ARN}")

# Wait for the manager to reach READY state
while True:
    status = client.get_payment_manager(paymentManagerArn=PAYMENT_MANAGER_ARN)
    if status["status"] == "READY":
        break
    print(f"Status: {status['status']}... waiting")
    time.sleep(5)
```

Then create the Payment Connector for your provider:

**Coinbase CDP:**

```
connector = client.create_payment_connector(
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    name="my-coinbase-connector",
    paymentConnectorType="CoinbaseCDP",
    credentialProviderArn=CREDENTIAL_PROVIDER_ARN
)
PAYMENT_CONNECTOR_ID = connector["paymentConnectorId"]
print(f"Connector created: {PAYMENT_CONNECTOR_ID}")
```

**Privy:**

```
connector = client.create_payment_connector(
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    name="my-privy-connector",
    paymentConnectorType="StripePrivy",
    credentialProviderArn=CREDENTIAL_PROVIDER_ARN
)
PAYMENT_CONNECTOR_ID = connector["paymentConnectorId"]
print(f"Connector created: {PAYMENT_CONNECTOR_ID}")
```

If you do not have a service role, see [IAM roles for AgentCore payments](payments-iam-roles.md "payments-iam-roles.md") for instructions on creating one. The console can also create a role on your behalf. For the complete request and response schemas, see [CreatePaymentManager](../../../bedrock-agentcore-control/latest/APIReference/API_CreatePaymentManager.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreatePaymentManager.md") and [CreatePaymentConnector](../../../bedrock-agentcore-control/latest/APIReference/API_CreatePaymentConnector.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreatePaymentConnector.md") in the API Reference.

### Step 4: Create a payment instrument

A payment instrument is an embedded crypto wallet that your agent uses to pay merchants on behalf of a user. Each instrument is associated with a specific blockchain network.

###### Example

AWS CLI

```
aws bedrock-agentcore create-payment-instrument \
    --payment-manager-arn "$PAYMENT_MANAGER_ARN" \
    --payment-connector-id "$PAYMENT_CONNECTOR_ID" \
    --user-id "test-user-123" \
    --payment-instrument-type "EMBEDDED_CRYPTO_WALLET" \
    --payment-instrument-details '{
        "embeddedCryptoWallet": {
            "network": "ETHEREUM",
            "linkedAccounts": [{"email": {"emailAddress": "your-email@example.com"}}]
        }
    }' \
    --client-token "$(uuidgen)" \
    --region us-west-2
```

Save the `paymentInstrumentId` and `redirectUrl` from the response.

AWS SDK

```
import uuid

dp_client = boto3.client("bedrock-agentcore", region_name="us-west-2",
    endpoint_url="https://bedrock-agentcore.us-west-2.amazonaws.com")

instrument = dp_client.create_payment_instrument(
    userId="test-user-123",
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    paymentConnectorId=PAYMENT_CONNECTOR_ID,
    paymentInstrumentType="EMBEDDED_CRYPTO_WALLET",
    paymentInstrumentDetails={
        "embeddedCryptoWallet": {
            "network": "ETHEREUM",
            "linkedAccounts": [{"email": {"emailAddress": "your-email@example.com"}}]
        }
    },
    clientToken=str(uuid.uuid4()),
)
INSTRUMENT_ID = instrument["paymentInstrumentId"]
REDIRECT_URL = instrument["paymentInstrumentDetails"]["redirectUrl"]
print(f"Instrument created: {INSTRUMENT_ID}")
print(f"Fund the wallet at: {REDIRECT_URL}")
```

For the complete request and response schema, see [CreatePaymentInstrument](../APIReference/API_CreatePaymentInstrument.md "../APIReference/API_CreatePaymentInstrument.md") in the API Reference.

#### Fund the wallet and grant permissions

Before the agent can transact, the end user must fund the wallet and grant signing permissions. Open the `redirectUrl` from the response above in a browser. From the wallet hub, the user can:

- Top up the wallet using crypto transfer, credit/debit card, Apple Pay, Google Pay, or ACH
- Grant the agent permission to sign transactions on their behalf

For a test environment, fund the wallet with testnet USDC.

After funding, poll the instrument status until it becomes `ACTIVE`:

###### Example

AWS CLI

```
aws bedrock-agentcore get-payment-instrument \
    --payment-manager-arn "$PAYMENT_MANAGER_ARN" \
    --payment-instrument-id "$INSTRUMENT_ID" \
    --region us-west-2
```

AWS SDK

```
while True:
    inst_status = dp_client.get_payment_instrument(
        paymentManagerArn=PAYMENT_MANAGER_ARN,
        paymentInstrumentId=INSTRUMENT_ID
    )
    if inst_status["status"] == "ACTIVE":
        print("Instrument is active and funded.")
        break
    print(f"Instrument status: {inst_status['status']}... waiting for funding")
    time.sleep(10)
```

For more details on funding flows by provider, see [Funding the wallet](payments-how-it-works.md#payments-how-it-works-funding-wallet "payments-how-it-works.md#payments-how-it-works-funding-wallet").

### Step 5: Create a payment session

A payment session is a time-bounded context with optional spending limits. When the session expires or the budget is exhausted, the agent cannot make further payments within that session.

###### Example

AgentCore CLI
When using the CLI, you do not need to create a session manually. Pass `--auto-session` to `agentcore invoke` and the CLI creates or reuses a session with the default spend limit you configured on the payment manager.

```
agentcore invoke \
  --prompt "your prompt here" \
  --payment-instrument-id <INSTRUMENT_ID> \
  --auto-session \
  --payment-user-id test-user-123
```

To use a specific session you created through the SDK, pass `--payment-session-id` instead of `--auto-session`.

AWS CLI

```
aws bedrock-agentcore create-payment-session \
    --payment-manager-arn "$PAYMENT_MANAGER_ARN" \
    --user-id "test-user-123" \
    --expiry-time-in-minutes 60 \
    --limits '{"maxSpendAmount": {"value": "5.00", "currency": "USD"}}' \
    --client-token "$(uuidgen)" \
    --region us-west-2
```

AWS SDK

```
session = dp_client.create_payment_session(
    userId="test-user-123",
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    expiryTimeInMinutes=60,
    limits={"maxSpendAmount": {"value": "5.00", "currency": "USD"}},
    clientToken=str(uuid.uuid4()),
)
SESSION_ID = session["paymentSessionId"]
print(f"Session created: {SESSION_ID} (expires in 60 minutes, $5.00 limit)")
```

For the complete request and response schema, see [CreatePaymentSession](../APIReference/API_CreatePaymentSession.md "../APIReference/API_CreatePaymentSession.md") in the API Reference.

### Step 6: Process a payment with a Strands agent

With all resources in place, create a Strands agent that handles x402 payments automatically. When the agent calls a paid endpoint and receives an HTTP 402 response, the payments plugin signs the transaction and retries the request.

###### Example

AgentCore CLI
Invoke your deployed agent with payment context. The CLI passes the payment instrument and session to the agent at runtime, and the agent’s x402 interceptor handles payment automatically.

```
agentcore invoke \
  --prompt "Access the premium endpoint at https://example-x402-merchant.com/paid-api" \
  --payment-instrument-id <INSTRUMENT_ID> \
  --auto-session \
  --payment-user-id test-user-123
```

To pass an explicit session instead of auto-creating one:

```
agentcore invoke \
  --prompt "Access the premium endpoint at https://example-x402-merchant.com/paid-api" \
  --payment-instrument-id <INSTRUMENT_ID> \
  --payment-session-id <SESSION_ID> \
  --payment-user-id test-user-123
```

AWS CLI
Call `process-payment` directly with an x402 payload (used when you handle payment orchestration yourself):

```
aws bedrock-agentcore process-payment \
    --payment-manager-arn "$PAYMENT_MANAGER_ARN" \
    --payment-session-id "$SESSION_ID" \
    --payment-instrument-id "$INSTRUMENT_ID" \
    --payment-type "CRYPTO_X402" \
    --payment-input '{
        "cryptoX402": {
            "version": "2",
            "payload": {
                "scheme": "exact",
                "network": "eip155:84532",
                "amount": "100000",
                "asset": "0x036CbD53842c5426634e7929541eC2318f3dCF7e",
                "payTo": "0xMERCHANT_ADDRESS",
                "maxTimeoutSeconds": 300,
                "extra": {"name": "USDC", "version": "2"}
            }
        }
    }' \
    --client-token "$(uuidgen)" \
    --region us-west-2
```

For the complete request and response schema, see [ProcessPayment](../APIReference/API_ProcessPayment.md "../APIReference/API_ProcessPayment.md") in the API Reference.

AWS SDK

```
from strands import Agent
from strands_tools import http_request
from bedrock_agentcore.payments.integrations.config import AgentCorePaymentsPluginConfig
from bedrock_agentcore.payments.integrations.strands.plugin import AgentCorePaymentsPlugin

config = AgentCorePaymentsPluginConfig(
    payment_manager_arn=PAYMENT_MANAGER_ARN,
    user_id="test-user-123",
    payment_instrument_id=INSTRUMENT_ID,
    payment_session_id=SESSION_ID,
    region="us-west-2",
)

plugin = AgentCorePaymentsPlugin(config=config)
agent = Agent(
    system_prompt="You are a helpful assistant that can access paid APIs.",
    tools=[http_request],
    plugins=[plugin],
)

# The agent handles 402 responses automatically
response = agent("Access the premium endpoint at https://example-x402-merchant.com/paid-api")
print(response)
```

For the complete request and response schema of the underlying API call, see [ProcessPayment](../APIReference/API_ProcessPayment.md "../APIReference/API_ProcessPayment.md") in the API Reference.

### Verify the payment

After the agent processes a payment, check the session to confirm the transaction was recorded:

###### Example

AWS CLI

```
aws bedrock-agentcore get-payment-session \
    --payment-manager-arn "$PAYMENT_MANAGER_ARN" \
    --payment-session-id "$SESSION_ID" \
    --region us-west-2

aws bedrock-agentcore get-payment-instrument-balance \
    --payment-manager-arn "$PAYMENT_MANAGER_ARN" \
    --payment-instrument-id "$INSTRUMENT_ID" \
    --region us-west-2
```

AWS SDK

```
session_status = dp_client.get_payment_session(
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    paymentSessionId=SESSION_ID
)
print(f"Session status: {session_status['status']}")
print(f"Amount spent: {session_status.get('spentAmount', '0.00')} USD")
```

You can also check the instrument balance:

```
balance = dp_client.get_payment_instrument_balance(
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    paymentInstrumentId=INSTRUMENT_ID
)
print(f"Remaining balance: {balance['amount']} {balance['currency']}")
```

## Troubleshooting

The following issues apply to both the skill-based and manual setup paths.

| Issue                                | Solution                                                                                                                 |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Payment Manager stuck in CREATING    | Wait up to 2 minutes. If it moves to CREATE\_FAILED, check that your service role ARN and permissions are correct.       |
| "PaymentInstrument not active"       | The end user must fund the wallet and grant signing permissions through the redirect URL before the agent can transact.  |
| "Session expired or budget exceeded" | Create a new payment session with a longer expiry or higher spending limit.                                              |
| "CredentialProvider not found"       | Verify the credential provider ARN matches what you created in Step 2. Ensure the region is consistent across all calls. |
| ProcessPayment returns FAILED        | Check that the wallet has sufficient USDC balance for the transaction amount plus gas fees.                              |

## Cleanup

Delete the resources you created during this tutorial:

###### Example

AgentCore CLI

```
agentcore remove payment-connector --manager my-payment-manager --name my-coinbase-connector --yes
agentcore remove payment-manager --name my-payment-manager --yes
agentcore deploy
```

The `remove` commands update the local configuration. The follow-up `deploy` tears down the payment infrastructure in your account.

AWS CLI

```
aws bedrock-agentcore delete-payment-instrument \
    --payment-manager-arn "$PAYMENT_MANAGER_ARN" \
    --payment-instrument-id "$INSTRUMENT_ID" \
    --region us-west-2

aws bedrock-agentcore-control delete-payment-connector \
    --payment-manager-id "$PAYMENT_MANAGER_ID" \
    --payment-connector-id "$PAYMENT_CONNECTOR_ID" \
    --region us-west-2

aws bedrock-agentcore-control delete-payment-manager \
    --payment-manager-id "$PAYMENT_MANAGER_ID" \
    --region us-west-2
```

AWS SDK

```
# Delete payment instrument
dp_client.delete_payment_instrument(
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    paymentInstrumentId=INSTRUMENT_ID
)

# Delete payment connector
client.delete_payment_connector(
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    paymentConnectorId=PAYMENT_CONNECTOR_ID
)

# Delete payment manager
client.delete_payment_manager(
    paymentManagerArn=PAYMENT_MANAGER_ARN
)

print("All payment resources deleted.")
```

## What you’ve built

Through this tutorial, you created:

- **PaymentCredentialProvider** — Payment provider credentials stored in AgentCore Identity
- **PaymentManager** — Top-level resource coordinating payment operations
- **PaymentConnector** — Integration between your manager and the external payment provider
- **PaymentInstrument** — An embedded crypto wallet, funded and authorized by the end user
- **PaymentSession** — A time-bounded, budget-limited payment context
- **Strands Agent** — An AI agent that handles x402 payments automatically

## Next steps

- [Connect to Coinbase x402 Bazaar](payments-connect-bazaar.md "payments-connect-bazaar.md") to discover 10,000+ paid MCP tools.
- [Integrate with Browser Tool](payments-browser.md "payments-browser.md") to access paywalled websites.
- [Enable observability](payments-observability.md "payments-observability.md") to monitor payment operations in CloudWatch.
- [Review IAM roles](payments-iam-roles.md "payments-iam-roles.md") to configure least-privilege access for production.
