# Delete an alias of a flow in Amazon Bedrock

To learn how to delete an alias of flow, choose the tab for your preferred method, and then follow the steps:

Console

###### To delete an alias

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Bedrock.
2. Select **Flows** from the left navigation pane. Then, in the **Flows** section,
   select a flow.
3. To choose the alias for deletion, in the **Aliases** section, choose the option button next to the alias that you want to delete.
4. Choose **Delete**.
5. A dialog box appears warning you about the consequences of deletion. To confirm that you want to delete the alias, enter `delete` in the input field and choose **Delete**.
6. A banner appears to inform you that the alias is being deleted. When deletion is complete, a success banner appears.

API
To delete a flow alias, send a [DeleteFlowAlias](../APIReference/API_agent_DeleteFlowAlias.md "../APIReference/API_agent_DeleteFlowAlias.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Specify the ARN or ID of the flow in the `flowIdentifier` field and the ARN or ID of the alias to delete in the `aliasIdentifier` field.
