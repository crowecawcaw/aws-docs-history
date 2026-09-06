

# Send a message to the AI Agent
<a name="3P-apps-ai-agents-sendaiagentmessage"></a>

Sends a message to the AI Agent. Returns a handle containing the assigned `inputId` for correlating responses.

 **Signature** 

```
sendAIAgentMessage(params: SendAIAgentMessageParams): Promise<SendAIAgentMessageResult>
```

 **Usage** 

```
const handle = await aiAgentsClient.sendAIAgentMessage({
    contactId: "contact-123",
    text: "How do I reset my password?",
    metadata: {
        RECOMMENDATION_TYPE: "DETECTED_INTENT"
    }
});

console.log("Request ID:", handle.inputId);

// SendAIAgentMessageParams Structure
{
  contactId?: string;       // Contact identifier
  text: string;             // The message text (max 512 characters)
  metadata?: {              // Optional attribution metadata (max 50 entries)
    RECOMMENDATION_TYPE?: "DETECTED_INTENT" | "SUGGESTED_MESSAGE";
    INTENT_ID?: string;
  };
}

// SendAIAgentMessageResult Structure
{
  inputId: string;          // Unique ID for correlation
}
```

**Note**  
Responses to a sent message are delivered via the `onAIAgentMessageReceived` event. Use the `inputId` returned in the result to correlate incoming messages with the original request.

**Note**  
The `text` field has a maximum length of 512 characters. The `metadata` object supports a maximum of 50 entries, with keys up to 4,096 characters and values up to 4,096 characters. Identifier fields such as `contactId` have a maximum length of 256 characters.

 **Permissions required:** 

```
*
```