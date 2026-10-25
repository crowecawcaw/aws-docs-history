

# Run an A/B test with target-based routing
<a name="ab-testing-target-based"></a>

Use the target-based routing pattern when the change you are testing involves code changes, a framework upgrade, or an entirely different agent implementation. Target-based routing routes traffic between multiple versions of the same AgentCore Runtime (named endpoints), or between entirely different AgentCore Runtimes. The AgentCore Gateway registers each endpoint as a separate target and routes each session to one endpoint or the other based on the A/B test’s traffic weights.

Key configuration for target-based A/B tests:
+ Variant configuration: `variantConfiguration.target` with the AgentCore Gateway target name
+ Evaluation configuration: `perVariantOnlineEvaluationConfig` (one online evaluation config per variant, since each endpoint has its own log group)
+ Gateway filter: `gatewayFilter.targetPaths` scopes which AgentCore Gateway paths the A/B test intercepts

This walkthrough deploys two versions of the customer support agent. The control uses Claude Sonnet and the treatment uses Claude Opus. You create an endpoint for each version, run an A/B test, send traffic, review the results, and route traffic to the winner.

**Note**  
This walkthrough is for agents hosted on an AgentCore Runtime. If your agent runs **outside** an AgentCore Runtime (a third-party or self-hosted agent — for example on AWS Lambda), see [Run an A/B test for agents hosted outside of AgentCore](ab-testing-3p-agents.md) instead.

For a detailed comparison of A/B test patterns, see [Choosing a pattern](ab-testing.md#ab-testing-pattern-comparison).

## Step 1: Create the project
<a name="target-based-create-project"></a>

Create the project with the AgentCore CLI:

```
agentcore create --name ABTestTargetBased --template empty
cd ABTestTargetBased
```

## Step 2: Add the runtime
<a name="target-based-add-runtime"></a>

Add the agent runtime. You will deploy two versions of this runtime — one for control and one for treatment — then create named endpoints to alias each version.

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
ABTestTargetBased/
├── agentcore/
│   ├── agentcore.json
│   ├── aws-targets.json
│   └── cdk/
└── app/
    └── csAgent/
        ├── main.py         # Created in Step 3
        └── pyproject.toml
```

## Step 3: Deploy control and treatment versions
<a name="target-based-agent-code"></a>

Create `app/csAgent/main.py` with the control version (using Claude Sonnet):

```
"""Customer support agent — control variant."""
from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()
MODEL_ID = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"
SYSTEM_PROMPT = "You are a helpful customer support assistant for Acme Store."


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


agent = Agent(
    model=BedrockModel(model_id=MODEL_ID),
    tools=[lookup_order, initiate_return, apply_discount],
    system_prompt=SYSTEM_PROMPT,
)


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

Deploy the control version (this creates version 1):

```
agentcore deploy
```

Now update `main.py` to use a different model for the treatment variant and deploy (this creates version 2):

```
MODEL_ID = "global.anthropic.claude-opus-4-6-v1"
```

```
agentcore deploy
```

Create named endpoints for each version and deploy:

```
agentcore add runtime-endpoint \
  --runtime csAgent \
  --name control \
  --version 1 \
  --description "Control variant — Claude Sonnet"

agentcore add runtime-endpoint \
  --runtime csAgent \
  --name treatment \
  --version 2 \
  --description "Treatment variant — Claude Opus"

agentcore deploy
```

You now have:
+ Runtime endpoint `control` — serving version 1 with Claude Sonnet.
+ Runtime endpoint `treatment` — serving version 2 with Claude Opus.

Verify the runtime is working. The `arn` field for `csAgent` in the `status` output is the Runtime ARN, and the Runtime ID is the last segment of that ARN.

```
agentcore status --json

agentcore invoke --runtime csAgent \
  --qualifier control \
  --payload '{"prompt":"What is the status of order ORD-1003?"}'
```

## Step 4: Create online evaluation configurations
<a name="target-based-online-eval"></a>

Each endpoint has its own log group (the log group name ends with the endpoint name), so you need one online evaluation config per variant:

```
agentcore eval online-eval create \
  --name controlEvalTb \
  --agent <runtime-id> \
  --endpoint control \
  --evaluators Builtin.Helpfulness \
  --sampling-rate 100 \
  --enable-on-create true \
  --json

agentcore eval online-eval create \
  --name treatmentEvalTb \
  --agent <runtime-id> \
  --endpoint treatment \
  --evaluators Builtin.Helpfulness \
  --sampling-rate 100 \
  --enable-on-create true \
  --json
```

Save the `onlineEvaluationConfigId` that each command returns. You need both IDs to create the A/B test.

For more details on evaluator options and configuration, see [Create online evaluation](create-online-evaluations.md).

## Step 5: Create the gateway and targets
<a name="target-based-create-gateway"></a>

A target-based A/B test routes traffic through an AgentCore Gateway, so the gateway and its two targets must already be deployed before you start the test. Add a gateway and register each runtime endpoint as a Runtime target (target type `httpRuntime`), then deploy:

```
agentcore add gateway --name csGateway --authorizer-type AWS_IAM

agentcore add gateway-target \
  --name customer-support-control \
  --gateway csGateway \
  --runtime csAgent \
  --runtime-endpoint control

agentcore add gateway-target \
  --name customer-support-treatment \
  --gateway csGateway \
  --runtime csAgent \
  --runtime-endpoint treatment

agentcore deploy

agentcore status --json
```

Read the `arn` field for `csGateway` in the `status` output. The Gateway ID is the last segment of that ARN. Save the Gateway ID. The A/B test command and final routing rule use the deployed ID rather than the project resource name.

## Step 6: Create the A/B test
<a name="target-based-create-test"></a>

Start the A/B test with `agentcore eval ab-test target-based run`. Each variant references one of the Gateway targets you created and has its own online evaluation config. The command initiates the test directly on the service against the already-deployed Gateway.

**Example**  

```
agentcore eval ab-test target-based run \
  --name customerSupportTargetTest \
  --gateway <gateway-id> \
  --control '{"gateway-target":"customer-support-control","online-eval":"<control-online-evaluation-config-id>"}' \
  --treatment '{"gateway-target":"customer-support-treatment","online-eval":"<treatment-online-evaluation-config-id>"}' \
  --treatment-weight 20 \
  --gateway-filter '{"targetPaths":["/customer-support-control/*"]}'
```
The test starts running by default. Pass `--enable-on-create false` to create it paused. The `--gateway` value is the deployed Gateway ID from Step 5, and each `online-eval` value is an ID returned in Step 4. The command returns the `abTestId` that the lifecycle commands below require. Only one test can be running per Gateway at a time.

```
import boto3
import uuid

REGION = "us-west-2"
ACCOUNT_ID = "123456789012"

# Runtime ARN from the Step 3 deployment output
RUNTIME_ARN = f"arn:aws:bedrock-agentcore:{REGION}:{ACCOUNT_ID}:runtime/ABTestTargetBased_csAgent-abc123"

# Online evaluation config ARNs from Step 4
CONTROL_EVAL_ARN = f"arn:aws:bedrock-agentcore:{REGION}:{ACCOUNT_ID}:online-evaluation-config/controlEvalTb-abc123"
TREATMENT_EVAL_ARN = f"arn:aws:bedrock-agentcore:{REGION}:{ACCOUNT_ID}:online-evaluation-config/treatmentEvalTb-def456"

# IAM roles
GATEWAY_ROLE_ARN = f"arn:aws:iam::{ACCOUNT_ID}:role/AgentCoreGatewayRole"
AB_TEST_ROLE_ARN = f"arn:aws:iam::{ACCOUNT_ID}:role/ABTestRole"

cp_client = boto3.client("bedrock-agentcore-control", region_name=REGION)
dp_client = boto3.client("bedrock-agentcore", region_name=REGION)

# 1. Create an AgentCore Gateway
gateway_response = cp_client.create_gateway(
    name="customerSupportTargetTest-gw",
    roleArn=GATEWAY_ROLE_ARN,
    authorizerType="AWS_IAM",
    clientToken=str(uuid.uuid4()),
)
gateway_id = gateway_response["gatewayId"]
gateway_arn = gateway_response["gatewayArn"]
print(f"Created AgentCore Gateway: {gateway_id}")

# 2. Add the control endpoint as an AgentCore Gateway target
cp_client.create_gateway_target(
    gatewayIdentifier=gateway_id,
    name="customer-support-control",
    targetConfiguration={
        "http": {
            "agentcoreRuntime": {
                "arn": RUNTIME_ARN,
                "qualifier": "control"
            }
        }
    },
    clientToken=str(uuid.uuid4()),
)
print("Added target: customer-support-control")

# 3. Add the treatment endpoint as an AgentCore Gateway target
cp_client.create_gateway_target(
    gatewayIdentifier=gateway_id,
    name="customer-support-treatment",
    targetConfiguration={
        "http": {
            "agentcoreRuntime": {
                "arn": RUNTIME_ARN,
                "qualifier": "treatment"
            }
        }
    },
    clientToken=str(uuid.uuid4()),
)
print("Added target: customer-support-treatment")

# 4. Create the A/B test
response = dp_client.create_ab_test(
    name="customerSupportTargetTest",
    gatewayArn=gateway_arn,
    roleArn=AB_TEST_ROLE_ARN,
    evaluationConfig={
        "perVariantOnlineEvaluationConfig": [
            {"name": "C", "onlineEvaluationConfigArn": CONTROL_EVAL_ARN},
            {"name": "T1", "onlineEvaluationConfigArn": TREATMENT_EVAL_ARN}
        ]
    },
    gatewayFilter={
        "targetPaths": ["/customer-support-control/*"]
    },
    variants=[
        {
            "name": "C",
            "weight": 80,
            "variantConfiguration": {
                "target": {"name": "customer-support-control"}
            }
        },
        {
            "name": "T1",
            "weight": 20,
            "variantConfiguration": {
                "target": {"name": "customer-support-treatment"}
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

## Step 7: Send traffic through the AgentCore Gateway
<a name="target-based-send-traffic"></a>

After the A/B test is running, send traffic through the AgentCore Gateway HTTP endpoint. The AgentCore Gateway assigns each request to a variant (control or treatment) based on the runtime session ID.

### How variant assignment works
<a name="_how_variant_assignment_works"></a>

The AgentCore Gateway uses the `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id` header to determine which target to route traffic to. This header is **optional** — if you do not provide it, the runtime generates a session ID automatically. The AgentCore Gateway then uses the session ID (whether you provided it or the runtime generated it) to assign the request to a variant based on your configured traffic weights.

Session assignment is **sticky**: once a session ID is assigned to a variant, all subsequent requests with that same session ID route to the same target. This ensures a consistent experience within a session while still distributing new sessions across variants according to your traffic split.

### Generate traffic for testing
<a name="_generate_traffic_for_testing"></a>

Save the following script as `loadgen.sh` in the project directory. The script sends every request to the `customer-support-control` target path. The A/B test filter intercepts only the control target path, and the Gateway splits that traffic between both variants. Each request uses a new session ID:

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
    --path /customer-support-control/invocations \
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

## Step 8: Get results
<a name="target-based-get-results"></a>

Poll the A/B test to monitor results as sample sizes grow. Polling does not affect statistical validity.

**Example**  
Get current results (replace `<ab-test-id>` with the ID returned in Step 6):  

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

ab_test_id = "customerSupportTargetTest-Ab1Cd2Ef3G"

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
The time it takes for results to appear depends primarily on the session timeout configured in your online evaluation configs. A session is considered complete once no new requests arrive within the timeout window. After a session ends, results typically appear within 15 minutes. Results accumulate as more sessions complete — statistical significance improves with sample size.
+  **p-value < 0.05 and positive `percentChange`:** The treatment is significantly better than control. Consider deploying the treatment.
+  **p-value < 0.05 and negative `percentChange`:** The treatment is significantly worse. Keep the control.
+  **p-value >= 0.05:** Not enough evidence to conclude a difference. Continue collecting samples or increase traffic to the treatment.
+  **Check all evaluators:** A treatment may improve one metric while regressing another. Review all evaluator results before deciding.

## Step 9: Confirm results and stop the A/B test
<a name="target-based-confirm-stop"></a>

Once the A/B test reaches statistical significance, review the results and stop the experiment.

1.  **Confirm significance.** Verify that the target evaluator has `isSignificant: true` and a positive `percentChange` on the treatment variant (or confirm the control is the winner if the treatment regressed).

1.  **Stop the A/B test.** Run `agentcore eval ab-test stop --id <ab-test-id>`. Traffic routing ends immediately and all requests revert to the default target. See [View, pause, resume, and stop](ab-testing-manage.md#manage-ab-test-start-stop).

## Step 10: Route traffic to the winner
<a name="target-based-deploy-winner"></a>

After stopping the A/B test, route all traffic to the winning variant.

If the control won, no routing change is required. If the treatment won, use the AWS CLI to create a Gateway rule that routes requests for the control path to the treatment target:

```
aws bedrock-agentcore-control create-gateway-rule \
  --gateway-identifier <gateway-id> \
  --priority 100 \
  --conditions '[{"matchPaths":{"anyOf":["/customer-support-control/*"]}}]' \
  --actions '[{"routeToTarget":{"staticRoute":{"targetName":"customer-support-treatment"}}}]'
```

The rule updates the live Gateway immediately. Save the returned rule ID so that you can update or delete the rule later. The rule is not part of the project, and `agentcore deploy` does not manage it. To change an existing production rule instead, use `aws bedrock-agentcore-control update-gateway-rule --gateway-identifier <gateway-id> --rule-id <rule-id>`. For more rule examples, see [Gateway rules API examples](gateway-rules-examples.md).

After routing traffic to the winner:
+  **Delete the A/B test** to clean up resources. See [Delete an A/B test](ab-testing-manage.md#manage-ab-test-remove).
+  **Delete the Gateway rule before you remove its target or Gateway.** If you created a rule in Step 10, delete it before you run `agentcore remove` on the target or the Gateway. To find the rule ID, run `agentcore gateway rule list --gateway-id <gateway-id>`. Then run `aws bedrock-agentcore-control delete-gateway-rule --gateway-identifier <gateway-id> --rule-id <rule-id>`. See [Route traffic to the winning variant](ab-testing-manage.md#manage-ab-test-promote).
+  **Monitor the new baseline.** Online evaluation continues scoring sessions on the winning configuration. Watch for regressions.
+  **Start the next iteration.** New traces from the winning configuration provide the foundation for the next recommendation cycle. See [How it works](optimization-how-it-works.md).

## Understanding results
<a name="target-based-results-shape"></a>

When you call `GetABTest`, the response includes a `results` object once the aggregation pipeline has processed enough sessions. The results contain per-evaluator metrics broken down by variant.

### Results structure
<a name="_results_structure"></a>

```
{
  "results": {
    "analysisTimestamp": "2026-04-30T18:45:00Z",
    "evaluatorMetrics": [
      {
        "evaluatorArn": "arn:aws:bedrock-agentcore:::evaluator/Builtin.Helpfulness",
        "controlStats": {
          "variantName": "C",
          "sampleSize": 24,
          "mean": 0.72
        },
        "variantResults": [
          {
            "variantName": "T1",
            "sampleSize": 6,
            "mean": 0.85,
            "absoluteChange": 0.13,
            "percentChange": 18.1,
            "pValue": 0.032,
            "confidenceInterval": {
              "lower": 0.02,
              "upper": 0.24
            },
            "isSignificant": true
          }
        ]
      }
    ]
  }
}
```

### Field reference
<a name="_field_reference"></a>


| Field | Description | 
| --- | --- | 
|  `analysisTimestamp`  | When the service last computed statistics. | 
|  `evaluatorMetrics`  | One entry per evaluator in the online evaluation config. | 
|  `controlStats.mean`  | Average evaluator score across all control sessions. | 
|  `controlStats.sampleSize`  | Number of scored sessions for the control variant. | 
|  `variantResults[].mean`  | Average evaluator score across all treatment sessions. | 
|  `variantResults[].sampleSize`  | Number of scored sessions for the treatment variant. | 
|  `variantResults[].absoluteChange`  | Difference between treatment mean and control mean. | 
|  `variantResults[].percentChange`  | Percent improvement (positive) or regression (negative) relative to control. | 
|  `variantResults[].pValue`  | Probability the observed difference is due to chance. Below 0.05 indicates statistical significance. | 
|  `variantResults[].confidenceInterval`  | 95% confidence interval for the absolute change (`lower` and `upper` bounds). | 
|  `variantResults[].isSignificant`  |  `true` when p-value < 0.05 and sample sizes are sufficient. | 

## Troubleshooting
<a name="target-based-troubleshooting"></a>

### A/B test shows no results after sending traffic
<a name="target-based-no-results"></a>

Results do not appear immediately. The time it takes depends on the session timeout configured in your online evaluation config — a session is considered complete only after no new requests arrive within the timeout window. After a session ends, expect results within approximately 15 minutes.

If results still do not appear after this window:
+  **Verify the online eval log group.** The online evaluation configuration must point to the runtime agent’s output log group. If the online eval config references a different log group (or one that does not receive spans from your runtime), sessions will not be scored and the A/B test will never produce results.
+  **Check the log group name.** For target-based routing, each endpoint has its own log group (the log group name ends with the endpoint name). Ensure each online eval config references the correct endpoint’s log group.
+  **Confirm the runtime is emitting spans.** Check CloudWatch Logs for the expected log group. The key attributes you’re looking for on each span:
  +  `aws.agentcore.gateway.routing_experiment_arn` 
  +  `aws.agentcore.gateway.routing_experiment_variant_name` (values: `C` or `T1`)
  +  `session.id` 
+  **Check configurations that you created with the API.** If you used `agentcore eval online-eval create --agent <runtime-id> --endpoint <qualifier>`, the CLI configures the correct log group. If you created the online evaluation configuration with the API, make sure `dataSourceConfig.cloudWatchLogs.logGroupNames` matches the span log group of your Runtime.