

# PERF04-BP06 Choose your workload's location based on network requirements

 Traffic that crosses continents is slower than traffic served nearby. Placing resources close to users and caching content at the edge reduces page load and data transfer times for remote users. 

 **Desired outcome:** 
+  You place resources in the locations that minimize latency for your workload's users. 
+  You use edge locations to cache content and shorten the path between users and your workload. 
+  Your placement decisions reflect where users and data are, not only where your team is located. 

 **Common anti-patterns:** 
+  Teams consolidate all workload resources into one geographic location. 
+  Teams choose the Region closest to their office rather than to the workload's end users. 
+  Teams serve a global audience from a single Region without edge caching or acceleration. 

 **Benefits of establishing this best practice:** 
+  You reduce latency for users by placing resources close to them. 
+  You improve throughput and page load times through edge caching and optimized routing. 
+  You deliver a consistent experience to a global audience using the AWS private global network. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A request between continents spends tens of milliseconds on fiber alone. Proximity to users and data is the most effective way to reduce latency. 

 AWS placement options trade reach against proximity. [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) and their Availability Zones cover broad geographies. [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) push compute and storage into metropolitan areas closer to users. [AWS Outposts](https://aws.amazon.com/outposts/) runs AWS infrastructure in your own data center for workloads that must stay on-premises. [AWS Wavelength](https://aws.amazon.com/wavelength/) embeds infrastructure inside 5G networks for ultra-low-latency mobile applications. Match the option to your latency requirement. 

 Edge services cache content and terminate connections at locations near users. They route traffic across the AWS private global network instead of the public internet. Content delivery and DNS at the edge answer many requests without reaching your origin. Cache-control settings for DNS and HTTP determine how much traffic the edge absorbs, and incorrect settings serve stale content or defeat the cache. 

 Place user-facing applications close to users. Place data-heavy applications, such as analytics and machine learning, close to their data, because moving large datasets across Regions is slow and costly. When users and data are far apart, prioritize one or split the workload so each part is close to what it needs. Cost and compliance add further constraints, since not every workload can run in every Region. 

 Placement matters within a Region too. Placement groups cluster instances to reduce latency and increase throughput between them, which helps tightly coupled workloads. For these workloads, pair supported instance types with an Elastic Network Adapter for a low-latency, high-throughput path between nodes. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Capture traffic and access patterns:** Log IP traffic with [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) and, where you use acceleration, [preserve the client IP address in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.headers.html). If you use Amazon CloudFront, turn on [access logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) to see the geographic distribution of viewers and which edge locations serve them. Analyze the data with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to learn how users reach your application. 

1.  **Select Regions from data, users, and constraints:** Run data-heavy applications as close to the data as possible. Place user-facing applications in the Region or Regions closest to users. Do not assume geographic proximity equals lowest latency. [Measure network latency to candidate Regions before deployment](https://aws.amazon.com/blogs/networking-and-content-delivery/measuring-network-latency-to-aws-region-before-deployment/), because routing paths can make a farther Region faster than a nearer one. Weigh other constraints such as cost and compliance, as described in [what to consider when selecting a Region for your workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/). 

1.  **Extend closer to users where latency demands it:** Use [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) to run applications close to end users for real-time gaming, live streaming, AR/VR, virtual workstations, and ISV application acceleration. Use [AWS Outposts](https://aws.amazon.com/outposts/) for workloads that must remain on-premises while running consistently with the rest of your AWS environment. Use [AWS Wavelength](https://aws.amazon.com/wavelength/) for ultra-low-latency 5G applications such as live video, high-fidelity audio, and AR/VR. Wavelength embeds AWS infrastructure inside [telecommunications carrier partner networks](https://aws.amazon.com/blogs/industries/lower-access-latency-for-your-apps-with-aws-wavelength-and-our-telco-partners), so your effective latency depends on which carrier partner serves your users in each metro area. 

1.  **Extend closer to partners where latency demands it:** For workloads such as high-frequency trading and crypto market-making, where competitive edge depends on shaving microseconds off the path to an exchange or counterparty, use a [shared placement group](https://aws.amazon.com/blogs/industries/crypto-market-making-latency-and-amazon-ec2-shared-placement-groups/) so your instances launch physically close to your trading partner's instances within the same Availability Zone. Combine this with a [Capacity Reservation in the placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html) so that low-latency capacity is available when you need to scale. 

1.  **Cache frequently used content:** Use [AWS caching solutions](https://aws.amazon.com/caching/aws-caching/) to reduce data movement and latency for repeated requests. 


<table>
<thead>
  <tr><th> Service </th><th> When to use </th></tr>
</thead>
<tbody>
  <tr><td> <a href="https://aws.amazon.com/cloudfront/">Amazon CloudFront</a> </td><td> Cache static content such as images, scripts, and videos, and dynamic content such as API responses. </td></tr>
  <tr><td> <a href="https://aws.amazon.com/elasticache/">Amazon ElastiCache</a> </td><td> Fully managed caching service delivering microsecond latency performance with full Valkey, Memcached, and Redis OSS compatibility. </td></tr>
  <tr><td> <a href="https://aws.amazon.com/dynamodbaccelerator/">Amazon DynamoDB Accelerator</a> </td><td> Add in-memory acceleration to DynamoDB tables. </td></tr>
  <tr><td> <a href="https://aws.amazon.com/filecache/">Amazon File Cache</a> </td><td> Cache file data from on-premises file systems, AWS file systems, and Amazon S3 buckets for high-throughput, low-latency access by file-based applications. </td></tr>
</tbody>
</table>


1.  **Run code closer to users:** Move compute to the edge for requests that benefit from proximity. 


<table>
<thead>
  <tr><th> Service </th><th> When to use </th></tr>
</thead>
<tbody>
  <tr><td> <a href="https://aws.amazon.com/lambda/edge/">Lambda@Edge</a> </td><td> Compute-heavy operations initiated when objects are not in the cache. </td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html">Amazon CloudFront Functions</a> </td><td> Lightweight HTTP request or response manipulations from short-lived functions. </td></tr>
  <tr><td> <a href="https://aws.amazon.com/greengrass/">AWS IoT Greengrass</a> </td><td> Local compute, messaging, and data caching for connected devices. </td></tr>
</tbody>
</table>


1.  **Provide static entry points and TCP termination at the edge:** For HTTP and HTTPS workloads, use [Amazon CloudFront](https://aws.amazon.com/cloudfront/) in front of your origin even for uncacheable, dynamic content: it terminates the client's TLS connection at the nearest edge location and reuses a persistent connection back to the origin, removing the handshake latency a distant client would otherwise pay on every request. For applications that need fixed entry points, non-HTTP protocols, or quick failover, use [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/). Unlike CloudFront, it works at the network layer for any TCP or UDP traffic, not just HTTP, so it also suits gaming, IoT, and voice workloads. It provides static anycast IP addresses that bring traffic onto the AWS global network close to users, and it sets up the TCP connection at the nearest edge location to reduce initial connection time. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF04-BP02 Evaluate available networking features](perf04-bp02.md) 
+  [SUS04-BP03 Implement distributed systems appropriately](sus04-bp03.md) 
+  [FND07-BP01 Define your network and connectivity strategy and centralized resources](fnd07-bp01.md) 
+  [COST04-BP03 Optimize services to reduce data transfer costs](cost04-bp03.md) 

 **Related documents:** 
+  [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) 
+  [Placement groups for your Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) 
+  [Network latency concepts and best practices for a resilient architecture](https://aws.amazon.com/blogs/networking-and-content-delivery/network-latency-concepts-and-best-practices-for-a-resilient-architecture/) 
+  [Region selection criteria for networking](https://aws.github.io/aws-networking-best-practices/foundation/regions-azs/#region-selection-criteria-for-networking) 
+  [Differences between CloudFront Functions and Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-choosing.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - AWS Networking Fundamentals: Connect, secure and scale (NET208)](https://www.youtube.com/watch?v=nXBqxnp5ybY&feature=youtu.be) 
+  [AWS re:Invent 2025 - Advanced VPC design and new capabilities (NET340)](https://www.youtube.com/watch?v=40QfxdvDGsw&feature=youtu.be) 
+  [AWS re:Invent 2024 - Dive into the depths of routing on AWS (NET318)](https://www.youtube.com/watch?v=2tHMnbTj4pw&feature=youtu.be) 
+  [AWS re:Invent 2024 - AWS application networking: Build simple, secure, and reliable apps](https://www.youtube.com/watch?v=-obQxSPclrw) 

 **Related examples:** 
+  [Guidance for Network Connectivity on AWS](https://docs.aws.amazon.com/solutions/network-connectivity-on-aws/) 