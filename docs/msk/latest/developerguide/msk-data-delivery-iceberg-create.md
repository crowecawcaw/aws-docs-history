

# Create a Channel
<a name="msk-data-delivery-iceberg-create"></a>

## Using the AWS Management Console
<a name="msk-data-delivery-iceberg-create-console"></a>

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the navigation pane, choose **Clusters**.

1. Choose the name of your Amazon MSK Provisioned cluster with Express brokers.

1. Choose the **Channel** tab, then choose **Create Channel**.

1. In the **Source configuration** step:
   + **Channel name:** enter the name of the Channel to create.
   + **Topic:** select an existing topic. Create a new topic if one doesn't exist yet.

1. Proceed to the **Destination configuration** step.

1. Under **Destination type**, select **streaming tables for Apache Iceberg**.
   + Select a **Record conversion format** (JSON or JSON (Glue Schema Registry)). Also choose the Glue Schema Registry schema for plain JSON.
   + Under **Warehouse location**:
     + Select **Current account** or **Cross account**.
     + Select an S3 Table bucket, or enter an S3 Table bucket ARN if **Cross account** was selected.
   + Under **Destination table**:
     + Select or enter the **Namespace**.
     + Enter the **Table name** and the **Column name**, and choose the **Compression type** (ZSTD or Snappy).
   + For streaming tables for Apache Iceberg, **Partitioning** is time-based.
   + Set the **Data freshness** (5–15 minutes).

1. Proceed to the **Additional configuration** step.

1. Under **Encryption configuration**, optionally select a customer-managed key to customize your encryption settings.

1. Under **Service Access**, select or create an IAM role with the required permissions.

1. Under **Dead-letter queue**, select **Current account** or **Cross account** and specify the S3 bucket URI for unprocessable records. Optionally enter an error output prefix. If **Cross account** was selected, you may need to enter an additional **Account ID**.

1. (Optional) Under **Log Delivery**, select an Amazon CloudWatch log group, Amazon S3 bucket, or Amazon Data Firehose stream to send logs for monitoring and troubleshooting.

1. (Optional) Add tags.

1. Proceed to the **Review** step.

1. Review and choose **Create Channel**.

The Channel enters the **Creating** state and transitions to **Active** once the delivery pipeline is fully provisioned.

## Using the AWS CLI
<a name="msk-data-delivery-iceberg-create-cli"></a>

The source topic is set in `TopicConfigurationList` (exactly one topic). The destination is set in either `IcebergDestinationConfiguration` or `S3DestinationConfiguration` (mutually exclusive), and each destination configuration contains its own `ServiceExecutionRoleArn`, `DataFreshnessInSeconds` (300–900, default 600), and `DeadLetterQueueS3`.

To create a Channel with a streaming tables for Apache Iceberg destination, use the following command.

```
aws kafka create-channel \
    --cluster-arn "arn:aws:kafka:us-east-1:123456789012:cluster/my-express-cluster/abc123" \
    --channel-name "orders-channel" \
    --topic-configuration-list '[
        {
            "TopicArn": "arn:aws:kafka:us-east-1:123456789012:topic/my-express-cluster/abc123/orders-topic",
            "RecordConverter": { "ValueConverter": "JSON" },
            "RecordSchema": { "GsrArn": "arn:aws:glue:us-east-1:123456789012:schema/my-registry/orders-schema" }
        }
    ]' \
    --iceberg-destination-configuration '{
        "ServiceExecutionRoleArn": "arn:aws:iam::123456789012:role/MSKChannelRole",
        "DataFreshnessInSeconds": 300,
        "Catalog": {
            "WarehouseLocation": "arn:aws:s3tables:us-east-1:123456789012:bucket/analytics-table-bucket"
        },
        "DeadLetterQueueS3": {
            "BucketArn": "arn:aws:s3:::my-dlq-bucket",
            "ErrorOutputPrefix": "dlq/"
        },
        "DestinationTableList": [
            {
                "DestinationDatabaseName": "analytics_db",
                "DestinationTableName": "orders_iceberg",
                "PartitionSpec": {
                    "PartitionStrategy": "TIME_HOUR",
                    "SourceList": [ { "SourceName": "timestamp" } ]
                }
            }
        ],
        "CompressionType": "ZSTD"
    }'
```
+ `RecordConverter.ValueConverter` is `JSON` (plain JSON — provide `RecordSchema.GsrArn`, the ARN of the Glue Schema Registry schema that defines the data) or `JSON_SCHEMA_GSR` (GSR-serialized JSON — the schema ID is embedded in each record).
+ `Catalog` is optional. If you provide `Catalog.CatalogArn`, it must reference the S3 Tables catalog (`.../catalog/s3tablescatalog/<bucket-name>`); if omitted, Amazon MSK derives it from `WarehouseLocation`.
+ `CompressionType` is `ZSTD` (default) or `SNAPPY`. Partitioning uses `PartitionStrategy: TIME_HOUR` with a single timestamp source column.

The response is the same for both destinations.

```
{
    "ChannelArn": "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-channel",
    "ClusterOperationArn": "arn:aws:kafka:us-east-1:123456789012:cluster-operation/my-express-cluster/abc123/..."
}
```

**Note**  
Use the `ClusterOperationArn` to track the asynchronous operation's status and any error message. The Channel starts in `CREATING` and transitions to `ACTIVE` when provisioning completes.

**API reference** — see `CreateChannel` in the *Amazon MSK API Reference*.