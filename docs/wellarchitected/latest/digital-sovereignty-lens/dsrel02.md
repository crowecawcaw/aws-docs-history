

# Third-party sovereignty risk management
<a name="dsrel02"></a>

 Third-party vendors can introduce sovereignty risks that remain invisible until an audit or incident exposes them. Data processed in non-approved jurisdictions, operators accessing systems from foreign locations, and sub-processors that don't adhere to data residency requirements are common examples. Standard vendor risk assessments focus on security posture and financial stability but miss sovereignty-specific concerns. 

 This capability covers continuous third-party risk management that assesses vendor data residency, operator location, cross-border data flows, and contractual safeguards throughout the vendor lifecycle. 


|  DSREL02: How do you manage third-party sovereignty risks?  | 
| --- | 
| [DSREL02-BP01 Implement continuous third-party risk management (TPRM) processes](dsrel02-bp01.md) | 

## Capability intent
<a name="capability-intent-1"></a>
+  Third-party vendors are assessed against sovereignty-specific criteria (data residency, operator location, sub-processor chains, and contractual exit provisions) before onboarding and continuously thereafter. 
+  Vendor data flows are mapped to identify where data is stored, processed, and transferred, including flows through sub-processors. 
+  Contractual safeguards address sovereignty requirements explicitly, including data return provisions, audit rights, and notification of material changes to processing locations. 
+  Vendor risk posture is monitored continuously rather than assessed only at contract renewal, with triggers for reassessment when vendor circumstances change. 
+  Exit plans exist for critical vendors, with tested procedures for data extraction, migration, and continuity that maintain sovereignty compliance during transition. 

## Common issues to watch for
<a name="common-issues-to-watch-for-1"></a>
+  Vendor risk assessments that focus on security certifications without evaluating where data is actually processed or where operators are located. 
+  Sub-processor chains that are not mapped beyond the direct vendor, so sovereignty risks stay hidden in second-tier and third-tier relationships. 
+  Data return provisions that exist in contracts but have never been tested, so the organization has no validated path to reclaim data under sovereignty constraints. 
+  Vendor reassessment triggered only at contract renewal on annual or multi-year cycles, which misses material changes in processing locations or corporate ownership between assessments. 
+  Concentration of critical capabilities in a single vendor without pre-qualified alternatives, which becomes a sovereignty-relevant continuity risk if that vendor faces trade restrictions or regulatory action. 