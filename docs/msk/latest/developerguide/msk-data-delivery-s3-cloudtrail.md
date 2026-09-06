

# CloudTrail logging
<a name="msk-data-delivery-s3-cloudtrail"></a>

All Channel API calls are logged in AWS CloudTrail: `CreateChannel`, `DescribeChannel`, `UpdateChannel`, `DeleteChannel`, `ListChannels`. Each event includes the caller identity, timestamp, source IP address, request parameters, and response elements.

The following is an example CloudTrail event.

```
{
    "eventVersion": "1.08",
    "eventSource": "kafka.amazonaws.com",
    "eventName": "CreateChannel",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "203.0.113.25",
    "userAgent": "aws-cli/2.15.0",
    "requestParameters": {
        "clusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/my-express-cluster/abc123",
        "channelName": "orders-channel",
        "topicConfigurationList": [
            {
                "topicArn": "arn:aws:kafka:us-east-1:123456789012:topic/my-express-cluster/abc123/orders-topic",
                "recordConverter": { "valueConverter": "JSON" }
            }
        ]
    },
    "responseElements": {
        "channelArn": "arn:aws:kafka:us-east-1:123456789012:channel/my-express-cluster/abc123/orders-channel",
        "clusterOperationArn": "arn:aws:kafka:us-east-1:123456789012:cluster-operation/my-express-cluster/abc123/..."
    }
}
```