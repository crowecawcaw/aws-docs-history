

# Create an event
<a name="short-term-create-event"></a>

Events are the fundamental units of short-term from which structured informations are extracted into long-term memory in AgentCore Memory. The [CreateEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CreateEvent.html) operation lets you store various types of data within AgentCore Memory, organized by an actor and session. Events are scoped within memory under:

 **ActorId**   
Identifies the entity associated with the event, such as end-users or agent/user combinations

 **SessionId**   
Groups related events together, such as a conversation session

The `CreateEvent` operation stores a new immutable event within a specified memory session. Events represent individual pieces of information that your agent wants to remember, such as conversation messages, user actions, or system events.

This operation is useful for:
+ Recording conversation history between users, agents and tools
+ Storing user interactions and behaviors
+ Capturing system events and state changes
+ Building a chronological record of activities within a session

For example code, see [Scenario: A customer support AI agent using AgentCore Memory](memory-customer-scenario.md).

**Note**  
If you want to feed content into long-term memory without retaining it as a retrievable short-term event, use the [IngestData](long-term-ingest-data.md) operation instead.

## Event payload types
<a name="event-payload-types"></a>

The `payload` parameter accepts a list of payload items, letting you store different types of data in a single event. Common payload types include:

 **Conversational**   
For storing conversation messages with roles (for example, "user" or "assistant") and content.

 **JSON**   
For storing non-conversational, JSON-formatted data—such as behavioral events, activity logs, or system events—up to 100 KB for each payload.

 **Blob**   
For storing binary format data, such as images and documents, or data that is unique to your agent, such as data stored in JSON format.

**Note**  
Conversational and JSON payloads are extracted into long-term memory. Blob payloads are stored in short-term memory only and are not extracted.

Because `payload` is a list, a single event can carry more than one payload item and mix payload types. The following example shows a JSON request body that stores a conversational message, a JSON activity log, and a binary blob (a base64-encoded image) in one event:

 **Example – Multi-payload event request** 

```
{
  "memoryId": "mem-12345abcdef",
  "actorId": "agent-support-123/customer-456",
  "sessionId": "session-789",
  "eventTimestamp": 1718806000000,
  "payload": [
    {
      "conversational": {
        "content": {
          "text": "Here's a photo of the camera I'm interested in."
        },
        "role": "USER"
      }
    },
    {
      "json": {
        "content": {
          "eventType": "product_viewed",
          "productId": "cam-9921",
          "category": "action-cameras",
          "priceUsd": 349.99
        }
      }
    },
    {
      "blob": "iVBORw0KGgoAAAANSUhEUg..."
    }
  ]
}
```

## Extraction configuration
<a name="short-term-event-extraction-config"></a>

Use the `extractionConfig` parameter to configure how long-term memory extraction behaves for this event. Use this parameter to pass custom namespace variable values that the service substitutes into `namespaceTemplates` during extraction.

 **namespaceVariables**   
A map of custom namespace variable keys to their values. If you defined [custom namespace variables](specify-long-term-memory-organization.md#specify-custom-namespace-variables) with the `namespaceKeys` parameter when creating the memory, pass their values here so the service can resolve the namespace hierarchy for long-term memory storage. All keys and values must be lowercase.

The following example shows how to pass custom namespace variable values when creating an event:

```
{
  "memoryId": "mem-12345abcdef",
  "actorId": "user456",
  "sessionId": "session789",
  "eventTimestamp": 1692804206123,
  "payload": [
    {
      "conversational": {
        "content": {"text": "I need help with my deployment."},
        "role": "USER"
      }
    }
  ],
  "extractionConfig": {
    "namespaceVariables": {
      "orgname": "engineering",
      "teamname": "backend"
    }
  }
}
```

**Note**  
If required values in `extractionConfig` are missing or invalid, the `CreateEvent` operation still succeeds and the event is persisted in short-term memory. However, long-term memory extraction may not be initiated for affected strategies. Set up vended logs to monitor for extraction failures.

## Event branching
<a name="short-term-event-branching"></a>

The `branch` parameter lets you organize events through advanced branching. This is useful for scenarios like message editing or alternative conversation paths. For example, suppose you have a long-running conversation, and you realize you’re interested in exploring an alternative conversation starting from 5 messages ago. You can use the `branch` parameter to start a new conversation from that message, stored in the new branch — which lets you also return to the original conversation. And more mundanely, this is useful if you want to let your user edit their most recent message (in case the user presses enter early or has a typo) and continue the conversation.

When creating a branch, you specify:

 **name**   
A descriptive name for the branch, such as "edited-conversation".

 **rootEventId**   
The ID of the event from which the branch originates.

Here’s an example of creating a branched event to represent an edited message:

```
{
  "memoryId": "mem-12345abcdef",
  "actorId": "agent-support-123/customer-456",
  "sessionId": "session-789",
  "eventTimestamp": 1718806000000,
  "payload": [
    {
      "conversational": {
        "content": {
          "text": "I'm looking for a waterproof action camera for extreme sports."
        },
        "role": "USER"
      }
    }
  ],
  "branch": {
    "name": "edited-conversation",
    "rootEventId": "evt-67890"
  }
}
```