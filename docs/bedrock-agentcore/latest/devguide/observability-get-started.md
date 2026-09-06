

# Get started with AgentCore Observability
<a name="observability-get-started"></a>

Amazon Bedrock AgentCore Observability helps you trace, debug, and monitor agent performance in production environments. This guide helps you implement observability features in your agent applications.

**Topics**
+ [Prerequisites](#prerequisites)
+ [Step 1: Enable transaction search on CloudWatch](#enabling-transaction-search)
+ [Step 2: Enable observability for Amazon Bedrock AgentCore Runtime hosted agents](#enabling-observability-runtime-hosted)
+ [Step 3: Enable observability for non-Amazon Bedrock AgentCore-hosted agents](#enabling-observability-non-runtime-hosted)
+ [Step 4: Observe your agent with GenAI observability on Amazon CloudWatch](#agentcore-observability-genai-cloudwatch)
+ [Best practices](#best-practices)

## Prerequisites
<a name="prerequisites"></a>

Before starting, make sure you have:
+  ** AWS Account** with credentials configured ( `aws configure` ) with model access enabled to the Foundation Model you would like to use.
+  **Python 3.10\+** installed
+  **Enable transaction search** on Amazon CloudWatch. Only once, first-time users must enable [CloudWatch Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html) to view Bedrock Amazon Bedrock AgentCore spans and traces
+  **(Non-runtime agents only) Add the OpenTelemetry library** – Include `aws-opentelemetry-distro` (ADOT) in your requirements.txt file. If you host your agent on AWS Lambda, use the [AWS Lambda Layer for OpenTelemetry](https://aws-otel.github.io/docs/getting-started/lambda) on the AWS Distro for OpenTelemetry website instead.
+  **(Non-runtime agents only)** Make sure that your framework is configured to emit traces (for example, `strands-agents[otel]` package). You may sometimes need to include your agent framework’s auto-instrumentor (for example, `opentelemetry-instrumentation-langchain` ).

Amazon Bedrock AgentCore Observability offers two ways to configure monitoring to match different infrastructure needs:

1. Amazon Bedrock AgentCore Runtime-hosted agents

1. Non-runtime hosted agents

As a one time setup per AWS account, first time users need to enable Transaction Search on Amazon CloudWatch. There are two ways to do this, via the API and via the CloudWatch Console.

## Step 1: Enable transaction search on CloudWatch
<a name="enabling-transaction-search"></a>

After you enable Transaction Search, it can take ten minutes for spans to become available for search and analysis. Choose one of the options below:

### Option 1: Enable transaction search using an API
<a name="enable-transaction-search-api"></a>

 **To enable transaction search using the API** 

1. Create a policy that grants access to ingest spans in CloudWatch Logs using AWS CLI.

   An example is shown below on how to format your AWS CLI command with `PutResourcePolicy`.

   ```
   aws logs put-resource-policy --policy-name MyResourcePolicy --policy-document '{ "Version": "2012-10-17", "Statement": [ { "Sid": "TransactionSearchXRayAccess", "Effect": "Allow", "Principal": { "Service": "xray.amazonaws.com" }, "Action": "logs:PutLogEvents", "Resource": [ "arn:partition:logs:region:account-id:log-group:aws/spans:*", "arn:partition:logs:region:account-id:log-group:/aws/application-signals/data:*" ], "Condition": { "ArnLike": { "aws:SourceArn": "arn:partition:xray:region:account-id:*" }, "StringEquals": { "aws:SourceAccount": "account-id" } } } ]}'
   ```

1. Configure the destination of trace segments.

   An example is shown below on how to format your AWS CLI command with `UpdateTraceSegmentDestination`.

   ```
   aws xray update-trace-segment-destination --destination CloudWatchLogs
   ```

1.  **Optional** Configure the amount of spans to index.

   Configure your desired sampling percentage with `UpdateIndexingRule`.

   ```
   aws xray update-indexing-rule --name "Default" --rule '{"Probabilistic": {"DesiredSamplingPercentage": number}}'
   ```

### Option 2: Enable transaction search in the CloudWatch console
<a name="enable-transaction-search-console"></a>

 **To enable transaction search in the CloudWatch console** 

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane under **Setup** , choose **Settings**.

1. Select **Account** and choose **X-Ray traces** tab.

1. In the **Transaction Search** section, choose **View settings**.

1. On the page that opens, choose **Edit**.

1. Choose **Enable Transaction Search**.

1. Select **For X-Ray users** and enter the percentage of traces to index. You can index 1% of traces at no cost and adjust this percentage later based on your needs.

1. Choose **Save** . Wait till **Ingest OpenTelemetry spans** shows **Enabled** before sending traces.

Let’s now proceed to exploring the two ways to configure observability.

## Step 2: Enable observability for Amazon Bedrock AgentCore Runtime hosted agents
<a name="enabling-observability-runtime-hosted"></a>

Amazon Bedrock AgentCore Runtime-hosted agents are deployed and executed directly within the Amazon Bedrock AgentCore environment, providing automatic instrumentation with minimal configuration. When you deploy an agent using the AgentCore CLI, the runtime automatically instruments your agent with OpenTelemetry — no additional OTEL libraries or configuration are needed.

For a complete example, refer to the [AgentCore Observability samples on GitHub](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-features/06-observe-evaluate-optimize-your-agent/01-observe) 

### Create your agent project
<a name="create-agent-strands"></a>

Create a new project using the AgentCore CLI. This sets up your project folder, virtual environment, and dependencies:

```
npm install -g @aws/agentcore
agentcore create \
  --project-name StrandsObservability \
  --name StrandsClaudeGettingStarted \
  --language Python \
  --framework Strands \
  --model-provider Bedrock \
  --memory none
cd StrandsObservability/app/StrandsClaudeGettingStarted
uv add strands-agents-tools
cd ../..
```

In the project’s agent directory, replace the default agent code with your own agent logic. The following is an example using the Strands Agents SDK:

```
## app/StrandsClaudeGettingStarted/main.py
from strands import Agent, tool
from strands_tools import calculator
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands.models import BedrockModel

app = BedrockAgentCoreApp()

@tool
def weather():
    """Get weather"""
    return "sunny"

model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
)
agent = Agent(
    model=model,
    tools=[calculator, weather],
    system_prompt="You're a helpful assistant. You can do simple math calculation, and tell the weather."
)

@app.entrypoint
def strands_agent_bedrock(payload):
    """Invoke the agent with a payload"""
    user_input = payload.get("prompt")
    if not isinstance(user_input, str) or not user_input:
        return "Error: 'prompt' must be a non-empty string"
    response = agent(user_input)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    app.run()
```

### Deploy and invoke your agent
<a name="deploy-invoke-agent"></a>

Deploy the agent to AgentCore Runtime. The AgentCore CLI handles packaging, deployment, and automatic OTEL instrumentation:

```
agentcore deploy
```

After deployment, your agent runs on AgentCore Runtime and is automatically instrumented using OpenTelemetry. Invoke your agent and view the traces, sessions, and metrics on the GenAI Observability dashboard in Amazon CloudWatch:

```
agentcore invoke
```

Alternatively, you can invoke your agent programmatically using the AWS SDK:

```
import boto3, json

client = boto3.client('bedrock-agentcore')

response = client.invoke_agent_runtime(
    agentRuntimeArn="YOUR_AGENT_RUNTIME_ARN",
    runtimeSessionId="my-observability-session-001",
    payload=json.dumps({"prompt": "What is 2 + 2?"}),
    qualifier="DEFAULT"
)

print(json.loads(response['response'].read()))
```

## Step 3: Enable observability for non-Amazon Bedrock AgentCore-hosted agents
<a name="enabling-observability-non-runtime-hosted"></a>

For agents running outside of the Amazon Bedrock AgentCore runtime, you can deliver the same monitoring capabilities for agents deployed on your own infrastructure. This allows consistent observability regardless of where your agents run. Use the following steps to configure the environment variables needed to observe your agents.

For a complete example, see the [Agents on Amazon EKS sample](https://github.com/awslabs/agentcore-samples/tree/main/03-integrations/agents-hosted-outside-runtime/agents-on-eks) on the GitHub website.

### Configure AWS environment variables
<a name="configure-aws-environment-variables"></a>

```
export AWS_ACCOUNT_ID=<account id>
export AWS_DEFAULT_REGION=<default region>
export AWS_REGION=<region>
export AWS_ACCESS_KEY_ID=<access key id>
export AWS_SECRET_ACCESS_KEY=<secret key>
```

### Configure CloudWatch logging
<a name="configure-cloudwatch-logging"></a>

Create a log group and log stream for your agent in Amazon CloudWatch which you can use to configure below environment variables.

### Configure OpenTelemetry environment variables
<a name="configure-opentelemetry-environment-variables"></a>

```
export AGENT_OBSERVABILITY_ENABLED=true # Activates the ADOT pipeline
export OTEL_PYTHON_DISTRO=aws_distro # Uses AWS Distro for OpenTelemetry
export OTEL_PYTHON_CONFIGURATOR=aws_configurator # Sets AWS configurator for ADOT SDK
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf # Configures export protocol
export  OTEL_EXPORTER_OTLP_LOGS_HEADERS=x-aws-log-group=<YOUR-LOG-GROUP>,x-aws-log-stream=<YOUR-LOG-STREAM>,x-aws-metric-namespace=<YOUR-NAMESPACE>
# Directs logs to CloudWatch groups
export OTEL_EXPORTER_OTLP_TRACES_HEADERS=x-aws-log-group=<YOUR-LOG-GROUP>,x-aws-log-stream=<YOUR-TRACES-LOG-STREAM>
# (Optional) Directs spans to your log group instead of the aws/spans log group. Requires ADOT version 0.18.0 or later.
export OTEL_RESOURCE_ATTRIBUTES=service.name=<YOUR-AGENT-NAME> # Identifies your agent in observability data
export OTEL_AWS_APPLICATION_SIGNALS_ENABLED=false # AWS Lambda Layer for OpenTelemetry only: disables Application Signals
export OTEL_LOGS_EXPORTER=otlp # AWS Lambda Layer for OpenTelemetry only: exports logs over OTLP
export OTEL_METRICS_EXPORTER=awsemf # AWS Lambda Layer for OpenTelemetry only: exports metrics as CloudWatch EMF
```

Replace {{<YOUR-AGENT-NAME>}} with a unique name to identify this agent in the GenAI Observability dashboard and logs.

**Note**  
If you set `OTEL_EXPORTER_OTLP_TRACES_HEADERS` to deliver spans to your own log group, you must also add an Amazon CloudWatch Logs resource policy. The policy must allow X-Ray (`xray.amazonaws.com`) to call `logs:PutLogEvents` on that log group. Use the same policy shown in [Enable transaction search using an API](#enable-transaction-search-api), with your log group’s ARN in `Resource`. Without this policy, X-Ray can’t deliver spans to your log group.

### Create an agent locally
<a name="create-agent-locally"></a>

```
# Create agent.py -  Strands agent that is a weather assistant
from strands import Agent
from strands_tools import http_request

# Define a weather-focused system prompt
WEATHER_SYSTEM_PROMPT = """You are a weather assistant with HTTP capabilities. You can:

1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States

When retrieving weather information:
1. First get the coordinates or grid information using https://api.weather.gov/points/{latitude},{longitude} or https://api.weather.gov/points/{zipcode}
2. Then use the returned forecast URL to get the actual forecast

When displaying responses:
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language

Always explain the weather conditions clearly and provide context for the forecast.
"""

# Create an agent with HTTP capabilities
weather_agent = Agent(
    system_prompt=WEATHER_SYSTEM_PROMPT,
    tools=[http_request],  # Explicitly enable http_request tool
)

response = weather_agent("What's the weather like in Seattle?")
print(response)
```

### Run your agent with automatic instrumentation command
<a name="run-agent-automatic-instrumentation"></a>

With `aws-opentelemetry-distro` in your requirements.txt, the `opentelemetry-instrument` command will:
+ Load your OTEL configuration from your environment variables
+ Automatically instrument Strands, Amazon Bedrock calls, agent tools and databases, and other requests made by the agent
+ Send traces to CloudWatch
+ Enable you to visualize the agent’s decision-making process in the GenAI Observability dashboard

Use the following command to run your agent with automatic instrumentation:

```
opentelemetry-instrument python agent.py
```

If you host your agent on AWS Lambda, use the [AWS Lambda Layer for OpenTelemetry](https://aws-otel.github.io/docs/getting-started/lambda) on the AWS Distro for OpenTelemetry website. Add the layer to your function, and then set the `AWS_LAMBDA_EXEC_WRAPPER` environment variable to `/opt/otel-instrument`. The layer then auto-instruments your function. With this approach, you don’t need to add the `aws-opentelemetry-distro` package or run the `opentelemetry-instrument` command described earlier.

**ADOT Collector not supported for agent observability**  
The ADOT Collector is not supported for agent observability. To send telemetry from an agent hosted outside of AgentCore runtime, you must use either the ADOT SDK or the AWS Lambda Layer for OpenTelemetry.

You can now view your traces, sessions and metrics on GenAI Observability Dashboard on Amazon CloudWatch with the value of **YOUR-AGENT-NAME** that you configured in your [environment variables](#configure-opentelemetry-environment-variables).

To correlate traces across multiple agent runs, you can associate a session ID with your telemetry data using OpenTelemetry baggage:

```
from opentelemetry import baggage, context
ctx = baggage.set_baggage("session.id", session_id)
```

## Step 4: Observe your agent with GenAI observability on Amazon CloudWatch
<a name="agentcore-observability-genai-cloudwatch"></a>

After implementing observability, you can view the collected data in CloudWatch:

### Observe your agent
<a name="agentcore-observability-observe"></a>

1. Open the [GenAI Observability on CloudWatch console](https://console.aws.amazon.com/cloudwatch/home#gen-ai-observability) 

1. You can view the data related to model invocations and agents on Bedrock Amazon Bedrock AgentCore on the dashboard.

1. In the Bedrock Agentcore tab you can view Agents View, Sessions View and Traces View.

1. Agents View lists all your Agents that are on and not on runtime, you can also choose an agent and view further details like runtime metrics, sessions and traces specific to an agent.

1. In the **Sessions View** tab, you can navigate across all the sessions associated with agents.

1. In the **Trace View** tab, you can look into the traces and span information for agents. Also explore the trace trajectory and timeline by choosing a trace.

### View logs in CloudWatch
<a name="view-logs-cloudwatch"></a>

 **To view logs in CloudWatch** 

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/) 

1. In the left navigation pane, expand **Logs** and select **Log groups** 

1. Search for your agent’s log group:
   + Standard logs (stdout/stderr) Location: `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/[runtime-logs] <UUID>` 
   + OTEL structured logs: `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/runtime-logs` 

### View traces and spans
<a name="view-traces-spans"></a>

 **To view traces and spans** 

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/) 

1. Select **Transaction Search** from the left navigation

1. Location: the `spans` log stream in the agent’s log group (`/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>`), or the `default` log stream in the `aws/spans` log group for agents that use the shared span destination

1. Filter by service name or other criteria

1. Select a trace to view the detailed execution graph

### View metrics
<a name="view-metrics"></a>

 **To view metrics** 

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/) 

1. Select **Metrics** from the left navigation

1. Browse to the `bedrock-agentcore` namespace

1. Explore the available metrics

## Best practices
<a name="best-practices"></a>

1.  **Start simple, then expand** - The default observability provided by Amazon Bedrock AgentCore captures most critical metrics automatically, including model calls, token usage, and tool execution.

1.  **Configure for development stage** - Tailor your observability configuration to match your current development phase and progressively adjust.

1.  **Use consistent naming** - Establish naming conventions for services, spans, and attributes from the start

1.  **Filter sensitive data** - Prevent exposure of confidential information by filtering sensitive data from observability attributes and payloads.

1.  **Set up alerts** - Configure CloudWatch alarms to notify you of potential issues before they impact users