# Tiered storage for Standard brokers

Tiered storage is a low-cost storage tier for Amazon MSK that scales to virtually unlimited
storage, making it cost-effective to build streaming data applications.

You can create an Amazon MSK cluster configured with tiered storage that balances
performance and cost. Amazon MSK stores streaming data in a performance-optimized primary
storage tier until it reaches the Apache Kafka topic retention limits. Then, Amazon MSK
automatically moves data into the new low-cost storage tier.

When your application starts reading data from the tiered storage, you can expect an increase in read latency for the first few bytes.
As you start reading the remaining data sequentially from the low-cost tier, you can expect latencies that are similar to the primary storage tier.
You don't need to provision any storage for the low-cost tiered
storage or manage the infrastructure. You can store any amount of data and pay only for
what you use. This feature is compatible with the APIs introduced in [KIP-405: Kafka Tiered Storage](https://cwiki.apache.org/confluence/display/KAFKA/KIP-405%3A+Kafka+Tiered+Storage "https://cwiki.apache.org/confluence/display/KAFKA/KIP-405%3A+Kafka+Tiered+Storage").

For information about sizing, monitoring, and optimizing your MSK tiered storage cluster, see [Best practices for running production workloads using Amazon MSK tiered storage](https://aws.amazon.com/blogs/big-data/best-practices-for-running-production-workloads-using-amazon-msk-tiered-storage/ "https://aws.amazon.com/blogs/big-data/best-practices-for-running-production-workloads-using-amazon-msk-tiered-storage/").

Here are some of the features of tiered storage:

- You can scale to virtually unlimited storage. You don't have to guess how to scale your Apache Kafka infrastructure.
- You can retain data longer in your Apache Kafka topics, or
  increase your topic storage, without the need to increase the number of
  brokers.
- It provides a longer duration safety buffer to handle unexpected delays in
  processing.
- You can reprocess old data in its exact production order with your existing
  stream processing code and Kafka APIs.
- Partitions rebalance faster because data on secondary storage doesn't require
  replication across broker disks.
- Data between brokers and the tiered storage moves within the VPC and doesn't
  travel through the internet.
- A client machine can use the same process to connect to new clusters with
  tiered storage enabled as it does to connect to a cluster without tiered storage
  enabled. See [Create a client
  machine](create-client-machine.md "create-client-machine.md").

## Tiered storage

requirements for Amazon MSK clusters

- You must use Apache Kafka client version 3.0.0 or higher to create a new topic with tiered storage enabled. To
  transition an existing topic to tiered storage, you
  can reconfigure a client machine that uses a Kafka client
  version lower than 3.0.0 (minimum supported Apache Kafka version is 2.8.2.tiered) to
  enable tiered storage. See [Step 4: Create a topic in the Amazon MSK cluster](create-topic.md "create-topic.md").
- The Amazon MSK cluster with tiered storage enabled must use version 3.6.0 or higher, or
  2.8.2.tiered.

## Tiered storage constraints and

limitations for Amazon MSK clusters

Tiered storage has the following constraints and limitations:

- Make sure clients are not configured to `read_committed` when reading from the remote_tier in Amazon MSK, unless the application is actively using the transactions feature.
- Tiered storage isn't available in AWS GovCloud (US) regions.
- Tiered storage applies only to provisioned mode clusters.
- Tiered storage doesn’t support broker size t3.small.
- The minimum retention period in low-cost storage is 3 days. There is no minimum retention period for primary storage.
- Tiered storage doesn’t support Multiple Log directories on a broker (JBOD
  related features).
- Tiered storage doesn't support compacted topics. Make sure that all topics
  that have tiered storage turned on have their cleanup.policy configured
  to 'DELETE' only.
- Tiered storage cluster doesn’t support altering the log.cleanup.policy policy for a topic after it’s created.
- Tiered storage can be disabled for individual topics but not for the
  entire cluster. Once disabled, tiered storage cannot be re-enabled for a
  topic.
- If you use Amazon MSK version 2.8.2.tiered, you can migrate only to another tiered storage-supported Apache Kafka version. If you don't want to continue using a tiered storage-supported version, create a new MSK cluster and migrate your data to it.
- The kafka-log-dirs tool can't report tiered storage data
  size. The tool only reports the size of the log segments in primary storage.

For information about default settings and constraints you must be mindful of when you configure tiered storage at the topic level, see [Guidelines for Amazon MSK tiered
storage topic-level configuration](msk-guidelines-tiered-storage-topic-level-config.md "msk-guidelines-tiered-storage-topic-level-config.md").
