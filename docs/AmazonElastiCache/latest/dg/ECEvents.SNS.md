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

###### SNS topic access policy requirement

When you configure an Amazon SNS topic for ElastiCache notifications, the topic's access policy
must use the `aws:SourceOwner` condition key, not `aws:SourceAccount`.
Newly created Amazon SNS topics default to `aws:SourceAccount` in their access policy,
which ElastiCache does not support for event notifications.

If your Amazon SNS topic uses `aws:SourceAccount`, ElastiCache cannot publish
notifications to the topic and automatically sets the topic status to
_inactive_. Global Datastore failovers and other cluster operations can trigger this error.

To ensure ElastiCache notifications work correctly, verify your Amazon SNS topic access policy
includes the following statement:

```
{
  "Statement": [
    {
      "Sid": "AllowElastiCachePublish",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:`region`:`account-id`:`topic-name`",
      "Condition": {
        "StringEquals": {
          "AWS:SourceOwner": "`account-id`"
        }
      }
    }
  ]
}
```

If ElastiCache shows your Amazon SNS topic status as _inactive_
after a failover or other cluster operation, check the topic's access policy and replace
`aws:SourceAccount` with `aws:SourceOwner`. Then re-enable the
notification on the cluster with the `ModifyReplicationGroup` API operation or the console.

For more information about these condition keys, see
[aws:SourceAccount vs aws:SourceOwner](../../../sns/latest/dg/sns-access-policy-use-cases.md#source-account-versus-source-owner "../../../sns/latest/dg/sns-access-policy-use-cases.md#source-account-versus-source-owner") in the _Amazon SNS Developer Guide_.

## Prerequisites

Before you configure Amazon SNS notifications for ElastiCache, verify the following
requirements:

- The Amazon SNS topic must be in the same AWS Region as your ElastiCache
  cluster.
- The Amazon SNS topic must be owned by the same AWS account as your ElastiCache
  cluster.
- The Amazon SNS topic must not be encrypted with a customer managed AWS KMS
  key. ElastiCache does not support publishing notifications to Amazon SNS topics that are
  encrypted with customer managed AWS KMS keys.
- You must have permissions to modify the Amazon SNS topic access policy
  (`sns:SetTopicAttributes` or equivalent).

## Granting ElastiCache permission to publish to your Amazon SNS topic

To receive event notifications, you must grant ElastiCache permission to publish
messages to your Amazon SNS topic. You do this by adding a resource-based policy to the
Amazon SNS topic that allows the `elasticache.amazonaws.com` service principal
to publish messages.

The following policy grants ElastiCache the required permission:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowElastiCachePublish",
      "Effect": "Allow",
      "Principal": {
        "Service": "elasticache.amazonaws.com"
      },
      "Action": "sns:Publish",
      "Resource": "arn:aws:sns:`region`:`account-id`:`topic-name`",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`account-id`"
        }
      }
    }
  ]
}
```

The following table describes the policy components.

| Component                      | Value                       | Description                                                                |
| ------------------------------ | --------------------------- | -------------------------------------------------------------------------- |
| Principal                      | `elasticache.amazonaws.com` | The ElastiCache service principal                                          |
| Action                         | `sns:Publish`               | The minimum required permission                                            |
| Resource                       | Topic ARN                   | The ARN of your specific Amazon SNS topic                                  |
| Condition: `aws:SourceAccount` | Your AWS account ID         | Restricts access to requests originating from your specific<br>AWS account |

### Granting permission (Console)

###### To grant ElastiCache permission to publish to your Amazon SNS topic (Console)

1. Open the Amazon Simple Notification Service console at [https://console.aws.amazon.com/sns/](https://console.aws.amazon.com/sns/ "https://console.aws.amazon.com/sns/").
2. In the navigation pane, choose **Topics**.
3. Select your topic and choose **Edit**.
4. Expand the **Access policy** section.
5. In the JSON editor, add the preceding policy statement.
6. Choose **Save changes**.

### Granting permission (AWS CLI)

Save the access policy to a file named `sns-policy.json`,
then run the following command:

For Linux, macOS, or Unix:

```
aws sns set-topic-attributes \
    --topic-arn arn:aws:sns:`region`:`account-id`:`topic-name` \
    --attribute-name Policy \
    --attribute-value file://sns-policy.json \
    --region `region`
```

For Windows:

```
aws sns set-topic-attributes ^
    --topic-arn arn:aws:sns:`region`:`account-id`:`topic-name` ^
    --attribute-name Policy ^
    --attribute-value file://sns-policy.json ^
    --region `region`
```

To verify the policy was applied correctly, run the following command:

For Linux, macOS, or Unix:

```
aws sns get-topic-attributes \
    --topic-arn arn:aws:sns:`region`:`account-id`:`topic-name` \
    --query 'Attributes.Policy' \
    --output text \
    --region `region`
```

For Windows:

```
aws sns get-topic-attributes ^
    --topic-arn arn:aws:sns:`region`:`account-id`:`topic-name` ^
    --query 'Attributes.Policy' ^
    --output text ^
    --region `region`
```

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

## Security best practices for Amazon SNS topic policies

To help secure your Amazon SNS topic policy, follow these best practices:

- Always include the `aws:SourceAccount` condition key to
  prevent cross-account confused deputy attacks.
- Use the `elasticache.amazonaws.com` service principal
  rather than individual AWS account IDs.
- Never use `"Principal": {"AWS": "*"}` without
  additional condition keys.
- Grant only the minimum required permissions
  (`sns:Publish` only).
- Regularly audit your Amazon SNS topic access policies.

## Verifying that notifications are working

After configuring the Amazon SNS topic policy and adding the topic to your ElastiCache
cluster, verify that notifications are working:

1. Trigger an ElastiCache event, such as a configuration change on your
   cluster.
2. Check your Amazon SNS subscription endpoint (email, Lambda function, or
   SQS queue) for the notification message.
3. In the Amazon SNS console, verify that the subscription status shows
   _Confirmed_.

## Troubleshooting Amazon SNS notifications

If you are not receiving Amazon SNS notifications from ElastiCache, check the
following:

Region mismatch
Verify that the Amazon SNS topic is in the same AWS Region as your
ElastiCache cluster.

Account ownership
Verify that the Amazon SNS topic is owned by the same AWS account
as your ElastiCache cluster.

Incorrect account ID in condition
Check that the `aws:SourceAccount` value is your
exact 12-digit AWS account ID.

KMS encryption
Verify that the Amazon SNS topic is not encrypted with a customer
managed AWS KMS key. ElastiCache does not support publishing to topics with customer
managed AWS KMS encryption.

Topic ARN mismatch
Confirm that the Amazon SNS topic ARN in the policy matches exactly
the ARN of the topic attached to your ElastiCache cluster.

Unconfirmed subscription
Verify that your Amazon SNS subscription is in
_Confirmed_ status.

Insufficient permissions
Confirm that you have `sns:SetTopicAttributes`
permission to modify the topic's access policy.
