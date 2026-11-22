

# REL11-BP04 Rely on the data plane and not the control plane during recovery

 A control plane creates, changes, and describes resources, while a data plane carries the day-to-day traffic those resources serve. During a large impairment, when you most need recovery to work, control planes are more likely to be degraded and slower to respond. Design recovery to lean on data plane actions and to use as few control plane operations as possible. 

 **Desired outcome:** 
+  When a resource becomes impaired, the workload recovers by shifting traffic to healthy resources that already exist. 
+  Recovery paths use data plane operations and avoid creating or reconfiguring resources during the event. 
+  Any control plane actions a recovery needs are completed in advance, during steady state. 
+  You have identified, for each recovery runbook, which operations are control plane and which are data plane. 

 **Common anti-patterns:** 
+  Recovery depends on changing DNS records to reroute traffic. 
+  Recovery depends on control plane scaling to replace impaired components because capacity was not pre-provisioned. 
+  Remediation relies on extensive, multi-service control plane sequences for every category of impairment. 

 **Benefits of establishing this best practice:** 
+  Automated remediation succeeds more often because it avoids the operations most likely to be degraded. 
+  Recovery time and mean time to recovery drop because data plane operations are faster and more available. 
+  Recovery behavior is more predictable during exactly the large-scale events that matter most. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Control plane operations, such as launching an instance, creating a volume, or changing a DNS record, are complex orchestration. Launching a compute instance alone requires finding a host with capacity, allocating network interfaces, preparing storage, generating credentials, and applying security rules. Each step is a dependency that can fail. The more steps a recovery relies on, the more ways it can fail. Data plane operations, such as serving a request or answering a DNS query, are comparatively simple and run on infrastructure built for very high availability. 

 The Amazon Route 53 data plane that answers DNS queries and evaluates health checks is globally distributed and carries a [100% availability SLA](https://aws.amazon.com/route53/sla/). The Route 53 management APIs that create and change records run on a control plane concentrated in a single Region. That control plane is not covered by the SLA, because it is tuned for the strong consistency and durability that DNS management needs. In a rare event, the data plane can keep working while the control plane cannot. A recovery that changes DNS records depends on the weaker path, while a recovery that flips a pre-configured routing control uses the stronger one. 

 Static stability avoids the control plane during recovery. Provision failover capacity ahead of time. Recovery then shifts traffic on the data plane to resources that already exist, rather than creating them on the control plane during the event. For Amazon EC2, this means holding spare instances in the failover cluster instead of asking Auto Scaling to add them mid-incident. Where you must cap that spare capacity for cost reasons, throttle the total traffic reaching the reduced fleet so it degrades gracefully. The same reasoning maps onto Kubernetes: adding pods is a data plane action, while adding nodes is a control plane action. Over-provisioning nodes lets you scale pods without touching the control plane during an event. 

 Some control plane work is unavoidable, so schedule it for calm periods. Create functions, load balancers, API gateways, and tables before an event, as part of failover rehearsal. Reserve the event itself for data plane actions: routing, serving, and reading already-provisioned resources. 

 The path you use to invoke recovery is a dependency too. A failover that an operator triggers manually in a web console depends on the console being reachable and on someone being available to act. Both dependencies are least dependable during the large-scale event that prompted the failover. The console session itself can also carry Regional and control plane dependencies. Make the failover callable from a CLI or API so an automated runbook can trigger it directly. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory control plane actions in each recovery path:** For every workload that must be restored after a degradation, review the failover runbook, high-availability design, and auto-healing design. Identify each step that is a control plane action. See [static stability using Availability Zones](https://builder.aws.com/content/3K9SiqiJ369TGkkGzqPM95BuYWI/static-stability-using-availability-zones) for how AWS reasons about this distinction. 

1.  **Convert control plane actions to data plane equivalents:** Replace on-demand creation with pre-provisioned resources. Prefer pre-scaled Amazon EC2 capacity over Auto Scaling during an event, prefer adding Kubernetes pods over adding nodes, and use [over-provisioned nodes](https://www.eksworkshop.com/docs/fundamentals/compute/managed-node-groups/cluster-autoscaler/overprovisioning/) so pod scaling stays on the data plane. 

1.  **Use data plane routing to shift traffic:** For cross-Region failover, use [ARC Region Switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html) to orchestrate the full failover as a single data plane operation with pre-flight checks. It maintains the data plane advantage while simplifying orchestration into one API call. For custom multi-cell topologies or fine-grained per-service routing decisions, use [Amazon Application Recovery Controller routing controls](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html) directly. Use [Route 53 health checks](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/) to automate updates through the data plane. In all cases, avoid editing Route 53 records manually, as that introduces a control plane dependency on the recovery path. 

1.  **Pre-create resources during steady state:** Complete control plane work, such as creating functions, load balancers, API gateways, and tables, before an event and as part of failover rehearsal, so the event itself needs only data plane operations. 

1.  **Pre-provision a secondary Region for mission-critical workloads:** For the most critical workloads, run capacity such as Amazon EC2 Auto Scaling groups or Amazon EKS in a secondary Region ahead of time, and route traffic there, rather than creating that capacity during the event. 

1.  **Trigger failover from an API or CLI:** Make the trigger for your data plane failover path callable from a command-line interface or API, so an automated runbook or a single command can start it directly. This keeps the console and a human operator off the critical recovery path during the event. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL11-BP05 Use static stability to prevent bimodal behavior](rel11-bp05.md) 
+  [REL11-BP02 Fail over to healthy resources](rel11-bp02.md) 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 

 **Related documents:** 
+  [Static stability using Availability Zones](https://builder.aws.com/content/3K9SiqiJ369TGkkGzqPM95BuYWI/static-stability-using-availability-zones) 
+  [The Amazon Builders' Library: Avoiding overload in distributed systems by putting the smaller service in control](https://builder.aws.com/content/3EukISjbJAGNdrxjKaN6RG0wlHG/avoiding-overload-in-distributed-systems-by-putting-the-smaller-service-in-control) 
+  [DynamoDB API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.API.html) 
+  [What is ARC?](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) 
+  [Building highly resilient applications using Amazon Route 53 Application Recovery Controller, Part 1: Single-Region stack](https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-1-single-region-stack/) 
+  [Building highly resilient applications using Amazon Route 53 Application Recovery Controller, Part 2: Multi-Region stack](https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-2-multi-region-stack/) 
+  [Creating Disaster Recovery Mechanisms Using Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/) 
+  [Managing Kubernetes control plane events in Amazon EKS \| Containers](https://aws.amazon.com/blogs/containers/managing-kubernetes-control-plane-events-in-amazon-eks/) 
+  [APN Partners that help with fault tolerance automation](https://partners.amazonaws.com/search/partners?keyword=automation) 
+  [AWS Marketplace: products for fault tolerance](https://aws.amazon.com/marketplace/search/results?searchTerms=fault+tolerance) 

 **Related videos:** 
+  [Back to Basics: Static Stability Using a Circuit Breaker Pattern](https://www.youtube.com/watch?v=gy1RITZ7N7s) 
+  [AWS re:Invent 2022 - Building resilient multi-site workloads using AWS global services (SUP401)](https://www.youtube.com/watch?v=62ZQHTruBnk) 

 **Related examples:** 
+  [Introducing Amazon Route 53 Application Recovery Controller](https://aws.amazon.com/blogs/aws/amazon-route-53-application-recovery-controller/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Logging and monitoring in AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/security-logging-monitoring.html) 