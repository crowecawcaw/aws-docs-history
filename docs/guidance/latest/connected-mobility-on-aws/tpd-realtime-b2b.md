

# Real-time B2B delivery over Amazon MSK
<a name="tpd-realtime-b2b"></a>

The subscription plane above delivers by REST pull. This section describes the pattern for subscribers that need records in real time, such as a fleet customer or an insurer that runs its own Kafka client. The pattern is opinionated: Amazon MSK is the only delivery mechanism, and each subscription gets its own topic.

![Real-time B2B data products architecture in five stages. 1](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/real-time-b2b-msk-delivery-architecture.png)


## Stages
<a name="tpd-rt-ships"></a>


| Stage | What it does | 
| --- | --- | 
| 1. Data collection | CMS campaigns, decoder manifests and the signal catalog are CMS tables. `CampaignSyncProcessor` pushes the decoder manifest and collection scheme to the FleetWise Edge Agent (FWE) over MQTT. CMS does not use the managed AWS IoT FleetWise service. | 
| 2. Vehicle edge and IoT | FWE publishes to `cms/fleetwise/vehicles/<VIN>/signals` over MQTT with TLS and an X.509 certificate. The IoT rule writes each message to `fw-telemetry-raw`, keyed by the VIN so one vehicle’s records stay on one partition, in order. Each certificate is attached exclusively to its own thing and carries the scoped device policy, so it publishes only under its own VIN’s topic; see [IoT Core configuration](iot-stack.md#iot-core-configuration). | 
| 3. Ingest and normalize |  `FWTelemetryProcessor` decodes the protobuf and writes `cms-telemetry-preprocessed`, which also carries the OEM cloud and simulator sources. The router reads this topic, so every source is covered. | 
| 4. Entitlement routing | The entitlement projector writes the `dp-entitlements` topic, the B2B delivery router sends each subscription only its entitled VINs, and the backfill job supplies history. See [Entitlement routing](#tpd-rt-routing). | 
| 5. MSK delivery | A dedicated delivery cluster holds one `dp-<subscription_id>` topic per subscription, which the subscriber reads over private connectivity with IAM authentication. See [MSK delivery](#tpd-rt-delivery). | 

## Entitlement routing
<a name="tpd-rt-routing"></a>

The router is one Flink application, not one per subscriber. It decides which VINs reach each subscription’s topic.
+  **Entitlement source.** The router’s grant comes from four facts: the vehicle’s current owner, the subscriber’s customer identity, the producer having made the vehicle available, and the subscription’s vehicle scope. Consent for the purpose must also be valid, held in the pattern’s consent store. Leaving out ownership means selling a vehicle would not stop delivery.
+  **State.** DynamoDB holds the authoritative entitlement records. A Lambda projector turns its change stream into the compacted `dp-entitlements` topic, keyed by `VIN|subscription_id` with tombstones for revocation. The router holds per-VIN grants in keyed state and subscription status and product projections in broadcast state, so suspending a whole subscription is one record rather than one per VIN. The topic is used instead of reading DynamoDB Streams directly, because Streams keeps records for only 24 hours, too short to rebuild state.
+  **Validity.** Each grant carries a valid-from and valid-to time, compared with each record’s collection time.
+  **Default deny.** A record with no valid grant is dropped and counted. A separate checker samples each delivery topic, compares its VINs with the entitlement store and raises an alarm on any mismatch, because IAM cannot catch a record the router wrote to the wrong topic.
+  **Minimize.** The router emits only the signals the subscription’s product contracts for. For personal data, use pseudonymous vehicle identifiers per subscriber and coarser location where required.
+  **Revocation latency.** The chain from DynamoDB to the router is usually seconds but has no end-to-end guarantee. Publish an entitlement apply-lag metric.

## MSK delivery
<a name="tpd-rt-delivery"></a>
+  **One topic per subscription.** MSK IAM and Kafka ACLs authorize whole topics and consumer groups, never a subset of a topic’s keys, so two subscribers entitled to different VINs cannot share a topic. Name topics with opaque IDs (`dp-<subscription_id>`) rather than customer names, which anyone who can list topics or read metrics would see, and which cannot be renamed later. The `dp-` prefix must never match the `OEMTelemetryProcessor` input pattern `(cms-telemetry-oem|cs-product-.+)`, or delivered records would loop back into the platform. A shared outbound topic is acceptable only when every reader may see every record, for example aggregated data with no VIN. Inbound product topics keep one topic per product; see [Delivery](dp-delivery.md).
+  **Dedicated delivery cluster.** Put delivery topics on their own cluster, with IAM authentication only, topic auto-creation off and a replication factor of 3, so subscriber connections and partition growth do not land on the ingest cluster that carries safety and command traffic. Auto-creation off matters because a router writing before a topic is provisioned would otherwise create a default topic silently. The ingest cluster keeps SASL/SCRAM, which the IoT rule’s Kafka action needs.
+  **Provisioning.** Adding a subscriber is a provisioning step plus a configuration row, not a new Flink job: create the topic, add the cluster-policy statement, set the quota, name the consumer group and accept the subscriber’s VPC connection.
+  **Private access.** Subscribers read from their own AWS accounts over MSK multi-VPC private connectivity with IAM authentication. The cluster has one cluster policy, with a statement per subscriber account that allows `Connect`, `DescribeTopic` and `ReadData` on its topic, and `DescribeGroup` and `AlterGroup` on its consumer group. Multi-VPC connectivity works only within one Region, requires Kafka 2.7.1 or later, is not available on `kafka.t3.small` brokers, and the subscriber’s client subnets must match the cluster’s subnet count and Availability Zone IDs.
+  **Quotas.** Under IAM authentication the quota principal is the assumed-role session, which the subscriber chooses. Set a strict default quota and explicit quotas for known principals. Quotas apply per broker.
+  **Schemas.** Register one schema per product in AWS Glue Schema Registry, not one per topic. Subscribers need a role in the producer’s account to read it; verify that path before relying on it.
+  **Delivery guarantee.** Delivery is at least once, and each record carries an idempotency key of VIN, collection time and sequence. Flink’s exactly-once Kafka sink would release data only at each checkpoint, in steps as long as the checkpoint interval.
+  **Retention.** Retention is both the subscriber’s replay window and the deletion bound. Keep it short: Kafka cannot delete one key’s records from a time-series topic, so records already written stay readable until they expire.
+  **Revocation.** Revoking one VIN stops the router writing it, and its written records expire with retention. Revoking a subscription removes the cluster-policy statement, rejects the VPC connection and deletes the topic.
+  **History.** A new subscription starts empty. History comes from a bounded per-subscription backfill job that reads the raw Amazon S3 backup, applies entitlement as of each record’s collection time and writes to a separate backfill topic. Re-running the raw topic through the live router would duplicate data to every subscriber.

## Sizing and cost
<a name="tpd-rt-sizing"></a>

Partition replicas grow as subscriptions × partitions per topic × replication factor. AWS recommends at most 1,000 partition replicas per broker on `m5.large` and `m5.xlarge` brokers, so partitions per topic is the main lever: default delivery topics to one partition and raise it per tier. For example, 600 subscriptions at one partition and a replication factor of 3 is 1,800 replicas, which fits on three `m5.large` brokers; the same at three partitions needs about twice as many brokers. Fan-out multiplies broker writes and storage by the number of entitled subscriptions per record. The managed VPC connection is billed to the subscriber’s account.