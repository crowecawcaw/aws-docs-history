# Purchase Provisioned Throughput for a custom model

To use a custom model with dedicated compute capacity and guaranteed throughput, you can purchase Provisioned
Throughput for it. You can then use the resulting provisioned model for inference. For more information about Provisioned Throughput, see [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](prov-throughput.md "prov-throughput.md").

Console

###### To purchase Provisioned Throughput for a custom model.

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, choose **Custom models** under **Tune**.
3. In the **Models** tab, choose the radio button next to the model for which you want to buy Provisioned Throughput or select the model name to navigate to the details page.
4. Select **Purchase Provisioned Throughput**.
5. For more details, follow the steps in the provisioned throughput documentation.
6. After purchasing Provisioned Throughput for your custom model, follow the steps in the provisioned throughput usage documentation.

When you carry out any operation that supports usage of custom models, you will see your custom model as an option in the model selection menu.

API
To purchase Provisioned Throughput for a custom model, follow the steps in the provisioned throughput documentation to send a [CreateProvisionedModelThroughput](../APIReference/API_CreateProvisionedModelThroughput.md "../APIReference/API_CreateProvisionedModelThroughput.md") (see link for request and response formats and field details) request with a [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). Use the name or ARN of your custom model as the `modelId`. The response returns a `provisionedModelArn` that you can use as the `modelId` when making an [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") request.

[See code examples](model-customization-code-samples.md "model-customization-code-samples.md")
