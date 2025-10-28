# Storing and analyzing Amazon SNS messages in Amazon S3

destinations

This topic explains how delivery streams publish data to Amazon Simple Storage Service (Amazon S3).

![The integration and workflow of Amazon services for message handling. It shows how a publisher sends messages to an Amazon SNS topic, which then fans out messages to multiple Amazon SQS queues and an Data Firehose delivery stream. From there, messages can be processed by Lambda functions or stored persistently in an Amazon S3 bucket.](images/firehose-architecture-s3.png)

###### Topics

- [Formatting notifications for storage in Amazon S3 destinations](firehose-archived-message-format-S3.md "firehose-archived-message-format-S3.md")
- [Analyzing messages stored in Amazon S3 using Athena](firehose-message-analysis-s3.md "firehose-message-analysis-s3.md")
