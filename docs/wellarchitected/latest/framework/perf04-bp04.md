

# PERF04-BP04 Use load balancing to distribute traffic across multiple resources

 Distributing traffic across multiple resources lets a workload scale with demand and stay available when a single resource fails. A load balancer also offloads work such as encryption termination, which frees backend resources to serve requests. 

 **Desired outcome:** 
+  You distribute traffic across multiple resources so the workload scales with demand and tolerates the loss of any single resource. 
+  You choose the load balancer type from your workload's protocol, target, and placement requirements. 
+  You use load balancer features such as encryption offloading to reduce backend processing demands. 

 **Common anti-patterns:** 
+  Teams choose a load balancer type without considering workload requirements. 
+  Teams do not use load balancer features for performance optimization. 
+  Teams expose a workload directly to the internet without a load balancer. 
+  Teams route all internet traffic through a single existing load balancer. 
+  Teams use generic TCP load balancing and make each compute node handle SSL encryption. 

 **Benefits of establishing this best practice:** 
+  You handle varying application load across one or multiple Availability Zones. 
+  You improve availability because traffic shifts away from unhealthy targets automatically. 
+  You improve backend utilization by right-sizing targets behind the load balancer. 
+  You reduce backend processing by offloading encryption and connection management to the load balancer. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A load balancer is the entry point to your workload. It spreads requests across backend targets so no single instance becomes a hotspot. The backend fleet can grow or shrink without changing how clients reach the workload. Because every request passes through it, you can also move work off the backends, for example by terminating encryption once instead of on every node. 

 The load balancer type follows from your workload's characteristics. A Layer 7 load balancer routes HTTP and HTTPS on paths and headers. It suits application architectures built from microservices and containers. A Layer 4 load balancer works at the connection level for TCP and UDP. It handles millions of requests per second at low latency and absorbs sudden, volatile traffic. List your protocols, target types, application requirements such as long-running connections or stickiness, and placement needs before you choose. Changing the type later is disruptive. 

 The TLS handshake is CPU-intensive, and running it on every instance wastes capacity that could serve requests. When the load balancer terminates TLS, it frees backend CPU and centralizes certificate management. When compliance requires end-to-end encryption, re-encrypt to the backend. HTTP/2 and connection keep-alives bring similar gains, because the load balancer reuses connections more efficiently than backends do. 

 The routing algorithm matters when requests or targets are uneven. Routing to the target with the fewest outstanding requests balances load better than round robin when request cost varies. Turning cross-zone load balancing on spreads traffic across targets in all zones for higher availability and flexibility. Turning it off keeps traffic within a zone, which lowers latency and creates a zonal failure domain. Latency-sensitive workloads often prefer zonal isolation, while availability-sensitive workloads prefer cross-zone. 

 Integrate the load balancer with an automatic scaling group or a container orchestrator. Targets register and deregister as traffic rises and falls, so capacity tracks demand without manual steps. To cut latency for latency-sensitive workloads, place the load balancer closer to users through edge or local infrastructure. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define your load balancing requirements:** Capture traffic volume, availability and scalability targets, protocols, target types, and placement. These characteristics determine the type and configuration in the following steps. 

1.  **Choose the load balancer type:** Use [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) for HTTP and HTTPS workloads and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) for TCP and UDP workloads. For latency-sensitive or mobile-first applications that use HTTP/3, [Network Load Balancer passes QUIC traffic through to your targets](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-quic-protocol-support-for-network-load-balancer-accelerating-mobile-first-applications/), since Application Load Balancer does not terminate HTTP/3. [Amazon CloudFront](https://aws.amazon.com/cloudfront/) is the AWS service that terminates HTTP/3 at the edge. To combine both, place an [Application Load Balancer as a target of a Network Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/application-load-balancer-type-target-group-for-network-load-balancer/) when you need static IPs with header-based routing or to expose an HTTP workload through [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html). For a full comparison, see [Elastic Load Balancing features](https://aws.amazon.com/elasticloadbalancing/features/). 

1.  **Offload SSL/TLS where possible:** Configure HTTPS or TLS listeners on [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/) with [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/). Choose a [security policy](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html) that matches your performance and compliance needs, including the post-quantum key exchange policies for TLS. For a global audience, terminate TLS even closer to users at [Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-cloudfront-delivering-millisecond-performance-to-global-audiences/) edge locations in front of the load balancer, which removes the TLS handshake latency for users far from your origin Region and reuses persistent connections back to the load balancer. When a workload requires end-to-end encryption for compliance, re-encrypt to the targets rather than forwarding traffic in the clear. For related guidance, see [SEC09-BP02 Enforce encryption in transit](sec09-bp02.md). 

1.  **Select the routing algorithm (Application Load Balancer):** Choose from [three routing algorithms](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#modify-routing-algorithm). Use least outstanding requests when request complexity or target capacity varies. Use round robin when requests and targets are similar or you need equal distribution. Use weighted random with [anomaly mitigation](https://aws.amazon.com/blogs/networking-and-content-delivery/improving-availability-with-application-load-balancer-automatic-target-weights/) to automatically shift traffic away from targets showing gray failures or elevated latency. Network Load Balancer has no configurable routing algorithm. It [selects a target using a flow hash](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html#nlb-flow-hash-algorithm) of the connection's protocol, IP addresses, and ports (plus the TCP sequence number for TCP, or the QUIC Connection ID once established), which pins each flow to one target for its lifetime but cannot rebalance away from an unevenly loaded target. 

1.  **Decide whether session stickiness is worth its trade-off (Application Load Balancer):** Turning on sticky sessions can improve response time when a target caches session state locally, but it overrides the routing algorithm's load balancing decision and can concentrate load on specific targets. Only enable it when the measured caching benefit outweighs the risk of hot targets. 

1.  **Enforce per-target concurrency limits where needed (Application Load Balancer):** For workloads that can only process a handful of concurrent requests per target, such as GPU-bound inference, use [ALB Target Optimizer](https://aws.amazon.com/blogs/networking-and-content-delivery/drive-application-performance-with-application-load-balancer-target-optimizer/) so targets pull requests only when they have spare capacity, instead of relying on a routing algorithm's estimate of target load. 

1.  **Choose cross-zone or zonal isolation:** Turn cross-zone off for latency improvements and zonal failure domains. It is off by default on Network Load Balancer, and you can [turn it off per target group on Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/). Turn it on for higher availability. It is on by default on Application Load Balancer, and you can [turn it on per target group on Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/). 

1.  **Turn on HTTP keep-alives (Application Load Balancer):** Reuse backend connections until the keep-alive timeout expires to improve request and response time and reduce backend utilization. For Apache and NGINX settings, see [optimal backend settings for Elastic Load Balancing](https://repost.aws/knowledge-center/apache-backend-elb). 

1.  **Integrate with scaling and container services:** Connect the load balancer to automatic scaling groups so targets register and deregister with demand. For containers, use load balancing with [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) and [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html). The AWS Load Balancer Controller [supports the Kubernetes Gateway API](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-load-balancer-controller-adds-general-availability-support-for-kubernetes-gateway-api/), which standardizes routing, TLS, and cross-zone configuration that Ingress requires custom annotations for, reducing the chance of a misconfigured or unsupported setting degrading performance. For planned traffic spikes such as a launch or sale, request a [Load Balancer Capacity Unit (LCU) Reservation](https://aws.amazon.com/blogs/networking-and-content-delivery/using-load-balancer-capacity-unit-reservation-to-prepare-for-sharp-increases-in-traffic/) on Application, Network, or Gateway Load Balancer to pre-provision capacity ahead of the event rather than relying on automatic scaling to catch up. 

1.  **Turn on monitoring:** Turn on access logs for [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-access-logging.html) and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html). Watch request\_processing\_time and response\_processing\_time for Application Load Balancer, and connection\_time and tls\_handshake\_time for Network Load Balancer. Query logs with Amazon Athena for [Application Load Balancer](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs.html) and [Network Load Balancer](https://docs.aws.amazon.com/athena/latest/ug/networkloadbalancer-classic-logs.html), and alarm on metrics such as [TargetResponseTime](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF04-BP05 Choose network protocols to improve performance](perf04-bp05.md) 
+  [PERF04-BP01 Understand how networking impacts performance](perf04-bp01.md) 
+  [PERF04-BP06 Choose your workload's location based on network requirements](perf04-bp06.md) 
+  [SEC09-BP02 Enforce encryption in transit](sec09-bp02.md) 

 **Related documents:** 
+  [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) 
+  [Monitor your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html) 
+  [Monitor your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-monitoring.html) 
+  [Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html) 
+  [Scaling strategies for Elastic Load Balancing](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-strategies-for-elastic-load-balancing/) 
+  [Drive application performance with Application Load Balancer Target Optimizer](https://aws.amazon.com/blogs/networking-and-content-delivery/drive-application-performance-with-application-load-balancer-target-optimizer/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Deep dive: The evolution of AWS load balancing and new capabilities (NET334)](https://www.youtube.com/watch?v=0sg7KtCuhh0&feature=youtu.be) 
+  [AWS re:Invent 2024 - Optimizing ELB traffic distribution for high availability](https://www.youtube.com/watch?v=EhbFossuQhI) 

 **Related examples:** 
+  [How do I use Athena to analyze my Application Load Balancer access logs?](https://repost.aws/knowledge-center/athena-analyze-access-logs) 
+  [Analyze Application Load Balancer Logs with Amazon CloudWatch Logs](https://aws.amazon.com/blogs/mt/analyze-application-load-balancer-logs-with-amazon-cloudwatch-logs/) 
+  [Guidance for Network Connectivity on AWS](https://docs.aws.amazon.com/solutions/network-connectivity-on-aws/) 