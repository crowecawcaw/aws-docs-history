

# OPS05-BP04 Assess operational readiness

 An operational readiness review (ORR) is a structured check that your team can operate a workload safely before it goes live and as it evolves. It uses a checklist built from best practices and past incidents to surface gaps while they are still cheap to fix. 

 **Desired outcome:** 
+  Your organization has an ORR checklist that captures its operational best practices. 
+  Your teams run an ORR before a workload launches to general availability. 
+  Your teams re-run the ORR periodically across a workload's lifecycle to catch drift. 
+  You feed lessons from past incidents back into the ORR checklist so failures do not recur. 

 **Common anti-patterns:** 
+  A team launches a workload without confirming it can operate it. 
+  Governance and security requirements are left out of launch certification. 
+  Workloads are never re-evaluated after launch. 
+  Workloads launch without the required operational procedures in place. 
+  The same root-cause failure appears in multiple workloads. 
+  Operational readiness checklist is treated as a manual document that is filled out from scratch at a single point before launch and then left stale as the workload evolves. 

 **Benefits of establishing this best practice:** 
+  Workloads launch with architecture, process, and management best practices in place. 
+  Lessons from service disruptions and other impacting events feed into the review process. 
+  Required procedures exist before a workload launches. 
+  Reviews continue across the workload lifecycle, not only at launch. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 An ORR has two parts: a process and a checklist. The process is a self-service review your team runs to certify its own workload against a set of requirements. Your organization must adopt the ORR and back it with an executive sponsor. Without that mandate, teams skip readiness reviews under deadline pressure. The [Operational Readiness Reviews (ORR) whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) describes the practice in detail. Read it before you build your own. 

 A strong checklist covers architecture, operational process, event management, and release quality. It also includes your security, governance, and compliance requirements. The items that matter most come from your own post-incident analysis. At Amazon, the Correction of Error process is a major source of ORR items. 

 Run the ORR before a workload reaches general availability. Re-run it periodically to catch drift from best practices as the workload changes. Many teams keep two variants: a fuller checklist for new launches and a lighter one for periodic reviews. As your cloud practice matures, encode recurring requirements as architecture defaults and automated controls, so those checks don't need manual review. 

 An ORR produces discoveries. A discovery with a mitigation already in place can pass, but without a mitigation, it becomes a backlog item to resolve before go-live. Services such as [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), and [AWS Control Tower controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) can detect many checklist items automatically. 

 Where possible, connect your readiness checklist to live signals such as alarm configuration, infrastructure-as-code definitions, and deployment pipelines, so draft answers stay current without being compiled by hand at each review. This lets you catch drift while a workload is still being built. Generated answers are suggestions, not verified facts. A person must accept, decline, or correct each one, and an unreviewed answer counts as unanswered. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Gather the key stakeholders:** Bring together representatives from security, operations, and development to define what operating this class of workload safely requires. Their combined view keeps the checklist from reflecting a single team's blind spots. 

1.  **Collect requirements from each stakeholder:** Ask each stakeholder to contribute at least one requirement, and cap the first iteration at about thirty items so the review stays usable. The [example ORR questions](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/appendix-b-example-orr-questions.html) in the ORR whitepaper are a useful starting set. 

1.  **Consolidate the requirements into a checklist:** Collect the requirements into a single shared checklist. You can use [custom lenses](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-custom.html) in the [AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/) to build the ORR and share it across your accounts and organization. 

1.  **Select a workload to review first:** Choose one workload to pilot the ORR, ideally one that is pre-launch or internal. A lower-stakes workload lets you refine the checklist before you apply it broadly. 

1.  **Run the checklist and triage discoveries:** Work through the checklist and record each discovery. A discovery is acceptable when a mitigation is already in place. Any discovery without a mitigation goes to the backlog and is resolved before launch. 

1.  **Iterate and expand the checklist over time:** Add new requirements and best practices as they emerge, and incorporate lessons from post-incident analysis. As your practice matures, encode recurring checklist items as automated controls using services such as [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), and [AWS Control Tower controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html). 

1.  **Automate checklist evidence from live signals:** Connect your checklist tooling to monitoring data, alarm configuration, and infrastructure or code repositories. Pre-populate items with draft answers and linked evidence, refresh them on a regular cadence, and route each draft through a human accept or decline step before it counts as satisfied. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS04-BP03 Develop and test rollout for consuming external dependencies](ops04-bp03.md) 
+  [OPS05-BP03 Create support plans for production workloads](ops05-bp03.md) 
+  [OPS07-BP01 Perform post-incident analysis](ops07-bp01.md) 
+  [SEC01-BP02 Identify and validate control objectives](sec01-bp02.md) 
+  [REL13-BP01 Define recovery objectives for downtime and data loss](rel13-bp01.md) 

 **Related documents:** 
+  [Operational Readiness Reviews (ORR) whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) 
+  [Controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) 

 **Related examples:** 
+  [Sample operational readiness review (ORR) lens](https://github.com/aws-samples/custom-lens-wa-hub/tree/main/ORR-Lens) 

 **Related services:** 
+  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 
+  [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) 
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 
+  [AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/tool.html) 