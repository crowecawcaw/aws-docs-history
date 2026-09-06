

# Subscribe to AI Agent contact ready event in Connect Customer agent workspace
<a name="3P-apps-ai-agents-onaiagentcontactready"></a>

Subscribes a handler that fires when the session and agentic state have been resolved for a contact. Use this event to know when AI Agents features are available for a specific contact.

 **Signature** 

```
onAIAgentContactReady(handler: AIAgentContactReadyHandler, contactId: string): void
```

 **Usage** 

```
const handler: AIAgentContactReadyHandler = (data: AIAgentContactReadyEvent) => {
    console.log("AI Agent ready for contact:", data.contactId);
    console.log("Agentic enabled:", data.isAgenticEnabled);
};

aiAgentsClient.onAIAgentContactReady(handler, contactId);

// AIAgentContactReadyEvent Structure
{
  contactId: string;
  isAgenticEnabled: boolean;
}
```

 **Permissions required:** 

```
*
```