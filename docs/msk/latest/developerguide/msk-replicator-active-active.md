# Create an active-active setup using MSK

Replicator

If you want to create an active-active setup where both MSK clusters are actively serving reads and writes, we recommend that you use an MSK Replicator with Prefixed topic name replication (**Add prefix to topics name** in console). However, this will require you to reconfigure your consumers to read the replicated topics.

Follow these steps to set up active-active topology between source MSK cluster A and target MSK cluster B.

1. Create a MSK Replicator with MSK cluster A as source and MSK cluster B as target.
2. After the above MSK Replicator has been successfully created, create a Replicator with cluster B as source and cluster A as target.
3. Create two sets of producers, each writing data at the same time into the local topic (for example, “topic”) in the cluster in the same region as the producer.
4. Create two sets of consumers, each reading data using a wildcard subscription (such as “.\*topic”) from the MSK cluster in the same AWS Region as the consumer. This way your consumers will automatically read data produced locally in the Region from the local topic (for example, `topic`), as well as data replicated from other Region in topic with the prefix `<sourceKafkaClusterAlias>.topic`). These two sets of consumers should have different consumer group IDs so that consumer group offsets are not overwritten when MSK Replicator copies them to the other cluster.
   If you want to avoid reconfiguring your clients, instead of the Prefixed topic name replication (**Add prefix to topics name** in console), you can create the MSK Replicators using Identical topic name replication (**Keep the same topics name** in console) to create an active-active setup. However, you will pay additional data processing and data transfer charges for each Replicator. This is because each Replicator will need to process twice the usual amount of data, once for replication and again to prevent infinite loops. You can track the total amount of data processed by each replicator using the `ReplicatorBytesInPerSec` metric. See [Monitor replication](msk-replicator-monitor.md "msk-replicator-monitor.md"). This metric includes the data replicated to target cluster as well as the data filtered by MSK Replicator to prevent the data being coped back to the same topic it originated from.

###### Note

If you're using Identical topic name replication (**Keep the same topics name** in console) to set up active-active topology, wait at least 30 seconds after deleting a topic before re-creating a topic with the same name. This waiting period helps to prevent duplicated messages being replicated back to the source cluster. Your consumers must be able to reprocess duplicate messages without downstream impact. See [Considerations for building
multi-Region Apache Kafka applications](msk-replicator-increase-resiliency.md#msk-replication-multi-region-kafka-applications "msk-replicator-increase-resiliency.md#msk-replication-multi-region-kafka-applications").
