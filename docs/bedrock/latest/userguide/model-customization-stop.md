# Stop a model customization job

You can stop an Amazon Bedrock model customization job while it's in progress. Choose the tab for your preferred method, and then follow the steps:

###### Warning

You can't resume a stopped job. Amazon Bedrock charges for the tokens that it used to train the model
before you stopped the job. Amazon Bedrock doesn't create an intermediate
custom model for a stopped job.

Console

###### To stop a model customization job

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, choose **Custom models** under **Tune**.
3. In the **Training Jobs** tab, choose the radio button next to the job to stop or select the job to stop to navigate to the details page.
4. Select the **Stop job** button. You can only stop a job if its status is `Training`.
5. A modal appears to warn you that you can't resume the training job if you stop it. Select **Stop job** to confirm.

API
To stop a model customization job, send a [StopModelCustomizationJob](../APIReference/API_StopModelCustomizationJob.md "../APIReference/API_StopModelCustomizationJob.md") (see link for request and response formats and field details) request with a [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"), using the `jobArn` of the job.

You can only stop a job if its status is `IN_PROGRESS`. Check the `status` with a [GetModelCustomizationJob](../APIReference/API_GetModelCustomizationJob.md "../APIReference/API_GetModelCustomizationJob.md") request. The system marks the job for termination and sets the state to `STOPPING`. Once the job is stopped, the state becomes `STOPPED`.

[See code examples](model-customization-code-samples.md "model-customization-code-samples.md")
