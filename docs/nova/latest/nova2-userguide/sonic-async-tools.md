# Asynchronous tool calling

Unlike traditional synchronous tool calling where the AI waits silently for tool
results, Amazon Nova 2 Sonic's asynchronous approach allows it to:

- Continue accepting user input while tools are running
- Respond to new questions without waiting for pending tool results
- Handle multiple tool calls simultaneously
- Maintain natural conversation flow without awkward pauses
- No extra configuration is required. Asynchronous tool calling works out of
  the box.

## How it works

When Nova 2 Sonic issues a tool call, it doesn't pause the conversation.
Instead, it continues listening and responsing naturally until the tool
arrives.

![](images/Asynchronous-Tool-Calling_6.png)

## Handling user

interruptions

If a user changes their request while a tool is executing, Nova 2 Sonic
handles it intelligently without canceling pending tools calls.

![](images/Asynchronous-User-Interruption_7.png)

Example Scenario

```
User: "Can I book a flight from Boston to Chicago?"
                Agent: "Sure, let me look that up for you."
                Agent: [initiates tool call for Chicago flights]
                User: "Actually, I want to go to Seattle"
                Agent: "Ok let me update that search"
                Agent: [initiates tool call for Seattle flights]
                [First tool returns with Chicago flight results]
                Agent: [receives Chicago results and processes them contextually]
```

## How it works

Tool results are always delivered: When a tool call completes, its result is
always sent to the model, even if the user has changed their request. The model
uses its reasoning capabilities to determine how to handle the
information.

Context-aware processing: The model understands the conversation context and
can appropriately handle outdated tool results. For example:

- If the user says "thank you" after changing their mind, the model
  still needs the original results for context
- If the user changes their request, the model can acknowledge the
  original results while focusing on the new request

No automatic cancellation: The system does not automatically cancel or ignore
tool calls based on new user input. This ensures the model has complete
information to make intelligent decisions about how to respond.
