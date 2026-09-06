

# Create a streaming table delivery
<a name="data-delivery-st-create"></a>

 Create a delivery that continuously sends records from an Amazon Kinesis Data Streams stream to a streaming table on Apache Iceberg backed by an S3 table bucket. You can create a delivery with the AWS Management Console or the AWS CLI. When you create a delivery, Amazon Kinesis Data Streams creates the destination Iceberg table in the table bucket you specify. 

**Note**  
 Before you create a delivery, complete the prerequisites in [Getting started with streaming tables](data-delivery-st-getting-started.md), including the IAM service execution role described in [IAM permissions for data delivery](data-delivery-iam.md). A streaming table delivery requires a schema in AWS Glue Schema Registry and a dead-letter queue. 

## Using the AWS Management Console
<a name="data-delivery-st-create-console"></a>

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the navigation pane, choose **Streaming tables**, and then choose **Create streaming table**.

1. **Step 1: Source configuration.** Under **Delivery details**, enter a **Delivery name**. Acceptable characters are uppercase and lowercase letters, numbers, underscores, hyphens, and periods. For **Source**, choose the On-Demand stream to deliver from. Only On-Demand streams are displayed. Choose **Next**.

1. **Step 2: Destination configuration.** Under **Record conversion configuration**, choose a **Record conversion format**:
   + **JSON** – JSON records that are validated against a schema in AWS Glue Schema Registry. Provide the schema ARN under **Glue Schema registry**.
   + **Glue Schema registry JSON** – Convert records using a AWS Glue Schema Registry JSON schema.

   For **Glue Schema registry**, specify the schema ARN or choose **Browse** to select one.

1. Under **Destination table**, specify where Amazon Kinesis Data Streams creates the Iceberg table:
   + **S3 table bucket ARN** – the ARN of the S3 table bucket. Choose **Browse S3** to select one.
   + **Namespace** – the namespace for the table (lowercase letters, numbers, and underscores only).
   + **Table name** – the name of the table to create.
   + **Column name** – the name of a date-time field from your schema used to partition the table by hour. The field must be a string field with the date-time format in the schema.
   + **Compression type** – choose **ZSTD**, **Snappy**, or **None**.
   + **Data freshness** – the maximum buffering time in seconds before records are delivered (minimum 300, maximum 900).

   Choose **Next**.

1. **Step 3: Additional configuration.** Configure the following, then choose **Next**:
   + **Encryption configuration** – by default, data is encrypted with default Amazon S3 encryption. To use a customer managed key, select **Customize encryption settings (advanced)**.
   + **Service access** – for **IAM role ARN**, choose or create the IAM role that grants access to the destination. Choose **Create IAM role** to create one.
   + **Dead letter queue** – for **S3 bucket URI**, choose the Amazon S3 bucket that stores undeliverable records. Optionally set an **S3 bucket error output prefix**.
   + **Log delivery** – optionally select **Deliver to Amazon CloudWatch Logs** to capture delivery diagnostics.
   + **Tags** – optionally add key-value tags to identify and organize your delivery.

1. **Step 4: Review and create.** Review your configuration, and then choose **Create streaming table**. The delivery transitions from CREATING to ACTIVE after provisioning is complete.

## Using the AWS CLI
<a name="data-delivery-st-create-cli"></a>

 Use the `create-channel` command to create a streaming table delivery. This configuration requires a schema from AWS Glue Schema Registry and a dead-letter queue: 

```
aws kinesis create-channel \
    --channel-name "my-iceberg-delivery" \
    --service-execution-role-arn "arn:aws:iam::123456789012:role/my-channel-role" \
    --stream-configuration-list '[
        {
            "StreamARN": "arn:aws:kinesis:us-east-1:123456789012:stream/my-stream",
            "RecordConfiguration": {
                "RecordFormatType": "JSON",
                "GSRSchemaARN": "arn:aws:glue:us-east-1:123456789012:schema/my-registry/my-schema"
            }
        }
    ]' \
    --s3-tables-destination-configuration '{
        "DataFreshnessInSeconds": 300,
        "DeadLetterQueueS3Configuration": {
            "BucketARN": "arn:aws:s3:::my-dlq-bucket",
            "ExpectedBucketOwner": "123456789012",
            "ErrorOutputPrefix": "dlq/"
        },
        "S3TablesConfigurationList": [
            {
                "TableBucketARN": "arn:aws:s3tables:us-east-1:123456789012:bucket/my-table-bucket",
                "Namespace": "my_namespace",
                "TableName": "my_table",
                "CompressionType": "ZSTD",
                "PartitionSpec": {
                    "PartitionFields": [
                        {
                            "SourceName": "timestamp",
                            "Transform": "TIME_HOUR"
                        }
                    ]
                }
            }
        ]
    }'
```

 The command returns the channel ARN (`ChannelARN`). Use it with `describe-channel` to verify the delivery reaches the ACTIVE state. See [Describe a streaming table delivery](data-delivery-st-describe.md). 

 **API reference** – see `CreateChannel` in the *Amazon Kinesis Data Streams API Reference*. 