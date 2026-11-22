

# REL13-BP05 Automate recovery

 During an incident, manual steps invite mistakes and extend downtime. Automate recovery so it runs reliably and repeatably, observe it while it works, and maintain the ability to stop it if it goes wrong. 

 **Desired outcome:** 
+  Your recovery runs from documented, standardized, and tested automation rather than manual steps. 
+  Low-risk issues are corrected automatically without human intervention. 
+  You can invoke recovery quickly for serious incidents and observe its behavior as it runs. 
+  You can halt a recovery in progress if it behaves dangerously or fails. 

 **Common anti-patterns:** 
+  Recovery plans depend on components that are themselves failed or degraded during the incident. 
+  Recovery requires manual console work, which is slow and inconsistent under pressure. 
+  Automation initiates recovery in situations that carry a high risk of data loss or unavailability. 
+  Recovery automation has no abort mechanism, so a misbehaving procedure cannot be stopped. 

 **Benefits of establishing this best practice:** 
+  Recovery is more reliable, predictable, and consistent because it does not depend on manual execution. 
+  Tighter recovery time and recovery point objectives become achievable because automation runs faster than manual steps. 
+  Recovery is less likely to fail during an incident because the procedure has been tested. 
+  Human error is removed from the critical path of recovery. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Automated recovery removes the human bottleneck from the critical path, but automation requires judgment. Some faults are low-risk and well understood, and automating them is safe. Others risk data loss or making an incident worse, and automating them can escalate a contained incident. Decide which failures recover automatically and which require a human to begin. 

 Recovery automation must know what the workload needs to function. *Hard dependencies* are components the workload cannot run without and for which no substitute exists. *Soft dependencies* are ones it normally uses but can do without temporarily, through a substitute or [REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies](rel05-bp01.md). Classifying dependencies tells the automation what to restore first and what it can defer, and prevents a recovery from stalling on a component that was never essential. 

 A recovery procedure cannot depend on the failing site. If your automation calls services in the primary site or relies on its control plane, the same event that took down the workload can disable the recovery. Design recovery actions to run independently of the primary site, and prefer data plane operations, so redirecting traffic or promoting resources does not require a control plane that might be unavailable. 

 Automation can encounter unanticipated situations, and a recovery that goes wrong can cause new downtime and data loss. Provide an abort control, sometimes called an andon cord or a big red button, so operators can halt a dangerous recovery and take corrective steps. Pair the abort control with observability so operators can see whether to stop it. 

 Build recovery automation with infrastructure as code, so the recovery environment is reproducible and consistent with the source, and the procedures are version-controlled. For complex workflows, orchestrate steps with a service such as [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) or [AWS Step Functions](https://aws.amazon.com/step-functions/). Test the automation, refine it after each incident and drill, and keep it current as the workload and available services change. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify what to recover and how:** Review the workload's architecture, components, and dependencies, and categorize each dependency as hard or soft. Establish how to identify and recover missing or corrupted data, and define the steady state that confirms recovery is complete. Account for warm-up actions such as pre-populating caches, and for scenarios where the primary site and its control plane are unreachable. Use [ARC Region Switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html) as the orchestrated failover action, a single operation that redirects traffic with pre-flight checks and health validation, without manually changing DNS records. 

1.  **Build the automated recovery process:** Implement automated fault detection and failover for hands-free recovery of low-risk issues. Build dashboards with a service such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to show the progress and health of recovery as it runs, and include validation that recovery succeeded. Provide a mechanism to abort a recovery in progress. 

1.  **Provide fallback playbooks:** Create [REL12-BP01 Use playbooks to investigate failures](rel12-bp01.md) for faults that automation cannot recover from, and align them with your broader disaster recovery plan. Keep the playbooks available to the whole team and consistent with the automated paths they back up. 

1.  **Prepare the recovery site in advance:** Evaluate the state of the recovery site and deploy critical components ahead of an incident so recovery does not start from zero. Manage this readiness alongside your configuration drift controls, as described in [REL13-BP04 Manage configuration drift at the DR site or Region](rel13-bp04.md), so the site stays consistent with the primary. 

1.  **Define roles, conditions, and rollback:** Assign clear roles, responsibilities, and decision-making authority for recovery, and define the conditions that initiate the automated process. Plan how to revert the recovery and fall back to the primary site once it is safe. Test the recovery process regularly, as described in [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel13-bp03.md), so it stays reliable. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel13-bp02.md) 
+  [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel13-bp03.md) 
+  [REL13-BP04 Manage configuration drift at the DR site or Region](rel13-bp04.md) 
+  [REL07-BP01 Use automation when obtaining or scaling resources](rel07-bp01.md) 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 

 **Related documents:** 
+  [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [Orchestrate disaster recovery automation using Amazon Route 53 ARC and AWS Step Functions](https://aws.amazon.com/blogs/networking-and-content-delivery/orchestrate-disaster-recovery-automation-using-amazon-route-53-arc-and-aws-step-functions/) 
+  [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) 
+  [Using Elastic Disaster Recovery for recovery and failback](https://docs.aws.amazon.com/drs/latest/userguide/failback.html) 
+  [AWS Elastic Disaster Recovery resources](https://aws.amazon.com/disaster-recovery/resources/) 
+  [APN Partner: partners that can help with disaster recovery](https://partners.amazonaws.com/search/partners?keyword=Disaster+Recovery) 
+  [AWS Marketplace: products that can be used for disaster recovery](https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Disaster Recovery (DR) with AWS Elastic Disaster Recovery Service (COP356)](https://www.youtube.com/watch?v=IfVpaSe4H4k) 