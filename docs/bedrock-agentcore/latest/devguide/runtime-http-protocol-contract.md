# HTTP protocol contract

Understand the requirements for implementing the HTTP protocol in your agent
application. Use the HTTP protocol to create direct REST API endpoints for traditional
request/response patterns.

For example code, see [Get started with the Amazon Bedrock AgentCore starter
toolkit](runtime-get-started-toolkit.md "runtime-get-started-toolkit.md").

###### Topics

- [Container requirements](#container-requirements-http "#container-requirements-http")
- [Path requirements](#path-requirements-http "#path-requirements-http")

## Container requirements

Your agent must be deployed as a containerized application meeting these
specifications:

- **Host**: `0.0.0.0`
- **Port**: `8080` - Standard port
  for HTTP-based agent communication
- **Platform**: ARM64 container - Required for
  compatibility with the AgentCore Runtime environment

## Path requirements

### /invocations - POST

This is the primary agent interaction endpoint with JSON input and JSON/SSE
output.

###### Purpose

Receives incoming requests from users or applications and processes them
through your agent's business logic

###### Use cases

The `/invocations` endpoint serves several key purposes:

- Direct user interactions and conversations
- API integrations with external systems
- Batch processing of multiple requests
- Real-time streaming responses for long-running operations

###### Example Request format

```
Content-Type: application/json

{
  "prompt": "What's the weather today?"
}
```

###### Response formats

Your agent can respond using either of the following formats depending on
the use case:

#### JSON response (non-streaming)

###### Purpose

Provides complete responses for requests that can be processed
quickly

###### Use cases

JSON responses are ideal for:

- Simple question-answering scenarios
- Deterministic computations
- Quick data lookups
- Status confirmations

###### Example JSON response format

```
Content-Type: application/json

{
  "response": "Your agent's response here",
  "status": "success"
}
```

#### SSE response (streaming)

Server-sent events (SSE) let you deliver real-time streaming responses.
For more information, see the [Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events "https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events") specification.

###### Purpose

Enables incremental response delivery for long-running operations and
improved user experience

###### Use cases

SSE responses are ideal for:

- Real-time conversational experiences
- Progressive content generation
- Long-running computations with intermediate results
- Live data feeds and updates

###### Example SSE response format

```
Content-Type: text/event-stream

data: {"event": "partial response 1"}
data: {"event": "partial response 2"}
data: {"event": "final response"}
```

### /ping - GET

###### Purpose

Verifies that your agent is operational and ready to handle
requests

###### Use cases

The `/ping` endpoint serves several key purposes:

- Service monitoring to detect and remediate issues
- Automated recovery through AWS's managed infrastructure

###### Response format

Returns a status code indicating your agent's health:

- **Content-Type**:
  `application/json`
- **HTTP Status Code**: `200`
  for healthy, appropriate error codes for unhealthy states

If your agent needs to process background tasks, you can indicate it with the
`/ping` status. If the ping status is `HealthyBusy`,
the runtime session is considered active.

###### Example Ping response format

```
{
  "status": "<status_value>",
  "time_of_last_update": <unix_timestamp>
}
```

**status**

`Healthy` - System is ready to accept new work

`HealthyBusy` - System is operational but currently
busy with async tasks

**time_of_last_update**

Used to determine how long the system has been in its current
state
