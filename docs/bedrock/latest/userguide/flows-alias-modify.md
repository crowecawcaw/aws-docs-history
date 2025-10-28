# Modify an alias of a flow in Amazon Bedrock

To learn how to modify an alias of a flow, choose the tab for your preferred method, and then follow the steps:

Console

###### To modify an alias

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Bedrock.
2. Select **Flows** from the left navigation pane. Then, in the **Flows** section,
   select a flow.
3. In the **Aliases** section, choose the option button next to the alias that you want to edit.
4. You can edit the name and description of the alias. Additionally, you can perform one of the following actions:
   - To create a new version and associate this alias with that version, choose **Create a new version and associate it to this alias**.
   - To associate this alias with a different existing version, choose **Use an existing version and associate this alias**.

5. Select **Save**.

API
To update an alias, send an [UpdateFlowAlias](../APIReference/API_agent_UpdateFlowAlias.md "../APIReference/API_agent_UpdateFlowAlias.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Include both fields you want to maintain and fields that you want to change in the request.
