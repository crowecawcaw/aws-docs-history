# Deploy your knowledge base for your AI application

To deploy a knowledge base for your application, set it up to make [Retrieve](../APIReference/API_agent-runtime_Retrieve.md "../APIReference/API_agent-runtime_Retrieve.md") or [RetrieveAndGenerate](../APIReference/API_agent-runtime_RetrieveAndGenerate.md "../APIReference/API_agent-runtime_RetrieveAndGenerate.md") requests to the knowledge base. To see how to use these API operations for querying and generating responses, see [Test your knowledge base with queries and responses](knowledge-base-test.md "knowledge-base-test.md").

You can also associate the knowledge base with an agent and the agent will invoke it when necessary during orchestration. For more information, see [Automate tasks in your application using AI agents](agents.md "agents.md").

You must configure and sync your data source/sources with your knowledge base before you can deploy your knowledge base. See [Supported data sources](data-source-connectors.md "data-source-connectors.md").

Choose the tab for your preferred method, and then follow the steps:

Console

###### To associate a knowledge base with an agent

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, select **Agents**.
3. Choose the agent to which you want to add a knowledge base.
4. In the **Working draft** section, choose **Working draft**.
5. In the **Knowledge bases** section, select **Add**.
6. Choose a knowledge base from the dropdown list under **Select knowledge base** and specify the instructions for the agent regarding how it should interact with the knowledge base and return results.

###### To dissociate a knowledge base with an agent

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, select **Agents**.
3. Choose the agent to which you want to add a knowledge base.
4. In the **Working draft** section, choose **Working draft**.
5. In the **Knowledge bases** section, choose a knowledge base.
6. Select **Delete**.

API
To associate a knowledge base with an agent, send an [AssociateAgentKnowledgeBase](../APIReference/API_agent_AssociateAgentKnowledgeBase.md "../APIReference/API_agent_AssociateAgentKnowledgeBase.md") request.

- Include a detailed `description` to provide instructions for how the agent should interact with the knowledge base and return results.
- Set the `knowledgeBaseState` to `ENABLED` to allow the agent to query the knowledge base.

You can update an knowledge base that is associated with an agent by sending an [UpdateAgentKnowledgeBase](../APIReference/API_agent_UpdateAgentKnowledgeBase.md "../APIReference/API_agent_UpdateAgentKnowledgeBase.md") request. For example, you might want to set the `knowledgeBaseState` to `ENABLED` to troubleshoot an issue. Because all fields will be overwritten, include both fields that you want to update as well as fields that you want to keep the same.

To dissociate a knowledge base with an agent, send a [DisassociateAgentKnowledgeBase](../APIReference/API_agent_DisassociateAgentKnowledgeBase.md "../APIReference/API_agent_DisassociateAgentKnowledgeBase.md") request.
