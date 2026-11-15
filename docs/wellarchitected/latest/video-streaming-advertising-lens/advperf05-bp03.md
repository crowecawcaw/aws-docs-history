

# ADVPERF05-BP03 Use load balancers to improve high availability and load distribution
<a name="advperf05-bp03"></a>

 Use an elastic load balancer to distribute advertising traffic across healthy targets using algorithms matched to your request patterns. Advertising platforms serve traffic types with different latency and volume characteristics (bid requests, creative assets, and tracking beacons). Isolate these traffic types at the load balancer layer to keep high-volume, latency-tolerant tracking traffic from competing with latency-sensitive bid evaluation for compute. 

 **Desired outcome:** 
+  Bid requests, creative serving requests, and tracking beacons are routed to separate target groups so that tracking traffic volume can't consume compute capacity needed for bid evaluation. 
+  Routing algorithms are matched to the request cost profile of each advertising workload layer: round-robin for equal-cost bid handlers, Least Outstanding Requests for ML inference endpoints with variable processing time. 
+  Unhealthy targets are automatically removed from rotation without manual intervention, with health checks validating auction engine responsiveness rather than just container liveness. 
+  TLS termination is offloaded from application servers handling bid evaluation, releasing CPU for auction logic. 

 **Common anti-patterns:** 
+  Routing all advertising traffic (bid requests, creative serving, and tracking beacons) to the same target group, where high-volume tracking traffic saturates compute capacity needed for latency-sensitive bid evaluation. 
+  Using round-robin routing for ML inference endpoints on the bid evaluation path, where variable inference processing times cause slow calls to queue behind faster ones on overloaded targets while underloaded targets sit idle. 
+  Performing TLS and HTTPS termination on application servers handling bid evaluation or ad serving, which consumes CPU cycles on cryptographic operations that a load balancer can handle more efficiently at advertising-scale request volumes. 
+  Configuring health checks that test only container liveness rather than full auction engine responsiveness, so degraded bid evaluators stay in rotation after the auction engine has failed while the container still answers. 

 **Benefits of establishing this best practice:** 
+  Separating tracking traffic from bid evaluation traffic at the load balancer layer helps avoid the most common source of bid latency degradation at advertising scale. 
+  Least Outstanding Requests routing on ML inference target groups reduces p99 bid response latency by keeping slow inference calls from backing up behind normal requests on saturated targets. 
+  Load balancer TLS offload removes per-request cryptographic overhead from bid evaluation servers. At advertising-scale QPS, this translates directly to additional CPU headroom for auction logic. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB) supports multiple routing algorithms. Use round-robin for ad serving and bid evaluation endpoints where requests are roughly equal in processing cost. Use Least Outstanding Requests (LOR) for workloads with variable request processing times, such as ML inference endpoints. LOR routes new requests to the target with the fewest in-flight requests, producing more even utilization. 

 [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (ALB) supports content-based routing rules (URL path, HTTP headers, query parameters). Use this to route different advertising request types to separate target groups, such as bid requests to the bidding fleet, creative serving requests to the creative serving fleet, and tracking calls to the analytics fleet. 

 [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) (NLB) is optimized for TCP traffic and supports millions of requests per second at ultra-low latency. For RTB bid traffic between SSPs and DSPs where the request pattern is TCP and HTTPS at high QPS, NLB provides the lowest processing overhead. For workloads where RTB Fabric is deployed, NLB can be replaced entirely by the fabric's built-in load balancing. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select the load balancer type and routing algorithm for each workload:** Use ALB with path-based routing to direct different advertising request types (bid requests, creative serving, tracking) to separate target groups. Use NLB for high-QPS RTB bid traffic where you need millions of requests per second at ultra-low latency. Configure routing algorithm per target group (round-robin for equal-cost requests, LOR for variable-cost ML inference endpoints). 

1.  **Configure content-based routing for advertising request types:** Create ALB listener rules that match on request path or headers to route bid requests to bidding compute, creative asset requests to creative serving compute, and tracking beacon calls to analytics compute. This separates high-volume low-value tracking traffic from latency-sensitive bid evaluation. 

1.  **Offload TLS termination to the load balancer:** Configure HTTPS listeners on your load balancers and forward decrypted traffic to backend instances over the private VPC network using HTTP. Use [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) to manage TLS certificates with automatic renewal. For high-QPS RTB workloads, measure the CPU reduction on bid evaluation instances after enabling load balancer TLS offload. The savings compound at advertising-scale request volumes. 

1.  **Configure health checks appropriate to your advertising workload:** For bid evaluation targets, configure health checks that validate full auction engine responsiveness (not just container liveness). Set check intervals and thresholds that detect genuine failures quickly without generating false positives from transient slowness: 10-second intervals, 2 consecutive failures to mark unhealthy, 3 consecutive successes to mark healthy again. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF05-BP05 Use a managed low-latency fabric for real-time bidding infrastructure](advperf05-bp05.md) 

 **Related documents:** 
+  [ELB Best Practices Guides](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/best-practices-elk.html) 

 **Related services:** 
+  [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) 