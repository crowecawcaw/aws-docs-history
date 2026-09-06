

# Delete a Channel
<a name="msk-data-delivery-s3-delete"></a>

Deleting a Channel stops delivery from the Kafka topic to the destination. Data already delivered (the S3 objects) is not deleted.

**Important**  
Deleting a Channel is irreversible. Any undelivered data in the topic will not be delivered. Data already delivered remains intact and accessible.

## Using the AWS Management Console
<a name="msk-data-delivery-s3-delete-console"></a>

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the navigation pane, choose **Clusters**.

1. Choose the name of your Amazon MSK Provisioned cluster with Express brokers.

1. Choose the **Channel** tab.

1. Select the Channel to delete and choose **Delete**.

1. In the confirmation dialog, type `delete` and choose **Delete**.

## Using the AWS CLI
<a name="msk-data-delivery-s3-delete-cli"></a>

```
aws kafka delete-channel \
    --cluster-arn "arn:aws:kafka:us-east-1:123456789012:cluster/my-express-cluster/abc123" \
    --channel-arn "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-s3-channel"
```

Response:

```
{
    "ChannelArn": "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-s3-channel",
    "ClusterOperationArn": "arn:aws:kafka:us-east-1:123456789012:cluster-operation/my-express-cluster/abc123/..."
}
```

**Note**  
A `200` response indicates the deletion was accepted; the Channel transitions to `DELETING`. Track progress with the `ClusterOperationArn`.

**API reference** — see `DeleteChannel` in the *Amazon MSK API Reference*.