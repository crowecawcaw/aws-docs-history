

# Unsubscribe from AI Agent message status changes

Removes a previously registered `onAIAgentMessageStatusChanged` handler subscription.

 **Signature** 

```typescript
offAIAgentMessageStatusChanged(handler: AIAgentMessageStatusHandler, contactId?: string): void
```

 **Usage** 

```typescript
aiAgentsClient.offAIAgentMessageStatusChanged(handler, contactId);
```

 **Permissions required:** 

```typescript
*
```