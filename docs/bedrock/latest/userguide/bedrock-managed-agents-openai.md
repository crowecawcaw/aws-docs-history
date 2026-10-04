

# Amazon Bedrock Managed Agents, powered by OpenAI (preview)
<a name="bedrock-managed-agents-openai"></a>

Amazon Bedrock Managed Agents, powered by OpenAI, helps you build applications that run stateful agents with OpenAI models on Amazon Bedrock. You create a session, provide instructions and an execution environment, and submit messages. The service manages the agent's conversation and model interactions. Tools execute in the compute environment that you provide.

Use managed agents for tasks that require several steps, such as investigating a codebase, processing documents, or generating files. A session retains conversation context across messages. Skills provide reusable instructions, and Model Context Protocol (MCP) servers make additional tools available to the agent.

**Note**  
 **Preview** This feature is in public preview. Preview functionality and APIs can change. Review the [preview limitations](bedrock-managed-agents-openai-quotas-limitations.md) before building an application.

**Topics**
+ [How it works](#bedrock-managed-agents-openai-how-it-works)
+ [Choose an execution environment](#bedrock-managed-agents-openai-choose-an-execution-environment)
+ [Regional endpoints](#bedrock-managed-agents-openai-regional-endpoints)
+ [Next steps](#bedrock-managed-agents-openai-next-steps)
+ [Charges](#bedrock-managed-agents-openai-charges)
+ [Set up permissions and prerequisites](bedrock-managed-agents-openai-prerequisites.md)
+ [Run your first agent with self-hosted compute](bedrock-managed-agents-openai-self-hosted.md)
+ [Run your agent on Amazon Bedrock AgentCore Runtime](bedrock-managed-agents-openai-agentcore-runtime.md)
+ [Work with sessions, events, and results](bedrock-managed-agents-openai-sessions.md)
+ [Add skills and tools](bedrock-managed-agents-openai-skills-tools.md)
+ [Security and IAM roles](bedrock-managed-agents-openai-security.md)
+ [BMA preview REST API reference](bedrock-managed-agents-openai-api-reference.md)
+ [Preview availability and limitations](bedrock-managed-agents-openai-quotas-limitations.md)
+ [Troubleshooting](bedrock-managed-agents-openai-troubleshooting.md)
+ [Clean up example resources](bedrock-managed-agents-openai-cleanup.md)

## How it works
<a name="bedrock-managed-agents-openai-how-it-works"></a>

The principal components are:
+  **Session** — A stateful conversation with an agent. A session specifies a model, instructions, tools, an IAM role, and an execution environment.
+  **Turn** — The work performed in response to a submitted message. A turn can include reasoning, tool calls, and generated output.
+  **Execution environment** — Customer-provided compute where commands and local tools run. Use your own host or Amazon Bedrock AgentCore Runtime.
+  **Exec server** — The `codex exec-server` process that connects the execution environment to BMA. It makes an outbound connection to the service.
+  **Items and events** — Items contain durable conversation output. The event stream reports progress as work occurs.
+  **Session role** — An IAM role that BMA assumes for authorized operations on your behalf, including model inference and, when configured, AgentCore Runtime activation.

<a name="bedrock-managed-agents-openai-architecture"></a>![Your application calls BMA, which invokes an OpenAI model on Amazon Bedrock and exchanges tool requests and results with your execution environment.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/bma-architecture.png)


The service-managed conversation and the execution environment's files have separate lifecycles. Deleting a BMA session does not delete files that you store in your own S3 buckets or on your own host.

## Choose an execution environment
<a name="bedrock-managed-agents-openai-choose-an-execution-environment"></a>


|  Option  |  What you provide  |  When to use it  | 
| --- | --- | --- | 
| Self-hosted compute | A host, workspace, network access, and a running exec server | You want to use an existing development machine, container, or compute environment. | 
| AgentCore Runtime | An AgentCore Runtime containing the exec server and its adapter | You want managed runtime sessions and configurable storage in your AWS account. | 

The supplied [example bundle](samples/bma-examples.zip) includes both options. The self-hosted CDK application creates IAM roles; it does not create a host. The AgentCore CDK application creates a Runtime, storage, and networking.

## Regional endpoints
<a name="bedrock-managed-agents-openai-regional-endpoints"></a>

Use an endpoint in a supported AWS Region. Sign requests with the endpoint's Region and the signing service `bedrock-mantle`.


|  AWS Region  |  Region code  |  Endpoint  | 
| --- | --- | --- | 
| US East (N. Virginia) |  `us-east-1`  |  `https://bedrock-mantle.us-east-1.api.aws`  | 
| US West (Oregon) |  `us-west-2`  |  `https://bedrock-mantle.us-west-2.api.aws`  | 
| US East (Ohio) |  `us-east-2`  |  `https://bedrock-mantle.us-east-2.api.aws`  | 

The preview uses the `bedrock-mantle` endpoint. BMA session operations use the `/openai/v1/agents/sessions` path. Model discovery uses `/v1/models`. Model availability can differ by Region and account.

## Next steps
<a name="bedrock-managed-agents-openai-next-steps"></a>

1.  [Set up permissions and prerequisites](bedrock-managed-agents-openai-prerequisites.md).

1. Run your first agent with [self-hosted compute](bedrock-managed-agents-openai-self-hosted.md) or [AgentCore Runtime](bedrock-managed-agents-openai-agentcore-runtime.md).

1.  [Work with sessions and results](bedrock-managed-agents-openai-sessions.md), then [add skills and tools](bedrock-managed-agents-openai-skills-tools.md).

## Charges
<a name="bedrock-managed-agents-openai-charges"></a>

You incur charges for model inference and the AWS resources that your application uses. The AgentCore example also creates storage and networking resources, including a NAT gateway. A deployed stack can continue to incur charges when no BMA turn is running. See [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) and [Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/), and [clean up the examples](bedrock-managed-agents-openai-cleanup.md) when you finish.