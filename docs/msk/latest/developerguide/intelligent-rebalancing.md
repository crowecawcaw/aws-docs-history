

# Intelligent rebalancing for clusters
<a name="intelligent-rebalancing"></a>

Amazon MSK provides intelligent rebalancing for all new MSK Provisioned clusters with Express brokers. This feature automatically manages partition distribution and cluster scaling operations, eliminating the need for third-party tools. Intelligent rebalancing automatically rebalances partitions when you scale clusters up or down. It also continuously monitors your cluster’s health for resource imbalance or overload and redistributes workload.

Intelligent rebalancing provides fast scaling operations that complete within 30 minutes and doesn’t impact cluster availability during scaling. It’s turned on by default for all new MSK Express-based Provisioned clusters and works with the recommended maximum partition limit of 20,000 partitions per broker. Additionally, this feature is available at no additional cost and doesn’t require any configurations.

Effective 20th Nov 2025, Intelligent Rebalancing is available in all AWS Regions where Amazon MSK Express brokers are supported.

Effective June 18, 2026, Intelligent Rebalancing is available for all MSK Provisioned clusters with Express brokers. This includes Express clusters created prior to the launch of intelligent rebalancing feature in November 2025. For clusters created before November 20, 2025, Intelligent Rebalancing is available with **Rebalancing Status** set to **Paused**. To enable this feature for your existing clusters, set **Rebalancing Status** to **Active** using the Amazon MSK console, AWS CLI, or SDK. For instructions, see [Steady state rebalancing](intelligent-rebalancing-self-balancing-paritions.md).

**Topics**
+ [How intelligent rebalancing works](#how-intelligent-rebalancing-works)
+ [Monitoring intelligent rebalancing metrics](#intelligent-rebalancing-metrics)
+ [Considerations to use intelligent rebalancing](#intelligent-rebalancing-considerations)
+ [Scaling Amazon MSK clusters up and down with a single operation](intelligent-rebalancing-scaling-clusters.md)
+ [Steady state rebalancing for Amazon MSK clusters](intelligent-rebalancing-self-balancing-paritions.md)

## How intelligent rebalancing works
<a name="how-intelligent-rebalancing-works"></a>

Intelligent rebalancing is turned on by default for all new MSK Provisioned clusters with Express brokers. It includes support for the following situations:
+ **Scaling up and down**: Lets you add or remove brokers to your MSK Express-based clusters with a single click. Once you specify the brokers to add or remove, intelligent rebalancing automatically redistributes partitions across the new cluster setup based on internal AWS best practices.
+ **Steady state rebalancing**: At steady state, this feature monitors your cluster’s health continuously and automatically rebalances partitions when:
  + Resource utilization becomes skewed across brokers.
  + Brokers become over-provisioned or under-utilized.
  + New brokers are added or existing brokers are removed.

**Note**  
If intelligent rebalancing is turned on, you won’t be able to use third-party tools, such as Cruise Control, for partition rebalancing. You must first pause intelligent rebalancing to use the partition reassignment API provided by these third-party tools.

You can use this feature in the Amazon MSK console. You can also use this feature using the AWS CLI, Amazon MSK APIs or AWS SDK, and AWS CloudFormation. For more information, see [Scaling Amazon MSK clusters](intelligent-rebalancing-scaling-clusters.md) and [Steady state rebalancing](intelligent-rebalancing-self-balancing-paritions.md).

## Monitoring intelligent rebalancing metrics
<a name="intelligent-rebalancing-metrics"></a>

You can monitor the status of ongoing and historical intelligent rebalancing operations using the following Amazon CloudWatch metrics:
+ `RebalanceInProgress`: This metric is published every minute with a value of 1 when rebalancing is ongoing and 0 otherwise.
+ `UnderProvisioned`: Indicates that a cluster is currently under provisioned and any partition rebalancing can’t be performed. You either need to add more brokers or scale-up your cluster’s instance type.

For information about monitoring an MSK Provisioned cluster, see [Monitor an Amazon MSK Provisioned cluster](monitoring.md) and [View Amazon MSK metrics using CloudWatch](cloudwatch-metrics.md).

## Considerations to use intelligent rebalancing
<a name="intelligent-rebalancing-considerations"></a>
+ Effective June 18, 2026, Intelligent Rebalancing is available for all MSK Provisioned clusters with Express brokers. This includes Express clusters created prior to the launch of intelligent rebalancing feature in November 2025. For clusters created before November 20, 2025, Intelligent Rebalancing is available with **Rebalancing Status** set to **Paused**. To enable this feature for your existing clusters, set **Rebalancing Status** to **Active** using the Amazon MSK console, AWS CLI, or SDK. For instructions, see [Steady state rebalancing](intelligent-rebalancing-self-balancing-paritions.md).
+ For automatic partition reassignment, maximum support for up to 20,000 partitions per broker is available.
+ You can’t use partition reassignment APIs or third-party rebalancing tools when intelligent rebalancing is enabled. To use such APIs or third-party tools, you must first pause intelligent rebalancing for your MSK Express-based cluster.