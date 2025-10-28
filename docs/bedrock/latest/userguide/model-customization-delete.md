# Delete a custom model

To delete a custom model, choose the tab for your preferred method, and then follow the steps:

**Before you begin**

If you're deleting a distilled model, you must first delete any Provisioned Throughput or custom model deployment
associated with the model.

Console

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Provisioned Throughput** from the left navigation pane.
3. From the **Models** section, select a custom model.
4. Choose the options icon (

![Vertical ellipsis icon representing a menu or more options.](images/icons/vertical-ellipsis.png)

) and select **Delete**. 5. Follow the instructions to confirm deletion. Your custom model is then deleted.

API
To delete a custom model, send a [DeleteCustomModel](../APIReference/API_DeleteCustomModel.md "../APIReference/API_DeleteCustomModel.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). Specify either the name of the custom model or its ARN as the `modelIdentifier`.
