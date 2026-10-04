

# Analytics assessments
<a name="transform-app-assessments-analytics"></a>

AWS Transform assesses analytics and streaming workloads and recommends managed AWS alternatives that reduce the operational overhead of running the same workload yourself. The analytics assessment estimates the total cost of ownership of the target managed service and reviews the source workload for anything that would behave differently after migrating.

## Amazon MSK Express
<a name="transform-app-assessments-analytics-msk"></a>

AWS Transform assesses self-managed Apache Kafka clusters for migration to [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) (Amazon MSK) using Express brokers. AWS Transform takes the discovered cluster topology—brokers, coordination nodes, and engine version—together with cluster-wide throughput, recommends an MSK Express broker configuration, and calculates the total cost of ownership across broker hours, storage, data-in, and cross-Availability Zone transfer.

**Note**  
The MSK Express assessment recommends [Express brokers](https://docs.aws.amazon.com/msk/latest/developerguide/msk-broker-types-express.html), which are a broker type for Amazon MSK Provisioned. It does not assess Amazon MSK Serverless or Standard brokers. For guidance on operating Express brokers after you migrate, see [Best practices for Express brokers](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices-express.html) in the *Amazon MSK Developer Guide*.

Because Amazon MSK is a managed service, migrating to it replaces your Kafka broker hosts and their directly attached storage. The MSK Express assessment therefore takes ownership of those broker hosts and volumes, so they are not additionally costed as Amazon EC2 instances or Amazon EBS volumes elsewhere in your business case. If you choose not to migrate a cluster to MSK Express, exclude it from scope and its broker hosts and volumes return to the compute and storage assessments as a lift-and-shift estimate. This is the intended way to compare the managed-service option against running the same workload on Amazon EC2.

### How clusters are sized
<a name="transform-app-assessments-analytics-msk-sizing"></a>

AWS Transform sizes each cluster from its throughput, not from your current broker count. A cluster with many small brokers can be sized as a smaller number of larger Express brokers. AWS Transform evaluates three constraints independently for each broker size and chooses the one that requires the most brokers:
+ **Ingress**—the brokers needed to absorb your peak producer throughput.
+ **Egress**—the brokers needed to serve your peak consumer throughput.
+ **Partitions**—the brokers needed to hold your partitions within the per-broker recommendation.

Each broker count is rounded up to a multiple of three, because MSK Express always deploys across three Availability Zones with a minimum of three brokers. AWS Transform recommends the least expensive broker size and count that fits within the Amazon MSK per-cluster broker quota. You can adjust the utilization that AWS Transform plans each broker against (the default is 0.75, which leaves headroom for spikes) and the retention window used to size storage (the default is 24 hours).

### Throughput data you provide
<a name="transform-app-assessments-analytics-msk-data"></a>

The single most useful figure you can provide is peak cluster ingress throughput. AWS Transform can derive the remaining throughput figures from any one of them, so supplying peak ingress alone produces a sized cluster. If no throughput figure is available at all, AWS Transform reports the minimum deployable Express cluster (three brokers, no storage, and no network charge), which is a floor rather than an estimate. When a figure is missing, AWS Transform prompts you for it and you can answer in plain language.


| Field | Why it matters | 
| --- | --- | 
| Peak data in (cluster-wide) | Drives Express instance selection, the storage estimate, and the data-in charge. Required for a sized estimate. | 
| Average data in (cluster-wide) | Sizes retained storage. Assumed to be half of peak if absent. | 
| Peak data out (cluster-wide) | Can be the binding constraint on instance choice for fan-out heavy workloads. | 
| Average data out (cluster-wide) | Affects the cross-Availability Zone transfer estimate when consumers do not use nearest-replica fetching. | 
| Kafka engine version | Determines the compatibility findings and whether a version change is involved. | 

### Cost dimensions
<a name="transform-app-assessments-analytics-msk-cost"></a>

AWS Transform prices four dimensions from the published Amazon MSK rates for your target AWS Region, refreshed daily. There is no Reserved Instance or Savings Plan input for MSK Express; the estimate is an On-Demand, steady-state run rate.
+ **Broker hours**—per broker, per hour, by instance size, for 730 hours a month.
+ **Storage**—per GB-month of retained data. Storage is elastic and pay-as-you-go on Express, so it needs no sizing.
+ **Data in**—per GB of data written to the cluster.
+ **Cross-Availability Zone transfer**—per GB of client traffic that crosses an Availability Zone boundary. This is not billed by Amazon MSK, but a three-Availability-Zone cluster incurs it in practice, so AWS Transform includes it rather than leaving it for you to discover later.

### Compatibility review
<a name="transform-app-assessments-analytics-msk-compatibility"></a>

Alongside the cost estimate, AWS Transform reviews each cluster across five areas and reports findings you can act on. Sizing, cost, and compatibility are evaluated independently, so a cluster with a compatibility finding still gets a full cost estimate.
+ **Topology**—Availability Zone count, broker count, and ZooKeeper compared with KRaft coordination.
+ **Kafka version**—whether your source version is one that MSK Express supports (Apache Kafka 3.6, 3.8, 3.9, and 4.2).
+ **Configurations**—broker- and topic-level settings that diverge from the Apache Kafka default.
+ **Authentication**—the authentication mechanism and whether traffic is encrypted in transit. MSK Express supports unauthenticated access, TLS, SASL/SCRAM, and AWS IAM.
+ **Quotas**—per-broker ingress, egress, partitions, and connections against Express limits.

Each finding carries a severity. Findings marked as requiring action indicate something in your current setup that cannot be carried over as-is, such as an unsupported authentication mechanism or a configuration value outside the range MSK Express accepts. Advisory findings indicate that the migration works but something will behave differently, most often because MSK Express manages a setting on your behalf.

### Region availability
<a name="transform-app-assessments-analytics-msk-regions"></a>

MSK Express is available in most, but not all, AWS commercial Regions. Because Express always deploys across three Availability Zones, it is not available in Regions with fewer than three usable Availability Zones, such as US West (N. California). Set your target AWS Region explicitly: it determines both whether the assessment can run and every cost line it produces. If you select a Region where MSK Express is not available, the MSK line of your business case does not produce a cost, but your other assessments still complete.

### Example prompts
<a name="transform-app-assessments-analytics-msk-prompts"></a>
+ "Estimate the cost of migrating my Kafka clusters to Amazon MSK Express"
+ "My cluster's peak ingress is 30 MB/s—size it for MSK Express"
+ "Why was this cluster sized with six brokers?"
+ "Show me the compatibility findings for my Kafka clusters"