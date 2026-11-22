

# REL01-BP06 Verify that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover

 A failover creates new resources before the old ones stop counting against your quota. If the quota has no room for that overlap, the replacement cannot start and the recovery fails. Keep a deliberate gap between your quota and your normal usage so a zonal, network, or Regional failover fits within the quota. 

 **Desired outcome:** 
+  Your quotas leave enough headroom to create replacement resources during a failover without reaching the quota. 
+  Your planning accounts for zone, network, and Regional failures when sizing that headroom. 
+  Your critical workloads are sized so a statically stable configuration fits within quota in every Region and Availability Zone. 
+  You track consumption growth and adjust the gap as usage rises. 

 **Common anti-patterns:** 
+  Teams set quotas to current needs and leave no room for a failover. 
+  Teams ignore static stability when calculating the peak quota a service requires. 
+  Teams forget that inaccessible resources still count against the quota until they are terminated. 
+  Teams overlook AWS service fault isolation boundaries and the abnormal usage patterns a failure can produce. 

 **Benefits of establishing this best practice:** 
+  Replacement resources can be created during a failure without exhausting the quota. 
+  Headroom sized for zone and Regional failures keeps recovery within existing quotas. 
+  Planning for static stability avoids a dependency on scaling up at the worst possible moment. 
+  Tracking growth keeps the gap adequate as the workload expands. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 When a resource becomes inaccessible, it does not immediately stop counting against your quota. An instance in a degraded Availability Zone, a resource behind a blocked network route, or capacity in an impaired Region can remain active and quota-charged even though you cannot reach it. Recovery means creating replacements, so for a period you hold both the stranded resources and their replacements against the same quota. A quota sized to steady-state usage has no room for that overlap, and the replacement launch fails exactly when you need it. 

 A disrupted VPC, an unreachable subnet, a degraded Availability Zone, blocked or rerouted network paths, an impaired Region, or a subset of resources lost within a Region can all leave active resources you cannot use. Failover decisions depend on the specific business impact, so plan capacity and quotas for the failover location before you shift. 

 A *statically stable* system does not depend on launching new resources or changing its configuration during a failure. It already holds the capacity it needs to survive the loss. In quota planning, this means reserving enough headroom in advance, because quota increases and new capacity are least reliable during a failure. For the most critical workloads, size resources so a statically stable configuration fits within quota in every Region and Availability Zone the design relies on. 

 Your availability requirement, expressed in nines, sets how much failure the design must absorb and drives the buffer you add above normal usage. Start with around 15 percent headroom above peak, adjusted for your deployment methodology, your static stability requirements, and your growth trend. For scheduled business events, use On-Demand Capacity Reservations to reserve failover capacity in advance so it is available when the event arrives. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Determine your reliability requirements:** Establish the availability target for the workload, expressed as a number of nines, and identify the fault scenarios it must survive, such as the loss of a component, an Availability Zone, or a Region. 

1.  **Establish current quotas and usage:** Record your current quotas and typical usage per account and Region, accounting for your deployment patterns and consumption growth. 

1.  **Model the failover overlap:** For each fault scenario, calculate the resources that remain active but inaccessible plus the replacements needed to recover, and size the required quota to cover both at once. Account for [AWS fault isolation boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) and your deployment methodology, such as canary, blue/green, or rolling. 

1.  **Add a headroom buffer:** Set each quota above peak usage by a buffer that covers the modeled overlap, for example around 15 percent, and include calculations for zonal and Regional static stability where they apply. 

1.  **Request increases with lead time:** Where the calculated headroom exceeds the current quota, submit an increase request and anticipate the approval wait rather than requesting during an event. 

1.  **Reserve capacity for critical schedules:** For critical workloads with known peak events, use [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) to hold the required capacity ahead of a potential failover. 

1.  **Monitor growth and revisit the gap:** Track consumption trends over time and adjust the buffer so the gap stays adequate as the workload grows. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL01-BP02 Manage service quotas across accounts and regions](rel01-bp02.md) 
+  [REL01-BP03 Accommodate fixed service quotas and constraints through architecture](rel01-bp03.md) 
+  [REL01-BP04 Monitor and manage quotas](rel01-bp04.md) 
+  [REL11-BP05 Use static stability to prevent bimodal behavior](rel11-bp05.md) 
+  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) 

 **Related documents:** 
+  [Availability and recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-availability-and-recovery-objectives.html) 
+  [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) 
+  [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) 
+  [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) 
+  [Amazon EC2 service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) 
+  [Reserve compute capacity with EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) 
+  [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) 
+  [Availability with redundancy](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-redundancy.html) 
+  [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/) 

 **Related videos:** 
+  [How do I manage my service quotas for my AWS services?](https://www.youtube.com/watch?v=Ddf5WG5I0Qo) 

 **Related tools:** 
+  [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/quota-monitor/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 