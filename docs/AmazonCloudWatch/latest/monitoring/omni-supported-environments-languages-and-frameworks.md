

# Supported environments, languages, and frameworks
<a name="omni-supported-environments-languages-and-frameworks"></a>

The environments, languages, and frameworks with a documented path for sending telemetry to CloudWatch Omni.

**Environments**


| Environment | Workload | How telemetry leaves | Signals | Deployment tooling documented | Procedure | 
| --- | --- | --- | --- | --- | --- | 
| Amazon EC2 | Applications, AI agents | Applications: CloudWatch agent on the host. AI agents: direct export from the ADOT SDK. | Applications: traces, metrics, logs. AI agents: traces. | AWS CLI, CDK (TypeScript, Python, Java), Terraform, CloudFormation | [Applications](./omni-send-application-telemetry.html#amazon-ec2) · [AI agents](./omni-send-ai-agent-telemetry.html#amazon-ec2) | 
| Amazon ECS (Fargate) | Applications, AI agents | Applications: CloudWatch agent sidecar. AI agents: direct export from the ADOT SDK. | Applications: traces, metrics, logs. AI agents: traces. | AWS CLI, CDK (TypeScript, Python, Java), Terraform, CloudFormation | [Applications](./omni-send-application-telemetry.html#amazon-ecs) · [AI agents](./omni-send-ai-agent-telemetry.html#amazon-ecs) | 
| Amazon EKS | Applications, AI agents | Applications: CloudWatch Observability add-on (agent DaemonSet). AI agents: direct export from the ADOT SDK. | Applications: traces, metrics, logs. AI agents: traces. | AWS CLI, Terraform, or CDK for the add-on; kubectl, Helm, or CDK for the application | [Applications](./omni-send-application-telemetry.html#amazon-eks) · [AI agents](./omni-send-ai-agent-telemetry.html#amazon-eks) | 
| AWS Lambda | Applications, AI agents | Applications: Lambda delivers segments and logs itself; the ADOT layer adds handler spans. AI agents: the ADOT layer starts the OpenTelemetry runtime and the execution role signs trace exports. | Applications: traces, logs. AI agents: traces. | AWS CLI, CDK (TypeScript, Python, Java), Terraform, CloudFormation, AWS SAM | [Applications](omni-send-application-telemetry-from-aws-lambda.md) · [AI agents](./omni-send-ai-agent-telemetry.html#aws-lambda) | 
| Amazon Bedrock AgentCore | AI agents | The runtime exports traces. | Traces | AgentCore starter toolkit, CDK (TypeScript, Python), Terraform, CloudFormation | [AI agents](./omni-send-ai-agent-telemetry.html#agentcore) | 
| Azure VM | Applications | CloudWatch agent on the VM, credentials federated from the VM's managed identity. | Traces, metrics, logs | Azure setup script | [Applications](./omni-send-application-telemetry.html#azure-vm) | 
| Azure Kubernetes Service | Applications | CloudWatch Observability Helm chart, credentials federated from workload identity. | Traces, metrics, logs | Helm, kubectl | [Applications](./omni-send-application-telemetry.html#azure-aks) | 

**Application languages and frameworks**


| Language | Auto-instrumentation | Frameworks with documented notes | Procedure | 
| --- | --- | --- | --- | 
| Python | opentelemetry-instrument launcher | FastAPI, Flask, Django | [Step 4, Python tab](./omni-send-application-telemetry.html#python) | 
| Node.js | @opentelemetry/auto-instrumentations-node register hook | Express, gRPC | [Step 4, Node.js tab](./omni-send-application-telemetry.html#node.js) | 
| Java | OpenTelemetry Java agent (-javaagent) | Spring Boot, gRPC | [Step 4, Java tab](./omni-send-application-telemetry.html#java) | 
| .NET | Automatic instrumentation profiler for ASP.NET Core and gRPC services; SDK in code for console applications | ASP.NET Core, gRPC | [Step 4, .NET tab](./omni-send-application-telemetry.html#.net) | 
+ Any of these languages works in any application environment above. The listed frameworks are traced with no code changes; other libraries may be covered by the OpenTelemetry registry for the language.

**AI agent languages and frameworks**

Each language column lists the libraries documented for that framework: the OpenTelemetry distribution, and the OpenInference instrumentor where one exists. The distribution is required on both paths and is documented for Python and Node.js only: AWS Distro for OpenTelemetry 0.20.0 or later for Python, 0.13.0 or later for Node.js.


| Framework | Python | Node.js | Recommended versions | Notes | 
| --- | --- | --- | --- | --- | 
| LangGraph, LangChain | OpenTelemetry · OpenInference | OpenTelemetry · OpenInference | Python: langchain >=0.3.21,<2 Node.js: @langchain/core >=1.0.0,<2.0.0 | Traces through the LangChain instrumentor. Python is zero-code; Node.js needs startup code. | 
| Strands Agents | OpenTelemetry · OpenInference | OpenTelemetry | We recommend using the latest available Strands Agents version. | Built-in OpenTelemetry tracing on both languages, so the distribution needs no wiring: the SDK creates the agent, model, and tool spans itself. The Python OpenInference path attaches a span processor to the distribution's provider. Use one tracing path, not both, or the processor is inert. | 
| CrewAI | OpenTelemetry · OpenInference | — | crewai >=1.10.0,<2 | CrewAI is Python only. Zero-code. Requires setuptools<81 and CREWAI\_DISABLE\_TELEMETRY=true. | 
| LlamaIndex | OpenTelemetry · OpenInference | — | llama-index-core >=0.13.0,<1 | The LlamaIndex instrumentor is Python only. Call LlamaIndexInstrumentor().instrument() at startup; declaring the dependency alone produces no OpenInference spans. | 
| OpenAI Agents | OpenTelemetry · OpenInference | OpenTelemetry · OpenInference | Python: openai-agents >=0.3.3,<1 Node.js: @openai/agents-core >=0.1.0 | Python is zero-code once set\_tracing\_disabled(True) is removed. On Node.js, registering the instrumentation is not sufficient: the instrumentor attaches through the framework's own tracing processor, so you must also pass the imported SDK namespace to manuallyInstrument. Without that call, the agent creates no spans. | 
| Vercel AI SDK | — | OpenTelemetry | ai >=3.3.0,<7.0.0 | The Vercel AI SDK is Node.js only. The SDK emits its spans automatically once the distribution's provider is registered; no per-call telemetry flag is needed. Registering an OpenInference span processor has no effect on this path. | 