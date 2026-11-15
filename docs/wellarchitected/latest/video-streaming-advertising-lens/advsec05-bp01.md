

# ADVSEC05-BP01 Verify that your advertising workload meets applicable data protection obligations
<a name="advsec05-bp01"></a>

 Advertising platforms process data across many jurisdictions, business relationships, and delivery channels, and each has obligations from law, contracts, and voluntary frameworks. Adherence to obligations requires tracing each obligation to the data it affects, the purpose it governs, the control that enforces it, and the evidence you kept. 

 **Desired outcome:** 
+  You have approved obligation records that map data types and processing purposes to applicable requirements, covering obligations from laws and regulations, contracts, and voluntary frameworks. 
+  You have controls that identify new or changed personal data flows before they operate without a compliance decision. 
+  You have traceability from each obligation to a control owner, implementation evidence, exception status, and review history. 

 **Common anti-patterns:** 
+  Treating compliance as a point-in-time audit and allowing controls to drift between reviews. 
+  Presenting encryption or access-control settings as compliance proof without connecting them to a specific obligation. 
+  Applying one retention or consent policy to every advertising dataset, regardless of purpose or jurisdiction. 
+  Reconstructing evidence after an audit request instead of preserving it when a control operates. 

 **Benefits of establishing this best practice:** 
+  Finds compliance gaps before they affect viewers, partners, or regulatory commitments. 
+  Reduces audit preparation work by maintaining evidence with each control decision. 
+  Gives engineering teams clear requirements without asking them to interpret laws or contracts. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A control can run as designed and still back an invalid compliance claim when the claim names the wrong data, purpose, people, partner, or period. You cannot resolve overlapping requirements with a single rule that applies the strictest requirement. Longer retention satisfies a financial obligation but breaks data minimization. A transfer's terms can determine how a Region treats the data. 

 A claim can become invalid even when every control still works. Enriching a dataset makes it more sensitive, aggregating records changes disclosure risk, and a new use can exceed what you interpreted before. Evidence alone does not always corroborate details, especially when different sources cannot be cross-referenced. A point-in-time snapshot proves little once the data or the control changes between observations. 

 Independent proof and data minimization are often at odds. Detailed lineage and event records improve traceability, but they can grow into identity-bearing datasets with their own obligations. Independence weakens when one team interprets the requirement, operates the control, accepts the exceptions, and selects the proof. Design your governance so no single team or person does all of these compliance tasks, and weigh evidence fidelity against its cost and exposure. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Instantiate compliance claims:** Assign each approved claim a unique ID, authority, effective period, scope selector, control objective, evidence assertion, and accountable owners. Store legal and regulatory obligations, contractual commitments, and voluntary industry-framework claims as distinct claim types in one governed catalog. For a claim that depends on TCF, record the TCF policy version your workload implements, its applicable policy scope, an owner, and a review date. 

1.  **Bind claims to the data inventory:** Use [Amazon Macie sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs.html) to analyze supported objects in Amazon S3. Use catalog metadata to register other assets, and use workload lineage to trace derived datasets, destinations, and partner transfers. Generate coverage records from these scoped sources. Record unresolved scope rather than inferring approval. 

1.  **Gate material changes:** Compare proposed schema fields, partners, Regions, purposes, and destinations with the applicable claim scopes. Hold a changed use until the obligation authority approves a revised claim or the exception authority records bounded acceptance. 

1.  **Bind objectives to owned controls:** Map each objective to its data-protection control. Use [ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS](advsec02-bp01.md) for partner bid transport, [ADVSEC02-BP02 Protect linear distribution feeds and ad signaling in converged delivery](advsec02-bp02.md) for linear contribution and signaling, [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md) for collaboration, or [ADVSEC02-BP04 Implement confidential computing for cross-party measurement without exposing raw viewer data](advsec02-bp04.md) for record-level confidential computation. Use [AWS Config conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) and workload tests to evaluate the claim without duplicating the control design. 

1.  **Assemble the required evidence forms:** Retain design records, control evaluations, [AWS CloudTrail event records](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html), outcome records, approvals, and provenance for the claimed scope and period. 

1.  **Revalidate claims and exceptions:** Alert owners when scope, classifications, controls, evidence, or authority changes. Review exceptions before expiration, verify remediation against the original claim, and preserve the closure decision. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC05-BP02 Design for compliance across both linear and digital data flows](advsec05-bp02.md) 
+  [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md) 
+  [ADVSEC01-BP04 Implement least privilege access to protect programmatic workloads](advsec01-bp04.md) 

 **Related documents:** 
+  [Compliance validation for Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/compliance-validation.html) 
+  [Compliance validation for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-compliance.html) 
+  [Defining boundaries for regional services access](https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/defining-boundaries-for-regional-services-access.html) 
+  [IAB Europe Transparency and Consent Framework (TCF)](https://iabeurope.eu/transparency-consent-framework/). TCF is a voluntary industry framework. 