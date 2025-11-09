# Purchase a Provisioned Throughput for an Amazon Bedrock model

Amazon Bedrock offers two types of Provisioned Throughput - by Tokens and by Model Units. Refer to the following instructions for the type of Provisioned Throughput you wish to to purchase.

To learn more about the differences between the two types of Provisioned Throughput, see [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](prov-throughput.md "prov-throughput.md").

When you purchase a Provisioned Throughput by Model Units for a model, you specify the level of commitment for it and the number of model units (MUs) to allot. For MU quotas, see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md") in the AWS General Reference.
Before you can purchase a Provisioned Throughput (with commitment or no commitment), you must first visit the [AWS support center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase")
to request MUs for your account to be distributed between the Provisioned Throughputs. After your request has been granted, you can purchase a Provisioned Throughput.

###### Note

After you purchase the Provisioned Throughput, if it's associated with a custom model, you can change the model by specifying one of the following options:

- The base model from which the custom model was customized
- Another custom model that was customized from the same base model as the custom model
  You can only change the associated model for Provisioned Throughputs associated with a custom model.

To learn how to purchase Provisioned Throughput for a model, choose the tab for your preferred method, and then follow the steps:

Console

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Provisioned Throughput** from the left navigation pane.
3. In the **Provisioned Throughput** section, choose
   **Purchase Provisioned Throughput**.
4. For the **Provisioned Throughput details** section, do the following:
   1. In the **Provisioned Throughput name** field, enter a name for the Provisioned Throughput.
   2. Under **Select model**, select a base model provider or a custom model category. Then select the model for which to provision throughput.

   ###### Note

   To see the base models for which you can purchase Provisioned Throughput without commitment, see the supported models documentation.

   In the AWS GovCloud (US) Region, you can only purchase Provisioned Throughput for custom models with no commitment. 3. (Optional) To associate tags with your Provisioned Throughput, expand the **Tags** section and choose **Add new tag**. For more information, see [Tagging Amazon Bedrock resources](tagging.md "tagging.md").

5. For **Provisioning mode**, select **By Model Units**
6. For the **Commitment term & model units** section, do the following:
   1. In the **Select commitment term** section, select the amount of time for which you want to commit to using the Provisioned Throughput.
   2. In the **Model units** field, enter the desired number of model units (MUs). If you are provisioning a model with commitment, you must first visit the [AWS support center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase") to request an increase in the number of MUs that you can purchase.

7. Choose **Purchase Provisioned Throughput**.
8. Review the note that appears and acknowledge the commitment duration and price by selecting the checkbox. Then choose **Confirm purchase**.
9. The console displays the **Provisioned Throughput** overview page. The **Status** of the Provisioned Throughput in the Provisioned Throughput table becomes **Creating**. When the Provisioned Throughput is finished being created, the **Status** becomes **In service**. If the update fails, the **Status** becomes **Failed**.

API
To purchase a Provisioned Throughput, send a [CreateProvisionedModelThroughput](../APIReference/API_CreateProvisionedModelThroughput.md "../APIReference/API_CreateProvisionedModelThroughput.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp").

To learn more about the contents of the request body and the parameters you need to supply to create a Provisioned Throughput by Model Units, see
[CreateProvisionedModelThroughput](../APIReference/API_CreateProvisionedModelThroughput.md "../APIReference/API_CreateProvisionedModelThroughput.md") in the
_Amazon Bedrock API Reference_.

###### Note

To see the base models for which you can purchase Provisioned Throughput without commitment, see the supported models documentation.

In the AWS GovCloud (US) Region, you can only purchase Provisioned Throughput for custom models with no commitment.

The response returns a `provisionedModelArn` that you can use as a `modelId` in [model inference](inference.md "inference.md"). To check when the Provisioned Throughput is ready for use, send a [GetProvisionedModelThroughput](../APIReference/API_GetProvisionedModelThroughput.md "../APIReference/API_GetProvisionedModelThroughput.md") request and check that the status is `InService`. If the update fails, its status will be `Failed`, and the [GetProvisionedModelThroughput](../APIReference/API_GetProvisionedModelThroughput.md "../APIReference/API_GetProvisionedModelThroughput.md") response will contain a `failureMessage`.

[See code examples](prov-thru-code-examples.md "prov-thru-code-examples.md")
