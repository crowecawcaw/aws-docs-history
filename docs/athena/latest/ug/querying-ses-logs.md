# Query Amazon SES event logs

You can use Amazon Athena to query [Amazon Simple Email
Service](https://aws.amazon.com/ses/ "https://aws.amazon.com/ses/") (Amazon SES) event logs.

Amazon SES is an email platform that provides a convenient and cost-effective way to send and
receive email using your own email addresses and domains. You can monitor your Amazon SES sending
activity at a granular level using events, metrics, and statistics.

Based on the characteristics that you define, you can publish Amazon SES events to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"), [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/ "https://aws.amazon.com/kinesis/data-firehose/"), or [Amazon Simple Notification Service](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/"). After the information is stored in Amazon S3, you can query it from
Amazon Athena.

For an example Athena `CREATE TABLE` statement for Amazon SES logs, including steps
on how to create views and flatten nested arrays in Amazon SES event log data, see "Step 3: Using
Amazon Athena to query the SES event logs" in the AWS blog post [Analyzing Amazon SES event data with AWS Analytics Services](https://aws.amazon.com/blogs/messaging-and-targeting/analyzing-amazon-ses-event-data-with-aws-analytics-services/ "https://aws.amazon.com/blogs/messaging-and-targeting/analyzing-amazon-ses-event-data-with-aws-analytics-services/").
