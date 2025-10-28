# Connecting to Amazon S3 source actions that use

EventBridge and AWS CloudTrail

The instructions in this section provide the steps for creating the S3 source action
that uses AWS CloudTrail resources that you must create and manage. To use the S3 source
action with EventBridge that does not require additional AWS CloudTrail resources, use the CLI
instructions at [Migrate polling pipelines with an S3
source enabled for events](update-change-detection.md#update-change-detection-S3-event "update-change-detection.md#update-change-detection-S3-event").

###### Important

This procedure provides the steps for creating the S3 source action that uses
AWS CloudTrail resources that you must create and manage. The procedure to create this
action without AWS CloudTrail resources is not available in the console. To use the CLI,
see [Migrate polling pipelines with an S3
source enabled for events](update-change-detection.md#update-change-detection-S3-event "update-change-detection.md#update-change-detection-S3-event").

To add an Amazon S3 source action in CodePipeline, you choose either to:

- Use the CodePipeline console **Create pipeline** wizard ([Create a custom pipeline (console)](pipelines-create.md#pipelines-create-console "pipelines-create.md#pipelines-create-console")) or **Edit action** page to choose the
  **S3** provider option. The console creates an EventBridge rule
  and a CloudTrail trail that starts your pipeline when the source changes.
- Use the AWS CLI to add the action configuration for the `S3` action
  and create additional resources as follows:

      + Use the `S3` example action configuration in [Amazon S3 source action reference](action-reference-S3.md "action-reference-S3.md")
       to create your action as shown in [Create a pipeline (CLI)](pipelines-create.md#pipelines-create-cli "pipelines-create.md#pipelines-create-cli").
      + The change detection method defaults to starting the pipeline by
       polling the source. You should disable periodic checks and create the
       change detection rule and trail manually. Use one of the following
       methods: [Create an EventBridge rule for an
       Amazon S3 source (console)](create-cloudtrail-S3-source-console.md "create-cloudtrail-S3-source-console.md"), [Create an EventBridge rule for an Amazon S3
       source (CLI)](create-cloudtrail-S3-source-cli.md "create-cloudtrail-S3-source-cli.md"), or [Create an EventBridge rule for an Amazon S3
       source (AWS CloudFormation template)](create-cloudtrail-S3-source-cfn.md "create-cloudtrail-S3-source-cfn.md") .

  AWS CloudTrail is a service that logs and filters events on your Amazon S3 source bucket. The
  trail sends the filtered source changes to the EventBridge rule. The EventBridge rule detects the
  source change and then starts your pipeline.

**Requirements:**

- If you are not creating a trail, use an existing AWS CloudTrail trail for logging
  events in your Amazon S3 source bucket and sending filtered events to the EventBridge
  rule.
- Create or use an existing S3 bucket where AWS CloudTrail can store its log files.
  AWS CloudTrail must have the permissions required to deliver log files to an Amazon S3
  bucket. The bucket cannot be configured as a [Requester Pays](../../../AmazonS3/latest/dev/RequesterPaysBuckets.md "../../../AmazonS3/latest/dev/RequesterPaysBuckets.md") bucket. When you create an Amazon S3 bucket as part of
  creating or updating a trail in the console, AWS CloudTrail attaches the required
  permissions to a bucket for you. For more information, see [Amazon S3 Bucket Policy for CloudTrail](../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md").
