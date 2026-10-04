

# Integrating with the DevOps Agent A2A server
<a name="connecting-to-devops-agent-remote-servers-integrating-with-the-devops-agent-a2a-server"></a>

With the AWS DevOps Agent Agent-to-Agent (A2A) server, your autonomous agent can delegate operational work to the DevOps Agent over the [A2A v1.0 protocol](https://a2a-protocol.org/latest/specification/). Your agent discovers the DevOps Agent through an agent card, then sends messages to investigate incidents, review architecture, analyze costs, and map topology. The server implements the A2A v1.0 specification with the HTTP\+JSON binding.

This page describes the DevOps Agent's own A2A server. To connect the DevOps Agent as a client to a *remote* A2A agent that you host, see [Connecting Remote A2A Agents](configuring-integrations-and-knowledge-connecting-remote-a2a-agents.md) instead.

## Endpoint
<a name="endpoint"></a>

The A2A server is available at a regional URL. Replace `{region}` with your Agent Space's Region, for example `us-east-1`.

```
https://connect.aidevops.{region}.api.aws
```


| Operation | Method and path | 
| --- | --- | 
| Agent card discovery | GET /.well-known/agent-card.json | 
| SendMessage | POST /a2a/message:send | 
| SendStreamingMessage | POST /a2a/message:stream | 
| GetTask | GET /a2a/tasks/{id} | 
| ListTasks | GET /a2a/tasks | 
| CancelTask | POST /a2a/tasks/{id}:cancel | 
| SubscribeToTask | POST /a2a/tasks/{id}:subscribe | 

For the list of available Regions, see [Supported Regions](about-aws-devops-agent-supported-regions.md).

## Request headers
<a name="request-headers"></a>

Pass the following headers on A2A requests.


| Header | Required | Description | 
| --- | --- | --- | 
| A2A-Version | Yes | Must be 1.0. The server rejects a request that omits this header or sends another value with HTTP 400. | 
| Authorization | Yes | An access token (Bearer <access-token>) or an AWS Signature Version 4 (SigV4) signature. The mcp-proxy-for-aws proxy adds the SigV4 signature for you. | 
| X-Agent-Space-Id | SigV4 only | The target Agent Space ID. See the following section on tenancy for how the server resolves the Agent Space for each authentication method. | 
| Content-Type | Body only | application/json for a request that sends a body, such as message:send. | 

For token creation and SigV4 setup, see [Authentication and security](connecting-to-devops-agent-remote-servers-authentication-and-security.md).

## Agent card discovery
<a name="agent-card-discovery"></a>

Retrieve the agent card to discover the server's interfaces, security schemes, and skills.

```
GET https://connect.aidevops.{region}.api.aws/.well-known/agent-card.json
```

The card lists two `supportedInterfaces` entries, one per tenant, both using the `HTTP+JSON` binding at the `/a2a` base path. It also declares the `bearer` and `sigv4` security schemes and the `investigate` and `chat` skills, and reports `streaming: true` and `pushNotifications: false`.

## Tenancy
<a name="tenancy"></a>

The DevOps Agent A2A server is multi-tenant in two independent dimensions: the **Agent Space** a request runs against, and the **interface tenant** that selects between conversational chat and asynchronous investigation.

### Agent Space isolation
<a name="agent-space-isolation"></a>

Every A2A request runs against exactly one Agent Space, and the server uses the caller's own AWS credentials for all downstream work. Tasks, chats, and results created through one Agent Space are not visible from another.

How the server resolves the Agent Space depends on your authentication method.
+ **Access token (Bearer)** — The token is bound to a single Agent Space when it is created. The server resolves the Agent Space from the token, so you do not send the `X-Agent-Space-Id` header. If you include it, the server ignores it.
+ **AWS SigV4** — IAM credentials are not bound to an Agent Space. You must name the target Agent Space in the `X-Agent-Space-Id` request header. A SigV4 request that omits this header is rejected with HTTP 400 and the message `Agent space not resolved`. This lets one SigV4 client route across several Agent Spaces by changing the header per request.

### Interface tenant: chat and investigation
<a name="interface-tenant-chat-and-investigation"></a>

The agent card advertises two interfaces, distinguished by a `tenant` value. With the tenant value, you select which skill runs and which operations are available.


| Tenant | Skill | Behavior | Supported operations | 
| --- | --- | --- | --- | 
| chat | Operational Chat | Real-time conversational analysis for cost optimization, architecture review, topology mapping, and knowledge discovery. Returns a completed result in the response. | message:send, message:stream | 
| investigation | Incident Investigation | Deep asynchronous root cause analysis. Returns a working task immediately; the analysis takes 5–8 minutes. | message:send, then GetTask, ListTasks, CancelTask, or SubscribeToTask | 

Send the chosen tenant with the request. For `message:send` and `message:stream`, include it in the request body as a top-level `tenant` field. For `GetTask` and `ListTasks`, pass it as a `tenant` query parameter. For `CancelTask` and `SubscribeToTask`, pass it as a `tenant` field in the request body.

The tenant boundary is strict for follow-up operations. The investigation task operations (`GetTask`, `ListTasks`, `CancelTask`, `SubscribeToTask`) accept only the `investigation` tenant and reject a `chat` tenant with HTTP 400 (`UNSUPPORTED_TENANT`). Streaming (`message:stream`) accepts only the `chat` tenant; to stream an investigation's progress, start it with `message:send` and then call `SubscribeToTask`.

If you omit the `tenant` field, the server currently applies a compatibility fallback: `message:send` infers the tenant from keywords in your message text, and the other operations default to `investigation`. This fallback is temporary and exists only for migration. Always send an explicit `tenant` so routing stays deterministic.

## Skills
<a name="skills"></a>
+ **investigate** — Deep asynchronous root cause analysis for AWS incidents, such as ECS 503 errors, Lambda timeout spikes, or RDS connection exhaustion. Use the `investigation` tenant.
+ **chat** — Real-time conversational analysis for cost optimization, architecture review, topology mapping, and knowledge discovery. Use the `chat` tenant.

## Send a chat message
<a name="send-a-chat-message"></a>

The examples that follow use a Bearer access token for brevity. To use AWS SigV4 instead, replace the `Authorization: Bearer <access-token>` line with a SigV4-signed request and add the `X-Agent-Space-Id` header to name the target Agent Space. The request body and response are the same for both authentication methods. For setup, see [Authentication and security](connecting-to-devops-agent-remote-servers-authentication-and-security.md).

A chat request returns a completed task with the answer in its artifact. Replace `{region}` and `<access-token>` with your own values.

```
POST https://connect.aidevops.{region}.api.aws/a2a/message:send
A2A-Version: 1.0
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "tenant": "chat",
  "message": {
    "parts": [
      { "text": "Analyze cost optimization opportunities for account 123456789012" }
    ]
  }
}
```

The response is an A2A task in the `TASK_STATE_COMPLETED` state, with the answer text in the artifact parts.

```
{
  "task": {
    "id": "<execution-id>",
    "contextId": "<context-id>",
    "status": {
      "state": "TASK_STATE_COMPLETED",
      "timestamp": "2026-01-01T00:00:00.000Z"
    },
    "artifacts": [
      { "artifactId": "<artifact-id>", "parts": [{ "text": "..." }] }
    ]
  }
}
```

To continue a conversation, send the returned task ID as `taskId` in the next `message:send` request. Chat also supports `message:stream`, which returns the same content as a server-sent event stream and continues a conversation the same way: send the returned task ID as `taskId` in the next `message:stream` request.

## Start an investigation
<a name="start-an-investigation"></a>

An investigation request returns immediately with a working task. Poll `GetTask` or subscribe with `SubscribeToTask` for progress.

```
POST https://connect.aidevops.{region}.api.aws/a2a/message:send
A2A-Version: 1.0
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "tenant": "investigation",
  "message": {
    "parts": [
      { "text": "Investigate why my ECS service is returning 503 errors" }
    ]
  }
}
```

The response is a task in the `TASK_STATE_WORKING` state. The artifact text carries the task ID and execution ID.

```
{
  "task": {
    "id": "<task-id>",
    "contextId": "<context-id>",
    "status": {
      "state": "TASK_STATE_WORKING",
      "timestamp": "2026-01-01T00:00:00.000Z"
    },
    "artifacts": [
      { "artifactId": "<artifact-id>", "parts": [{ "text": "{\"type\":\"investigation_started\",\"taskId\":\"...\"}" }] }
    ]
  }
}
```

### Check investigation status
<a name="check-investigation-status"></a>

Use the returned task ID to poll for the latest state. Include the `investigation` tenant.

```
GET https://connect.aidevops.{region}.api.aws/a2a/tasks/{task-id}?tenant=investigation
A2A-Version: 1.0
Authorization: Bearer <access-token>
```

When the task reaches a terminal state, the response includes an `artifacts` array with the investigation result. Each terminal artifact carries an availability marker in its metadata, so a result that is still being written is reported as unavailable rather than as an error.

### Subscribe to investigation updates
<a name="subscribe-to-investigation-updates"></a>

For a live progress stream instead of polling, subscribe to the task. The subscription streams updates as server-sent events until the task reaches a terminal state.

```
POST https://connect.aidevops.{region}.api.aws/a2a/tasks/{task-id}:subscribe
A2A-Version: 1.0
Authorization: Bearer <access-token>
Content-Type: application/json

{ "tenant": "investigation" }
```

Subscribing to a task that has already reached a terminal state returns HTTP 400 (`UNSUPPORTED_OPERATION`). Use `GetTask` for a completed task.

## Task states
<a name="task-states"></a>

The server maps DevOps Agent task status to A2A v1.0 task states.


| A2A task state | Meaning | 
| --- | --- | 
| TASK\_STATE\_SUBMITTED | The task was accepted but has not started. | 
| TASK\_STATE\_WORKING | The task is in progress. | 
| TASK\_STATE\_COMPLETED | The task finished successfully. | 
| TASK\_STATE\_CANCELED | The task was canceled. | 
| TASK\_STATE\_FAILED | The task ended without completing, for example it failed, timed out, or was skipped. | 

## Errors
<a name="errors"></a>

Errors use the A2A v1.0 `google.rpc.Status` shape. Common cases follow.


| HTTP status | Reason | Cause | 
| --- | --- | --- | 
| 400 | INVALID\_ARGUMENT | A missing or invalid A2A-Version header, a missing message text, an unsupported tenant value, or a SigV4 request without X-Agent-Space-Id. | 
| 400 | UNSUPPORTED\_TENANT | The operation does not support the requested tenant, such as streaming an investigation or retrieving a chat task. | 
| 400 | UNSUPPORTED\_OPERATION | You subscribed to a task that is already in a terminal state. | 
| 401 | UNAUTHENTICATED | The credentials are missing, invalid, or expired. | 
| 404 | TASK\_NOT\_FOUND | No task exists for the given ID in the resolved Agent Space. | 
| 500 | INTERNAL\_ERROR | The task could not be executed. Retry the request. | 

For authentication troubleshooting, token lifecycle, and CloudTrail traceability, see [Authentication and security](connecting-to-devops-agent-remote-servers-authentication-and-security.md).