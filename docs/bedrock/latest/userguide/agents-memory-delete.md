# Delete session summaries

To learn how to delete the session summaries, choose the tab for your preferred method, and then follow the steps:

Console

###### To delete session summaries,

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. Choose **Edit in Agent Builder**
4. In the **Memory** section, choose **View memory** and choose **Memory** tab.
5. ###### To choose the session summaries you want to delete,
   1. In the **Find memory sessions**, select the filter you want to use to search for the sessions summaries you want to delete.
   2. Specify the filter criteria.

6. Choose **Delete alias memory** and then choose **Delete**.

API
To delete session summaries, send a [DeleteAgentMemory](../APIReference/API_agent-runtime_DeleteAgentMemory.md "../APIReference/API_agent-runtime_DeleteAgentMemory.md") request (see link for request and
response formats and field details) with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt").

The following fields are required:

| Field        | Short description                  |
| ------------ | ---------------------------------- |
| agentId      | The identifier of the agent.       |
| agentAliasId | The identifier of the agent alias. |

The following field is optional.

| Field    | Short description                                           |
| -------- | ----------------------------------------------------------- |
| memoryId | The identifier of the memory that has the session summaries |
