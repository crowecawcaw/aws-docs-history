# View information about aliases of agents in Amazon Bedrock

To learn how to view information about the aliases of an agent, choose the tab for your preferred method, and then follow the steps:

Console

###### To view the details of an alias

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. Choose the alias to view from the **Aliases** section.
4. You can view the name and description of the alias and tags that are associated with the alias.

API
To get information about an agent alias, send a [GetAgentAlias](../APIReference/API_agent_GetAgentAlias.md "../APIReference/API_agent_GetAgentAlias.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Specify the `agentId` and `agentAliasId`.

To list information about an agent's aliases, send a [ListAgentVersions](../APIReference/API_agent_ListAgentVersions.md "../APIReference/API_agent_ListAgentVersions.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the `agentId`. You can specify the following optional parameters:

| Field      | Short description                                                                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| maxResults | The maximum number of results to return in a response.                                                                                                                                                        |
| nextToken  | If there are more results than the number you specified in the `maxResults` field, the response returns a `nextToken` value. To see the next batch of results, send the `nextToken` value in another request. | To view all the tags for an alias, send a [ListTagsForResource](../APIReference/API_agent_ListTagsForResource.md "../APIReference/API_agent_ListTagsForResource.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and include the Amazon Resource Name (ARN) of the alias. |
