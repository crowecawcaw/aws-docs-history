# Delete an action group

To learn how to delete an action group, choose the tab for your preferred method, and then follow the steps:

Console

###### To delete an action group

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. Choose **Edit in Agent builder**
4. In the **Action groups** section, choose the option button that's next to the action group you want to delete.
5. A dialog box appears warning you about the consequences of deletion. To confirm that you want to delete the action group, enter `delete` in the input field and then select **Delete**.
6. When deletion is complete, a success banner appears.
7. To apply the changes that you made to the agent before testing it, choose **Prepare** in the **Test** window or at the top of the **Working draft** page.

API
To delete an action group, send a [DeleteAgentActionGroup](../APIReference/API_agent_DeleteAgentActionGroup.md "../APIReference/API_agent_DeleteAgentActionGroup.md") request. Specify the `actionGroupId` and the `agentId` and `agentVersion` from which to delete it. By default, the `skipResourceInUseCheck` parameter is `false` and deletion is stopped if the resource is in use. If you set `skipResourceInUseCheck` to `true`, the resource will be deleted even if the resource is in use.

To apply the changes to the working draft, send a [PrepareAgent](../APIReference/API_agent_PrepareAgent.md "../APIReference/API_agent_PrepareAgent.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Include the `agentId` in the request. The changes apply to the `DRAFT` version, which the `TSTALIASID` alias points to.
