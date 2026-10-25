

# Run an A/B test with configuration bundles
<a name="ab-testing-config-bundle"></a>

Use a configuration bundle when you are testing only a configuration change, such as a system prompt, model ID, or tool descriptions. Both variants run on the same AgentCore Runtime with different configuration bundle versions. When you run the A/B test, your agent receives the assigned bundle reference through W3C baggage headers, a standard mechanism for passing context between services. You deploy one AgentCore Runtime and one online evaluation configuration.

Key configuration for configuration bundle A/B tests:
+ Variant configuration: `variantConfiguration.configurationBundle` with bundle ARN and version
+ Evaluation configuration: a single shared `onlineEvaluationConfigArn` 

If the change you are testing involves code changes, a framework upgrade, or an entirely different agent implementation, use target-based routing instead. See [Run an A/B test with target-based routing](ab-testing-target-based.md).

This walkthrough uses a customer support agent as an example. The agent handles order lookups, returns, and discount requests. You will deploy the agent, create two configuration bundles with different system prompts (control and treatment), create an A/B test, send traffic, review results, and route traffic to the winner.

## Step 1: Create the project
<a name="config-bundle-create-project"></a>

Create the project with the AgentCore CLI:

```
agentcore create --name ABTestConfigBased --template empty
cd ABTestConfigBased
```

## Step 2: Add the runtime
<a name="config-bundle-add-runtime"></a>

Add the agent runtime:

```
agentcore add runtime \
  --name csAgent \
  --language python \
  --protocol HTTP
cd app/csAgent
uv init --bare
cd ../..
```

Abbreviated project structure:

```
ABTestConfigBased/
├── agentcore/
│   ├── agentcore.json      # Project and resource configuration
│   ├── aws-targets.json    # Populated with a deployment target during deploy
│   └── cdk/                # CDK infrastructure
└── app/
    └── csAgent/
        ├── main.py         # Agent entrypoint, created in Step 3
        └── pyproject.toml  # Python dependencies
```

## Step 3: Update the agent code and deploy
<a name="config-bundle-agent-code"></a>

Create `app/csAgent/main.py` with the following. The `BeforeModelCallEvent` hook reads the active configuration bundle at runtime:

```
"""Customer support agent with configuration bundle integration."""
from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from strands.hooks.events import BeforeModelCallEvent
from bedrock_agentcore.runtime import BedrockAgentCoreApp, BedrockAgentCoreContext

app = BedrockAgentCoreApp()
DEFAULT_MODEL_ID = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"
DEFAULT_SYSTEM_PROMPT = "You are a helpful customer support assistant."


@tool
def lookup_order(order_id: str) -> str:
    """Look up an order by ID."""
    orders = {
        "ORD-1001": {"status": "delivered", "item": "Blue T-Shirt", "total": "$29.99"},
        "ORD-1002": {"status": "in_transit", "item": "Running Shoes", "est_delivery": "2026-04-05"},
        "ORD-1003": {"status": "delayed", "item": "Wireless Headphones", "days_late": 5},
    }
    return str(orders.get(order_id, {"error": f"Order {order_id} not found"}))


@tool
def initiate_return(order_id: str, reason: str) -> str:
    """Initiate a return for an order."""
    return f"Return initiated for {order_id}. Reason: {reason}. Return label sent to customer email."


@tool
def apply_discount(order_id: str, discount_percent: int, reason: str) -> str:
    """Apply a discount to an order."""
    return f"Applied {discount_percent}% discount to {order_id}. Reason: {reason}."


def dynamic_config_hook(event: BeforeModelCallEvent):
    """Read config bundle and apply system prompt before every model call."""
    config = BedrockAgentCoreContext.get_config_bundle()
    event.agent.system_prompt = config.get("system_prompt", DEFAULT_SYSTEM_PROMPT)


agent = Agent(
    model=BedrockModel(model_id=DEFAULT_MODEL_ID),
    tools=[lookup_order, initiate_return, apply_discount],
    system_prompt=DEFAULT_SYSTEM_PROMPT,
)
agent.hooks.add_callback(BeforeModelCallEvent, dynamic_config_hook)


@app.entrypoint
def invoke(payload, context):
    result = agent(str(payload.get("prompt", "Hello")))
    return {"response": result.message["content"][0]["text"]}


if __name__ == "__main__":
    app.run()
```

Update `app/csAgent/pyproject.toml` dependencies:

```
dependencies = [
    "aws-opentelemetry-distro",
    "bedrock-agentcore >= 1.8.0",
    "boto3",
    "botocore[crt] >= 1.35.0",
    "strands-agents[otel] >= 1.13.0",
    "opentelemetry-distro",
    "opentelemetry-instrumentation",
]
```

Deploy the customer support agent to AgentCore Runtime:

```
agentcore deploy
```

After deployment, check the project status and note the `arn` field for `csAgent`. This is the Runtime ARN, and the Runtime ID is the last segment of that ARN. You will use the ID to create the online evaluation configuration and the ARN in the configuration bundle components:

```
agentcore status --json
```

Verify the agent is running:

```
agentcore invoke --runtime csAgent \
  --payload '{"prompt":"What is the status of order ORD-1003?"}'
```

The `BeforeModelCallEvent` hook fires before each LLM call, reading the active configuration bundle from the request context. During an A/B test, the AgentCore Gateway assigns each session to a variant and propagates the corresponding bundle reference via W3C baggage headers. The runtime makes this available through `BedrockAgentCoreContext`, so control sessions receive the control bundle and treatment sessions receive the treatment bundle. The agent applies the system prompt from the bundle it receives.

For more details, see [Use configuration bundles at runtime](configuration-bundles-runtime.md).

## Step 4: Create configuration bundles
<a name="config-bundle-create-bundles"></a>

Create two configuration bundles, one for control (current prompt) and one for treatment (optimized prompt). The A/B test will split traffic between these to measure which prompt yields better evaluator scores. In each command, replace `<runtime-arn>` with the `arn` value for `csAgent` from `agentcore status --json`.

Control bundle — the current system prompt:

```
agentcore eval config-bundle create \
  --name customerSupportControl \
  --components '{
    "<runtime-arn>": {
      "configuration": {
        "system_prompt": "You are a helpful customer support assistant for Acme Store."
      }
    }
  }' \
  --json
```

Treatment bundle — an optimized system prompt that instructs the agent to be more proactive:

```
agentcore eval config-bundle create \
  --name customerSupportTreatment \
  --components '{
    "<runtime-arn>": {
      "configuration": {
        "system_prompt": "You are a customer support assistant for Acme Store. Be proactive: check order status before the customer asks, offer discounts for delayed orders, and summarize actions taken at the end of each response."
      }
    }
  }' \
  --json
```

Each command returns a `bundleId`, `bundleArn`, and `versionId`. Save these values for each bundle. The A/B test command uses the bundle and version IDs, and the final Gateway rule uses the bundle ARN and version ID.

## Step 5: Create an online evaluation configuration
<a name="config-bundle-online-eval"></a>

An A/B test requires an online evaluation configuration to score sessions from both variants. The online evaluation runs evaluators against live traffic and feeds scores to the A/B test’s statistical engine.

For configuration bundle variants, create a single online evaluation config that monitors the shared AgentCore Runtime:

```
agentcore eval online-eval create \
  --name customerSupportEval \
  --agent <runtime-id> \
  --evaluators Builtin.Helpfulness \
  --sampling-rate 100 \
  --enable-on-create true \
  --json
```

Save the returned `onlineEvaluationConfigId`. You need it to create the A/B test.

**Tip**  
Set `--sampling-rate 100` during A/B testing so that every session is evaluated and results reach statistical significance faster. You can lower the rate after the test concludes.

For more details on evaluator options and configuration, see [Create online evaluation](create-online-evaluations.md).

## Step 6: Create the gateway and target
<a name="config-bundle-create-gateway"></a>

A config-bundle A/B test routes traffic through an AgentCore Gateway, so the gateway and its target must already be deployed before you start the test. Add a gateway with the runtime as a Runtime target (target type `httpRuntime`), then deploy:

```
agentcore add gateway --name csGateway --authorizer-type AWS_IAM

agentcore add gateway-target \
  --name customer-support \
  --gateway csGateway \
  --runtime csAgent

agentcore deploy

agentcore status --json
```

Read the `arn` field for `csGateway` in the `status` output. The Gateway ID is the last segment of that ARN. Save the Gateway ID. The A/B test command and final routing rule use the deployed ID rather than the project resource name.

## Step 7: Create the A/B test
<a name="config-bundle-create-test"></a>

Create an A/B test that splits traffic 80/20 between the control and treatment prompts. Both variants reference configuration bundles on the same AgentCore Runtime and share a single online evaluation config for scoring.

**Example**  

```
agentcore eval ab-test config-based run \
  --name customerSupportPromptTest \
  --gateway <gateway-id> \
  --control '{"config-bundle":"<control-bundle-id>","bundle-version":"<control-bundle-version-id>"}' \
  --treatment '{"config-bundle":"<treatment-bundle-id>","bundle-version":"<treatment-bundle-version-id>"}' \
  --online-eval <online-evaluation-config-id> \
  --treatment-weight 20 \
  --gateway-filter '{"targetPaths":["/customer-support/*"]}'
```
The command creates the A/B test directly on the service and starts it by default. Pass `--enable-on-create false` to create it paused. The `--gateway` value is the deployed Gateway ID from Step 6. The command returns the `abTestId` that the lifecycle commands below require. Only one test can be running per Gateway at a time.  
Use the bundle and version IDs returned in Step 4, not the bundle names or ARNs.

```
import boto3
import uuid

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.create_ab_test(
    name="customerSupportPromptTest",
    gatewayArn="arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/gw-abc123",
    roleArn="arn:aws:iam::123456789012:role/ABTestRole",
    evaluationConfig={
        "onlineEvaluationConfigArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:online-evaluation-config/eval-abc123"
    },
    variants=[
        {
            "name": "C",
            "weight": 80,
            "variantConfiguration": {
                "configurationBundle": {
                    "bundleArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:configuration-bundle/customerSupportControl-Ab1Cd2Ef3G",
                    "bundleVersion": "12345678-1234-1234-1234-123456789012"
                }
            }
        },
        {
            "name": "T1",
            "weight": 20,
            "variantConfiguration": {
                "configurationBundle": {
                    "bundleArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:configuration-bundle/customerSupportTreatment-Ab1Cd2Ef3G",
                    "bundleVersion": "12345678-1234-5678-9abc-123456789012"
                }
            }
        }
    ],
    enableOnCreate=True,
    clientToken=str(uuid.uuid4()),
)

ab_test_id = response["abTestId"]
print(f"Created A/B test: {ab_test_id}")
print(f"Status: {response['status']}")
print(f"Execution status: {response['executionStatus']}")
```

## Step 8: Send traffic through the AgentCore Gateway
<a name="config-bundle-send-traffic"></a>

After the A/B test is running, send traffic through the AgentCore Gateway HTTP endpoint. The AgentCore Gateway assigns each request to a variant (control or treatment) based on the runtime session ID.

### How variant assignment works
<a name="_how_variant_assignment_works"></a>

The AgentCore Gateway uses the `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id` header to determine which configuration bundle variant to serve. This header is **optional** — if you do not provide it, the runtime generates a session ID automatically. The AgentCore Gateway then uses the session ID (whether you provided it or the runtime generated it) to assign the request to a variant based on your configured traffic weights.

Session assignment is **sticky**: once a session ID is assigned to a variant, all subsequent requests with that same session ID route to the same variant. This ensures a consistent experience within a session while still distributing new sessions across variants according to your traffic split.

### Generate traffic for testing
<a name="_generate_traffic_for_testing"></a>

Save the following script as `loadgen.sh` in the project directory. The script sends every request to the `customer-support` target path, which the A/B test filter intercepts. Each request uses a new session ID:

```
#!/bin/bash
PROMPTS=(
  "What is the status of order ORD-1003?"
  "I want to return order ORD-1001, it doesn't fit."
  "My order ORD-1003 is late. Can I get a discount?"
  "Where is my order ORD-1002?"
  "I need help with a return for order ORD-1001. The color is wrong."
  "Can you check on order ORD-1003? I've been waiting forever."
  "I'd like to cancel order ORD-1002 if it hasn't shipped yet."
  "Order ORD-1003 is delayed again. This is unacceptable."
  "What's your return policy for order ORD-1001?"
  "My headphones order ORD-1003 still hasn't arrived. What can you do?"
)

for i in $(seq 1 30); do
  PROMPT="${PROMPTS[$(( (i - 1) % ${#PROMPTS[@]} ))]}"
  echo "=== Request $i: $PROMPT ==="
  agentcore invoke --gateway csGateway \
    --path /customer-support/invocations \
    --session-id "$(uuidgen)" \
    --payload "{\"prompt\": \"$PROMPT\"}"
  echo ""
  sleep 2
done
```

Run the script:

```
bash loadgen.sh
```

## Step 9: Get results
<a name="config-bundle-get-results"></a>

Poll the A/B test to monitor results as sample sizes grow. Polling does not affect statistical validity.

**Example**  
Get current results (replace `<ab-test-id>` with the ID returned in Step 7):  

```
agentcore eval ab-test get --id <ab-test-id>
```
Get results as JSON:  

```
agentcore eval ab-test get --id <ab-test-id> --json
```
Poll until results reach statistical significance:  

```
import boto3
import time

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

ab_test_id = "customerSupportPromptTest-Ab1Cd2Ef3G"

while True:
    response = client.get_ab_test(abTestId=ab_test_id)

    status = response["status"]
    exec_status = response["executionStatus"]
    print(f"Status: {status}, Execution: {exec_status}")

    results = response.get("results")
    if results:
        print(f"Analysis timestamp: {results.get('analysisTimestamp')}")
        for metric in results["evaluatorMetrics"]:
            evaluator = metric["evaluatorArn"]
            control = metric["controlStats"]
            print(f"\nEvaluator: {evaluator}")
            print(f"  Control: mean={control['mean']:.3f}, n={control['sampleSize']}")

            for variant in metric["variantResults"]:
                print(f"  {variant['variantName']}: mean={variant['mean']:.3f}, "
                      f"n={variant['sampleSize']}, "
                      f"pValue={variant.get('pValue', 'N/A')}, "
                      f"significant={variant['isSignificant']}")

                if variant["isSignificant"]:
                    print(f"  >>> Statistically significant! "
                          f"Change: {variant.get('percentChange', 0):.1f}%")

        # Check if any evaluator has reached significance
        all_significant = all(
            variant["isSignificant"]
            for metric in results["evaluatorMetrics"]
            for variant in metric["variantResults"]
        )
        if all_significant:
            print("\nAll evaluators have reached statistical significance.")
            break

    time.sleep(300)  # Poll every 5 minutes
```

**Note**  
The time it takes for results to appear depends primarily on the session timeout configured in your online evaluation config. A session is considered complete once no new requests arrive within the timeout window. After a session ends, results typically appear within 15 minutes. Results accumulate as more sessions complete — statistical significance improves with sample size.
+  **p-value < 0.05 and positive `percentChange`:** The treatment is significantly better than control. Consider deploying the treatment.
+  **p-value < 0.05 and negative `percentChange`:** The treatment is significantly worse. Keep the control.
+  **p-value >= 0.05:** Not enough evidence to conclude a difference. Continue collecting samples or increase traffic to the treatment.
+  **Check all evaluators:** A treatment may improve one metric while regressing another. Review all evaluator results before deciding.

For a detailed explanation of the results structure and field definitions, see [Understanding results](ab-testing-target-based.md#target-based-results-shape) in the target-based routing guide.

## Step 10: Confirm results and stop the A/B test
<a name="config-bundle-confirm-stop"></a>

Once the A/B test reaches statistical significance, review the results and stop the experiment.

1.  **Confirm significance.** Verify that the target evaluator has `isSignificant: true` and a positive `percentChange` on the treatment variant (or confirm the control is the winner if the treatment regressed).

1.  **Stop the A/B test.** Run `agentcore eval ab-test stop --id <ab-test-id>`. Traffic routing ends immediately and all requests revert to the default configuration. See [View, pause, resume, and stop](ab-testing-manage.md#manage-ab-test-start-stop).

## Step 11: Route traffic to the winner
<a name="config-bundle-deploy-winner"></a>

After stopping the A/B test, route all traffic to the winning configuration bundle version.

Use the AWS CLI to create a Gateway rule that applies the winning bundle, whether the control or the treatment won. Without a rule, the agent falls back to `DEFAULT_SYSTEM_PROMPT`, which differs from the control bundle’s prompt. Replace `<winning-bundle-arn>` and `<winning-bundle-version-id>` with the values that Step 4 returned for the winning bundle:

```
aws bedrock-agentcore-control create-gateway-rule \
  --gateway-identifier <gateway-id> \
  --priority 100 \
  --conditions '[{"matchPaths":{"anyOf":["/customer-support/*"]}}]' \
  --actions '[{"configurationBundle":{"staticOverride":{"bundleArn":"<winning-bundle-arn>","bundleVersion":"<winning-bundle-version-id>"}}}]'
```

The rule updates the live Gateway immediately. Save the returned rule ID so that you can update or delete the rule later. The rule is not part of the project, and `agentcore deploy` does not manage it. To change an existing production rule instead, use `aws bedrock-agentcore-control update-gateway-rule --gateway-identifier <gateway-id> --rule-id <rule-id>`. For more rule examples, see [Gateway rules API examples](gateway-rules-examples.md).

After routing traffic to the winner:
+  **Delete the A/B test** to clean up resources. See [Delete an A/B test](ab-testing-manage.md#manage-ab-test-remove).
+  **Delete the Gateway rule before you delete its bundle or remove the Gateway.** If you created a rule in Step 11, delete it before you delete the bundle or run `agentcore remove` on the target or the Gateway. To find the rule ID, run `agentcore gateway rule list --gateway-id <gateway-id>`. Then run `aws bedrock-agentcore-control delete-gateway-rule --gateway-identifier <gateway-id> --rule-id <rule-id>`. See [Route traffic to the winning variant](ab-testing-manage.md#manage-ab-test-promote).
+  **Monitor the new baseline.** Online evaluation continues scoring sessions on the winning configuration. Watch for regressions.
+  **Start the next iteration.** New traces from the winning configuration provide the foundation for the next recommendation cycle. See [How it works](optimization-how-it-works.md).

## Example: A/B testing tool descriptions
<a name="config-bundle-tool-description-example"></a>

You can use the same configuration bundle pattern to test optimized tool descriptions. Unlike system prompt A/B tests where the agent reads the bundle directly, tool description overrides are applied by the AgentCore Gateway. When the agent calls `tools/list` through the gateway, the gateway reads the configuration bundle and returns tool descriptions with overrides applied. No agent code changes are needed.

For details on how the gateway applies tool description overrides, see [Behavior on MCP targets](gateway-rules-propagation.md#gateway-rules-propagation-mcp).

### Configuration bundles
<a name="_configuration_bundles"></a>

As in Step 4, replace `<runtime-arn>` with the `arn` value for `csAgent` from `agentcore status --json`.

Control bundle — current tool descriptions:

```
agentcore eval config-bundle create \
  --name toolDescControl \
  --components '{
    "<runtime-arn>": {
      "configuration": {
        "tools": {
          "lookup_order": {
            "description": "Look up an order by ID."
          },
          "initiate_return": {
            "description": "Initiate a return for an order."
          },
          "apply_discount": {
            "description": "Apply a discount to an order."
          }
        }
      }
    }
  }' \
  --json
```

Treatment bundle — optimized tool descriptions from a recommendation:

```
agentcore eval config-bundle create \
  --name toolDescTreatment \
  --components '{
    "<runtime-arn>": {
      "configuration": {
        "tools": {
          "lookup_order": {
            "description": "Look up order details including status, item, and total by order ID. Use when the customer asks about an order or references an order number."
          },
          "initiate_return": {
            "description": "Start a return process for an order. Use only when the customer explicitly requests a return or exchange, not for order status inquiries."
          },
          "apply_discount": {
            "description": "Apply a percentage discount to an order. Use when compensating for service issues such as delivery delays. Requires a reason."
          }
        }
      }
    }
  }' \
  --json
```

### How it works
<a name="_how_it_works"></a>

1. When the agent calls `tools/list` through the gateway (MCP targets), the A/B test assigns each session to a variant (control or treatment) on the gateway and resolves the corresponding configuration bundle.

1. Gateway reads the configuration bundle and returns tool descriptions with overrides applied.

1. The agent uses the returned descriptions for tool selection — no agent code changes required.

### Create the A/B test
<a name="_create_the_ab_test"></a>

```
agentcore eval ab-test config-based run \
  --name toolDescTest \
  --gateway <gateway-id> \
  --control '{"config-bundle":"<control-bundle-id>","bundle-version":"<control-bundle-version-id>"}' \
  --treatment '{"config-bundle":"<treatment-bundle-id>","bundle-version":"<treatment-bundle-version-id>"}' \
  --online-eval <online-evaluation-config-id> \
  --treatment-weight 20
```

The remaining steps (send traffic, get results, and route traffic to the winner) are identical to the preceding system prompt example.

## Troubleshooting
<a name="config-bundle-troubleshooting"></a>

For troubleshooting A/B test issues (such as missing results after sending traffic), see [Troubleshooting](ab-testing-target-based.md#target-based-troubleshooting) in the target-based routing guide.