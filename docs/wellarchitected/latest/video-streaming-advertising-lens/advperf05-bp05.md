

# ADVPERF05-BP05 Use a managed low-latency fabric for real-time bidding infrastructure

 Traditional RTB setups use NLB or HA Proxy along with an ingress setup for request forwarding to application pods. [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) offloads client-side load balancing, TLS termination, and observability to the RTB Fabric Service itself. With Managed Endpoints, RTB Fabric routes bid traffic directly from the responder gateway to individual bidder pod IPs, bypassing the NLB, TLS termination layer, and ingress controller that traditional architectures place on the critical path. 

 **Desired outcome:** 
+  RTB bid traffic routes directly from the responder gateway to individual bidder pod IPs, bypassing the load balancer and ingress controller that traditional NLB-based architectures require. 
+  Load distribution, service discovery, and observability are handled by RTB Fabric, removing the processing overhead that each additional infrastructure layer contributes to p99 bid response latency. 
+  Partner connectivity flows over a private, purpose-built network rather than the public internet. 

 **Common anti-patterns:** 
+  Routing RTB bid traffic over the public internet through a traditional NLB-based architecture that traverses an internet-facing NLB, a TLS termination layer, and an ingress controller. 
+  Maintaining a separate load balancer for bidder fleet traffic distribution when RTB Fabric's managed endpoints can handle load distribution directly, at the cost of extra infrastructure and an additional network hop. 

 **Benefits of establishing this best practice:** 
+  RTB Fabric managed endpoints consolidate client-side load balancing, TLS termination, and observability into the RTB Fabric service, removing the layers that traditional setups require on the bid path. 
+  Direct routing from the responder gateway to bidder pod IPs removes both the load balancer and ingress controller from the request path, reducing the number of network hops each bid request traverses. 
+  Replacing public internet routing with a private network removes internet congestion variability from your p99 latency profile. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Traditional RTB architectures route bid traffic from partner SSPs through a sequence of infrastructure layers: internet-facing NLB → TLS termination → ingress controller → bidder application pods. Each layer adds processing overhead and network transit time. On a private network with low baseline latency, these layers might contribute 2–5 ms to the total bid response time. On the public internet with variable routing, they add unpredictable overhead that can push tail latency beyond the bid deadline. 

 Removing a layer helps only when another component already performs its work. A load balancer in the bid path performs three functions: it discovers which backends exist, determines which are healthy, and distributes traffic across them. A connectivity layer that runs its own service discovery covers all three functions, which makes the load balancer redundant. When the replacement's discovery is narrower than what the load balancer provided, removing the load balancer obscures work instead of removing it. Confirm first which of the three functions the replacement actually covers. 

 Health determination is the function that most often fails this check, and it fails uniquely across deployment types. A discovery mechanism that reads a system's own readiness state inherits whatever that state means, so routing accuracy depends on how the readiness signal is configured rather than on the connectivity layer. A mechanism that enumerates instances in a scaling group might have its own health metrics, and those metrics might not extend to the other deployment type. This asymmetry determines where to look when traffic reaches an unready backend. Assuming the two deployment types behave the same way is how a fleet ends up routing to pods that are running but not serving. 

 The larger benefit is reduced variance. Removing layers lowers the median by a small and measurable amount. Removing public internet transit changes the distribution, because routing changes, congestion, and peering variability leave the path and the tail shortens. A bid is worthless once the deadline passes, so the tail determines revenue. 

 Decommissioning the old path is the risky step. Run both paths concurrently and confirm that the new one reaches the same set of healthy backends before removing anything, because a load balancer is quick to remove and slow to reinstate under live partner traffic. Anything else the removed layer provided, such as TLS handling, access logging, or a place to apply request policy, needs a new owner before it disappears. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable RTB Fabric Managed Endpoints for your bidder fleet:** Enable the Managed Endpoints feature on your RTB Fabric responder gateway. Select the deployment type: EKS Managed Endpoints for Kubernetes-based bidder fleets, or EC2 ASG Managed Endpoints for Auto Scaling Group-based fleets. Configure the EKS cluster credentials or ASG ARN that RTB Fabric will use for service discovery. 

1.  **Use EKS Managed Endpoints for real-time pod discovery:** With EKS Managed Endpoints configured, RTB Fabric reads the Kubernetes Endpoints object for your bidder Service, so it routes only to pods the readiness probe reports as ready. As the fleet scales, newly ready pods are picked up and terminating pods are dropped without ingress controller changes. Confirm the access role references the correct Service name and that the readiness probe actually reflects bid-serving capability, because RTB Fabric's own health-check metrics cover Auto Scaling group endpoints only and the readiness probe is the equivalent signal for EKS. 

1.  **Validate that bid traffic is routing directly to bidder pod IPs:** After enabling Managed Endpoints, confirm that traffic from the responder gateway goes directly to individual bidder pod IPs rather than to a load balancer VIP. Use VPC Flow Logs and RTB Fabric CloudWatch metrics to verify the routing path. Compare p99 bid response latency before and after enabling Managed Endpoints to quantify the latency improvement. 

1.  **Configure RTB Fabric partner links for private network connectivity:** Establish RTB Fabric links to each advertising partner (SSP or DSP). Both parties benefit from private network routing. SSPs benefit from lower request transmission latency, DSPs benefit from lower response transmission latency. Monitor per-link metrics in the AWSRTBFabric CloudWatch namespace for forwarding latency (in microseconds), request counts, and HTTP status code distribution. 

1.  **Decommission separate NLBs for RTB partner traffic after validation:** Once RTB Fabric Managed Endpoints is validated in production (confirmed routing path, measured latency improvement, stable error rates), remove the NLB and ingress controller layers that previously handled RTB partner traffic. Update infrastructure as code to remove these resources. This reduces both latency and the operational overhead of maintaining redundant load balancing infrastructure. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST05-BP01 Design fraud detection pipelines to minimize redundant processing and optimize inference costs](advcost05-bp01.md) 

 **Related documents:** 
+  [AWS RTB Fabric Managed Endpoints documentation](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/managed-endpoints.html) 
+  [Guidance for AWS RTB Fabric with Real-Time Bidding Workloads on AWS](https://aws.amazon.com/solutions/guidance/aws-rtb-fabric-with-real-time-bidding-workloads-on-aws/) 
+  [Monitoring RTB Fabric with Amazon CloudWatch](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch.html) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 