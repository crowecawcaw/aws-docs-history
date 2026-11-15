

# ADVCOST01-BP03 Consolidate identity resolution to reduce redundant matching across linear and digital audiences
<a name="advcost01-bp03"></a>

 You pay twice for matching and resolution when you maintain separate identity graphs for linear and digital audiences, often through different vendors with overlapping capabilities. A single resolution process builds one unified audience graph, cuts redundant matching costs, and deduplicates audiences across screens. 

 **Desired outcome:** 
+  A single identity resolution process creates a unified audience graph spanning household-level linear identifiers and individual-level digital identifiers. 
+  Consolidation reduces duplicate identity vendor costs. 
+  Cost per resolved identity is tracked and decreasing. 

 **Common anti-patterns:** 
+  Paying separate identity resolution vendors for linear panel-based household matching and digital device graph with overlapping coverage, duplicating matching costs for the same underlying viewers. 
+  Maintaining real-time cross-region identity synchronization when batch synchronization (once or twice daily) would satisfy most frequency management needs at far lower cost. 

 **Benefits of establishing this best practice:** 
+  Reduce duplicate identity vendor costs (linear panel matching \+ digital ID graph = 2x the spend). 
+  Cross-screen frequency management reduces wasted impressions, improving ROI on ad spend. 
+  Unified graph improves audience accuracy, increasing yield on audience-targeted campaigns. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Identity resolution maps disparate identifiers (cookies, mobile advertising IDs, set-top box IDs, CTV device IDs, first-party login IDs, and ACR fingerprints) to a single viewer or household. One vendor resolves household-level identifiers from linear panel data, and a separate vendor resolves device-level identifiers from digital impression streams. These vendors resolve the same underlying viewers through different identifier types and charge separately for each resolution. 

 A unified identity graph consolidates all identifier types into a single resolution process. The graph structure maps relationships between identifiers. A household ID connects to multiple device IDs, which connect to individual-level identifiers. [AWS Entity Resolution](https://aws.amazon.com/entity-resolution/) provides managed matching workflows that accept heterogeneous identifier types and produce deduplicated entity records. ID namespaces maintain structured mappings between identifier types without exposing raw PII. This supports privacy compliance when combining linear (often household-level, less regulated) with digital (often individual-level, more regulated) data. 

 The unified graph also supports cross-screen frequency management. Without it, a viewer who watches linear TV and then opens a streaming app on their phone appears as two separate identities. When you apply frequency caps independently per channel, the same viewer sees the ad three times on linear and three times on digital. With a unified identity, you can cap frequency across screens, cutting wasted impressions and improving advertiser ROI. 

 Synchronization cadence has a direct effect on cost. Real-time cross-region identity synchronization is expensive and rarely necessary. Most frequency management use cases tolerate batch synchronization once or twice daily, because campaigns run over days or weeks and a few hours of lag in identity updates does not materially affect delivery. Real-time sync is justified only for short-burst campaigns or strict per-hour frequency caps, which are a small minority of campaigns. 

 The graph storage supports two access patterns at the same time. For relationship traversal queries (for example, finding all devices belonging to a particular household), consider graph databases like [Amazon Neptune](https://aws.amazon.com/neptune/). For low-latency key-value lookups during real-time bid evaluation (for example, determining if a device ID is known or what its frequency count is), consider [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). Both access patterns read the same underlying identity data, produced by the same resolution process. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Audit identity resolution vendors and quantify overlap:** Catalog all identity resolution vendors: linear panel-based household matching, digital device graph, cookie sync, and first-party ID resolution. Calculate total annual spend and identify coverage overlap (where both vendors resolve the same underlying viewers through different identifier types). 

1.  **Configure AWS Entity Resolution with both linear and digital identifiers:** Create Entity Resolution matching workflows that accept both linear household identifiers (STB IDs, ACR device fingerprints, and panel IDs) and digital identifiers (MAIDs, first-party IDs, and CTV device IDs). Define ID namespaces to maintain structured mappings between identifier types without exposing raw PII. 

1.  **Build the unified audience graph in Neptune and DynamoDB:** Store identity resolution outputs in Amazon Neptune (for relationship traversal queries: "all devices in this household") and Amazon DynamoDB (for low-latency key-value lookups during real-time bid evaluation and frequency capping). The unified graph replaces separate vendor-specific identity graphs. 

1.  **Replace point-to-point vendor integrations with the unified resolution step:** Update ad server, DSP, and frequency cap systems to query the unified audience graph rather than maintaining separate vendor connections. This simplifies integration maintenance and reduces the number of vendor relationships you have to manage. 

1.  **Track cost per resolved identity and compare to previous vendor invoices:** Calculate cost per resolved identity (Entity Resolution monthly cost / total unique identities resolved). Compare monthly costs against the previous sum of separate vendor invoices. Track match rate improvements as the unified graph benefits from bidirectional signal enrichment that siloed graphs could not achieve. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST01-BP01 Continually measure costs of advertising workloads, and adjust resource and model allocation accordingly](advcost01-bp01.md) 

 **Related documents:** 
+  [Create a 360-degree View of Consumers Using Entity Resolution and Neptune](https://aws.amazon.com/blogs/industries/create-a-360-degree-view-of-your-consumers-using-aws-entity-resolution-and-amazon-neptune/) 
+  [Solve Customer Identity Fragmentation at Scale](https://aws.amazon.com/blogs/industries/solve-customer-identity-fragmentation-at-scale-with-aws-entity-resolution/) 

 **Related services:** 
+  [AWS Entity Resolution](https://aws.amazon.com/entity-resolution/) 
+  [Amazon Neptune](https://aws.amazon.com/neptune/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 