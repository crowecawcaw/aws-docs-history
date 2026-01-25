# PERF04-BP04 Use load

balancing to distribute traffic across multiple resources

Distribute traffic across multiple resources or services to allow your workload to take
advantage of the elasticity that the cloud provides. You can also use load balancing for
offloading encryption termination to improve performance, reliability and manage and route
traffic effectively.

**Common anti-patterns:**

- You don’t consider your workload requirements when choosing the load balancer type.
- You don’t leverage the load balancer features for performance optimization.
- The workload is exposed directly to the internet without a load balancer.
- You route all internet traffic through existing load balancers.
- You use generic TCP load balancing and making each compute node handle SSL encryption.

**Benefits of establishing this best practice:** A load balancer
handles the varying load of your application traffic in a single Availability Zone or across
multiple Availability Zones and enables high availability, automatic scaling, and better
utilization for your workload.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Load balancers act as the entry point for your workload, from which point they distribute
the traffic to your backend targets, such as compute instances or containers, to improve
utilization.

Choosing the right load balancer type is the first step to optimize your architecture.
Start by listing your workload characteristics, such as protocol (like TCP, HTTP, TLS, or
WebSockets), target type (like instances, containers, or serverless), application requirements
(like long running connections, user authentication, or stickiness), and placement (like
Region, Local Zone, Outpost, or zonal isolation).

AWS provides multiple models for your applications to use load balancing. [Application Load Balancer](../../../elasticloadbalancing/latest/application/introduction.md "../../../elasticloadbalancing/latest/application/introduction.md") is best suited for load balancing of HTTP and HTTPS traffic and provides
advanced request routing targeted at the delivery of modern application architectures,
including microservices and containers.

[Network Load Balancer](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md") is best suited for load balancing of TCP traffic where extreme performance is
required. It is capable of handling millions of requests per second while maintaining
ultra-low latencies, and it is optimized to handle sudden and volatile traffic patterns.

[Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/ "https://aws.amazon.com/elasticloadbalancing/") provides integrated
certificate management and SSL/TLS decryption, allowing you the flexibility to centrally
manage the SSL settings of the load balancer and offload CPU intensive work from your
workload.

After choosing the right load balancer, you can start leveraging its features to reduce
the amount of effort your backend has to do to serve the traffic.

For example, using both Application Load Balancer (ALB) and Network Load Balancer (NLB), you can perform SSL/TLS encryption
offloading, which is an opportunity to avoid the CPU-intensive TLS handshake from being
completed by your targets and also to improve certificate management.

When you configure SSL/TLS offloading in your load balancer, it becomes responsible for
the encryption of the traffic from and to clients while delivering the traffic unencrypted to
your backends, freeing up your backend resources and improving the response time for the
clients.

Application Load Balancer can also serve HTTP/2 traffic without needing to support it on your targets. This
simple decision can improve your application response time, as HTTP/2 uses TCP connections
more efficiently.

Your workload latency requirements should be considered when defining the architecture.
As an example, if you have a latency-sensitive application, you may decide to use Network Load Balancer, which
offers extremely low latencies. Alternatively, you may decide to bring your workload closer to
your customers by leveraging Application Load Balancer in [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/") or even [AWS Outposts](https://aws.amazon.com/outposts/rack/ "https://aws.amazon.com/outposts/rack/").

Another consideration for latency-sensitive workloads is cross-zone load balancing. With
cross-zone load balancing, each load balancer node distributes traffic across the registered
targets in all allowed Availability Zones.

Use Auto Scaling integrated with your load balancer. One of the key aspects of a performance
efficient system has to do with right-sizing your backend resources. To do this, you can
leverage load balancer integrations for backend target resources. Using the load balancer
integration with Auto Scaling groups, targets will be added or removed from the load balancer as
required in response to incoming traffic. Load balancers can also integrate with [Amazon ECS](../../../AmazonECS/latest/developerguide/service-load-balancing.md "../../../AmazonECS/latest/developerguide/service-load-balancing.md") and [Amazon EKS](../../../eks/latest/userguide/alb-ingress.md "../../../eks/latest/userguide/alb-ingress.md") for containerized workloads.

- [Amazon ECS - Service load
  balancing](../../../AmazonECS/latest/developerguide/service-load-balancing.md "../../../AmazonECS/latest/developerguide/service-load-balancing.md")
- [Application load
  balancing on Amazon EKS](../../../eks/latest/userguide/alb-ingress.md "../../../eks/latest/userguide/alb-ingress.md")
- [Network
  load balancing on Amazon EKS](../../../eks/latest/userguide/network-load-balancing.md "../../../eks/latest/userguide/network-load-balancing.md")

### Implementation steps

- Define your load balancing requirements including traffic volume, availability and
  application scalability.
- Choose the right load balancer type for your application.
  - Use Application Load Balancer for HTTP/HTTPS workloads.
  - Use Network Load Balancer for non-HTTP workloads that run on TCP or UDP.
  - Use a combination of both ([ALB as a target of NLB](https://aws.amazon.com/blogs/networking-and-content-delivery/application-load-balancer-type-target-group-for-network-load-balancer/ "https://aws.amazon.com/blogs/networking-and-content-delivery/application-load-balancer-type-target-group-for-network-load-balancer/")) if you want to leverage features of both
    products. For example, you can do this if you want to use the static IPs of NLB
    together with HTTP header based routing from ALB, or if you want to expose your HTTP
    workload to an [AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-share-your-services.md "../../../vpc/latest/privatelink/privatelink-share-your-services.md").
  - For a full comparison of load balancers, see [ELB product comparison](https://aws.amazon.com/elasticloadbalancing/features/ "https://aws.amazon.com/elasticloadbalancing/features/").

- Use SSL/TLS offloading if possible.
  - Configure HTTPS/TLS listeners with both [Application Load Balancer](../../../elasticloadbalancing/latest/application/create-https-listener.md "../../../elasticloadbalancing/latest/application/create-https-listener.md") and [Network Load Balancer](../../../elasticloadbalancing/latest/network/create-tls-listener.md "../../../elasticloadbalancing/latest/network/create-tls-listener.md") integrated with [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/").
  - Note that some workloads may require end-to-end encryption for compliance
    reasons. In this case, it is a requirement to allow encryption at the targets.
  - For security best practices, see [SEC09-BP02 Enforce encryption in transit](../security-pillar/sec_protect_data_transit_encrypt.md "../security-pillar/sec_protect_data_transit_encrypt.md").

- Select the right routing algorithm (only ALB).
  - The routing algorithm can make a difference in how well-used your backend
    targets are and therefore how they impact performance. For example, ALB
    provides [two options for routing algorithms](../../../elasticloadbalancing/latest/application/load-balancer-target-groups.md#modify-routing-algorithm "../../../elasticloadbalancing/latest/application/load-balancer-target-groups.md#modify-routing-algorithm"):
  - **Least outstanding requests:** Use to achieve a better
    load distribution to your backend targets for cases when the requests for your
    application vary in complexity or your targets vary in processing capability.
  - **Round robin:** Use when the requests and targets are
    similar, or if you need to distribute requests equally among targets.

- Consider cross-zone or zonal isolation.
  - Use cross-zone turned off (zonal isolation) for latency improvements and zonal
    failure domains. It is turned off by default in NLB and in [ALB you can
    turn it off per target group](../../../elasticloadbalancing/latest/application/disable-cross-zone.md "../../../elasticloadbalancing/latest/application/disable-cross-zone.md").
  - Use cross-zone turned on for increased availability and flexibility. By
    default, cross-zone is turned on for ALB and in [NLB you can
    turn it on per target group](../../../elasticloadbalancing/latest/network/target-group-cross-zone.md "../../../elasticloadbalancing/latest/network/target-group-cross-zone.md").

- Turn on HTTP keep-alives for your HTTP workloads (only ALB). With this feature, the
  load balancer can reuse backend connections until the keep-alive timeout expires,
  improving your HTTP request and response time and also reducing resource utilization on
  your backend targets. For detail on how to do this for Apache and Nginx, see [What are
  the optimal settings for using Apache or NGINX as a backend server for ELB?](https://aws.amazon.com/premiumsupport/knowledge-center/apache-backend-elb/ "https://aws.amazon.com/premiumsupport/knowledge-center/apache-backend-elb/")
- Turn on monitoring for your load balancer.
  - Turn on access logs for your [Application Load Balancer](../../../elasticloadbalancing/latest/application/enable-access-logging.md "../../../elasticloadbalancing/latest/application/enable-access-logging.md") and [Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/network/load-balancer-access-logs.md").
  - The main fields to consider for ALB
    are `request_processing_time`, `request_processing_time`,
    and `response_processing_time`.
  - The main fields to consider for NLB
    are `connection_time` and `tls_handshake_time`.
  - Be ready to query the logs when you need them. You can use Amazon Athena to query
    both [ALB
    logs](../../../athena/latest/ug/application-load-balancer-logs.md "../../../athena/latest/ug/application-load-balancer-logs.md") and [NLB logs](../../../athena/latest/ug/networkloadbalancer-classic-logs.md "../../../athena/latest/ug/networkloadbalancer-classic-logs.md").
  - Create alarms for performance related metrics such as [`TargetResponseTime` for ALB](../../../elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.md "../../../elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.md").

## Resources

**Related documents:**

- [ELB product
  comparison](https://aws.amazon.com/elasticloadbalancing/features/ "https://aws.amazon.com/elasticloadbalancing/features/")
- [AWS Global
  Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/")
- [Improving Performance and Reducing Cost Using Availability Zone Affinity](https://aws.amazon.com/blogs/architecture/improving-performance-and-reducing-cost-using-availability-zone-affinity/ "https://aws.amazon.com/blogs/architecture/improving-performance-and-reducing-cost-using-availability-zone-affinity/")
- [Step by step for Log Analysis with Amazon Athena](https://github.com/aws/elastic-load-balancing-tools/tree/master/amazon-athena-for-elb "https://github.com/aws/elastic-load-balancing-tools/tree/master/amazon-athena-for-elb")
- [Querying Application Load Balancer logs](../../../athena/latest/ug/application-load-balancer-logs.md "../../../athena/latest/ug/application-load-balancer-logs.md")
- [Monitor your
  Application Load Balancers](../../../elasticloadbalancing/latest/application/load-balancer-monitoring.md "../../../elasticloadbalancing/latest/application/load-balancer-monitoring.md")
- [Monitor your
  Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-monitoring.md "../../../elasticloadbalancing/latest/network/load-balancer-monitoring.md")
- [Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group](../../../autoscaling/ec2/userguide/autoscaling-load-balancer.md "../../../autoscaling/ec2/userguide/autoscaling-load-balancer.md")

**Related videos:**

- [AWS re:Invent 2023: What can
  networking do for your application?](https://www.youtube.com/watch?v=tUh26i8uY9Q "https://www.youtube.com/watch?v=tUh26i8uY9Q")
- [AWS re:Inforce 20: How to use
  Elastic Load Balancing to enhance your security posture at scale](https://www.youtube.com/watch?v=YhNc5VSzOGQ "https://www.youtube.com/watch?v=YhNc5VSzOGQ")
- [AWS re:Invent 2018: Elastic Load Balancing: Deep
  Dive and Best Practices](https://www.youtube.com/watch?v=VIgAT7vjol8 "https://www.youtube.com/watch?v=VIgAT7vjol8")
- [AWS re:Invent 2021 - How to
  choose the right load balancer for your AWS workloads](https://www.youtube.com/watch?v=p0YZBF03r5A "https://www.youtube.com/watch?v=p0YZBF03r5A")
- [AWS re:Invent 2019: Get the
  most from Elastic Load Balancing for different workloads](https://www.youtube.com/watch?v=HKh54BkaOK0 "https://www.youtube.com/watch?v=HKh54BkaOK0")

**Related examples:**

- [Gateway Load Balancer](https://catalog.workshops.aws/gwlb-networking/en-US "https://catalog.workshops.aws/gwlb-networking/en-US")
- [CDK and CloudFormation samples for Log Analysis with Amazon Athena](https://github.com/aws/elastic-load-balancing-tools/tree/master/log-analysis-elb-cdk-cf-template "https://github.com/aws/elastic-load-balancing-tools/tree/master/log-analysis-elb-cdk-cf-template")
