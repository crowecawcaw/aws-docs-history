

# Managing throughput with Kafka quotas
<a name="msk-replicator-bp-quotas"></a>

Since MSK Replicator acts as a consumer for your source cluster, replication can cause other consumers to be throttled on your source cluster. The amount of throttling depends on the read capacity you have on your source cluster and the throughput of data you are replicating.

You can set Kafka quotas for the Replicator on your source cluster to control how much capacity the MSK Replicator can use. A network bandwidth quota is recommended. A network bandwidth quota defines a byte rate threshold, defined as bytes per second, for one or more clients sharing a quota. This quota is defined on a per-broker basis.

Follow these steps to apply a quota:

1. Retrieve the bootstrap server string for the source cluster. See [Get the bootstrap brokers for an Amazon MSK cluster](msk-get-bootstrap-brokers.md).

1. Retrieve the service execution role (SER) used by the MSK Replicator. This is the SER you used for a `CreateReplicator` request. You can also pull the SER from the `DescribeReplicator` response.

1. Using Kafka CLI tools, run the following command against the source cluster:

   ```
   ./kafka-configs.sh --bootstrap-server <source-cluster-bootstrap-server> \
     --alter \
     --add-config 'consumer_byte_rate=<quota_in_bytes_per_second>' \
     --entity-type users \
     --entity-name arn:aws:sts::<customer-account-id>:assumed-role/<ser-role-name>/<customer-account-id> \
     --command-config <client-properties-for-iam-auth>
   ```

1. After executing the command, verify that the `ReplicatorThroughput` metric does not cross the quota you have set.

If you reuse a service execution role between multiple MSK Replicators, they are all subject to this quota. If you want to maintain separate quotas per Replicator, use separate service execution roles.

For a bi-directional setup, we recommend the following:
+ Use two separate service execution roles (SERs), one for each direction of replication. This makes sure that each Replicator works correctly and can access the internal topics that it creates on its target cluster.
+ For each SER, apply the quota only on the source cluster of the corresponding Replicator. If you must set a quota on the target cluster, make sure that it's higher than 10 MB/s to avoid impacting replication.

For more information on using MSK IAM authentication with quotas, see [Multi-tenancy Apache Kafka clusters in Amazon MSK with IAM access control and Kafka Quotas – Part 1](https://aws.amazon.com/blogs/big-data/multi-tenancy-apache-kafka-clusters-in-amazon-msk-with-iam-access-control-and-kafka-quotas-part-1/).

**Warning**  
Setting an extremely low `consumer_byte_rate` on the target cluster may cause MSK Replicator to behave unexpectedly and result in replication failure.