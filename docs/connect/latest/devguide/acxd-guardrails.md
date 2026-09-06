

# Guardrails
<a name="acxd-guardrails"></a>

Define safety rules that monitor conversation content and enforce behavior like masking, modifying, rerouting, or flagging when violations are detected.

**Topics**
+ [ListGuardrails](#acxd-guardrails-listguardrails)
+ [CreateGuardrail](#acxd-guardrails-createguardrail)
+ [GetGuardrail](#acxd-guardrails-getguardrail)
+ [UpdateGuardrail](#acxd-guardrails-updateguardrail)
+ [DeleteGuardrail](#acxd-guardrails-deleteguardrail)
+ [TestGuardrail](#acxd-guardrails-testguardrail)
+ [ListGuardrailEvents](#acxd-guardrails-listguardrailevents)
+ [Request Parameters](#acxd-guardrails-request-parameters)
+ [Guardrail Rule](#acxd-guardrails-guardrail-rule)
+ [Detection](#acxd-guardrails-detection)
+ [Enforcement](#acxd-guardrails-enforcement)
+ [Enforcement Behavior](#acxd-guardrails-enforcement-behavior)
+ [Fallback Behavior](#acxd-guardrails-fallback-behavior)

## ListGuardrails
<a name="acxd-guardrails-listguardrails"></a>

Lists all guardrails in the workspace.

### Input
<a name="acxd-guardrails-listguardrails-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-guardrails-listguardrails-sample-request"></a>

```
await client.send(new ListGuardrailsCommand({}));
```

### Output
<a name="acxd-guardrails-listguardrails-output"></a>

```
{
  "items": [
    {
      "guardrailId": "g1a2b3c4-5678-90ab-cdef-1234567890ab",
      "name": "PII Filter",
      "trigger": "output",
      "description": "Masks personally identifiable information in bot responses",
      "active": true,
      "rules": [
        {
          "id": "r1a2b3c4-...",
          "name": "Email detection",
          "detection": { "method": "regex", "pattern": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" },
          "enforcement": { "action": "mask", "behavior": {"maskText": "[REDACTED]" } },
          "active": true
        }
      ],
      "metadata": { "path": "/safety", "tags": ["pii"] },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "lastUpdatedBy": "ci-deploy-bot"
    }
  ]
}
```

### Errors
<a name="acxd-guardrails-listguardrails-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateGuardrail
<a name="acxd-guardrails-createguardrail"></a>

Creates a new guardrail.

### Input
<a name="acxd-guardrails-createguardrail-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| rules | array | Yes | 
| trigger | string | Yes | 
| description | string | No | 
| active | boolean | No | 
| metadata | object | No | 
| fallbackBehavior | object | No | 

### Sample Request
<a name="acxd-guardrails-createguardrail-sample-request"></a>

```
await client.send(new CreateGuardrailCommand({
  name: "PII Filter",
  trigger: "output",
  description: "Masks PII in bot responses",
  active: true,
  rules: [
    {
      name: "Email detection",
      detection: {
        method: "regex",
        pattern: "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}",
      },
      enforcement: {
        action: "mask",
        behavior: {maskText: "[REDACTED]"},
      },
      active: true,
    },
  ],
  metadata: { path: "/safety", tags: ["pii"] },
}));
```

### Output
<a name="acxd-guardrails-createguardrail-output"></a>

```
{
    "guardrailId": "g1a2b3c4-5678-90ab-cdef-1234567890ab",
    "name": "PII Filter",
    "trigger": "output",
    "description": "Masks PII in bot responses",
    "active": true,
    "rules": [
      {
        "id": "r1a2b3c4-...",
        "name": "Email detection",
        "detection": { "method": "regex", "pattern": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" },
        "enforcement": { "action": "mask", "behavior": {"maskText": "[REDACTED]" } },
        "active": true
      }
    ],
    "metadata": { "path": "/safety", "tags": ["pii"] },
    "createdAt": "2026-08-01T12:00:00.000Z",
    "updatedAt": "2026-08-01T12:00:00.000Z",
    "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-guardrails-createguardrail-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetGuardrail
<a name="acxd-guardrails-getguardrail"></a>

Gets a single guardrail by ID.

### Sample Request
<a name="acxd-guardrails-getguardrail-sample-request"></a>

```
await client.send(new GetGuardrailCommand({
  guardrailIdentifier: "g1a2b3c4-5678-90ab-cdef-1234567890ab"
}));
```

### Input
<a name="acxd-guardrails-getguardrail-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| guardrailIdentifier | string | Yes | 

### Output
<a name="acxd-guardrails-getguardrail-output"></a>

```
{
    "guardrailId": "g1a2b3c4-5678-90ab-cdef-1234567890ab",
    "name": "PII Filter",
    "trigger": "output",
    "description": "Masks personally identifiable information in bot responses",
    "active": true,
    "rules": [
      {
        "id": "r1a2b3c4-...",
        "name": "Email detection",
        "detection": { "method": "regex", "pattern": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" },
        "enforcement": { "action": "mask", "behavior": {"maskText": "[REDACTED]" } },
        "active": true
      }
    ],
    "metadata": { "path": "/safety", "tags": ["pii"] },
    "createdAt": "2026-08-01T12:00:00.000Z",
    "updatedAt": "2026-08-01T12:00:00.000Z",
    "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-guardrails-getguardrail-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateGuardrail
<a name="acxd-guardrails-updateguardrail"></a>

Updates an existing guardrail. Only include fields you want to change.

### Input
<a name="acxd-guardrails-updateguardrail-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| guardrailIdentifier | string | Yes | 
| name | string | No | 
| rules | array | No | 
| trigger | string | No | 
| description | string | No | 
| active | boolean | No | 
| metadata | object | No | 
| fallbackBehavior | object | No | 

### Sample Request
<a name="acxd-guardrails-updateguardrail-sample-request"></a>

```
await client.send(new UpdateGuardrailCommand({
  guardrailIdentifier: "g1a2b3c4-5678-90ab-cdef-1234567890ab",
  name: "PII Filter",
  trigger: "output",
  description: "Updated - masks PII patterns",
  active: false,
  rules: [
    {
      name: "Email detection",
      detection: {
        method: "regex",
        pattern: "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}",
      },
      enforcement: {
        action: "mask",
        behavior: {maskText: "[REDACTED]"},
      },
      active: true,
    },
  ],
  metadata: { path: "/safety", tags: ["pii"] },
}));
```

### Output
<a name="acxd-guardrails-updateguardrail-output"></a>

```
{
    "guardrailId": "g1a2b3c4-5678-90ab-cdef-1234567890ab",
    "name": "PII Filter",
    "trigger": "output",
    "description": "Updated - masks PII patterns",
    "active": false,
    "rules": [
      {
        "id": "r1a2b3c4-...",
        "name": "Email detection",
        "detection": { "method": "regex", "pattern": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" },
        "enforcement": { "action": "mask", "behavior": {"maskText": "[REDACTED]" } },
        "active": true
      }
    ],
    "metadata": { "path": "/safety", "tags": ["pii"] },
    "createdAt": "2026-08-01T12:00:00.000Z",
    "updatedAt": "2026-08-01T12:00:00.000Z",
    "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-guardrails-updateguardrail-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteGuardrail
<a name="acxd-guardrails-deleteguardrail"></a>

Deletes a guardrail.

### Input
<a name="acxd-guardrails-deleteguardrail-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| guardrailIdentifier | string | Yes | 

### Sample Request
<a name="acxd-guardrails-deleteguardrail-sample-request"></a>

```
await client.send(new DeleteGuardrailCommand({
  guardrailIdentifier: "2be7442d-3cb4-4f45-940a-20335a339f70",
}));
```

### Output
<a name="acxd-guardrails-deleteguardrail-output"></a>

No response body.

### Errors
<a name="acxd-guardrails-deleteguardrail-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## TestGuardrail
<a name="acxd-guardrails-testguardrail"></a>

Tests a guardrail against sample input without affecting live conversations.

### Input
<a name="acxd-guardrails-testguardrail-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| guardrailIdentifier | string | Yes | 
| input | string | Yes | 
| trigger | string | No | 

### Sample Request
<a name="acxd-guardrails-testguardrail-sample-request"></a>

```
await client.send(new TestGuardrailCommand({
  guardrailIdentifier: created.guardrailId,
  input: "My email is john@example.com",
}));
```

### Output
<a name="acxd-guardrails-testguardrail-output"></a>

```
{
  "input": "My email is john@example.com",
  "processedInput": "My email is [REDACTED]",
  "output": "My email is [REDACTED]",
  "blocked": false,
  "terminalRuleId": null,
  "violations": [
    {
      "ruleId": "r1a2b3c4-...",
      "ruleName": "Email detection",
      "action": "mask",
      "behavior": {"maskText": "[REDACTED]" },
      "metadata": { "pattern": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" },
      "latencyMs": 12
    }
  ]
}
```

### Errors
<a name="acxd-guardrails-testguardrail-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## ListGuardrailEvents
<a name="acxd-guardrails-listguardrailevents"></a>

Lists historical guardrail trigger events.

### Input
<a name="acxd-guardrails-listguardrailevents-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| startTimestamp | string | Yes | 
| endTimestamp | string | Yes | 
| guardrailIdentifier | string | No | 
| behaviorType | enum | No | 
| userId | string | No | 
| applicationId | string | No | 
| conversationId | string | No | 
| languageCode | enum | No | 
| ruleId | string | No | 
| sortBy | enum | No | 
| sortOrder | enum | No | 
| timezone | string | No | 

### Sample Request
<a name="acxd-guardrails-listguardrailevents-sample-request"></a>

```
const now = new Date();
  const sevenDaysAgo = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000);
  const events = await client.send(new ListGuardrailEventsCommand({
    startTimestamp: sevenDaysAgo.toISOString(),
    endTimestamp: now.toISOString(),
}));
```

### Output
<a name="acxd-guardrails-listguardrailevents-output"></a>

```
{
  "items": [
    {
      "timestamp": "2026-08-01T12:05:00.000Z",
      "applicationId": "05c3fcc2-...",
      "conversationId": "conv-uuid",
      "userId": "user-123",
      "guardrailId": "g1a2b3c4-...",
      "guardrailName": "PII Filter",
      "behaviorType": "mask",
      "ruleId": "r1a2b3c4-...",
      "ruleName": "Email detection",
      "originalResponse": "My email is john@example.com",
      "ruleOutput": "My email is [REDACTED]",
      "responseTime": 15.2
    }
  ]
}
```

### Errors
<a name="acxd-guardrails-listguardrailevents-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-guardrails-request-parameters"></a>

### Request Parameters
<a name="acxd-guardrails-request-parameters-fields"></a>

`guardrailIdentifier`  
Type: String  
The guardrail ID used in Get, Update, Delete, and Test operations.

`guardrailId`  
Type: String  
The unique guardrail identifier (assigned on creation).

`name`  
Type: String  
Guardrail name. 1–100 characters.

`trigger`  
Type: String  
When to evaluate the guardrail. One of: `input` (check user messages), `output` (check bot responses).

`description`  
Type: String  
Guardrail description. Max 100 characters.

`active`  
Type: Boolean  
Whether the guardrail is active.

`rules`  
Type: Array  
List of rules (max 50). See Guardrail Rule.

`fallbackBehavior`  
Type: Object  
What to do if guardrail processing fails. See Fallback Behavior.

`input`  
Type: String  
Sample input text to test against the guardrail (TestGuardrail only).

`metadata`  
Type: Object  
Organizational metadata. See Common Types.

`startTimestamp`  
Type: String  
Start of time range for events (ISO 8601).

`endTimestamp`  
Type: String  
End of time range for events (ISO 8601).

`behaviorType`  
Type: String  
Filter events by enforcement action. One of: `mask`, `modify`, `route`, `flag`.

`userId`  
Type: String  
Filter events by end-user ID. Max 255 characters.

`applicationId`  
Type: String  
Filter events by application.

`conversationId`  
Type: String  
Filter events by conversation.

`languageCode`  
Type: String  
Filter events by language. See Common Types.

`ruleId`  
Type: String  
Filter events by a specific rule.

`sortBy`  
Type: String  
Sort events by field. `timestamp`.

`sortOrder`  
Type: String  
Sort direction: `asc` or `desc`.

`timezone`  
Type: String  
Timezone for the time range filter.

`nextToken`  
Type: String  
Pagination token. See Common Types.

`maxResults`  
Type: Integer  
Max items per page (1–500). See Common Types.

`createdAt`  
Type: String  
When the guardrail was created (ISO 8601).

`updatedAt`  
Type: String  
When the guardrail was last modified (ISO 8601).

`lastUpdatedBy`  
Type: String  
The identity of who last modified the guardrail.

## Guardrail Rule
<a name="acxd-guardrails-guardrail-rule"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| id | string | No | 
| name | string | Yes | 
| detection | object | Yes | 
| enforcement | object | Yes | 
| description | string | No | 
| active | boolean | No | 
| stateModifications | array | No | 
| tags | array | No | 

`id`  
Type: String  
Rule identifier. Server-generated if omitted on create.

`name`  
Type: String  
Rule name. Max 100 characters.

`detection`  
Type: Object  
How to detect violations. See Detection.

`enforcement`  
Type: Object  
What to do when triggered. See Enforcement.

`description`  
Type: String  
Rule description. Max 100 characters.

`active`  
Type: Boolean  
Whether this rule is active.

`stateModifications`  
Type: Array  
State changes to apply when the rule triggers.

`tags`  
Type: Array  
Analytics tags to apply when triggered: `[{ "label": "tag_name" }]`.

## Detection
<a name="acxd-guardrails-detection"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| method | enum | Yes | 
| pattern | string | No | 
| keywords | array | No | 
| prompt | string | No | 
| threshold | float | No | 

`method`  
Type: String  
Detection method. One of: `regex`, `keyword`, `llmJudge`.

`pattern`  
Type: String  
Regex pattern (for `regex` method). Max 200 characters.

`keywords`  
Type: Array  
Keyword list (for `keyword` method). Max 200 keywords, each max 50 characters.

`prompt`  
Type: String  
LLM evaluation prompt (for `llmJudge` method). Max 4000 characters.

`threshold`  
Type: Number  
Confidence threshold for `llmJudge` detection (0–1).

## Enforcement
<a name="acxd-guardrails-enforcement"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| action | enum | Yes | 
| behavior | object | No | 
| tags | array | No | 

`action`  
Type: String  
What to do when the rule triggers. One of: `mask`, `modify`, `route`, `flag`.

`behavior`  
Type: Object  
Action-specific configuration. Provide the variant matching the action. See Enforcement Behavior.

`tags`  
Type: Array  
Tags to apply when triggered.

## Enforcement Behavior
<a name="acxd-guardrails-enforcement-behavior"></a>

Fields depend on the enforcement action:

**For** `mask` or `flag`:

```
{ "maskChar": "*", "maskText": "[REDACTED]" }
```

**maskChar:** Single character to use for masking.

**maskText**: Text to replace matched content with. Max 50 characters.

**For** `modify`:

```
{ "message": "I can't help with that.", "prompt": "...", "flowId": "..." }
```

**message:** Static replacement message. Max 500 characters.

**prompt**: LLM prompt to generate a replacement. Max 1000 characters.

**flowId:** Flow to route to after modification.

**For** `route`:

```
{ "flowId": "EscalationFlow" }
```

**flowId:** Flow to route the conversation to (required).

## Fallback Behavior
<a name="acxd-guardrails-fallback-behavior"></a>

What to do if guardrail processing itself fails (e.g., LLM timeout).

`type`  
Type: String  
One of: `continue` (proceed without guardrail), `routeToFlow` (route to a safe flow).

`flowId`  
Type: String  
Flow to route to (required when type is `routeToFlow`).