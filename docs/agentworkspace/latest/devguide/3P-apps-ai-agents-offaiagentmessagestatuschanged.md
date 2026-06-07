# Unsubscribe from AI Agent message status changes

Removes a previously registered `onAIAgentMessageStatusChanged` handler
subscription.

**Signature**

```
offAIAgentMessageStatusChanged(handler: AIAgentMessageStatusHandler, contactId?: string): void
```

**Usage**

```
aiAgentsClient.offAIAgentMessageStatusChanged(handler, contactId);
```

**Permissions required:**

```
*
```
