

# ADVSUS03-BP05 Remove dedicated load balancers from the bid path to reduce their idle energy draw
<a name="advsus03-bp05"></a>

 A managed bidding fabric can distribute traffic directly to healthy compute targets, using DNS-based routing for compute hosts and managed endpoints for container pods. This removes the need for dedicated load balancers and their ongoing energy draw. 

 **Desired outcome:** 
+  Real-time bidding (RTB) partner traffic is distributed to healthy compute targets using RTB Fabric's built-in routing (DNS-based for EC2 hosts, and the Managed Endpoints feature for EKS pods), and dedicated load balancers provisioned solely for that traffic are decommissioned. 
+  The workload provisions fewer persistent infrastructure components, reducing the idle energy footprint of the advertising request path. 
+  RTB partner traffic relies on RTB Fabric routing rather than dedicated Application Load Balancers (ALBs) or Network Load Balancers (NLBs). 
+  Load balancer resources that exist only to serve RTB traffic are identified and removed after routing is validated. 
+  Reductions in provisioned infrastructure are reflected in resource inventory and utilization metrics. 

 **Common anti-patterns:** 
+  Keeping dedicated load balancers running for RTB partner traffic after RTB Fabric can already distribute that traffic natively. 
+  Decommissioning load balancers before validating that RTB Fabric routing reaches all healthy hosts opens availability gaps. 
+  Provisioning load balancers sized for peak bid volume that sit largely idle between traffic spikes. 

 **Benefits of establishing this best practice:** 
+  Lower idle energy consumption by removing persistent load balancer infrastructure. 
+  Reduced operational and provisioned resource footprint for the RTB request path. 
+  Simpler architecture with fewer components to scale, patch, and monitor. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 A dedicated load balancer is a persistent tier. It holds provisioned capacity and draws energy even when no RTB partner traffic flows through it. In video-streaming advertising, bid traffic is bursty and partner-specific, so a load-balancer tier sized for peak volume is idle much of the time while still consuming its provisioned capacity. 

 RTB Fabric offers built-in load balancing. For EC2 hosts, it resolves partner requests to healthy targets through DNS-based routing. For EKS workloads, its Managed Endpoints feature (an opt-in capability for responder gateways) reads the Kubernetes Endpoints object for the named Service and routes traffic directly to those pod IPs. Kubernetes populates that object only with pods that pass their readiness probe, so RTB Fabric inherits pod health from Kubernetes rather than probing itself. The traffic-distribution function moves out of your provisioned discrete tier and into a capability the fabric already provides for the connectivity in place. Retiring the redundant tier produces the sustainability gain because it removes provisioned capacity rather than resizing it. Use built-in routing as the default for partner traffic, and reserve dedicated load balancers for workloads with requirements the fabric can't meet. 

 DNS resolution is subject to client-side caching and record time-to-live, so a target's health window can differ from what a load balancer's health checks enforce. If you retire a load balancer before confirming the fabric reaches every healthy host, partner requests can land on an incomplete target set, causing an availability gap. Account for any load balancer behavior the workload depends on, such as a specific routing or connection-handling capability, before treating that tier as redundant. 

 The clearest evidence is the change in provisioned resources, such as fewer persistent load balancers and the capacity they held. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Evaluate existing load balancers:** Identify Application Load Balancers (ALBs) and Network Load Balancers (NLBs) dedicated to RTB partner traffic and assess whether RTB Fabric's built-in load balancing can replace them. 

1.  **Validate RTB Fabric routing:** Confirm that RTB Fabric reaches the full set of healthy compute targets before treating any load balancer as redundant. For EC2 hosts, verify DNS-based routing distributes incoming RTB requests across healthy hosts within the responder's infrastructure. For EKS pods, verify the Managed Endpoints feature is enabled on the responder gateway and that the Kubernetes Endpoints object for your bidder Service lists the pods you expect, which means confirming the access role references the correct Service name and that the readiness probe is correct. RTB Fabric's own health-check metrics cover Auto Scaling group endpoints only, so for EKS the equivalent signal is Kubernetes pod readiness (Managed Endpoints is opt-in, so engage your AWS Solutions Architect before relying on it in production). 

1.  **Decommission redundant load balancers:** Remove the dedicated load balancers serving RTB partner traffic once RTB Fabric routing is validated as healthy and complete. 

1.  **Measure the sustainability gain:** Attribute the gain to concrete signals: the count of decommissioned Application Load Balancers and Network Load Balancers and the associated reduction in persistent provisioned capacity. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS03-BP01 Align partner connectivity capacity with bid activity to reduce idle energy draw](advsus03-bp01.md) 
+  [ADVSUS03-BP06 Continuously measure fabric utilization and retire unjustified capacity](advsus03-bp06.md) 

 **Related documents:** 
+  [AWS RTB Fabric features](https://aws.amazon.com/rtb-fabric/features/) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 