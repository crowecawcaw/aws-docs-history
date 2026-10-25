

# Update a connector
<a name="mkc-update-connector"></a>

This procedure describes how to update the configuration of an existing MSK Connect connector using the AWS Management Console.

**Updating connector configuration using the AWS Management Console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. In the left pane, under **MSK Connect**, choose **Connectors**.

1. Select an existig connector.

1. Choose **Edit connector configuration**.

1. Update the connector configuration. You can't override `connector.class` using UpdateConnector. The following example shows an example configuration for the Confluent Amazon S3 Sink connector. 

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

1. Choose **Submit**.

1. You can then monitor the current state of the operation in the **Operations** tab of the connector. 

Use the `skipHealthValidation` parameter to control whether Amazon MSK Connect runs connector-level and task-level health checks after it applies your update. If you set it to `true`, Amazon MSK Connect skips those checks. If you set it to `false` or omit it, the checks run.

Every update to a connector that is in the `PAUSED` state requires `skipHealthValidation` to be `true`, because Amazon MSK Connect cannot validate the health of a connector that is not processing records. For more information, see [Pause and resume a connector](mkc-pause-resume-connector.md).

To use the MSK Connect API to update the configuration of a connector, see [UpdateConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_UpdateConnector.html).