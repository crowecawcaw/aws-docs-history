

# PERF04-BP02 Evaluate available networking features

 The cloud exposes network features that reduce latency, shorten the distance traffic travels, and raise throughput. Not every feature helps every workload, and each one adds configuration or cost. When you evaluate features against measured requirements and confirm their impact through testing, you improve performance without adding complexity that does not pay off. 

 **Desired outcome:** 
+  You evaluate available networking features against your workload's latency, bandwidth, and geographic distribution needs. 
+  You measure the impact of each feature you adopt through testing and metrics rather than assuming benefit. 
+  Your architecture uses the features that improve performance and skips those that add cost or complexity without measurable gain. 

 **Common anti-patterns:** 
+  Teams stay in one Region because that is where the headquarters sits, ignoring where users are. 
+  Teams use standalone firewalls for traffic filtering instead of cloud-native controls such as security groups. 
+  Teams break TLS for inspection rather than relying on security groups, endpoint policies, and other cloud-native controls. 
+  Teams rely on subnet-based segmentation alone instead of security groups. 

 **Benefits of establishing this best practice:** 
+  You increase workload performance by adopting features that address real bottlenecks. 
+  You reduce infrastructure cost and maintenance effort by skipping features that add no measurable value. 
+  You improve the experience for a global audience by using the AWS backbone and edge network. 
+  You strengthen security posture because cloud-native controls replace inspection detours that add latency. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Each feature adds configuration, cost, or operational surface. Match each feature to a measured bottleneck. 

 Global acceleration and content delivery shorten the distance between users and your workload. They move traffic onto a private backbone or cache it at the edge. Enhanced adapters, placement groups, and storage-optimized instances raise how much data each node can move inside a Region. 

 Establish a baseline before evaluating features. The baseline tells you whether the workload is network-bound and where its bottlenecks are. For an existing workload, capture current bandwidth, latency, packet loss, jitter, and retransmits. For a new workload, load test until it breaks. 

 Elastic network interfaces enforce per-flow bandwidth caps. A workload that pushes everything through one connection cannot use an instance's full capacity regardless of which adapter it has. Spreading load across multiple flows often matters more than any single feature. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory your workload components and connections:** Use an existing configuration management database or [AWS Config](https://aws.amazon.com/config/) to record each component and how it is configured. When you build a unified global network across accounts, consider [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/) to build, manage, and monitor it from one place. 

1.  **Establish a performance baseline:** For an existing workload, document benchmark metrics and focus on the bottlenecks: bandwidth, latency, packet loss, jitter, and retransmits. For a new workload, Run [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) to find where performance breaks. Use [AWS Network Manager](https://aws.amazon.com/products/) to view aggregate latency between and within Regions and Availability Zones, [Amazon CloudWatch metrics](https://docs.aws.amazon.com/network-manager/latest/tgwnm/monitoring-cloudwatch-metrics.html) for global and core networks, and [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) for client-side experience. Use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) and [CloudWatch AI Operations: Investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) to correlate this telemetry and help identify where the baseline is bounded by the network versus the application. 

1.  **Match features to each bottleneck:** For every bottleneck you identified, review the configuration options and features that address it. 


<table>
<thead>
  <tr><th> Improvement opportunity </th><th> Options to evaluate </th></tr>
</thead>
<tbody>
  <tr><td> Network path or routes </td><td> Use <a href="https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html">Network Access Analyzer</a> to identify paths and routes. </td></tr>
  <tr><td> Network protocols </td><td> See <a href="perf04-bp05.md">PERF04-BP05 Choose network protocols to improve performance</a>. </td></tr>
  <tr><td> Network topology </td><td> Weigh the operational and performance trade-offs between <a href="https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html">VPC peering</a>, <a href="https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html">AWS PrivateLink</a>, and <a href="https://aws.amazon.com/transit-gateway/">AWS Transit Gateway</a> when connecting multiple accounts. PrivateLink gives one-directional, private access to a specific service across accounts and Regions without exposing the rest of the VPC. Transit Gateway interconnects VPCs across thousands of accounts and into on-premises networks, and you can share it with <a href="https://aws.amazon.com/ram/">AWS Resource Access Manager</a>. See <a href="perf04-bp03.md">PERF04-BP03 Choose appropriate dedicated connectivity or VPN for your workload</a>. </td></tr>
  <tr><td> Network services </td><td> <a href="https://aws.amazon.com/global-accelerator/">AWS Global Accelerator</a> improves traffic performance over the AWS global network. <a href="https://aws.amazon.com/cloudfront/">Amazon CloudFront</a> improves content delivery and latency globally, and <a href="https://aws.amazon.com/lambda/edge/">Lambda@Edge</a> customizes that content closer to users. Amazon Route 53 offers <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html">latency-based</a>, <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html">geolocation</a>, <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html">geoproximity</a>, and <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-ipbased.html">IP-based</a> routing to match users to the closest endpoint. </td></tr>
  <tr><td> Storage features </td><td> <a href="https://aws.amazon.com/s3/transfer-acceleration/">Amazon S3 Transfer Acceleration</a> uses the CloudFront network to speed large uploads from remote locations. <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html">Amazon S3 Multi-Region Access Points</a> route requests to the lowest-latency bucket through a single access point. </td></tr>
  <tr><td> Compute features </td><td> <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html">Elastic network interfaces</a> apply per-flow limits, so design applications to use multiple flows and review <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html">instance network bandwidth</a> and placement groups. <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html">Elastic Network Adapter</a>, <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html">ENA Express</a>, and <a href="https://aws.amazon.com/hpc/efa/">Elastic Fabric Adapter</a> raise throughput and lower tail latency, and <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html">Amazon EBS-optimized instances</a> add dedicated storage I/O capacity. Monitor these with CloudWatch and <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-network-performance-ena.html">ethtool metrics from the ENA driver</a> published as <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html">custom metrics</a>. </td></tr>
</tbody>
</table>


1.  **Test and confirm the impact:** Re-run your baseline measurements after you adopt a feature. Keep the change if the metric improves against your requirements, and remove it if the gain does not justify the added cost or complexity. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF04-BP01 Understand how networking impacts performance](perf04-bp01.md) 
+  [PERF04-BP03 Choose appropriate dedicated connectivity or VPN for your workload](perf04-bp03.md) 
+  [PERF04-BP05 Choose network protocols to improve performance](perf04-bp05.md) 
+  [PERF04-BP06 Choose your workload's location based on network requirements](perf04-bp06.md) 

 **Related documents:** 
+  [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) 
+  [Amazon EC2 instance types](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html) 
+  [Amazon EC2 enhanced networking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) 
+  [Amazon EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) 
+  [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) 
+  [Networking products with AWS](https://aws.amazon.com/products/networking/) 
+  [Transition to latency-based routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html) 
+  [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html) 
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Advanced VPC design and new capabilities (NET340)](https://www.youtube.com/watch?v=40QfxdvDGsw&feature=youtu.be) 
+  [AWS re:Invent 2025 - AWS Networking Fundamentals: Connect, secure and scale (NET208)](https://www.youtube.com/watch?v=nXBqxnp5ybY&feature=youtu.be) 
+  [AWS re:Invent 2025 - Powering your success through AWS Infrastructure innovations (NET402)](https://www.youtube.com/watch?v=YQOuYK23VEI&feature=youtu.be) 
+  [AWS re:Invent 2024 - Design well-architected networks on AWS](https://www.youtube.com/watch?v=Pd5p-fzwsLA) 
+  [AWS re:Invent 2024 - Dive into the depths of routing on AWS (NET318)](https://www.youtube.com/watch?v=2tHMnbTj4pw&feature=youtu.be) 
+  [AWS re:Invent 2024 - Amazon CloudFront: Enhancing web performance one HTTP request at a time (CDN308)](https://www.youtube.com/watch?v=lLnKaPqL3u0&feature=youtu.be) 
+  [AWS re:Invent 2023 - What can networking do for your application?](https://www.youtube.com/watch?v=tUh26i8uY9Q) 
+  [AWS re:Invent 2023 - Building hybrid network connectivity with AWS (TNC217)](https://www.youtube.com/watch?v=Fi4me2vPwrQ&feature=youtu.be) 
+  [Diving Deep on AWS DevOps Agent \| AWS Tech Tales](https://www.youtube.com/live/PcbOQAtT13I) 

 **Related examples:** 
+  [Guidance for Network Connectivity on AWS](https://docs.aws.amazon.com/solutions/network-connectivity-on-aws/) 

 **Related workshops:** 
+  [AWS Networking Workshop](https://catalog.workshops.aws/networking/) 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US) 
+  [Hands-on Network Firewall Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/d071f444-e854-4f3f-98c8-025fa0d1de2f/en-US) 
+  [Observing and diagnosing your network on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US) 
+  [Improve Your Architecture With Amazon CloudFront](https://catalog.workshops.aws/improve-architecture-with-cloudfront/en-US) 
+  [AWS DevOps Agent Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/767d3081-b4fa-4e08-81da-17e5c94a1a08/en-US) 