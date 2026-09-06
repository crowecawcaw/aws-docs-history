

# Subscribe to AI Agent message status changes in Connect Customer agent workspace
<a name="3P-apps-ai-agents-onaiagentmessagestatuschanged"></a>

Subscribes to status lifecycle transitions for AI Agent messages. Use this to track whether messages have been received, succeeded, were blocked by guardrails, or failed.

 **Signature** 

```
onAIAgentMessageStatusChanged(handler: AIAgentMessageStatusHandler, contactId?: string): void
```

 **Usage** 

```
const handler: AIAgentMessageStatusHandler = (data: AIAgentMessageStatusEvent) => {
    console.log("Input ID:", data.inputId);
    console.log("Status:", data.status);
};

aiAgentsClient.onAIAgentMessageStatusChanged(handler, contactId);

// AIAgentMessageStatusEvent Structure
{
  inputId: string;
  status: "IN_FLIGHT" | "RECEIVED" | "SUCCESS" | "BLOCKED" | "FAILED";
  contactId?: string;
}
```

 **Permissions required:** 

```
*
```