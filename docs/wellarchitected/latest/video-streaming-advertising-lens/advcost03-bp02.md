

# ADVCOST03-BP02 Implement Availability Zone affinity across the RTB data path

 Cross-AZ data transfer charges accumulate at RTB scale into one of the largest line items on an advertising infrastructure bill. Availability Zone affinity keeps all components of a bid request's processing path within a single Availability Zone (such as SSP-to-DSP communication, bidder-to-database queries, caching lookups, and RTB Fabric gateway routing). Intra-AZ traffic over private IP addresses incurs no data transfer charges and has sub-millisecond latency. 

 **Desired outcome:** 
+  SSP and DSP components are deployed in the same Availability Zones with zone-aware NLB routing, avoiding cross-AZ data transfer charges on the bid path. 
+  Bidder nodes communicate with database nodes and caching layers within the same Availability Zone over private IP addresses. 
+  RTB Fabric gateways, bidder containers, ElastiCache clusters, and DynamoDB DAX nodes are all co-located in matching Availability Zone subnets. 
+  Availability Zone IDs (not Availability Zone names) are used for cross-account Availability Zone coordination to keep physical placement consistent. 
+  Cross-AZ data transfer costs for RTB traffic are measured and monitored as an anomaly signal. 

 **Common anti-patterns:** 
+  Enabling cross-zone load balancing by default on ALBs and NLBs serving RTB traffic, which distributes requests across all Availability Zones regardless of origin and incurs $0.02/GB round-trip cross-AZ charges on every bid request at million-QPS scale. 
+  Deploying SSP and DSP components across multiple Availability Zones without zone-aware routing. 
+  Querying database nodes in a different Availability Zone from the bidder, so every bid evaluation lookup crosses an Availability Zone boundary and pays cross-AZ charges. 
+  Coordinating Availability Zone placement with partners using names (us-east-1a) rather than IDs (use1-az1), which map to different physical zones across AWS accounts. 
+  Deploying RTB Fabric gateways and bidder infrastructure in mismatched Availability Zones, which adds unnecessary cross-AZ hops between the connectivity fabric and application compute. 
+  Relying solely on database multi-AZ failover for read traffic rather than using zone-local read replicas to keep queries within the same Availability Zone. 
+  Using Application Load Balancers (ALBs) for TCP bid traffic where NLB would provide lower latency and supports disabling cross-zone load balancing at the target group level. 
+  Setting up infrastructure once and never re-evaluating placement as bid traffic patterns shift across Availability Zones. 

 **Benefits of establishing this best practice:** 
+  Elimination of round-trip cross-AZ charges at million-QPS scale, often the single largest data transfer cost reduction available. 
+  1-2 ms latency reduction on every bid request improves auction competitiveness and win rates. 
+  NLB handles millions of requests per second with low latency, which suits RTB traffic patterns. 
+  Simplified traffic patterns reduce debugging complexity and cost attribution ambiguity. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Cross-AZ data transfer incurs costs when the data moves in each direction. At RTB scale, millions of bid requests per second carry payloads between SSP and DSP components, hit databases, and traverse caching layers. Even kilobyte-sized messages add up to large monthly transfer costs when they cross Availability Zone boundaries. The principle behind Availability Zone affinity is that every component in a bid request's critical path exists in the same Availability Zone, communicating over private IP addresses with no data transfer cost. 

 SSP-to-DSP bid traffic produces the highest cross-AZ volume when zone affinity is missing. [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) supports disabling cross-zone load balancing at the target group level. When cross-zone load balancing is off, each NLB node routes only to targets registered in its own Availability Zone. This differs from Application Load Balancer behavior, where cross-zone distribution is enabled by default. NLB also operates at Layer 4 (TCP/UDP), which matches RTB bid traffic characteristics: high connection rates, small payloads, and no need for HTTP-layer inspection. NLB charges per connection and ALB charges per request evaluation rule, so the cost difference widens at high request volumes. 

 Disabling cross-zone load balancing requires matching capacity distribution to traffic patterns. If 70% of inbound requests arrive in Availability Zone a but only 30% of DSP capacity sits there, the Availability Zone a targets become overloaded while Availability Zone b targets sit idle. Zone affinity only works when capacity in each Availability Zone proportionally matches the traffic that zone receives. Auto Scaling group configurations must account for this, either by weighting desired capacity per Availability Zone or by having upstream routing distribute requests proportionally. 

 Every bid request triggers bidder-to-database queries. User profile lookups, frequency cap checks, audience segment matches, and targeting data reads all occur within the tight latency budget of a bid response (typically under 50ms for the data tier portion). Different database engines expose zone locality differently. An [Amazon Aurora custom endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoints.Custom.html) is a set of DB instances selected on criteria such as instance class, and it distributes connections across them randomly through DNS. It has no Availability Zone selector. Zone-local reads happen only if the named instances sit in one zone, and Aurora does not maintain that mapping as the cluster changes. 

 [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/wwe-troubleshooting.html) has no server-side Availability Zone affinity either: routing a read to a replica in the caller's zone is a client read-preference setting, and it trades strong consistency for locality. DynamoDB, as a managed service, handles placement internally with no cross-AZ charge for DynamoDB API calls from within the same Region, though DAX nodes have placement considerations. 

 Placing an in-memory cache (Redis or Memcached) in the same Availability Zone as bidder nodes intercepts high-frequency reads before they reach the database. This reduces both cross-AZ transfer costs and database load, which trades memory cost for transfer cost. Replicate the working set to every bidder Availability Zone so reads stay zone-local. A shared single-AZ cache reintroduces cross-AZ charges for bidders in other zones, and is worthwhile only when the memory cost of full replication exceeds the transfer cost it saves. 

 Multi-AZ database deployments designed for high availability conflict with cost optimization. Aurora's writer instance exists in one Availability Zone, and replicas spread across others. If bidders in Availability Zone b direct writes to the writer in Availability Zone a, the writes cross Availability Zones. The cost of cross-AZ writes is acceptable because write volume in bid evaluation is far lower than read volume. Route reads to zone-local replicas. Accept the cross-AZ cost on writes as the availability trade-off. 

 RTB Fabric gateways operate within specific Availability Zones. Placing them in different Availability Zones from your bidder fleet introduces cross-AZ charges and adds 1-2 ms of latency. Co-locating gateways in the same Availability Zones as compute instances avoids both problems. Organizations running bidders across multiple Availability Zones need a gateway in each Availability Zone where compute runs. 

 Availability Zone names like us-east-1a map to different physical data centers in different AWS accounts. Two accounts that both deploy to us-east-1a may be in different physical zones, defeating the purpose of colocation. [Availability Zone IDs](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html) (like use1-az4) are consistent across accounts and must be used for any cross-account Availability Zone coordination. 

 Zone-affinity routing concentrates traffic within a single Availability Zone, which reduces costs but creates a dependency on that Availability Zone's health. If an Availability Zone experiences degradation, traffic must shift to healthy zones, temporarily reintroducing cross-AZ charges. Most RTB workloads favor zone affinity as the default because impairments are infrequent and the steady-state savings are large. Monitor cross-AZ RTB traffic as an anomaly signal. Any sustained cross-AZ flow outside a failover event indicates misconfiguration. 

 Infrastructure provisioned correctly at launch can drift as traffic patterns shift. Bidder Auto Scaling groups might expand into a new Availability Zone where no database replica, cache node, or RTB Fabric gateway exists, which reintroduces cross-AZ traffic. Without ongoing monitoring of per-AZ traffic flows through VPC Flow Logs, you might only discover the cost regression in a monthly billing review. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze current cross-AZ traffic and quantify cost:** Use VPC Flow Logs and the CUDOS Data Transfer tab to identify bid path traffic that crosses Availability Zone boundaries. Calculate the monthly cost of cross-AZ transfers for SSP-to-DSP, bidder-to-database, and bidder-to-cache traffic paths separately to prioritize remediation. 

1.  **Configure NLB with cross-zone load balancing disabled for bid traffic:** Set CrossZoneLoadBalancing to false on NLBs serving RTB bid traffic. Enable NLB Availability Zone DNS Affinity so DNS queries resolve to the NLB endpoint in the client's Availability Zone. Verify per-AZ traffic distribution in CloudWatch to confirm zone affinity is working. 

1.  **Co-locate SSP, DSP, bidder, database, and cache in matching Availability Zone subnets:** Place Auto Scaling groups for SSP and DSP components, bidder nodes, and RTB Fabric gateways in the same Availability Zone subnets. For Aurora, create a READER-type custom endpoint per zone through the CLI or API, naming at least two replicas in that zone so the endpoint retains a local target through a failure, and reconcile membership whenever the cluster changes. For ElastiCache, deploy replicas in every bidder zone and set an Availability Zone-aware read preference in the client. 

1.  **Deploy ElastiCache and DAX nodes in each bidder Availability Zone:** Place ElastiCache Redis or Memcached nodes and DynamoDB DAX clusters in each Availability Zone used by bidder instances. Configure bidder connection strings to prefer the local Availability Zone cache endpoint. This avoids cross-AZ charges for the high-frequency cache reads (user profiles, frequency caps, audience segments) that characterize bid evaluation. 

1.  **Coordinate Availability Zone placement with partners using Availability Zone IDs:** Share Availability Zone IDs (not Availability Zone names) with DSP/SSP partners to enable same-AZ routing for the highest-volume RTB Fabric links. Place RTB Fabric gateways in the same Availability Zone IDs as your compute fleet and your partners' gateways. 

1.  **Implement a fallback strategy for Availability Zone impairments:** Configure health checks so that traffic can shift to healthy Availability Zones during impairments. Accept the temporary cross-AZ cost as the trade-off for availability during failures. Monitor cross-AZ RTB traffic with CloudWatch alarms: any sustained cross-AZ flow outside a failover event indicates misconfiguration requiring investigation. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST03-BP01 Consider private communication channels between SSP and DSP](advcost03-bp01.md) 

 **Related documents:** 
+  [Improving Performance and Reducing Cost Using AZ Affinity](https://aws.amazon.com/blogs/architecture/improving-performance-and-reducing-cost-using-availability-zone-affinity/) 
+  [Announcing new AWS Network Load Balancer (NLB) availability and performance capabilities](https://aws.amazon.com/about-aws/whats-new/2023/10/aws-nlb-availability-performance-capabilities/) 
+  [Exploring Data Transfer Costs for AWS Managed Databases](https://aws.amazon.com/blogs/architecture/exploring-data-transfer-costs-for-aws-managed-databases/) 
+  [Guidance for AdTech Private Network on AWS](https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/) 

 **Related services:** 
+  [Elastic Load Balancing (NLB)](https://aws.amazon.com/elasticloadbalancing/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/) 
+  [Amazon Aurora](https://aws.amazon.com/rds/aurora/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 