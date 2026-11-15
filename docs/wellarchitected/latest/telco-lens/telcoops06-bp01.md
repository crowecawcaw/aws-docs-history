

# TELCOOPS06-BP01 Implement proactive capacity reservation and diversified scaling strategies
<a name="telcoops06-bp01"></a>

 Telco network functions often run on large instance types with limited availability in any single Availability Zone. They can't gracefully degrade when they fail to scale. A capacity shortage that blocks scale-out degrades service for subscribers. This best practice combines reservations, instance diversification, and predictive scaling so capacity is available when needed. 

 **Desired outcome:** 
+  Capacity reservations for mission-critical workloads that must scale on demand without risk of an insufficient-capacity error. 
+  Scaling configurations that use multiple instance types and sizes to maximize the probability of successful provisioning. 
+  Predictive scaling policies based on historical traffic patterns that pre-provision capacity before demand peaks. 

 **Common anti-patterns:** 
+  Relying on a single large instance type for all CNF deployments without fallback options. 
+  Not using On-Demand Capacity Reservations for workloads with strict availability commitments. 
+  Scaling reactively only after traffic spikes occur, which causes provisioning delays during peak demand. 
+  Not testing scale-out regularly, so capacity availability in the target Availability Zones is never validated. 

 **Benefits of establishing this best practice:** 
+  Critical network functions can scale without being blocked by capacity constraints, which helps protect service continuity. 
+  Instance-type diversification means a shortage in one instance family doesn't prevent scaling entirely. 
+  Capacity reservations provide guaranteed access to compute for baseline and failover needs. 
+  Combining reservations with predictive scaling avoids over-provisioning during off-peak periods, which controls cost. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Capacity assurance mechanisms have different costs and address different needs. On-Demand Capacity Reservations (ODCRs) guarantee that specific instance types are available in specific Availability Zones. A mission-critical function with a strict recovery-time objective requires that guarantee during failover or burst. The tradeoff is that an ODCR incurs charges whether the instance runs or not. Use ODCRs on workloads where the cost of unavailability exceeds the reservation cost. 

 Beyond the reserved baseline, elastic scaling needs breadth. A scaling configuration bound to one instance type inherits that type's scarcity. Diversify across several instance families that can each run the workload to eliminate that single point of capacity failure. For Kubernetes-based CNFs, use a provisioner such as Karpenter. It can select from multiple instance families to satisfy the same pod resource requirements and consolidate as demand changes. Choose instance types that meet the function's network and compute requirements, since unsuitable types fail to provision. 

 Reactive scaling means that your capacity lags behind your demand. Subscriber traffic in a telco network has structure visible in history: daily peaks, event-driven spikes, and seasonal patterns. Predictive scaling pre-provisions capacity against that structure. This removes the provisioning delay reactive autoscaling can't avoid. Validate all three mechanisms with a scale-out test in the target Availability Zones. Without that test, a reservation, a diversification list, and a predictive policy are assumptions. 

### Implementation steps
<a name="implementation-steps"></a>
+  Identify capacity-critical workloads: classify CNF deployments by their tolerance for provisioning delay. Workloads with sub-minute recovery-time objectives or regulatory availability mandates are candidates for capacity reservations. 
+  Establish On-Demand Capacity Reservations in the target Availability Zones for the instance types and quantities needed to handle failover or burst, and review them quarterly against growth projections. 
+  Diversify instance types in scaling policies: define multiple instance types per workload in Amazon EC2 Auto Scaling mixed instance policies or Karpenter NodePools, prioritizing by cost-performance while verifying every candidate meets network and compute requirements. 
+  Implement predictive scaling: analyze historical traffic patterns and configure predictive scaling policies that pre-provision capacity ahead of anticipated demand. 
+  Validate scale-out regularly: schedule periodic scale-out tests during maintenance windows to confirm that target Availability Zones have sufficient capacity and that the diversification strategy works as expected. 
+  Monitor capacity and alarm early: configure Amazon CloudWatch alarms on insufficient-capacity and provisioning-failure events so constraints are detected before they impact service. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [Amazon EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) 
+  [Amazon EKS (Elastic Kubernetes Service)](https://aws.amazon.com/pm/eks/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 