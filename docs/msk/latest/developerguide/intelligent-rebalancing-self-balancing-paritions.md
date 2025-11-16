# Steady state rebalancing for Amazon MSK clusters

Steady state rebalancing is a part of the intelligent rebalancing feature, which is turned on by default for all new MSK Provisioned clusters with Express brokers. As you scale your clusters up or down, Amazon MSK automatically handles partition management by distributing partitions to new brokers and moving partitions from brokers due for removal. To ensure optimal distribution of workload across brokers, intelligent rebalancing uses Amazon MSK best practices to determine thresholds for automatically initiating rebalancing for your brokers.

You can pause and resume steady state rebalancing when needed. Steady state rebalancing continuously monitors your cluster and does the following:

- Tracks broker resource usage (CPU, network, storage).
- Adjusts partition placement automatically without any impact on data availability.
- Completes rebalancing operations up to 180x faster for Express brokers as compared to Standard brokers.
- Maintains cluster performance.

###### Topics

Pause and resume steady state rebalancing in AWS Management Console

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. On the **Clusters** page, choose an Express-based cluster. For information about creating a provisioned Express-based cluster, see [Step 1: Create an MSK Provisioned cluster](create-cluster.md "create-cluster.md").
3. On the Cluster detail page, verify that the **Intelligent rebalancing** status is **Active**. If Intelligent rebalancing isn’t available or the status is **Paused**, create a new Express-based cluster.
4. On the **Actions** dropdown list, choose **Edit intelligent rebalancing**.
5. On the **Edit intelligent rebalancing** page, do the following:
   1. Choose **Paused**.
   2. Choose **Save changes**.

Pause and resume steady state rebalancing using AWS CLI
To set the rebalancing status of a cluster to `ACTIVE` using the AWS CLI, use the [update-rebalancing](../../../cli/latest/reference/kafka/update-rebalancing.md "../../../cli/latest/reference/kafka/update-rebalancing.md") command, as shown in the following example. In this command, specify the status with the `rebalancing` parameter.

```
aws msk update-rebalancing --cluster-arn arn:aws:kafka:`us-east-1`:`123456789012`:cluster/`myCluster`/`abcd1234-5678-90ef-ghij-klmnopqrstuv-1` --current-version `ABCDEF1GHIJK0L` --rebalancing "{\"Rebalancing\":{\"Status\":\"`ACTIVE`\"}}"
```

Pause and resume steady state rebalancing using AWS SDK
You can also set the rebalancing status of a cluster using the [UpdateRebalancingRequest](../../1.0/apireference/clusters-clusterarn-rebalancing.md#UpdateRebalancing "../../1.0/apireference/clusters-clusterarn-rebalancing.md#UpdateRebalancing") API to programmatically modify the broker count. The following examples show how to set the rebalancing status to `ACTIVE` and `PAUSED`.

```
final UpdateRebalancingRequest updateRebalancingRequest = new UpdateRebalancingRequest()
    .withClusterArn(arn:aws:kafka:`us-east-1`:`123456789012`:cluster/`myCluster`/`abcd1234-5678-90ef-ghij-klmnopqrstuv-1`)
    .withCurrentVersion(`ABCDEF1GHIJK0L`)
    .withRebalancing(new Rebalancing().withStatus("`ACTIVE`"));
```

```
final UpdateRebalancingRequest updateRebalancingRequest = new UpdateRebalancingRequest()
    .withClusterArn(arn:aws:kafka:`us-east-1`:`123456789012`:cluster/`myCluster`/`abcd1234-5678-90ef-ghij-klmnopqrstuv-1`)
    .withCurrentVersion(`ABCDEF1GHIJK0L`)
    .withRebalancing(new Rebalancing().withStatus("`PAUSED`"));
```
