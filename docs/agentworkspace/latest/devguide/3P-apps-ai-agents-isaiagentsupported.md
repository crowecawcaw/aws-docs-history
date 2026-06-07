# Check if AI Agent is supported

Checks whether the Connect Customer instance has an AI Agent configured.

**Signature**

```
isAIAgentSupported(): Promise<AIAgentSupportedResult>
```

**Usage**

```
const result = await aiAgentsClient.isAIAgentSupported();
console.log("AI Agent supported:", result.isSupported);

// AIAgentSupportedResult Structure
{
  isSupported: boolean;
}
```

**Permissions required:**

```
*
```
