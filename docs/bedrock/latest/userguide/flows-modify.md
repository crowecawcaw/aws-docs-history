# Modify a flow in Amazon Bedrock

To learn how to modify a flow, choose the tab for your preferred method, and then follow the steps:

Console

###### To modify the details of a flow

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Amazon Bedrock Flows** from the left navigation pane. Then, in the **Amazon Bedrock Flows** section,
   select a flow.
3. In the **Flow details** section, choose **Edit**.
4. You can edit the name, description, and associate a different service role for the flow.
5. Select **Save changes**.

###### To modify a flow

1. If you're not already in the **flow builder**, do the following:
   1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
      [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
   2. Select **Amazon Bedrock Flows** from the left navigation pane. Then, choose a flow in the **Amazon Bedrock Flows** section.
   3. Choose **Edit in flow builder**.

2. Add, remove, and modify nodes and connections as necessary. For more information, refer to [Create and design a flow in Amazon Bedrock](flows-create.md "flows-create.md") and [Node types for your flow](flows-nodes.md "flows-nodes.md").
3. When you're done modifying your flow, choose **Save** or **Save and exit**.

API
To edit a flow, send an [UpdateFlow](../APIReference/API_agent_UpdateFlow.md "../APIReference/API_agent_UpdateFlow.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Include both fields that you want to maintain and fields that you want to change. For considerations on the fields in the request, see [Create and design a flow in Amazon Bedrock](flows-create.md "flows-create.md").
