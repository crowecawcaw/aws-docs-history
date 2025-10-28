# Events placeholder bucket reference

This section is a reference only. For information about creating a pipeline with event detection resources, see
[Source actions and change detection
methods](change-detection-methods.md "change-detection-methods.md").

Source actions provided by Amazon S3 and CodeCommit use event-based change detection resources to
trigger your pipeline when a change is made in the source bucket or repository. These resources
are the CloudWatch Events rules that are configured to respond to events in the pipeline source, such as a
code change to the CodeCommit repository. When you use CloudWatch Events for an Amazon S3 source, you must turn on
CloudTrail so the events are logged. CloudTrail requires an S3 bucket where it can send its digests. You can
access the log files for your CloudWatch Events resources from the custom bucket, but you cannot access the
data from the placeholder bucket.

- If you used the CLI or AWS CloudFormation to set up the CloudWatch Events resources, you can find your CloudTrail files in the bucket that
  you specified when you set up your pipeline.
- If you used the console to set up your pipeline with an S3 source, the console uses a
  CloudTrail placeholder bucket when it creates your CloudWatch Events resources for you. CloudTrail digests are
  stored in the placeholder bucket in the AWS Region where the pipeline is created.
  You can change the configuration if you want to use a bucket other than the placeholder bucket.

###### Note

Data written to CloudTrail placeholder buckets automatically expires after one day and is not
retained.

For more information about finding and managing your CloudTrail log files, see [Getting and Viewing Your CloudTrail Log
Files](../../../awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.md "../../../awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.md").

###### Topics

- [Events placeholder bucket names by Region](#reference-ct-placeholder-buckets-list "#reference-ct-placeholder-buckets-list")

## Events placeholder bucket names by Region

This table lists the names of the S3 placeholder buckets that contain log files that track
change detection events for pipelines with Amazon S3 source actions.

| Region name               | Placeholder bucket name                                        | Region identifier |
| ------------------------- | -------------------------------------------------------------- | ----------------- |
| US East (Ohio)            | codepipeline-cloudtrail-placeholder-bucket-us-east-2           | us-east-2         |
| US East (N. Virginia)     | codepipeline-cloudtrail-placeholder-bucket-us-east-1           | us-east-1         |
| US West (N. California)   | codepipeline-cloudtrail-placeholder-bucket-us-west-1           | us-west-1         |
| US West (Oregon)          | codepipeline-cloudtrail-placeholder-bucket-us-west-2           | us-west-2         |
| Canada (Central)          | codepipeline-cloudtrail-placeholder-bucket-ca-central-1        | ca-central-1      |
| Europe (Frankfurt)        | codepipeline-cloudtrail-placeholder-bucket-eu-central-1        | eu-central-1      |
| Europe (Ireland)          | codepipeline-cloudtrail-placeholder-bucket-eu-west-1           | eu-west-1         |
| Europe (London)           | codepipeline-cloudtrail-placeholder-bucket-eu-west-2           | eu-west-2         |
| Europe (Paris)            | codepipeline-cloudtrail-placeholder-bucket-eu-west-3           | eu-west-3         |
| Europe (Stockholm)        | codepipeline-cloudtrail-placeholder-bucket-eu-north-1          | eu-north-1        |
| Asia Pacific (Hong Kong)  | codepipeline-cloudtrail-placeholder-bucket-ap-east-1           | ap-east-1         |
| Asia Pacific (Hyderabad)  | codepipeline-cloudtrail-placeholder-bucket-ap-south-2          | ap-south-2        |
| Asia Pacific (Jakarta)    | codepipeline-cloudtrail-placeholder-bucket-ap-southeast-3      | ap-southeast-3    |
| Asia Pacific (Melbourne)  | codepipeline-cloudtrail-placeholder-bucket-ap-southeast-4      | ap-southeast-4    |
| Asia Pacific (Mumbai)     | codepipeline-cloudtrail-placeholder-bucket-ap-south-1          | ap-south-1        |
| Asia Pacific (Osaka)      | codepipeline-cloudtrail-placeholder-bucket-ap-northeast-3-prod | ap-northeast-3    |
| Asia Pacific (Tokyo)      | codepipeline-cloudtrail-placeholder-bucket-ap-northeast-1      | ap-northeast-1    |
| Asia Pacific (Seoul)      | codepipeline-cloudtrail-placeholder-bucket-ap-northeast-2      | ap-northeast-2    |
| Asia Pacific (Singapore)  | codepipeline-cloudtrail-placeholder-bucket-ap-southeast-1      | ap-southeast-1    |
| Asia Pacific (Sydney)     | codepipeline-cloudtrail-placeholder-bucket-ap-southeast-2      | ap-southeast-2    |
| Asia Pacific (Tokyo)      | codepipeline-cloudtrail-placeholder-bucket-ap-northeast-1      | ap-northeast-1    |
| Canada (Central)          | codepipeline-cloudtrail-placeholder-bucket-ca-central-1        | ca-central-1      |
| Europe (Frankfurt)        | codepipeline-cloudtrail-placeholder-bucket-eu-central-1        | eu-central-1      |
| Europe (Ireland)          | codepipeline-cloudtrail-placeholder-bucket-eu-west-1           | eu-west-1         |
| Europe (London)           | codepipeline-cloudtrail-placeholder-bucket-eu-west-2           | eu-west-2         |
| Europe (Milan)            | codepipeline-cloudtrail-placeholder-bucket-eu-south-1          | eu-south-1        |
| Europe (Paris)            | codepipeline-cloudtrail-placeholder-bucket-eu-west-3           | eu-west-3         |
| Europe (Spain)            | codepipeline-cloudtrail-placeholder-bucket-eu-south-2          | eu-south-2        |
| Europe (Stockholm)        | codepipeline-cloudtrail-placeholder-bucket-eu-north-1          | eu-north-1        |
| Europe (Zurich)\*         | codepipeline-cloudtrail-placeholder-bucket-eu-central-2        | eu-central-2      |
| Israel (Tel Aviv)         | codepipeline-cloudtrail-placeholder-bucket-il-central-1        | il-central-1      |
| Middle East (Bahrain)\*   | codepipeline-cloudtrail-placeholder-bucket-me-south-1          | me-south-1        |
| Middle East (UAE)         | codepipeline-cloudtrail-placeholder-bucket-me-central-1        | me-central-1      |
| South America (São Paulo) | codepipeline-cloudtrail-placeholder-bucket-sa-east-1           | sa-east-1         |
