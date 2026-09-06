# Describe a streaming table delivery

Retrieve the configuration and current status of a streaming table delivery, including
its state (`ChannelStatus`) and status reason
(`ChannelStatusReason`). Use this to verify that a delivery reached the
ACTIVE state after creation, or to diagnose a delivery in the FAILED state.

## Using the AWS Management Console

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. In the navigation pane, choose **Streaming tables**. From
   the list of deliveries, choose the delivery that you want to view.
3. The delivery details page shows the delivery status, source stream,
   destination table, data freshness, service access role, and dead-letter
   queue configuration. Use the **Configurations** tab to view
   source and destination settings, and the **Logs and tags**
   tab to view log delivery and tags.

## Using the AWS CLI

Use the `describe-channel` command and pass the channel ARN
(`ChannelARN`) returned by `create-channel`:

```
aws kinesis describe-channel \
    --channel-arn "arn:aws:kinesis:us-east-1:123456789012:channel/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
```

The response includes the delivery's `ChannelStatus` (CREATING, ACTIVE,
UPDATING, DELETING, or FAILED), the source stream configuration, the destination
table configuration, and the data freshness setting. A delivery is ready to receive
records when `ChannelStatus` is ACTIVE.

**API reference** – see `DescribeChannel` in
the _Amazon Kinesis Data Streams API Reference_.
