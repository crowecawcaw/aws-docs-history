# Evaluating DB instance usage for Aurora MySQL with Amazon CloudWatch metrics

You can use CloudWatch metrics to monitor your DB instance throughput and determine whether your DB instance class provides sufficient resources for
your applications. For information about your DB instance class limits, see [Hardware specifications for DB instance classesfor Aurora](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md"). Find the specifications for your DB instance class to find the network performance.

If your DB instance usage is near the instance class limit, then performance may begin to slow. The CloudWatch metrics can confirm this situation so you
can plan to manually scale-up to a larger instance class.

Combine the following CloudWatch metrics values to find out if you are nearing the instance class limit:

- **NetworkThroughput** – The amount of network throughput received and transmitted by the clients for each instance
  in the Aurora DB cluster. This throughput value doesn't include network traffic between instances in the DB cluster and the cluster volume.
- **StorageNetworkThroughput** – The amount of network throughput received and sent to the Aurora storage subsystem
  by each instance in the Aurora DB cluster.
  Add the **NetworkThroughput** to the **StorageNetworkThroughput** to find the network throughput received from
  and sent to the Aurora storage subsystem by each instance in your Aurora DB cluster. The instance class limit for your instance should be greater than
  the sum of these two combined metrics.

You can use the following metrics to review additional details of the network traffic from your client applications when sending and
receiving:

- **NetworkReceiveThroughput** – The amount of network throughput received from clients by each DB instance in the
  Aurora MySQL DB cluster. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume.
- **NetworkTransmitThroughput** – The amount of network throughput sent to clients by each instance in the Aurora DB
  cluster. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume.
- **StorageNetworkReceiveThroughput** – The amount of network throughput received from the Aurora storage subsystem
  by each instance in the DB cluster.
- **StorageNetworkTransmitThroughput** – The amount of network throughput sent to the Aurora storage subsystem by
  each instance in the DB cluster.
  Add all of these metrics together to evaluate how your network usage compares to the DB instance class limit. The instance class limit should be greater
  than the sum of these combined metrics.

The network limits and CPU usage for storage are directly related. When the network throughput increases, then the CPU usage also increases.
Monitoring the CPU and network usage provides information about how and why the resources are being exhausted.

To help minimize network usage, you can consider the following:

- Using a larger DB instance class.
- Dividing the write requests in batches to reduce overall transactions.
- Directing the read-only workload to a read-only instance.
- Deleting any unused indexes.
