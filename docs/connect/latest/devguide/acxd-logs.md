

# Logs
<a name="acxd-logs"></a>

Query conversation event logs with time-based and attribute-based filters.

**Topics**
+ [QueryLogs](#acxd-logs-querylogs)

## QueryLogs
<a name="acxd-logs-querylogs"></a>

Queries logs from the workspace.

### Input
<a name="acxd-logs-querylogs-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| timeFilter | object | Yes | 
| searchFilter | object | No | 
| sortOrder | string | No | 
| maxResults | integer | No | 
| nextToken | string | No | 

### Sample Request
<a name="acxd-logs-querylogs-sample-request"></a>

#### Query with relative time filter (last 7 days)
<a name="acxd-logs-querylogs-sample-relative"></a>

```
await client.send(new QueryLogsCommand({
  timeFilter: {
    relative: { span: "604800000" },
  },
  maxResults: 10,
}));
```

#### Query with absolute time filter
<a name="acxd-logs-querylogs-sample-absolute"></a>

```
const now = new Date();
const oneDayAgo = new Date(now.getTime() - 24 * 60 * 60 * 1000);
const absolute = await client.send(new QueryLogsCommand({
  timeFilter: {
    absolute: {
      startTimestamp: oneDayAgo.toISOString(),
      endTimestamp: now.toISOString(),
    },
  },
  maxResults: 10,
}));
```

#### Query with search filter (by event type)
<a name="acxd-logs-querylogs-sample-search"></a>

```
const filtered = await client.send(new QueryLogsCommand({
  timeFilter: {
    relative: { span: "604800000" },
  },
  searchFilter: {
    eventType: "ConversationStarted",
  },
  maxResults: 10,
}));
```

### Output
<a name="acxd-logs-querylogs-output"></a>

```
{
  "queryStatus": {
    "progressPercentage": 100.0,
    "cumulativeBytesScanned": 524288,
    "cumulativeBytesMetered": 1048576
  },
  "items": [
    {
      "eventType": "ConversationStarted",
      "eventTime": "2026-08-01T12:00:01.000Z",
      "commonProperties": [
        { "key": "conversationId", "value": "conv-uuid" },
        { "key": "applicationId", "value": "05c3fcc2-..." },
        { "key": "userId", "value": "user-123" }
      ],
      "eventProperties": [
        { "key": "buildId", "value": "b6c9ccd8-..." },
        { "key": "nodeId", "value": "f2a20ad1-..." },
        { "key": "messages", "value": ["Let me connect you with a specialist who can help."] },
        { "key": "responseTime", "value": 137 },
        { "key": "languageCode", "value": "en-US" }
      ]
    },
    {
      "eventType": "NlpInvoked",
      "eventTime": "2026-08-01T12:00:02.000Z",
      "commonProperties": [
        { "key": "conversationId", "value": "conv-uuid" }
      ],
      "eventProperties": [
        { "key": "utterance", "value": "I need help with my order" },
        { "key": "flowId", "value": "SupportFlow" }
      ]
    },
    ...
  ],
  "nextToken": "eyJvZmZzZXQiOjIwfQ=="
}
```

### Errors
<a name="acxd-logs-querylogs-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)
+ `ThrottlingException` (429)

### Request Parameters
<a name="acxd-logs-querylogs-request-parameters"></a>

`timeFilter`  
Type: Object  
Time range filter. Provide exactly one of `relative` or `absolute`. See Time Filter.

`searchFilter`  
Type: Object  
Attribute filters to narrow results. See Search Filter.

`sortOrder`  
Type: String  
Sort direction: `asc` or `desc`.

`maxResults`  
Type: Integer  
Max items per page (5–100). See Common Types.

`nextToken`  
Type: String  
Pagination token. See Common Types.

### Response Fields
<a name="acxd-logs-querylogs-response-fields"></a>

`queryStatus`  
Type: Object  
Progress information for the query.

`queryStatus.progressPercentage`  
Type: Number  
Query completion percentage (0–100).

`queryStatus.cumulativeBytesScanned`  
Type: Integer  
Total bytes scanned so far.

`queryStatus.cumulativeBytesMetered`  
Type: Integer  
Total bytes metered for billing.

`items`  
Type: Array  
List of log entries.

`items.eventType`  
Type: String  
The event type. See Event Types.

`items.eventTime`  
Type: String  
When the event occurred (ISO 8601).

`items.commonProperties`  
Type: Array  
Properties common across events (e.g., conversationId, applicationId). Each entry: `{ "key": "...", "value": "..." }`.

`items.eventProperties`  
Type: Array  
Properties specific to this event type (e.g., utterance, flowId). Each entry: `{ "key": "...", "value": "..." }`.

### Time Filter
<a name="acxd-logs-querylogs-time-filter"></a>

Provide exactly one variant:

`relative`  
Type: Object  
A relative time span from now.  

```
{ "relative": { "span": "86400000" } } // 24hrs = 86400000 ms
```

`relative.span`  
Type: String

`absolute`  
Type: Object  
An explicit start and end time.  

```
{ "absolute": { "startTimestamp": "2026-08-01T00:00:00.000Z", "endTimestamp": "2026-08-01T23:59:59.000Z" } }
```

`absolute.startTimestamp`  
Type: String  
Start of time range (ISO 8601).

`absolute.endTimestamp`  
Type: String  
End of time range (ISO 8601).

### Search Filter
<a name="acxd-logs-querylogs-search-filter"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| applicationId | string | No | 
| buildId | string | No | 
| conversationId | string | No | 
| correlationId | string | No | 
| deploymentId | string | No | 
| languageCode | string | No | 
| userId | string | No | 
| eventType | string | No | 

`applicationId`  
Type: String  
Filter by application.

`buildId`  
Type: String  
Filter by build.

`conversationId`  
Type: String  
Filter by conversation.

`correlationId`  
Type: String  
Filter by correlation ID.

`deploymentId`  
Type: String  
Filter by deployment.

`languageCode`  
Type: String  
Filter by language. See Common Types.

`userId`  
Type: String  
Filter by end-user ID. Max 256 characters.

`eventType`  
Type: String  
Filter by event type. See Event Types.

### Event Types
<a name="acxd-logs-querylogs-event-types"></a>


| Event Type | Description | 
| --- | --- | 
| AutoEscalationState | Conversation auto-escalated to a human | 
| EscalationState | Conversation enters an escalation state | 
| ChoiceSelected | User selected a choice | 
| ConditionEvaluated | A condition was evaluated | 
| DefaultFlowRetrieval | The Default flow was retrieved | 
| FallbackState | Fallback flow triggered, conversation entered a fallback state | 
| FrustrationState | User frustration was detected | 
| IncomprehensionState | Input could not be understood | 
| FlowCaptureState | Flow captured user input | 
| FlowRedirection | Conversation redirected to another flow | 
| NodeMetAllConditions | A node's conditions were all satisfied | 
| NodeTraversal | A flow node was traversed | 
| RepeatState | A step was repeated | 
| Redirection | Conversation redirected to another node | 
| ResponseSkippedAwaitingUserTurn | Response skipped, awaiting user turn | 
| StateValuesEjected | State values cleared | 
| NluRequestReceived | An NLU request received | 
| NluResponded | The NLU engine responded | 
| LifecycleHookInvoked | Lifecycle hook was invoked | 
| LifecycleHookResponded | The lifecycle hook responded | 
| LifecycleHookValidationFailed | Lifecycle hook validation failed | 
| WebhookResponseValidationFailed | Webhook response failed validation | 
| AgentStarted | Agent Started | 
| AgentEnded | Agent Ended | 
| AgenticToolStart | A tool wired up to an agent starts | 