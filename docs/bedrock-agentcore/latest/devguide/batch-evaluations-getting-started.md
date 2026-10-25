

# Getting started with batch evaluation
<a name="batch-evaluations-getting-started"></a>

This walkthrough takes you from a deployed agent to batch evaluation results using an Acme Store customer support agent. You will create the agent, deploy it, generate sample sessions, run a batch evaluation, and read the results.

**Topics**
+ [Before you begin](#batch-gs-before-you-begin)
+ [Step 1: Create and deploy the sample agent](#batch-gs-step1)
+ [Step 2: Generate sample sessions](#batch-gs-step2)
+ [Step 3: Run batch evaluation](#batch-gs-step3)
+ [Step 4: Read per-session detail](#batch-gs-step4)
+ [Next steps](#batch-gs-next-steps)

## Before you begin
<a name="batch-gs-before-you-begin"></a>

Make sure you have:
+ The AgentCore CLI installed (`agentcore --version`)
+  AWS credentials with permissions for `bedrock-agentcore` and `logs` 
+ Transaction Search enabled in CloudWatch
+ Python 3.10\+ (for boto3 examples)

For full details, see [Prerequisites](batch-evaluations-prereqs.md).

The following constants are used in the boto3 examples. Replace them with your own values after deploying the agent:

```
REGION       = "us-west-2"
AGENT_ARN    = "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/AcmeSupport_default_agent-abc123"
SERVICE_NAME = "AcmeSupport_default_agent.DEFAULT"
LOG_GROUP    = "/aws/bedrock-agentcore/runtimes/AcmeSupport_default_agent-abc123-DEFAULT"
```

## Step 1: Create and deploy the sample agent
<a name="batch-gs-step1"></a>

Create an AgentCore project and replace the default agent code with the Acme Store customer support agent. This agent has five tools for handling orders, returns, shipping, discounts, and escalations.

### Create the project
<a name="batch-gs-step1a"></a>

```
agentcore create --name AcmeSupport --template agent-python-strands
cd AcmeSupport
agentcore remove memory --name agentMemory
```

### Replace the agent code
<a name="batch-gs-step1b"></a>

Open `app/agent/main.py` and replace its contents with the following:

```
"""Acme Store customer support agent."""
from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()
MODEL_ID = "global.anthropic.claude-sonnet-4-6"
SYSTEM_PROMPT = (
    "You are a helpful customer support assistant for Acme Store. "
    "Help customers with their orders, returns, and shipping questions."
)


@tool
def lookup_order(order_id: str) -> str:
    """Look up an order by ID and return its status, item, and delivery details."""
    orders = {
        "ORD-1001": {
            "status": "delivered",
            "item": "Blue T-Shirt (L)",
            "delivered": "2026-03-28",
            "total": "$29.99",
        },
        "ORD-1002": {
            "status": "in_transit",
            "item": "Running Shoes (10)",
            "shipped": "2026-03-30",
            "est_delivery": "2026-04-05",
            "total": "$89.99",
        },
        "ORD-1003": {
            "status": "delayed",
            "item": "Wireless Headphones",
            "shipped": "2026-03-25",
            "est_delivery": "2026-03-29",
            "days_late": 5,
            "total": "$59.99",
        },
        "ORD-1004": {
            "status": "processing",
            "item": "Yoga Mat",
            "ordered": "2026-04-02",
            "total": "$34.99",
        },
        "ORD-1005": {
            "status": "delivered",
            "item": "Coffee Maker",
            "delivered": "2026-03-20",
            "total": "$149.99",
        },
    }
    return str(orders.get(order_id, {"error": f"Order {order_id} not found"}))


@tool
def initiate_return(order_id: str, reason: str) -> str:
    """Initiate a return for an order. Sends a return label to the customer."""
    return (
        f"Return initiated for {order_id}. Reason: {reason}. "
        "Return label sent to customer email. Please ship within 14 days."
    )


@tool
def check_shipping_status(order_id: str) -> str:
    """Check detailed shipping status including carrier location and delays."""
    statuses = {
        "ORD-1002": (
            "Package is with carrier, currently in Portland OR. "
            "On schedule for April 5."
        ),
        "ORD-1003": (
            "Package delayed at distribution center in Memphis TN. "
            "Original delivery was March 29. Now 5 days late. "
            "Acme Store policy: orders delayed 3+ days qualify for 15% discount."
        ),
    }
    return statuses.get(order_id, f"No active shipment found for {order_id}.")


@tool
def apply_discount(order_id: str, discount_percent: int, reason: str) -> str:
    """Apply a percentage discount to an order and issue a refund."""
    return (
        f"Applied {discount_percent}% discount to {order_id}. "
        f"Reason: {reason}. Refund will appear in 3-5 business days."
    )


@tool
def escalate_to_human(reason: str) -> str:
    """Escalate the conversation to a human support agent."""
    return (
        f"Escalated to human agent. Reason: {reason}. "
        "Estimated wait time: 3 minutes."
    )


agent = Agent(
    model=BedrockModel(model_id=MODEL_ID),
    tools=[lookup_order, initiate_return, check_shipping_status,
           apply_discount, escalate_to_human],
    system_prompt=SYSTEM_PROMPT,
)


@app.entrypoint
def invoke(payload, context):
    result = agent(str(payload.get("prompt", "Hello")))
    return {"response": str(result)}


if __name__ == "__main__":
    app.run()
```

### Deploy and verify
<a name="batch-gs-step1c"></a>

```
agentcore deploy
```

After deployment, verify the agent is running:

```
agentcore invoke --runtime agent \
  --payload '{"prompt":"What is the status of order ORD-1001?"}'
```

You should see a response with the order details. Run `agentcore status --json` and note the Runtime ARN. The Runtime ID is the last segment of the ARN.

**Note**  
If you already have an agent deployed on AgentCore Runtime with observability enabled, skip this step and use your own agent for the rest of the walkthrough.

## Step 2: Generate sample sessions
<a name="batch-gs-step2"></a>

Invoke the agent with varied prompts to create sessions for evaluation. These prompts cover different scenarios: order lookups, returns, shipping delays, discount requests, and multi-tool interactions.

**Example**  

```
agentcore invoke --runtime agent --payload '{"prompt":"What is the status of my order ORD-1001?"}'
agentcore invoke --runtime agent --payload '{"prompt":"I need to return order ORD-1001, the shirt does not fit."}'
agentcore invoke --runtime agent --payload '{"prompt":"What is the shipping status on ORD-1002?"}'
agentcore invoke --runtime agent --payload '{"prompt":"My order ORD-1003 is delayed, can you help?"}'
agentcore invoke --runtime agent --payload '{"prompt":"I would like to check on order ORD-1004."}'
agentcore invoke --runtime agent --payload '{"prompt":"Can you look up order ORD-1005 for me?"}'
agentcore invoke --runtime agent --payload '{"prompt":"I want to return the coffee maker from order ORD-1005; it is defective."}'
agentcore invoke --runtime agent --payload '{"prompt":"Where is my order ORD-1002? It should have arrived by now."}'
agentcore invoke --runtime agent --payload '{"prompt":"ORD-1003 is really late; I want a discount."}'
agentcore invoke --runtime agent --payload '{"prompt":"Can you check order ORD-1001 and tell me when it was delivered?"}'
```

```
import boto3
import json
import uuid

client = boto3.client("bedrock-agentcore", region_name=REGION)

prompts = [
    "What's the status of my order ORD-1001?",
    "I need to return order ORD-1001, the shirt doesn't fit.",
    "What's the shipping status on ORD-1002?",
    "My order ORD-1003 is delayed, can you help?",
    "I'd like to check on order ORD-1004 please.",
    "Can you look up order ORD-1005 for me?",
    "I want to return the coffee maker from order ORD-1005, it's defective.",
    "Where is my order ORD-1002? It should have arrived by now.",
    "ORD-1003 is really late, I want a discount.",
    "Can you check order ORD-1001 and tell me when it was delivered?",
]

for i, prompt in enumerate(prompts):
    session_id = f"acme-eval-{uuid.uuid4()}"
    print(f"[{i+1}/10] {prompt[:60]}...")

    response = client.invoke_agent_runtime(
        agentRuntimeArn=AGENT_ARN,
        runtimeSessionId=session_id,
        payload=json.dumps({"prompt": prompt}).encode(),
    )
    response_body = response["response"].read()
    print(f"  Done (session: {session_id})")

print("\nAll sessions created.")
```

Wait 2–3 minutes after the last invocation for CloudWatch to ingest the telemetry before proceeding.

## Step 3: Run batch evaluation
<a name="batch-gs-step3"></a>

Start a batch evaluation to score all recent sessions. The service discovers sessions from CloudWatch Logs, runs each evaluator against each session, and returns aggregate results.

**Example**  

```
agentcore eval batch-evaluation evaluate \
  --agent <RUNTIME_ID> \
  --evaluators Builtin.GoalSuccessRate Builtin.Helpfulness Builtin.Faithfulness \
  --name acme_baseline
```
The command starts the asynchronous evaluation and returns its batch evaluation ID. Retrieve status and results with:  

```
agentcore eval batch-evaluation get --id <BATCH_EVALUATION_ID>
```

```
import boto3
import uuid
import time
import json

eval_client = boto3.client("bedrock-agentcore", region_name=REGION)

# Start the batch evaluation
response = eval_client.start_batch_evaluation(
    batchEvaluationName=f"acme_baseline_{uuid.uuid4().hex[:8]}",
    evaluators=[
        {"evaluatorId": "Builtin.GoalSuccessRate"},
        {"evaluatorId": "Builtin.Helpfulness"},
        {"evaluatorId": "Builtin.Faithfulness"},
    ],
    dataSourceConfig={
        "cloudWatchLogs": {
            "serviceNames": [SERVICE_NAME],
            "logGroupNames": [LOG_GROUP],
        }
    },
    clientToken=str(uuid.uuid4()),
)

batch_eval_id = response["batchEvaluationId"]
print(f"Started: {batch_eval_id}")

# Poll until complete
while True:
    result = eval_client.get_batch_evaluation(batchEvaluationId=batch_eval_id)
    status = result["status"]
    print(f"Status: {status}")

    if status in ("COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "STOPPED"):
        break
    time.sleep(30)

print(json.dumps(result, indent=4, default=str))
```

## Step 4: Read per-session detail
<a name="batch-gs-step4"></a>

The aggregate scores tell you the overall picture. To see per-turn, per-evaluator scores for individual sessions, use the built-in CLI viewing commands or read the evaluation events directly from CloudWatch Logs.

**Example**  
View a job and its results by its batch evaluation ID, or list jobs:  

```
# View a batch evaluation job and its results
agentcore eval batch-evaluation get --id <BATCH_EVALUATION_ID>

# List batch evaluation jobs
agentcore eval batch-evaluation list
```
Add `--json` for machine-readable output.

```
# Get the output location from the batch evaluation result
output = result["outputConfig"]["cloudWatchConfig"]
log_group = output["logGroupName"]
log_stream = output["logStreamName"]

# Read the events
logs_client = boto3.client("logs", region_name=REGION)
response = logs_client.get_log_events(
    logGroupName=log_group,
    logStreamName=log_stream,
)

for event in response["events"]:
    event_attrs = json.loads(event["message"]).get("attributes", {})
    print(f"Score: {event_attrs.get('gen_ai.evaluation.score.value')}")
    print(f"Label: {event_attrs.get('gen_ai.evaluation.score.label')}")
    print(f"Explanation: {event_attrs.get('gen_ai.evaluation.explanation', '')[:200]}")
    print()
```

## Next steps
<a name="batch-gs-next-steps"></a>
+  **Filter sessions** — Evaluate specific sessions by ID or time range. See [Start a batch evaluation](batch-evaluations-start.md).
+  **Run against a dataset** — Invoke your agent against predefined scenarios and evaluate the results automatically. See [Dataset evaluation](dataset-evaluations.md).
+  **Compare runs** — Run batch evaluation before and after a change and compare scores. See [Understanding results and output](batch-evaluations-results.md).