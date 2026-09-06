

# Create an Amazon S3 delivery
<a name="data-delivery-s3-create"></a>

 Create a delivery that sends records from an Amazon Kinesis Data Streams stream to a general purpose Amazon S3 bucket. You can create a delivery with the AWS Management Console or the AWS CLI. Records are delivered in their source format, batched into optimally sized objects, with configurable compression and an S3 key structure you define. 

**Note**  
 Before you create a delivery, complete the prerequisites in [Getting started with S3 general purpose delivery](data-delivery-s3-getting-started.md), including the IAM service execution role described in [IAM permissions for data delivery](data-delivery-iam.md). 

## Using the AWS Management Console
<a name="data-delivery-s3-create-console"></a>

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the navigation pane, choose **S3 general purpose delivery**, and then choose **Create delivery**.

1. **Step 1: Source configuration.** Under **Delivery details**, enter a **Delivery name**. For **Source**, choose the On-Demand stream to deliver from. Only On-Demand streams are displayed. Choose **Next**.

1. **Step 2: Destination configuration.** Choose a **Record format** (**JSON**, **STRING**, or **BYTE\_ARRAY**), and then specify the destination:
   + **S3 bucket ARN** – the ARN of the destination general purpose Amazon S3 bucket.
   + **Expected bucket owner** – the 12-digit AWS account ID of the expected bucket owner.
   + **Compression type** – choose **GZIP**, **ZSTD**, or **None**.
   + **Storage class** – optionally choose an Amazon S3 storage class.
   + **Output key template** – optionally define the Amazon S3 object key structure. For details, see [S3 output key template for Amazon S3 delivery](data-delivery-s3-key-template.md).
   + **Data freshness** – the maximum buffering time in seconds before records are delivered (minimum 300, maximum 900).

   Choose **Next**.

1. **Step 3: Additional configuration.** Configure encryption, service access (the IAM role), an optional dead-letter queue, log delivery, and tags. Choose **Next**.

1. **Step 4: Review and create.** Review your configuration, and then choose **Create delivery**. The delivery transitions from CREATING to ACTIVE after provisioning is complete.

## Using the AWS CLI
<a name="data-delivery-s3-create-cli"></a>

 Use the `create-channel` command to create an Amazon S3 delivery that sends records to a general purpose Amazon S3 bucket with JSON format and GZIP compression: 

```
aws kinesis create-channel \
    --channel-name "my-s3-delivery" \
    --service-execution-role-arn "arn:aws:iam::123456789012:role/my-channel-role" \
    --stream-configuration-list '[
        {
            "StreamARN": "arn:aws:kinesis:us-east-1:123456789012:stream/my-stream",
            "RecordConfiguration": {
                "RecordFormatType": "JSON"
            }
        }
    ]' \
    --s3-destination-configuration '{
        "DataFreshnessInSeconds": 300,
        "StorageConfiguration": {
            "BucketARN": "arn:aws:s3:::my-destination-bucket",
            "ExpectedBucketOwner": "123456789012",
            "CompressionType": "GZIP",
            "StorageClass": "STANDARD"
        }
    }'
```

 The command returns the channel ARN (`ChannelARN`). Use it with `describe-channel` to verify the delivery reaches the ACTIVE state. See [Describe an Amazon S3 delivery](data-delivery-s3-describe.md). To customize the Amazon S3 object key structure, see [S3 output key template for Amazon S3 delivery](data-delivery-s3-key-template.md). 

 **API reference** – see `CreateChannel` in the *Amazon Kinesis Data Streams API Reference*. 