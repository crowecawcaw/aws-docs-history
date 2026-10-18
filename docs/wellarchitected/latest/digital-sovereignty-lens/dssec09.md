

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

## Common issues to watch for
<a name="common-issues-to-watch-for-8"></a>
+  Incident response plans that treat all jurisdictions identically, missing variation in notification timelines, evidence requirements, and authority coordination protocols. 
+  Evidence collection workflows that move data to a central investigation environment in another jurisdiction, violating data residency requirements during the investigation itself. 
+  Regional response teams that lack the authority or tooling to contain incidents within their jurisdiction, forcing delays while centralized teams coordinate cross-border. 
+  Regulatory notification tracked informally (email, spreadsheet) rather than through auditable workflows, making it difficult to prove timely notification after the fact. 
+  Post-incident reviews focused exclusively on security improvements, missing opportunities to strengthen the compliance response process and update jurisdiction-specific playbooks. 