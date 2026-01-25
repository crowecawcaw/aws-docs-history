# Managing MemoryDB Amazon SNS notifications

You can configure MemoryDB to send notifications for important cluster events using
Amazon Simple Notification Service (Amazon SNS). In these examples, you will configure a cluster with the Amazon
Resource Name (ARN) of an Amazon SNS topic to receive notifications.

###### Note

This topic assumes that you've signed up for Amazon SNS and have set up and subscribed to an
Amazon SNS topic. For information on how to do this, see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").

## Adding an Amazon SNS topic

The following sections show you how to add an Amazon SNS topic using the AWS Console, the AWS CLI, or
the MemoryDB API.

### Adding an Amazon SNS topic (Console)

The following procedure shows you how to add an Amazon SNS topic for a cluster.

###### Note

This process can also be used to modify the Amazon SNS topic.

###### To add or modify an Amazon SNS topic for a cluster (Console)

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. In **Clusters**,
   choose the cluster for which you want to add or modify an Amazon SNS topic ARN.
3. Choose **Modify**.
4. In **Modify Cluster** under **Topic for SNS Notification**, choose the SNS topic
   you want to add, or choose **Manual ARN input**
   and type the ARN of the Amazon SNS topic.
5. Choose **Modify**.

### Adding an Amazon SNS topic (AWS CLI)

To add or modify an Amazon SNS topic for a cluster,
use the AWS CLI command `update-cluster`.

The following code example adds an Amazon SNS topic arn to _my-cluster_.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name `my-cluster` \
    --sns-topic-arn `arn:aws:sns:us-east-1:565419523791:memorydbNotifications`
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name `my-cluster` ^
    --sns-topic-arn `arn:aws:sns:us-east-1:565419523791:memorydbNotifications`
```

For more information,
see [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md")
.

### Adding an Amazon SNS topic (MemoryDB API)

To add or update an Amazon SNS topic for a cluster, call the
`UpdateCluster` action with the following parameters:

- `ClusterName``=my-cluster`
- `SnsTopicArn``=arn%3Aaws%3Asns%3Aus-east-1%3A565419523791%3AmemorydbNotifications`

To add or update an Amazon SNS topic for a cluster,
call the `UpdateCluster` action.

For more information,
see [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md").

## Enabling and disabling Amazon SNS notifications

You can turn notifications on or off for a cluster. The following
procedures show you how to disable Amazon SNS notifications.

### Enabling and disabling Amazon SNS notifications (Console)

###### To disable Amazon SNS notifications using the AWS Management Console

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. Choose the radio button to the left of the cluster you want to modify notification for.
3. Choose **Modify**.
4. In **Modify Cluster** under **Topic for SNS Notification**,
   choose _Disable Notifications_.
5. Choose **Modify**.

### Enabling and disabling Amazon SNS notifications (AWS CLI)

To disable Amazon SNS notifications, use the command `update-cluster`
with the following parameters:

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name `my-cluster` \
    --sns-topic-status `inactive`
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name `my-cluster` ^
    --sns-topic-status `inactive`
```

### Enabling and disabling Amazon SNS notifications (MemoryDB API)

To disable Amazon SNS notifications, call the `UpdateCluster` action with the
following parameters:

- `ClusterName``=my-cluster`
- `SnsTopicStatus``=inactive`

This call returns output similar to the following:

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=UpdateCluster
    &ClusterName=my-cluster
    &SnsTopicStatus=inactive
    &Version=2021-01-01
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20210801T220302Z
    &X-Amz-Algorithm=Amazon4-HMAC-SHA256
    &X-Amz-Date=20210801T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Expires=20210801T220302Z
    &X-Amz-Credential=<credential>
    &X-Amz-Signature=<signature>
```
