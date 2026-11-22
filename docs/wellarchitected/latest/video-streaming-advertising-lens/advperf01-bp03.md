

# ADVPERF01-BP03 Design for low latency with appropriate compute, storage, and network considerations

 Use purpose-built AWS compute, storage, and network features to minimize latency at every layer of your advertising stack. When you match each infrastructure component to the demands of ad serving and bidding workloads, you get the consistent single-digit-millisecond response times that programmatic advertising requires. 

 **Desired outcome:** 
+  Every layer of your infrastructure (compute, storage, and networking) is configured to minimize latency for ad serving and bidding workloads. 
+  Instance selection, storage type, caching, and network configuration are chosen with performance benchmarks in mind, not defaults. 
+  Frequently accessed bid data (user profiles, frequency caps, audience segments) is served from in-memory caches rather than network-attached databases. 
+  All AWS service calls from your VPC travel over private endpoints, removing public internet hops from the data path. 

 **Common anti-patterns:** 
+  Using general-purpose instances without benchmarking against workload-specific parameters (CPU performance, memory bandwidth, launch time). 
+  Relying on network-attached storage or remote service calls for latency-sensitive data access paths where instance-attached SSD or in-memory caching would be much faster. 
+  Accessing AWS services (S3, DynamoDB, and ElastiCache) over public endpoints from within a VPC, which routes traffic through the internet gateway and introduces latency variability. 
+  Placing EC2 instances across Availability Zones without a placement group, when a cluster placement group would give tighter inter-instance latency. 

 **Benefits of establishing this best practice:** 
+  Matching each infrastructure layer to the specific demands of advertising workloads reduces bid response times and improves throughput under high request volumes. 
+  Purpose-built configurations reduce wasted compute spend by right-sizing resources to actual workload characteristics rather than paying for general-purpose overhead. 
+  Private connectivity and in-memory caching remove two of the most common sources of latency variability in production advertising systems. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A bid response that arrives a few milliseconds late misses the auction window entirely. The cost of latency is immediate and measurable in dollars, so infrastructure design for advertising workloads differs from general enterprise applications. 

 On a bid path, most of the budget is spent waiting rather than computing, on a data lookup, a network hop, or a queue. Compute selection matters, but it optimizes only the smaller share. A faster processor can't recover a round trip that should never have been on the critical path. Measure the split between waiting and working on each request and tune the higher measurement. 

 Tail behavior deserves more weight than the average, because the deadline is a hard cutoff. A path with a good median and an erratic tail loses the auctions at the tail. Those tail requests count the same as a total outage. Jitter is a first-class concern, and reducing variance at an unchanged median is a gain. Lowering the median at the cost of a longer tail can be a net loss. Shared and burstable resources vary by design, so use them cautiously on latency-critical paths. 

 Storage placement is the most frequent decision on the path, which concerns access patterns. Data consulted on every request must be reachable without a network round trip. At auction volume that round trip has the highest cost regardless of the store's speed. Data consulted occasionally can be stored anywhere. The trade-off is that the fastest options are the least durable, so anything in local or volatile storage must be reconstructible or replicated. 

 Pursue physical proximity between components only where they communicate constantly, since it trades against failure isolation. Co-locating instances reduces the latency between them but concentrates their exposure to a single failure. For each tier, decide whether to co-locate only a latency-critical tier, and spread the rest across failure boundaries. 

 Per-packet efficiency depends on the instance and its driver, so address it when you provision. Path selection is a property of the topology. A service call that leaves the private network and returns adds an unnecessary hop that no instance tuning fixes. The hop is easy to miss because the traffic works either way. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select compute-optimized instances based on benchmarking:** Benchmark candidate instance types against your specific workload parameters (CPU clock speed, memory bandwidth, instance startup time, and burst performance) before selecting. For ad serving components where inter-instance communication is latency-sensitive, place EC2 instances in a cluster placement group to deliver the lowest possible network latency between them. 

1.  **Attach SSD-backed EBS volumes for your lowest-latency storage needs:** Use GP3 volumes as the default for application servers and decision engines. Use Provisioned IOPS SSD (io1/io2) volumes for databases that power bid management systems and ad servers where I/O variability directly affects response times. Use EC2 Instance Store (NVMe-backed) when you need the highest possible storage throughput for real-time database workloads like Aerospike. Instance Store data doesn't persist beyond the instance lifecycle. 

1.  **Deploy [Amazon ElastiCache](https://aws.amazon.com/elasticache/) to serve frequently accessed data from memory:** Use ElastiCache for Redis or Memcached to cache high-read data such as user segments, frequency caps, and targeting metadata. Serving this data from memory avoids repeated database lookups on the critical bid path, directly reducing response latency. Colocate ElastiCache nodes in the same Availability Zone as your bidding compute to avoid cross-AZ network hops from cache reads. 

1.  **Enable enhanced networking on EC2 instances:** Enhanced networking uses single-root I/O virtualization (SR-IOV) to deliver higher packet-per-second performance, lower inter-instance latency, and reduced jitter, all critical for high-throughput ad serving under load. Verify that your AMI and instance type support enhanced networking and that the ENA or ixgbevf driver is enabled. 

1.  **Create VPC endpoints for AWS services on the critical path:** Configure VPC interface endpoints for the AWS services your workloads call most frequently on the bid path (S3, DynamoDB, and ElastiCache). This routes traffic for those services directly from your VPC to the service endpoint over the AWS private network, bypassing the internet gateway. Verify that DNS resolution returns private endpoint addresses after configuration by checking that service calls no longer appear in VPC Flow Logs as traffic traversing the internet gateway. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP04 Use a specialized instance family and features](advperf02-bp04.md) 
+  [ADVPERF05-BP01 Establish private connections between your VPC and AWS services to improve performance](advperf05-bp01.md) 

 **Related documents:** 
+  [Enhanced Networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) 
+  [Leverage Amazon EKS managed node group with placement group for low latency critical applications](https://aws.amazon.com/blogs/containers/leveraging-amazon-eks-managed-node-group-with-placement-group-for-low-latency-critical-applications/) 

 **Related services:** 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon EBS](https://aws.amazon.com/ebs/) 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 