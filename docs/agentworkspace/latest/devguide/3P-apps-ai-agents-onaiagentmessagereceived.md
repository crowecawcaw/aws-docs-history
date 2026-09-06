

# Subscribe to AI Agent message events in Connect Customer agent workspace
<a name="3P-apps-ai-agents-onaiagentmessagereceived"></a>

Subscribes to the unified AI Agents message stream. The handler fires for all message types including `USER_INPUT`, `RESPONSE_CHUNK`, `INTENT`, and `PREDEFINED`. Use the `contactId` parameter to scope the subscription to a specific contact.

 **Signature** 

```
onAIAgentMessageReceived(handler: AIAgentMessageHandler, contactId?: string): void
```

 **Usage** 

```
const handler: AIAgentMessageHandler = (data: AIAgentMessageEvent) => {
    console.log("Message type:", data.message.type);
    console.log("Content:", data.message.response.value);
    if (data.message.response.citations) {
        console.log("Citations:", data.message.response.citations);
    }
};

aiAgentsClient.onAIAgentMessageReceived(handler, contactId);

// AIAgentMessageEvent Structure
{
  inputId: string;
  message: {
    type: "RESPONSE_CHUNK" | "USER_INPUT" | "INTENT" | "PREDEFINED";
    status: "IN_FLIGHT" | "RECEIVED" | "SUCCESS" | "BLOCKED" | "FAILED";
    response: {
      value: string;
      citations?: Citation[];
      isGuardrailBlocked?: boolean;
    };
    isFinalResponse: boolean;
  };
  contactId?: string;
}

// Citation Structure
{
  citationSpan: {
    beginOffsetInclusive: number;
    endOffsetExclusive: number;
  };
  referenceType: CitationReferenceType;
  contentId?: string;
  knowledgeBaseId?: string;
  sourceURL?: string;
  title?: string;
}
```

 **Permissions required:** 

```
*
```