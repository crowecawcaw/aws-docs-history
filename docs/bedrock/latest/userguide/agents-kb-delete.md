# Disassociate a knowledge base from an agent

To learn how to disassociate a knowledge base from an agent, choose the tab for your preferred method, and then follow the steps:

Console

###### To disassociate a knowledge base from an agent

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. Choose **Edit in Agent builder**
4. In the **Knowledge bases** section, choose the option button that's next to the knowledge base that you want to delete. Then choose **Delete**.
5. Confirm the message that appears and then choose **Delete**.
6. To apply the changes that you made to the agent before testing it, choose **Prepare** in the **Test** window or at the top of the **Working draft** page.

API
To disassociate a knowledge base from an agent, send a [DisassociateAgentKnowledgeBase](../APIReference/API_agent_DisassociateAgentKnowledgeBase.md "../APIReference/API_agent_DisassociateAgentKnowledgeBase.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Specify the `knowledgeBaseId` and the `agentId` and `agentVersion` of the agent from which to disassociate it.

To apply the changes to the working draft, send a [PrepareAgent](../APIReference/API_agent_PrepareAgent.md "../APIReference/API_agent_PrepareAgent.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Include the `agentId` in the request. The changes apply to the `DRAFT` version, which the `TSTALIASID` alias points to.
