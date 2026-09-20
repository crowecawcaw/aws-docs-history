

# Incident response
<a name="dssec09"></a>

 A security incident in a sovereign workload triggers jurisdiction-specific obligations that standard incident response plans don't cover. Notification timelines vary by regulatory framework. Evidence preservation has to respect data residency, and coordination with national competent authorities follows jurisdiction-specific protocols. When these regulatory requirements are built into incident response planning and execution, teams meet compliance obligations at the same time as containment and remediation. 

 This capability covers integrating regulatory compliance requirements into incident response planning, execution, and reporting for sovereign workloads. 


|  DSSEC09: How do you respond to security incidents while meeting sovereignty requirements?  | 
| --- | 
| [DSSEC09-BP01 Integrate compliance requirements into incident response](dssec09-bp01.md) | 

## Capability intent
<a name="capability-intent-8"></a>
+  Incident response plans incorporate jurisdiction-specific notification timelines, evidence requirements, and authority coordination protocols. 
+  Evidence is preserved within approved jurisdictions throughout the investigation, meeting data residency requirements even under incident conditions. 
+  Regional response teams can contain and investigate incidents within their jurisdiction without waiting for centralized coordination from another jurisdiction. 
+  Regulatory notification obligations are tracked and executed within mandatory timeframes, with documented proof of compliance. 
+  Post-incident review incorporates lessons learned into both the security posture and the compliance response process. 

## Maturity levels
<a name="maturity-levels-8"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Incident response follows a single generic playbook without jurisdiction-specific considerations. Notification obligations are identified after the fact. Evidence is preserved without explicit attention to data residency.  | 
|  2  |  Emerging  |  Jurisdiction-specific notification timelines are documented. Response plans acknowledge data residency requirements for evidence, but procedures are not fully operationalized. Coordination with regulatory authorities is informal.  | 
|  3  |  Defined  |  Response playbooks include jurisdiction-specific procedures for notification, evidence preservation, and authority coordination. Regional teams have defined roles in incident response. Evidence storage complies with data residency requirements by design.  | 
|  4  |  Proactive  |  Incident response procedures are tested through exercises that simulate sovereignty-specific scenarios (cross-border data exposure, regulatory notification deadlines). Automated workflows handle evidence preservation and notification tracking. Regional teams demonstrate independent response capability through regular drills.  | 
|  5  |  Optimized  |  Response effectiveness is measured against regulatory timelines and improved iteratively. Lessons learned feed back into both security controls and compliance processes. Cross-jurisdictional coordination is pre-established through documented agreements and rehearsed communication channels.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-8"></a>
+  Incident response plans that treat all jurisdictions identically, missing variation in notification timelines, evidence requirements, and authority coordination protocols. 
+  Evidence collection workflows that move data to a central investigation environment in another jurisdiction, violating data residency requirements during the investigation itself. 
+  Regional response teams that lack the authority or tooling to contain incidents within their jurisdiction, forcing delays while centralized teams coordinate cross-border. 
+  Regulatory notification tracked informally (email, spreadsheet) rather than through auditable workflows, making it difficult to prove timely notification after the fact. 
+  Post-incident reviews focused exclusively on security improvements, missing opportunities to strengthen the compliance response process and update jurisdiction-specific playbooks. 