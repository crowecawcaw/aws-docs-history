# Get started with AgentCore Observability

Amazon Bedrock Amazon Bedrock AgentCore Observability helps you trace, debug, and monitor agent
performance in production environments. This guide helps you implement observability
features in your agent applications.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Step 1: Enable transaction search on
  CloudWatch](#enabling-transaction-search "#enabling-transaction-search")
- [Step 2: Enable observability for
  Amazon Bedrock AgentCore Runtime hosted agents](#enabling-observability-runtime-hosted "#enabling-observability-runtime-hosted")
- [Step 3: Enable observability for
  non-Amazon Bedrock AgentCore-hosted agents](#enabling-observability-non-runtime-hosted "#enabling-observability-non-runtime-hosted")
- [Step 4: Observe your agent with GenAI observability on Amazon CloudWatch](#agentcore-observability-genai-cloudwatch "#agentcore-observability-genai-cloudwatch")
- [Best practices](#best-practices "#best-practices")

## Prerequisites

Before starting, make sure you have:

- **AWS Account** with credentials configured
  (`aws configure`) with model access enabled to the Foundation
  Model you would like to use.
- **Python 3.10+** installed
- **Enable transaction search** on Amazon CloudWatch. Only once, first-time users must enable [CloudWatch Transaction Search](../../../AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.md "../../../AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.md") to view Bedrock Amazon Bedrock AgentCore
  spans and traces
- **Add the OpenTelemetry library** Include
  `aws-opentelemetry-distro` (ADOT) in your requirements.txt
  file.
- Make sure that your framework is configured to emit traces (eg.
  `strands-agents[otel]` package), you may sometimes need to
  include `<your-agent-framework-auto-instrumentor>` # e.g.,
  `opentelemetry-instrumentation-langchain`

Amazon Bedrock AgentCore Observability offers two ways to configure monitoring to match
different infrastructure needs:

1. Amazon Bedrock AgentCore Runtime-hosted agents
2. Non-runtime hosted agents

As a one time setup per AWS account, first time users
need to enable Transaction Search on Amazon CloudWatch. There are two ways to do
this, via the API and via the CloudWatch Console.

## Step 1: Enable transaction search on

CloudWatch

After you enable Transaction Search, it can take ten minutes for spans to become
available for search and analysis. Choose one of the options below:

### Option 1: Enable transaction search

using an API

###### To enable transaction search using the API

1. Create a policy that grants access to ingest spans in CloudWatch Logs
   using AWS CLI.

An example is shown below on how to format your AWS CLI command with
`PutResourcePolicy`.

```
aws logs put-resource-policy --policy-name MyResourcePolicy --policy-document '{ "Version": "2012-10-17"		 	 	 , "Statement": [ { "Sid": "TransactionSearchXRayAccess", "Effect": "Allow", "Principal": { "Service": "xray.amazonaws.com" }, "Action": "logs:PutLogEvents", "Resource": [ "arn:partition:logs:region:account-id:log-group:aws/spans:*", "arn:partition:logs:region:account-id:log-group:/aws/application-signals/data:*" ], "Condition": { "ArnLike": { "aws:SourceArn": "arn:partition:xray:region:account-id:*" }, "StringEquals": { "aws:SourceAccount": "account-id" } } } ]}'
```

2. Configure the destination of trace segments.

An example is shown below on how to format your AWS CLI command with
`UpdateTraceSegmentDestination`.

```
aws xray update-trace-segment-destination --destination CloudWatchLogs
```

3. **Optional** Configure the amount of spans to
   index.

Configure your desired sampling percentage with
`UpdateIndexingRule`.

```
aws xray update-indexing-rule --name "Default" --rule '{"Probabilistic": {"DesiredSamplingPercentage": number}}'
```

### Option 2: Enable transaction

search in the CloudWatch console

###### To enable transaction search in the CloudWatch console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. From the navigation pane, under **Application Signals**, choose **Transaction
   Search**.
3. Choose **Enable Transaction Search**.
4. Select the box to ingest spans as structured logs, and enter a percentage
   of spans to be indexed. You can index spans at 1% for free and change the
   percentage later based on your requirements.

Now proceed to exploring the two ways to configure observability.

## Step 2: Enable observability for

Amazon Bedrock AgentCore Runtime hosted agents

Amazon Bedrock AgentCore Runtime-hosted agents are deployed and executed directly within the
Amazon Bedrock AgentCore environment, providing automatic instrumentation with minimal
configuration. This approach offers the fastest path to deployment and is ideal for
rapid development and testing.

For a complete example, refer to this [notebook](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/06-AgentCore-observability/01-Agentcore-runtime-hosted/runtime_with_strands_and_bedrock_models.ipynb "https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/06-AgentCore-observability/01-Agentcore-runtime-hosted/runtime_with_strands_and_bedrock_models.ipynb")

### Set up folder and virtual

environment

Create a new folder for your agent. Then create and initialize a new python
virtual environment.

```
mkdir agentcore-observability-quickstart
cd agentcore-observability-quickstart
python3 -m venv .venv
source .venv/bin/activate
```

### Create your agent

The following is an example of using the Strands Agents SDK.

To enable OTEL exporting, install [Strands Agents](https://strandsagents.com/latest/ "https://strandsagents.com/latest/") with otel extra
dependencies:

```
pip install 'strands-agents[otel]'
```

Use the following steps to host a strands agent on an AgentCore Runtime:

```
##  Save this as strands_claude.py
from strands import Agent, tool
from strands_tools import calculator # Import the calculator tool
import argparse
import json
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands.models import BedrockModel

app = BedrockAgentCoreApp()

# Create a custom tool
@tool
def weather():
    """ Get weather """ # Dummy implementation
    return "sunny"


model_id = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
model = BedrockModel(
    model_id=model_id,
)
agent = Agent(
    model=model,
    tools=[calculator, weather],
    system_prompt="You're a helpful assistant. You can do simple math calculation, and tell the weather."
)

@app.entrypoint
def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")
    print("User input:", user_input)
    response = agent(user_input)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    app.run()
```

### Deploy and invoke your agent on

Amazon Bedrock AgentCore Runtime

Use the following code to deploy the agent to AgentCore Runtime by using the
`bedrock_agentcore_starter_toolkit` package.

```
from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session
boto_session = Session()
region = boto_session.region_name

agentcore_runtime = Runtime()
agent_name = "strands_claude_getting_started"
response = agentcore_runtime.configure(
    entrypoint="strands_claude.py",
    auto_create_execution_role=True,
    auto_create_ecr=True,
    requirements_file="requirements.txt", # make sure aws-opentelemetry-distro exists along with your libraries required to run your agent
    region=region,
    agent_name=agent_name
)

launch_result = agentcore_runtime.launch()
launch_result
```

In these steps you deployed your strands agent to an AgentCore Runtime with the starter
toolkit. When you invoke your agent, it is automatically instrumented using Open Telemetry.

Invoke your agent using the following command and view the Traces, sessions and
metrics on GenAI Observability dashboard on Amazon CloudWatch.

```
invoke_response = agentcore_runtime.invoke({"prompt": "How is the weather now?"})
invoke_response
```

## Step 3: Enable observability for

non-Amazon Bedrock AgentCore-hosted agents

For agents running outside of the Amazon Bedrock AgentCore runtime, you can deliver the same
monitoring capabilities for agents deployed on your own infrastructure. This allows
consistent observability regardless of where your agents run. Use the
following steps to configure the environment variables needed to observe
your agents.

For a complete example, refer to this [notebook](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/06-AgentCore-observability/02-Agent-not-hosted-on-runtime/Strands/Strands_Observability.ipynb "https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/06-AgentCore-observability/02-Agent-not-hosted-on-runtime/Strands/Strands_Observability.ipynb")

### Configure AWS

environment variables

```
export AWS_ACCOUNT_ID=<account id>
export AWS_DEFAULT_REGION=<default region>
export AWS_REGION=<region>
export AWS_ACCESS_KEY_ID=<access key id>
export AWS_SECRET_ACCESS_KEY=<secret key>
```

### Configure CloudWatch

logging

Create a log group and log stream for your agent in Amazon CloudWatch which you
can use to configure below environment variables.

### Configure

OpenTelemetry environment variables

```
export AGENT_OBSERVABILITY_ENABLED=true # Activates the ADOT pipeline
export OTEL_PYTHON_DISTRO=aws_distro # Uses AWS Distro for OpenTelemetry
export OTEL_PYTHON_CONFIGURATOR=aws_configurator # Sets AWS configurator for ADOT SDK
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf # Configures export protocol
export  OTEL_EXPORTER_OTLP_LOGS_HEADERS=x-aws-log-group=<YOUR-LOG-GROUP>,x-aws-log-stream=<YOUR-LOG-STREAM>,x-aws- metric-namespace=<YOUR-NAMESPACE>
# Directs logs to CloudWatch groups
export OTEL_RESOURCE_ATTRIBUTES=service.name=`<YOUR-AGENT-NAME>` # Identifies your agent in observability data
```

Replace `<YOUR-AGENT-NAME>` with a unique name to
identify this agent in the GenAI Observability dashboard and logs.

### Create an agent locally

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

### Run your agent with

automatic instrumentation command

With aws-opentelemetry-distro in your requirements.txt, the
`opentelemetry-instrument` command will:

- Load your OTEL configuration from your environment variables
- Automatically instrument Strands, Amazon Bedrock calls, agent tool and
  databases, and other requests made by agent
- Send traces to CloudWatch
- Enable you to visualize the agent's decision-making process in the GenAI
  Observability dashboard

```
opentelemetry-instrument python agent.py
```

You can now view your traces, sessions and metrics on GenAI Observability
Dashboard on Amazon CloudWatch with the value of **YOUR-AGENT-NAME** that you configured in your
[environment
variables](#configure-opentelemetry-environment-variables "#configure-opentelemetry-environment-variables").

To correlate traces across multiple agent runs, you can associate a session ID
with your telemetry data using OpenTelemetry baggage:

```
from opentelemetry import baggage, context
ctx = baggage.set_baggage("session.id", session_id)
```

Run the session-enabled version following command, complete implementation
provided in the [notebook](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/06-AgentCore-observability/02-Agent-not-hosted-on-runtime/Strands/Strands_Observability.ipynb "https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/06-AgentCore-observability/02-Agent-not-hosted-on-runtime/Strands/Strands_Observability.ipynb"):

```
opentelemetry-instrument python strands_travel_agent_with_session.py --session-id "user-session-123"
```

## Step 4: Observe your agent with GenAI observability on Amazon CloudWatch

After implementing observability, you can view the collected data in
CloudWatch:

### Observe your agent

1. Open the [GenAI Observability on CloudWatch console](https://console.aws.amazon.com/cloudwatch/home#gen-ai-observability "https://console.aws.amazon.com/cloudwatch/home#gen-ai-observability")
2. You can view the data related to model invocations and agents on
   Bedrock Amazon Bedrock AgentCore on the dashboard.
3. In the Bedrock Agentcore tab you can view Agents View, Sessions
   View and Traces View.
4. Agents View lists all your Agents that are on and not on runtime, you can
   also choose an agent and view further details like runtime metrics,
   sessions and traces specific to an agent.
5. In the **Sessions View** tab, you can navigate across all the sessions
   associated with agents.
6. In the **Trace View** tab, you can look into the traces and span information
   for agents. Also explore the trace trajectory and timeline by choosing a
   trace.

### View logs in CloudWatch

###### To view logs in CloudWatch

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/")
2. In the left navigation pane, expand **Logs** and select
   **Log groups**
3. Search for your agent's log group:
   - Standard logs (stdout/stderr) Location:
     `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/[runtime-logs]
<UUID>`
   - OTEL structured logs:
     `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/runtime-logs`

### View traces and spans

###### To view traces and spans

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/")
2. Select **Transaction Search** from the left
   navigation
3. Location: `/aws/spans/default`
4. Filter by service name or other criteria
5. Select a trace to view the detailed execution graph

### View metrics

###### To view metrics

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/")
2. Select **Metrics** from the left navigation
3. Browse to the `bedrock-agentcore` namespace
4. Explore the available metrics

## Best practices

1. **Start simple, then expand** - The default
   observability provided by Amazon Bedrock AgentCore captures most critical metrics
   automatically, including model calls, token usage, and tool execution.
2. **Configure for development stage** - Tailor your
   observability configuration to match your current development phase and
   progressively adjust.
3. **Use consistent naming** - Establish naming
   conventions for services, spans, and attributes from the start
4. **Filter sensitive data** - Prevent exposure of
   confidential information by filtering sensitive data from observability
   attributes and payloads.
5. **Set up alerts** - Configure CloudWatch alarms
   to notify you of potential issues before they impact users
