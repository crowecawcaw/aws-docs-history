

# Preparing your agent
<a name="model-customize-mtrl-agent"></a>

Before you can launch a training job, you need to set up an agent that can participate in the training loop. This section walks you through how to configure and deploy your agent, whether you are using Amazon Bedrock AgentCore for managed hosting or bringing your own infrastructure with a custom agent.

## Agent code integration overview
<a name="model-customize-mtrl-agent-overview"></a>

During training, SageMaker AI sends prompts from your training dataset to your agent. Your agent processes each prompt, calls the policy model for a response, and takes actions in your environment such as calling tools. The policy model is the model being trained. It starts as your base model and its weights are updated over time as it receives feedback through the training loop. Based on the outcome, your agent reports a reward back to SageMaker AI to complete the training loop. This repeats for all prompts in your dataset, and the policy model improves over time based on the rewards collected.

## SageMaker AI Job Runtime Service
<a name="model-customize-mtrl-agent-runtime-service"></a>

During training, your agent communicates with the SageMaker AI Job Runtime Service to call the policy model for inference and report results back to the trainer. The SDK decorator handles this integration automatically, but if your agent has custom requirements, you can call the Runtime APIs directly.

**Endpoint**

`https://job-runtime.sagemaker.{{region}}.api.aws`

**APIs**


| API | Purpose | When to call | 
| --- | --- | --- | 
| Sample | Call the policy model for a single inference response | Each turn where your agent needs model output | 
| SampleWithResponseStream | Call the policy model with streaming response (SSE) | Same as Sample, when you need token-by-token streaming | 
| CompleteRollout | Signal that the rollout is finished | After your agent completes all turns for a prompt | 
| UpdateReward | Report the reward score for the complete rollout | After computing reward, typically called with CompleteRollout | 

**Note**  
Both `Sample` and `SampleWithResponseStream` are OpenAI-compatible APIs.

**Authentication**

Your agent authenticates with the Runtime Service using bearer tokens. Generate a token using the SDK:

```
from sagemaker.core.token_generator import generate_token

token = generate_token(region="us-west-2")
```

Pass this token as the API key when calling the Runtime Service.

**Direct API integration (advanced)**

If your agent framework cannot use the SDK decorator, call the APIs directly:

```
import requests
import openai
from sagemaker.core.token_generator import generate_token
from sagemaker.train.rft.headers import make_inference_headers

token = generate_token(region="us-west-2")
endpoint = "https://job-runtime.sagemaker.us-west-2.api.aws"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    **make_inference_headers(metadata),  # injects jobArn, rolloutId tracking
}

# Sample (inference call)

# Option 1: Create OpenAI-compatible client pointing to the Runtime Service (recommended)
client = openai.OpenAI(
    base_url=endpoint + "/v1",
    api_key=token,
    default_headers=headers,
)

# Option 2: direct request call
response = requests.post(
    f"{endpoint}/v1/chat/completions",
    headers=headers,
    json={
        "model": "default",
        "messages": [{"role": "user", "content": "..."}],
        "max_tokens": 256,
        "temperature": 1.0,
    }
)

# CompleteRollout + UpdateReward (after all turns complete)
# The decorator handles this; for direct calls, use the SDK's
# RolloutFeedbackClient or call the APIs per the Smithy model.
```

## Agent deployment options
<a name="model-customize-mtrl-agent-options"></a>

SageMaker AI supports two options for connecting your agent to the training loop:
+ **Bedrock AgentCore:** Deploy your agent to Amazon Bedrock AgentCore for fully managed hosting. SageMaker AI calls your agent directly during training with no additional infrastructure setup required. This option works best for agents built with the Strands SDK.
+ **Bring your own agent:** Host your agent in any environment, including Amazon EKS, Amazon EC2, or your own infrastructure, and connect it to the training loop through a Lambda forwarder. The Lambda forwarder is a Lambda function that acts as a bridge between SageMaker AI and your agent, giving SageMaker AI a consistent way to reach your agent without requiring direct access to your infrastructure or credentials. This option is a good fit when you want full control over your hosting environment or want to use an agent framework of your choice.

## Scenario 1: Agents on Bedrock AgentCore Runtime
<a name="model-customize-mtrl-agent-agentcore"></a>

Deploy your agent to Amazon Bedrock AgentCore for fully managed hosting. SageMaker AI invokes your agent during the model training.

### Prerequisites
<a name="model-customize-mtrl-agent-agentcore-prereqs"></a>

Before you begin, complete the following prerequisites.

**Bedrock AgentCore execution role**

During training, SageMaker AI assumes your SageMaker execution role to invoke your agent. Your agent also needs its own separate role, called the Bedrock AgentCore execution role, to call the RFT Runtime for model inference and reward reporting. The RFT Runtime is the SageMaker AI service endpoint your agent communicates with during training. It handles two things: serving responses from the policy model during inference, and receiving the reward your agent reports at the end of each rollout.

Create the Bedrock AgentCore execution role with the following trust policy. This policy grants Bedrock AgentCore permission to assume the role on your behalf during training. Without it, Bedrock AgentCore cannot access your container image or call the RFT Runtime.

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {"Service": "bedrock-agentcore.amazonaws.com"},
        "Action": "sts:AssumeRole"
    }]
}
```

Then attach the **AmazonSageMakerJobRuntimeAccess** managed policy to this role. This grants the permissions your agent needs to call the policy model for inference and report results during training.

### Write or update your agent code
<a name="model-customize-mtrl-agent-agentcore-code"></a>

Your agent must use the [`sagemaker-train`](https://github.com/aws/sagemaker-python-sdk/tree/master/sagemaker-train) SDK and apply the `@sagemaker_rft_handler` decorator to your agent's entry point function. This decorator sets up the HTTP server that AgentCore invokes during training, listening for incoming rollout requests and routing prompts to your entrypoint function.

**Install the SDK**

Install the SDK in your agent's environment using one of the following methods.

Option 1: Direct install

```
pip install sagemaker-train
```

Option 2: Build and install wheels individually. Use this if the direct install exceeds your environment's size constraints.

```
# Clone the SDK repository
git clone https://github.com/aws/sagemaker-python-sdk.git

# Build the wheels
cd sagemaker-python-sdk/sagemaker-train
python -m build --wheel --outdir ./dist/

cd sagemaker-python-sdk/sagemaker-core
python -m build --wheel --outdir ./dist/

# Install
pip install ./sagemaker-train/dist/sagemaker_train-*.whl
pip install ./sagemaker-core/dist/sagemaker_core-*.whl
```

**Authentication**

Your agent authenticates with SageMaker AI using bearer tokens. Generate a token using the SDK's `generate_token()` method and pass it as the API key when calling the policy model for inference.

**Agent requirements**

Your agent must do the following for each rollout:
+ Receive a rollout request containing a prompt
+ Call the policy model for a response
+ Execute actions in your environment such as tool calls or API requests
+ Repeat the previous two steps for multiple turns until the task is complete
+ Return a reward score

The following example shows a basic agent template using the Strands SDK:

```
from sagemaker.train.rft import sagemaker_rft_handler, RolloutFeedbackClient
from sagemaker.train.rft.adapters.strands import wrap_model
from sagemaker.core.token_generator import generate_token
from strands import Agent, OpenAIModel
import os

@sagemaker_rft_handler
def handle_rollout(payload):
    metadata = payload.get("metadata", {})
    prompt = payload.get("prompt", "")
    endpoint = metadata.get("endpoint", os.environ.get("RFT_RUNTIME_ENDPOINT", ""))

    # Generate bearer token for authenticating with the RFT Runtime
    token = generate_token(region=os.environ.get("AWS_REGION", "us-west-2"))

    # Create client for model inference
    model = OpenAIModel(
        model_id="default",
        client_args={
            "api_key": token,
            "base_url": endpoint + "/v1",
        },
    )

    # Wrap model to auto-inject RFT tracking headers and inference parameters
    model = wrap_model(model)

    # Execute actions in your environment (tools, APIs, etc.)
    agent = Agent(model=model, tools=[..., ...])
    result = agent(prompt)

    # Return reward -   decorator handles CompleteRollout + UpdateReward
    return {"reward": compute_reward(result)}
```

### Deploy your agent to Bedrock AgentCore
<a name="model-customize-mtrl-agent-agentcore-deploy"></a>

Deploy your agent to Amazon Bedrock AgentCore following the AgentCore development guide.

Once you have deployed your agent using the AgentCore CLI, note the Agent Runtime ARN from the output. You need this when creating your training job. The Runtime ARN follows the format of `arn:aws:bedrock-agentcore:<region>:<account-id>:runtime/<agent-name>`.

Verify your agent is deployed and healthy:

```
aws bedrock-agentcore-control list-agent-runtimes --region us-west-2
```

## Scenario 2: Custom Agent with Lambda Forwarder
<a name="model-customize-mtrl-agent-custom"></a>

In addition to Bedrock AgentCore, SageMaker AI supports custom agents hosted in any environment. Your agent connects to the training loop through a Lambda forwarder, giving you the flexibility to use any agent framework and hosting platform of your choice.

Your agent can be built using any framework or platform, such as Strands Agents SDK, or your own custom implementation. It can run on any compute environment including Amazon Bedrock AgentCore, Amazon EKS, Amazon EC2, AWS Fargate, or your own infrastructure.

The Lambda function receives rollout requests from SageMaker AI and forwards them to your agent's HTTP endpoint.

The following sections provide more information about setting up a custom agent with a Lambda forwarder, with examples using a custom agent deployed on Amazon EKS.

### Prerequisites
<a name="model-customize-mtrl-agent-custom-prereqs"></a>

**Lambda execution role**

During training, SageMaker AI assumes your SageMaker execution role to invoke your Lambda forwarder. The Lambda function requires its own execution role so that AWS Lambda can run it. This role allows Lambda to run and write logs.

```
aws iam create-role \
  --role-name RFTLambdaForwarderRole \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "lambda.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

aws iam attach-role-policy \
  --role-name RFTLambdaForwarderRole \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

### Write your agent code
<a name="model-customize-mtrl-agent-custom-code"></a>

Your agent must expose an HTTP endpoint that accepts rollout requests and interacts with the RFT Runtime service, by calling it for model inference and reporting the rewards once the task is complete.

**Rollout request format**

Your agent receives requests in the following format from the Lambda forwarder:

```
{
    "prompt": "string",
    "metadata": {
        "jobArn": "string",
        "rolloutId": "string"
    },
    "inferenceParams": {
        "temperature": 1.0,
        "topP": 1.0,
        "maxTokens": 256
    }
}
```

**Agent expectations**

For Amazon SageMaker AI to successfully complete rollouts, your agent must:
+ Accept rollout requests from the Lambda forwarder
+ Call the RFT Runtime for model inference using the provided headers and token
+ Execute actions in your environment (tools, APIs, etc.)
+ Support multiple inference calls per rollout (multi-turn)
+ Report the trajectory as complete when the task is finished
+ Submit a reward score to the RFT Runtime

The following example shows a custom agent with a FastAPI endpoint:

```
"""
Custom Lambda Agent for SageMaker RFT.

This is a minimal example showing the required integration points.
You can use any framework (Strands, LangChain, raw OpenAI, etc.)
or any HTTP framework (FastAPI, Flask, Django, etc.) for your agent.
"""
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict
from sagemaker.train.rft import sagemaker_rft_handler, set_rollout_context
from sagemaker.train.rft.headers import make_inference_headers
from sagemaker.core.token_generator import generate_token

app = FastAPI()

@app.post("/rollout")
def rollout_endpoint(payload: dict):
    handle_rollout(payload)
    return {"status": "accepted"}

@sagemaker_rft_handler
def handle_rollout(payload):
    """Handle a rollout request from RFT."""
    prompt = payload.get("prompt", "")
    metadata = payload.get("metadata", {})
    inference_params = payload.get("inferenceParams", {})
    endpoint = metadata.get("endpoint", os.environ.get("RFT_RUNTIME_ENDPOINT", ""))

    # 1. Set rollout context and capture inference headers
    set_rollout_context(metadata)
    headers = make_inference_headers(metadata)

    # 2. Get bearer token for RFT Runtime authentication
    token = generate_token(region=os.environ.get("AWS_REGION", "us-west-2"))

    # 3. Run your agent logic
    result = run_agent(prompt, token, endpoint, inference_params, headers)

    # 4. Compute reward based on your task's success criteria
    reward = compute_reward(result)

    # 5. Report completion with reward to RFT Runtime
    # decorator handles CompleteRollout + UpdateReward
    return {"reward": reward}

def run_agent(prompt: str, token: str, endpoint: str, inference_params: dict, headers: dict) -> str:
    """Your agent logic goes here."""
    import openai
    client = openai.OpenAI(
        base_url=(endpoint or os.environ.get("RFT_RUNTIME_ENDPOINT", "")) + "/v1",
        api_key=token,
        default_headers=headers,
    )

    response = client.chat.completions.create(
        model="default",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=inference_params.get("maxTokens", 256),
        temperature=inference_params.get("temperature", 1.0),
        top_p=inference_params.get("topP", 1.0),
    )

    return response.choices[0].message.content

def compute_reward(result: str) -> float:
    """Implement your task-specific reward function here."""

@app.get("/health")
def health():
    return {"status": "ok"}
```

Install the required dependencies in your agent environment:

```
pip install sagemaker-train fastapi uvicorn openai
```

### Deploy your agent
<a name="model-customize-mtrl-agent-custom-deploy"></a>

Your agent can run on any compute environment. It needs outbound network access to reach the SageMaker AI Runtime for inference and reward reporting. If the Lambda forwarder calls your agent directly, your agent must also expose an HTTP endpoint reachable from Lambda.

The following steps deploy a custom agent to Amazon EKS.

**Create an EKS cluster**

For full EKS setup instructions, see the EKS Getting Started guide. The following is a minimal setup for this example:

```
eksctl create cluster \
  --name external-agent \
  --region us-west-2 \
  --nodegroup-name agent-nodes \
  --node-type t3.medium \
  --nodes 1 \
  --nodes-min 1 \
  --nodes-max 2 \
  --managed
```

Update your kubeconfig to connect to the cluster:

```
aws eks update-kubeconfig --name external-agent --region us-west-2
```

Build and push your container image:

```
aws ecr create-repository --repository-name my-external-agent --region us-west-2

aws ecr get-login-password --region us-west-2 | \
  docker login --username AWS --password-stdin account-id.dkr.ecr.us-west-2.amazonaws.com

docker build -t my-external-agent .
docker tag my-external-agent:latest account-id.dkr.ecr.us-west-2.amazonaws.com/my-external-agent:latest
docker push account-id.dkr.ecr.us-west-2.amazonaws.com/my-external-agent:latest
```

Deploy to EKS:

```
kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: external-agent
spec:
  replicas: 1
  selector:
    matchLabels:
      app: external-agent
  template:
    metadata:
      labels:
        app: external-agent
    spec:
      containers:
      - name: agent
        image: <account-id>.dkr.ecr.us-west-2.amazonaws.com/external-agent:latest
        ports:
        - containerPort: 8080
        env:
        - name: AWS_REGION
          value: us-west-2
        - name: RFT_RUNTIME_ENDPOINT
          value: https://job-runtime.sagemaker.us-west-2.api.aws
---
apiVersion: v1
kind: Service
metadata:
  name: external-agent
spec:
  selector:
    app: external-agent
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
EOF
```

Get your agent endpoint:

```
AGENT_ENDPOINT=$(kubectl get svc external-agent -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')

echo "Agent endpoint: http://$AGENT_ENDPOINT"
```

Verify the deployment:

```
curl -s "http://$AGENT_ENDPOINT/health"

# Expected: {"status": "ok"}
```

### Create your Lambda forwarder
<a name="model-customize-mtrl-agent-custom-lambda"></a>

The Lambda forwarder receives rollout requests from SageMaker AI and forwards them to your agent. The main thing to customize is the `_call_agent()` function, which translates the rollout request into your agent's API format.

If your agent doesn't have a public HTTP endpoint, you can replace the HTTP call in `_call_agent()` with an SQS `send_message` and have your agent poll the queue instead.

```
"""
Lambda Template

Bridges SageMaker Job rollout requests to any agent platform with a public endpoint.
Implement _call_agent() with your platform-specific logic.

If your agent environment does not have a public endpoint, you can
replace the HTTP call with an SQS send_message to enqueue the request,
and have your agent poll the queue for work.

Env vars:
    AGENT_ENDPOINT  - target agent base URL
    AGENT_API_KEY   - API key for the target agent (prefer Secrets Manager)
"""

import json
import logging
import os
import re
import urllib.error
import urllib.request

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

AGENT_ENDPOINT = os.environ.get("AGENT_ENDPOINT", "")
AGENT_API_KEY = os.environ.get("AGENT_API_KEY", "")

_SAFE_ID = re.compile(r"^[\w\-.]+$")

# ---------------------------------------------------------------------------
# CUSTOMIZE THIS - translate rollout request to your platform's API
# ---------------------------------------------------------------------------
def _call_agent(prompt: str, metadata: dict, inference_params: dict):
    """
    Forward the prompt to your agent platform.
    Replace the body below with your platform's request format.
    """
    payload = json.dumps({
        "prompt": prompt,
        "metadata": metadata,
        "inferenceParams": inference_params,
    }).encode()

    req = urllib.request.Request(
        AGENT_ENDPOINT,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AGENT_API_KEY}",
        },
        method="POST",
    )

    urllib.request.urlopen(req, timeout=120)


# ---------------------------------------------------------------------------
# Validation - no changes needed below
# ---------------------------------------------------------------------------
def _validate(event: dict) -> dict:
    body = json.loads(event["body"]) if isinstance(event.get("body"), str) else event

    prompt = body.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("'prompt' is required and must be a non-empty string")

    meta = body.get("metadata")
    if not isinstance(meta, dict):
        raise ValueError("'metadata' is required")
    for key in ("jobArn", "rolloutId"):
        val = meta.get(key)
        if not isinstance(val, str) or not val.strip():
            raise ValueError(f"metadata.{key} must match [a-zA-Z0-9_\\-.]")

    params = body.get("inferenceParams") or {}
    if not isinstance(params, dict):
        raise ValueError("'inferenceParams' must be an object")

    return {
        "prompt": prompt.strip(),
        "metadata": meta,
        "inferenceParams": params,
    }


# ---------------------------------------------------------------------------
# CUSTOMIZE THIS - handle errors thrown from your agent environment
# ---------------------------------------------------------------------------
def _handle_agent_error(exc: Exception) -> dict:
    """
    Called when _call_agent() raises an exception. Customize this to map
    platform-specific errors to appropriate error types and messages.

    The return payload must follow this structure:
        {"errorType": "<type>", "errorMessage": "<description>"}

    Supported errorType values:
        ValidationError, InternalServerError, AccessDenied

    Examples:
          return {"errorType": "AccessDenied","errorMessage": "Agent denied access"}
          return {"errorType": "ValidationError","errorMessage": "Missing required field"}
          return {"errorType":"InternalServerError", "errorMessage": str(exc)}
    """

def handler(event, context):
    try:
        body = _validate(event)
    except ValueError as exc:
        logger.warning("Validation error: %s", exc)
        return {"errorType": "ValidationError", "errorMessage": str(exc)}

    try:
        result = _call_agent(body["prompt"], body["metadata"], body["inferenceParams"])
        logger.info("Rollout %s completed", body["metadata"]["rolloutId"])
        return {}
    except Exception as exc:
        return _handle_agent_error(exc)
```

**Deploy the Lambda function:**

Package the Lambda function:

```
zip lambda_forwarder.zip lambda_forwarder.py
```

Create the function:

```
aws lambda create-function \
  --function-name rft-agent-forwarder \
  --runtime python3.12 \
  --handler lambda_forwarder.handler \
  --role arn:aws:iam::account-id:role/RFTLambdaForwarderRole \
  --zip-file fileb://lambda_forwarder.zip \
  --timeout 600 \
  --environment "Variables={AGENT_ENDPOINT=http://$AGENT_ENDPOINT}" \
  --region us-west-2
```

Test the Lambda:

```
aws lambda invoke \
  --function-name rft-agent-forwarder \
  --cli-binary-format raw-in-base64-out \
  --payload '{"prompt": "Plan a 3-day itinerary for a trip to Seattle", "metadata": {"jobArn": "arn:aws:sagemaker:us-west-2:123456789012:job/AgentRFT/test", "rolloutId": "roll-1"}}' \
  --region us-west-2 \
  /tmp/response.json && cat /tmp/response.json
```

**Note**  
This test confirms that Lambda is deployed and can reach your agent. The rollout won't complete successfully because no active training job exists, so an error response is expected. Check your agent's logs to confirm it received the request.