# AWS CloudTrail in AWS GovCloud (US)

With AWS CloudTrail, you can monitor your AWS deployments in the cloud by getting a history of AWS API calls for your account, including API calls made via the AWS Management Console, the AWS SDKs, the command line tools, and higher-level AWS services. You can also identify which users and accounts called AWS APIs for services that support CloudTrail, the source IP address the calls were made from, and when the calls occurred. You can integrate CloudTrail into applications using the API, automate trail creation for your organization, check the status of your trails, and control how administrators turn CloudTrail logging on and off.

## How AWS CloudTrail differs for AWS GovCloud (US)

The following list details the differences for using this service in AWS GovCloud (US) Regions compared to other AWS Regions:

- As of November 22, 2021, AWS CloudTrail changed how trails capture global
  service events. Now, events created by CloudFront, IAM, and AWS STS are
  recorded in the AWS Region in which they were created, the AWS GovCloud (US-West) Region,
  us-gov-west-1. This makes CloudTrail's treatment of these services consistent with that of other
  AWS global services.

To continue receiving global service events outside of AWS GovCloud (US-West), be
sure to convert _single-Region trails_ using global service events
outside of AWS GovCloud (US-West) into _multi-Region trails_. For
more information about using the CLI to update or create trails for global service
events, see [Using update-trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.md").

In contrast, the **Event history** in the CloudTrail console and the **aws cloudtrail lookup-events** command will show these events
in the Region where they occurred.

- For all AWS GovCloud (US) accounts created after 12/15/2014, AWS CloudTrail event log delivery to
  Amazon S3 is enabled automatically. However, you must set up Amazon SNS notifications. You can turn
  off logging through the AWS CloudTrail console for the AWS GovCloud (US) Region.
- If you are using AWS Direct Connect, you must enable CloudTrail in your standard AWS account (not your
  AWS GovCloud (US) account) and enable logging.
- The Amazon S3 and Amazon SNS policy statements must refer to the ARN for AWS GovCloud (US) Regions.
  For more information, see [Amazon Resource Names (ARNs) in GovCloud (US)
  Regions](using-govcloud-arns.md "using-govcloud-arns.md").
- The following CloudTrail Lake features are currently not available in the
  AWS GovCloud (US) Regions:
  - CloudTrail Lake integrations
  - CloudTrail Lake query generation
  - CloudTrail Lake query results summarization
  - CloudTrail Lake event data stores for AWS Config configuration items, AWS Audit Manager evidence, and
    events outside of AWS.
  - The **Activity summary** widget on the Highlights dashboard.

- CloudTrail network activity events are only available for AWS KMS, Amazon S3, AWS CloudTrail, and AWS Secrets Manager. You can also log network activity events in
  Amazon CloudWatch that are sent through the monitoring VPC interface endpoint. For more information, see [Using CloudWatch, CloudWatch Synthetics, and CloudWatch Network Monitoring with interface VPC endpoints](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-and-interface-VPC.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-and-interface-VPC.md").
- CloudTrail enriched events are currently not supported.
- To enable CloudTrail to write log files to your bucket in AWS GovCloud (US) Regions, you can
  use the following policy.

###### Warning

If the bucket already has one or more policies attached, add the statements for CloudTrail
access to that policy or policies. We recommend that you evaluate the resulting set of
permissions to be sure they are appropriate for the users who will be accessing the
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSCloudTrailAclCheck20131101",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws-us-gov:s3:::`amzn-s3-demo-logging-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws-us-gov:cloudtrail:`region`:`myAccountID`:trail/`trailName`"
 }
 }
 },
 {
 "Sid": "AWSCloudTrailWrite20131101",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws-us-gov:s3:::`amzn-s3-demo-logging-bucket`/`[optional] prefix`/AWSLogs/`myAccountID`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceArn": "arn:aws-us-gov:cloudtrail:`region`:`myAccountID`:trail/`trailName`"
 }
 }
 }
 ]
}`

```

For more information, see [Amazon S3 bucket policy](../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md") and [Amazon SNS topic policy for CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-permissions-for-sns-notifications.md "../../../awscloudtrail/latest/userguide/cloudtrail-permissions-for-sns-notifications.md").

###### Note

This note applies to bucket policies that use a CloudTrail account ID as the Principal. In AWS GovCloud (US) Regions, do not add CloudTrail account IDs of non-isolated Regions to
your policy templates, or an "Invalid principal in policy" error will occur. Similarly, if
you are in a non-isolated Region, do not add the CloudTrail account ID for AWS GovCloud (US) to your
policy templates.

## Documentation for AWS CloudTrail

[AWS CloudTrail documentation](https://aws.amazon.com/documentation/cloudtrail/ "https://aws.amazon.com/documentation/cloudtrail/").

## Services supported within CloudTrail

CloudTrail supports logging for the services supported in the AWS GovCloud (US) Regions that are integrated with CloudTrail. You can find the specifics for each supported service in that service's guide. For more information, see [AWS service topics for CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-list "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-list") in the
_AWS CloudTrail User Guide_.

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- CloudTrail
  logs do not contain export-controlled data.
- CloudTrail configuration data may not contain export-controlled
  data.
