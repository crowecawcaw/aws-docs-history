

# BMA preview REST API reference
<a name="bedrock-managed-agents-openai-api-reference"></a>

This reference describes the session, event, and item operations used by the preview examples. Use an AWS SigV4-signed request to the regional `bedrock-mantle` endpoint. The signing service is `bedrock-mantle`.

## Operations
<a name="bedrock-managed-agents-openai-api-reference-operations"></a>


|  Operation  |  Method and path  |  Successful response  | 
| --- | --- | --- | 
| Create a session |  `POST /openai/v1/agents/sessions`  | Session resource | 
| List sessions |  `GET /openai/v1/agents/sessions`  | Paginated session list | 
| Retrieve a session |  `GET /openai/v1/agents/sessions/{session_id}`  | Session resource | 
| Delete a session |  `DELETE /openai/v1/agents/sessions/{session_id}`  | Deletion acknowledgement | 
| Submit input events |  `POST /openai/v1/agents/sessions/{session_id}/events`  | Acceptance acknowledgement; the body can be empty | 
| Stream events |  `GET /openai/v1/agents/sessions/{session_id}/events`  |  `text/event-stream`  | 
| List items |  `GET /openai/v1/agents/sessions/{session_id}/items`  | Paginated item list | 

Use the IDs returned by the service. Treat session IDs, environment IDs, turn IDs, and pagination cursors as opaque values.

## Create a session
<a name="bedrock-managed-agents-openai-api-reference-create-a-session"></a>

### Request
<a name="bedrock-managed-agents-openai-api-reference-request"></a>

```
POST /openai/v1/agents/sessions
Content-Type: application/json
```

```
{
  "agent": {
    "model": "openai.gpt-5.6-luna",
    "instructions": "Use the workspace tools to complete the user's task."
  },
  "environment": {
    "type": "self_hosted",
    "workspace_directory": "/path/to/workspace",
    "capability_directories": ["/path/to/workspace/skills"]
  },
  "role_arn": "arn:aws:iam::123456789012:role/BedrockManagedAgentsPreviewInferenceServiceRole",
  "stream": false
}
```


|  Field  |  Required  |  Description  | 
| --- | --- | --- | 
|  `agent`  | Yes | Agent configuration. | 
|  `agent.model`  | Yes | A BMA-supported OpenAI model available in the selected Region and account. | 
|  `agent.instructions`  | No | Instructions for the agent. | 
|  `agent.tools`  | No | Tool definitions, such as the environment-based STDIO MCP configuration in [skills and tools](bedrock-managed-agents-openai-skills-tools.md). | 
|  `environment`  | Yes | Execution-environment configuration. | 
|  `role_arn`  | Yes for this preview workflow | IAM role in the calling account that BMA assumes. The caller must be allowed to pass it to BMA. | 
|  `input`  | No for the two execution-environment examples | Optional initial input, supplied as a string or an array of input messages. | 
|  `stream`  | No | The examples use `false` to receive a JSON session resource. The default is `false`. | 

Unknown or unsupported configuration fields can result in a validation error. Use the documented preview surface rather than copying an OpenAI-hosted Agents API request without adapting it for BMA.

### Environment configuration
<a name="bedrock-managed-agents-openai-api-reference-environment-configuration"></a>

For a self-hosted environment:

```
{
  "type": "self_hosted",
  "workspace_directory": "/path/to/workspace",
  "capability_directories": ["/path/to/workspace/skills"]
}
```

For an AgentCore Runtime environment:

```
{
  "type": "aws_bedrock_agentcore",
  "runtime_arn": "arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/example-runtime",
  "runtime_qualifier": "DEFAULT",
  "workspace_directory": "/mnt/workspace",
  "capability_directories": ["/mnt/workspace/skills"]
}
```

 `workspace_directory` is a path in the execution environment. `capability_directories` identifies directories that contain skills and other discoverable capabilities. Use absolute paths. The schema permits at most 32 unique capability-directory entries.

 `runtime_arn` is required for `aws_bedrock_agentcore`. Use a Runtime in the intended account and Region, and configure the session role to invoke and stop that Runtime. `runtime_qualifier` selects the Runtime endpoint; the example uses `DEFAULT`.

### Response
<a name="bedrock-managed-agents-openai-api-reference-response"></a>

A JSON session resource includes:


|  Field  |  Description  | 
| --- | --- | 
|  `id`  | Session ID. | 
|  `object`  |  `agent.session`. | 
|  `agent`  | Resolved agent ID, model, instructions, and tool configuration. | 
|  `environment`  | Resolved environment, including its ID. | 
|  `role_arn`  | Role used for customer-authorized session operations. | 
|  `status`  |  `idle`, `in_progress`, or `failed`. | 
|  `created_at`  | Creation timestamp in Unix seconds. | 
|  `last_active_at`  | Last activity timestamp in Unix seconds. | 
|  `error`  | Error details when present. | 

A newly created self-hosted session can be `idle` before an exec server is attached. Attach the environment before asking it to execute commands.

## List and retrieve sessions
<a name="bedrock-managed-agents-openai-api-reference-list-and-retrieve-sessions"></a>

List sessions:

```
python3 bma_client.py GET '/openai/v1/agents/sessions?limit=20&order=desc'
```

The list operation accepts `limit`, `order`, `after`, and `agent_id`. `order` is `asc` or `desc`. Pass the previous page's `last_id` as `after` when `has_more` is true.

Retrieve one session:

```
python3 bma_client.py GET "/openai/v1/agents/sessions/${SESSION_ID}"
```

## Submit events
<a name="bedrock-managed-agents-openai-api-reference-submit-events"></a>

Messages and cancellation requests are submitted through the same endpoint. The request body must contain a nonempty `events` array.

Message event:

```
{
  "events": [{
    "type": "agent.session.input.message",
    "input": [{
      "role": "user",
      "content": [{"type": "input_text", "text": "Run the hello-docs skill."}]
    }]
  }]
}
```

Cancel event:

```
{"events":[{"type":"agent.session.input.cancel"}]}
```

The preview examples use text input. An accepted input event does not mean that the resulting turn has finished.

## Stream events
<a name="bedrock-managed-agents-openai-api-reference-stream-events"></a>

Send `GET` to the session's `/events` path and accept `text/event-stream`. Parse SSE frames rather than attempting to deserialize the entire response as one JSON object.

Events report changes in session state and turn progress, including generated text, command output, completion, failure, and cancellation. Keep your event parser tolerant of event types that it does not use, while validating fields that it consumes. Use durable items to reconcile after a disconnected stream.

See [stream progress](bedrock-managed-agents-openai-sessions.md#bedrock-managed-agents-openai-sessions-stream-progress) for an executable example.

## List items
<a name="bedrock-managed-agents-openai-api-reference-list-items"></a>

```
python3 bma_client.py GET "/openai/v1/agents/sessions/${SESSION_ID}/items?limit=100&order=asc"
```


|  Query parameter  |  Description  | 
| --- | --- | 
|  `limit`  | Number of items, from 1 to 100. Default: 20. | 
|  `order`  |  `asc` or `desc`. Default: `desc`. | 
|  `after`  | Opaque cursor from the previous page's `last_id`. | 

The list response includes `data`, `has_more`, `first_id`, and `last_id`. A message item contains its role and content. A command-execution item can include its command, working directory, output, exit code, and duration. An MCP-call item includes its server label, tool name, arguments, result, and status.

## Delete a session
<a name="bedrock-managed-agents-openai-api-reference-delete-a-session"></a>

```
python3 bma_client.py DELETE "/openai/v1/agents/sessions/${SESSION_ID}"
```

The deletion acknowledgement identifies the deleted session. Once deleted, the session is no longer available for continued work. Clean up separately provisioned resources as described in [cleanup](bedrock-managed-agents-openai-cleanup.md).

## Errors and retries
<a name="bedrock-managed-agents-openai-api-reference-errors-and-retries"></a>


|  HTTP status  |  What to check  | 
| --- | --- | 
|  `400`  | Required fields, supported field names, request types, model configuration, and the role ARN. | 
|  `401` or `403`  | AWS credentials, Region and signing service, BMA permissions, `iam:PassRole`, and role trust. | 
|  `404`  | Endpoint and route, resource ID, preview access, or an API that is not deployed. | 
|  `409`  | A conflicting session or environment operation. Re-read current state before retrying. | 
|  `429`  | Request or account limits. Reduce concurrency and use backoff with jitter. | 
|  `500` or `503`  | Service or dependency failure. Retain the request ID and retry where doing so is safe. | 

Capture response error details and the request ID when troubleshooting. Retry read operations with bounded exponential backoff. Before retrying a create or input submission after a network interruption, check whether it was accepted to avoid duplicate sessions or turns.