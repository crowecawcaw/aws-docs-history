

# Connect Customer agent workspace AI Agents API
<a name="api-reference-3P-apps-ai-agents-client"></a>

The Amazon Connect SDK provides an `AIAgentsClient` which serves as an interface that your app can use to interact with AI Agent functionality. This client provides methods for real-time agent assistance use cases like checking AI Agent support, sending messages to AI Agents, retrieving message history, fetching knowledge content, and subscribing to real-time AI Agent message events.

The `AIAgentsClient` accepts an optional constructor argument, ` ConnectClientConfig` which itself is defined as:

```
export type ConnectClientConfig = {  
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using the **AmazonConnectProvider** set in the global provider scope. You can also manually configure this using **setGlobalProvider**.

You can instantiate the client as follows:

```
import { AIAgentsClient } from "@amazon-connect/ai-agents";

const aiAgentsClient = new AIAgentsClient();
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md) which initializes the default AmazonConnectProvider and returns ` { provider }`. This is the recommended option.

Alternatively, you can provide a constructor argument:

```
import { AIAgentsClient } from "@amazon-connect/ai-agents";

const aiAgentsClient = new AIAgentsClient({
    context: sampleContext,
    provider: sampleProvider
});
```

The following sections describe the API calls for working with the AI Agents API.

**Topics**
+ [isAIAgentSupported()](3P-apps-ai-agents-isaiagentsupported.md)
+ [onAIAgentContactReady()](3P-apps-ai-agents-onaiagentcontactready.md)
+ [offAIAgentContactReady()](3P-apps-ai-agents-offaiagentcontactready.md)
+ [sendAIAgentMessage()](3P-apps-ai-agents-sendaiagentmessage.md)
+ [listAIAgentMessages()](3P-apps-ai-agents-listaiagentmessages.md)
+ [getKnowledgeContent()](3P-apps-ai-agents-getknowledgecontent.md)
+ [onAIAgentMessageReceived()](3P-apps-ai-agents-onaiagentmessagereceived.md)
+ [offAIAgentMessageReceived()](3P-apps-ai-agents-offaiagentmessagereceived.md)
+ [onAIAgentMessageStatusChanged()](3P-apps-ai-agents-onaiagentmessagestatuschanged.md)
+ [offAIAgentMessageStatusChanged()](3P-apps-ai-agents-offaiagentmessagestatuschanged.md)