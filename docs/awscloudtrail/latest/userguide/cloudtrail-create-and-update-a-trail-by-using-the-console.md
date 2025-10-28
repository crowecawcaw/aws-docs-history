# Creating and updating a trail with the console

You can use the CloudTrail console to create, update, or delete your trails. Trails created using the console are multi-Region. To create a trail that logs
events in only one AWS Region, [use
the AWS CLI](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-single "cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-single").

You can create up to five trails for each Region. After you create a trail, CloudTrail
automatically starts logging API calls and related events in your account to the Amazon S3 bucket
that you specify.

You can change the following settings for your trail using the CloudTrail console:

- You can change the S3 bucket location and specify a prefix.
- The management account for an AWS Organizations organization can convert an
  account-level trail to an organization trail, or can
  convert an organization trail to an account-level trail.
- You can enable or disable KMS key encryption.
- You can enable or disable [log file validation](cloudtrail-log-file-validation-intro.md "cloudtrail-log-file-validation-intro.md"). Log file validation
  allows you to determine whether a log file was modified, deleted, or
  unchanged after CloudTrail delivered it. By default, log file validation is enabled.
- You can configure a trail to send notifications to an Amazon SNS topic.
- You can configure a trail to send events to a CloudWatch Logs log group. Both the log group
  and IAM role must exist in your own account.
- You can update settings for management events, data events, network activity events, and Insights events.
- You can add or remove tags. You can add up to 50 tag key pairs to help you identify your trails.
  Using the CloudTrail console to create or update a trail provides the following advantages.

- If this is your first time creating a trail, using the CloudTrail console allows you to view the available feature and options.
- If you are configuring a trail to log data events, using the CloudTrail console allows you to view the available data types. For more information, see
  [Logging data events](logging-data-events-with-cloudtrail.md "logging-data-events-with-cloudtrail.md").
- If you are configuring a trail to network activity events, using the CloudTrail console allows you to view the available event sources. For more information, see
  [Logging network activity
  events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md").
  For information specific to creating a trail for an organization in AWS Organizations, see [Creating a trail for an organization](creating-trail-organization.md "creating-trail-organization.md").

###### Topics

- [Creating a trail with the CloudTrail console](cloudtrail-create-a-trail-using-the-console-first-time.md "cloudtrail-create-a-trail-using-the-console-first-time.md")
- [Updating a trail with the CloudTrail console](cloudtrail-update-a-trail-console.md "cloudtrail-update-a-trail-console.md")
- [Deleting a trail with the CloudTrail console](cloudtrail-delete-trails-console.md "cloudtrail-delete-trails-console.md")
- [Turning off logging for a trail](cloudtrail-turning-off-logging.md "cloudtrail-turning-off-logging.md")
