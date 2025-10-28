End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Deleting an Elastic Transcoder Pipeline

You can delete a pipeline by using the AWS Management Console or by using the Elastic Transcoder Delete Pipeline API. The following procedure explains how to
delete pipelines using the console. For information about how to delete pipelines using the API, see [Delete Pipeline](delete-pipeline.md "delete-pipeline.md").

###### Note

You can't delete a pipeline that contains unprocessed jobs.

###### To delete a pipeline using the Elastic Transcoder console

1. Sign in to the AWS Management Console and open the Elastic Transcoder console at
   [https://console.aws.amazon.com/elastictranscoder/](https://console.aws.amazon.com/elastictranscoder/ "https://console.aws.amazon.com/elastictranscoder/").
2. In the navigation bar of the Elastic Transcoder console, select the region that contains the pipeline that you want to delete.
3. In the navigation (left) pane of the console, click **Pipelines**.
4. Select the check box for the pipeline that you want to delete.
5. Click **Remove**.
