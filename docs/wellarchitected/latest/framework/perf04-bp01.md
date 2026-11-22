

# PERF04-BP01 Understand how networking impacts performance

 Networking connects every part of a distributed workload, so network decisions shape latency, throughput, and user experience. Treating a cloud network like an on-premises data center recreates old bottlenecks and wastes capacity. 

 **Desired outcome:** 
+  You have documented network requirements for each workload, including latency, bandwidth, packet size, protocols, traffic patterns, and routing rules. 
+  Your network design decisions rest on measured workload characteristics, not assumptions carried over from on-premises environments. 
+  You know which network metrics matter for your workload and where bottlenecks are most likely to appear. 

 **Common anti-patterns:** 
+  Teams route all traffic back through existing data centers rather than using cloud-native paths. 
+  Teams send every flow through central firewalls instead of cloud-native network security controls. 
+  Teams provision dedicated connections without understanding actual bandwidth and latency requirements. 
+  Teams ignore workload characteristics and encryption overhead when they design networking. 
+  Teams apply on-premises networking concepts and topologies directly to the cloud. 

 **Benefits of establishing this best practice:** 
+  You identify potential bottlenecks before they reach production. 
+  You improve user experience by reducing avoidable latency. 
+  You increase reliability because the network design matches real traffic patterns. 
+  You lower operational maintenance as the workload changes, because the network can evolve without hardware changes. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A request that crosses Regions, traverses a VPN, or waits on a TLS handshake carries delay that compute tuning cannot remove. Latency between services adds up across a call chain, and one constrained link caps throughput for everything behind it. 

 Four properties describe most network behavior, and they interact. Latency is one-way packet travel time. Bandwidth is the maximum data rate a link supports. Throughput is the rate you achieve. Jitter is variation in latency over time. Throughput depends on both bandwidth and latency, so a high-bandwidth link with high latency still delivers poor throughput for protocols that wait for acknowledgements. Packet loss, congestion, and routing add further variation. Identify which of these properties your workload is sensitive to. 

 The most common mistake is importing on-premises assumptions. On-premises networks are fixed: you buy hardware, run cables, and route traffic through appliances that sit in one place. Cloud networks are software-defined, so you can rebuild topology, add paths, and move inspection points without touching hardware. If you route all cloud traffic back through a central data center, or force every flow through one firewall, you recreate on-premises bottlenecks. Traffic that never needed to leave the cloud picks up extra latency. 

 Every security and reliability control has a performance cost. Encryption in transit adds handshake round-trips and per-packet processing. Traffic inspection adds hops. Per-flow bandwidth limits mean a single connection cannot always saturate an instance's total network capacity. A workload built around one large flow behaves differently from one that spreads load across many flows. Measure these costs and design around them. 

 Network telemetry spans several layers. Foundational metrics come from VPC and transit gateway flow logs. Application-layer visibility comes from network adapters and service meshes. Edge and hybrid connectivity each expose their own metrics, and distributed tracing ties latency back to a specific hop. Build this observability before you have a problem. You can then tell whether a slow request is the application, the network, or the path between Regions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Document network performance requirements:** Record the metrics that define acceptable performance for the workload, including network latency, bandwidth, protocols, locations, traffic patterns (spikes and frequency), throughput, encryption, inspection, and routing rules. Capture both steady-state and peak conditions so the design accounts for spikes. 

1.  **Map requirements to networking services:** Match each requirement to the service that meets it. Review foundational and connectivity options such as [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html), [AWS Direct Connect](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html), [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), and [Amazon Route 53](https://aws.amazon.com/route53/). 

1.  **Capture networking characteristics across layers:** Instrument each layer of your network so you can attribute performance to a specific component. The following tools cover foundational, application, edge, hybrid, security, and tracing characteristics. 


<table>
<thead>
  <tr><th> Characteristic </th><th> Tools and metrics </th></tr>
</thead>
<tbody>
  <tr><td> Foundational </td><td> <a href="https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html">VPC Flow Logs</a>, <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html">AWS Transit Gateway Flow Logs</a>, <a href="https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-cloudwatch-metrics.html">Transit Gateway metrics</a>, <a href="https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-cloudwatch-metrics.html">AWS PrivateLink metrics</a> </td></tr>
  <tr><td> Application </td><td> <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-network-performance-ena.html">Elastic Fabric Adapter monitoring</a>, <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-cloudwatch.html">Amazon VPC Lattice metrics</a>, <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Amazon ECS Service Connect metrics</a>, <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html">Amazon API Gateway metrics</a> </td></tr>
  <tr><td> Edge </td><td> <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html">Amazon CloudFront metrics</a>, <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-cloudwatch.html">Amazon Route 53 metrics</a>, <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/cloudwatch-monitoring.html">AWS Global Accelerator metrics</a> </td></tr>
  <tr><td> Hybrid </td><td> <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html">AWS Direct Connect metrics</a>, <a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-cloudwatch-vpn.html">AWS Site-to-Site VPN metrics</a>, <a href="https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/monitoring-cloudwatch.html">AWS Client VPN metrics</a>, <a href="https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-cloudwatch-metrics.html">AWS Cloud WAN metrics</a>, <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html">Network Synthetic Monitor</a> </td></tr>
  <tr><td> Security </td><td> <a href="https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html">AWS Shield, AWS WAF, and AWS Network Firewall metrics</a> </td></tr>
  <tr><td> Tracing </td><td> <a href="https://aws.amazon.com/cloudwatch/features/application-observability-apm/">Application Observability (APM)</a>, <a href="https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html">Reachability Analyzer</a>, <a href="https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html">Network Access Analyzer</a>, <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-What-is-NetworkFlowMonitor.html">Amazon CloudWatch Network Flow Monitor</a>, <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.what-is-cwim.html">Amazon CloudWatch Internet Monitor</a>, <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html">Amazon CloudWatch RUM</a> </td></tr>
</tbody>
</table>


1.  **Benchmark and test network performance:** [Benchmark network throughput](https://repost.aws/knowledge-center/network-throughput-benchmark-linux-ec2) between instances in the same VPC to establish a baseline, because placement and instance type affect results. Use [APerf](https://github.com/aws/aperf) to collect network interface, CPU, and memory metrics from the instance during a benchmark so you can correlate network results with system-level behavior. Run [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) to compare networking options under realistic traffic before you commit to a design. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF04-BP02 Evaluate available networking features](perf04-bp02.md) 
+  [PERF04-BP06 Choose your workload's location based on network requirements](perf04-bp06.md) 
+  [PERF04-BP07 Optimize network configuration based on metrics](perf04-bp07.md) 

 **Related documents:** 
+  [Concepts: AWS Regions, Availability Zones, Local Zones, AWS Outposts, and Wavelength Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) 
+  [Amazon EC2 enhanced networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) 
+  [Amazon EC2 enhanced networking on Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) 
+  [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) 
+  [Amazon EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) 
+  [Enable enhanced networking with the Elastic Network Adapter (ENA) on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html) 
+  [Transition to latency-based routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html) 
+  [Optimizing application performance: The strategic benefits of combining Amazon CloudFront with Application Load Balancers](https://aws.amazon.com/blogs/networking-and-content-delivery/optimizing-application-performance-the-strategic-benefits-of-combining-amazon-cloudfront-with-application-load-balancers/) 
+  [Performance Testing on AWS](https://docs.aws.amazon.com/solutions/latest/performance-testing/overview.html) 

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
+  [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) 
+  [Guidance for Network Connectivity on AWS](https://docs.aws.amazon.com/solutions/network-connectivity-on-aws/) 

 **Related workshops:** 
+  [AWS Networking Workshop](https://catalog.workshops.aws/networking/) 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US) 
+  [Hands-on Network Firewall Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/d071f444-e854-4f3f-98c8-025fa0d1de2f/en-US) 
+  [Observing and diagnosing your network on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US) 
+  [Improve Your Architecture With Amazon CloudFront](https://catalog.workshops.aws/improve-architecture-with-cloudfront/en-US) 
+  [AWS DevOps Agent Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/767d3081-b4fa-4e08-81da-17e5c94a1a08/en-US) 