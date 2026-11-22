

# ADVSEC01-BP05 Implement cross-platform identity governance for converged linear and digital operations

 The unified platform of linear television and digital advertising means that identity governance must cover two unique data models: household panels and user-level impressions. Without it, identity resolution can expose viewer data across consent boundaries or reveal panel membership to unauthorized parties. 

 **Desired outcome:** 
+  You have a unified identity governance policy covering both linear (panel-based, household-level) and digital (user-level, device-level) identity spaces. 
+  Your identity resolution operations enforce consent boundaries so data collected under one consent scope isn't resolved into another without authorization. 
+  You have integrated industry identity frameworks (UID2 and RampID) with proper security controls including token lifecycle management and sharing participant verification. 

 **Common anti-patterns:** 
+  Resolving linear panel data (household-level) to individual digital identifiers without verifying that consent covers both use cases. 
+  Storing identity mappings between linear and digital identifiers indefinitely without TTL aligned to consent validity periods. 
+  Using a single identity resolution pipeline for all purposes (targeting, measurement, and attribution) without purpose-level access controls. 

 **Benefits of establishing this best practice:** 
+  Reduces the risk of identity leakage that could compromise panel methodology (exposing who is in a measurement panel) or violate viewer privacy. 
+  Enables measurement and attribution across linear and digital environments while maintaining privacy boundaries between data sources. 
+  Supports interoperability with IAB identity frameworks (UID2 and RampID) using their mandated security controls rather than ad-hoc implementations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Linear TV historically operated without user-level identifiers. Measurement relied on statistical panels (Nielsen and Comscore) representing populations. Digital operates with deterministic identifiers (device IDs, logged-in users, and IP addresses). Govern the identity bridge between panel and census data as your most sensitive data. A compromise exposes both the measurement methodology and individual viewer privacy. 

 Industry identity frameworks provide the interoperability layer. UID2 (Unified ID 2.0) uses multi-layer hashing with rotating salt values and encrypted tokens. This supports deterministic identity across publishers, mobile apps, and CTV without exposing raw PII. For every identity data exchange, the UID2 sharing security model mandates authentication, authorization (contract-based participant verification), and accounting (transaction logs with checksums). RampID from LiveRamp resolves disparate identifiers (cookies, device IDs, and offline PII touchpoints) into a pseudonymous people-based identifier across digital, mobile, CTV, and offline channels. 

 Decide whether your cross-environment identity resolution happens in your own account or in a clean room. In-account resolution keeps full control and full liability, and data never leaves your environment. It gives complete auditability and faster iteration, but a breach exposes the full mapping table. Clean room resolution shares computation, distributes liability, and limits the scope of impact, because each party sees only its contributed data plus aggregate results. This introduces operational dependencies. If your measurement partner's configuration changes, your resolution pipeline breaks until you realign it. 

 Enforce consent boundaries architecturally so the pipeline cannot join linear-consent and digital-consent data without validation. Every join must pass through a validation gate that checks consent metadata on both source records. UID2's Authenticated Advertising model provides a similar structural approach, using separate token types for different permitted uses. 

 Identity mappings can outlive their consent validity. A viewer opts out of measurement participation, but their panel-to-digital mapping persists in a derived dataset created before the opt-out. Every downstream query against that dataset now processes data without valid consent. TTL-based expiration aligned to consent refresh periods is a structural requirement. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define identity governance policy for both linear and digital identity spaces:** Document which identity types exist in your system (panel IDs, ACR household IDs, device IDs, logged-in user IDs, UID2 tokens, and RampIDs), their consent scope, and which resolution operations are permitted between them. 

1.  **Implement consent boundary enforcement in identity resolution pipelines:** Enforce consent upstream of matching: AWS Entity Resolution doesn't expose a pre-processing hook inside its matching workflows, so filter records on consent metadata during source data preparation (AWS Glue ETL, or Lambda orchestrated with Step Functions) and write only records consented for the intended purpose (measurement, targeting, or attribution) to the S3/Glue input tables the matching workflow consumes. 

1.  **Integrate UID2 with proper sharing security controls:** Implement the UID2 AAA model: authenticate sharing participants, verify UID2 Participation Policy signatures before sharing, maintain transaction logs (timestamp, recipient ID, data volume, transfer method, and checksum). Configure UID2 token refresh to enforce short-lived credentials. 

1.  **Configure AWS Entity Resolution with LiveRamp RampID provider:** Enable LiveRamp identity resolution through the AWS Marketplace integration. Configure matching workflows to resolve to RampID within your AWS environment. Implement audit logging for all resolution operations through CloudTrail. 

1.  **Implement temporal controls on identity mappings:** Configure TTL on all cross-environment identity mapping records (DynamoDB TTL or S3 Lifecycle). Align retention periods with consent validity. Delete mappings when underlying consent expires or is withdrawn. 

1.  **Establish audit trail for identity resolution operations:** Log all resolution operations with: who initiated, what data was resolved, which purpose, timestamp, and result. Use CloudTrail plus custom application logs. This supports both regulatory adherence and UID2 accounting requirements. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC01-BP04 Implement least privilege access to protect programmatic workloads](advsec01-bp04.md) 
+  [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md) 
+  [ADVSEC05-BP02 Design for compliance across both linear and digital data flows](advsec05-bp02.md) 

 **Related documents:** 
+  [AWS Entity Resolution in Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-entity-resolution.html) 
+  [UID2 Sharing Security Requirements](https://unifiedid.com/docs/sharing/sharing-security) 
+  [LiveRamp Identity using AWS Entity Resolution](https://docs.liveramp.com/identity/en/liveramp-identity-using-aws-entity-resolution.html) 
+  [IAB Tech Lab Identity Solutions Guide](https://iabtechlab.com/navigating-the-maze-of-identity-solutions-a-guide-for-advertisers-publishers-and-adtech/) 

 **Related services:** 
+  [AWS Entity Resolution](https://aws.amazon.com/entity-resolution/) 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 
+  [LiveRamp for AWS Entity Resolution (Marketplace)](https://aws.amazon.com/marketplace/pp/prodview-ozomi3ns66nig) 