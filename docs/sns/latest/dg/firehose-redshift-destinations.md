# Configuring Amazon SNS message delivery and analysis

in Amazon Redshift destinations

This topic explains how to fan out Amazon SNS notifications to an delivery stream, which
then publishes data to Amazon Redshift. With this setup, you can connect to the Amazon Redshift database
and use a SQL query tool to retrieve Amazon SNS messages that match specific criteria.

![Messages published by a sender to an Amazon SNS topic are distributed to multiple Amazon SQS queues for processing by Lambda functions, and also sent through an Data Firehose delivery stream to an Amazon Redshift cluster for storage and analysis in a message data warehouse. This setup demonstrates a robust message handling and data warehousing architecture using AWS services.](images/firehose-architecture-rs.png)

###### Topics

- [Structuring message archives in Amazon Redshift tables](firehose-archive-table-structure-redshift.md "firehose-archive-table-structure-redshift.md")
- [Analyzing messages stored in Amazon Redshift destinations](firehose-message-analysis-redshift.md "firehose-message-analysis-redshift.md")
