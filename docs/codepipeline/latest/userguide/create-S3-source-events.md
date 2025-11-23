# Connecting to Amazon S3 source actions with a

source enabled for events

The instructions in this section provide the steps for creating the S3 source action
that does not require that you create or manage AWS CloudTrail resources.

###### Important

The procedure to create this action without AWS CloudTrail resources is not available in
the console. To use the CLI, see the procedures here or see [Migrate polling pipelines with an S3
source enabled for events](update-change-detection.md#update-change-detection-S3-event "update-change-detection.md#update-change-detection-S3-event").

For a pipeline with an Amazon S3 source, modify the pipeline so that change detection is
automated through EventBridge and with a source bucket that is enabled for event notifications.
This is the recommend method if you are using the CLI or CloudFormation to migrate your
pipeline.

###### Note

This includes using a bucket that is enabled for event notifications, where you do
not need to create a separate CloudTrail trail. If you are using the console, then an
event rule and CloudTrail trail are set up for you. For those steps, see [Migrate polling pipelines with an S3 source
and CloudTrail trail](update-change-detection.md#update-change-detection-S3 "update-change-detection.md#update-change-detection-S3").

- **CLI:** [Migrate polling pipelines with an
  S3 source and CloudTrail trail (CLI)](update-change-detection.md#update-change-detection-cli-S3 "update-change-detection.md#update-change-detection-cli-S3")
- **CloudFormation:** [Migrate polling pipelines with an
  S3 source and CloudTrail trail (CloudFormation template)](update-change-detection.md#update-change-detection-cfn-s3 "update-change-detection.md#update-change-detection-cfn-s3")
