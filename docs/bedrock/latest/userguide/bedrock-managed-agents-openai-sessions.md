

# Work with sessions, events, and results
<a name="bedrock-managed-agents-openai-sessions"></a>

A BMA session keeps conversation context across turns. Create one session for a related sequence of tasks, submit messages to it, and delete it when the application no longer needs it.

## Session lifecycle
<a name="bedrock-managed-agents-openai-sessions-session-lifecycle"></a>

The session resource reports one of these states:


|  State  |  Meaning  | 
| --- | --- | 
|  `idle`  | The session is not currently performing a turn. | 
|  `in_progress`  | The session is performing work. | 
|  `failed`  | The session encountered a failure. Inspect its error details. | 

An `idle` state is not, by itself, proof that every command or requested task succeeded. Inspect the output items and the terminal events for the turn. For command-execution items, check the exit code and output.

The examples save one active session per state file. Use a different `BMA_STATE_FILE` for each concurrent test or application session. Do not overwrite a state file that you still need for cleanup.

## Submit a message
<a name="bedrock-managed-agents-openai-sessions-submit-a-message"></a>

Send `POST /openai/v1/agents/sessions/{session_id}/events` with an input-message event:

```
{
  "events": [
    {
      "type": "agent.session.input.message",
      "input": [
        {
          "role": "user",
          "content": [
            {"type": "input_text", "text": "Summarize the files in the workspace."}
          ]
        }
      ]
    }
  ]
}
```

A successful submission can return an empty response body. It acknowledges acceptance; completion is reported separately through session state, output items, and events.

For an introductory application, submit the next message after the current turn finishes. Keep application-side records of the session ID and the messages you submitted. After an ambiguous network failure, inspect session activity before resubmitting a message, because the service might already have accepted it.

## Read durable output
<a name="bedrock-managed-agents-openai-sessions-read-durable-output"></a>

Use `GET /openai/v1/agents/sessions/{session_id}/items` to retrieve conversation items. Items can include user and assistant messages, reasoning summaries, command execution, and MCP tool calls. Related output items include a `turn_id`.

From the bundle root, after installing the Python client requirements, substitute your session ID:

```
export SESSION_ID=sess_replace_with_your_session_id
python3 bma_client.py GET "/openai/v1/agents/sessions/${SESSION_ID}/items?limit=100&order=asc"
```

Use `order=asc` for chronological processing. The items endpoint accepts a `limit` from 1 to 100. The response includes `data`, `has_more`, `first_id`, and `last_id`.

When `has_more` is `true`, pass the response's `last_id` as the next request's `after` cursor. Treat cursors as opaque values and URL-encode them. For example:

```
from urllib.parse import urlencode
from bma_client import BmaClient

client = BmaClient()
session_id = "sess_replace_with_your_session_id"
after = None

while True:
    query = {"limit": 100, "order": "asc"}
    if after is not None:
        query["after"] = after
    response = client.request(
        "GET", f"/openai/v1/agents/sessions/{session_id}/items?{urlencode(query)}"
    )
    response.raise_for_status()
    page = response.json()
    for item in page["data"]:
        print(item)
    if not page["has_more"]:
        break
    after = page["last_id"]
```

## Stream progress
<a name="bedrock-managed-agents-openai-sessions-stream-progress"></a>

The events endpoint returns server-sent events (SSE), not a JSON list. Open the stream before submitting work:

```
python3 bma_client.py GET "/openai/v1/agents/sessions/${SESSION_ID}/events" --stream
```

Leave that command running in one terminal. In another terminal, submit a message with the example's `2.submit-turn.sh` script. The stream reports session and turn activity as it occurs. An idle session might not immediately produce an event.

An application should parse SSE event boundaries and JSON data, handle network interruptions, and reconcile with durable items. A client disconnect does not delete the session or necessarily cancel work. If you reconnect, use the session and items APIs to determine what happened while the stream was unavailable.

The dedicated turn-list and turn-retrieval endpoints are not part of this guide's supported preview API surface. Use session events and item `turn_id` values to correlate work.

## Cancel the current turn
<a name="bedrock-managed-agents-openai-sessions-cancel-the-current-turn"></a>

To request cancellation, post an input-cancel event:

```
python3 bma_client.py POST "/openai/v1/agents/sessions/${SESSION_ID}/events" \
  --body '{"events":[{"type":"agent.session.input.cancel"}]}'
```

Cancellation does not undo side effects from tools that already completed. Monitor the terminal event and session state before starting additional work. If a tool wrote to an external system, inspect that system separately.

## Delete a session
<a name="bedrock-managed-agents-openai-sessions-delete-a-session"></a>

```
python3 bma_client.py DELETE "/openai/v1/agents/sessions/${SESSION_ID}"
```

Delete only sessions that your application owns and no longer needs. Deleting a session requests cleanup of its managed runtime attachment. It does not destroy an AgentCore Runtime definition, its CloudFormation stack, or the files on self-hosted compute.