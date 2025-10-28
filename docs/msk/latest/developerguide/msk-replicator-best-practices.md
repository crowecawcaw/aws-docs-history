# Best practices for using MSK Replicator

This section covers common best practices and implementation strategies for using
Amazon MSK Replicator.

###### Topics

- [Managing MSK Replicator throughput using Kafka quotas](msk-replicator-best-practices.md#msk-replicator-manage-throughput-kafka-quotas "msk-replicator-best-practices.md#msk-replicator-manage-throughput-kafka-quotas")
- [Setting cluster retention period](msk-replicator-best-practices.md#msk-replicator-retention-period "msk-replicator-best-practices.md#msk-replicator-retention-period")

## Managing MSK Replicator throughput using Kafka quotas

Since MSK Replicator acts as a consumer for your source cluster, replication can cause other consumers to be throttled on your source cluster. The amount of throttling depends on the read capacity you have on your source cluster and the throughput of data you’re replicating. We recommend that your provision identical capacity for your source and target clusters, and account for the replication throughput when calculating how much capacity you need.

You can also set Kafka quotas for the Replicator on your source and target clusters to control how much capacity the MSK Replicator can use. A network bandwidth quota is recommended. A network bandwidth quota defines a byte rate threshold, defined as bytes per second, for one or more clients sharing a quota. This quota is defined on a per-broker basis.

Follow these steps to apply a quota.

1. Retrieve the bootstrap server string for the source cluster. See [Get the bootstrap brokers for an
   Amazon MSK cluster](msk-get-bootstrap-brokers.md "msk-get-bootstrap-brokers.md").
2. Retrieve the service execution role (SER) used by the MSK Replicator. This is the SER you used for a `CreateReplicator` request. You can also pull the SER from the DescribeReplicator response from an existing Replicator.
3. Using Kafka CLI tools, run the following command against the source cluster.

```
./kafka-configs.sh --bootstrap-server <source-cluster-bootstrap-server> --alter --add-config 'consumer_byte_
rate=<quota_in_bytes_per_second>' --entity-type users --entity-name arn:aws:sts::<customer-account-id>:assumed-role/<ser-role-name>/<customer-account-id> --command-config <client-properties-for-iam-auth></programlisting>
```

4. After executing the above command, verify that the `ReplicatorThroughput` metric does not cross the quota you have set.

Note that if you re-use a service execution role between multiple MSK Replicators they are all subject to this quota. If you want to maintain separate quotas per Replicator, use separate service execution roles.

For more information on using MSK IAM authentication with quotas, see [Multi-tenancy Apache Kafka clusters in Amazon MSK with IAM access control and Kafka Quotas – Part 1](https://aws.amazon.com/blogs/big-data/multi-tenancy-apache-kafka-clusters-in-amazon-msk-with-iam-access-control-and-kafka-quotas-part-1/ "https://aws.amazon.com/blogs/big-data/multi-tenancy-apache-kafka-clusters-in-amazon-msk-with-iam-access-control-and-kafka-quotas-part-1/").

###### Warning

Setting an extremely low consumer_byte_rate may cause your MSK Replicator to act in unexpected ways.

## Setting cluster retention period

You can set the log retention period for MSK provisioned and serverless clusters. The recommended retention period is 7 days. See [Cluster configuration changes](msk-replicator-serverless-requirements.md#msk-replicator-config-changes "msk-replicator-serverless-requirements.md#msk-replicator-config-changes") or [Supported MSK Serverless cluster
configuration](msk-replicator-serverless-requirements.md "msk-replicator-serverless-requirements.md").
