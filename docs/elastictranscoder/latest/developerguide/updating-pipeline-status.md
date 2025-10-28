End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Pausing and Reactivating Pipelines in Elastic Transcoder

If you want to cancel a job, we recommend that you first pause the corresponding pipeline so Elastic Transcoder doesn't
start processing the job. After the status of a job changes from **Submitted** to
**Progressing**, you can't cancel it.

The following procedure explains how to pause and reactivate a pipeline by using the
console. For information about how to pause and reactivate a pipeline by using the API, see
[Update Pipeline Status](update-pipeline-status.md "update-pipeline-status.md").

###### To pause or reactivate a pipeline using the Elastic Transcoder console

1. Sign in to the AWS Management Console and open the Elastic Transcoder console at
   [https://console.aws.amazon.com/elastictranscoder/](https://console.aws.amazon.com/elastictranscoder/ "https://console.aws.amazon.com/elastictranscoder/").
2. In the navigation bar of the Elastic Transcoder console, select the region in which you want to pause or reactivate a pipeline.
3. In the navigation (left) pane, click **Pipelines**.
4. Select the check box next to the pipeline that you want to pause or reactivate.
5. Click **Pause** or **Activate** as applicable.
