

# ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls

 Advertising measurement, attribution, and audience insights require multiple parties to combine their data. Privacy-preserving collaborating mechanisms help you avoid sharing raw data (privacy riks) forgoing cross-party insights (business cost). Secure data collaboration produces those insights without data exposure. 

 **Desired outcome:** 
+  You have established data collaboration environments where multiple parties can analyze combined datasets without exposing raw data to each other. 
+  You have selected a privacy mechanism for each collaboration and query pattern from your assessment, and the configured analysis rules match that selection. 
+  You have service and workflow audit evidence that a reviewer can join on a recorded query identifier, covering query submission, status, purpose, approval, output release, recipient, and delivery. 

 **Common anti-patterns:** 
+  Sharing raw audience segment files through Amazon S3 bucket sharing or file transfer between publisher and advertiser accounts without controls on downstream access. 
+  Allowing unrestricted SQL queries against collaborative datasets without minimum aggregation thresholds, which lets partners extract individual-level records. 
+  Running measurement collaborations without audit logs, so no one can verify how shared data was used or detect policy violations. 

 **Benefits of establishing this best practice:** 
+  Enables cross-publisher measurement attribution and audience overlap analysis without exposing individual viewer data to any party. 
+  Supports advertiser-publisher deal troubleshooting with shared data access that is auditable and purpose-limited. 
+  Provides cryptographic and policy controls that limit what each party can learn, which a privacy or legal authority can assess against data minimization obligations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Raw data collaboration with supply-side platforms (SSPs), demand-side platforms (DSPs), and third-party measurement systems requires governance because the collaboration mechanism becomes an attack surface. AWS Clean Rooms provides the architectural container, but its security properties depend on the access rules, privacy mechanisms, and encryption configured for each collaboration. 

 The trust model for multi-party advertising collaboration defines the architectural requirements before any technology selection. An advertiser running a campaign across multiple publishers needs aggregate reach and frequency without learning any individual publisher's competitively sensitive audience composition. A publisher validating campaign delivery needs to confirm impressions reached the contracted audience without exposing its content-consumption graph. These confidentiality requirements define what each party must learn and which privacy mechanisms are necessary. 

 Clean room queries use three privacy mechanisms with different security properties. 

1.  Analysis rules provide deterministic controls for minimum aggregation thresholds, permitted join keys, and column access without adding computational noise. 

1.  Repeated queries can still probe boundary cases and narrow the result set. 

1.  Differential privacy adds calibrated noise and provides a formal, quantified privacy guarantee. 

 Each query consumes privacy budget, so query capacity and result utility both fall as analysis accumulates. Small populations exhaust usable utility first, which affects niche audiences and geographic microtargets. A scheduled privacy budget refresh restores query capacity, and it also moves the guarantee. When the same rows are queried again after each refresh, cumulative disclosure is no longer bounded by one budget. Recurring campaign measurement tends to query the same audiences month after month, so a refresh cadence chosen for reporting convenience can undo the protection the budget provides. 

 Cryptographic Computing for Clean Rooms encrypts data client-side, so neither the service nor the other members hold cleartext. Protected columns support JOIN and SELECT only. Aggregate functions such as SUM and AVERAGE are unavailable on protected columns even where an analysis rule would allow them, which rules out pairing this mechanism with aggregate reporting on the same columns. Table shape, column names, row counts, an upper bound on value lengths, and the timing of row additions can still be inferred. 

 A data handling agreement must precede technical configuration. It identifies whether the contributor, consumer, or a joint framework defines analysis rules. It also defines escalation for rejected queries, contributor veto authority, and onboarding when legal review outlasts the campaign launch schedule. 

 Service logs and business evidence answer different questions. AWS Clean Rooms analysis logging records that a query ran, which tables it referenced, and whether it succeeded. It doesn't record why the query was authorized, who approved it, who received the result, or whether the output was released as agreed. Those facts are recorded in the system your organization uses to run the approval, so a collaboration produces two evidence sets rather than one. A query log without an approval record shows activity without authority, and an approval record that can't be tied to a specific query shows intent without execution. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Match each advertising use case to an AWS Clean Rooms analysis rule type:** Create collaborations for specific scenarios such as measurement attribution, audience overlap, and yield analysis. Define each party's role and specify who can query, receive results, or contribute data. For each configured table, select the analysis rule type the use case requires: aggregation for count and sum reporting under a minimum aggregation threshold, list for row-level overlap, or custom for reviewed analysis templates and for differential privacy. A query can reference only configured tables that share an analysis rule type, and where a query spans tables the service applies the more restrictive control, so group use cases into collaborations accordingly. 

1.  **Set minimum aggregation thresholds from a privacy assessment:** Define thresholds for each collaboration and query pattern through a documented re-identification risk assessment. Assess query shape, contribution limits, repeated-query behavior, auxiliary data, output policy, and differential-privacy configuration. Restrict join keys to approved identifiers. Test boundary and repeated-query attacks, and obtain privacy-owner approval before production use. Record the assessment reference, the approved parameters, the tested query set and its results, the residual risk, the accountable owner, the approval date, and the next review date. 

1.  **Apply the approved differential privacy policy:** For the query patterns your assessment placed in scope, create the AWS Clean Rooms differential privacy policy using the privacy budget and the noise added per query that the assessment approved. The privacy budget is a single finite resource shared by every differential-privacy protected table you contribute to the collaboration, and each query depletes it at a rate the noise setting governs. Compare candidate settings with the service's privacy impact preview before you commit them, and record the previewed query capacity alongside the approved values. 

1.  **Encrypt collaboration source data at rest and scope decrypt access:** Apply server-side encryption with AWS Key Management Service (AWS KMS) keys to the Amazon S3 locations that back your configured tables. Grant decrypt permission only to the service role your AWS Clean Rooms membership uses to read that data, and scope that role's own policies to the membership and configured-table resources it needs. Decide your key boundary, whether that is one key for each collaboration, partner, or data class, and record the decision with its rationale. 

1.  **Create query and workflow audit evidence:** Enable [AWS Clean Rooms analysis logging](https://docs.aws.amazon.com/clean-rooms/latest/userguide/query-logs.html) for the documented query-submission and status information available to each member. Use separate application or workflow logs for business purpose, approval, result recipient, output release, and delivery evidence. Carry the protected query identifier and the collaboration identifier in your workflow records, because those two fields appear in the analysis log and let a reviewer join a workflow record to the query it authorized. Retain both log sets for the period the data handling agreement and your assessed obligations require, using the longer period where they differ. 

1.  **Assign ownership and controls to the workflow evidence:** Name the system of record for the workflow evidence and the owner accountable for it. Record the requesting actor and the approving actor as separate values, and reject any record in which they match, because an approval the requester can grant to themselves isn't evidence of oversight. Limit write access to approval fields to the approving role. Define how records are protected from later alteration, how deletion is carried out and logged, and how a missing or conflicting record becomes a tracked exception with an owner and a due date. 

1.  **Reconcile the two evidence sets:** Reconcile the sets on a schedule. Alert when an executed query has no matching workflow record, when a workflow record has no matching query, and when a released result has no recorded release decision. Treat an unmatched record on either side as an exception with an owner rather than as an absent record. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC02-BP04 Implement confidential computing for cross-party measurement without exposing raw viewer data](advsec02-bp04.md) 
+  [ADVSEC01-BP05 Implement cross-platform identity governance for converged linear and digital operations](advsec01-bp05.md) 
+  [ADVSEC05-BP03 Enable privacy-preserving advertising capabilities while protecting user data](advsec05-bp03.md) 

 **Related documents:** 
+  [AWS Clean Rooms proof of concept: media measurement](https://aws.amazon.com/blogs/big-data/aws-clean-rooms-proof-of-concept-scoping-part-1-media-measurement/) 
+  [How AWS Clean Rooms works with IAM](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security_iam_service-with-iam.html) 
+  [Using server-side encryption with KMS keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) 
+  [AWS Clean Rooms differential privacy settings](https://docs.aws.amazon.com/clean-rooms/latest/userguide/dp-settings.html) 

 **Related services:** 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS KMS](https://aws.amazon.com/kms/) 
+  [AWS IAM](https://aws.amazon.com/iam/) 