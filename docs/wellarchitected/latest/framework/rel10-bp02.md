

# REL10-BP02 Automate recovery for components constrained to a single location

 Some components cannot run in more than one location. A licensing limit, a single-instance data store, or a legacy system may tie a component to one Availability Zone or one data center. When you cannot spread such a component across locations, resilience has to come from the ability to rebuild it quickly. Automating that rebuild keeps recovery within the time and data-loss limits the business has set. 

 **Desired outcome:** 
+  You can rebuild each single-location component automatically, within your defined recovery time and recovery point objectives. 
+  Infrastructure, application code, and data for these components are defined as code or replicated to durable storage, so nothing depends on manual reconstruction. 
+  Failed instances or tasks are detected and replaced without human intervention. 
+  You have tested the rebuild path and know how long recovery actually takes. 

 **Common anti-patterns:** 
+  Teams run a single-location component with no automated way to recreate it after a failure. 
+  Recovery depends on manual steps captured only in tribal knowledge or an outdated document. 
+  Teams assume a component is multi-location by default without verifying whether it actually runs in more than one location. 
+  Teams never test the rebuild process, so its real recovery time stays unknown until an incident. 
+  Data for the constrained component lives only on the instance, so a failure loses it. 

 **Benefits of establishing this best practice:** 
+  Recovery time stays predictable because the rebuild runs automatically instead of relying on manual effort. 
+  A component tied to one location still meets its recovery objectives. 
+  Automatic detection and replacement of failed instances reduces downtime and operational load. 
+  Storing data on durable, replicated storage protects it from the loss of a single instance or zone. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A service may pin all its nodes to one Availability Zone for performance, a database engine may place a cluster in a single zone by design, or a legacy application may carry licensing terms that forbid running copies. When this constraint applies, resilience depends on your ability to recreate the component's infrastructure, redeploy its code, and restore its data fast enough to meet your recovery objectives. Automate this path, because manual rebuilds are too slow and error-prone. 

 Recovery patterns differ by whether the component holds state. Stateless components can be replaced outright: if an instance fails, launch a fresh one from the same definition and it resumes work. Automatic scaling handles this self-healing case because a replacement is functionally identical to what it replaced. Stateful components are harder because the replacement must recover the data the failed instance held. Move state off the instance and onto durable, replicated storage so the rebuild can reach the data. 

 Even a single-location constraint usually allows some redundancy. A cluster confined to one zone can still run multiple nodes within that zone, which protects against the loss of any single node. Its data can be stored in a service that replicates across zones or Regions independently of the compute, so the data survives even when the compute does not. Look for these options before you treat a component as a single point of failure, because reducing the failure domain is cheaper than rebuilding after every fault. 

 Confirm the constraint is real before you invest in rebuild automation. A managed AWS service may not be multi-location by default: a managed database might default to a single Availability Zone, or a service that supports multi-AZ may not have it enabled. Check the deployment configuration of every component in the workload and confirm which ones cannot run in more than one location. The answer determines whether you need this best practice or the multi-location deployment described in [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md). 

 A recovery process that has never run against a real failure is only a hypothesis. Its stated recovery time is a guess, and incidents routinely expose missing permissions, stale image references, or data that was never replicated. Treat the rebuild automation as production code and test it on a schedule to measure its recovery time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Confirm the constraint and reduce it where possible:** Verify that the component truly must run in a single location, and provision redundancy by other means where you can. For a cluster pinned to one zone, run [multiple nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha-launch.html) within that zone to survive single-node failures. For a database that defaults to a single Availability Zone, check whether the engine supports multi-AZ deployment (for example, [Amazon RDS Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)). This may eliminate the single-location constraint entirely. 

1.  **Externalize state and data to durable storage:** Move the component's data off the instance and onto storage that replicates across zones or Regions independently of the compute. For example, store cluster data in Amazon S3 through [EMR File System (EMRFS)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-fs.html) so it persists beyond the life of any single node. For database workloads, enable [automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) or cross-Region read replicas so data survives the loss of the primary instance. 

1.  **Define the rebuild as code:** Capture the component's infrastructure and deployment in infrastructure as code (for example, [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html)) so you can recreate it consistently. This removes the manual reconstruction that makes recovery slow and unrepeatable. 

1.  **Implement self-healing for stateless compute:** Use [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) to replace failed instances that need no fixed identity. For instances that require a fixed IP address or metadata, use [automatic recovery of Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html), and use [EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) or [Amazon ECS events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwe_events.html) to drive custom healing where neither applies. 

1.  **Protect stateful single-location workloads with continuous replication:** For server-based stateful workloads that cannot be made multi-location, use [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) to replicate at the block level to a staging area, so you can recover to another zone or Region. 

1.  **Test the recovery path on a schedule:** Run the automated rebuild against a simulated failure and measure the actual recovery time and data loss. Compare the results to your objectives, and fix any gaps the test exposes before they surface in a real incident. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) 
+  [REL10-BP03 Use bulkhead architectures to limit scope of impact](rel10-bp03.md) 
+  [REL11-BP03 Automate healing on all layers](rel11-bp03.md) 
+  [REL13-BP05 Automate recovery](rel13-bp05.md) 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel13-bp02.md) 

 **Related documents:** 
+  [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) 
+  [Automatic instance recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) 
+  [Amazon ECS events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwe_events.html) 
+  [Automatically scale your Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) 
+  [Launch an Amazon EMR Cluster with multiple primary nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha-launch.html) 
+  [EMR File System (EMRFS)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-fs.html) 
+  [What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) 
+  [Configuring and managing a Multi-AZ deployment for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) 
+  [Introduction to backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) 
+  [What is CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) 
+  [What is the AWS CDK?](https://docs.aws.amazon.com/cdk/v2/guide/home.html) 

 **Related tools:** 
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) 
+  [Amazon ECS](https://aws.amazon.com/ecs/) 
+  [Amazon EMR](https://aws.amazon.com/emr/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [AWS CDK](https://aws.amazon.com/cdk/) 