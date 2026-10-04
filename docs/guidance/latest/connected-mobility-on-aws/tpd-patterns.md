

# Four delivery patterns and when each fits
<a name="tpd-patterns"></a>

 **Direct consumer access.** The third party runs a Kafka consumer against the platform’s cluster, authenticated with its own identity and confined to a dedicated consumer group. This gives the lowest latency and no data duplication, and suits consumers that can hold a persistent connection and operate a well-behaved client. Its cost is coupling: the consumer is tied to the platform’s cluster and quotas.

 **Replication to a consumer-owned cluster.** The platform replicates selected topics into a cluster the consumer owns, using MSK Replicator or MirrorMaker2. This decouples the consumer from the source cluster and is the right answer when the consumer needs isolation or its own retention, at the cost of duplicated storage and replication lag.

 **Private-connectivity delivery.** For a consumer in another VPC, account, or cloud, the stream is delivered over AWS PrivateLink, VPC peering, or a managed multicloud interconnect so it never traverses the public internet — the reliability and security layer beneath the first two patterns.

 **Mediated or pull-based delivery.** For consumers that cannot hold a persistent Kafka consumer, a gateway such as a REST proxy, or tiered storage backed by Amazon S3, exposes the same data for pull. This trades latency for reach.