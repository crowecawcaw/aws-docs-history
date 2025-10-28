End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Updating Pipeline Notifications in Elastic Transcoder

When you create a pipeline, you can optionally configure Elastic Transcoder to send a message to an Amazon Simple Notification Service (Amazon SNS) topic when
the status of a job changes, including when Elastic Transcoder starts or finishes processing a job, and when Elastic Transcoder encounters a
warning or error condition while processing a job. You can change whether you want Elastic Transcoder to send a message, and, if so,
you can change which SNS topic to send the message to.

Amazon SNS offers a variety of notification options, including the ability to send Amazon SNS messages to Amazon Simple Queue Service (Amazon SQS) queues.
For more information, see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").

The following procedure explains how to update notifications using the console. For information about how to
update notifications using the API, see [Update Pipeline Notifications](update-pipeline-notifications.md "update-pipeline-notifications.md").

###### To update pipeline notifications using the Elastic Transcoder console

1. Sign in to the AWS Management Console and open the Elastic Transcoder console at
   [https://console.aws.amazon.com/elastictranscoder/](https://console.aws.amazon.com/elastictranscoder/ "https://console.aws.amazon.com/elastictranscoder/").
2. In the navigation bar of the Elastic Transcoder console, select the region in which you want to pause or reactivate a pipeline.
3. In the navigation (left) pane, click **Pipelines**.
4. Select the check box next to the pipeline for which you want to change notifications.
5. Click **Edit**.
6. Change values as applicable. For more information, see
   [Settings that You Specify When You Create an Elastic Transcoder Pipeline](pipeline-settings.md "pipeline-settings.md").
7. Click **Save** to save your changes.
