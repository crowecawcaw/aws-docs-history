# Unsubscribe from AI Agent message events

Removes a previously registered `onAIAgentMessageReceived` handler
subscription.

**Signature**

```
offAIAgentMessageReceived(handler: AIAgentMessageHandler, contactId?: string): void
```

**Usage**

```
aiAgentsClient.offAIAgentMessageReceived(handler, contactId);
```

**Permissions required:**

```
*
```
