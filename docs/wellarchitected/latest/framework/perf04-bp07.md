

# PERF04-BP07 Optimize network configuration based on metrics

 Base your network configuration on measured behavior. When you collect and analyze network telemetry, you can tune configuration to real traffic and confirm each change improves performance. 

 **Desired outcome:** 
+  You collect the network metrics that reveal how your workload uses the network. 
+  You base configuration changes on analyzed data rather than assumptions or overprovisioning. 
+  You can distinguish network-caused performance issues from application-caused ones. 

 **Common anti-patterns:** 
+  Teams assume every performance issue is application-related. 
+  Teams test network performance only from a location close to the deployment. 
+  Teams use default configurations for all network services. 
+  Teams overprovision network resources to cover for a lack of measurement. 
+  Teams read a throughput ceiling as a network limit without checking for CPU overhead in packet processing. 

 **Benefits of establishing this best practice:** 
+  You understand real network performance instead of guessing at it. 
+  You optimize configuration to match actual traffic patterns. 
+  You avoid paying for capacity that does not address the real bottleneck. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Without measurement, network optimization defaults to overprovisioning: more bandwidth, larger instances, or extra connections that do not address the actual bottleneck. Metrics show whether a slow response is the network, the path, or the application. 

 The metrics that matter are latency, packet loss, throughput, and traffic volume by source. Testing near your deployment hides the latency your distant users experience, so the workload looks fast to the team and slow to those users. Measure from your users' locations, and capture both real-user data and synthetic tests. 

 Flow logs record which sources exchanged traffic and how much, revealing top talkers and traffic patterns. Path and reachability analyzers confirm that traffic takes the intended route, catching misconfiguration. Metric services aggregate counters over time so you can set alarms on trends. IP address management tracks allocation so you do not exhaust address space. 

 Traffic patterns shift as the workload grows and users move, so last quarter's configuration might not fit now. A regular review of metrics keeps topology, routing, and capacity aligned with demand. When application and network teams disagree about the cause of a slowdown, shared network metrics settle the question. 

 When throughput per node plateaus well below the provisioned network bandwidth, profile the CPU cost of packet processing before you add network capacity. Kernel-to-user copies and per-packet system calls can use up CPU before the link saturates. If the data path is CPU-bound, reduce that overhead in software or scale out, and validate either change under load. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify and collect key metrics:** Decide which metrics reveal your workload's network behavior, such as latency and packet loss, and collect them with the tools below. 


<table>
<thead>
  <tr><th> Tool </th><th> Where to use it </th></tr>
</thead>
<tbody>
  <tr><td> <a href="https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html">Amazon VPC IP Address Manager</a> </td><td> Plan, track, and monitor IP address usage for AWS and on-premises workloads. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html">VPC Flow Logs</a> </td><td> Capture traffic to and from network interfaces to diagnose security group rules and traffic direction. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html">AWS Transit Gateway Flow Logs</a> </td><td> Capture IP traffic going to and from your transit gateways. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html">DNS query logging</a> </td><td> Log public and private DNS queries to understand requested domains and responding edge locations. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html">Reachability Analyzer</a> </td><td> Test connectivity between a source and destination to confirm the network matches intended connectivity. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html">Network Access Analyzer</a> </td><td> Specify access requirements and find paths that do not meet them. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html">Amazon CloudWatch</a> </td><td> Turn on metrics for network options such as NAT gateway, Transit Gateway, VPN tunnels, and Elastic Load Balancing, and monitor them continuously. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/network-manager/latest/infrastructure-performance/what-is-nmip.html">Infrastructure Performance</a> </td><td> Obtain near real-time and historical network latency across AWS Regions and across or within Availability Zones for a specified time period. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html">Amazon CloudWatch RUM</a> </td><td> Collect real-user metrics that show where to improve user experience. </td></tr>
</tbody>
</table>


1.  **Identify top talkers and traffic patterns:** Use VPC Flow Logs and AWS Transit Gateway Flow Logs to find which sources generate the most traffic and how patterns change over time. 

1.  **Assess and optimize your network architecture:** Review VPCs, subnets, and routing against the traffic you observed. For example, evaluate whether VPC peering or AWS Transit Gateway improves the connections in your architecture. When a performance issue surfaces, use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) and [CloudWatch AI Operations: Investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) to trace the root cause back to a specific hop or configuration, and feed what you learn back into your architecture and instrumentation so the same class of issue is caught earlier next time. 

1.  **Verify routing paths:** Confirm that traffic takes the shortest path between destinations. Use Network Access Analyzer to check the paths against your intended design. 

1.  **Check for CPU-bound packet processing:** When per-node throughput plateaus below the provisioned bandwidth, profile the data path, for example with flame graphs, to see whether CPU overhead rather than the network is the limit. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF04-BP01 Understand how networking impacts performance](perf04-bp01.md) 
+  [PERF04-BP02 Evaluate available networking features](perf04-bp02.md) 
+  [PERF05-BP05 Review metrics at regular intervals](perf05-bp05.md) 
+  [PERF05-BP01 Use monitoring solutions to understand the areas where performance is most critical](perf05-bp01.md) 

 **Related documents:** 
+  [CloudWatch metrics for your VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cloudwatch.html) 
+  [Monitoring your global and core networks with Amazon CloudWatch metrics](https://docs.aws.amazon.com/network-manager/latest/tgwnm/monitoring-cloudwatch-metrics.html) 

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
+  [AWS network monitoring](https://github.com/aws-samples/monitor-vpc-network-patterns) 
+  [Guidance for Network Connectivity on AWS](https://docs.aws.amazon.com/solutions/network-connectivity-on-aws/) 
+  [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) 
+  [Guidance for Automating Networking Monitoring and Alerting on AWS](https://docs.aws.amazon.com/solutions/automating-networking-monitoring-and-alerting-on-aws/) 

 **Related workshops:** 
+  [AWS Networking Workshop](https://catalog.workshops.aws/networking/) 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US) 
+  [Hands-on Network Firewall Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/d071f444-e854-4f3f-98c8-025fa0d1de2f/en-US) 
+  [Observing and diagnosing your network on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US) 
+  [Improve Your Architecture With Amazon CloudFront](https://catalog.workshops.aws/improve-architecture-with-cloudfront/en-US) 
+  [AWS DevOps Agent Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/767d3081-b4fa-4e08-81da-17e5c94a1a08/en-US) 