

# SEC01-BP04 Reduce security management scope

 Every control you operate yourself is a control you must configure, patch, monitor, and prove. Managed services shift some of that operational work to the provider, which reduces the surface you maintain and the compliance scope you own. Choosing where to hand off management is a deliberate trade-off between control, effort, and total cost of ownership. 

 **Desired outcome:** 
+  You weigh the scope of security management when selecting services for a workload. 
+  You include management overhead and maintenance in the total cost of ownership, not just the service price. 
+  You incorporate provider control and compliance documentation into your own control evaluation. 
+  Your service choices reflect a deliberate balance between the responsibility you keep and the responsibility you transfer. 

 **Common anti-patterns:** 
+  Teams deploy workloads without understanding the shared responsibility model for the services they choose. 
+  Databases and similar technologies run on virtual machines without evaluating a managed equivalent. 
+  Security management tasks are left out of the total cost of ownership when comparing self-hosted options to managed services. 
+  Teams assume a managed service removes all responsibility, and skip the configuration and update duties that remain theirs. 

 **Benefits of establishing this best practice:** 
+  Operational security burden drops, which lowers both risk and total cost of ownership. 
+  Time saved on undifferentiated tasks moves to work that adds more business value. 
+  Compliance scope narrows, because some control requirements shift to the provider. 
+  Fewer self-managed components mean fewer opportunities for misconfiguration. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) divides security work between you and AWS, and the split varies by service. Running software on [Amazon EC2](https://aws.amazon.com/ec2/) instances leaves you responsible for the largest share, including the operating system, patching, and configuration. Managed services move part of that work to AWS. Using [Amazon RDS](https://aws.amazon.com/rds/) for databases, [Amazon EKS](https://aws.amazon.com/eks/) or [Amazon ECS](https://aws.amazon.com/ecs/) for containers, or [serverless](https://aws.amazon.com/serverless/) options shifts responsibility for the underlying infrastructure to the provider. 

 Base the decision on *total cost of ownership*. The full cost of a self-managed option includes staff time to provision, patch, monitor, and audit. A managed service that costs more per hour is often cheaper once you include that operational effort. Perform the same comparison for new applications and migrations, where your choice (rehost, replatform, refactor, rebuild, or replace) determines how much management you keep. 

 Compliance scope moves with responsibility. When a managed service takes on a control, the audit scope for that control moves from you to AWS. Confirm with your compliance team that they can audit the aspects you still operate and accept the control statements in AWS audit reports. Provide the audit artifacts from [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html) to your auditors as evidence. Use the responsibility guidance there to design the controls your use cases still require. 

 You still choose when updates happen and evaluate their impact, from database engine versions in Amazon RDS to language runtimes for functions. Track these lifecycle events across your environments to plan updates. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify components a managed service can replace:** Review your workload and identify components that a managed service could operate instead. When migrating, factor the reduced management effort and risk into whether you rehost, replatform, refactor, rebuild, or replace, because early investment often pays off over the life of the workload. 

1.  **Adopt managed services for undifferentiated components:** Replace self-installed technologies with managed equivalents, such as running databases on Amazon RDS instead of provisioning and maintaining them yourself. 

1.  **Determine your residual controls:** Use the responsibility guidance in AWS Artifact to identify the security controls that remain yours after a service takes on part of the shared responsibility. 

1.  **Plan and track managed-service updates:** Track lifecycle and update events with [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html), and review [planned lifecycle events](https://docs.aws.amazon.com/health/latest/ug/aws-health-planned-lifecycle-events.html) so you control update timing and understand the impact on operations. 

1.  **Reassess scope as services evolve:** Keep an inventory of the technologies in use, and review new services and approaches on a cadence to find further opportunities to reduce management scope. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP05 Automate deployment of standard security controls](sec01-bp05.md) 
+  [PERF02-BP01 Select the best compute options for your workload](perf02-bp01.md) 

 **Related documents:** 
+  [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) 
+  [Downloading reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Manage resource lifecycle events at scale with AWS Health (SUP309)](https://www.youtube.com/watch?v=VoLLNL5j9NA) 