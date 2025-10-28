# Fanout to Firehose delivery streams

You can subscribe [delivery streams](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md") to
Amazon SNS topics, allowing you to send notifications to additional storage and analytics
endpoints. Messages published to an Amazon SNS topic are sent to the subscribed Firehose delivery
stream, and delivered to the destination as configured in Firehose. A subscription owner can
subscribe up to five Firehose delivery streams to an Amazon SNS topic. Each Firehose delivery stream has a
[default quota](../../../firehose/latest/dev/limits.md "../../../firehose/latest/dev/limits.md") for
requests and throughput per second. This limit could result in more messages published (inbound
traffic) than delivered (outbound traffic). When there's more inbound than outbound traffic,
your subscription can accumulate a large message backlog, causing high message delivery latency.
You can request an [increase in quota](https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase") based on the publish rate to avoid adverse impact on your workload.

Through Firehose delivery streams, you can fan out Amazon SNS notifications to Amazon Simple Storage Service (Amazon S3),
Amazon Redshift, Amazon OpenSearch Service (OpenSearch Service), and to third-party service providers such as Datadog, New Relic, MongoDB,
and Splunk.

For example, you can use this functionality to permanently store messages sent to a topic in
an Amazon S3 bucket for compliance, archival, or other purposes. To do this, create a Firehose delivery
stream with an Amazon S3 bucket destination, and subscribe that delivery stream to the Amazon SNS topic. As
another example, to perform analysis on messages sent to an Amazon SNS topic, create a delivery
stream with an OpenSearch Service index destination. You can then subscribe the Firehose delivery stream to the
Amazon SNS topic.

Amazon SNS also supports message delivery status logging for notifications sent to Firehose
endpoints. For more information, see [Amazon SNS message delivery status](sns-topic-attributes.md "sns-topic-attributes.md").
