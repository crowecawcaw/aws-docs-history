# Send CloudWatch Logs to Firehose

CloudWatch Logs events can be sent to Firehose using CloudWatch subscription filters. For more information, see [Subscription filters with Amazon Data Firehose](../../../AmazonCloudWatch/latest/logs/SubscriptionFilters.md#FirehoseExample "../../../AmazonCloudWatch/latest/logs/SubscriptionFilters.md#FirehoseExample").

CloudWatch Logs events are sent to Firehose in compressed gzip format. If you want to deliver decompressed log events to Firehose destinations, you can use the decompression feature in Firehose to automatically decompress CloudWatch Logs.

###### Important

Currently, Firehose does not support the delivery of CloudWatch Logs to Amazon OpenSearch Service destination
because Amazon CloudWatch combines multiple log events into one Firehose record and Amazon OpenSearch Service
cannot accept multiple log events in one record. As an alternative, you can consider
[Using subscription
filter for Amazon OpenSearch Service in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.md "../../../AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.md").
