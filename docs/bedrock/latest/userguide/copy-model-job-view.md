# View information about model copy jobs

To learn how to view information about model copy jobs that you've submitted, choose the tab for your preferred method, and then follow the steps:

Console

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, choose **Custom models** under **Tune**.
3. Select the **Jobs** tab.
4. If a model is still being copied, the **Status** is **Copying**. If it's finished and ready for use, the **Status** is **Completed**.
5. When the job is complete, the model appears in the **Models** section in the **Models** tab in the Region that you copied the model to.

API
To get information about a model copy job, send a [GetModelCopyJob](../APIReference/API_GetModelCopyJob.md "../APIReference/API_GetModelCopyJob.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). Include the `jobArn` in the request.

To list the model copy jobs that you've submitted, send a [ListModelCopyJobs](../APIReference/API_ListModelCopyJobs.md "../APIReference/API_ListModelCopyJobs.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). You can use the headers in the request to specify filters for which jobs to return.

The response returns a list, each of which contains information about a model copy job that you've submitted.

When the job is complete, you should be able to see the copied model by sending a [ListCustomModels](../APIReference/API_ListCustomModels.md "../APIReference/API_ListCustomModels.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"), specifying the Region that you copied the model to.
