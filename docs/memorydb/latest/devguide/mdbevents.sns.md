

# Managing MemoryDB Amazon SNS notifications
<a name="mdbevents.sns"></a>

You can configure MemoryDB to send notifications for important cluster events using Amazon Simple Notification Service (Amazon SNS). In these examples, you will configure a cluster with the Amazon Resource Name (ARN) of an Amazon SNS topic to receive notifications. 

**Note**  
This topic assumes that you've signed up for Amazon SNS and have set up and subscribed to an Amazon SNS topic. For information on how to do this, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/). 

## Adding an Amazon SNS topic
<a name="mdbevents.sns.adding"></a>

The following sections show you how to add an Amazon SNS topic using the AWS Console, the AWS CLI, or the MemoryDB API.

### Adding an Amazon SNS topic (Console)
<a name="mdbevents.sns.addingclusters.viewdetails.console"></a>

 The following procedure shows you how to add an Amazon SNS topic for a cluster. 

**Note**  
 This process can also be used to modify the Amazon SNS topic. 

**To add or modify an Amazon SNS topic for a cluster (Console)**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. In ** Clusters**, choose the cluster for which you want to add or modify an Amazon SNS topic ARN.

1. Choose **Modify**.

1. In **Modify Cluster** under **Topic for SNS Notification**, choose the SNS topic you want to add, or choose **Manual ARN input** and type the ARN of the Amazon SNS topic. 

1. Choose **Modify**.

### Adding an Amazon SNS topic (AWS CLI)
<a name="mdbevents.sns.adding.cli"></a>

To add or modify an Amazon SNS topic for a cluster, use the AWS CLI command `update-cluster`. 

The following code example adds an Amazon SNS topic arn to *my-cluster*.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name {{my-cluster}} \
    --sns-topic-arn {{arn:aws:sns:us-east-1:565419523791:memorydbNotifications}}
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name {{my-cluster}} ^
    --sns-topic-arn {{arn:aws:sns:us-east-1:565419523791:memorydbNotifications}}
```

For more information, see [UpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html) .

### Adding an Amazon SNS topic (MemoryDB API)
<a name="mdbevents.sns.adding.api"></a>

To add or update an Amazon SNS topic for a cluster, call the `UpdateCluster` action with the following parameters:
+ `ClusterName``=my-cluster`
+ `SnsTopicArn``=arn%3Aaws%3Asns%3Aus-east-1%3A565419523791%3AmemorydbNotifications`

To add or update an Amazon SNS topic for a cluster, call the `UpdateCluster` action.

For more information, see [UpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html).

## Enabling and disabling Amazon SNS notifications
<a name="mdbevents.sns.disabling"></a>

 You can turn notifications on or off for a cluster. The following procedures show you how to disable Amazon SNS notifications. 

### Enabling and disabling Amazon SNS notifications (Console)
<a name="mdbevents.sns.disablingclusters.viewdetails.console"></a>

**To disable Amazon SNS notifications using the AWS Management Console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. Choose the radio button to the left of the cluster you want to modify notification for.

1. Choose **Modify**.

1. In **Modify Cluster** under **Topic for SNS Notification**, choose *Disable Notifications*.

1. Choose **Modify**.

### Enabling and disabling Amazon SNS notifications (AWS CLI)
<a name="mdbevents.sns.disabling.cli"></a>

To disable Amazon SNS notifications, use the command `update-cluster` with the following parameters:

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name {{my-cluster}} \
    --sns-topic-status {{inactive}}
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name {{my-cluster}} ^
    --sns-topic-status {{inactive}}
```

### Enabling and disabling Amazon SNS notifications (MemoryDB API)
<a name="mdbevents.sns.disabling.api"></a>

To disable Amazon SNS notifications, call the `UpdateCluster` action with the following parameters:
+ `ClusterName``=my-cluster`
+ `SnsTopicStatus``=inactive`

This call returns output similar to the following:

**Example**  

```
 1. https://memory-db.us-east-1.amazonaws.com/
 2.     ?Action=UpdateCluster    
 3.     &ClusterName=my-cluster
 4.     &SnsTopicStatus=inactive
 5.     &Version=2021-01-01
 6.     &SignatureVersion=4
 7.     &SignatureMethod=HmacSHA256
 8.     &Timestamp=20210801T220302Z
 9.     &X-Amz-Algorithm=Amazon4-HMAC-SHA256
10.     &X-Amz-Date=20210801T220302Z
11.     &X-Amz-SignedHeaders=Host
12.     &X-Amz-Expires=20210801T220302Z
13.     &X-Amz-Credential=<credential>
14.     &X-Amz-Signature=<signature>
```