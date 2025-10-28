# Delete a version of an agent in Amazon Bedrock

To learn how to delete a version of an agent, choose the tab for your preferred method, and then follow the steps:

Console

###### To delete a version of an agent

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. To choose the version for deletion, in the **Versions** section, choose the option button next to the version that you want to delete.
4. Choose **Delete**.
5. A dialog box appears warning you about the consequences of deletion. To confirm that you want to delete the version, enter `delete` in the input field and choose **Delete**.
6. A banner appears to inform you that the version is being deleted. When deletion is complete, a success banner appears.

API
To delete a version of an agent, send a [DeleteAgentVersion](../APIReference/API_agent_DeleteAgentVersion.md "../APIReference/API_agent_DeleteAgentVersion.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). By default, the `skipResourceInUseCheck` parameter is `false` and deletion is stopped if the resource is in use. If you set `skipResourceInUseCheck` to `true`, the resource will be deleted even if the resource is in use.
