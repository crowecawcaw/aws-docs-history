

# Scenario 1: Programmatic advertising workloads
<a name="scenario-01-programmatic-advertising"></a>

 The petabyte-scale, millisecond-latency world of programmatic advertising brings significant challenges for performance, throughput, latency, and costs. SSPs, ad exchanges, and DSPs form the core infrastructure, exchanging OpenRTB bid requests and responses across organizational and network boundaries in the time it takes a webpage to load. The key systems are ad servers, ad exchanges, SSPs, and DSPs. 

## Characteristics
<a name="s01-characteristics"></a>
+  Real-time bidding (RTB) workloads processing tens of millions of transactions per second. 
+  End-to-end bid response SLOs under 100 ms, with DSP responses required within 2 ms when using third-party ISVs. 
+  Large user profile stores (100 million to 5 billion profiles) requiring sub-millisecond read latency. 
+  Traffic variability, with spikes of 10x or more during live events and seasonal campaigns. 
+  Data transfer is the dominant cost category. Even small optimizations compound at RTB scale. 
+  Low revenue and profit margin per transaction drives the focus on cost efficiency. 
+  Rapid changes in traffic volumes and associated fluctuations in compute and network infrastructure. 

## Reference architecture
<a name="s01-reference-architecture"></a><a name="scenario-01-fig1"></a>

![Ad serving architecture on AWS showing the publisher ad request path through SSP, ad exchange, and supporting data stores connected through AWS RTB Fabric, with Kinesis for event capture, ElastiCache for user profiles, and DynamoDB for campaign data](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-01a-ad-serving.jpg)


 The architecture consists of the following components: 

1.  **Publisher ad request**: A viewer loads a page or starts a video stream. The publisher's ad server detects an ad opportunity and initiates a programmatic auction. 

1.  **SSP (Supply-Side Platform)**: The SSP receives the ad request, packages it as an OpenRTB bid request, and fans out to demand partners. Deployed on Amazon EKS across multiple Availability Zones with Karpenter for fast scaling. 

1.  **AWS RTB Fabric**: Purpose-built private network connecting SSP and DSP partners. Provides single-digit millisecond latency, per-transaction pricing that replaces per-GB NAT Gateway charges, and built-in OpenRTB Filter and Rate Limiter modules for traffic management. 

1.  **DSP (Demand-Side Platform)**: The DSP receives bid requests, enriches them with user profile and targeting data, evaluates against campaign constraints, and returns bid responses. The bid evaluation tier runs on Compute Optimized (C-series) EC2 instances or EKS pods with Karpenter. 

1.  **User profile store**: Aerospike on Storage Optimized (I-series) instances with NVMe-backed local storage, providing sub-millisecond user profile reads for bid enrichment. DynamoDB TTL expires profiles older than 30 days, with older data archived to S3. 

1.  **Amazon ElastiCache**: In-memory cache (Redis) colocate in the same Availability Zones as bidder compute for frequency caps, audience segments, and creative metadata. Provides sub-millisecond cache reads that avoid database round-trips on the bid path. 

1.  **Amazon Kinesis Data Streams**: Captures OpenRTB bid events asynchronously from the bid path, routing to Amazon Data Firehose for delivery to S3 data lake and Amazon Managed Service for Apache Flink for real-time analytics. 

1.  **Amazon DynamoDB**: Stores campaign configurations, bid floors, and targeting parameters. Used with DynamoDB Accelerator (DAX) for microsecond reads of frequently accessed campaign data. 

1.  **Analytics data lake (Amazon S3)**: Long-term storage for bid events, impression logs, and campaign performance data in Apache Parquet format with Snappy compression. Queried through Amazon Athena for attribution and reporting. 

## Configuration notes
<a name="s01-configuration-notes"></a>

### Bid path latency
<a name="bid-path-latency"></a><a name="scenario-01-fig2"></a>

![Realtime bidder architecture on AWS showing the DSP bid evaluation tier on Compute Optimized EC2 or EKS with Karpenter, colocated ElastiCache for sub-millisecond reads, and AWS RTB Fabric Managed Endpoints routing bid traffic directly to bidder pod IPs](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-01b-realtime-bidder.jpg)


 Deploy bid evaluation on Compute Optimized EC2 instances (C7i Intel, C7g Graviton) with ElastiCache Redis colocate in the same Availability Zone. Implement fast-fail patterns with no exponential backoff on the bid path. Use AWS RTB Fabric for partner connectivity to replace per-GB NAT Gateway charges with per-transaction pricing. 

 Use AWS RTB Fabric Managed Endpoints to route bid traffic directly from responder gateways to individual bidder pod IPs on EKS, removing the NLB and ingress controller layers from the critical path. This reduces network hops and avoids TCP-level head-of-line blocking risk from intermediate load balancers. 

### User profile storage
<a name="user-profile-storage"></a>

 Use Aerospike on Storage Optimized instances (I4i) for the highest-throughput, lowest-latency profile access. Configure Aerospike's Availability Zone affinity feature so client applications access nodes in the same Availability Zone, avoiding cross-AZ transfer charges on high-frequency read paths. Apply DynamoDB TTL to expire profiles beyond the 30-day hot window. 

### Traffic filtering
<a name="traffic-filtering"></a><a name="scenario-01-fig3"></a>

![AdTech private network on AWS showing the AWS RTB Fabric connecting SSP and DSP partners over a purpose-built private network with OpenRTB Filter and Rate Limiter modules replacing public internet routing and NAT Gateway charges](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-01c-adtech-private-network.jpg)


 Configure RTB Fabric OpenRTB Filter to reject malformed requests, unsupported protocols, and floor-price-mismatched inventory at the network layer before they consume application compute. Build per-DSP bid rate profiles segmented by inventory type, geo, device type, and time of day. Suppress low-probability requests before sending using holdback-tested filter rules. 

### Scaling for variable demand
<a name="scaling-for-variable-demand"></a>

 Perform regular load tests at five times the baseline RTB traffic to validate capacity projections. Use Karpenter for fast node provisioning during traffic spikes. Configure per-partner rate limits using RTB Fabric Rate Limiter to guard against a single partner's traffic spike consuming capacity allocated to others. 

### Cost optimization
<a name="cost-optimization"></a>

 Replace NAT Gateways for RTB partner traffic with AWS RTB Fabric (84–87% networking cost reduction). Colocate SSP and DSP components in the same Availability Zones with NLB cross-zone load balancing disabled to avoid cross-AZ transfer charges. Deploy analytics processing on Spot Instances with checkpointing. 