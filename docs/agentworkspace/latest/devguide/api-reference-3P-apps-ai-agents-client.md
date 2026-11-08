

# Connect Customer SDK AI Agents API
<a name="api-reference-3P-apps-ai-agents-client"></a>

The Connect Customer SDK provides an `AIAgentsClient` which serves as an interface that your app can use to interact with AI Agent functionality. This client provides methods for real-time agent assistance use cases like checking AI Agent support, sending messages to AI Agents, retrieving message history, fetching knowledge content, and subscribing to real-time AI Agent message events.

The `AIAgentsClient` constructor requires a `ConnectClientConfig` argument, which is defined as:

```
export type ConnectClientConfig =
    | AmazonConnectProvider
    | { context: ModuleContext; provider?: AmazonConnectProvider }
    | { provider: AmazonConnectProvider };
```

Pass the `provider` that `AmazonConnectApp.init` returns to the constructor. You must provide this argument.

```
import { AIAgentsClient } from "@amazon-connect/ai-agents";

const aiAgentsClient = new AIAgentsClient(provider);
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md), which initializes the default AmazonConnectProvider and returns `{ provider }`.

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