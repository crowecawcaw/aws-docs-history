# View information about versions of flows in Amazon Bedrock

To learn how to view information about the versions of a flow, choose the tab for your preferred method, and then follow the steps:

Console

###### To view information about a version of a flow

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Bedrock.
2. Select **Flows** from the left navigation pane. Then, in the **Flows** section,
   select a flow you want to view.
3. Choose the version to view from the **Versions** section.
4. To view details about the nodes and configurations attached to version of the flow, select the node and view the details
   in the **Flow builder** pane. To make modifications to the flow, use the working draft and create a new version.

API
To get information about a version of your flow, send a [GetFlowVersion](../APIReference/API_agent_GetFlowVersion.md "../APIReference/API_agent_GetFlowVersion.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the ARN or ID of the flow as the `flowIdentifier`. In the `flowVersion` field, specify the version number.

To list information for all versions of a flow, send a [ListFlowVersions](../APIReference/API_agent_ListFlowVersions.md "../APIReference/API_agent_ListFlowVersions.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the ARN or ID of the flow as the `flowIdentifier`. You can specify the following optional parameters:

| Field      | Short description                                                                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxResults | The maximum number of results to return in a response.                                                                                                                                                        |
| nextToken  | If there are more results than the number you specified in the `maxResults` field, the response returns a `nextToken` value. To see the next batch of results, send the `nextToken` value in another request. |
