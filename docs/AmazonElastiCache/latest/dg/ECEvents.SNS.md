

# Managing ElastiCache Amazon SNS notifications
<a name="ECEvents.SNS"></a>

You can configure ElastiCache to send notifications for important cluster events using Amazon Simple Notification Service (Amazon SNS). In these examples, you will configure a cluster with the Amazon Resource Name (ARN) of an Amazon SNS topic to receive notifications. 

**Note**  
This topic assumes that you've signed up for Amazon SNS and have set up and subscribed to an Amazon SNS topic. For information on how to do this, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/). 
By default, the `API modify-replication-group` affects all groups in a Region and not just the current specified group. If you want to configure one specific group in a Region differently than the other groups, you can use the `--notification-topic-arn` option to create a separate topic for that group.

**SNS topic access policy requirement**  
When you configure an Amazon SNS topic for ElastiCache notifications, the topic's access policy must use the `aws:SourceOwner` condition key, not `aws:SourceAccount`. Newly created Amazon SNS topics default to `aws:SourceAccount` in their access policy, which ElastiCache does not support for event notifications.  
If your Amazon SNS topic uses `aws:SourceAccount`, ElastiCache cannot publish notifications to the topic and automatically sets the topic status to *inactive*. Global Datastore failovers and other cluster operations can trigger this error.  
To ensure ElastiCache notifications work correctly, verify your Amazon SNS topic access policy includes the following statement:  

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
      "Resource": "arn:aws:sns:{{region}}:{{account-id}}:{{topic-name}}",
      "Condition": {
        "StringEquals": {
          "AWS:SourceOwner": "{{account-id}}"
        }
      }
    }
  ]
}
```
If ElastiCache shows your Amazon SNS topic status as *inactive* after a failover or other cluster operation, check the topic's access policy and replace `aws:SourceAccount` with `aws:SourceOwner`. Then re-enable the notification on the cluster with the `ModifyReplicationGroup` API operation or the console.  
For more information about these condition keys, see [aws:SourceAccount vs aws:SourceOwner](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-use-cases.html#source-account-versus-source-owner) in the *Amazon SNS Developer Guide*.

## Prerequisites
<a name="ECEvents.SNS.Prerequisites"></a>

Before you configure Amazon SNS notifications for ElastiCache, verify the following requirements:
+ The Amazon SNS topic must be in the same AWS Region as your ElastiCache cluster.
+ The Amazon SNS topic must be owned by the same AWS account as your ElastiCache cluster.
+ The Amazon SNS topic must not be encrypted with a customer managed AWS KMS key. ElastiCache does not support publishing notifications to Amazon SNS topics that are encrypted with customer managed AWS KMS keys.
+ You must have permissions to modify the Amazon SNS topic access policy (`sns:SetTopicAttributes` or equivalent).

## Granting ElastiCache permission to publish to your Amazon SNS topic
<a name="ECEvents.SNS.Permissions"></a>

To receive event notifications, you must grant ElastiCache permission to publish messages to your Amazon SNS topic. You do this by adding a resource-based policy to the Amazon SNS topic that allows the `elasticache.amazonaws.com` service principal to publish messages.

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
      "Resource": "arn:aws:sns:{{region}}:{{account-id}}:{{topic-name}}",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{account-id}}"
        }
      }
    }
  ]
}
```

The following table describes the policy components.


| Component | Value | Description | 
| --- | --- | --- | 
| Principal | elasticache.amazonaws.com | The ElastiCache service principal | 
| Action | sns:Publish | The minimum required permission | 
| Resource | Topic ARN | The ARN of your specific Amazon SNS topic | 
| Condition: aws:SourceAccount | Your AWS account ID | Restricts access to requests originating from your specific AWS account | 

### Granting permission (Console)
<a name="ECEvents.SNS.Permissions.Console"></a>

**To grant ElastiCache permission to publish to your Amazon SNS topic (Console)**

1. Open the Amazon Simple Notification Service console at [https://console.aws.amazon.com/sns/](https://console.aws.amazon.com/sns/).

1. In the navigation pane, choose **Topics**.

1. Select your topic and choose **Edit**.

1. Expand the **Access policy** section.

1. In the JSON editor, add the preceding policy statement.

1. Choose **Save changes**.

### Granting permission (AWS CLI)
<a name="ECEvents.SNS.Permissions.CLI"></a>

Save the access policy to a file named `sns-policy.json`, then run the following command:

For Linux, macOS, or Unix:

```
aws sns set-topic-attributes \
    --topic-arn arn:aws:sns:{{region}}:{{account-id}}:{{topic-name}} \
    --attribute-name Policy \
    --attribute-value file://sns-policy.json \
    --region {{region}}
```

For Windows:

```
aws sns set-topic-attributes ^
    --topic-arn arn:aws:sns:{{region}}:{{account-id}}:{{topic-name}} ^
    --attribute-name Policy ^
    --attribute-value file://sns-policy.json ^
    --region {{region}}
```

To verify the policy was applied correctly, run the following command:

For Linux, macOS, or Unix:

```
aws sns get-topic-attributes \
    --topic-arn arn:aws:sns:{{region}}:{{account-id}}:{{topic-name}} \
    --query 'Attributes.Policy' \
    --output text \
    --region {{region}}
```

For Windows:

```
aws sns get-topic-attributes ^
    --topic-arn arn:aws:sns:{{region}}:{{account-id}}:{{topic-name}} ^
    --query 'Attributes.Policy' ^
    --output text ^
    --region {{region}}
```

## Adding an Amazon SNS topic
<a name="ECEvents.SNS.Adding"></a>

The following sections show you how to add an Amazon SNS topic using the AWS Console, the AWS CLI, or the ElastiCache API.

### Adding an Amazon SNS topic (Console)
<a name="ECEvents.SNS.Adding.Console"></a>

 The following procedure shows you how to add an Amazon SNS topic for a cluster. When using Valkey or Redis OSS to add an Amazon SNS topic for a replication group in step 2, instead of choosing a cluster, choose a replication group. Then follow the same remaining steps.

**Note**  
 This process can also be used to modify the Amazon SNS topic. 

**To add or modify an Amazon SNS topic for a cluster (Console)**

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. In ** Clusters**, choose the cluster for which you want to add or modify an Amazon SNS topic ARN.

1. Choose **Modify**.

1. In **Modify Cluster** under **Topic for SNS Notification**, choose the SNS topic you want to add, or choose **Manual ARN input** and type the ARN of the Amazon SNS topic. 

1. Choose **Modify**.

### Adding an Amazon SNS topic (AWS CLI)
<a name="ECEvents.SNS.Adding.CLI"></a>

To add or modify an Amazon SNS topic for a cluster, use the AWS CLI command `modify-cache-cluster`.

The following code example adds an Amazon SNS topic arn to *my-cluster*.

For Linux, macOS, or Unix:

```
aws elasticache modify-cache-cluster \
    --cache-cluster-id {{my-cluster}} \
    --notification-topic-arn {{arn:aws:sns:us-west-2:123456789xxx:ElastiCacheNotifications}}
```

For Windows:

```
aws elasticache modify-cache-cluster ^
    --cache-cluster-id {{my-cluster}} ^
    --notification-topic-arn {{arn:aws:sns:us-west-2:123456789xx:ElastiCacheNotifications}}
```

For more information, see [modify-cache-cluster](https://docs.aws.amazon.com/cli/latest/reference/elasticache/modify-cache-cluster.html).

### Adding an Amazon SNS topic (ElastiCache API)
<a name="ECEvents.SNS.Adding.API"></a>

To add or modify an Amazon SNS topic for a cluster, call the `ModifyCacheCluster` action with the following parameters:
+ `CacheClusterId``=my-cluster`
+ `TopicArn``=arn%3Aaws%3Asns%3Aus-west-2%3A565419523791%3AElastiCacheNotifications`

**Example**  

```
 1. https://elasticache.amazon.com/
 2.     ?Action=ModifyCacheCluster
 3.     &ApplyImmediately=false
 4.     &CacheClusterId=my-cluster
 5.     &NotificationTopicArn=arn%3Aaws%3Asns%3Aus-west-2%3A565419523791%3AElastiCacheNotifications
 6.     &Version=2014-12-01
 7.     &SignatureVersion=4
 8.     &SignatureMethod=HmacSHA256
 9.     &Timestamp=20141201T220302Z
10.     &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
11.     &X-Amz-Date=20141201T220302Z
12.     &X-Amz-SignedHeaders=Host
13.     &X-Amz-Expires=20141201T220302Z
14.     &X-Amz-Credential=<credential>
15.     &X-Amz-Signature=<signature>
```

For more information, see [ModifyCacheCluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html).

## Enabling and disabling Amazon SNS notifications
<a name="ECEvents.SNS.Disabling"></a>

 You can turn notifications on or off for a cluster. The following procedures show you how to disable Amazon SNS notifications. 

### Enabling and disabling Amazon SNS notifications (Console)
<a name="ECEvents.SNS.Disabling.Console"></a>

**To disable Amazon SNS notifications using the AWS Management Console**

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. To see a list of your clusters running Memcached, in the navigation pane choose **Memcached**.

   To see a list of your clusters running Valkey or Redis OSS, in the navigation pane choose **Valkey** or **Redis OSS**.

1. Choose the box to the left of the cluster you want to modify notification for.

1. Choose **Modify**.

1. In **Modify Cluster** under **Topic for SNS Notification**, choose *Disable Notifications*.

1. Choose **Modify**.

### Enabling and disabling Amazon SNS notifications (AWS CLI)
<a name="ECEvents.SNS.Disabling.CLI"></a>

To disable Amazon SNS notifications, use the command `modify-cache-cluster` with the following parameters:

For Linux, macOS, or Unix:

```
aws elasticache modify-cache-cluster \
    --cache-cluster-id {{my-cluster}} \
    --notification-topic-status {{inactive}}
```

For Windows:

```
aws elasticache modify-cache-cluster ^
    --cache-cluster-id {{my-cluster}} ^
    --notification-topic-status {{inactive}}
```

**Note**  
When the cluster belongs to a replication group, you must use the CLI command `modify-replication-group` to enable or disable SNS notifications.

### Enabling and disabling Amazon SNS notifications (ElastiCache API)
<a name="ECEvents.SNS.Disabling.API"></a>

To disable Amazon SNS notifications, call the `ModifyCacheCluster` action with the following parameters:
+ `CacheClusterId``=my-cluster`
+ `NotificationTopicStatus``=inactive`

This call returns output similar to the following:

**Example**  

```
 1. https://elasticache.us-west-2.amazonaws.com/
 2.     ?Action=ModifyCacheCluster
 3.     &ApplyImmediately=false
 4.     &CacheClusterId=my-cluster
 5.     &NotificationTopicStatus=inactive
 6.     &Version=2014-12-01
 7.     &SignatureVersion=4
 8.     &SignatureMethod=HmacSHA256
 9.     &Timestamp=20141201T220302Z
10.     &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
11.     &X-Amz-Date=20141201T220302Z
12.     &X-Amz-SignedHeaders=Host
13.     &X-Amz-Expires=20141201T220302Z
14.     &X-Amz-Credential=<credential>
15.     &X-Amz-Signature=<signature>
```

## Security best practices for Amazon SNS topic policies
<a name="ECEvents.SNS.SecurityBestPractices"></a>

To help secure your Amazon SNS topic policy, follow these best practices:
+ Always include the `aws:SourceAccount` condition key to prevent cross-account confused deputy attacks.
+ Use the `elasticache.amazonaws.com` service principal rather than individual AWS account IDs.
+ Never use `"Principal": {"AWS": "*"}` without additional condition keys.
+ Grant only the minimum required permissions (`sns:Publish` only).
+ Regularly audit your Amazon SNS topic access policies.

## Verifying that notifications are working
<a name="ECEvents.SNS.Verification"></a>

After configuring the Amazon SNS topic policy and adding the topic to your ElastiCache cluster, verify that notifications are working:

1. Trigger an ElastiCache event, such as a configuration change on your cluster.

1. Check your Amazon SNS subscription endpoint (email, Lambda function, or SQS queue) for the notification message.

1. In the Amazon SNS console, verify that the subscription status shows *Confirmed*.

## Troubleshooting Amazon SNS notifications
<a name="ECEvents.SNS.Troubleshooting"></a>

If you are not receiving Amazon SNS notifications from ElastiCache, check the following:

Region mismatch  
Verify that the Amazon SNS topic is in the same AWS Region as your ElastiCache cluster.

Account ownership  
Verify that the Amazon SNS topic is owned by the same AWS account as your ElastiCache cluster.

Incorrect account ID in condition  
Check that the `aws:SourceAccount` value is your exact 12-digit AWS account ID.

KMS encryption  
Verify that the Amazon SNS topic is not encrypted with a customer managed AWS KMS key. ElastiCache does not support publishing to topics with customer managed AWS KMS encryption.

Topic ARN mismatch  
Confirm that the Amazon SNS topic ARN in the policy matches exactly the ARN of the topic attached to your ElastiCache cluster.

Unconfirmed subscription  
Verify that your Amazon SNS subscription is in *Confirmed* status.

Insufficient permissions  
Confirm that you have `sns:SetTopicAttributes` permission to modify the topic's access policy.