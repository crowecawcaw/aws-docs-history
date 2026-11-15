

# ADVOPS01-BP02 Create RACI matrices that define the roles and responsibilities for each key advertising process
<a name="advops01-bp02"></a>

 Define stakeholder roles so key advertising processes run without handoff gaps. Use RACI (responsible, accountable, consulted, and informed) matrices to assign accountability and decisions for publisher-specific workloads (SGAI manifest pipelines, prebid adapter onboarding, and FAST channel scheduling) and for converged linear and digital operations. 

 **Desired outcome:** 
+  Publisher-specific RACI matrices clearly define accountability for Prebid adapter lifecycle management, SGAI manifest generation pipeline ownership, FAST channel scheduling and playout monitoring, and innovative ad format rendering operations. 
+  Each publisher theme has a designated operational owner accountable for yield outcomes, not just system health. 
+  For converged environments, a unified command structure bridges the linear broadcast NOC and digital ad operations with pre-defined cross-functional escalation paths. 

 **Common anti-patterns:** 
+  Assigning SGAI manifest generation ownership to infrastructure teams without ad operations input on SCTE-35 marker configuration, resulting in technically correct manifests that miss ad break opportunities. 
+  Leaving Prebid adapter onboarding accountability undefined between engineering and partner management teams, causing delays when new demand partners need to be integrated. 
+  Operating FAST channels without clear ownership boundaries between content scheduling, playout engineering, and ad operations functions. 
+  Maintaining separate RACI matrices for linear and digital teams, with no cross-functional ownership defined for converged failure scenarios. 

 **Benefits of establishing this best practice:** 
+  Clear accountability reduces coordination delays during incidents. 
+  Faster decision-making through pre-defined escalation paths. 
+  Reduced ownership gaps where issues that affect revenue fall between team boundaries. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Engineering owns infrastructure, ad operations owns yield outcomes, partner management owns DSP and SSP relationships, and content teams own programming schedules. Without explicit accountability mapping, cross-boundary incidents create coordination overhead. 

 For SGAI, the manifest generation pipeline exists at the intersection of media infrastructure (transcoding, packaging, and CDN) and advertising (ad break timing, SCTE-35 accuracy, and yield reporting). Neither team can own it independently, so the RACI must assign responsible parties from both domains with explicit coordination points. For Prebid Server, adapter onboarding involves engineering (container deployment and configuration), partner management (commercial agreements and technical integration specs), and ad operations (yield monitoring after launch). Without a documented process owner, adapters accumulate unmaintained. 

 Converged linear and digital operations need a Tier 2 cross-functional incident commander with authority to bridge the linear NOC and digital ad ops teams during incidents. This person needs pre-approved authority to escalate, request resources, and make trade-off decisions. The RACI must define this role and identify who holds it per shift. 

 Assign data stewards to specific advertising domains, such as bid management, user profile, campaign, and analytics. Each steward is accountable for the quality, retention, and access controls of their domain's data. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify all publisher-specific operational processes requiring RACI definition:** Catalog processes across adapter onboarding, manifest pipeline management, FAST channel scheduling, ad format rendering, and converged linear and digital campaign management. For each process, identify the teams involved: engineering, ad operations, partner management, content, and any external partners. 

1.  **Map each process to RACI roles:** For each identified process, define responsible (who does the work), accountable (who is answerable for the outcome), consulted (who provides input), and informed (who is notified of outcomes). For publisher yield processes, the accountable role must sit with whoever owns the revenue outcome, typically ad operations for processes that affect yield. 

1.  **Define handoff points and escalation triggers at team boundaries:** Document the specific conditions that trigger escalation from one team to another. For SGAI: if manifest error rates exceed X%, escalate from infrastructure to ad operations and initiate the joint runbook. For prebid: if a new adapter's win rate is below Y% after 48 hours, escalate from ad operations to engineering for technical review. Clear escalation criteria help teams avoid debating ownership during an incident. 

1.  **Define the cross-functional incident commander role for converged operations:** For organizations running both linear broadcast and digital ad serving, document a Tier 2 incident commander role with a 15-minute escalation authority. Define the conditions that activate this role (incidents affecting both linear and digital delivery simultaneously), the pre-approved actions this role can take without further approval, and the on-call rotation that covers this role. 

1.  **Publish RACI matrices and review quarterly:** Store RACI matrices in a shared operational wiki accessible to all relevant teams. Schedule quarterly reviews to update accountability when team structures change, when new workload types are onboarded, and after incident retrospectives that reveal ownership gaps. Update the RACI before changes go live, so an incident isn't the first time a team discovers an ownership gap. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS01-BP03 Establish performance metrics by defining key performance indicators (KPIs) and service-level objectives (SLOs)](advops01-bp03.md) 
+  [ADVOPS04-BP01 Create runbooks for the most common operational events and incidents that can impact your advertising workload](advops04-bp01.md) 

 **Related documents:** 
+  [Create a RACI or RASCI matrix for a cloud operating model](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-raci-or-rasci-matrix-for-a-cloud-operating-model.html) 
+  [AWS Organizations best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html) 

 **Related services:** 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 
+  [AWS IAM](https://aws.amazon.com/iam/) 