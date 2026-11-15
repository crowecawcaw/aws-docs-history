

# ADVCOST03-BP09 Use built-in fabric load balancing instead of dedicated load balancers
<a name="advcost03-bp09"></a>

 A managed bidding fabric can distribute traffic to compute instances and container platforms through DNS-based routing. This removes the need for dedicated load balancers, along with their hourly fees and per-LCU charges at high RTB-scale QPS. 

 **Desired outcome:** 
+  Dedicated load balancers for RTB partner traffic are removed, with traffic distribution handled natively by RTB Fabric's built-in DNS-based routing capabilities. 
+  Infrastructure as code is updated to remove RTB-dedicated load balancer resources. 

 **Common anti-patterns:** 
+  Maintaining dedicated ALBs or NLBs for RTB partner traffic when RTB Fabric already provides built-in DNS-based traffic distribution, which pays redundant hourly fees and per-LCU charges for functionality that is natively included. 
+  Assuming load balancers are required in every case for traffic distribution without evaluating whether RTB Fabric's built-in routing capabilities meet health checking, distribution, and failover requirements. 
+  Keeping decommissioned load balancers provisioned as a precaution after migrating to fabric-based routing, so hourly charges continue on idle resources. 
+  Deploying both fabric-based routing and a load balancer in series, which adds an unnecessary intermediate hop that increases latency and cost. 
+  Failing to calculate the total cost of existing load balancers (hourly fees plus LCU charges at RTB-scale QPS) before migration. 

 **Benefits of establishing this best practice:** 
+  Remove hourly and LCU-based load balancer charges for RTB traffic. 
+  Simplified architecture with fewer components to manage. 
+  Availability Zone-aware routing distributes QPS efficiently within each Availability Zone. 
+  Reduced latency by removing an intermediate hop from the traffic path. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Traditional load balancers (Application Load Balancer and Network Load Balancer) charge both an hourly fee and a per-LCU fee that scales with connection count, bandwidth, and rule evaluations. At RTB-scale QPS (hundreds of thousands of requests per second), LCU charges alone can exceed the base hourly cost by an order of magnitude. [RTB Fabric](https://aws.amazon.com/rtb-fabric/) includes DNS-based traffic distribution as part of its per-transaction pricing, so load balancing adds no cost beyond what you already pay for RTB Fabric connectivity. Before you remove a load balancer, confirm that fabric-based routing meets your requirements without one in the path. 

 A load balancer inspects every connection and routes it to a specific backend based on health checks, connection counts, or request attributes. DNS-based routing resolves endpoints to healthy hosts at DNS query time, then traffic flows directly to those hosts until the next DNS resolution. This makes distribution granularity coarser. Traffic shifts happen at DNS TTL intervals rather than per connection. For RTB workloads where requests are short-lived (sub-100ms) and stateless, this coarser granularity is acceptable because no single request requires session affinity or connection draining. 

 ALBs provide path-based routing, header inspection, AWS WAF integration, and detailed access logs per request. NLBs provide static IPs, TLS termination at scale, and cross-zone load balancing with per-connection granularity. Removing the load balancer leaves a gap if your RTB traffic relies on any of these features for security, compliance, or operational visibility. Audit which of these features your RTB traffic uses. A general-purpose template may configure more than you need. 

 An intermediate hop (the load balancer) adds 1-3 ms, so removing it can reduce latency. DNS routing can temporarily send disproportionate traffic to a subset of hosts during scaling events if DNS caches have not expired. Run both paths for one to two weeks under production load to confirm equivalent error rates and latency percentiles before decommissioning. 

 Load balancers can reappear by accident after you remove them. IaC templates and Kubernetes ingress controllers often create them automatically as part of service deployment. If the RTB service definition still references a LoadBalancer-type service or an ingress resource, the next deployment recreates the resource and resumes hourly billing. Remove the load balancer at the orchestration layer (Helm charts, Terraform modules, and CDK constructs). Deleting the AWS resource alone is not enough. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory RTB-dedicated load balancers and calculate monthly cost:** List all ALBs and NLBs serving RTB partner traffic. Calculate total monthly cost including hourly fees and LCU charges at current QPS levels. 

1.  **Configure RTB Fabric responder gateway with DNS-based routing:** Enable RTB Fabric managed endpoints for your bidder fleet (EKS Managed Endpoints for Kubernetes-based deployments, and EC2 ASG Managed Endpoints for Auto Scaling Group-based fleets). Configure health check endpoints and thresholds. 

1.  **Validate RTB Fabric routing in parallel with existing load balancer:** Run both paths in parallel for 1-2 weeks. Compare latency, error rates, and traffic distribution between RTB Fabric routing and the existing load balancer. Confirm equivalent or better performance before decommissioning. 

1.  **Decommission dedicated load balancers and update IaC:** After validation, shift 100% of RTB partner traffic to RTB Fabric routing. Delete dedicated load balancer resources. Update infrastructure as code templates to guard against recreation. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST03-BP05 Replace per-gigabyte egress with transaction-priced partner connectivity](advcost03-bp05.md) 
+  [ADVCOST03-BP02 Implement Availability Zone affinity across the RTB data path](advcost03-bp02.md) 

 **Related documents:** 
+  [AWS RTB Fabric Features](https://aws.amazon.com/rtb-fabric/features/) 
+  [AWS RTB Fabric Managed Endpoints](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/managed-endpoints.html) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 