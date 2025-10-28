# Monitor batch inference jobs

Apart from the configurations you set for a batch inference job, you can also monitor its progress by seeing its status. For more information about the possible statuses for a job, see the `status` field in [ModelInvocationJobSummary](../APIReference/API_ModelInvocationJobSummary.md "../APIReference/API_ModelInvocationJobSummary.md").

You can also track a job's status by comparing the total number of records and number of records that have already been processed. These numbers can be found in the `manifest.json.out` file in the Amazon S3 bucket containing the output files. For more information, see [View the results of a batch inference job](batch-inference-results.md "batch-inference-results.md"). To learn how to download an S3 object, see [Downloading objects](../../../AmazonS3/latest/userguide/download-objects.md "../../../AmazonS3/latest/userguide/download-objects.md").

To learn how to view details about batch inference jobs, choose the tab for your preferred method, and then follow the steps:

Console

###### To view information about batch inference jobs

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, select **Batch inference**.
3. In the **Batch inference jobs** section, choose a job.
4. On the job details page, you can view information about the job's configuration and monitor its progress by viewing its **Status**.

API
To get information about a batch inference job, send a [GetModelInvocationJob](../APIReference/API_GetModelInvocationJob.md "../APIReference/API_GetModelInvocationJob.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") and provide the ID or ARN of the job in the `jobIdentifier` field.

To list information about multiple batch inference jobs, send [ListModelInvocationJobs](../APIReference/API_ListModelInvocationJobs.md "../APIReference/API_ListModelInvocationJobs.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). You can specify the following optional parameters:

| Field      | Short description                                                                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxResults | The maximum number of results to return in a response.                                                                                                                                                        |
| nextToken  | If there are more results than the number you specified in the `maxResults` field, the response returns a `nextToken` value. To see the next batch of results, send the `nextToken` value in another request. | To list all the tags for a job, send a [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") and include the Amazon Resource Name (ARN) of the job. You can also monitor batch inference jobs with Amazon EventBridge. For more information, see [Monitor Amazon Bedrock job state changes using Amazon EventBridge](monitoring-eventbridge.md "monitoring-eventbridge.md"). |
