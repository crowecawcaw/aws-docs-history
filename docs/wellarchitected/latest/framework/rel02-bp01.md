

# REL02-BP01 Use highly available network connectivity for your workload public endpoints

 Users reach your workload through its public endpoints. If the network path fails, users can't reach the workload even when it is healthy and running. Highly available connectivity spreads that path across redundant components for name resolution, content delivery, load balancing, and traffic routing. If one component fails, users still reach the workload. 

 **Desired outcome:** 
+  Your public endpoints resolve and respond even when an individual network component, path, or location fails. 
+  Your DNS service runs health checks and returns only healthy endpoints to users. 
+  You serve cacheable content from locations close to users, which lowers origin load and improves reachability. 
+  Your endpoints are protected against both volumetric and application-layer denial-of-service attacks. 
+  You have tested loss-of-connectivity scenarios and know how and how quickly traffic fails over. 

 **Common anti-patterns:** 
+  Teams design a highly available workload but leave DNS and network connectivity as single points of failure. 
+  Teams expose individual instances or containers on public internet addresses and manage connectivity to them through DNS. 
+  Teams locate services by IP address instead of by domain name, which defeats DNS failover. 
+  Teams serve content to a wide geographic audience without a content delivery network. 
+  Teams never test scenarios where connectivity to a public endpoint is lost. 
+  Teams do not plan for distributed denial-of-service (DDoS) attacks, which crowd out legitimate traffic and lower availability. 

 **Benefits of establishing this best practice:** 
+  Users continue to reach your workload during the failure of a single network component or location. 
+  Health-based routing directs traffic away from impaired endpoints automatically. 
+  Content served from edge locations improves reachability and reduces the load on your origin. 
+  DDoS protection preserves availability for legitimate users during an attack. 
+  Tested failover paths reduce recovery time when connectivity problems occur. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A user request passes through several independent layers before reaching your workload. Name resolution turns a domain name into an address. An edge or entry point accepts the connection. A load balancer or router distributes the request. Only then does your compute tier run the work. Each layer can fail on its own, and the availability of the whole path is the product of the availability of its layers. Remove single points of failure at every layer. 

 DNS is the first layer. Use a highly available, scalable DNS service such as [Amazon Route 53](https://aws.amazon.com/route53/what-is-dns/) to resolve your domain names. Route 53 runs health checks that mimic real user requests. When an endpoint fails a health check, DNS stops returning it and routes users to healthy endpoints. Resolvers cache records for each record's TTL, so failover is not instant. Shorter TTL values trade higher query volume for faster recovery. Clients that connect by IP address bypass DNS and lose failover, so use domain names to reach services. Route 53 also supports geolocation and latency-based routing to send users to the closest or fastest healthy endpoint. 

 Behind DNS, the entry point must also be redundant. [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) spreads traffic across targets in multiple Availability Zones. A serverless combination of [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) and [AWS Lambda](https://aws.amazon.com/lambda/) provides managed, highly available endpoints with no servers to run. For the highest availability, you can serve the same workload from more than one AWS Region. In a multi-site active/active pattern, several Regions serve traffic at once. In an active/passive pattern, a standby Region takes over when the primary fails. DNS failover moves users between Regions in either case. 

 Content delivery reduces both latency and load on your origin. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) caches content at [edge locations](https://aws.amazon.com/products/networking/edge-networking/) close to users. Most requests never reach your servers, and edge caching absorbs load spikes. A low cache hit ratio sends more traffic to the origin, and dynamic content needs a resilient origin and origin failover. For traffic that cannot be cached, [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) provides two static anycast IP addresses from independent network zones. Global Accelerator pulls traffic onto the AWS global network close to the user and routes it to healthy endpoints across Regions. 

 Denial-of-service attacks operate at different layers, and the defense differs by layer. [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) Standard absorbs infrastructure attacks at layers 3 and 4, such as SYN or UDP floods, and is always on at no extra charge. Larger or more sophisticated attacks call for AWS Shield Advanced. Application-layer floods at layer 7, such as HTTP GET or POST floods, look like normal requests. Use [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html) to inspect and filter them by IP address, headers, body, or request pattern. 

 Rehearse the loss of connectivity to each public endpoint. Confirm that health checks fail over as designed. Measure how long clients take to follow the change given DNS caching. Assign a clear owner to network reachability, separate from the application code. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up highly available DNS:** Use [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html) to manage your domain's records and resolve user requests to your endpoints. Register each public endpoint under a domain name rather than exposing raw IP addresses, so that routing decisions stay under DNS control. 

1.  **Configure health checks and DNS failover:** Create [Route 53 health checks and configure DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html) so that only healthy endpoints are returned. Decide [how Route 53 determines the health of an endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html), then [monitor health check status and set up notifications](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-monitor-view-status.html). Follow the [best practices for Amazon Route 53 DNS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-dns.html) when you set time-to-live values. 

1.  **Route to redundant application endpoints:** Point DNS at redundant entry points. For a load balancer target, create an [alias record](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html) that references the load balancer's Regional endpoint and set Evaluate target health to Yes. For serverless or private APIs, [direct traffic to API Gateway](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-api-gateway.html). 

1.  **Distribute content through a CDN:** Understand [how CloudFront delivers content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html), then create a [distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.SimpleDistribution.html). Raise the [cache hit ratio](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html) to shield your origin, and configure [origin failover](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html) for high availability. 

1.  **Consider a global network entry point:** For a geographically distributed user base, evaluate [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) to provide static anycast entry points and route users to Regional endpoints based on health and performance. 

1.  **Protect against application-layer attacks:** Review [how AWS WAF works](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html) and [get started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html) to filter HTTP floods and common web exploits. When you serve through CloudFront, apply [AWS WAF with CloudFront features](https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html). 

1.  **Add infrastructure DDoS protection:** Confirm that AWS Shield Standard protection is active, then evaluate [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html) for endpoints that need stronger coverage. Review [examples of DDoS-resilient architectures](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-resiliency.html) and [get started with AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL02-BP02 Provision redundant connectivity between private networks in the cloud and on-premises environments](rel02-bp02.md) 
+  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) 
+  [REL11-BP04 Rely on the data plane and not the control plane during recovery](rel11-bp04.md) 
+  [REL11-BP06 Send notifications when events impact availability](rel11-bp06.md) 

 **Related documents:** 
+  [What is AWS Global Accelerator?](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) 
+  [What is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) 
+  [What is Amazon Route 53?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) 
+  [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) 
+  [What is Amazon API Gateway?](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) 
+  [What are AWS WAF, AWS Shield Advanced, AWS Shield network security director and AWS Firewall Manager?](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) 
+  [What is ARC?](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) 
+  [Network Connectivity capability](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/network-connectivity-capability.html) 
+  [APN Partner: partners that can help plan your networking](https://partners.amazonaws.com/search/partners?keyword=network) 
+  [AWS Marketplace for Network Infrastructure](https://aws.amazon.com/marketplace/b/3141913d-a073-4452-8473-843f58081505) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Improve web application performance using AWS Global Accelerator (NET327)](https://www.youtube.com/watch?v=ecNDlRNWW3w) 
+  [AWS re:Invent 2024 - Design well-architected networks on AWS (NET202)](https://www.youtube.com/watch?v=Pd5p-fzwsLA) 
+  [AWS re:Invent 2025 - Global Resilient Apps: Guide to Multi-AZ/Region Architecture with ELB (NET311)](https://www.youtube.com/watch?v=_WFrt9ABrMM) 
+  [AWS re:Invent 2024 - Design well-architected networks on AWS (NET202)](https://www.youtube.com/watch?v=Pd5p-fzwsLA) 

 **Related workshops:** 
+  [Amazon Application Recovery Controller in Practice](https://catalog.us-east-1.prod.workshops.aws/workshops/4d9ab448-5083-4db7-bee8-85b58cd53158/en-US/) 
+  [AWS Global Accelerator Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/7d3a2f4d-43e9-4a6c-b190-d15f64aae67f/en-US) 