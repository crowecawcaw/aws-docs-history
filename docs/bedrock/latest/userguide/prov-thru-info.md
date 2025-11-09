# View information about a Provisioned Throughput

To learn how to view information about a Provisioned Throughput that you've purchased, choose the tab for your preferred method, and then follow the steps:

Console

###### To view information about a Provisioned Throughput

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Provisioned Throughput** from the left navigation pane.
3. From the **Provisioned Throughput** section, select a Provisioned Throughput.
4. View the details for the Provisioned Throughput in the **Provisioned Throughput overview** section and the tags associated with your Provisioned Throughput in the **Tags** section.

API
To retrieve information about a specific Provisioned Throughput, send a [GetProvisionedModelThroughput](../APIReference/API_GetProvisionedModelThroughput.md "../APIReference/API_GetProvisionedModelThroughput.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). Specify either the name of the Provisioned Throughput or its ARN as the `provisionedModelId`.

To list information about all the Provisioned Throughputs in an account, send a [ListProvisionedModelThroughputs](../APIReference/API_ListProvisionedModelThroughputs.md "../APIReference/API_ListProvisionedModelThroughputs.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). To control the number of results that are returned, you can specify the following optional parameters:

| Field      | Short description                                                                                                                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxResults | The maximum number of results to return in a<br>response.                                                                                                                                                                 |
| nextToken  | If there are more results than the number you specified<br>in the `maxResults` field, the response returns a `nextToken`<br>value. To see the next batch of results, send the<br>`nextToken` value in another<br>request. |

For other optional parameters that you can specify to sort and filter the results, see [ListProvisionedModelThroughputs](../APIReference/API_ListProvisionedModelThroughputs.md "../APIReference/API_ListProvisionedModelThroughputs.md").

To list all the tags for a Provisioned Throughput, send a [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") and include the Amazon Resource Name (ARN) of the Provisioned Throughput.

[See code examples](prov-thru-code-examples.md "prov-thru-code-examples.md")
