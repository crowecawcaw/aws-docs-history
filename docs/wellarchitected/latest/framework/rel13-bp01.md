

# REL13-BP01 Define recovery objectives for downtime and data loss

 Failures interrupt service and can leave data lost, stale, or inconsistent. Two objectives set the target for how fast you recover and how much data you can afford to lose: a recovery time objective (RTO) and a recovery point objective (RPO). Define both for every workload, based on business impact. 

 **Desired outcome:** 
+  Every workload has an assigned RTO and RPO derived from business impact and technical constraints. 
+  Your recovery objectives are validated against regulatory, contractual, and compliance requirements. 
+  Your objectives are consistent with the recovery capabilities of the workloads you depend on. 
+  Business and technical stakeholders agree on each objective and revisit it as the workload changes. 

 **Common anti-patterns:** 
+  Teams set no recovery objectives, or pick arbitrary values with no link to business impact. 
+  Objectives are too lenient and fail to meet what the business actually requires. 
+  Objectives are more stringent than the business needs, which forces costlier and more complex recovery than the workload warrants. 
+  Teams choose targets such as zero downtime or zero data loss that the workload configuration cannot achieve. 
+  A workload's objectives conflict with the recovery capabilities of a dependency. 
+  Teams overlook regulatory and compliance obligations when setting objectives. 

 **Benefits of establishing this best practice:** 
+  Recovery goals are clear and measurable, so disaster recovery plans have a concrete target. 
+  Recovery spending matches business value because objectives reflect real impact, not guesswork. 
+  Recovery designs stay achievable because objectives account for dependency capabilities and technical limits. 
+  Compliance risk drops because objectives incorporate regulatory and contractual obligations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 RTO is the maximum acceptable time between service interruption and restoration. RPO is the maximum acceptable data loss, measured as the time between the last recoverable data point and the failure. A workload can tolerate a long RTO but a short RPO, or the reverse, so treat the two independently, as the architecture that meets one does not automatically meet the other. 

 Impact rarely grows in a straight line with downtime. A workload might absorb an hour of downtime with little consequence, then cross a threshold where lost revenue, missed contractual commitments, or eroded customer trust escalate sharply. Before you fix a number, map financial, reputational, operational, and regulatory impact. 

 Most organizations group workloads into tiers of criticality. Tiers such as critical, high, medium, and low each carry a target RTO and RPO. The following figure shows an example tiering matrix. Assign each workload to the tier that matches its impact profile, then adjust where a specific workload justifies it. 

![Matrix showing an example workload tiering by criticality — critical, high, medium, and low — with a target RTO and RPO for each tier.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/disaster-recovery-matrix.png)

*Example workload tiering matrix for RTO and RPO*


 Objectives of zero downtime or zero data loss are often unachievable and always expensive. Anchor each number to a demonstrated impact so the cost of meeting it is justified. 

 A workload cannot recover faster than the downstream dependencies it relies on, so its RTO must be achievable given their recovery capabilities. Upstream workloads that depend on yours can force you to a more stringent target than your own analysis suggests. Where data can be regenerated from another source, known as *derived data*, the RPO of those source systems governs how quickly you can rebuild. Objectives can also tighten during peak periods such as sales events or product launches, so account for that variation. The following worksheet helps you capture this analysis consistently for each workload. 

![Worksheet template for capturing recovery objectives per workload, including RTO, RPO, downstream dependencies, upstream constraints, derived data sources, and peak-period variations.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/worksheet.png)

*Worksheet for capturing recovery objectives per workload*


### Implementation steps
<a name="implementation-steps"></a>

1.  **Engage business and technical stakeholders:** Identify the business owners and technical teams for each workload and bring them together. The business side supplies impact data, and the technical side supplies feasibility constraints. Both must agree on the final objectives. 

1.  **Define criticality tiers:** Create categories such as critical, high, medium, and low, and assign a target RTO and RPO to each. Base the tier definitions on your organization's disaster recovery strategy and any line-of-business requirements. 

1.  **Assess impact for each workload:** Quantify the impact of downtime and data loss across financial, reputational, operational, and regulatory dimensions. Work through the key questions, such as the maximum tolerable downtime, whether lost data can be recreated from other sources, and whether objectives change during peak events. Record the analysis so the assigned tier is defensible. 

1.  **Assign each workload to a tier:** Map every workload to the tier that matches its impact profile, which produces a candidate RTO and RPO. Check the candidates against the recovery capabilities of downstream dependencies and the demands of upstream consumers. 

1.  **Validate and adjust with stakeholders:** Review the candidate objectives with business and technical teams. Adjust where business stakeholders require tighter targets or where technical teams identify constraints that make a target unachievable. Confirm the final objectives meet regulatory and contractual obligations before recording them. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel13-bp02.md) 
+  [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel13-bp03.md) 
+  [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel09-bp04.md) 
+  [REL12-BP01 Use playbooks to investigate failures](rel12-bp01.md) 

 **Related documents:** 
+  [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) 
+  [Managing resiliency policies](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resiliency-policies.html) 
+  [Disaster Recovery Series](https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/) 
+  [APN Partner: partners that can help with disaster recovery](https://partners.amazonaws.com/search/partners?keyword=Disaster+Recovery) 
+  [AWS Marketplace: products that can be used for disaster recovery](https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Backup and disaster recovery strategies for increased resilience (COP319)](https://www.youtube.com/watch?v=Gd7U-zGeZEo) 
+  [Disaster Recovery of Workloads on AWS \| AWS Events](https://www.youtube.com/watch?v=cJZw5mrxryA) 