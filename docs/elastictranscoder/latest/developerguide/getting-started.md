End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Getting Started with Elastic Transcoder

The example in this topic gives you a quick overview of how to use Amazon Elastic Transcoder to transcode media files from one media format
into another. You only need to perform a few basic steps to start transcoding your media files using Elastic Transcoder. The first step is
signing up for AWS. After that, you create an Amazon S3 bucket and upload a media file that you want to transcode. You then
create a pipeline to process your jobs, and create a job to transcode a specific file into a specific format.
If you want to transcode to a format for which we don't provide a preset (a template), you can create a custom preset
before you create the job.

###### Note

If you aren't already acquainted with jobs, pipelines, and presets—the basic concepts behind Elastic Transcoder—take a quick
look at the short overview topic: [What is Amazon Elastic Transcoder?](introduction.md "introduction.md")

###### Topics

- [Create an Amazon S3 Bucket or Two, and Upload a Media
  File](gs-2-create-s3-buckets.md "gs-2-create-s3-buckets.md")
- [Create a Pipeline](gs-3-create-a-pipeline.md "gs-3-create-a-pipeline.md")
- [(Optional) Create a Preset](gs-4-create-a-preset.md "gs-4-create-a-preset.md")
- [Create a Job](gs-5-create-a-job.md "gs-5-create-a-job.md")
- [Monitor the Progress of Your Job](gs-6-monitor-progress.md "gs-6-monitor-progress.md")
