# Amazon Bedrock AgentCore Runtime targets

You can add an Amazon Bedrock AgentCore Runtime agent as a gateway target. The gateway sends traffic directly to the runtime agent without aggregation or protocol translation. Unlike MCP targets that combine tool capabilities into a unified virtual MCP server, the AgentCore Runtime target forwards requests and responses between clients and the runtime agent without modification.

###### Note

AgentCore Runtime targets for Gateway are in public preview. Features and APIs may change before general availability.

Adding an AgentCore Runtime target to your gateway is useful when you want to:

- Provide centralized access management for your runtime agents through a single gateway endpoint.
- Use the gateway’s built-in authentication and observability for your runtime agents.
- Route requests to specific runtime agents using path-based routing when multiple targets are attached to a gateway.
- Optimize your agent’s performance by using Amazon Bedrock AgentCore optimization to generate recommendations from agent traces, A/B test changes with live traffic through the gateway, and deploy winning configurations. For more information, see [AgentCore optimization](optimization.md "optimization.md").

###### Topics

- [Key considerations and limitations](#gateway-target-http-runtime-considerations "#gateway-target-http-runtime-considerations")
- [Target configuration](#gateway-target-http-runtime-config "#gateway-target-http-runtime-config")
- [Invoking an AgentCore Runtime target](#gateway-target-http-runtime-invoke "#gateway-target-http-runtime-invoke")
- [Outbound authorization](#gateway-target-http-runtime-auth "#gateway-target-http-runtime-auth")
- [Capability comparison with MCP targets](#gateway-target-http-runtime-comparison "#gateway-target-http-runtime-comparison")

## Key considerations and limitations

When working with AgentCore Runtime targets, be aware of the following considerations:

- The gateway sends traffic directly to AgentCore Runtime targets without aggregating capabilities.
- AgentCore Runtime targets can be added to gateways that don’t have a protocol type set. They cannot be added to MCP protocol type gateways.
- No capability synchronization or semantic tool search is available for AgentCore Runtime targets. Clients must address each target individually through path-based routing.
- Server-Sent Events (SSE) streaming is supported for AgentCore Runtime targets.
- Request interceptor Lambda functions are supported. Response interceptor Lambda functions with payload are not supported in the initial release due to SSE streaming incompatibility.

## Target configuration

When you create an AgentCore Runtime target, you provide the runtime ARN and an optional qualifier. The gateway resolves the runtime endpoint internally, so you don’t need to construct the runtime URL yourself.

The target configuration for an AgentCore Runtime target uses the following structure:

```
{
    "http": {
        "agentcoreRuntime": {
            "arn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/RUNTIME_ID",
            "qualifier": "DEFAULT"
        }
    }
}
```

- **arn** (required) – The ARN of the Amazon Bedrock AgentCore Runtime agent.
- **qualifier** (optional) – The runtime qualifier. Defaults to `DEFAULT`.

## Invoking an AgentCore Runtime target

To invoke an AgentCore Runtime target through the gateway, send a POST request to the target’s invocation URL. The URL format is:

```
https://{gatewayId}.gateway.bedrock-agentcore.{region}.amazonaws.com/{targetName}/invocations
```

Replace `{gatewayId}` with your gateway ID, `{region}` with the AWS Region, and `{targetName}` with the name of the target.

The following example uses curl to invoke an AgentCore Runtime target:

```
curl -X POST https://gateway-id.gateway.bedrock-agentcore.us-west-2.amazonaws.com/my-target/invocations \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <token>" \
    -d '{"input": {"prompt": "Hello"}}'
```

You can also use the Amazon Bedrock AgentCore SDK with an endpoint URL override:

```
aws bedrock-agentcore invoke-agent-runtime \
    --endpoint-url https://gateway-id.gateway.bedrock-agentcore.us-west-2.amazonaws.com/my-target \
    --runtimeArn arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/RUNTIME_ID
```

## Outbound authorization

AgentCore Runtime targets support the following outbound authorization types:

- **IAM (SigV4)** – The gateway assumes the gateway service role to obtain credentials for signing requests to the runtime target. When you configure IAM authorization, you can use IAM policies to restrict access exclusively to the gateway role, ensuring all runtime requests flow through the gateway.
- **Caller IAM credentials** – The gateway uses the caller’s IAM credentials to sign requests to the runtime target. The gateway assumes a role on behalf of the caller and signs the outbound request with the caller’s identity.
- **OAuth (JWT)** – The gateway retrieves OAuth tokens from credential providers configured in the target through the Amazon Bedrock AgentCore identity service.
- **Token passthrough** – The gateway validates the inbound token and passes it through to the runtime target without modification. This is useful when the runtime handles its own authorization.

## Capability comparison with MCP targets

You can integrate MCP servers with the Amazon Bedrock AgentCore gateway using two approaches: using the MCP target type in aggregation mode, or using the AgentCore Runtime target type. The following table compares the capabilities of each approach.

| Capability                  | MCP gateway with MCP targets                                                                                                               | AgentCore Runtime target                                                                                                                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tool/capability aggregation | Aggregates capabilities from all MCP targets into a single unified virtual MCP server. Clients see one consolidated `tools/list` response. | Operates in isolation. The gateway sends traffic directly to the target without merging capabilities. Clients must address each target individually through path-based routing.                                           |
| Semantic tool search        | Indexes tool descriptions and enables discovery through natural-language queries.                                                          | Not available. The gateway does not ingest or index capabilities. Clients must know exact tool names or use the server’s own `tools/list`.                                                                                |
| Response interceptor Lambda | Supports both request and response interceptors for non-streaming MCP operations.                                                          | Response interceptor Lambda with payload is not supported in the initial release due to SSE streaming incompatibility. Only request interceptor Lambda functions and response interceptors without payload are supported. |
