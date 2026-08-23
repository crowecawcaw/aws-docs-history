# Describe a Channel

## Using the AWS Management Console

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. In the navigation pane, choose **Clusters**.
3. Choose the name of your Amazon MSK Provisioned cluster with Express brokers.
4. Choose the **Channel** tab.
5. Choose the name of the Channel to describe.

The detail page shows source topic, destination, delivery settings, current state, and recent Amazon CloudWatch metrics.

## Using the AWS CLI

```
aws kafka describe-channel \
    --cluster-arn "arn:aws:kafka:us-east-1:123456789012:cluster/my-express-cluster/abc123" \
    --channel-arn "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-s3-channel"
```

The following is an example response for an Amazon S3 general purpose bucket destination.

```
{
    "ChannelArn": "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-s3-channel",
    "ChannelName": "orders-s3-channel",
    "TopicConfigurationList": [
        {
            "TopicArn": "arn:aws:kafka:us-east-1:123456789012:topic/my-express-cluster/abc123/orders-topic",
            "RecordConverter": { "ValueConverter": "JSON" }
        }
    ],
    "S3DestinationConfiguration": {
        "ServiceExecutionRoleArn": "arn:aws:iam::123456789012:role/MSKChannelRole",
        "DataFreshnessInSeconds": 300,
        "DeadLetterQueueS3": {
            "BucketArn": "arn:aws:s3:::my-dlq-bucket",
            "ErrorOutputPrefix": "dlq/"
        },
        "Storage": {
            "BucketArn": "arn:aws:s3:::my-delivery-bucket",
            "OutputPrefix": "expresslink/",
            "OutputKeyTemplate": "!{channel-id}/!{topic-name}/year=!{yyyy}/month=!{MM}/day=!{dd}/hour=!{HH}/!{topic-name}+!{partition-id}+!{kafka-offset}",
            "StorageClass": "STANDARD",
            "CompressionType": "GZIP"
        }
    },
    "Status": "ACTIVE",
    "DestinationType": "S3",
    "CreationTime": "2026-06-19T08:15:00.000Z"
}
```

###### Note

`Status` is one of `CREATING`, `ACTIVE`, `UPDATING`, `DELETING`, `FAILED`, `SUSPENDING`, `SUSPENDED`. When `Status` is `FAILED`, the response includes a `StateInfo` object with a `Code` and `Message` describing the cause. While an operation is in flight (`CREATING`, `UPDATING`, `DELETING`), the response also includes `ClusterOperationArn`.

**API reference** — see `DescribeChannel` in the _Amazon MSK API Reference_.
