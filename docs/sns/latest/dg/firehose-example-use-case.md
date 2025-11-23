# Amazon SNS message archiving and analytics: An example

use case for airline ticketing platforms

This topic provides a tutorial for a common use case of archiving and analyzing Amazon SNS
messages.

The setting of this use case is an airline ticketing platform that operates in a regulated
environment.

1. The platform is subject to a compliance framework that requires the company to archive
   all ticket sales for at least five years.
2. To meet the compliance goal on data retention, the company subscribes an
   delivery stream to an existing Amazon SNS topic.
3. The destination for the delivery stream is an Amazon Simple Storage Service (Amazon S3) bucket. With this
   configuration, all events published to the SNS topic are archived in the Amazon S3 bucket.
   The following diagram shows the architecture of this configuration:

![An AWS architecture for an airline ticketing platform, illustrating how ticket sales data is processed and archived. It shows the flow of data from a Lambda function through an Amazon SNS topic, which then distributes messages to Amazon SQS queues for payment processing and fraud detection, handled by respective Lambda functions. The data is also streamed via Data Firehose to an Amazon S3 bucket for long-term archival, supporting compliance with data retention requirements. This setup enables the platform to run detailed analytics on ticket sales data using tools like Amazon Athena.](images/sns-archiving-use-case.png)
To run analytics and gain insights on ticket sales, the company runs SQL queries using
Amazon Athena. For example, the company can query to learn about the most popular destinations and
the most frequent flyers.

To create the AWS resources for this use case, you can use the AWS Management Console or an CloudFormation
template.

###### Topics

- [Setting-up initial AWS resources for message archiving and
  analytics](firehose-example-initial-resources.md "firehose-example-initial-resources.md")
- [Setting-up a Firehose delivery stream for message archiving](firehose-example-create-delivery-stream.md "firehose-example-create-delivery-stream.md")
- [Subscribing the delivery stream to the topic](firehose-example-subscribe-delivery-stream-to-topic.md "firehose-example-subscribe-delivery-stream-to-topic.md")
- [Testing and querying a configuration for effective data management](firehose-example-test-and-query.md "firehose-example-test-and-query.md")
- [Automating message archiving with an CloudFormation template](firehose-example-cfn.md "firehose-example-cfn.md")
