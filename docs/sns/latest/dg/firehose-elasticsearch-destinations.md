# Integrating Amazon SNS messages with Amazon OpenSearch Service

destinations

This section explains how delivery streams publish data to Amazon OpenSearch Service (OpenSearch Service).

![A publisher sends messages to an Amazon SNS topic, which then distributes these messages to multiple Amazon SQS queues. Messages from these queues can be processed by Lambda functions or sent through an Data Firehose delivery stream to an Amazon OpenSearch Service, creating a searchable message index. This setup demonstrates an advanced message routing and processing scenario using AWS services.](images/firehose-architecture-es.png)

###### Topics

- [Archived message format](firehose-archived-message-format-elasticsearch.md "firehose-archived-message-format-elasticsearch.md")
- [Analyzing messages](firehose-message-analysis-elasticsearch.md "firehose-message-analysis-elasticsearch.md")
