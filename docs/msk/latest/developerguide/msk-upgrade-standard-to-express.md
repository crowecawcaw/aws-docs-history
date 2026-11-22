

# Upgrade Standard brokers to Express brokers

You can upgrade an existing Amazon MSK Provisioned cluster from Standard brokers to Express brokers in place, without creating a new cluster or migrating your applications. Express brokers deliver increased stability at higher throughputs, scale up to 20 times faster, and recover up to 90% faster than standard Apache Kafka brokers. The in-place upgrade is the fastest, simplest path to those benefits. In-place upgrade adds Express brokers to your existing cluster and migrates your topics from Standard to Express brokers. Your cluster endpoint is preserved throughout, so no application changes are needed. Your Standard brokers stay in the cluster until you choose to decommission them to complete the upgrade, or to roll back.

**Note**  
In-place upgrade to Express brokers is available for Amazon MSK Provisioned clusters running Standard brokers on Apache Kafka version 3.9 with KRaft, in all AWS Regions where Amazon MSK Express brokers are supported.

**Topics**
+ [Benefits](#msk-upgrade-benefits)
+ [How in-place upgrade works](#msk-upgrade-how-it-works)
+ [Migration modes](#msk-upgrade-migration-modes)
+ [Getting started](#msk-upgrade-getting-started)
+ [Upgrade readiness assessment](msk-upgrade-assessment.md)
+ [Initiate the in-place upgrade](msk-upgrade-initiate.md)
+ [Manage topic migration during upgrade](msk-upgrade-manage-topics.md)
+ [Monitor and validate the upgrade](msk-upgrade-monitor-validate.md)
+ [Complete or roll back the upgrade](msk-upgrade-complete.md)

## Benefits
<a name="msk-upgrade-benefits"></a>
+ **No application changes**: The cluster ARN and endpoints are preserved, so your producers, consumers, and streaming applications continue to work without any code changes or endpoint updates.
+ **High availability throughout**: Applications continue serving traffic from whichever broker currently holds their partitions. Amazon MSK manages data movement so that your workloads remain available during the upgrade.
+ **Consumer offsets are preserved**: Amazon MSK reassigns partitions within the same cluster instead of moving data to a new one, so each message keeps its original topic, partition, and offset, and stateful applications such as Apache Flink and Kafka Streams continue without reprocessing or duplicates.
+ **Fully reversible**: The upgrade is fully reversible until you decommission Standard brokers from the cluster. You can roll back individual topics or all topics to Standard brokers at any time before completing the upgrade.
+ **On-demand readiness assessment**: You can assess your cluster's readiness for Express brokers at any time, independent of an upgrade. The assessment checks your cluster and topic configurations against Express broker requirements and reports what to resolve, so you can plan ahead. For more information, see [Upgrade readiness assessment](msk-upgrade-assessment.md).
+ **Express broker performance**: Express brokers deliver increased stability at higher throughputs, 20 times faster scaling, and 90% faster recovery than Standard brokers. For more information, see [Amazon MSK Express brokers](msk-broker-types-express.md).

You can upgrade your Standard brokers to Express brokers on M7g or M8g instances. Express brokers on AWS Graviton4-based M8g instances deliver up to 15% lower compute costs, up to 45% lower P99 produce latency, 2 times faster recovery when consumers fall behind, and 25% higher partition count per broker than Express brokers on M7g. You also no longer pay the broker-side cost when moving data across Availability Zones, which reduces total cross-AZ data transfer costs by 50%. For more information, see [Amazon MSK broker sizes](broker-instance-sizes.md).

## How in-place upgrade works
<a name="msk-upgrade-how-it-works"></a>

In-place upgrade uses Apache Kafka's native replication protocol to move topic partitions from Standard brokers to Express brokers within the same cluster. This is the same mechanism Kafka uses when rebalancing partitions across brokers during a scale-out operation. The process works as follows:

1. **Assess readiness (recommended)**: Run an assessment to check your cluster and topic configurations against Express broker requirements. Resolve any blocking findings before you start the upgrade. You can run an assessment at any time, independent of an upgrade. For more information, see [Upgrade readiness assessment](msk-upgrade-assessment.md).

1. **Initiate the upgrade**: Choose a migration mode, Automatic or Controlled, and start the upgrade. Amazon MSK adds Express brokers that match the count and size of your Standard brokers, and your cluster temporarily runs both broker types. For more information, see [Migration modes](#msk-upgrade-migration-modes) and [Initiate the in-place upgrade](msk-upgrade-initiate.md).

1. **Move topics**: Topics move from Standard to Express brokers based on the migration mode you chose. In both modes, Amazon MSK manages each reassignment and your applications stay available. Because partitions move within the same cluster, each message keeps its original topic, partition, and offset. For more information, see [Manage topic migration during upgrade](msk-upgrade-manage-topics.md).

1. **Monitor and validate**: Track migration progress, then validate your applications on Express brokers. Your Standard brokers stay in the cluster during this step, so you can move topics back to them if you find an issue. For more information, see [Monitor and validate the upgrade](msk-upgrade-monitor-validate.md).

1. **Complete or roll back**: If you find issues during validation, you can roll back topics to Standard brokers at any point before you complete the upgrade. When your applications are validated on Express brokers, decommission the Standard brokers from the cluster to complete the upgrade. After you decommission the Standard brokers, you can no longer roll back. For more information, see [Complete or roll back the upgrade](msk-upgrade-complete.md).

## Migration modes
<a name="msk-upgrade-migration-modes"></a>

When you initiate the upgrade, you choose how topics move from Standard brokers to Express brokers. In both modes, Amazon MSK manages the topic reassignment and keeps your applications available. The only difference is who decides which topics move and when. You can choose between the following two topic migration modes when you initiate the upgrade.
+ **Automatic mode**: Amazon MSK moves all your topics to Express brokers. Your Standard brokers stay in the cluster after migration so that you can validate your applications before you complete the upgrade. You can stop the topic reassignment at any time with `StopTopicReassignment`; topics that have already moved stay on Express brokers. In the AWS CLI, set `--topic-reassignment` to `AUTO`.
+ **Controlled mode**: You choose which topics move and when, and Amazon MSK manages each reassignment. You can move topics individually or in batches, validate each batch before you continue, and stop and resume at any point. To stop an in-flight reassignment, use `StopTopicReassignment`. In the AWS CLI, set `--topic-reassignment` to `MANUAL`. For more information, see [Manage topic migration during upgrade](msk-upgrade-manage-topics.md).

In both modes, you can stop an in-flight topic reassignment at any time with `StopTopicReassignment`. Topics that have already moved stay on Express brokers. You can also roll back topics to Standard brokers at any point before you complete the upgrade. For more information, see [Manage topic migration during upgrade](msk-upgrade-manage-topics.md).

## Getting started
<a name="msk-upgrade-getting-started"></a>

To get started, confirm that your cluster meets the prerequisites for in-place upgrade: Apache Kafka version 3.9 with KRaft, three Availability Zones, tiered storage not in use, and a supported Standard broker instance type. We recommend that you then run an upgrade readiness assessment. For more information, see [Upgrade readiness assessment](msk-upgrade-assessment.md). When your cluster is ready, choose **Upgrade to Express** on the cluster details page in the Amazon MSK console, or call the `UpdateBrokerType` API. For more information, see [Initiate the in-place upgrade](msk-upgrade-initiate.md).