

# ADVSEC05-BP02 Design for compliance across both linear and digital data flows

 When you design across datasets that can intersect, treat the joined result as its own compliance case. For example, household data and device data might each be fine on their own, but when you match them, they can pinpoint one person. The combined dataset then falls under tighter privacy obligations, even though you followed every rule on either data source. 

 **Desired outcome:** 
+  You have classified linear and digital data by source, granularity, jurisdiction, consent scope, authorized purpose, and retention requirement. 
+  You have controls that permit cross-source processing only when every contributing dataset authorizes the intended purpose. 
+  You have retained lineage and rights-management identifiers through joins, aggregates, exports, and measurement outputs. 

 **Common anti-patterns:** 
+  Applying one consent model to panel data, device data, and impression-level records. 
+  Joining household and user-level data without deciding which purposes every source authorizes. 
+  Dropping consent, retention, or deletion metadata after an aggregate or matched dataset is created. 
+  Treating regional infrastructure placement as proof that every processing purpose is permitted. 

 **Benefits of establishing this best practice:** 
+  Supports converged measurement without crossing approved consent or purpose boundaries. 
+  Makes retention, access, and privacy-rights decisions traceable across derived datasets. 
+  Gives reviewers evidence of which rules governed each cross-channel processing operation. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Linear and digital tell you where data comes from, but not necessarily how sensitive it is. For example: 
+  Panel records can identify a household 
+  Automatic content recognition data can reveal what someone watched 
+  Impression logs can identify a device or a person 

 Matching sources can create relationships that none of them exposed alone. Aggregating them can lower disclosure risk yet leave contract and consent constraints in force. 

 A *data treatment envelope* holds the constraints attached to a source. When you process across sources, apply the *purpose intersection rule*: every contributing source must authorize the purpose you intend. Reconciling what "purpose" means across panel agreements, consent frameworks, and partner contracts takes human review. Two sources can use the same purpose label for different scopes. Automated matching cannot resolve that mismatch, and defaulting to the least restrictive reading is unsafe. 

 Consent can expire after you release an aggregate, and a partner can leave after you match records. Keeping identity lineage so you can delete data later creates its own exposure. Deleting a source record, blocking recomputation, suppressing disclosure, and editing a released aggregate each produce a different outcome. Your compliance authority decides which outcome is acceptable. Your identity and data-protection controls enforce separate parts of that decision. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Register source treatment envelopes:** Assign each source an envelope ID and store its approved metadata in the [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) or another governed system. Reject records that lack the envelope required for the processing path. 

1.  **Create a cross-source use-case record:** Identify the intended purpose, contributing envelopes, approved purpose mappings, output classification, lifecycle decisions, and accountable authority. Record unresolved conflicts instead of selecting the least restrictive source. When a mapping depends on a voluntary framework, record the framework version, mapping owner, and review date. 

1.  **Enforce the approved boundary:** Check the use-case record before query jobs, extract, transform, and load (ETL) jobs, or measurement jobs run. Use [AWS Lake Formation data filters](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html) or equivalent controls to limit inputs and columns to the approved scope. 

1.  **Generate bounded lineage:** Carry envelope IDs, treatment decisions, retention dates, consent state, and protected deletion handles into matched and derived records. Restrict access to identity-bearing lineage separately from the analytical output. 

1.  **Attach owned protection controls:** Map each constraint to its enforcing control. Use [ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS](advsec02-bp01.md) for partner transport, [ADVSEC02-BP02 Protect linear distribution feeds and ad signaling in converged delivery](advsec02-bp02.md) for converged feeds, [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md) for collaboration, or [ADVSEC02-BP04 Implement confidential computing for cross-party measurement without exposing raw viewer data](advsec02-bp04.md) for record-level computation. Link identity constraints to [ADVSEC01-BP05 Implement cross-platform identity governance for converged linear and digital operations](advsec01-bp05.md), and retain each control's evaluation evidence. 

1.  **Exercise lifecycle decisions:** Test deletion, consent withdrawal, partner termination, retention expiration, disclosure suppression, and recomputation blocking. Route outputs that can't follow the approved treatment through the compliance exception process. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC05-BP01 Verify that your advertising workload meets applicable data protection obligations](advsec05-bp01.md) 
+  [ADVSEC01-BP05 Implement cross-platform identity governance for converged linear and digital operations](advsec01-bp05.md) 
+  [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md) 
+  [ADVSEC04-BP02 Create guardrails and controls to maintain brand safety and content moderation within your workload](advsec04-bp02.md) 

 **Related documents:** 
+  [AWS Control Tower data residency controls](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-controls.html) 
+  [IAB Europe Transparency and Consent Framework (TCF) policies](https://iabeurope.eu/iab-europe-transparency-consent-framework-policies/). TCF is a voluntary industry framework. 
+  [Children's Online Privacy Protection Rule](https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa) 