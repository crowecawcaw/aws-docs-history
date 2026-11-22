

# REL11-BP05 Use static stability to prevent bimodal behavior

 A statically stable workload behaves the same way whether or not a failure is occurring. Bimodal behavior is the opposite: the workload acts one way in normal operation and a different way during a failure, usually because it tries to acquire new resources at the moment of impairment. Design workloads to operate in a single mode so their behavior stays predictable when a component fails. 

 **Desired outcome:** 
+  Your workload behaves the same during normal operation and during a failure. 
+  Capacity to absorb a failure is provisioned before the failure, not requested during it. 
+  Static stability is evaluated across compute, databases, storage, and routing, not compute alone. 
+  Recovery shifts load to resources that already exist rather than creating new ones. 

 **Common anti-patterns:** 
+  Teams assume resources can always be provisioned, regardless of the scope of a failure. 
+  Workloads try to acquire resources dynamically during a failure. 
+  Teams provision adequate cross-zone or cross-Region capacity only after a failure occurs. 
+  Teams apply static stability to compute resources and overlook databases, storage, and routing. 

 **Benefits of establishing this best practice:** 
+  Behavior stays predictable during both normal and failure events. 
+  Recovery does not depend on spare capacity or a control plane being available mid-incident. 
+  Negative feedback loops that amplify a small fault into a larger failure are avoided. 
+  Resilience decisions are made deliberately against cost, rather than discovered during an event. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Bimodal behavior is dangerous because it hides a dependency that only appears under stress. A workload that runs comfortably every day but needs to launch new instances the instant an Availability Zone fails has a failure-mode dependency on a working control plane and available spare capacity. Both dependencies are least certain during a large event. Static stability removes that dependency by holding the capacity in advance. Figure 1 shows the pattern for compute. Enough instances are provisioned in each Availability Zone that the healthy zones can carry the full load if one zone is lost. Recovery only requires routing traffic away from the impaired zone. 

![Architecture diagram showing enough compute instances provisioned in each Availability Zone that the healthy zones can carry full load if one zone fails.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/static-stability.png)

*Static stability for compute with pre-provisioned capacity across Availability Zones*


 Holding idle capacity to survive a zone or Region loss is more expensive than provisioning to demand and adding capacity when a failure occurs. The cheaper approach is also the less reliable one, because it leans on the operations most likely to be impaired at the worst time. Weigh the two approaches against the business value of keeping the workload available in every failure case. One way to reduce the cost is to spread across more zones. With more zones sharing the load, the extra capacity each zone must reserve for static stability shrinks. 

 Bimodal behavior also appears in software. Consider a network timeout that prompts a component to refresh the entire configuration state of the system. That refresh adds sudden load to another component, which might then fail, which triggers more refreshes, forming a negative feedback loop that degrades the whole workload. A statically stable design avoids this by doing constant work. It refreshes state on a fixed cadence regardless of failures, and when a call fails it uses the last cached value and raises an alarm. Letting clients bypass a cache during failures is the same trap in another form. Removing the cache changes the load profile when the workload can least absorb it. 

 Databases, storage, and load balancing each have their own failure-mode behaviors to evaluate. Read replica fleets must carry the read load after losing a replica or a primary. Single-zone storage classes are not statically stable, because losing that one zone removes access to the data. Assess which workloads are critical enough to justify these designs, then review each component. A statically stable compute tier in front of a single-zone data store still fails when that zone is lost. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Provision single-mode capacity across locations:** Build systems that operate in one mode by provisioning enough capacity in each Availability Zone or Region to carry the full load if one location is lost. Route traffic to healthy resources using [cross-Region DNS routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html), [Amazon S3 Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequestRouting.html), [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/), or [Amazon Application Recovery Controller](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html). 

1.  **Size read replicas for loss:** Configure [database read replicas](https://aws.amazon.com/rds/features/multi-az/) so the replicas remaining after the loss of a primary or a single replica still meet the read demand in each affected zone or Region. 

1.  **Use statically stable storage for critical data:** Store critical data in a storage class that survives the loss of an Availability Zone. Treat [Amazon S3 One Zone-IA](https://aws.amazon.com/about-aws/) as not statically stable, because losing that zone removes access to the stored data. 

1.  **Verify load balancer zone coverage:** Review load balancer configuration, because [cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) is sometimes disabled by design for latency, cost, or security. Where a design serves a specific zone, spread the workload across zones so a single-zone impairment does not remove the service. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL11-BP04 Rely on the data plane and not the control plane during recovery](rel11-bp04.md) 
+  [REL11-BP02 Fail over to healthy resources](rel11-bp02.md) 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 
+  [REL04-BP03 Do constant work](rel04-bp03.md) 

 **Related documents:** 
+  [Static stability using Availability Zones](https://builder.aws.com/content/3K9SiqiJ369TGkkGzqPM95BuYWI/static-stability-using-availability-zones) 
+  [Minimizing Dependencies in a Disaster Recovery Plan](https://aws.amazon.com/blogs/architecture/minimizing-dependencies-in-a-disaster-recovery-plan/) 
+  [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) 
+  [Amazon RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/) 
+  [Multi-Region Access Point request routing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequestRouting.html) 
+  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) 
+  [What is ARC?](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) 
+  [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Global Resilient Apps: Guide to Multi-AZ/Region Architecture with ELB (NET311)](https://www.youtube.com/watch?v=_WFrt9ABrMM) 

 **Related examples:** 
+  [Guidance for Cross Region Failover & Graceful Failback on AWS](https://docs.aws.amazon.com/solutions/cross-region-failover-and-graceful-failback-on-aws/) 