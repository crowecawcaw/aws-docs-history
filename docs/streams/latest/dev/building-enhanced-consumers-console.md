# Manage enhanced fan-out consumers with the AWS CLI or APIs

Consumers that use _enhanced fan-out_ in Amazon Kinesis Data Streams can receive
records from a data stream with dedicated throughput of up to 2 MB of data per second
per shard. For more information, see [Develop enhanced fan-out consumers with dedicated
throughput](enhanced-consumers.md "enhanced-consumers.md").

You can use AWS CLI or Kinesis Data Streams APIs to register, describe, list, and deregister a consumer that uses enhanced fan-out in Kinesis Data Streams.

## Manage consumers using the AWS CLI

You can register, describe, list, and deregister enhanced fan-out consumers using the AWS CLI. For examples, see the following documentation.

[register-stream-consumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/register-stream-consumer.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/register-stream-consumer.html")

Registers a consumer for a Kinesis data stream. You can apply tags while registering the consumer.

[describe-stream-consumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream-consumer.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream-consumer.html")

Gets the description of a registered consumer with either consumer ARN or consumer name and stream ARN combination.

[list-stream-consumers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-stream-consumers.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-stream-consumers.html")

Lists the consumers registered to receive data from a stream using enhanced fan-out.

[deregister-stream-consumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/deregister-stream-consumer.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/deregister-stream-consumer.html")

Deregister a consumer with either consumer ARN or consumer name and stream ARN combination.

## Manage consumers using the Kinesis Data Streams APIs

You can register, describe, list, and deregister enhanced fan-out consumers using the Kinesis Data Streams APIs. For examples, see the following documentation.

[RegisterStreamConsumer](../../../kinesis/latest/APIReference/API_RegisterStreamConsumer.md "../../../kinesis/latest/APIReference/API_RegisterStreamConsumer.md")

Registers a consumer for a Kinesis data stream with tags. You can apply tags while registering the consumer.

[DescribeStreamConsumer](../../../kinesis/latest/APIReference/API_DescribeStreamConsumer.md "../../../kinesis/latest/APIReference/API_DescribeStreamConsumer.md")

Gets the description of a registered consumer with either consumer ARN or consumer name and stream ARN combination.

[ListStreamConsumers](../../../kinesis/latest/APIReference/API_ListStreamConsumers.md "../../../kinesis/latest/APIReference/API_ListStreamConsumers.md")

Lists the consumers registered to receive data from a stream using enhanced fan-out.

[DeregisterStreamConsumer](../../../kinesis/latest/APIReference/API_DeregisterStreamConsumer.md "../../../kinesis/latest/APIReference/API_DeregisterStreamConsumer.md")

Deregister a consumer with either consumer ARN or consumer name and stream ARN combination.

## Tagging consumers

You can assign your own metadata to streams and enhanced fan-out consumers you create in Kinesis Data Streams in the form of tags. You can use tags to categorize and track costs of your consumers. You can also control access to consumers using tags with [attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"). For more information, see [Tag your Amazon Kinesis Data Streams resources](tagging.md "tagging.md").
