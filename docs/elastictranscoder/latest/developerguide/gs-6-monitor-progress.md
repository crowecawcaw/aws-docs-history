End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Monitor the Progress of Your Job

When you created a pipeline in [Create a Pipeline](gs-3-create-a-pipeline.md "gs-3-create-a-pipeline.md"),
you had the option to configure notifications, so Elastic Transcoder sends a message to an Amazon Simple Notification Service (Amazon SNS) topic when
Elastic Transcoder begins processing a job and finishes processing a job. If you configured notifications and if you
subscribed to the applicable Amazon SNS topic, you can monitor the progress of your job.
