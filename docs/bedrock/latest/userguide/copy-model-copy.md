# Copy a model to a Region

After you [fulfill the prerequisites](copy-model-prereq.md "copy-model-prereq.md"), you can copy a model. You can copy a model that you own into a different Region, or a model that has been shared with you into a Region so that you can use it. Choose the tab for your preferred method, and then follow the steps:

Console

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, choose **Custom models** under **Tune**.
3. Depending on your use case, do one of the following:
   - To copy a model that you own into a different Region, select the button next to the model that you want to share in the **Models** section. Then, choose the three dots (

   ![Vertical ellipsis icon representing a menu or more options.](images/icons/vertical-ellipsis.png)

   ) and select **Copy**.
   - To copy a model that was shared with you into a Region, select the button next to the model that you want to share in the **Models shared with you** section. Then, choose **Copy**.

4. In the **Copy details** section, do the following:
   1. In the **Model name** field, give the model copy a name.
   2. Select a Region from the dropdown menu in the **Destination Region** field.
   3. (Optional) To add tags, expand the **Tags** section. For more information, see [Tagging Amazon Bedrock resources](tagging.md "tagging.md").

5. In the **Copy job name** section, give the job a **Name**.
6. (Optional) To encrypt the model copy, select an AWS KMS key that you have access to. For more information, see [Permissions and key policies for custom and copied models](encryption-custom-job.md#encryption-cm-statements "encryption-custom-job.md#encryption-cm-statements").
7. Choose **Copy model**.
8. The model copy job appears in the **Jobs** tab. When the job is complete, the model's status becomes **Complete** and it appears in the **Models** section in the **Models** tab in the Region that you copied the model to.

API
To copy a model to another Region, send a [CreateModelCopyJob](../APIReference/API_CreateModelCopyJob.md "../APIReference/API_CreateModelCopyJob.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") in the Region in which you want to use the model.

The following fields are required:

| Field           | Brief description                                                                                                                                                                                                                            |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| sourceModelArn  | The Amazon Resource Name (ARN) of the model to copy.                                                                                                                                                                                         |
| targetModelName | A name for the model copy.                                                                                                                                                                                                                   | The following fields are optional:                                              |
| Field           | Use-case                                                                                                                                                                                                                                     |
| ---             | ---                                                                                                                                                                                                                                          |
| clientToken     | To ensure the API request completes only once. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md").                                  |
| modelKmsKeyId   | To provide a KMS key to encrypt the model copy. For more information, see [Permissions and key policies for custom and copied models](encryption-custom-job.md#encryption-cm-statements "encryption-custom-job.md#encryption-cm-statements") |
| targetModelTags | To provide tags for the model copy. For more information, see [Tagging Amazon Bedrock resources](tagging.md "tagging.md").                                                                                                                   | The response includes a `jobArn` field, which is the ARN of the model copy job. |
