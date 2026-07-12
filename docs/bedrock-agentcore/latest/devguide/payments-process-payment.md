# Process a payment

To process a payment, you need two resources:

- **Payment instrument** — An embedded crypto wallet with Coinbase or Stripe. See [Create a payment instrument](payments-create-instrument.md "payments-create-instrument.md").
- **Payment session** — A time-bounded session that optionally enforces a spending budget. See [Create a payment session](payments-create-session.md "payments-create-session.md").
  Once both exist, call `ProcessPayment` with the payment session ID, payment instrument ID, and an x402 payment payload. The service validates the request, checks the budget, signs the transaction on the appropriate blockchain, and returns a cryptographic proof. For the complete request and response schema, see [ProcessPayment](../APIReference/API_ProcessPayment.md "../APIReference/API_ProcessPayment.md") in the API Reference.

###### Tip

You can automate the steps on this page with the AgentCore Payments skill in the AWS agent toolkit. The skill is part of the **aws-agents** plugin and lets an AI coding agent create your Payment Manager, connector, credential provider, payment instrument, and session using the `agentcore` CLI, and add an x402 payment tool to your agent. For details, see the [quickstart](payments-getting-started.md "payments-getting-started.md") and the [AWS agent toolkit on GitHub](https://github.com/aws/agent-toolkit-for-aws/tree/main "https://github.com/aws/agent-toolkit-for-aws/tree/main").

There are five ways to invoke the ProcessPayment API:

###### Example

AgentCore CLI
If your agent is deployed with payment capabilities configured, invoke it with payment context and the x402 interceptor handles payment processing automatically:

```
agentcore invoke \
  --prompt "Access the premium endpoint at https://example-x402-merchant.com/paid-api" \
  --payment-instrument-id <INSTRUMENT_ID> \
  --auto-session \
  --payment-user-id user@example.com
```

To use an explicit session instead of auto-creating one:

```
agentcore invoke \
  --prompt "Access the premium endpoint at https://example-x402-merchant.com/paid-api" \
  --payment-instrument-id <INSTRUMENT_ID> \
  --payment-session-id <SESSION_ID> \
  --payment-user-id user@example.com
```

The deployed agent’s x402 plugin intercepts HTTP 402 responses, calls `ProcessPayment`, and retries the request with proof. Requires AgentCore CLI v0.19.0 or later.

AWS CLI

```
aws bedrock-agentcore process-payment \
    --payment-manager-arn "arn:aws:bedrock-agentcore:us-west-2:123456789012:payment-manager/my-manager" \
    --payment-session-id "payment-session-abc123" \
    --payment-instrument-id "payment-instrument-xyz789" \
    --payment-type "CRYPTO_X402" \
    --payment-input '{
        "cryptoX402": {
            "version": "2",
            "payload": {
                "scheme": "exact",
                "network": "eip155:84532",
                "amount": "100000",
                "asset": "0x036CbD53842c5426634e7929541eC2318f3dCF7e",
                "payTo": "0x99935f281d3ED1E804bF1413b76E0B03e1fed4F9",
                "maxTimeoutSeconds": 300,
                "extra": {"name": "USDC", "version": "2"}
            }
        }
    }' \
    --client-token "$(uuidgen)" \
    --region us-west-2
```

AWS SDK
Call `process_payment` directly with the full x402 payload:

```
import uuid

payment = dp_client.process_payment(
    userId="test-user-123",
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    paymentSessionId=SESSION_ID,
    paymentInstrumentId=INSTRUMENT_ID,
    paymentType="CRYPTO_X402",
    paymentInput={
        "cryptoX402": {
            "version": "2",
            "payload": {
                "scheme": "exact",
                "network": "eip155:84532",
                "amount": "100000",
                "asset": "0x036CbD53842c5426634e7929541eC2318f3dCF7e",
                "payTo": "0x99935f281d3ED1E804bF1413b76E0B03e1fed4F9",
                "maxTimeoutSeconds": 300,
                "extra": {"name": "USDC", "version": "2"},
            },
        }
    },
    clientToken=str(uuid.uuid4()),
)
```

Response:

```
{
    "processPaymentId": "12345678-1234-1234-1234-123456789012",
    "paymentManagerArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:payment-manager/my-manager-a1b2c3d4e5",
    "paymentSessionId": "payment-session-abc123def4567",
    "paymentInstrumentId": "payment-instrument-xyz789abc1234",
    "paymentType": "CRYPTO_X402",
    "status": "PROOF_GENERATED",
    "paymentOutput": {
        "cryptoX402": {
            "version": "2",
            "payload": {
                "...signed transaction proof..."
            }
        }
    },
    "createdAt": "2025-07-15T10:35:00Z",
    "updatedAt": "2025-07-15T10:35:02Z"
}
```

A `status` of `PROOF_GENERATED` indicates the transaction was signed and the cryptographic proof is included in `paymentOutput`.

AgentCore SDK
Use the `PaymentManager` class to generate payment headers manually within any agent framework:

```
import uuid
from bedrock_agentcore.payments import PaymentManager

manager = PaymentManager(
    payment_manager_arn=mgr["paymentManagerArn"],
    region_name="us-west-2"
)

# When you receive a 402 response, generate payment proof
payment_required_request = {
    "statusCode": 402,
    "headers": payment_required["headers"],
    "body": payment_required["body"],
}
payment_proof_headers = manager.generate_payment_header(
    user_id="test-user-123",
    payment_instrument_id=instrument["paymentInstrumentId"],
    payment_session_id=session["paymentSessionId"],
    payment_required_request=payment_required_request,
    client_token=str(uuid.uuid4()),
)
```

`payment_proof_headers` contains the payment proof header. Include this header when retrying the request to the paid endpoint. You can also call the `process_payment` method of `PaymentManager` for more control over inputs.

Strands SDK
The AgentCore payments plugin provides automated payment processing for Strands Agents. It supports the [x402 Payment Required](https://www.x402.org/ "https://www.x402.org/") protocol, enabling agents to automatically handle HTTP 402 responses.

**Installation:**

```
pip install 'bedrock-agentcore[strands-agents]'
```

**Configure and use the plugin:**

```
from strands import Agent
from strands_tools import http_request
from bedrock_agentcore.payments.integrations.config import AgentCorePaymentsPluginConfig
from bedrock_agentcore.payments.integrations.strands.plugin import AgentCorePaymentsPlugin

# Configure the plugin
config = AgentCorePaymentsPluginConfig(
    payment_manager_arn="arn:aws:bedrock-agentcore:us-west-2:123456789012:payment-manager/pm-abc123",
    user_id="test-user-123",
    payment_instrument_id="payment-instrument-XJU4RSQP9VO0ler",
    payment_session_id="payment-session-xuzrnUCd7RT725G",
    region="us-west-2",
)

# Create the plugin
plugin = AgentCorePaymentsPlugin(config=config)

# Create agent with the plugin
agent = Agent(
    system_prompt="You are a helpful assistant that can access paid APIs.",
    tools=[http_request],
    plugins=[plugin],
)

# Use the agent -- 402 responses are automatically handled
agent("access https://drvd12nxpcyd5.cloudfront.net/market-recap")
```

The AgentCore payments plugin intercepts x402 payment requests automatically, processes the payment, and retries the request with payment proof for the agent.

## Strands SDK reference

The following sections describe Strands-specific configuration and behavior.

### Handling payment interrupts

When payment processing fails, the plugin stores the failure and raises an interrupt. Your application should handle these interrupts:

```
result = agent("Access the premium endpoint at https://api.example.com/premium")
while result.stop_reason == "interrupt":
    responses = []
    for interrupt in result.interrupts:
        if interrupt.name.startswith("payment-failure-"):
            reason = interrupt.reason
            exception_type = reason.get("exceptionType")

            if exception_type == "PaymentInstrumentConfigurationRequired":
                plugin.config.update_payment_instrument_id("payment-instrument-new123")
                responses.append({
                    "interruptResponse": {
                        "interruptId": interrupt.id,
                        "response": "Payment instrument configured. Please retry.",
                    }
                })
            elif exception_type == "PaymentSessionConfigurationRequired":
                plugin.config.update_payment_session_id("payment-session-new456")
                responses.append({
                    "interruptResponse": {
                        "interruptId": interrupt.id,
                        "response": "Payment session configured. Please retry.",
                    }
                })
            else:
                responses.append({
                    "interruptResponse": {
                        "interruptId": interrupt.id,
                        "response": f"Payment failed: {reason.get('exceptionMessage')}",
                    }
                })

    result = agent(responses)
```

### Disabling auto-payment

To access only payment visibility tools without automatic payment execution (for example, to keep a human or custom logic in the loop before any payment transaction), disable automatic processing:

```
config = AgentCorePaymentsPluginConfig(
    payment_manager_arn="arn:aws:bedrock-agentcore:us-east-1:123456789012:payment-manager/pm-abc123",
    user_id="user-123",
    region="us-east-1",
    auto_payment=False,  # Disable automatic 402 processing
)
```

### Network preferences

You can specify preferred blockchain networks for payment processing:

```
config = AgentCorePaymentsPluginConfig(
    payment_manager_arn="arn:aws:bedrock-agentcore:us-east-1:123456789012:payment-manager/pm-abc123",
    user_id="user-123",
    payment_instrument_id="payment-instrument-xyz789",
    payment_session_id="payment-session-def456",
    region="us-east-1",
    network_preferences_config=["eip155:8453", "base-sepolia", "solana-mainnet"],
)
```

If not specified, the system uses a default preference order prioritizing Solana mainnet and Base (Ethereum L2) for low transaction fees.

### Configuration options

The following table lists the `AgentCorePaymentsPluginConfig` parameters:

| Parameter                    | Type                  | Required             | Description                                                                  |
| ---------------------------- | --------------------- | -------------------- | ---------------------------------------------------------------------------- |
| `payment_manager_arn`        | `str`                 | Yes                  | ARN of the Bedrock AgentCore Payment Manager resource                        |
| `user_id`                    | `str`                 | Yes                  | Unique identifier for the user                                               |
| `payment_instrument_id`      | `Optional[str]`       | No                   | Payment instrument ID. Can be set later via `update_payment_instrument_id()` |
| `payment_session_id`         | `Optional[str]`       | No                   | Payment session ID. Can be set later via `update_payment_session_id()`       |
| `region`                     | `Optional[str]`       | No                   | AWS region for the payment manager                                           |
| `network_preferences_config` | `Optional[list[str]]` | No                   | List of network CAIP-2 identifiers in order of preference                    |
| `auto_payment`               | `bool`                | No (default: `True`) | Whether to automatically process 402 payment requirements                    |
| `max_interrupt_retries`      | `int`                 | No (default: `5`)    | Maximum interrupt retries per tool use. Set to 0 to disable interrupts       |
| `agent_name`                 | `Optional[str]`       | No                   | Agent name propagated via HTTP header on API calls                           |

### Built-in agent tools

The plugin registers three tools that agents can use to query payment information at runtime:

| Tool                       | Description                                                       |
| -------------------------- | ----------------------------------------------------------------- |
| `get_payment_instrument`   | Retrieve details about a specific payment instrument              |
| `list_payment_instruments` | List all payment instruments for a user                           |
| `get_payment_session`      | Retrieve details about a payment session (budget, status, expiry) |

These tools enable agents to make informed decisions about payment methods and payment limits during conversations. For more details and end-to-end examples, refer to the [Strands Agents](https://strandsagents.com/latest/ "https://strandsagents.com/latest/") documentation.
