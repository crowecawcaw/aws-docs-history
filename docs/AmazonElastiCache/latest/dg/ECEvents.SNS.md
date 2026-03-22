# Managing ElastiCache Amazon SNS notifications

You can configure ElastiCache to send notifications for important cluster events using
Amazon Simple Notification Service (Amazon SNS). In these examples, you will configure a cluster with the Amazon
Resource Name (ARN) of an Amazon SNS topic to receive notifications.

###### Note

- This topic assumes that you've signed up for Amazon SNS and have set up and subscribed to an
  Amazon SNS topic. For information on how to do this, see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").
- By default, the `API modify-replication-group` affects all groups in a Region
  and not just the current specified group. If you want to configure one specific group in a Region
  differently than the other groups, you can use the `--notification-topic-arn` option
  to create a separate topic for that group.

## Adding an Amazon SNS topic

The following sections show you how to add an Amazon SNS topic using the AWS Console, the AWS CLI, or
the ElastiCache API.

### Adding an Amazon SNS topic (Console)

The following procedure shows you how to add an Amazon SNS topic for a cluster. When using Valkey or Redis OSS
to add an Amazon SNS topic for a replication group in step 2, instead of choosing a cluster,
choose a replication group. Then follow the same remaining steps.

###### Note

This process can also be used to modify the Amazon SNS topic.

###### To add or modify an Amazon SNS topic for a cluster (Console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In **Clusters**,
   choose the cluster for which you want to add or modify an Amazon SNS topic ARN.
3. Choose **Modify**.
4. In **Modify Cluster** under **Topic for SNS Notification**, choose the SNS topic
   you want to add, or choose **Manual ARN input**
   and type the ARN of the Amazon SNS topic.
5. Choose **Modify**.

### Adding an Amazon SNS topic (AWS CLI)

To add or modify an Amazon SNS topic for a cluster,
use the AWS CLI command `modify-cache-cluster`.

The following code example adds an Amazon SNS topic arn to _my-cluster_.

For Linux, macOS, or Unix:

```
aws elasticache modify-cache-cluster \
    --cache-cluster-id `my-cluster` \
    --notification-topic-arn `arn:aws:sns:us-west-2:123456789xxx:ElastiCacheNotifications`
```

For Windows:

```
aws elasticache modify-cache-cluster ^
    --cache-cluster-id `my-cluster` ^
    --notification-topic-arn `arn:aws:sns:us-west-2:123456789xx:ElastiCacheNotifications`
```

For more information, see [modify-cache-cluster](../../../cli/latest/reference/elasticache/modify-cache-cluster.md "../../../cli/latest/reference/elasticache/modify-cache-cluster.md").

### Adding an Amazon SNS topic (ElastiCache API)

To add or modify an Amazon SNS topic for a cluster, call the
`ModifyCacheCluster` action with the following parameters:

- `CacheClusterId``=my-cluster`
- `TopicArn``=arn%3Aaws%3Asns%3Aus-west-2%3A565419523791%3AElastiCacheNotifications`

###### Example

```
https://elasticache.amazon.com/
    ?Action=ModifyCacheCluster
    &ApplyImmediately=false
    &CacheClusterId=my-cluster
    &NotificationTopicArn=arn%3Aaws%3Asns%3Aus-west-2%3A565419523791%3AElastiCacheNotifications
    &Version=2014-12-01
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20141201T220302Z
    &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
    &X-Amz-Date=20141201T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Expires=20141201T220302Z
    &X-Amz-Credential=<credential>
    &X-Amz-Signature=<signature>
```

For more information, see [ModifyCacheCluster](../APIReference/API_ModifyCacheCluster.md "../APIReference/API_ModifyCacheCluster.md").

## Enabling and disabling Amazon SNS notifications

You can turn notifications on or off for a cluster. The following
procedures show you how to disable Amazon SNS notifications.

### Enabling and disabling Amazon SNS notifications (Console)

###### To disable Amazon SNS notifications using the AWS Management Console

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. To see a list of your clusters running Memcached, in the navigation pane
   choose **Memcached**.

To see a list of your clusters running Valkey or Redis OSS, in the navigation pane
choose **Valkey** or **Redis OSS**. 3. Choose the box to the left of the cluster you want to modify notification for. 4. Choose **Modify**. 5. In **Modify Cluster** under **Topic for SNS Notification**,
choose _Disable Notifications_. 6. Choose **Modify**.

### Enabling and disabling Amazon SNS notifications (AWS CLI)

To disable Amazon SNS notifications, use the command `modify-cache-cluster`
with the following parameters:

For Linux, macOS, or Unix:

```
aws elasticache modify-cache-cluster \
    --cache-cluster-id `my-cluster` \
    --notification-topic-status `inactive`
```

For Windows:

```
aws elasticache modify-cache-cluster ^
    --cache-cluster-id `my-cluster` ^
    --notification-topic-status `inactive`
```

###### Note

When the cluster belongs to a replication group, you must use the CLI command `modify-replication-group` to enable or disable SNS notifications.

### Enabling and disabling Amazon SNS notifications (ElastiCache API)

To disable Amazon SNS notifications, call the `ModifyCacheCluster` action with the
following parameters:

- `CacheClusterId``=my-cluster`
- `NotificationTopicStatus``=inactive`

This call returns output similar to the following:

###### Example

```
https://elasticache.us-west-2.amazonaws.com/
    ?Action=ModifyCacheCluster
    &ApplyImmediately=false
    &CacheClusterId=my-cluster
    &NotificationTopicStatus=inactive
    &Version=2014-12-01
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20141201T220302Z
    &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
    &X-Amz-Date=20141201T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Expires=20141201T220302Z
    &X-Amz-Credential=<credential>
    &X-Amz-Signature=<signature>
```
