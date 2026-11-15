

# ADVOPS01-BP01 Assess trade-offs between ad serving architecture options and associated risks
<a name="advops01-bp01"></a>

 When you design ad-serving infrastructure, evaluate the trade-offs between architectural options and their risks. Consider performance, scalability, availability, security, and cost. For publisher workloads, also evaluate server-guided ad insertion (SGAI) patterns, prebid deployment topologies, and free ad-supported streaming TV (FAST) channel assembly approaches. Do this through structured trade-off workshops that produce documented architecture decision records (ADRs). 

 **Desired outcome:** 
+  Publisher teams systematically evaluate architecture trade-offs for SGAI, prebid Server, and FAST channel workloads alongside existing demand-side RTB evaluations. 
+  Each evaluation produces a documented ADR that captures rationale, risk exposure, and reversibility for each architectural choice. 
+  Teams review ADRs quarterly to validate that the original assumptions remain valid as workloads evolve. 

 **Common anti-patterns:** 
+  You select an SGAI architecture (hybrid or fully server-side) without evaluating CDN caching implications and differences in scope of impact. Hybrid SGAI manifests are CDN-cacheable and serve all viewers from a single cached copy. Personalized SGAI generates a manifest for each session, which scales origin load with viewer count. 
+  You choose a prebid Server deployment topology (self-managed or third-party wrapper) based only on initial cost. You do not consider adapter lifecycle management overhead. 
+  You adopt dynamic AI-powered FAST channel assembly without validating operational readiness for an emerging, experimental pattern. 
+  You make architecture decisions without cross-functional stakeholder input from engineering, ad operations, and business teams. Each team holds different pieces of the risk picture. 

 **Benefits of establishing this best practice:** 
+  Informed architecture decisions balance yield optimization with operational complexity. 
+  Lower risk of costly architecture migrations after launch. 
+  Documented decision records help future teams understand rationale and constraints. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The downside of a wrong architecture decision in an ad platform exceeds the upside of a right one. A CDN architecture that works well for standard video delivery can fail for SGAI if SCTE-35 markers do not propagate through the caching layer. A prebid Server topology chosen to minimize initial infrastructure cost can accumulate adapter lifecycle debt that becomes operational burden at scale. 

 Many ad platforms lack a formal process for consequential architecture decisions. The first team to ship a working prototype sets the standard, and everything downstream inherits it. Informal evaluation ranks concerns by organizational volume, so risk exposure gets underweighted. A monetization team measured on revenue lift can rationally accept operational fragility. An infrastructure team measured on availability can veto those changes. Each team's judgment is correct within its own objective function. No shared objective reconciles the two. 

 Launch pressure compounds this problem by discounting reversibility. A hard-to-reverse choice costs the same to make as a reversible one but takes many more steps to undo. Examples include an ad signaling format built into deployed player behavior or a bidder integration built around one wrapper's request semantics. A deliberate assessment process makes these implicit decisions visible while they are still cheap to change. 

 For SGAI, you choose between CDN cacheability and personalization for each viewer. Hybrid SGAI generates manifests that are not viewer-specific. The CDN can cache these manifests and serve them to all concurrent viewers, which cuts origin load at FAST channel scale. Personalized SGAI generates a manifest for each session, which provides greater targeting precision but scales origin infrastructure linearly with concurrent viewers. Scheduled content benefits from the CDN efficiency of hybrid SGAI. Premium live events can justify the targeting fidelity of personalized SGAI. 

 For prebid servers, a self-managed containerized deployment gives you full control over adapter configuration, auction timeout settings, and bidder-level analytics. It requires engineering ownership of upgrades, security patches, and scaling operations. Managed header-bidding solutions reduce operational overhead but limit customization. Weigh the choice against team capacity, active adapter count, and adapter onboarding rate. 

 Architecture decision records (ADRs) capture the decision context, options evaluated, criteria applied, decision rationale, and accepted risks in a structured format. They prevent teams from re-debating the same trade-offs and inform re-evaluations when circumstances change. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory all publisher workload architecture decisions that need evaluation:** Catalog all pending or recently made architecture choices across SGAI pattern selection, prebid server deployment topology, FAST channel assembly approach, and agentic AI integration patterns. Include decisions already made but not documented. Capture the rationale retroactively rather than leave the decision undocumented. 

1.  **Define evaluation criteria by decision type:** For each architecture decision, document the evaluation dimensions. Yield impact: what is the expected CPM and fill rate outcome? Operational complexity: what does the team need to own? Scope of impact: what breaks when this fails, and how many viewers are affected? Reversibility: how straightforward is it to change the decision after launch? Cost: what infrastructure and engineering does this require? 

1.  **Conduct structured trade-off workshops:** Run cross-functional workshops with engineering, ad operations, and business stakeholders for each architecture decision category. Each discipline contributes a distinct view. Engineering assesses technical feasibility and operational burden. Ad operations assesses yield and monetization impact. Business sets revenue expectations and risk tolerance. Document the outcome as an ADR with a consistent template. 

1.  **Document Architecture Decision Records with risk and reversibility:** Produce an ADR for each evaluated decision. Capture the options considered, criteria applied, decision made, rationale, accepted risks, and conditions to revisit the decision. Store ADRs in a version-controlled repository alongside the code they describe. Include a next review date field to prompt quarterly re-evaluation. 

1.  **Review ADRs quarterly to validate assumptions:** Schedule quarterly ADR reviews to assess whether the original assumptions remain valid. Trigger re-evaluation on any of these: significant changes in viewer volume, new SGAI or prebid capabilities from AWS or the open-source community, changes in adapter performance or partner relationships, and observed scope-of-impact events that exceeded the documented risk estimate. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS01-BP02 Create RACI matrices that define the roles and responsibilities for each key advertising process](advops01-bp02.md) 
+  [ADVOPS01-BP03 Establish performance metrics by defining key performance indicators (KPIs) and service-level objectives (SLOs)](advops01-bp03.md) 

 **Related documents:** 
+  [Guidance for AWS RTB Fabric with Real-Time Bidding Workloads on AWS](https://aws.amazon.com/solutions/guidance/aws-rtb-fabric-with-real-time-bidding-workloads-on-aws/) 
+  [Guidance for Advertising Agents on AWS](https://aws.amazon.com/solutions/guidance/advertising-agents-on-aws/) 

 **Related services:** 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 