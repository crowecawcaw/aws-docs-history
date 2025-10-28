End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Pipeline Operations

###### Topics

- [Create Pipeline](create-pipeline.md "create-pipeline.md")
- [List Pipelines](list-pipelines.md "list-pipelines.md")
- [Read Pipeline](get-pipeline.md "get-pipeline.md")
- [Update Pipeline](update-pipeline.md "update-pipeline.md")
- [Update Pipeline Status](update-pipeline-status.md "update-pipeline-status.md")
- [Update Pipeline Notifications](update-pipeline-notifications.md "update-pipeline-notifications.md")
- [Delete Pipeline](delete-pipeline.md "delete-pipeline.md")
- [Test Role](test-pipeline-role.md "test-pipeline-role.md")
  Pipelines are queues that manage your transcoding jobs. When you create a job, you specify which pipeline you want to
  add the job to. Elastic Transcoder starts processing the jobs in a pipeline in the order in which you added them.

This section describes operations that you can perform on pipelines using the Elastic Transcoder API. For more information about
pipelines, including how to perform the same operations using the Elastic Transcoder console, see
[Working with Pipelines](working-with-pipelines.md "working-with-pipelines.md").
