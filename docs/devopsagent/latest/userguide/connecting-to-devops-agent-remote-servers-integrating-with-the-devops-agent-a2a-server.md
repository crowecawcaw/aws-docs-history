

# Integrating with the DevOps Agent A2A server
<a name="connecting-to-devops-agent-remote-servers-integrating-with-the-devops-agent-a2a-server"></a>

The A2A endpoint implements the [A2A v1.0 specification](https://a2a-protocol.org/latest/specification/) using HTTP\+JSON binding.

## Request headers
<a name="request-headers"></a>

Pass the following headers on A2A requests.


| Header | Required | Description | 
| --- | --- | --- | 
| A2A-Version | Yes | Must be 1.0. The server rejects requests that omit it or send another value with HTTP 400. | 
| Authorization | Yes | Access token (Bearer <access-token>) or an AWS SigV4 signature. The mcp-proxy-for-aws proxy adds the SigV4 signature for you. | 
| X-Agent-Space-Id | SigV4 only | Target Agent Space ID. With SigV4, the server resolves the Agent Space from this header. With a Bearer token, the token identifies the Agent Space and the server ignores this header. | 
| Content-Type | Body only | application/json for requests that send a body, such as message:send. | 

For token creation and SigV4 setup, see [Authentication and security](connecting-to-devops-agent-remote-servers-authentication-and-security.md).

## Agent card discovery
<a name="agent-card-discovery"></a>

Retrieve the agent card at:

```
GET https://connect.aidevops.{region}.api.aws/.well-known/agent-card.json
```

## Supported operations
<a name="supported-operations"></a>
+ `SendMessage` – Send a message and receive a response.
+ `SendStreamingMessage` – Stream responses as they are generated.
+ `GetTask` – Check the status of an asynchronous task.
+ `ListTasks` – List tasks for an Agent Space.
+ `CancelTask` – Cancel a running task.
+ `SubscribeToTask` – Subscribe to task updates through server-sent events.

## Skills
<a name="skills"></a>
+ **investigate** – Deep asynchronous analysis of operational issues (5–8 minutes).
+ **chat** – Instant answers to operational questions.