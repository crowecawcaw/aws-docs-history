

# Send AI agent telemetry
<a name="omni-send-ai-agent-telemetry"></a>

Add OpenTelemetry tracing to an AI agent written in Python or Node.js with LangGraph, LangChain, Strands Agents, CrewAI, OpenAI Agents, LlamaIndex, or the Vercel AI SDK, then run it on Amazon Bedrock AgentCore, AWS Lambda, or on your own compute (Amazon EC2, Amazon ECS, or Amazon EKS) so that its traces reach CloudWatch. CloudWatch Omni reads the model calls, tool calls, and orchestration steps from those traces to analyze and evaluate the agent. On AgentCore, the runtime exports the traces for you; on other compute, the agent exports them directly, as shown in Step 2.

If you are monitoring an application or service instead, see [Send application telemetry](omni-send-application-telemetry.md). For the endpoints and authentication that every path uses, see "Choose an endpoint" in [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

Step 2 shows one environment at a time: expand the section for where your agent runs (Amazon Bedrock AgentCore, AWS Lambda, Amazon EC2, Amazon ECS, or Amazon EKS).

**Choose how to instrument**

Three approaches lead to the same instrumented agent. Choose the first that fits how you work; this page is the manual path.


| Approach | What happens | Where to go | 
| --- | --- | --- | 
| AI coding assistant (default in the console) | Your coding agent installs the Omni skills from the Agent Toolkit for AWS, reads your repository, makes the changes on this page for you, and runs the verification. | [Use Omni skills](omni-use-omni-skills.md) | 
| IDE extension | The CloudWatch Omni extension for Visual Studio Code and Kiro detects your framework, applies the instrumentation, and shows traces in the editor as you develop. | [Develop with the IDE extension](omni-develop-with-the-ide-extension.md) | 
| Manually | You install a library, set environment variables where your agent runs, and verify in your space. Every command is on this page. | Continue below. | 

**Prerequisites**
+ **Transaction Search is enabled** in the account and Region that receive traces. Traces sent before it is enabled are not searchable. See [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html). On AgentCore, the administrator part of Step 2 enables it if it is not.
+ Your agent is written in **Python** or **Node.js**, and its framework is in [Supported environments, languages, and frameworks](omni-supported-environments-languages-and-frameworks.md).
+ On **AgentCore**, you can change the runtime's environment variables, and you or an administrator can edit its execution role.
+ On **AWS Lambda or your own compute**, you must attach the AWS managed policy [AWSXrayWriteOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSXrayWriteOnlyAccess.html) to the role your compute uses. For the endpoints, see "Choose an endpoint" in [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

**Step 1: Install an instrumentation library**

Choose your agent's language in the tabs. The choice applies to every code sample on this page and is remembered on the other pages in this guide. Then choose one of the two libraries; both export the same OTLP traces to CloudWatch and differ in what the spans contain. Zero-code instrumentation covers the frameworks and languages in [Supported environments, languages, and frameworks](omni-supported-environments-languages-and-frameworks.md).


| Library | What you get | Choose it when | 
| --- | --- | --- | 
| OpenTelemetry distribution (recommended) | The AWS Distro for OpenTelemetry auto-instruments model and tool calls with no code changes and records them as spans with gen\_ai.\* attributes. Frameworks with built-in OpenTelemetry tracing, such as Strands Agents, need no extra wiring. | You want the least code and standard semantic conventions, or your framework and language pair is listed only under the distribution in [Supported environments, languages, and frameworks](omni-supported-environments-languages-and-frameworks.md). | 
| OpenInference | Your framework's OpenInference instrumentor runs on top of the distribution. Spans are framework-native: AGENT, LLM, and TOOL span kinds with structured input and output. | You want framework-native spans and can add a package and, for some frameworks, a few lines of startup code. | 

**Important**  
On startup, the distribution registers the global tracer provider. OpenTelemetry uses only the first provider registered, so do not create another tracer provider or exporter. Attach instrumentors, processors, and custom spans to the distribution's provider, as shown in every snippet on this page.

**OpenTelemetry distribution (recommended)**

------
#### [ Python ]

```
pip install "aws-opentelemetry-distro>=0.20.0"
```

------
#### [ Node.js ]

```
npm install @aws/aws-distro-opentelemetry-node-autoinstrumentation@">=0.13.0"
```

------

**OpenInference**

**OpenInference is optional.** Choose it if you want its framework spans and accept the additional packages and, for some frameworks, startup code. Otherwise, use the OpenTelemetry distribution setup in the previous section.

Install the packages shown, and add any **startup code** to a module that your entry point imports first, before the agent is created. Every install command includes the distribution, so this path does not also need the previous section.

## LangGraph
<a name="omni-send-ai-agent-telemetry-langgraph"></a>

------
#### [ Python ]

```
pip install "aws-opentelemetry-distro>=0.20.0" openinference-instrumentation-langchain
```
+ No startup code is needed. Invoke the graph after startup, not at import time.

------
#### [ Node.js ]

```
npm install @aws/aws-distro-opentelemetry-node-autoinstrumentation@">=0.13.0" @opentelemetry/api @arizeai/openinference-instrumentation-langchain @langchain/core@">=1.0.0" @langchain/openai langchain zod
```

**agent.ts**

```
import { trace } from "@opentelemetry/api";
import { LangChainInstrumentation } from "@arizeai/openinference-instrumentation-langchain";
import * as CallbackManager from "@langchain/core/callbacks/manager";
import { ChatOpenAI } from "@langchain/openai";
import { createAgent, tool } from "langchain";
import * as z from "zod";

const instrumentation = new LangChainInstrumentation({
  tracerProvider: trace.getTracerProvider(),
});
instrumentation.manuallyInstrument(CallbackManager);

const getWeather = tool(
  ({ city }) => `The weather in ${city} is sunny.`,
  {
    name: "get_weather",
    description: "Get the weather for a city",
    schema: z.object({ city: z.string() }),
  },
);

const agent = createAgent({
  model: new ChatOpenAI({ model: "gpt-4o-mini" }),
  tools: [getWeather],
});

const result = await agent.invoke({
  messages: [{ role: "user", content: "What is the weather in Seattle?" }],
});
console.log(result.messages.at(-1)?.content);
```
+ Requires `@langchain/core` 1.0.0 or later.
+ `manuallyInstrument(CallbackManager)` is required for ESM. It attaches OpenInference to the distribution's global tracer provider; do not create another provider or exporter.
+ At startup, the distribution attempts to detect another instrumentation library for the same framework and disables its own. If detection fails, add `aws_langchain` to `OTEL_NODE_DISABLED_INSTRUMENTATIONS` so the distribution's instrumentation does not run alongside OpenInference. If the variable is not already set, use `OTEL_NODE_DISABLED_INSTRUMENTATIONS=fs,dns,aws_langchain`.

------

## Strands Agents
<a name="omni-send-ai-agent-telemetry-strands-agents"></a>

------
#### [ Python ]

```
pip install "aws-opentelemetry-distro>=0.20.0" openinference-instrumentation-strands-agents
```

**tracing.py**

```
from opentelemetry import trace
from strands.telemetry import StrandsTelemetry
from openinference.instrumentation.strands_agents import StrandsAgentsToOpenInferenceProcessor

current = trace.get_tracer_provider()
StrandsTelemetry(tracer_provider=current)
current.add_span_processor(StrandsAgentsToOpenInferenceProcessor())
```
+ Pass the distribution's provider into `StrandsTelemetry`. A provider that `StrandsTelemetry` creates itself is orphaned and never exports.
+ Use this path or the plain distribution, not both. Strands' native tracer occupies the instrumentation point, so the OpenInference processor is inert when native tracing is already active.

------
#### [ Node.js ]

Use the OpenTelemetry distribution; Strands' built-in OpenTelemetry tracing needs no extra wiring.

------

## CrewAI
<a name="omni-send-ai-agent-telemetry-crewai"></a>

CrewAI is Python only.

```
pip install "aws-opentelemetry-distro>=0.20.0" openinference-instrumentation-crewai "crewai[bedrock]>=1.10.1" "setuptools<81"
```
+ No startup code is needed.
+ Set `CREWAI_DISABLE_TELEMETRY=true` where the agent runs.
+ `crewai` earlier than 1.10.1 emits no spans.

## LlamaIndex
<a name="omni-send-ai-agent-telemetry-llamaindex"></a>

The LlamaIndex OpenInference instrumentor is Python only.

```
pip install "aws-opentelemetry-distro>=0.20.0" openinference-instrumentation-llama-index
```

**tracing.py**

```
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor

LlamaIndexInstrumentor().instrument()
```
+ The distribution does not discover this instrumentor at startup, so the dependency alone produces no framework spans. Call `LlamaIndexInstrumentor().instrument()` in startup code, before the agent is built. With no argument it attaches to the distribution's global tracer provider; do not create another provider or exporter.
+ Requires `llama-index-core` 0.10.5 or later; the `FunctionAgent` and `AgentWorkflow` APIs require 0.12 or later.
+ The `FunctionAgent` and `AgentWorkflow` workflow spans carry the `CHAIN` span kind, not `AGENT`; the model spans use `llm.*` attributes.

## OpenAI Agents
<a name="omni-send-ai-agent-telemetry-openai-agents"></a>

------
#### [ Python ]

```
pip install "aws-opentelemetry-distro>=0.20.0" openinference-instrumentation-openai-agents
```
+ No startup code is needed.
+ Remove any `set_tracing_disabled(True)` call from your code. While the built-in tracer is disabled, the instrumentor receives no spans.

------
#### [ Node.js ]

```
npm install @aws/aws-distro-opentelemetry-node-autoinstrumentation@">=0.13.0" @arizeai/openinference-instrumentation-openai-agents
```

**agent.ts**

```
import * as agents from "@openai/agents";
import { trace } from "@opentelemetry/api";
import { OpenAIAgentsInstrumentation } from "@arizeai/openinference-instrumentation-openai-agents";

const instrumentation = new OpenAIAgentsInstrumentation({
  tracerProvider: trace.getTracerProvider(),
});
instrumentation.manuallyInstrument(agents);

const agent = new agents.Agent({
  name: "Assistant",
  instructions: "You are a helpful assistant.",
});

const result = await agents.run(agent, "What is the capital of France?");
console.log(result.finalOutput);
```
+ At startup, the distribution attempts to detect another instrumentation library for the same framework and disables its own. If detection fails, add `aws_openai_agents` to `OTEL_NODE_DISABLED_INSTRUMENTATIONS` so the distribution's instrumentation does not run alongside OpenInference. If the variable is not already set, use `OTEL_NODE_DISABLED_INSTRUMENTATIONS=fs,dns,aws_openai_agents`.

------

## Vercel AI SDK
<a name="omni-send-ai-agent-telemetry-vercel-ai-sdk"></a>

The Vercel AI SDK is Node.js only. Use the OpenTelemetry distribution:

```
npm install @aws/aws-distro-opentelemetry-node-autoinstrumentation@">=0.13.0" ai @ai-sdk/amazon-bedrock
```

**Step 2: Run your agent and deliver its traces**

Expand the section for where your agent runs. Each one ends at Step 3.

**Start the agent with instrumentation**

The distribution must load before your application. AgentCore starter toolkit images configure startup automatically. Use these instructions for custom AgentCore images and your own compute.

------
#### [ Python ]

```
AGENT_OBSERVABILITY_ENABLED=true \
AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT=true \
OTEL_PYTHON_DISTRO=aws_distro \
OTEL_PYTHON_CONFIGURATOR=aws_configurator \
OTEL_RESOURCE_ATTRIBUTES="service.name=<agent-name>,deployment.environment.name=<stage>,aws.log.group.names=<your-custom-log-group>" \
OTEL_EXPORTER_OTLP_TRACES_HEADERS="x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>" \
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
OTEL_TRACES_EXPORTER=otlp \
OTEL_LOGS_EXPORTER=none \
OTEL_METRICS_EXPORTER=none \
opentelemetry-instrument python /path/to/your/agent.py
```

------
#### [ Node.js ]

Determine the module format from the compiled application, not the TypeScript source.

For CommonJS:

```
AGENT_OBSERVABILITY_ENABLED=true \
OTEL_RESOURCE_ATTRIBUTES="service.name=<agent-name>,deployment.environment.name=<stage>,aws.log.group.names=<your-custom-log-group>" \
OTEL_EXPORTER_OTLP_TRACES_HEADERS="x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>" \
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
OTEL_TRACES_EXPORTER=otlp \
OTEL_LOGS_EXPORTER=none \
OTEL_METRICS_EXPORTER=none \
NODE_OPTIONS="--require=@aws/aws-distro-opentelemetry-node-autoinstrumentation/register" \
node /path/to/your/agent.js
```

For ESM:

```
AGENT_OBSERVABILITY_ENABLED=true \
OTEL_RESOURCE_ATTRIBUTES="service.name=<agent-name>,deployment.environment.name=<stage>,aws.log.group.names=<your-custom-log-group>" \
OTEL_EXPORTER_OTLP_TRACES_HEADERS="x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>" \
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
OTEL_TRACES_EXPORTER=otlp \
OTEL_LOGS_EXPORTER=none \
OTEL_METRICS_EXPORTER=none \
NODE_OPTIONS="--experimental-loader=@opentelemetry/instrumentation/hook.mjs --import=@aws/aws-distro-opentelemetry-node-autoinstrumentation/register" \
node /path/to/your/agent.js
```

Replace `/path/to/your/agent.js` with your compiled entry point. For more ESM startup options, see [Using the zero-code option with `@opentelemetry/auto-instrumentations-node`](https://github.com/open-telemetry/opentelemetry-js/blob/66c04030f8f2cb9c1a05e8dcf63c2ba52ffdc1da/doc/esm-support.md#using-the-zero-code-option-with-auto-instrumentations-node).

------

**Sampling**

Sampling determines which traces are recorded and exported.

For the complete list of supported sampler configurations, see [https://opentelemetry.io/docs/languages/sdk-configuration/general/\#otel\_traces\_sampler](https://opentelemetry.io/docs/languages/sdk-configuration/general/#otel_traces_sampler).

We recommend leaving `OTEL_TRACES_SAMPLER` unset. When your agent is the **instrumented root service** — it has no instrumented upstream caller — 100 percent of incoming traffic is captured as traces, so span-derived metrics such as token usage are recorded accurately.

You can record fewer traces to match your traffic and telemetry requirements, at the cost of incomplete or inaccurate agent metrics. Sampling is configured on the **instrumented root service**. For example, if your hosted agent is the root service, you can configure ratio-based sampling:

```
export OTEL_TRACES_SAMPLER=parentbased_traceidratio
export OTEL_TRACES_SAMPLER_ARG=0.9
```

Approximately 90 percent of incoming requests then generate and export traces.

## AgentCore
<a name="omni-send-ai-agent-telemetry-agentcore"></a>

On Amazon Bedrock AgentCore, the runtime exports your agent's spans to CloudWatch; there is no collector to run. Two people are usually involved: the developer sets environment variables on the runtime with every deployment, and an administrator enables trace delivery and grants the runtime role permission once for the account and Region.

**Configure the runtime** (developer, every deployment)

Set these environment variables on the AgentCore runtime:

```
AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT=true
```
+ `AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT=true` keeps prompt and response text in the spans, which **Agent traces** and evaluators read. For production redaction and who can read kept content, see [Protect sensitive data](omni-data-protection.md).
+ If you build your own container image, its command must start the agent under the OpenTelemetry launcher, as shown in the Amazon EC2, ECS, and EKS sections of Step 2. Images built by the AgentCore starter toolkit do this already.

With the AgentCore starter toolkit:

```
agentcore deploy \
  --env AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT=true
```
+ `--env` is repeatable, and its values are not persisted, so pass them on every deployment.
+ The toolkit sets `AGENT_OBSERVABILITY_ENABLED` for you; do not pass it with `--env`.

With infrastructure as code, this is the environment block for the runtime resource. AgentCore Runtime injects `AGENT_OBSERVABILITY_ENABLED=true`. When the AWS Distro for OpenTelemetry starts, that flag configures the trace-export defaults, including `OTEL_TRACES_EXPORTER=otlp`, `OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf`, and the regional X-Ray OTLP endpoint. Do not duplicate those managed defaults in the runtime resource; the only variable to set here is the content-extraction opt-out. The name and value are identical across tooling; only the syntax changes.

------
#### [ CDK TypeScript ]

```
environmentVariables: {
  AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT: "true",
}
```

------
#### [ CDK Python ]

```
environment_variables={
    "AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT": "true",
}
```

------
#### [ Terraform ]

```
environment_variables = {
  AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT = "true"
}
```

------
#### [ CloudFormation ]

```
EnvironmentVariables:
  AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT: "true"
```

------

**Enable trace delivery and grant permissions** (administrator, once per account and Region)

AgentCore delivers spans through the account's trace destination, which is the setting Transaction Search turns on. If Transaction Search is not enabled, set the destination:

```
aws xray update-trace-segment-destination --destination CloudWatchLogs --region <region>
```
+ The change takes effect after about 10 minutes.

**Note**  
You must configure the AgentCore Runtime execution role with the required telemetry permissions. See [Execution role for running an agent in AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html#runtime-permissions-execution).

**To send traces to AgentCore's custom log group**, you must also attach the following statement to the agent runtime's execution role. `logs:PutResourcePolicy` does not support resource-level permissions, so the statement grants it on all resources:

```
{
  "Effect": "Allow",
  "Action": [
    "logs:PutResourcePolicy"
  ],
  "Resource": "*"
}
```
+ A runtime deployed from a container image also needs permission to pull the image from Amazon ECR.

Continue to Step 3.

## AWS Lambda
<a name="omni-send-ai-agent-telemetry-aws-lambda"></a>

We recommend the [AWS Distro for OpenTelemetry Lambda layer](https://aws-otel.github.io/docs/getting-started/lambda#getting-started-with-aws-lambda-layers). Follow those instructions to attach the appropriate layer and configure its execution wrapper. Then set the following environment variables.

------
#### [ Python ]

```
AGENT_OBSERVABILITY_ENABLED=true
AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT=true
OTEL_PYTHON_DISTRO=aws_distro
OTEL_PYTHON_CONFIGURATOR=aws_configurator
OTEL_PYTHON_DISABLED_INSTRUMENTATIONS=none
OTEL_AWS_APPLICATION_SIGNALS_ENABLED=false
OTEL_EXPORTER_OTLP_TRACES_HEADERS=x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=none
OTEL_METRICS_EXPORTER=none
```

The Python Lambda layer enables a limited set of instrumentations by default to reduce cold-start duration. `OTEL_PYTHON_DISABLED_INSTRUMENTATIONS=none` enables the agent framework instrumentations, but can increase cold-start duration.

------
#### [ Node.js ]

```
AGENT_OBSERVABILITY_ENABLED=true
OTEL_AWS_APPLICATION_SIGNALS_ENABLED=false
OTEL_EXPORTER_OTLP_TRACES_HEADERS=x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=none
OTEL_METRICS_EXPORTER=none
```

If you chose the OpenTelemetry distribution, set `OTEL_NODE_ENABLED_INSTRUMENTATIONS` for your framework. The layer enables only `aws-sdk`, `aws-lambda`, and `http` by default, and it appends `aws-lambda` and `http` to any value you set, so do not include them:


| Framework | `OTEL_NODE_ENABLED_INSTRUMENTATIONS` | 
| --- | --- | 
| LangGraph or LangChain | aws-sdk,undici,aws\_langchain | 
| OpenAI Agents | aws-sdk,undici,aws\_openai\_agents | 
| Vercel AI SDK | aws-sdk,undici,aws\_vercel\_ai | 
| Strands Agents | Leave unset. Strands Agents emits spans through the tracer provider the layer starts. | 

With OpenInference, leave `OTEL_NODE_ENABLED_INSTRUMENTATIONS` unset. Install and initialize the OpenInference instrumentor before creating your agent, as shown in Step 1.

**Note**  
You must attach the AWS managed policy [`AWSXrayWriteOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSXrayWriteOnlyAccess.html) to the function's execution role so that the exporter can send traces to X-Ray.

**Important**  
**Custom trace destination requires a resource policy.** If you set `OTEL_EXPORTER_OTLP_TRACES_HEADERS` to deliver spans to your own log group, you must also add an Amazon CloudWatch Logs resource policy. The policy must allow X-Ray (`xray.amazonaws.com`) to call `logs:PutLogEvents` on that log group. Use the same policy shown in [Enabling CloudWatch Transaction Search](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html#observability-configure-builtin-cw), with your log group's ARN in `Resource`. Without this policy, X-Ray cannot deliver spans to your log group.

Continue to Step 3.

------

## Amazon EC2
<a name="omni-send-ai-agent-telemetry-amazon-ec2"></a>

On Amazon EC2, the instance role signs the traces.

**Start the agent with its environment**

Put the variables in the agent's systemd unit (`Environment=` lines) or start script, and make the launcher the unit's command.

------
#### [ Python ]

```
AGENT_OBSERVABILITY_ENABLED=true
AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT=true
OTEL_PYTHON_DISTRO=aws_distro
OTEL_PYTHON_CONFIGURATOR=aws_configurator
OTEL_RESOURCE_ATTRIBUTES=service.name=<agent-name>,deployment.environment.name=<stage>,aws.log.group.names=<your-custom-log-group>
OTEL_EXPORTER_OTLP_TRACES_HEADERS=x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=none
OTEL_METRICS_EXPORTER=none
```

------
#### [ Node.js ]

```
AGENT_OBSERVABILITY_ENABLED=true
OTEL_RESOURCE_ATTRIBUTES=service.name=<agent-name>,deployment.environment.name=<stage>,aws.log.group.names=<your-custom-log-group>
OTEL_EXPORTER_OTLP_TRACES_HEADERS=x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=none
OTEL_METRICS_EXPORTER=none
```
+ Node.js captures GenAI message content (model payloads and tool responses) by default; `AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT` is not required.

**Note**  
You must attach the AWS managed policy [`AWSXrayWriteOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSXrayWriteOnlyAccess.html) to the instance role so that the exporter can send traces to X-Ray.

**Important**  
**Custom trace destination requires a resource policy.** If you set `OTEL_EXPORTER_OTLP_TRACES_HEADERS` to deliver spans to your own log group, you must also add an Amazon CloudWatch Logs resource policy. The policy must allow X-Ray (`xray.amazonaws.com`) to call `logs:PutLogEvents` on that log group. Use the same policy shown in [Enabling CloudWatch Transaction Search](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html#observability-configure-builtin-cw), with your log group's ARN in `Resource`. Without this policy, X-Ray cannot deliver spans to your log group.

Continue to Step 3.

------

## Amazon ECS
<a name="omni-send-ai-agent-telemetry-amazon-ecs"></a>

On Amazon ECS, the task role signs the traces.

**Start the agent with its environment**

Put the variables in the `environment` block of the agent's container definition, and make the launcher the container's command.

------
#### [ Python ]

```
AGENT_OBSERVABILITY_ENABLED=true
AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT=true
OTEL_PYTHON_DISTRO=aws_distro
OTEL_PYTHON_CONFIGURATOR=aws_configurator
OTEL_RESOURCE_ATTRIBUTES=service.name=<agent-name>,deployment.environment.name=<stage>,aws.log.group.names=<your-custom-log-group>
OTEL_EXPORTER_OTLP_TRACES_HEADERS=x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=none
OTEL_METRICS_EXPORTER=none
```

------
#### [ Node.js ]

```
AGENT_OBSERVABILITY_ENABLED=true
OTEL_RESOURCE_ATTRIBUTES=service.name=<agent-name>,deployment.environment.name=<stage>,aws.log.group.names=<your-custom-log-group>
OTEL_EXPORTER_OTLP_TRACES_HEADERS=x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=none
OTEL_METRICS_EXPORTER=none
```

------
+ Node.js captures GenAI message content (model payloads and tool responses) by default; `AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT` is not required.

**Note**  
You must attach the AWS managed policy [`AWSXrayWriteOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSXrayWriteOnlyAccess.html) to the task role so that the exporter can send traces to X-Ray.

**Important**  
**Custom trace destination requires a resource policy.** If you set `OTEL_EXPORTER_OTLP_TRACES_HEADERS` to deliver spans to your own log group, you must also add an Amazon CloudWatch Logs resource policy. The policy must allow X-Ray (`xray.amazonaws.com`) to call `logs:PutLogEvents` on that log group. Use the same policy shown in [Enabling CloudWatch Transaction Search](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html#observability-configure-builtin-cw), with your log group's ARN in `Resource`. Without this policy, X-Ray cannot deliver spans to your log group.

Continue to Step 3.

## Amazon EKS
<a name="omni-send-ai-agent-telemetry-amazon-eks"></a>

On Amazon EKS, the pod's service account role signs the traces.

**Start the agent with its environment**

Put the variables in the `env` block of the agent's container in the pod spec, and make the launcher the container's command.

------
#### [ Python ]

```
AGENT_OBSERVABILITY_ENABLED=true
AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT=true
OTEL_PYTHON_DISTRO=aws_distro
OTEL_PYTHON_CONFIGURATOR=aws_configurator
OTEL_RESOURCE_ATTRIBUTES=service.name=<agent-name>,deployment.environment.name=<stage>,aws.log.group.names=<your-custom-log-group>
OTEL_EXPORTER_OTLP_TRACES_HEADERS=x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=none
OTEL_METRICS_EXPORTER=none
```

------
#### [ Node.js ]

```
AGENT_OBSERVABILITY_ENABLED=true
OTEL_RESOURCE_ATTRIBUTES=service.name=<agent-name>,deployment.environment.name=<stage>,aws.log.group.names=<your-custom-log-group>
OTEL_EXPORTER_OTLP_TRACES_HEADERS=x-aws-log-group=<your-custom-log-group>,x-aws-log-stream=<your-custom-log-stream>
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=none
OTEL_METRICS_EXPORTER=none
```

------
+ Set the log group and log stream in `OTEL_EXPORTER_OTLP_TRACES_HEADERS` to the destination you want the spans written to.
+ Node.js captures GenAI message content (model payloads and tool responses) by default; `AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT` is not required.
+ The pod's service account must have a role through Pod Identity or IRSA; without one the SDK falls back to the node role, which usually lacks the permission below.

**Note**  
You must attach the AWS managed policy [`AWSXrayWriteOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSXrayWriteOnlyAccess.html) to the pod's service account role so that the exporter can send traces to X-Ray.

**Important**  
**Custom trace destination requires a resource policy.** If you set `OTEL_EXPORTER_OTLP_TRACES_HEADERS` to deliver spans to your own log group, you must also add an Amazon CloudWatch Logs resource policy. The policy must allow X-Ray (`xray.amazonaws.com`) to call `logs:PutLogEvents` on that log group. Use the same policy shown in [Enabling CloudWatch Transaction Search](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html#observability-configure-builtin-cw), with your log group's ARN in `Resource`. Without this policy, X-Ray cannot deliver spans to your log group.

Continue to Step 3.

**Step 3: Verify**

Use the console's automated verification. In your space, open **Settings › Ingestion** and choose your source: the **Add source** flow's verification step invokes the check for you. It confirms that traces are arriving and that they carry the agent, model, and tool spans CloudWatch Omni reads, and it identifies the failing setting when they do not. Run it after every deployment change.

If verification fails, see the "Troubleshoot missing traces" section of this page.

## Verify manually
<a name="omni-send-ai-agent-telemetry-verify-manually"></a>

**Traces arrive.** Invoke your agent, then open your space and choose **Agent traces**. A trace for the invocation appears within about five minutes. On AgentCore, if the list is empty, check the log group `/aws/bedrock-agentcore/runtimes/<agent-id>-<endpoint-name>` (`<agent-id>-DEFAULT` for the default endpoint), where the runtime writes a `spans` stream; on your own compute, check the log group you set in `OTEL_EXPORTER_OTLP_TRACES_HEADERS`, or the shared `aws/spans` log group if that variable is not set. Transaction Search indexes 1 percent of spans by default for the trace list, so not every invocation is listed until you raise the indexing percentage; the spans themselves are all stored.

**The trace is complete.** Open the trace. A correctly instrumented agent shows an agent span with non-empty input and output and a child span for each model call and each tool call. With OpenInference, the spans carry `AGENT`, `LLM`, and `TOOL` kinds; with the OpenTelemetry distribution alone, the model calls carry `gen_ai.*` attributes. On AgentCore, the runtime's invoke span is the root and your agent's spans sit beneath it. If prompt and response text is blank, see [Protect sensitive data](omni-data-protection.md).

**Note**  
A successful invocation does not mean that traces arrived. Check for the agent, model, and tool spans, not only for an HTTP 200.

After verification passes, the agent appears in **Agents** in your space, and you can continue to [Analyze agent behavior](omni-agents-analyze.md).

**Troubleshoot missing traces**

The following table lists common troubleshooting steps for missing or incomplete traces.


| What you see | What to check | 
| --- | --- | 
| No spans are created | Auto-instrumentation did not start. Verify that the distribution and required instrumentation packages are installed in the application's runtime environment and that the application uses the documented startup command. Instrumentation must initialize before the agent framework is imported. For Python, also check package-manager environments, development reloaders, and pre-fork workers. For Node.js, verify the CommonJS or ESM preload configuration and confirm that the instrumentation is not disabled. Do not create another tracer provider or exporter. Temporarily use OTEL\_TRACES\_EXPORTER=console,otlp for Python or OTEL\_LOG\_LEVEL=debug for Node.js to inspect startup. | 
| HTTP spans appear, but agent, model, or tool spans do not | Verify that the framework and instrumentation versions are supported and that the corresponding instrumentation package is installed and enabled. Confirm that it is not listed in OTEL\_PYTHON\_DISABLED\_INSTRUMENTATIONS or OTEL\_NODE\_DISABLED\_INSTRUMENTATIONS. OpenInference startup code must run before the agent is created. | 
| Duplicate agent, model, or tool spans appear | Two equivalent instrumentations may be active. The distribution attempts to detect equivalent instrumentation at startup. If detection fails, add the corresponding AWS instrumentation, such as aws\_langchain or aws\_openai\_agents, to OTEL\_NODE\_DISABLED\_INSTRUMENTATIONS. | 
| Spans are created locally but do not reach CloudWatch | Verify OTEL\_TRACES\_EXPORTER, OTEL\_EXPORTER\_OTLP\_PROTOCOL, the OTLP endpoint, and OTEL\_EXPORTER\_OTLP\_TRACES\_HEADERS. Check exporter errors and network connectivity. On AWS Lambda, Amazon EC2, Amazon ECS, or Amazon EKS, verify that the compute role has [`AWSXrayWriteOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSXrayWriteOnlyAccess.html). On AgentCore, verify the execution-role permissions shown in the AgentCore section. | 
| The exporter returns 404 | OTEL\_EXPORTER\_OTLP\_ENDPOINT automatically appends /v1/traces. If the configured value already includes that path, use OTEL\_EXPORTER\_OTLP\_TRACES\_ENDPOINT instead so the path is not appended twice. | 
| Only the AgentCore runtime invocation span appears | AgentCore telemetry is working, but application auto-instrumentation did not start. Follow the checks in the first row. For a custom image, start the application under opentelemetry-instrument or the Node.js register hook. AgentCore enables agent observability, and the distribution derives the OTLP trace-export settings; you do not need to set OTEL\_TRACES\_EXPORTER on the runtime resource. | 
| Spans reach the log group but do not appear under Agent traces | Verify that Transaction Search is enabled and that the trace destination is CloudWatch Logs. Traces sent before Transaction Search was enabled are not searchable. After changing the destination, wait 10 minutes and invoke the agent again. | 
| Only some requests have traces | Check the caller's sampling decision. Unless the agent is the root service, leave OTEL\_TRACES\_SAMPLER unset so it follows the parent trace. | 
| Prompt, response, or tool content is blank | Set AWS\_GENAI\_CONTENT\_EXTRACTION\_OPT\_OUT=true to keep model payloads and tool request/response data on spans. If content is still missing, verify that the framework instrumentation captures it and that the application does not redact it. | 

For additional runtime-specific issues, see [Troubleshooting Python automatic instrumentation](https://opentelemetry.io/docs/zero-code/python/troubleshooting/), [JavaScript zero-code instrumentation](https://opentelemetry.io/docs/zero-code/js/), and [JavaScript zero-code configuration](https://opentelemetry.io/docs/zero-code/js/configuration/).