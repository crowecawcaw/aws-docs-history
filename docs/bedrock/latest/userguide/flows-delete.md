# Delete a flow in Amazon Bedrock

If you no longer need a flow, you can delete it. Flows that you delete are retained in the AWS servers for up to fourteen days. To learn how to delete a flow, choose the tab for your preferred method, and then follow the steps:

Console

###### To delete a flow

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Amazon Bedrock Flows** from the left navigation pane. Then, in the **Amazon Bedrock Flows** section,
   select a flow to delete.
3. Choose **Delete**.
4. A dialog box appears warning you about the consequences of deletion. To confirm that you want to delete the flow, enter `delete` in the input field and choose **Delete**.
5. A banner appears to inform you that the flow is being deleted. When deletion is complete, a success banner appears.

API
To delete a flow, send a [DeleteFlow](../APIReference/API_agent_DeleteFlow.md "../APIReference/API_agent_DeleteFlow.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the ARN or ID of the flow as the `flowIdentifier`.
