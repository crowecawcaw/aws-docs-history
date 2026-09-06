# Delete a streaming table delivery

Delete a streaming table delivery when you no longer need it. Deleting a delivery stops
delivery from the source stream to the destination. Data already delivered to the
Iceberg table is not removed.

###### Important

Deleting a delivery is irreversible. Undelivered records in the stream are not
delivered. Data already delivered to the destination remains intact and accessible.

## Using the AWS Management Console

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis"),
   choose **Streaming tables**, and then choose the delivery you
   want to delete.
2. On the delivery details page, choose **Delete**.
3. In the confirmation dialog box, confirm the deletion. The delivery is
   removed from the list when the deletion completes.

## Using the AWS CLI

Use the `delete-channel` command:

```
aws kinesis delete-channel \
    --channel-arn "arn:aws:kinesis:us-east-1:123456789012:channel/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
```

To avoid ongoing charges, also delete the IAM role you created for the delivery
and, if you no longer need them, the destination table bucket and dead-letter queue
bucket. For a full cleanup walkthrough, see
[Getting started with streaming tables](data-delivery-st-getting-started.md "data-delivery-st-getting-started.md").

###### Note

A stream cannot be deleted while it has active deliveries. To delete the stream,
first delete all deliveries attached to it. To find them, use
`list-channels` with a stream filter. See
[List streaming table deliveries](data-delivery-st-list.md "data-delivery-st-list.md").

**API reference** – see `DeleteChannel` in
the _Amazon Kinesis Data Streams API Reference_.
