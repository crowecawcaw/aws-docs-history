# Stop a batch inference job

To learn how to stop an ongoing batch inference job, choose the tab for your preferred method, and then follow the steps:

Console

###### To stop a batch inference job

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, select **Batch inference**.
3. Select a job to go to the job details page or select the option button next to a job.
4. Choose **Stop job**.
5. Review the message and choose **Stop job** to confirm.

###### Note

You're charged for tokens that have already been processed.

API
To stop a batch inference job, send a [StopModelInvocationJob](../APIReference/API_StopModelInvocationJob.md "../APIReference/API_StopModelInvocationJob.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") and provide the ID or ARN of the job in the `jobIdentifier` field.

If the job was successfully stopped, you receive an HTTP 200 response.
