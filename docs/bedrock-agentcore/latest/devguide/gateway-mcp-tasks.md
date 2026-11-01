

# Use tasks with your AgentCore gateway
<a name="gateway-mcp-tasks"></a>

AgentCore Gateway supports the MCP Tasks extension (`io.modelcontextprotocol/tasks`) on protocol version `2026-07-28`, using the polling model. With tasks, a long-running tool on an MCP server target can return a task ID immediately instead of holding the connection open, and the client polls for the result. Without tasks, a synchronous tool call through the gateway is limited by the 15-minute gateway invocation timeout.

This topic describes how the gateway handles tasks. For the task lifecycle, the task object, and the full method definitions, see [Tasks extension](https://tasks.extensions.modelcontextprotocol.io/) on the Model Context Protocol website.

## Prerequisites
<a name="gateway-mcp-tasks-prereqs"></a>

To use tasks with your gateway, you must have:
+  **Protocol version `2026-07-28` ** — Your gateway’s `supportedVersions` must include `2026-07-28`.
+  **An MCP server target** — Tasks are supported on MCP server targets.
+  **A client that declares the tasks extension** — The client places `io.modelcontextprotocol/tasks` in `params._meta["io.modelcontextprotocol/clientCapabilities"].extensions` on each `tools/call` that can return a task, and on each `tasks/get`, `tasks/update`, and `tasks/cancel` request, as the Tasks extension specification requires.

Tasks work without MCP sessions or response streaming, so you can skip `sessionConfiguration` and don’t need to set `streamingConfiguration.enableResponseStreaming`. After the gateway returns a task ID, the connection closes, and your client retrieves the result with plain request/response polling.

## How the gateway handles a task
<a name="gateway-mcp-tasks-flow"></a>

1. The client sends `tools/call` with the tasks extension declared in `_meta`. The gateway forwards the declaration to the target.

1. If the target returns a task, the gateway replaces the target’s task ID with a **gateway task ID** and returns the task to the client. The client never sees the target’s own task ID. If the target returns a result instead, the gateway passes it through unchanged.

1. The client sends `tasks/get`, `tasks/update`, and `tasks/cancel` with that task ID. The gateway sends each request to the MCP server target that created the task and returns the target’s response with the same task ID.

Your MCP server target runs the work and reports the task’s status, result, `ttlMs`, and `pollIntervalMs`. The gateway relays them to your client unchanged. Your client polls with `tasks/get` until the task finishes.

The gateway advertises the tasks extension in `server/discover` (`capabilities.extensions`). Discovery is optional; whether a call can become a task depends on the per-request declaration and on the target.

## Supported methods
<a name="gateway-mcp-tasks-methods"></a>

The following table describes how the gateway handles each task method.


| Method | Gateway behavior | 
| --- | --- | 
|  `tools/call`  | Returns the task with a task ID issued by the gateway, or the tool result if the target answers synchronously. | 
|  `tasks/get`  | Relays the target’s task status, and the result once the task is complete. | 
|  `tasks/update`  | Relays the client’s input to the target when the task is waiting for input. | 
|  `tasks/cancel`  | Relays the cancellation request. Cancellation is cooperative: the target might still finish the work. | 

## Request headers for follow-up requests
<a name="gateway-mcp-tasks-mcp-name"></a>

On `tasks/get`, `tasks/update`, and `tasks/cancel`, send the gateway task ID in `params.taskId` and set the `Mcp-Name` header to the same task ID. The gateway routes the request from `params.taskId`. When it forwards the request to the target, the gateway sets `Mcp-Name` to the target’s own task ID.

## Guidance for MCP server target developers
<a name="gateway-mcp-tasks-target-developers"></a>
+ Return a task only when the request declares the tasks extension in `_meta`.
+ Keep your task IDs at or below 1,024 bytes. If a task ID is longer, the gateway cannot issue a gateway task ID for it, and the client receives the task without a `taskId` and cannot poll it.
+ Own the task lifetime. The gateway does not expire tasks, so set `ttlMs` and clean up tasks on your side.

## Error handling
<a name="gateway-mcp-tasks-errors"></a>

The following table describes the errors that the gateway returns for task requests.


| Scenario | Error | Description | 
| --- | --- | --- | 
| Invalid or unknown task ID | JSON-RPC `-32602` (Invalid params) | The task ID in `params.taskId` is not a valid task ID for this gateway and caller, or the tool or target that created the task no longer exists. | 
| Internal error | JSON-RPC `-32603` (Internal error) | The gateway or target encountered an internal error while handling the request. | 

Errors that the target returns are relayed to the client. For example, if the target no longer has the task (because it expired or was deleted), or if the target rejects the request with `-32021` (Missing required client capability), the client receives the target’s error. The gateway relays a task’s `completed` and `failed` outcomes as the target reports them and does not reclassify one as the other.

## Security
<a name="gateway-mcp-tasks-security"></a>

Gateway task IDs are opaque and scoped to a single gateway. AgentCore Gateway validates each task ID it receives and rejects any ID that was modified or issued by a different gateway.

 **Caller binding.** On gateways that use JSON Web Token (JWT) inbound authorization (`CUSTOM_JWT`) or IAM identity inbound authorization (`AWS_IAM`), each task is bound to the caller that created it. The binding is at principal granularity: the IAM principal ARN for IAM identity authorization (for an assumed role, the role ARN), and the JWT subject and issuer for JWT authorization. If a JWT lacks a subject or an issuer claim, the binding uses its client ID, so all callers that use the same app client share tasks. Callers with the same IAM principal or the same JWT subject and issuer (or, in the fallback case, the same client ID) are the same caller. Credential refresh and role-session rotation don’t affect the binding, but changing the gateway’s inbound authorization type mid-task can make existing task IDs unusable. For more information, see [Set up inbound authorization for your gateway](gateway-inbound-auth.md).

**Important**  
On gateways that use **Authenticate only** (`AUTHENTICATE_ONLY`) or **No authorization** (`NONE`), the gateway does not bind tasks to a caller, so a task ID works as a bearer token for anyone who holds it. For more information, see [Offloaded inbound authorization](gateway-inbound-auth.md#gateway-inbound-auth-offloaded).

The gateway does not expire task IDs or cap task duration. Task lifetime is controlled by the target.

 **Mid-task input.** When a task needs input, the request appears in the `tasks/get` response and the client answers with `tasks/update`. Treat this input with the same trust model as a direct elicitation or sampling request. For guidance, see [Securing the request state for elicitation and sampling](gateway-target-MCPservers.md#gateway-target-MCPservers-request-state).

## Code samples
<a name="gateway-mcp-tasks-examples"></a>

This example shows the JSON-RPC bodies for a task through AgentCore Gateway. Send each request to your gateway’s MCP endpoint (for example, `https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp`) with your `Authorization` header and `MCP-Protocol-Version: 2026-07-28`. On `tools/call`, set the `Mcp-Method` and `Mcp-Name` headers as for any `2026-07-28` tool call. On the follow-ups, set `Mcp-Name` to the task ID. Task IDs are long, opaque strings; treat them as opaque and URL-encode them if you place one in a URL.

 **Call the tool, declaring the tasks extension.** 

```
{
  "jsonrpc": "2.0",
  "id": "tool-call-1",
  "method": "tools/call",
  "params": {
    "name": "compile_annual_audit",
    "arguments": {
      "fiscalYear": 2026
    },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {
        "extensions": {
          "io.modelcontextprotocol/tasks": {}
        }
      }
    }
  }
}
```

The target returns a task, and the gateway returns it with a gateway task ID.

```
{
  "jsonrpc": "2.0",
  "id": "tool-call-1",
  "result": {
    "resultType": "task",
    "taskId": "EXAMPLE-OPAQUE-GATEWAY-TASK-ID",
    "status": "working",
    "createdAt": "2026-10-16T18:04:22Z",
    "lastUpdatedAt": "2026-10-16T18:04:22Z",
    "ttlMs": 7200000,
    "pollIntervalMs": 5000
  }
}
```

 **Poll with the gateway task ID** until the task reaches a terminal status, declaring the tasks extension again. `tasks/update` and `tasks/cancel` take the same `params.taskId` and `_meta`.

```
{
  "jsonrpc": "2.0",
  "id": "poll-9",
  "method": "tasks/get",
  "params": {
    "taskId": "EXAMPLE-OPAQUE-GATEWAY-TASK-ID",
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {
        "extensions": {
          "io.modelcontextprotocol/tasks": {}
        }
      }
    }
  }
}
```

```
{
  "jsonrpc": "2.0",
  "id": "poll-9",
  "result": {
    "resultType": "complete",
    "taskId": "EXAMPLE-OPAQUE-GATEWAY-TASK-ID",
    "status": "completed",
    "createdAt": "2026-10-16T18:04:22Z",
    "lastUpdatedAt": "2026-10-16T19:38:40Z",
    "ttlMs": 7200000,
    "result": {
      "content": [
        {
          "type": "text",
          "text": "Annual audit report compiled. 142 pages, 3 findings."
        }
      ],
      "isError": false
    }
  }
}
```