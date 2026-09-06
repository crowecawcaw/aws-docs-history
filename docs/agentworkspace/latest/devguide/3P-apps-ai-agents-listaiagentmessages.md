

# List AI Agent messages for a contact
<a name="3P-apps-ai-agents-listaiagentmessages"></a>

Retrieves the AI Agent message history for a contact, ordered by sequence number.

 **Signature** 

```
listAIAgentMessages(params: ListAIAgentMessagesParams): Promise<ListAIAgentMessagesResult>
```

 **Usage** 

```
const result = await aiAgentsClient.listAIAgentMessages({
    contactId: "contact-123"
});

console.log("Messages:", result.messages);

// ListAIAgentMessagesParams Structure
{
  contactId?: string;
}

// ListAIAgentMessagesResult Structure
{
  contactId: string;
  messages: AIAgentMessageEvent[];
}
```

 **Permissions required:** 

```
*
```