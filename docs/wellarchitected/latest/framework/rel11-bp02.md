

# REL11-BP02 Fail over to healthy resources

 When one resource fails, healthy resources keep serving requests. Distribute load across independent resources, Availability Zones, or Regions so that any single impairment removes only part of your capacity. Then add mechanisms to detect the impairment and shift traffic away from it, so a localized fault does not spread to the whole workload. 

 **Desired outcome:** 
+  Your workload continues to serve requests when an individual resource, Availability Zone, or Region becomes impaired. 
+  Failover happens automatically where the service supports it, and through a rehearsed procedure where it does not. 
+  You have defined and measured the recovery time objective (RTO) and recovery point objective (RPO) for each component. 
+  Monitoring confirms that the failover target is healthy and tracks the progress of the failover and failback. 
+  A dampening period prevents the workload from failing back before the primary location is stable. 

 **Common anti-patterns:** 
+  Teams treat failure planning as an afterthought rather than part of design. 
+  Teams deploy without establishing RTO and RPO for each component. 
+  Monitoring is too thin to detect a failing resource before customers do. 
+  Failure detection is so aggressive that transient blips trigger unnecessary failover. 
+  Teams design failover but never test or validate it. 
+  Automation heals a resource but sends no notification that healing occurred. 
+  A workload fails back to the primary location before that location has stabilized. 

 **Benefits of establishing this best practice:** 
+  A localized failure reduces capacity rather than stopping the workload. 
+  Recovery is faster and more predictable because failover paths are defined and rehearsed. 
+  Measured RTO and RPO give the business a realistic view of resilience. 
+  Rehearsal surfaces broken automation and capacity gaps before a real event does. 
+  Dampening and notification prevent recovery actions from creating a second incident. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Spread work across independent copies so that losing one copy does not lose the service. The unit of isolation is the *failure domain*, the boundary within which a single fault is contained. An Availability Zone is a failure domain, a Region is a larger one, and a single resource is the smallest. The more failure domains you spread across, the smaller the fraction of capacity a fault removes. Plan capacity and failover together: if healthy domains cannot absorb the load shed by a failed domain, failover moves the problem. 

 The mechanism differs by scope. Many managed services span multiple Availability Zones by default and route around a failed zone with no action from you. Recovery within a Region is therefore often automatic. Data must be replicated across Regions, a replica must be promoted, and traffic must be redirected. Each step takes time and can fail. Region-level failover buys protection against a rare, large event at the cost of real operational complexity. Reserve it for workloads whose availability targets justify that cost. 

 Detection should react quickly enough to move traffic before customers feel the impairment, but not so quickly that a brief latency spike flaps traffic back and forth, which is often worse than the original blip. Failing back has the same hazard in reverse: returning to the primary location before it is truly stable can trigger a second incident. Build in a *dampening period* so the workload waits for sustained health before it fails back. Make sure every automated failover raises a notification to avoid obscuring faults that recur. 

 Quotas, scaling limits, stale configuration, and expired credentials in the recovery location routinely go unnoticed until they block a real failover. Rehearse failover and failback on a schedule, use fault injection to create the conditions that trigger them, and verify recovery-location capacity and quotas before you rely on them. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Design failover per component to meet RTO and RPO:** Isolate each architecture component and create a failover design that meets the recovery objectives for that component. Distribute load across resources, Availability Zones, or Regions according to the failure domains the component must survive. 

1.  **Provision and deploy with infrastructure as code:** Configure lower environments with every service that needs a failover plan, and deploy through infrastructure as code so the recovery configuration is repeatable and drift-free. Stand up a recovery site, such as a second Region, to implement and test the design, using temporary resources to limit cost where possible. 

1.  **Classify automation level and document objectives:** Determine which failover paths AWS automates, which your own automation handles, and which remain manual. Document and measure each service's RTO and RPO so gaps are visible. 

1.  **Route traffic to healthy locations:** Use traffic-management services to detect impairment and redirect requests. Within a Region, [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html) and [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) shift load across zones, and [zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/zonal-shift.html) evacuates traffic from an impaired AZ. Across Regions, use [ARC Region Switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html) to orchestrate cross-Region failover as a single operation with pre-flight checks and integrated CloudWatch health validation. For complex custom topologies requiring fine-grained control over individual routing decisions, use [Amazon Application Recovery Controller routing controls](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html). Amazon Route 53, Amazon CloudFront, and AWS Global Accelerator provide the underlying traffic-routing mechanisms. 

1.  **Write a failover playbook:** Capture every step required to fail over each resource, application, and service, including the health checks that confirm the target is ready. 

1.  **Write a failback playbook with a dampening period:** Capture the steps and timing to return to the primary location, and require sustained primary-location health before failback begins. 

1.  **Rehearse with simulations and fault injection:** Run the playbooks on a schedule, inject failures to trigger them, and confirm quotas, autoscaling levels, and running resources in the recovery location before you depend on them. Use [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to trigger zonal shift and AZ interruption scenarios that validate your failover paths under controlled conditions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL11-BP04 Rely on the data plane and not the control plane during recovery](rel11-bp04.md) 
+  [REL11-BP05 Use static stability to prevent bimodal behavior](rel11-bp05.md) 
+  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel13-bp02.md) 

 **Related documents:** 
+  [Establishing RPO and RTO Targets for Cloud Applications](https://aws.amazon.com/blogs/mt/establishing-rpo-and-rto-targets-for-cloud-applications/) 
+  [Building highly resilient applications using Amazon Route 53 Application Recovery Controller, Part 2: Multi-Region stack](https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-2-multi-region-stack) 
+  [Creating Disaster Recovery Mechanisms Using Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/) 
+  [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [Support cross-account for clusters in ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.failover-different-accounts.html) 
+  [Process Application Load Balancer requests with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html) 
+  [Configuring private image replication in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-settings-configure.html) 
+  [Replicating objects within and across Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) 
+  [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/) 
+  [New – Replication for Amazon Elastic File System (EFS)](https://aws.amazon.com/blogs/aws/new-replication-for-amazon-elastic-file-system-efs/) 
+  [Guidance for cross-Region failover and graceful failback on AWS](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cross-region-failover-and-graceful-failback-on-aws.pdf) 
+  [Deploying multi-region applications in AWS using AWS Global Accelerator](https://aws.amazon.com/blogs/networking-and-content-delivery/deploying-multi-region-applications-in-aws-using-aws-global-accelerator/) 
+  [Automating AWS Systems Manager Parameter Store Backup and Cross-Region Replication at Scale](https://builder.aws.com/content/320Yn9xIqlUjfPhh0Wwvas9Dymw/automating-aws-systems-manager-parameter-store-backup-and-cross-region-replication-at-scale) 

 **Related examples:** 
+  [Disaster recovery with Amazon Application Recovery Controller](https://catalog.us-east-1.prod.workshops.aws/workshops/4d9ab448-5083-4db7-bee8-85b58cd53158/en-US/) 
+  [Disaster Recovery on AWS :: Disaster Recovery on AWS](https://disaster-recovery.workshop.aws/en/) 
+  [Elastic Disaster Recovery on AWS workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/080af3a5-623d-4147-934d-c8d17daba346/en-US) 
+  [AWS Secrets Manager - Secrets Replication :: Disaster Recovery on AWS](https://disaster-recovery.workshop.aws/en/labs/basics/secrets-manager.html) 
+  [Amazon S3 Multi-Region Access Points failover workshop](https://catalog.workshops.aws/s3multiregionaccesspoints/en-US/0-setup/1-review-mrap) 
+  [Transferring file data across AWS Regions and accounts using AWS DataSync](https://aws.amazon.com/blogs/storage/transferring-file-data-across-aws-regions-and-accounts-using-aws-datasync/) 
+  [GitHub - aws-samples/sample-multi-region-resilient-microservice-on-aws](https://github.com/aws-samples/sample-multi-region-resilient-microservice-on-aws) 