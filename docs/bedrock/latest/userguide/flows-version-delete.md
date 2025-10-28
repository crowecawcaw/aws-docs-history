# Delete a version of a flow in Amazon Bedrock

To learn how to delete a version of a flow, choose the tab for your preferred method, and then follow the steps:

Console

###### To delete a version of a flow

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Bedrock.
2. Select **Flows** from the left navigation pane. Then, in the **Flows** section,
   select a flow.
3. Choose **Delete**.
4. A dialog box appears warning you about the consequences of deletion. To confirm that you want to delete the version, enter `delete` in the input field and choose **Delete**.
5. A banner appears to inform you that the version is being deleted. When deletion is complete, a success banner appears.

API
To delete a version of a flow, send a [DeleteFlowVersion](../APIReference/API_agent_DeleteFlowVersion.md "../APIReference/API_agent_DeleteFlowVersion.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Specify the ARN or ID of the flow in the `flowIdentifier` field and the version to delete in the `flowVersion` field.
