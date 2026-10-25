

# Run an A/B test for agents hosted outside of AgentCore
<a name="ab-testing-3p-agents"></a>

You can A/B test an agent hosted outside AgentCore Runtime, for example on AWS Lambda, Amazon EKS, or Amazon ECS. AgentCore Gateway routes traffic between variants, online evaluation scores each session, and the service computes per-variant statistical significance. Instrument the agent for observability, register it as an AgentCore Gateway target, and enable Gateway tracing so sessions can be attributed to a variant.

A/B testing supports [configuration bundles with a single agent runtime](ab-testing-config-bundle.md) and [target-based routing with two agent endpoints](ab-testing-target-based.md). This page shows how to set up an HTTP-reachable agent endpoint as an AgentCore Gateway target with tracing enabled. Gateway tracing supplies variant attribution, and observability on the agent endpoint supplies the message content for scoring.

This page is an addendum to [Run an A/B test with target-based routing](ab-testing-target-based.md). It covers only the extra setup that an agent outside AgentCore Runtime needs, and then returns you to that page to create and run the test. The example uses a Lambda-hosted agent behind a function URL. The same approach works for any HTTP-reachable agent endpoint that you register as an AgentCore Gateway target.

## Prerequisites
<a name="ab-testing-3p-prereqs"></a>

In addition to the [general A/B testing prerequisites](ab-testing-prereqs.md), you need:

1. AgentCore gateway tracing enabled on the gateway so sessions can be attributed to a variant.

1. Your agent added as a passthrough target on an AgentCore gateway using a supported protocol.

## Step 1: Instrument your agent for AgentCore observability
<a name="ab-testing-3p-step1-observability"></a>

**Note**  
Follow [Enabling observability for agents hosted outside of AgentCore](observability-configure.md#observability-configure-3p) for the full setup.

For a Lambda-hosted agent, attach the [AWS Lambda Layer for OpenTelemetry](https://aws-otel.github.io/docs/getting-started/lambda#adot-lambda-layer-arns) and set the following environment variables:

```
aws lambda update-function-configuration \
  --function-name <function-name> \
  --region <region> \
  --layers <adot-python-layer-arn> \
  --environment "Variables={
    AGENT_OBSERVABILITY_ENABLED=true,
    OTEL_PROPAGATORS='baggage,xray-lambda,tracecontext',
    OTEL_PYTHON_DISTRO=aws_distro,
    OTEL_PYTHON_CONFIGURATOR=aws_configurator,
    OTEL_LOGS_EXPORTER=otlp,
    OTEL_TRACES_EXPORTER=otlp,
    OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf,
    OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true,
    OTEL_AWS_APPLICATION_SIGNALS_ENABLED=false,
    OTEL_EXPORTER_OTLP_LOGS_HEADERS='x-aws-log-group=/aws/bedrock-agentcore/agents/<function-name>/runtime-logs,x-aws-log-stream=runtime-logs,x-aws-metric-namespace=agentcore',
    OTEL_RESOURCE_ATTRIBUTES='service.name=<function-name>',
    AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-instrument
  }"
```

A minimal Lambda handler that parses the function URL request and sets the session baggage:

```
import base64, json
from strands import Agent
from strands.models.bedrock import BedrockModel
from opentelemetry import baggage, context

_model = BedrockModel(model_id="global.anthropic.claude-sonnet-4-5-20250929-v1:0")


def lambda_handler(event, _context):
    # Lambda function URL payload format 2.0: JSON body is in event["body"], no httpMethod.
    raw = event.get("body")
    if raw is not None and event.get("isBase64Encoded"):
        raw = base64.b64decode(raw).decode()
    body = json.loads(raw) if isinstance(raw, str) else (raw or event)

    session_id = _session_id(event)
    token = context.attach(baggage.set_baggage("session.id", session_id))
    try:
        agent = Agent(model=_model, system_prompt="You are a helpful assistant. Be concise.")
        result = agent(body.get("prompt", "Hello"))
    finally:
        context.detach(token)
    return {"response": str(result), "sessionId": session_id}


def _session_id(event):
    return (event.get("headers") or {}).get("x-session-id") or "default"
```

For target-based routing, deploy this twice (control and treatment) with the change you are testing — for example, a different `model_id` or system prompt.

## Step 2: Expose your agent over HTTP
<a name="ab-testing-3p-step2-http"></a>

The agent must be reachable at an HTTP endpoint the AgentCore gateway can call. For the Lambda example, create a function URL with IAM authentication for each function:

```
aws lambda create-function-url-config \
  --function-name cs-agent-control \
  --auth-type AWS_IAM \
  --region us-west-2
```

Repeat for the treatment function. (For a container or self-hosted agent, expose an HTTPS endpoint instead and skip to Step 3.)

## Step 3: Register your agent as an AgentCore gateway target
<a name="ab-testing-3p-step3-target"></a>

Register each endpoint as an HTTP **passthrough** target on an AgentCore gateway. For the details of passthrough targets, including the `protocolType`, stickiness, and credential options, see [HTTP passthrough targets](gateway-target-http-passthrough.md).

To register a Lambda function URL as a target, set `protocolType` to `CUSTOM` and provide an `iamCredentialProvider`. The credential provider authorizes the gateway to sign each outbound request to the function URL as the `lambda` service:

**Note**  
The `stickinessConfiguration` tells the gateway to use the `x-session-id` header to recognize which requests belong to the same session. Session stickiness keeps in-flight sessions unaffected when you start or stop an A/B test: the gateway continues to route ongoing sessions to the same target they were already assigned to, and routes only new sessions according to your A/B test treatment weights while the test is running.
For observability, your agent must also set this same session ID in its trace context (for example, as `session.id` baggage). This lets online evaluation score agent sessions and traces, and attribute them to the correct A/B test treatment.

**Example**  
If you don’t have an AgentCore CLI project, create one:  

```
agentcore create --name ABTest3p --template empty
cd ABTest3p
```
In the project directory, save the following as `control-target.json`:  

```
{
  "name": "customer-support-control",
  "targetType": "passthrough",
  "passthrough": {
    "endpoint": "https://<control-id>.lambda-url.us-west-2.on.aws/",
    "protocolType": "CUSTOM",
    "stickinessConfiguration": {
      "identifier": "$.AMZN_AC_GW_CONTEXT.headers.x-session-id",
      "timeout": 28800
    }
  },
  "outboundAuth": {
    "type": "GATEWAY_IAM_ROLE",
    "service": "lambda",
    "region": "us-west-2"
  }
}
```
Add the target:  

```
agentcore add gateway --name cs-3p-abtest-gw --authorizer-type AWS_IAM

agentcore add gateway-target \
  --gateway cs-3p-abtest-gw \
  --target-configuration file://control-target.json
```

```
aws bedrock-agentcore-control create-gateway \
  --name cs-3p-abtest-gw \
  --role-arn <gateway-role-arn> \
  --authorizer-type AWS_IAM \
  --region us-west-2

aws bedrock-agentcore-control create-gateway-target \
  --gateway-identifier <gateway-id> \
  --name customer-support-control \
  --region us-west-2 \
  --target-configuration '{
    "http": {
      "passthrough": {
        "endpoint": "https://<control-id>.lambda-url.us-west-2.on.aws/",
        "protocolType": "CUSTOM",
        "stickinessConfiguration": {
          "identifier": "$.AMZN_AC_GW_CONTEXT.headers.x-session-id",
          "timeout": 28800
        }
      }
    }
  }' \
  --credential-provider-configurations '[
    {
      "credentialProviderType": "GATEWAY_IAM_ROLE",
      "credentialProvider": {
        "iamCredentialProvider": { "service": "lambda", "region": "us-west-2" }
      }
    }
  ]'
```

For the AgentCore CLI workflow, create `treatment-target.json` with the treatment name and function URL, then add it with the same command:

```
agentcore add gateway-target \
  --gateway cs-3p-abtest-gw \
  --target-configuration file://treatment-target.json
```

The AgentCore CLI creates the Gateway’s execution role. To let the Gateway call both function URLs, grant the role access in `agentcore/cdk/lib/cdk-stack.ts`. Add `aws_lambda` to the `aws-cdk-lib` import:

```
import { Stack, type StackProps, aws_lambda as lambda } from 'aws-cdk-lib';
```

Then add the grants after the line that creates the `AgentCoreApplication`:

```
const gateway = this.application.gateway('cs-3p-abtest-gw');
for (const functionName of ['cs-agent-control', 'cs-agent-treatment']) {
  lambda.Function.fromFunctionName(this, functionName, functionName).grantInvokeUrl(gateway);
}
```

 `grantInvokeUrl` adds `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction` on each function to the Gateway role, and allows `lambda:InvokeFunction` only for calls made through the function URL. The functions must be in the account and Region that the project deploys to. The deployment creates the targets after the grants are in place.

Deploy the project and run `agentcore status --json`. Read the `arn` field for `cs-3p-abtest-gw`. The Gateway ID is the last segment of that ARN.

```
agentcore deploy

agentcore status --json
```

The `status` output does not report target state. To wait until both targets report `READY`, list the targets with `agentcore gateway target list`.

```
agentcore gateway target list --gateway-id <gateway-id> --json
```

For the AWS CLI workflow, repeat `aws bedrock-agentcore-control create-gateway-target` for the treatment endpoint and name it `customer-support-treatment`. No project deployment is required. Use the Gateway ID returned by `create-gateway`, and poll each target with `get-gateway-target` until `status` is `READY`.

In the AWS CLI workflow, the role that you pass to `create-gateway` must trust the Gateway service, as described in [Trust permissions](gateway-prerequisites-permissions.md#gateway-service-role-permissions-trust). The role must also allow the Gateway to call both function URLs. The following policy grants the same permissions that `grantInvokeUrl` adds in the AgentCore CLI workflow. Replace `123456789012` with your account ID:

```
{
"Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "lambda:InvokeFunctionUrl",
      "Resource": [
        "arn:aws:lambda:us-west-2:123456789012:function:cs-agent-control",
        "arn:aws:lambda:us-west-2:123456789012:function:cs-agent-treatment"
      ],
      "Condition": {
        "StringEquals": {
          "lambda:FunctionUrlAuthType": "AWS_IAM"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "lambda:InvokeFunction",
      "Resource": [
        "arn:aws:lambda:us-west-2:123456789012:function:cs-agent-control",
        "arn:aws:lambda:us-west-2:123456789012:function:cs-agent-treatment"
      ],
      "Condition": {
        "Bool": {
          "lambda:InvokedViaFunctionUrl": true
        }
      }
    }
  ]
}
```

**Note**  
 `iamCredentialProvider` is required for an IAM-authenticated passthrough target. For a Lambda function URL, set `service` to `lambda`.

## Step 4: Enable AgentCore gateway tracing
<a name="ab-testing-3p-step4-gateway-tracing"></a>

Enable tracing delivery on the AgentCore gateway so that it emits variant-attribution spans to `aws/spans`. To enable tracing from the console, open the gateway detail page and choose **Log deliveries and tracing** → **Tracing** → **Enable**. For more information, see [Configure tracing delivery to CloudWatch](observability-configure.md#observability-configure-tracing).

Once traffic begins to flow, each gateway span carries the `aws.agentcore.gateway.routing_experiment_arn` and `aws.agentcore.gateway.routing_experiment_variant_name` (for example, `C` or `T1`) attributes, along with the `traceId` of the request. The online evaluation pipeline joins the gateway span to your agent’s spans by `traceId`, which is how each scored session is attributed to its variant. Without gateway tracing, sessions are still scored, but they cannot be attributed to a variant, and the A/B test does not produce per-variant results.

## Step 5: Create and run the A/B test
<a name="ab-testing-3p-step5-run"></a>

Your agent is now a gateway target emitting telemetry. Two steps remain:

1.  **Create one online evaluation configuration per variant endpoint.** See [Create online evaluation](create-online-evaluations.md). For each config, use the `service.name` and event log group you configured in [Step 1: Instrument your agent for AgentCore observability](#ab-testing-3p-step1-observability).

1.  **Create and run the A/B test.** Follow [Run an A/B test with target-based routing](ab-testing-target-based.md), starting from the **Create the A/B test** step. Create the test with `perVariantOnlineEvaluationConfig`, send traffic with the script in [Send traffic](#ab-testing-3p-send-traffic), poll results, stop the test, and route traffic to the winner.

When you send traffic through the gateway, direct it to the control variant’s target. The gateway splits all traffic arriving at the control target across the control (`C`) and treatment (`T1`) targets according to your A/B test configuration.

**Example**  
Add one online evaluation config per variant — using the `service.name` and event log group from [Step 1: Instrument your agent for AgentCore observability](#ab-testing-3p-step1-observability) as the data source — then start the test in `target-based` mode:  

```
agentcore eval online-eval create \
  --name cs_control_eval \
  --data-source-config '{"cloudWatchLogs":{"serviceNames":["cs-agent-control"],"logGroupNames":["/aws/bedrock-agentcore/agents/cs-agent-control/runtime-logs"]}}' \
  --evaluators Builtin.Correctness \
  --sampling-rate 100 \
  --enable-on-create true \
  --json

agentcore eval online-eval create \
  --name cs_treatment_eval \
  --data-source-config '{"cloudWatchLogs":{"serviceNames":["cs-agent-treatment"],"logGroupNames":["/aws/bedrock-agentcore/agents/cs-agent-treatment/runtime-logs"]}}' \
  --evaluators Builtin.Correctness \
  --sampling-rate 100 \
  --enable-on-create true \
  --json

agentcore eval ab-test target-based run \
  --name cs_3p_abtest \
  --gateway <gateway-id> \
  --control '{"gateway-target":"customer-support-control","online-eval":"<control-online-evaluation-config-id>"}' \
  --treatment '{"gateway-target":"customer-support-treatment","online-eval":"<treatment-online-evaluation-config-id>"}' \
  --treatment-weight 50 \
  --gateway-filter '{"targetPaths":["/customer-support-control/*"]}'
```
Each online evaluation create command returns an `onlineEvaluationConfigId`, and the A/B test command returns an `abTestId`. Use `agentcore eval ab-test get --id <ab-test-id>` to view per-variant results and `agentcore eval ab-test stop --id <ab-test-id>` to end the test.
Create one online evaluation config per variant with `create_online_evaluation_config`. Set `serviceNames` to the endpoint’s `service.name` and `logGroupNames` to its event log group. Then create the test with `create_ab_test`, using `perVariantOnlineEvaluationConfig`. For the full boto3 example — including polling results and stopping the test — see [Run an A/B test with target-based routing](ab-testing-target-based.md), starting from the **Create the A/B test** step.

### Send traffic
<a name="ab-testing-3p-send-traffic"></a>

The load generator on the target-based page sets `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id`. The Lambda handler and the stickiness configuration on these targets read `x-session-id` instead. Use the following script, which sends a new `x-session-id` for each session and reuses it for every request in that session. Replace `<gateway-id>` with your Gateway ID:

```
#!/bin/bash
PROMPTS=(
  "What is the status of order ORD-1003?"
  "It is late. Can I get a discount?"
)

for i in $(seq 1 30); do
  SESSION_ID=$(uuidgen)
  echo "=== Session $i: $SESSION_ID ==="
  for PROMPT in "${PROMPTS[@]}"; do
    agentcore invoke --gateway <gateway-id> \
      --region us-west-2 \
      --path /customer-support-control/invocations \
      --header "x-session-id: $SESSION_ID" \
      --payload "{\"prompt\": \"$PROMPT\"}"
    echo ""
  done
  sleep 2
done
```

## Troubleshooting
<a name="ab-testing-3p-troubleshooting"></a>

### A/B test shows no results after sending traffic
<a name="ab-testing-3p-no-results"></a>
+ Confirm gateway tracing is enabled ([Step 4: Enable AgentCore gateway tracing](#ab-testing-3p-step4-gateway-tracing)) — without it the aggregation pipeline cannot attribute sessions to variants.
+ Confirm each online evaluation config’s `serviceNames` matches the endpoint’s `service.name` and its `logGroupNames` includes the endpoint’s event log group. Online evaluation reads `aws/spans` automatically, so you do not list it — but the event log group (message content) must be listed.
+ Results appear after a session is idle for the configured `sessionTimeoutMinutes`, then within roughly 15 minutes of the next scoring cycle.