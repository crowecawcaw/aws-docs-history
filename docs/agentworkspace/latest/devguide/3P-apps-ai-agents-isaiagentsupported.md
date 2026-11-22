

# Check if AI Agent is supported

Checks whether the Connect Customer instance has an AI Agent configured.

 **Signature** 

```typescript
isAIAgentSupported(): Promise<AIAgentSupportedResult>
```

 **Usage** 

```typescript
const result = await aiAgentsClient.isAIAgentSupported();
console.log("AI Agent supported:", result.isSupported);

// AIAgentSupportedResult Structure
{
  isSupported: boolean;
}
```

 **Permissions required:** 

```typescript
*
```