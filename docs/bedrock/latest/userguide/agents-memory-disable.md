# Disable agent memory

You can disable memory for your agent at any time. You cannot access memory sessions after you disable memory for your agent.

###### Note

If you enable memory for the agent and do not specify `memoryId` when you invoke the agent, agent will not
store that specific turn in the memory.

To learn how to disable memory, choose the tab for your preferred method, and then follow the steps:

Console

###### To disable memory for your agent,

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. Choose **Edit in Agent Builder**
4. In the **Memory** section, choose **Disable**.

API
To disable memory, send a [UpdateAgent](../APIReference/API_agent_UpdateAgent.md "../APIReference/API_agent_UpdateAgent.md") request (see link for request and response
formats and field details) with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Send the request
without specifying the `memoryConfiguration` structure. This
will disassociate the memory from the agent.
