# Modify an Amazon Bedrock knowledge base

You can update a knowledge base, such as changing knowledge base configurations.

Choose the tab for your preferred method, and then follow the steps:

Console

###### To update a knowledge base

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, choose **Knowledge bases**.
3. Select a knowledge base to view details about it, or choose the radio button next to the knowledge base and select **Edit**.
4. You can modify the knowledge base in the following ways.
   - Change configurations for the knowledge base by choosing **Edit** in the **Knowledge base overview** section.
   - Change and manage the tags attached to the knowledge base by choosing **Manage tags** in the **Tags** section
   - Change and manage the data source for the knowledge base in the **Data source** section.

5. Select **Save changes** when you are finished editing.

API
To update a knowledge base, send an [UpdateKnowledgeBase](../APIReference/API_agent_UpdateKnowledgeBase.md "../APIReference/API_agent_UpdateKnowledgeBase.md") request with a [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Because all fields will be overwritten, include both fields that you want to update as well as fields that you want to keep the same.
