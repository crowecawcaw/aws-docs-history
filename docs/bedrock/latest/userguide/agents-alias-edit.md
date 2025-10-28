# Edit an alias of an agent in Amazon Bedrock

To learn how to edit an alias of an agent, choose the tab for your preferred method, and then follow the steps:

Console

###### To edit an alias

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. In the **Aliases** section, choose the option button next to the alias that you want to edit. Then choose **Edit**
4. Edit any of the existing fields as necessary. For more information about these fields, see [Deploy and use an Amazon Bedrock agent in your application](agents-deploy.md "agents-deploy.md").
5. Select **Save**.

###### To add or remove tags associated with an alias

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
3. Choose the alias for which you want to manage tags from the **Aliases** section.
4. In the **Tags** section, choose **Manage tags**.
5. To add a tag, choose **Add new tag**. Then enter a **Key** and optionally enter a **Value**. To remove a tag, choose **Remove**. For more information, see [Tagging Amazon Bedrock resources](tagging.md "tagging.md").
6. When you're done editing tags, choose **Submit**.

API
To edit an agent alias, send an [UpdateAgentAlias](../APIReference/API_agent_UpdateAgentAlias.md "../APIReference/API_agent_UpdateAgentAlias.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Because all fields will be overwritten, include both fields that you want to update as well as fields that you want to keep the same.

To add tags to an alias, send a [TagResource](../APIReference/API_agent_TagResource.md "../APIReference/API_agent_TagResource.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and include the Amazon Resource Name (ARN) of the alias. The request body contains a `tags` field, which is an object containing a key-value pair that you specify for each tag.

To remove tags from an alias, send an [UntagResource](../APIReference/API_agent_UntagResource.md "../APIReference/API_agent_UntagResource.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and include the Amazon Resource Name (ARN) of the alias. The `tagKeys` request parameter is a list containing the keys for the tags that you want to remove.
