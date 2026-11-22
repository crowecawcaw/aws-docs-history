

# ADVPERF01-BP02 Use appropriate scaling to handle burst traffic with cost considerations

 Consider start-up latency and scaling needs to handle burst traffic across networking, compute, and storage. Advertising workloads face sudden, order-of-magnitude traffic spikes during live events, programmatic campaign launches, and peak dayparts. Your infrastructure must absorb these spikes without dropped connections or latency degradation. 

 **Desired outcome:** 
+  Your architecture handles sudden traffic spikes without degraded performance or dropped connections. 
+  Load balancers, compute clusters, and databases scale proactively and elastically, so burst events are absorbed gracefully. 
+  Network, compute, and storage layers are scaled in concert. A spike that grows compute must not be limited by an undersized load balancer or database. 
+  Auto scaling policies respond to advertising-specific metrics (QPS, queue depth, custom business metrics) in addition to generic CPU and memory utilization. 

 **Common anti-patterns:** 
+  Relying solely on reactive auto scaling without pre-warming load balancers, which drops connections or throttles during sudden traffic bursts before scaling catches up. 
+  Scaling compute independently from networking and storage, so a database can run out of IOPS while compute scales correctly. 
+  Using manual capacity management for EKS or ECS clusters that can't respond to unpredictable live-event traffic. 
+  Setting auto scaling target utilization too high (for example, 90% CPU), which leaves no headroom to absorb burst requests before a new instance becomes available. 

 **Benefits of establishing this best practice:** 
+  Proactive capacity planning across all three layers (network, compute, and storage) helps your system absorb burst traffic without manual intervention. 
+  Reduces the risk of cascading failures where one layer becomes a bottleneck that takes down the others. 
+  Gives your operations team predictable, observable scaling behavior rather than emergency firefighting during high-value advertising events. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising traffic isn't uniformly distributed. For example, real-time bidding volumes can spike 10x or more during prime-time slots, live sporting events, or major seasonal campaigns. The same infrastructure that handles steady-state traffic must absorb these bursts. A failed bid auction or dropped ad request during a high-profile event loses revenue. 

 The metric monitored by a scaling policy determines whether it can react in time. Processor utilization rises only after load has arrived. By the time the metric rises, the queue has already formed and requests are missing deadlines. Queue depth and arrival rate move first, so the trigger choice matters more than the threshold. 

 Even a leading signal can't keep pace with a step change, and advertising bursts arrive as step changes. While capacity becomes ready, requests are served by whatever was already provisioned. In an auction, that gap is lost revenue: bids can't queue for later, and one that misses its deadline has no residual value. Meet the largest and most valuable peaks with capacity arranged in advance, since those peaks are scheduled and bought against ahead of time. Reactive scaling is still the right mechanism for unpredicted variation. 

 Scaling behavior depends on the whole request path, and the tiers interact in ways their individual metrics don't reveal. Compute that scales correctly increases pressure on whatever sits behind it, so the constraint moves downstream. Entry-point capacity, connection tables, and address space are the usual surprises. They are managed elsewhere, they scale on different dimensions than compute, and they show up as unexplained latency, not as capacity errors. Data tiers throttle under overload, so a compute fleet that scaled perfectly can end up unproductive. 

 Reserved capacity and elastic capacity address different needs. Reservation removes the scaling ramp for demand you can predict in advance. You pay for it regardless of whether the demand arrives. Elasticity covers demand you can't predict, at the cost of the scaling lag. Use both, and then size against which peaks are known, and how much revenue is at risk during the interval before elastic capacity arrives. 

 Because the tiers interact under load, you can't validate a scaling design by reasoning about each one on its own. Load-test the whole path together. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Size load balancers based on your traffic profile:** Establish baseline measurements for three key parameters: total number of long-lived connections, new TCP/TLS connections per second, and data transfer volume in GB/s. Use these values to size your NLB and ALB capacity. For events where a traffic spike is known in advance, configure LCU reservation to set a guaranteed minimum capacity so the load balancer doesn't need to ramp up from a cold state. 

1.  **Configure multi-dimensional auto scaling for Amazon EKS workloads:** Layer your scaling approach using Karpenter or Cluster Autoscaler for node-level scaling, HPA for pod-level scaling based on resource demand, and KEDA to extend scaling to external signals such as SQS queue depth or custom bid-volume metrics published to [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/). Set target CPU utilization no higher than 65% to leave headroom for burst absorption before new nodes are available. 

1.  **Enable Aurora storage auto scaling:** For Aurora-backed advertising databases, enable storage auto scaling to expand capacity as bid logs, user profiles, and campaign data accumulate during high-traffic periods. Set the maximum storage limit to limit runaway growth during incidents, and configure CloudWatch alarms on FreeStorageSpace to alert before storage becomes constrained. 

1.  **Implement predictive scaling for known advertising events:** Use [AWS Application Auto Scaling](https://aws.amazon.com/autoscaling/) predictive scaling policies for ECS services and EC2 Auto Scaling groups. Train policies on historical advertising traffic patterns (previous Super Bowls, previous Q4 peaks) to proactively add capacity before the event begins rather than reactively after CPU rises. For campaigns with a defined start time, combine predictive scaling with a scheduled scaling action to pre-scale immediately before launch. 

1.  **Validate burst capacity with load testing:** Before any major advertising event, run load tests at five times the expected baseline RTB traffic to validate that all three layers (load balancer, compute, and database) scale without bottlenecks. Use [AWS Fault Injection Service](https://aws.amazon.com/fis/) to simulate Availability Zone-level failures during burst conditions to validate that auto scaling continues to function correctly under degraded conditions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP03 Consider low-latency node provisioning tools to improve startup and scaling time](advperf02-bp03.md) 
+  [ADVREL03-BP04 Reserve appropriate capacity of services in the supported regions](advrel03-bp04.md) 

 **Related documents:** 
+  [Load Balancer Capacity Unit Reservation for Application and Network Load Balancers](https://aws.amazon.com/blogs/networking-and-content-delivery/using-load-balancer-capacity-unit-reservation-to-prepare-for-sharp-increases-in-traffic/) 
+  [Autoscaling Amazon EKS services based on custom Prometheus metrics using CloudWatch Container Insights](https://aws.amazon.com/blogs/containers/autoscaling-amazon-eks-services-based-on-custom-prometheus-metrics-using-cloudwatch-container-insights/) 
+  [Proactive autoscaling of Kubernetes workloads with KEDA](https://aws.amazon.com/blogs/mt/proactive-autoscaling-kubernetes-workloads-keda-metrics-ingested-into-aws-amp/) 

 **Related services:** 
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) 
+  [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) 
+  [Amazon Aurora](https://aws.amazon.com/rds/aurora/) 