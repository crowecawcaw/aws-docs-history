

# Flows
<a name="acxd-flows"></a>

A flow represents the structured path a conversation follows to fulfill a user's intent, whether that's answering FAQs, completing a task, or guiding a user toward an action. Each flow combines logic, prompts, and responses into a graph of connected nodes. Once attached to an application and deployed, the application can execute the flow and automate the corresponding task. A single flow can be shared across multiple applications in your workspace.

**Topics**
+ [ListFlows](#acxd-flows-listflows)
+ [CreateFlow](#acxd-flows-createflow)
+ [GetFlow](#acxd-flows-getflow)
+ [UpdateFlow](#acxd-flows-updateflow)
+ [DeleteFlow](#acxd-flows-deleteflow)
+ [Request Parameters](#acxd-flows-request-parameters)
+ [Attached Slot](#acxd-flows-attached-slot)
+ [Flow Node](#acxd-flows-flow-node)

## ListFlows
<a name="acxd-flows-listflows"></a>

Lists all flows in the workspace. Returns summary information without node details.

### Input
<a name="acxd-flows-listflows-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-flows-listflows-sample-request"></a>

```
await client.send(new ListFlowsCommand({}));
```

### Output
<a name="acxd-flows-listflows-output"></a>

```
{
  "items": [
    {
      "flowId": "MainFlow",
      "description": "Handles customer support inquiries",
      "mainLanguageCode": "en-US",
      "languageCodes": ["en-US", "es-ES"],
      "slotTypes": [],
      "contextVariables": [],
      "metadata": { "path": "/support", "tags": ["production"] },
      "saveId": "save-abc123",
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T14:00:00.000Z",
      "updatedBy": "ci-deploy-bot"
    }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-flows-listflows-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)
+ `ThrottlingException` (429)

## CreateFlow
<a name="acxd-flows-createflow"></a>

Creates a new flow with nodes (conversation logic), and optional slot types and context variables.

### Input
<a name="acxd-flows-createflow-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| flowId | string | Yes | 
| description | string | No | 
| nodes | object | Yes | 
| aiDescription | string | No | 
| untrained | boolean | No | 
| mainLanguageCode | string | No | 
| languageCode | enum | No | 
| languageCodes | array | No | 
| slotTypes | array | No | 
| contextVariables | array | No | 
| mcp | object | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-flows-createflow-sample-request"></a>

```
const created = await client.send(new CreateFlowCommand({
  flowId: "MainFlow",
  description: "Handles customer support inquiries",
  mainLanguageCode: "en-US",
  languageCodes: ["en-US"],
  slotTypes: [],
  contextVariables: [],
  nodes: {
    "a0000000-0000-4000-8000-000000000001": {
      nodeId: "a0000000-0000-4000-8000-000000000001",
      type: "start",
      childNodes: [{ nodeId: "a0000000-0000-4000-8000-000000000002" }],
    },
    "a0000000-0000-4000-8000-000000000002": {
      nodeId: "a0000000-0000-4000-8000-000000000002",
      type: "basic",
      messages: [{ body: "Hello! How can I help you today?", type: "text" }],
      childNodes: [{ nodeId: "a0000000-0000-4000-8000-000000000003" }],
    },
    "a0000000-0000-4000-8000-000000000003": {
      nodeId: "a0000000-0000-4000-8000-000000000003",
      type: "end",
    },
  },
  metadata: { path: "/support", tags: ["production"] },
}));
```

### Output
<a name="acxd-flows-createflow-output"></a>

```
{
  "flowId": "MainFlow",
  "description": "Handles customer support inquiries",
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "slotTypes": [],
  "contextVariables": [],
  "nodes": {
    "a0000000-0000-4000-8000-000000000001": {
      "nodeId": "a0000000-0000-4000-8000-000000000001",
      "type": "start",
      "childNodes": [
        {
          "nodeId": "a0000000-0000-4000-8000-000000000002"
        }
      ]
    },
    "a0000000-0000-4000-8000-000000000002": {
      "nodeId": "a0000000-0000-4000-8000-000000000002",
      "type": "basic",
      "messages": [
        {
          "type": "text",
          "body": "Hello! How can I help you today?",
          "messageId": "12a13e04-0bc1-4361-9505-8e9c7a2aeb7b"
        }
      ]
    },
    "a0000000-0000-4000-8000-000000000003": {
      "nodeId": "a0000000-0000-4000-8000-000000000003",
      "type": "end",
      "messages": []
    }
  },
  "metadata": { "path": "/support", "tags": ["production"] },
  "saveId": "save-abc123",
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-flows-createflow-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)
+ `ThrottlingException` (429)

## GetFlow
<a name="acxd-flows-getflow"></a>

Gets the full flow definition including all nodes, attached slots, and context variables.

### Input
<a name="acxd-flows-getflow-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| flowIdentifier | string | Yes | 
| languageCode | string | No | 

### Sample Request
<a name="acxd-flows-getflow-sample-request"></a>

```
const fetched = await client.send(new GetFlowCommand({
    flowIdentifier: "MainFlow",
}));
```

### Output
<a name="acxd-flows-getflow-output"></a>

```
{
  "flowId": "MainFlow",
  "description": "Handles customer support inquiries",
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "slotTypes": [],
  "contextVariables": [],
  "nodes": {
    "a0000000-0000-4000-8000-000000000001": {
      "nodeId": "a0000000-0000-4000-8000-000000000001",
      "type": "start",
      "childNodes": [
        {
          "nodeId": "a0000000-0000-4000-8000-000000000002"
        }
      ]
    },
    "a0000000-0000-4000-8000-000000000002": {
      "nodeId": "a0000000-0000-4000-8000-000000000002",
      "type": "basic",
      "messages": [
        {
          "type": "text",
          "body": "Hello! How can I help you today?",
          "messageId": "12a13e04-0bc1-4361-9505-8e9c7a2aeb7b"
        }
      ]
    },
    "a0000000-0000-4000-8000-000000000003": {
      "nodeId": "a0000000-0000-4000-8000-000000000003",
      "type": "end",
      "messages": []
    }
  },
  "metadata": { "path": "/support", "tags": ["production"] },
  "saveId": "save-abc123",
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-flows-getflow-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)
+ `ThrottlingException` (429)

## UpdateFlow
<a name="acxd-flows-updateflow"></a>

Updates an existing flow. Only include fields you want to change. Changes do not affect deployed applications until a new build is created.

### Input
<a name="acxd-flows-updateflow-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| flowIdentifier | string | Yes | 
| nodes | object | No | 
| description | string | No | 
| aiDescription | string | No | 
| untrained | boolean | No | 
| mainLanguageCode | string | No | 
| languageCode | enum | No | 
| languageCodes | array | No | 
| slotTypes | array | No | 
| contextVariables | array | No | 
| mcp | object | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-flows-updateflow-sample-request"></a>

```
await client.send(new UpdateFlowCommand({
    flowIdentifier: "MainFlow",
    description: "Updated Primary support flow",
    mainLanguageCode: "en-US",
    languageCodes: ["en-US"],
    slotTypes: [],
    contextVariables: [],
    nodes: {
      "a0000000-0000-4000-8000-000000000001": {
        nodeId: "a0000000-0000-4000-8000-000000000001",
        type: "start",
        childNodes: [{ nodeId: "a0000000-0000-4000-8000-000000000002" }],
      },
      "a0000000-0000-4000-8000-000000000002": {
        nodeId: "a0000000-0000-4000-8000-000000000002",
        type: "basic",
        messages: [{ body: "Hello! How can I help you today?", type: "text" }],
        childNodes: [{ nodeId: "a0000000-0000-4000-8000-000000000003" }],
      },
      "a0000000-0000-4000-8000-000000000003": {
        nodeId: "a0000000-0000-4000-8000-000000000003",
        type: "end",
      },
    },
    metadata: { path: "/support", tags: ["production"] },
  }));
```

### Output
<a name="acxd-flows-updateflow-output"></a>

```
{
  "flowId": "MainFlow",
  "description": "Updated Primary support flow",
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "slotTypes": [],
  "contextVariables": [],
  "nodes": {
    "a0000000-0000-4000-8000-000000000001": {
      "nodeId": "a0000000-0000-4000-8000-000000000001",
      "type": "start",
      "childNodes": [
        {
          "nodeId": "a0000000-0000-4000-8000-000000000002"
        }
      ]
    },
    "a0000000-0000-4000-8000-000000000002": {
      "nodeId": "a0000000-0000-4000-8000-000000000002",
      "type": "basic",
      "messages": [
        {
          "type": "text",
          "body": "Hello! How can I help you today?",
          "messageId": "12a13e04-0bc1-4361-9505-8e9c7a2aeb7b"
        }
      ]
    },
    "a0000000-0000-4000-8000-000000000003": {
      "nodeId": "a0000000-0000-4000-8000-000000000003",
      "type": "end",
      "messages": []
    }
  },
  "metadata": { "path": "/support", "tags": ["production"] },
  "saveId": "save-abc123",
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-flows-updateflow-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `ConflictException` (409)
+ `InternalServerException` (500)
+ `ThrottlingException` (429)

## DeleteFlow
<a name="acxd-flows-deleteflow"></a>

Deletes a flow. If the flow is attached to applications, detach it first.

### Input
<a name="acxd-flows-deleteflow-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| flowIdentifier | string | Yes | 

### Sample Request
<a name="acxd-flows-deleteflow-sample-request"></a>

```
await client.send(new DeleteFlowCommand({
  flowIdentifier: "TestFlowSDKClient",
}));
```

### Output
<a name="acxd-flows-deleteflow-output"></a>

No response body.

### Errors
<a name="acxd-flows-deleteflow-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)
+ `ThrottlingException` (429)

## Request Parameters
<a name="acxd-flows-request-parameters"></a>

`flowId`

Type: String

The flow identifier. Alphanumeric characters, 3–64 characters.

`flowIdentifier`

Type: String

The flow ID used in Get, Update, and Delete operations.

`description`

Type: String

Flow description. Max 200 characters.

`aiDescription`

Type: String

AI-readable description of what this flow does. Max 1000 characters. Used by generative features to understand flow purpose.

`untrained`

Type: Boolean

Whether to skip NLP training for this flow.

`mainLanguageCode`

Type: String

Primary language. See Common Types.

`languageCode`

Type: String

Language code. See Common Types.

`languageCodes`

Type: Array

Supported languages. See Common Types.

`nodes`

Type: Object

The flow node graph. A map of node IDs to node objects. See Flow Node.

`slotTypes`

Type: Array

Slot types attached to this flow. See Attached Slot.

`contextVariables`

Type: Array

Flow-scoped context variables. Each entry: `{ "name": "varName", "type": "text|number|boolean" }`.

`mcp`

Type: Object

MCP endpoint configuration: `{ "input": { "name": "...", "schema": {...} }, "output": { "name": "...", "schema": {...} } }`.

`metadata`

Type: Object

Organizational metadata. See Common Types.

`magicLayout`

Type: Boolean

Whether to apply automatic layout during validation.

`saveId`

Type: String

Internal save identifier (read-only).

`createdAt`

Type: String

When the flow was created (ISO 8601).

`updatedAt`

Type: String

When the flow was last modified (ISO 8601).

`updatedBy`

Type: String

The identity of who last modified the flow.

`nextToken`

Type: String

Pagination token. See Common Types.

`maxResults`

Type: Integer

Max items per page (1–500). See Common Types.

## Attached Slot
<a name="acxd-flows-attached-slot"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| type | string | Yes | 
| sensitive | boolean | No | 
| examples | array | No | 
| aiDescription | string | No | 
| regex | string | No | 

`name`

Type: String

Slot name. Alphabetic characters only, 3–30 characters.

`type`

Type: String

The slot type reference.

`sensitive`

Type: Boolean

Whether this slot captures sensitive data.

`examples`

Type: Array

Example values for this slot (array of strings).

`aiDescription`

Type: String

AI-readable description of what this slot captures. Max 1000 characters.

`regex`

Type: String

Optional regex pattern for validation. Max 300 characters.

## Flow Node
<a name="acxd-flows-flow-node"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| nodeId | string | Yes | 
| type | enum | Yes | 
| childNodes | array | No | 
| dataRequests | array | No | 
| messages | array | No | 
| modalities | object | No | 
| canvasMetadata | object | No | 
| metadata | object | No | 

`nodeId`

Type: String

Unique node identifier.

`type`

Type: String

The node type. One of: `basic`, `start`, `end`, `user_input`, `user_choice`, `choice`, `data_request`, `redirect`, `escalate`, `split`, `loop`, `define`, `wait`, `transform`, `note`, `knowledge_base`, `generative_text`, `generative_task`, `generative_journey`, `multimodal`, `intent_capture`, `application_handoff`.

`childNodes`

Type: Array

Connected child nodes. Each entry: `{ "nodeId": "...", "name": "...", "conditions": [...] }`.

`dataRequests`

Type: Array

Data requests triggered by this node.

`messages`

Type: Array

Messages displayed at this node.

`modalities`

Type: Object

Modality-specific content (free-form).

`canvasMetadata`

Type: Object

Visual editor position and display settings: `{ "x": 100, "y": 200, "width": 300, "height": 150, "color": "#fff", "pageId": "..." }`.

`metadata`

Type: Object

Node-type-specific configuration. The fields available depend on the node `type`. Contains configuration like `generativeText`, `choice`, `redirect`, `knowledgeBase`, `loop`, `multimodal`, `stateModifications`, `tags`, `name`, `timeout`, etc.