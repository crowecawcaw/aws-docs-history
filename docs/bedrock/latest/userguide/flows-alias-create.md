# Create an alias of a flow in Amazon Bedrock

To invoke a flow, you must first create an alias that points to a version of the flow. To learn how to create an alias, choose the tab for your preferred method, and then follow the steps:

Console

###### To create an alias for your Amazon Bedrock Flows

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Amazon Bedrock Flows** from the left navigation pane. Then, choose a flow in the **Flows** section.
3. In the **Aliases** section, choose **Create alias**.
4. Enter a unique name for the alias and provide an optional description.
5. Choose one of the following options:
   - To create a new version, choose **Create a new version and to associate it to this alias**.
   - To use an existing version, choose **Use an existing version to associate this alias**. From the dropdown menu, choose the version that you want to associate the alias to.

6. Select **Create alias**. A success banner appears at the top.

API
To create an alias to point to a version of your flow, send a [CreateFlowAlias](../APIReference/API_agent_CreateFlowAlias.md "../APIReference/API_agent_CreateFlowAlias.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt").

The following fields are required:

| Field                | Basic description                                                   |
| -------------------- | ------------------------------------------------------------------- |
| flowIdentifier       | The ARN or ID of the flow for which to create an<br>alias.          |
| name                 | A name for the alias.                                               |
| routingConfiguration | Specify the version to map the alias to in the `flowVersion` field. |

The following fields are optional:

| Field       | Use-case                                 |
| ----------- | ---------------------------------------- |
| description | To provide a description for the alias.  |
| clientToken | To prevent reduplication of the request. |

Creation of an alias produces a resource with an identifier and an Amazon Resource Name (ARN) that you can specify when you invoke a flow from your application. To learn how to invoke a flow, see [Test a flow in Amazon Bedrock](flows-test.md "flows-test.md").
