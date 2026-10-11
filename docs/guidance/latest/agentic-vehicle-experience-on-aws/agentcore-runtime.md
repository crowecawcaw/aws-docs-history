

# Amazon Bedrock AgentCore runtime
<a name="agentcore-runtime"></a>

Amazon Bedrock AgentCore is the managed container runtime that hosts the AVX supervisor agent. It handles container lifecycle, WebSocket connection management, SigV4 authentication, and session multiplexing, freeing the agent code to focus on orchestration.

## Two runtime modes
<a name="two-runtime-modes"></a>

AVX deploys two AgentCore runtimes from the same supervisor code base:


| Runtime mode | Transport | Use case | 
| --- | --- | --- | 
|  **Bidirectional voice** (bidi) | WebSocket — persistent bidirectional stream | Amazon Connect voice, iOS/mobile companion app, hands-free driver experience | 
|  **Text / HTTP**  | HTTP unary — request/response | Web chat, CMS Fleet Intelligence portal `/assistant/chat` route, API integrations | 

Both runtimes share the same supervisor agent logic and tool catalog; the difference is the Strands model class (`BidiNovaSonicModel` for voice, `BedrockModel` for text) and the entry-point file.

## Runtime entry point pattern
<a name="runtime-entry-point-pattern"></a>

The AgentCore runtime is wired through the Strands `BedrockAgentCoreApp` decorator:

```
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

@app.entrypoint                    
def handler(payload, context):     
    session_id = getattr(context, 'session_id', 'default')
    user_message = payload.get('prompt', '')
    # ... agent orchestration ...
    return str(result)

app.run()
```

The `@app.entrypoint` decorator registers the function with the AgentCore runtime.

The `context` parameter name is mandatory — the SDK inspects parameter names by position. Using any other name (for example, `ctx`) causes a `TypeError` at runtime.

For the bidi voice runtime the entry point uses `@app.websocket` instead, and the handler receives raw WebSocket frames rather than a payload dict. The `BidiAgent.run(inputs, outputs)` pump manages the bidirectional audio/transcript stream.

## Execution role and IAM grants
<a name="execution-role-and-iam-grants"></a>

The AgentCore execution role must trust `bedrock-agentcore.amazonaws.com` and carry grants for every AWS API the agent invokes at runtime. Key grants for AVX:


| Grant | Purpose | 
| --- | --- | 
|  `bedrock:InvokeModel` \+ `bedrock:InvokeModelWithResponseStream` on the supervisor inference profile and its underlying foundation-model ARNs | Strands `ConverseStream` calls for both the supervisor LLM and Nova 2 Sonic bidi | 
|  `bedrock:InvokeModelWithBidirectionalStream` on the Nova 2 Sonic foundation-model ARN (us-east-1) | Bidirectional audio streaming to Nova 2 Sonic | 
|  `bedrock-agent-runtime:Retrieve` on the ADP Knowledge Base ARN | Cross-account RAG grounding for reference tools | 
|  `bedrock-agentcore:CreateEvent`, `BatchCreateMemoryRecords`, `RetrieveMemoryRecords`  | AgentCore Memory LTM reads and writes for session grounding | 
|  `athena:StartQueryExecution`, `GetQueryExecution`, `GetQueryResults` on the AVX Athena workgroup | Cross-region ADP data-lake queries at session-init time | 
|  `lakeformation:GetDataAccess` on `*`  | Lake Formation credential vending for S3 access gated by column/row filters | 
|  `dynamodb:GetItem`, `PutItem`, `Query` on CMS tables | Live vehicle state and booking writes | 

**Note**  
Foundation-model ARNs carry no account ID (`arn:aws:bedrock:<region>::foundation-model/<id>`). Cross-region inference-profile ARNs require the account ID (`arn:aws:bedrock:<region>:<account>:inference-profile/<id>`). Both forms must be present in the IAM policy for Strands `ConverseStream` to succeed.

## Deployment
<a name="deployment"></a>

AVX uses the `agentcore` CLI from the AgentCore starter toolkit:

```
agentcore configure -e agents/supervisor/agentcore_app.py
agentcore deploy --auto-update-on-conflict \
  --env CMS_STAGE=staging \
  --env VSA_STAGE=staging \
  --env AWS_REGION=us-west-2 \
  --env NOVA_SONIC_REGION=us-east-1
```

The `--auto-update-on-conflict` flag updates an existing runtime in place (idempotent by runtime name). Environment variables injected via `--env` are available to the handler as `os.environ` values. The CDK stack (`vsa-staging-core`) provisions the execution role and supporting infrastructure; the AgentCore runtime itself is provisioned by the CLI outside CDK.