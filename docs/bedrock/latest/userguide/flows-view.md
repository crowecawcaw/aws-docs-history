# View information about flows in Amazon Bedrock

To learn how to view information about a flow, choose the tab for your preferred method, and then follow the steps:

Console

###### To view the details of a flow

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Amazon Bedrock Flows** from the left navigation pane. Then, in the **Amazon Bedrock Flows** section,
   select a flow.
3. View the details of the flow in the **Flow details** pane.

API
To get information about a flow, send a [GetFlow](../APIReference/API_agent_GetFlow.md "../APIReference/API_agent_GetFlow.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the ARN or ID of the flow as the `flowIdentifier`.

To list information about your flows, send a [ListFlows](../APIReference/API_agent_ListFlows.md "../APIReference/API_agent_ListFlows.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). You can specify the following optional parameters:

| Field      | Short description                                                                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxResults | The maximum number of results to return in a response.                                                                                                                                                        |
| nextToken  | If there are more results than the number you specified in the `maxResults` field, the response returns a `nextToken` value. To see the next batch of results, send the `nextToken` value in another request. |
