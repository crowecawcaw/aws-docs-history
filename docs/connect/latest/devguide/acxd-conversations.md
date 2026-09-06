

# Conversations
<a name="acxd-conversations"></a>

Access conversation history and transcripts.

**Topics**
+ [ListConversations](#acxd-conversations-listconversations)
+ [GetConversation](#acxd-conversations-getconversation)
+ [Request Parameters](#acxd-conversations-request-parameters)
+ [Response Fields](#acxd-conversations-response-fields)

## ListConversations
<a name="acxd-conversations-listconversations"></a>

Lists conversation transcripts with filters.

### Input
<a name="acxd-conversations-listconversations-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| startTimestamp | string | Yes | 
| endTimestamp | string | Yes | 
| userId | string | No | 
| applicationId | string | No | 
| conversationIdentifier | string | No | 
| flowId | string | No | 
| flowIds | string | No | 
| languageCode | string | No | 
| utterance | string | No | 
| search | string | No | 
| analyticsTags | string | No | 
| excludeTrivials | string | No | 
| userEngagement | string | No | 
| sortBy | string | No | 
| sortOrder | string | No | 
| includeSilence | boolean | No | 
| includeEvaluations | string | No | 
| timezone | string | No | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-conversations-listconversations-sample-request"></a>

```
await client.send(new ListConversationsCommand({
      startTimestamp: sevenDaysAgo.toISOString(),
      endTimestamp: now.toISOString(),
      maxResults: 10,
}));
```

### Output
<a name="acxd-conversations-listconversations-output"></a>

```
{
  "items": [
    {
      "conversationId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "firstTimestamp": "2026-08-01T12:00:00.000Z",
      "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
      "userId": "user-123",
      "firstUtterance": "I need help with my order",
      "flowIds": ["MainFlow", "SupportFlow"],
      "elapsedSeconds": 120,
      "analyticsTags": ["resolved_issue"],
      "avgSentimentScore": 0.8,
      "avgResponseTime": 1.2,
      "evaluationResults": []
    }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-conversations-listconversations-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## GetConversation
<a name="acxd-conversations-getconversation"></a>

Gets a single conversation's full transcript.

### Input
<a name="acxd-conversations-getconversation-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| conversationIdentifier | string | Yes | 
| includeSilence | boolean | No | 
| includeEvaluations | string | No | 

### Sample Request
<a name="acxd-conversations-getconversation-sample-request"></a>

```
await client.send(new GetConversationCommand({
  conversationIdentifier: "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
}));
```

### Output
<a name="acxd-conversations-getconversation-output"></a>

```
{
  "conversationId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "timestamp": "2026-08-01T12:00:00.000Z",
  "userId": "user-123",
  "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  "duration": 120.5,
  "flowIds": ["MainFlow", "SupportFlow"],
  "analyticsTags": ["resolved_issue"],
  "responseTime": 1.2,
  "messages": [
    {
      "isApplication": false,
      "text": "I need help with my order",
      "timestamp": "2026-08-01T12:00:01.000Z",
      "flowId": "MainFlow",
      "isEscalation": false,
      "isIncomprehension": false
    },
    {
      "isApplication": true,
      "text": "I'd be happy to help! Can you provide your order number?",
      "timestamp": "2026-08-01T12:00:02.000Z",
      "flowId": "SupportFlow",
      "nodeId": "ask-order-number",
      "isEscalation": false,
      "isIncomprehension": false
    }
  ],
  "evaluationResults": [
    {
      "evaluationId": "eval-uuid",
      "evaluationName": "Quality Check",
      "score": 0.95,
      "result": "pass",
      "feedback": null
    }
  ]
}
```

### Errors
<a name="acxd-conversations-getconversation-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-conversations-request-parameters"></a>

`conversationIdentifier`  
Type: String  
The conversation ID to retrieve.

`startTimestamp`  
Type: String  
Start of time range filter (ISO 8601). Required for listing conversations.

`endTimestamp`  
Type: String  
End of time range filter (ISO 8601). Required for listing conversations.

`userId`  
Type: String  
Filter by end-user ID.

`applicationId`  
Type: String  
Filter by application.

`flowId`  
Type: String  
Filter by a single flow ID (alphabetic characters, 3–64 chars).

`flowIds`  
Type: String  
Filter by multiple flow IDs (comma-separated, alphabetic characters).

`languageCode`  
Type: String  
Filter by language. See Common Types.

`utterance`  
Type: String  
Filter by user utterance text (max 2000 characters).

`search`  
Type: String  
Full-text search across conversation content (max 2000 characters).

`analyticsTags`  
Type: String  
Filter by analytics tags (comma-separated, alphanumeric \+ underscores).

`excludeTrivials`  
Type: String  
Exclude trivial conversations. `true` or `false`.

`userEngagement`  
Type: String  
Filter by user engagement. `true` or `false`.

`sortBy`  
Type: String  
Field to sort results by.

`sortOrder`  
Type: String  
Sort direction: `asc` or `desc`.

`includeSilence`  
Type: Boolean  
Whether to include silence events in the transcript.

`includeEvaluations`  
Type: String  
Whether to include evaluation results. `true` or `false`.

`timezone`  
Type: String  
Timezone for the time range filter.

`nextToken`  
Type: String  
Pagination token. See Common Types.

`maxResults`  
Type: Integer  
Max items per page (10–300). See Common Types.

## Response Fields
<a name="acxd-conversations-response-fields"></a>

`conversationId`  
Type: String  
The unique conversation identifier.

`timestamp`  
Type: String  
When the conversation started (ISO 8601).

`firstTimestamp`  
Type: String  
When the first message was sent (ISO 8601). Used in list responses.

`duration`  
Type: Number  
Total conversation duration in seconds.

`elapsedSeconds`  
Type: Integer  
Total elapsed time in seconds. Used in list responses.

`flowIds`  
Type: Array  
List of flow IDs traversed during the conversation.

`analyticsTags`  
Type: Array  
Analytics tags triggered during the conversation.

`responseTime`  
Type: Number  
Average bot response time in seconds.

`avgSentimentScore`  
Type: Number  
Average sentiment score across the conversation (0–1).

`avgResponseTime`  
Type: Number  
Average response time in seconds. Used in list responses.

`firstUtterance`  
Type: String  
The first user message. Used in list responses.

`messages`  
Type: Array  
Full list of conversation messages. Each message contains:

`messages.isApplication`  
Type: Boolean  
Whether this message is from the bot (true) or the user (false).

`messages.text`  
Type: String  
The message content.

`messages.timestamp`  
Type: String  
When the message was sent (ISO 8601).

`messages.flowId`  
Type: String  
The flow that was active when this message was sent.

`messages.nodeId`  
Type: String  
The node that generated this message (bot messages only).

`messages.correlationId`  
Type: String  
Correlation ID for tracing.

`messages.isEscalation`  
Type: Boolean  
Whether this message triggered an escalation.

`messages.isIncomprehension`  
Type: Boolean  
Whether the bot did not understand this input.

`messages.isStructured`  
Type: Boolean  
Whether this is a structured (non-text) message.

`messages.analyticsTags`  
Type: Array  
Analytics tags triggered by this message.

`messages.type`  
Type: String  
Message type identifier.

`evaluationResults`  
Type: Array  
Evaluation results for this conversation (if `includeEvaluations` was `true`).

`evaluationResults.evaluationId`  
Type: String  
The evaluation that scored this conversation.

`evaluationResults.evaluationName`  
Type: String  
Name of the evaluation.

`evaluationResults.score`  
Type: Number  
The evaluation score (0–1).

`evaluationResults.result`  
Type: String  
The evaluation result (e.g., `pass`, `fail`).

`evaluationResults.feedback`  
Type: String  
Optional feedback from the evaluation.