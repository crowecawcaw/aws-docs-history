# Disable code interpretation in Amazon Bedrock

You can disable code interpretation in Amazon Bedrock at any time.

To learn how to disable code interpretation, choose the tab for your preferred method, and then follow the steps:

Console

###### To disable code interpretation,

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. Choose **Edit in Agent builder**.
4. Expand **Additional setting** section, choose **Disable** for **Code Interpreter**.
5. Select **Prepare** at the top of the page. And then select **Save** to save the changes to your agent.

API
To disable code interpretation, send an [UpdateAgentActionGroup](../APIReference/API_agent_UpdateAgentActionGroup.md "../APIReference/API_agent_UpdateAgentActionGroup.md")
request (see link for request and response formats and field details) with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the following fields:

| Field                      | Short description                                                |
| -------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| actionGroupName            | Name of the action group                                         |
| parentActionGroupSignature | Specify `AMAZON.CodeInterpreter` to disable the code interpreter |
| actionGroupState           | Specify `DISABLED` to disable the code interpreter               | The following example shows the general format for specifying the required fields to disable code interpretation. `UpdateAgentActionGroup: { "actionGroupName": "CodeInterpreterAction", "parentActionGroupSignature": "AMAZON.CodeInterpreter", "actionGroupState": "DISABLED" }` After you've disabled code interpretation for your agent, make sure to send a [PrepareAgent](../APIReference/API_agent_PrepareAgent.md "../APIReference/API_agent_PrepareAgent.md") request (see link for request and response formats and field details) with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). |
