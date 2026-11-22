

# Complete or roll back the upgrade

After you validate your applications on Express brokers, complete the upgrade by decommissioning your Standard brokers. If your validation surfaces issues, you can instead roll back the upgrade before you complete it.

For more information, see [Monitor and validate the upgrade](msk-upgrade-monitor-validate.md).

**Important**  
Completing the upgrade is final. After Amazon MSK decommissions your Standard brokers, you can't move topics back to Standard brokers on this cluster. To return to Standard brokers, you must create a new cluster and migrate to it using [Amazon MSK Replicator](msk-replicator.md). Make sure all topics, including internal topics, are on Express brokers and your applications are performing as expected before you complete the upgrade.

**Topics**
+ [Complete the upgrade using the AWS Management Console](#msk-upgrade-complete-console)
+ [Complete the upgrade using the AWS CLI](#msk-upgrade-complete-cli)
+ [Full rollback to Standard brokers](#msk-upgrade-complete-rollback)
+ [Optimize your cluster after the upgrade](#msk-upgrade-complete-optimize)
+ [Considerations and limitations](#msk-upgrade-considerations)

## Complete the upgrade using the AWS Management Console
<a name="msk-upgrade-complete-console"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose the MSK cluster you are upgrading.

1. On the cluster details page, verify that all topics, including internal topics, have moved to Express brokers.

1. Choose **Complete upgrade**. Amazon MSK decommissions the Standard brokers from the cluster.

When decommissioning finishes, the cluster returns to the `ACTIVE` state as an Express-only cluster.

## Complete the upgrade using the AWS CLI
<a name="msk-upgrade-complete-cli"></a>

Before completing the upgrade, retrieve the current cluster version. The version changes after the initial upgrade step.

```
aws kafka describe-cluster-v2 \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --query 'ClusterInfo.CurrentVersion' \
    --output text
```

Then decommission Standard brokers by calling `UpdateBrokerType` specifying only the Express broker instance type.

```
aws kafka update-broker-type \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --current-version {{Current-Cluster-Version}} \
    --target-instance-type express.m7g.large
```

**Note**  
If any topics, including internal topics, remain on Standard brokers, the command fails. Move all topics to Express brokers before you complete the upgrade.

## Full rollback to Standard brokers
<a name="msk-upgrade-complete-rollback"></a>

If you decide not to proceed with Express brokers, you can roll back the entire upgrade. Move all topics back to Standard brokers, and then decommission the Express brokers. The cluster returns to its original Standard-only state, and you can restart the upgrade later. For more information, see [Full rollback to Standard brokers](msk-upgrade-manage-topics.md#msk-upgrade-full-rollback).

## Optimize your cluster after the upgrade
<a name="msk-upgrade-complete-optimize"></a>

After the upgrade completes, we recommend the following steps:
+ **Turn on intelligent rebalancing**: Intelligent rebalancing isn't turned on for upgraded clusters, unlike new Express clusters, where it's on by default. After the upgrade completes, turn it on so that Amazon MSK keeps partitions evenly distributed across brokers and you can add or remove brokers in a single operation. For more information, see [Intelligent rebalancing for clusters](intelligent-rebalancing.md).
+ **Right-size your cluster**: Because Amazon MSK adds one Express broker for each Standard broker, your cluster might have more capacity than your workload needs. After you turn on intelligent rebalancing, use your post-upgrade metrics to reduce the broker count or change the broker size.
+ **Update client bootstrap endpoints (optional)**: Express brokers provide `boot-*` bootstrap endpoints that distribute metadata connections across brokers. Applications that use broker-specific endpoints, such as `b-1.*`, continue to work, but you can switch to the `boot-*` endpoints at any time to improve connection distribution. For more information, see [Get the bootstrap brokers for an Amazon MSK cluster](msk-get-bootstrap-brokers.md).
+ **Update monitoring**: Update or retire alarms and dashboards that are specific to your former Standard brokers. For example, replace `KafkaDataLogsDiskUsed` with `StorageUsed`, and retire EBS storage metrics such as `BurstBalance`.

## Considerations and limitations
<a name="msk-upgrade-considerations"></a>
+ **Availability during upgrade**: Applications remain available throughout the upgrade. Amazon MSK manages data movement while applications continue serving traffic from whichever broker currently holds their partitions.
+ **Billing during upgrade**: The upgrade adds Express brokers in the instance family you choose. You're charged for both your Standard brokers and your Express brokers until the upgrade completes and the Standard brokers are decommissioned. There's no additional charge for the upgrade itself. For pricing for each instance family, see [Amazon MSK pricing](https://aws.amazon.com/msk/pricing/).
+ **Operations during upgrade**: During the upgrade, you can continue to produce and consume data, create and delete topics, and reboot brokers. Amazon MSK pauses topic migration during scaling operations and resumes it automatically afterward. Other cluster modifications are blocked during the upgrade to prevent configuration mismatches between broker types, including Apache Kafka version upgrades, broker configuration changes, and authentication or monitoring changes.
+ **Cluster endpoint**: The cluster endpoint is preserved throughout the upgrade. Applications use the same bootstrap string. Kafka's metadata protocol handles leader redirection transparently when topics move between broker types. For more information, see [Get the bootstrap brokers for an Amazon MSK cluster](msk-get-bootstrap-brokers.md).
+ **Consumer offsets**: Amazon MSK reassigns partitions within the same cluster, so each message keeps its original topic, partition, and offset. Consumers, including stateful applications such as Apache Flink and Kafka Streams, resume from the same offsets.
+ **New topics during upgrade**: In Automatic mode, topics that you create during the upgrade are placed on Express brokers.