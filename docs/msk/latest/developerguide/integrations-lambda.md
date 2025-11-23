# AWS Lambda integration with Amazon MSK

The Lambda integration connects your Amazon MSK cluster to the selected Lambda function, using an Event Source Mapping (ESM) which constantly polls for messages in your topic using a resource called Event Poller. The ESM evaluates the message backlog – using the [OffsetLag metric](https://aws.amazon.com/blogs/compute/offset-lag-metric-for-amazon-msk-as-an-event-source-for-lambda/ "https://aws.amazon.com/blogs/compute/offset-lag-metric-for-amazon-msk-as-an-event-source-for-lambda/") – for all partitions in the topic, and auto-scales Event Pollers to process messages efficiently.

For more information, see [Using Lambda with Amazon MSK](../../../lambda/latest/dg/with-msk.md "../../../lambda/latest/dg/with-msk.md") in the _AWS Lambda Developer Guide_.
