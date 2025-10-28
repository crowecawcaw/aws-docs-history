# Update a connector

This procedure describes how to update the configuration of an existing MSK Connect
connector using the AWS Management Console.

###### Updating connector configuration using the AWS Management Console

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/ "https://console.aws.amazon.com/msk/").
2. In the left pane, under **MSK Connect**, choose **Connectors**.
3. Select an existig connector.
4. Choose **Edit connector configuration**.
5. Update the connector configuration. You can't override `connector.class` using
   UpdateConnector. The following example shows an example configuration for the
   Confluent Amazon S3 Sink connector.

```
connector.class=io.confluent.connect.s3.S3SinkConnector
tasks.max=2
topics=my-example-topic
s3.region=us-east-1
s3.bucket.name=amzn-s3-demo-bucket
flush.size=1
storage.class=io.confluent.connect.s3.storage.S3Storage
format.class=io.confluent.connect.s3.format.json.JsonFormat
partitioner.class=io.confluent.connect.storage.partitioner.DefaultPartitioner
key.converter=org.apache.kafka.connect.storage.StringConverter
value.converter=org.apache.kafka.connect.storage.StringConverter
schema.compatibility=NONE
```

6. Choose **Submit**.
7. You can then monitor the current state of the operation in the
   **Operations** tab of the connector.
   To use the MSK Connect API to update the configuration of a connector, see [UpdateConnector](../../../MSKC/latest/mskc/API_UpdateConnector.md "../../../MSKC/latest/mskc/API_UpdateConnector.md").
