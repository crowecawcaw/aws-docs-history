

# Use Amazon MSK storage capacity alerts
<a name="cluster-alerts"></a>

On Amazon MSK provisioned clusters, you choose the cluster's primary storage capacity. If you exhaust the storage capacity on a broker in your provisioned cluster, it can affect its ability to produce and consume data, leading to costly downtime. Amazon MSK offers CloudWatch metrics to help you monitor your cluster's storage capacity. However, to make it easier for you to detect and resolve storage capacity issues, Amazon MSK automatically sends you dynamic cluster storage capacity alerts. The storage capacity alerts include recommendations for short-term and long-term steps to manage your cluster's storage capacity. From the [Amazon MSK console](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/), you can use quick links within the alerts to take recommended actions immediately.

There are two types of MSK storage capacity alerts: proactive and remedial.
+ Proactive ("Action required") storage capacity alerts warn you about potential storage issues with your cluster. When a broker in an MSK cluster has used over 60% or 80% of its disk storage capacity, you'll receive proactive alerts for the affected broker. 
+ Remedial ("Critical action required") storage capacity alerts require you to take remedial action to fix a critical cluster issue when one of the brokers in your MSK cluster has run out of disk storage capacity.

Amazon MSK automatically sends these alerts to the [Amazon MSK console](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/), [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health/), [Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/), and email contacts for your AWS account. You can also [configure Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destination-partners.html) to deliver these alerts to Slack or to tools such as New Relic, and Datadog. 

Storage capacity alerts are enabled by default for all MSK provisioned clusters and can't be turned off. This feature is supported in all regions where MSK is available.

## Monitor storage capacity alerts
<a name="cluster-alerts-monitoring"></a>

You can check for storage capacity alerts in several ways:
+ Go to the [Amazon MSK console](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/). Storage capacity alerts are displayed in the cluster alerts pane for 90 days. The alerts contain recommendations and single-click link actions to address disk storage capacity issues.
+ Use [ListClusters](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#ListClusters), [ListClustersV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters.html#ListClustersV2), [DescribeCluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster), or [DescribeClusterV2](https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters-clusterarn.html#DescribeClusterV2) APIs to view `CustomerActionStatus` and all the alerts for a cluster.
+ Go to the [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health/) to view alerts from MSK and other AWS services.
+ Set up [AWS Health API](https://docs.aws.amazon.com/health/latest/ug/health-api.html) and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destination-partners.html) to route alert notifications to 3rd party platforms such as Datadog, NewRelic, and Slack.

## Disk-full protection for Standard brokers
<a name="cluster-alerts-disk-full-protection"></a>

To keep a broker from running out of storage, Amazon MSK protects Standard brokers when their data disk usage reaches 90%. When a broker reaches this threshold, Amazon MSK does the following:
+ Stops accepting new produce requests and replication traffic on the broker.
+ Moves partition leadership from the broker to other in-sync replicas, so that producers can continue writing to those partitions through the new leaders. Consumers can continue reading.
+ Resumes normal operation on the broker automatically after its data disk usage stays below 90% for 5 minutes.

If all in-sync replicas of a partition are on protected brokers, writes to that partition fail until the broker's disk usage drops below 90%. To avoid this, act on the 60% and 80% storage capacity alerts. You can do any of the following:
+ Increase broker storage, or turn on automatic storage scaling. For information about increasing broker storage, see [Scale up Amazon MSK Standard broker storage](msk-update-storage.md). For information about automatic storage scaling, see [Automatic scaling for Amazon MSK clusters](msk-autoexpand.md).
+ Reduce the retention period for your topics. For information about retention settings, see [Adjust data retention parameters](bestpractices.md#bestpractices-retention-period).
+ Delete topics that you no longer need. For information about deleting topics, see [Delete a topic in an Amazon MSK cluster](msk-delete-topic.md).
+ If your brokers already use the maximum storage per broker, add brokers to the cluster or use tiered storage. For information about adding brokers, see [Expand the number of brokers in an Amazon MSK cluster](msk-update-broker-count.md). For information about tiered storage, see [Tiered storage for Standard brokers](msk-tiered-storage.md).

If a broker is already protected, use the same options to bring its disk usage below 90%. The broker resumes normal operation automatically after its disk usage stays below 90% for 5 minutes.

Disk-full protection is on by default, and you can't turn it off. You get disk-full protection on Standard brokers that run one of the following Apache Kafka versions:


| Apache Kafka version | Metadata mode | 
| --- | --- | 
| 3.6.0 | ZooKeeper | 
| 3.8.x | ZooKeeper | 
| 3.9.x | ZooKeeper | 
| 3.9.x.kraft | KRaft | 
| 4.0.x.kraft | KRaft | 
| 4.1.x.kraft | KRaft | 
| 4.2.x.kraft | KRaft | 

Express brokers don't need disk-full protection because they don't use provisioned storage.