# View information about an agent-knowledge base association

To learn how to view information about a knowledge base, choose the tab for your preferred method, and then follow the steps:

Console

###### To view information about a knowledge base that's associated with an agent

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. Choose **Edit in Agent builder**
4. In the **Knowledge bases** section, select the knowledge base for which you want to view information.

API
To get information about a knowledge base associated with an agent, send a [GetAgentKnowledgeBase](../APIReference/API_agent_GetAgentKnowledgeBase.md "../APIReference/API_agent_GetAgentKnowledgeBase.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Specify the following fields:

To list information about the knowledge bases associated with an agent, send a [ListAgentKnowledgeBases](../APIReference/API_agent_ListAgentKnowledgeBases.md "../APIReference/API_agent_ListAgentKnowledgeBases.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Specify the `agentId` and `agentVersion` for which you want to see associated knowledge bases.

| Field      | Short description                                                                                                                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxResults | The maximum number of results to return in a<br>response.                                                                                                                                                                 |
| nextToken  | If there are more results than the number you specified<br>in the `maxResults` field, the response returns a `nextToken`<br>value. To see the next batch of results, send the<br>`nextToken` value in another<br>request. |

[See code examples](bedrock-agent_example_bedrock-agent_ListAgentKnowledgeBases_section.md "bedrock-agent_example_bedrock-agent_ListAgentKnowledgeBases_section.md")
