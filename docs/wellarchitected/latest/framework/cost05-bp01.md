

# COST05-BP01 Identify workload requirements for cost

 Cost competes with performance, reliability, delivery speed, and team familiarity, and the right balance differs for every workload. Capture these priorities and the trade-offs behind them before you select services, then revisit them as the business changes. 

 **Desired outcome:** 
+  You document business priorities such as cost, performance, and reliability with clear weightings that teams agree on. 
+  Your cost optimization targets and acceptable trade-offs have consensus across product, engineering, finance, and business stakeholders. 
+  Your review cadence keeps cost priorities current as business needs and external conditions change. 

 **Common anti-patterns:** 
+  Teams make cost decisions in isolation from architecture and business goals. 
+  No process exists for weighing cost against other requirements, so trade-offs stay implicit. 
+  Trade-off decisions and their rationale go undocumented, so teams cannot trace why a choice was made. 
+  Stakeholders from finance, product, or business units are left out of cost discussions. 
+  Cost requirements are treated as fixed and never revisited. 

 **Benefits of establishing this best practice:** 
+  Cost optimization efforts align with business objectives rather than pulling against them. 
+  Resource allocation follows agreed priorities instead of individual preference. 
+  Finance and technology teams collaborate from a shared understanding of trade-offs. 
+  Trade-off decisions are traceable because the reasoning behind each one is recorded. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Because departments differ in skills and priorities, acceptable cost varies by team and by workload. Treat cost as one requirement among several, and make its relative weight explicit before you commit to services. 

 Every cost decision trades against something. Faster time to launch for a competitive feature can justify a more expensive managed service. A familiar database can accelerate a migration even when a cheaper engine exists. These are legitimate choices, but only when the trade-off is deliberate and recorded. The failure mode is the silent trade-off. A team optimizes for cost and degrades reliability, or delays a launch the business valued more than the savings. 

 Set cost requirements with input beyond engineering. Product owners identify which features justify premium spend, finance owns the budget envelope and reporting granularity, and business leaders set strategic direction. With a cross-functional group, you avoid re-litigating the same decision every quarter. 

 Priorities change over time. A workload tuned for rapid growth might need a cost focus once it matures, and a new service release can change which option is more cost-effective. Set a cadence to revisit these priorities so they stay aligned with the business. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assemble a cross-functional cost team:** Bring together the roles that shape cost decisions: product managers who hold business requirements, technical leads who understand architectural implications, financial analysts who assess cost impact, and business stakeholders who set strategic direction. Give the team defined roles, responsibilities, and a regular meeting cadence to track progress and changes. 

1.  **Define a prioritization framework:** Build a framework that lets you evaluate competing priorities objectively. Include criteria for assessing each business pillar, with metrics and a scoring system. Set thresholds that define when cost takes precedence over other factors and when it yields to them. 

1.  **Document the current state and requirements:** Map your existing cost centers and identify areas of significant spend and optimization potential. Work with business units to capture their requirements and constraints, including any regulatory or compliance needs that affect cost decisions. Record technical debt and how it affects both current cost and future optimization. 

1.  **Establish a review and adjustment process:** Set review cycles that match your planning rhythm, such as quarterly strategic reviews and monthly tactical adjustments. Define triggers for out-of-cycle reviews, such as major shifts in customer demand, new business initiatives, or new technology. Capture lessons learned so each cycle improves the next. 

1.  **Set up a communication mechanism:** Create standardized templates for documenting decisions and their rationale so trade-offs stay traceable over time. Establish regular reporting that gives stakeholders visibility into cost optimization initiatives and their impact. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST05-BP02 Analyze all components of the workload](cost05-bp02.md) 
+  [PERF01-BP02 Evaluate the trade-offs between performance and other non-functional requirements](perf01-bp02.md) 
+  [REL11-BP07 Architect your product to meet availability targets and uptime service level agreements (SLAs)](rel11-bp07.md) 

 **Related documents:** 
+  [AWS Pricing Calculator](https://calculator.aws/#/) 
+  [AWS Pricing MCP Server](https://awslabs.github.io/mcp/servers/aws-pricing-mcp-server) 