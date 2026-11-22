

# Initiate the in-place upgrade

This topic describes how to initiate the in-place upgrade from Standard brokers to Express brokers for an Amazon MSK Provisioned cluster.

**Topics**
+ [Prerequisites](#msk-upgrade-initiate-prerequisites)
+ [Choose a migration mode](#msk-upgrade-initiate-choose-mode)
+ [Choose a target broker type](#msk-upgrade-initiate-choose-target)
+ [Initiate the upgrade using the AWS Management Console](#msk-upgrade-initiate-console)
+ [Initiate the upgrade using the AWS CLI](#msk-upgrade-initiate-cli)
+ [What happens after you initiate](#msk-upgrade-initiate-what-happens)

## Prerequisites
<a name="msk-upgrade-initiate-prerequisites"></a>

Before you initiate the upgrade, ensure your cluster meets the following requirements:
+ **Apache Kafka version 3.9 with KRaft**: Clusters on other Kafka versions or using ZooKeeper must first move to version 3.9 with KRaft. The upgrade keeps your existing Kafka version and KRaft configuration on the Express brokers.
+ **Three Availability Zones**: The cluster must be deployed across three Availability Zones.
+ **Tiered storage not in use**: The cluster must not use tiered storage. Clusters that use tiered storage aren't supported for in-place upgrade.
+ **A supported Standard broker instance type**: Clusters on M5, M7g, or M8g Standard brokers are eligible for in-place upgrade. Clusters on `kafka.t3.small` must first upgrade to a supported broker size.
+ **Express configuration requirements**: All topics must have a replication factor of 3, `min.insync.replicas` of 2, and per-broker partition counts within recommended Express limits.

For more information, see [Supported Apache Kafka versions](supported-kafka-versions.md), [Amazon MSK Express broker quota](limits.md#msk-express-quota), and [Tiered storage for Standard brokers](msk-tiered-storage.md).

**Note**  
We recommend running an upgrade readiness assessment before initiating the upgrade to identify and resolve any configuration issues. For more information, see [Upgrade readiness assessment](msk-upgrade-assessment.md).

## Choose a migration mode
<a name="msk-upgrade-initiate-choose-mode"></a>



|  | Automatic | Controlled | 
| --- | --- | --- | 
| Best for | If you want all topics to be moved automatically. | If you want to control which topics move and when. | 
| Topic migration | Automatic. Amazon MSK moves all topics from Standard to Express brokers. You can stop the reassignment at any time. | Controlled. You choose which topics move and when, using StartTopicReassignment. Amazon MSK manages each reassignment, and you can stop and resume at any point. | 
| AWS CLI parameter | --topic-reassignment AUTO | --topic-reassignment MANUAL | 
| Rollback | Fully reversible before decommissioning Standard brokers. | Fully reversible. You can roll back individual topics or all topics at any time before decommissioning. | 

## Choose a target broker type
<a name="msk-upgrade-initiate-choose-target"></a>

Express brokers are available in the M7g and M8g instance families. When you initiate the upgrade, you choose the Express instance family, and the upgrade keeps your broker size and broker count. For example, a cluster with three `kafka.m5.large` Standard brokers gets three `express.m7g.large` or three `express.m8g.large` Express brokers. Clusters with Standard brokers on M8g instances can also upgrade to Express brokers on M8g instances.

T3 Standard brokers aren't supported, because there's no matching Express broker size. If your cluster uses T3 brokers, upgrade to a supported broker size before you start the in-place upgrade.

After the upgrade completes, you can change your cluster's broker count and broker size to match your workload.

**Note**  
Express brokers on M8g instances are available in the AWS Regions where Express brokers are supported.

## Initiate the upgrade using the AWS Management Console
<a name="msk-upgrade-initiate-console"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose the MSK cluster you want to upgrade.

1. On the cluster details page, choose **Upgrade to Express**.

1. For **Migration mode**, choose one of the following:
   + **Automatic**: Amazon MSK moves all your topics from Standard to Express brokers.
   + **Controlled**: Amazon MSK adds Express brokers, and you move topics at your own pace. Amazon MSK manages each reassignment.

1. For **Target broker type**, choose the Express instance family: **M7g** or **M8g**.

1. Choose **Initiate upgrade**.

Amazon MSK begins provisioning Express brokers. You can track progress on the **Cluster operations** tab.

## Initiate the upgrade using the AWS CLI
<a name="msk-upgrade-initiate-cli"></a>

Run the following command to initiate the upgrade with automatic topic migration. Replace the placeholder values with your cluster information.

```
aws kafka update-broker-type \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --current-version {{Current-Cluster-Version}} \
    --target-instance-type kafka.m7g.large-express.m7g.large \
    --topic-reassignment AUTO
```

Run the following command to initiate the upgrade without automatic topic migration.

```
aws kafka update-broker-type \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --current-version {{Current-Cluster-Version}} \
    --target-instance-type kafka.m7g.large-express.m7g.large \
    --topic-reassignment MANUAL
```

To upgrade to Express brokers on M8g instances, specify an M8g Express instance type in `--target-instance-type`. For example:

```
aws kafka update-broker-type \
    --region {{Region}} \
    --cluster-arn {{ClusterArn}} \
    --current-version {{Current-Cluster-Version}} \
    --target-instance-type kafka.m5.large-express.m8g.large \
    --topic-reassignment AUTO
```

The command returns a `ClusterOperationArn`. Use the following command to track the progress of the broker provisioning.

```
aws kafka describe-cluster-operation \
    --cluster-operation-arn {{ClusterOperationArn}}
```

## What happens after you initiate
<a name="msk-upgrade-initiate-what-happens"></a>

When you initiate the upgrade, Amazon MSK performs the following actions:

1. **Validates** your cluster and topic configurations against Express broker requirements. The upgrade proceeds only after all validation checks pass.

1. **Provisions Express brokers** in the instance family you choose, matching the count and size of your Standard brokers. For example, a cluster with three `kafka.m7g.large` Standard brokers gets three `express.m7g.large` or three `express.m8g.large` Express brokers. The cluster runs both broker types until you complete the upgrade.

1. **Starts moving topics** based on the migration mode you chose. In Automatic mode, Amazon MSK starts moving all topics to Express brokers. In Controlled mode, topics stay on Standard brokers until you start moving them.

**Important**  
During the upgrade, your cluster runs both Standard and Express brokers, and you are charged for both broker types until the upgrade completes and Standard brokers are decommissioned.

To track the upgrade after you initiate it, see [Monitor and validate the upgrade](msk-upgrade-monitor-validate.md).