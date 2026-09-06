

# Delete an Amazon S3 delivery
<a name="data-delivery-s3-delete"></a>

 Delete an Amazon S3 delivery when you no longer need it. Deleting a delivery stops delivery from the source stream to the destination. Data already delivered to the Amazon S3 bucket is not removed. 

**Important**  
 Deleting a delivery is irreversible. Undelivered records in the stream are not delivered. Data already delivered to the destination remains intact and accessible. 

## Using the AWS Management Console
<a name="data-delivery-s3-delete-console"></a>

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis), choose **S3 general purpose delivery**, and then choose the delivery you want to delete.

1. On the delivery details page, choose **Delete**.

1. In the confirmation dialog box, confirm the deletion. The delivery is removed from the list when the deletion completes.

## Using the AWS CLI
<a name="data-delivery-s3-delete-cli"></a>

 Use the `delete-channel` command: 

```
aws kinesis delete-channel \
    --channel-arn "arn:aws:kinesis:us-east-1:123456789012:channel/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
```

 To avoid ongoing charges, also delete the IAM role you created for the delivery and, if you no longer need them, the destination bucket and dead-letter queue bucket. For a full cleanup walkthrough, see [Getting started with S3 general purpose delivery](data-delivery-s3-getting-started.md). 

**Note**  
 A stream cannot be deleted while it has active deliveries. To delete the stream, first delete all deliveries attached to it. To find them, use `list-channels` with a stream filter. See [List Amazon S3 deliveries](data-delivery-s3-list.md). 

 **API reference** – see `DeleteChannel` in the *Amazon Kinesis Data Streams API Reference*. 