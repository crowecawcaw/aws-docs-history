# Scaling Amazon MSK clusters up and down with a single operation

With intelligent rebalancing, you can scale your clusters up or down by editing the broker count in your clusters in a single action. You can do this in the Amazon MSK console, or by using the AWS CLI, Amazon MSK APIs or AWS SDK, and AWS CloudFormation. When you change the broker count, Amazon MSK does the following:

- Automatically distributes partitions to new brokers.
- Moves partitions from brokers being removed.
  As you scale your clusters up and down, cluster availability for clients to produce and consume data remains unaffected.

###### Topics

Scaling clusters using AWS Management Console

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. On the **Clusters** page, choose a newly created Express-based cluster. For information about creating a provisioned Express-based cluster, see [Step 1: Create an MSK Provisioned cluster](create-cluster.md "create-cluster.md").
3. On the **Actions** dropdown list, choose **Edit number of brokers**.
4. On the **Edit number of brokers per zone** page, do one of the following:
   - To add more brokers in your cluster, choose **Add brokers to each Availability Zone**, and then enter the number of brokers you want to add.
   - To remove brokers from your cluster, choose **Remove one broker from each Availability Zone**.

5. Choose **Save changes**.

Scaling clusters using AWS CLI
You can scale your clusters up or down by editing their broker count. To do this in the AWS CLI, use the [update-broker-count](../../../cli/latest/reference/kafka/update-broker-count.md "../../../cli/latest/reference/kafka/update-broker-count.md") command, as shown in the following example. In this command, specify the number of brokers you want in your cluster in the `target-broker-count` parameter.

```
aws msk update-broker-count --cluster-arn arn:aws:kafka:`us-east-1`:`123456789012`:cluster/`myCluster`/`abcd1234-5678-90ef-ghij-klmnopqrstuv-1` --current-version `ABCDEF1GHIJK0L` --target-broker-count `6`
```

Scaling clusters using AWS SDK
You can scale your clusters up or down by programmatically editing the broker count. To do this using the AWS SDK, use the [UpdateBrokerCount](../../1.0/apireference/clusters-clusterarn-nodes-count.md#UpdateBrokerCount "../../1.0/apireference/clusters-clusterarn-nodes-count.md#UpdateBrokerCount") API, as shown in the following example. For the `TargetNumberOfBrokerNodes` parameter, specify the number of brokers you want in your cluster.

```
update_broker_count_response = client.update_broker_count(
    ClusterArn='arn:aws:kafka:`us-east-1`:`123456789012`:cluster/`myCluster`/`abcd1234-5678-90ef-ghij-klmnopqrstuv-1`',
    CurrentVersion='`ABCDEF1GHIJK0L`',
    TargetNumberOfBrokerNodes=`6`
)
```
