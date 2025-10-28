# Configure multiple file directories and

streams

By specifying multiple flow configuration settings, you can configure the agent to
monitor multiple file directories and send data to multiple streams. In the following
configuration example, the agent monitors two file directories and sends data to a Kinesis
data stream and a Firehose stream respectively. You can specify different
endpoints for Kinesis Data Streams and Amazon Data Firehose so that your data stream and Firehose stream don’t
need to be in the same Region.

```
{
    "cloudwatch.emitMetrics": `true`,
    "kinesis.endpoint": "`https://your/kinesis/endpoint`",
    "firehose.endpoint": "`https://your/firehose/endpoint`",
    "flows": [
        {
            "filePattern": "`/tmp/app1.log*`",
            "kinesisStream": "`yourkinesisstream`"
        },
        {
            "filePattern": "`/tmp/app2.log*`",
            "deliveryStream": "`yourfirehosedeliverystream`"
        }
    ]
}
```

For more detailed information about using the agent with Amazon Kinesis Data Streams, see
[Writing to Amazon Kinesis Data Streams with Kinesis Agent](../../../kinesis/latest/dev/writing-with-agents.md "../../../kinesis/latest/dev/writing-with-agents.md").
