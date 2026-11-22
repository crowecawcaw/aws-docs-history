

# Networking and content delivery

 The optimal networking solution for an advertising workload varies based on latency, throughput requirements, jitter, and bandwidth. AWS offers networking features including [Amazon Route 53](https://aws.amazon.com/route53/) latency routing, [Amazon VPC](https://aws.amazon.com/vpc/) endpoints, [AWS Direct Connect](https://aws.amazon.com/directconnect/), [Amazon CloudFront](https://aws.amazon.com/cloudfront/), and [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) to reduce network latency and jitter. For advertising workloads, network architecture is more important than in most systems because every ad request depends on a stable network path. A well-designed network directly affects both the performance and the viewer experience of advertising workloads on AWS. 


|  ADVPERF05: How do you design and configure your network architecture to meet the performance requirements of your advertising workload?  | 
| --- | 
| [ADVPERF05-BP01 Establish private connections between your VPC and AWS services to improve performance](advperf05-bp01.md) | 
| [ADVPERF05-BP02 Use edge services for static content caching and dynamic request acceleration](advperf05-bp02.md) | 
| [ADVPERF05-BP03 Use load balancers to improve high availability and load distribution](advperf05-bp03.md) | 
| [ADVPERF05-BP04 Provide dedicated network connection between your on-premises, multicloud environment and AWS](advperf05-bp04.md) | 
| [ADVPERF05-BP05 Use a managed low-latency fabric for real-time bidding infrastructure](advperf05-bp05.md) | 

## Capability intent
<a name="advperf05-capability-intent"></a>
+  Traffic between your advertising workloads and AWS services travels entirely within the AWS private network. Public internet routing is removed from every service call on your data path. 
+  Static advertising content is served from AWS edge locations nearest to viewers, minimizing round-trip latency and reducing origin load. 
+  [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) distributes requests across healthy targets with algorithms matched to your advertising request patterns, and HTTPS termination is offloaded to the load balancer layer. 
+  High-bandwidth workloads with strict compliance requirements connect on-premises advertising infrastructure to AWS over dedicated private connections. 
+  RTB bid traffic flows through a purpose-built, private network ([AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/)) rather than over the public internet, achieving single-digit-millisecond latency with optimized data transfer costs. 

## Common issues to watch for
<a name="advperf05-common-issues-to-watch-for"></a>
+  Accessing AWS services (S3, DynamoDB, and ElastiCache) over public endpoints from within a VPC, routing traffic through the internet gateway and adding latency variability and security exposure. 
+  Serving ad creative assets directly from origin infrastructure in a single Region for a globally distributed audience, forcing every user request to traverse the full distance to your origin. 
+  Performing TLS/HTTPS termination on application servers handling bid evaluation or ad serving logic, consuming CPU cycles on cryptographic operations that a load balancer can handle more efficiently. 
+  Routing RTB bid traffic over the public internet through a traditional NLB-based architecture when RTB Fabric provides purpose-built private connectivity with single-digit-millisecond latency. 