The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Tools Reference

The Partner Central Agent MCP Server exposes two MCP tools: `sendMessage` for all agent
interactions, and `getSession` for retrieving session state. All Partner Central
operations — opportunity queries, funding applications, document analysis — are handled
through natural language via `sendMessage`.

## Tools overview

| Tool          | Description                                                                                                                  | Category     |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `sendMessage` | Send messages to the Partner Central AI agent. Supports text, file attachments, and<br>human-in-the-loop approval responses. | Read / Write |
| `getSession`  | Retrieve session state including conversation history, events, and<br>metadata.                                              | Read-only    |

## `sendMessage`

Primary tool for all Partner Central AI agent interactions. Use this tool to ask questions,
request actions, attach documents for analysis, and respond to approval requests for write
operations.

The agent maintains conversation context within a session, so you can ask follow-up
questions without repeating prior context.

### Parameters

- `content` (required) — Array of content blocks. Each block must
  include a `type` field that determines the block structure. You can include
  multiple blocks in a single message (e.g., text + document attachment).

Content block types:

| Type                     | Fields                                                                                    | Description                                                                                    |
| ------------------------ | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `text`                   | `type` (required), `text` (required)                                                      | User message text sent to the agent                                                            |
| `document`               | `type` (required), `filename` (required),<br>`s3Uri` (required)                           | File attachment for the agent to analyze. The `s3Uri` must<br>include a `versionId` parameter. |
| `tool_approval_response` | `type` (required), `toolUseId` (required),<br>`decision` (required), `message` (optional) | Response to a human-in-the-loop approval request                                               |

- `catalog` (required) — Target environment for the
  operation.

Valid values: `"AWS"` (production), `"Sandbox"`
(testing)

- `sessionId` (optional) — UUID v4 identifying an existing
  session to continue. Omit to create a new session. Format:
  `session-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.

Default: A new session is created automatically.

- `stream` (optional) — Enable Server-Sent Events (SSE) streaming
  for real-time response delivery.

Valid values: `true`, `false`

Default: `false`

### Response

The response includes:

| Field       | Description                                                           |
| ----------- | --------------------------------------------------------------------- |
| `sessionId` | Session identifier for follow-up messages                             |
| `status`    | Response status: `"complete"`,<br>`"requires_approval"`, or `"error"` |
| `content`   | Array of response content blocks from the agent                       |

### Examples

#### Basic text message (new session)

Request:

```
{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "content": [
                {
                    "type": "text",
                    "text": "List my open opportunities with expected close date in Q1 2026"
                }
            ],
            "catalog": "AWS"
        }
    }
}
```

Response:

```
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "I found 12 open opportunities with expected close dates in Q1 2026. Here's a summary:\n\n1. **O1234567890** - Acme Corp Cloud Migration - $250,000 - Qualified stage\n2. **O1234567891** - GlobalTech Data Analytics - $180,000 - Prospect stage\n..."
            }
        ],
        "sessionId": "session-550e8400-e29b-41d4-a716-446655440000",
        "status": "complete"
    }
}
```

#### Follow-up message (existing session)

Request:

```
{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "sessionId": "session-550e8400-e29b-41d4-a716-446655440000",
            "content": [
                {
                    "type": "text",
                    "text": "Tell me more about O1234567890. Is it ready for submission?"
                }
            ],
            "catalog": "AWS"
        }
    }
}
```

#### File attachment

Upload a document to S3 first, then reference it in the message:

```
{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "sessionId": "session-550e8400-e29b-41d4-a716-446655440000",
            "content": [
                {
                    "type": "text",
                    "text": "Review this customer proposal and suggest which opportunity it aligns with"
                },
                {
                    "type": "document",
                    "filename": "acme-proposal.pdf",
                    "s3Uri": "s3://aws-partner-central-marketplace-ephemeral-writeonly-files/123456789012/acme-proposal.pdf?versionId=abc123def456"
                }
            ],
            "catalog": "AWS"
        }
    }
}
```

File upload constraints:

- Maximum 3 files per message
- Image size limit: 3.75 MB
- Document size limit: 4.5 MB
- Allowed extensions: `doc`, `docx`,
  `pdf`, `png`, `jpeg`, `xlsx`,
  `csv`, `txt`
- Files must be uploaded to
  `s3://{bucket}/{your-aws-account-id}/`
- The S3 URI must include the `versionId` query
  parameter

### Human-in-the-loop approval workflow

When the agent needs to perform a write operation (e.g., update an opportunity, submit
a funding application), it returns a `"requires_approval"` status with the
proposed action details. You must respond with a `tool_approval_response`
content block.

**Step 1 — Agent requests approval:**

```
{
    "jsonrpc": "2.0",
    "id": 4,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "I'd like to update opportunity O1234567890 with the following changes:\n- Target close date: 2026-03-31\n- Expected revenue: $300,000\n- Stage: Qualified\n\nPlease approve, reject, or override this action."
            },
            {
                "type": "tool_approval_request",
                "toolUseId": "tool-use-98765",
                "toolName": "update_opportunity_enhanced",
                "parameters": {
                    "opportunityId": "O1234567890",
                    "targetCloseDate": "2026-03-31",
                    "expectedRevenue": 300000,
                    "stage": "Qualified"
                }
            }
        ],
        "sessionId": "session-550e8400-e29b-41d4-a716-446655440000",
        "status": "requires_approval"
    }
}
```

**Step 2 — Approve the action:**

```
{
    "jsonrpc": "2.0",
    "id": 5,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "sessionId": "session-550e8400-e29b-41d4-a716-446655440000",
            "content": [
                {
                    "type": "tool_approval_response",
                    "toolUseId": "tool-use-98765",
                    "decision": "approve"
                }
            ],
            "catalog": "AWS"
        }
    }
}
```

**Step 2 (alternative) — Reject the action:**

```
{
    "jsonrpc": "2.0",
    "id": 5,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "sessionId": "session-550e8400-e29b-41d4-a716-446655440000",
            "content": [
                {
                    "type": "tool_approval_response",
                    "toolUseId": "tool-use-98765",
                    "decision": "reject",
                    "message": "The expected revenue should be $250,000, not $300,000"
                }
            ],
            "catalog": "AWS"
        }
    }
}
```

**Step 2 (alternative) — Override with custom
response:**

```
{
    "jsonrpc": "2.0",
    "id": 5,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "sessionId": "session-550e8400-e29b-41d4-a716-446655440000",
            "content": [
                {
                    "type": "tool_approval_response",
                    "toolUseId": "tool-use-98765",
                    "decision": "override",
                    "message": "Use expected revenue of $250,000 and keep the stage as Prospect instead"
                }
            ],
            "catalog": "AWS"
        }
    }
}
```

Approval decision values:

| Decision     | Behavior                                                            |
| ------------ | ------------------------------------------------------------------- |
| `"approve"`  | Execute the tool with the proposed parameters                       |
| `"reject"`   | Do not execute the tool. Optional `message` explains<br>why.        |
| `"override"` | Provide a custom response or modified instructions via<br>`message` |

### Streaming with SSE

Enable streaming to receive incremental response chunks as the agent processes your
request:

Request:

```
{
    "jsonrpc": "2.0",
    "id": 6,
    "method": "tools/call",
    "params": {
        "name": "sendMessage",
        "arguments": {
            "sessionId": "session-550e8400-e29b-41d4-a716-446655440000",
            "content": [
                {
                    "type": "text",
                    "text": "Analyze my pipeline and identify opportunities at risk"
                }
            ],
            "catalog": "AWS",
            "stream": true
        }
    }
}
```

The server responds with a stream of SSE events:

```
event: stream_start
data: {"sessionId": "session-550e8400-e29b-41d4-a716-446655440000"}

event: assistant-response.start
data: {}

event: server-tool-use
data: {"toolName": "analyze_pipeline", "parameters": {}}

event: server-tool-response
data: {"toolName": "analyze_pipeline", "result": {"opportunitiesAnalyzed": 47, "atRisk": 5}}

event: assistant-response.delta
data: {"text": "I analyzed your pipeline of 47 opportunities and identified "}

event: assistant-response.delta
data: {"text": "5 that are at risk of slipping:\n\n"}

event: assistant-response.delta
data: {"text": "1. **O2345678901** - Close date is past due by 15 days\n"}

event: assistant-response.completed
data: {"status": "complete"}

event: stream_end
data: {}
```

## `getSession`

Retrieve the current state of a conversation session, including full conversation
history, events, and metadata. Use this to inspect session state, review past interactions,
or resume a conversation.

### Parameters

- `sessionId` (required) — UUID of the session to retrieve.
  Format: `session-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.
- `catalog` (required) — Environment the session belongs
  to.

Valid values: `"AWS"`, `"Sandbox"`

### Response

| Field            | Type    | Description                                                              |
| ---------------- | ------- | ------------------------------------------------------------------------ |
| `sessionId`      | string  | Session identifier                                                       |
| `createdAt`      | string  | ISO 8601 timestamp of session creation                                   |
| `lastActivity`   | string  | ISO 8601 timestamp of last activity                                      |
| `sequenceNumber` | integer | Current event sequence number                                            |
| `stateType`      | string  | Current session state                                                    |
| `events`         | array   | Full conversation history (user messages, agent responses, tool<br>uses) |
| `variables`      | object  | Session variables and metadata                                           |
| `eventCount`     | integer | Total number of events in the session                                    |

### Example

Request:

```
{
    "jsonrpc": "2.0",
    "id": 7,
    "method": "tools/call",
    "params": {
        "name": "getSession",
        "arguments": {
            "sessionId": "session-550e8400-e29b-41d4-a716-446655440000",
            "catalog": "AWS"
        }
    }
}
```

Response:

```
{
    "jsonrpc": "2.0",
    "id": 7,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "{\"sessionId\":\"session-550e8400-e29b-41d4-a716-446655440000\",\"createdAt\":\"2026-01-15T10:30:00Z\",\"lastActivity\":\"2026-01-15T11:45:00Z\",\"sequenceNumber\":8,\"stateType\":\"END_TURN\",\"eventCount\":8,\"events\":[...],\"variables\":{}}"
            }
        ]
    }
}
```

## Error handling

All errors follow the JSON-RPC 2.0 error format:

```
{
    "jsonrpc": "2.0",
    "id": 1,
    "error": {
        "code": -32001,
        "message": "Authentication failed. Verify your SigV4 credentials and ensure they have not expired."
    }
}
```

See [Error codes](mcp-configuration-reference.md#mcp-config-error-codes "mcp-configuration-reference.md#mcp-config-error-codes") for the complete list of error codes and
their meanings.

**Recommended retry strategy**

- For `-32004` (LIMIT\_EXCEEDED): Retry with exponential backoff
  starting at 1 second
- For `-32603` (INTERNAL\_ERROR): Retry up to 3 times with
  exponential backoff
- For `-32001` (AUTHENTICATION\_FAILURE): Refresh credentials and
  retry
- For all other errors: Do not retry automatically — inspect the error message
  and correct the request
