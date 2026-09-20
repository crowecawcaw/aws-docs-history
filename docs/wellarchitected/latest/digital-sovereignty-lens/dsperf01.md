

# Sovereign solution selection
<a name="dsperf01"></a>

 Not every sovereign workload needs the same level of control, and applying maximum restrictions everywhere drives unnecessary cost and complexity. AWS provides a continuum of deployment options with different combinations of service availability, operational responsibility, and sovereignty controls. Selecting the right option for each workload requires a data-driven approach that matches regulatory obligations, data residency needs, and operational constraints to the deployment model that satisfies them without over-engineering. 

 This capability covers the evaluation and selection of sovereign deployment options across the continuum of AWS Regions, European Sovereign Cloud, Dedicated Local Zones, and Outposts, using data-driven criteria rather than blanket policies. 


|  DSPERF01: How do you select the right sovereign solution for each workload?  | 
| --- | 
| [DSPERF01-BP01 Evaluate sovereign solutions using a data-driven approach](dsperf01-bp01.md) | 

## Capability intent
<a name="capability-intent"></a>
+  Workloads are matched to sovereign deployment options based on specific regulatory obligations and data residency requirements, not blanket policies that apply the same restrictions to all workloads. 
+  Decision criteria are explicit, documented, and repeatable so that different teams evaluating similar workloads reach consistent conclusions. 
+  The trade-offs between sovereignty controls, service availability, operational complexity, and cost are understood and accepted for each workload before deployment. 
+  Decision criteria are reviewed when regulatory requirements, service availability, or deployment options change, so placement decisions remain valid over time. 
+  The evaluation process considers the full lifecycle of the workload, including growth scenarios where requirements may shift to more or less restrictive options. 

## Maturity levels
<a name="maturity-levels"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Sovereign deployment decisions are made informally based on perception of risk rather than documented criteria. The same deployment option is applied to all workloads regardless of their specific requirements. Trade-offs are not explicitly evaluated.  | 
|  2  |  Emerging  |  Decision criteria exist for selecting between deployment options, but they are applied inconsistently across teams. Some workloads are over-constrained while others are under-constrained relative to their actual requirements.  | 
|  3  |  Defined  |  A structured evaluation framework maps workloads to deployment options based on documented criteria (regulatory obligations, residency requirements, service needs, operational capacity). Decisions are recorded with their rationale.  | 
|  4  |  Proactive  |  Evaluation criteria are reviewed when deployment options, service availability, or regulatory requirements change. Workload placement is reassessed periodically. New deployment options are evaluated against existing workload requirements.  | 
|  5  |  Optimized  |  Placement decisions are informed by operational data (cost, performance, compliance posture) and refined over time. The organization anticipates how regulatory changes will shift requirements and pre-plans migration paths. Evaluation frameworks are shared across teams as reusable tooling.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for"></a>
+  Blanket policies that place all workloads in the most restrictive deployment option. Workloads that do not need maximum controls then carry unnecessary cost and lose access to services unavailable in that option. 
+  Decision criteria that weigh data residency alone and ignore operational complexity, service availability constraints, and cost, so the chosen option is compliant but hard to operate. 
+  Workload placement decisions made once at initial deployment and never revisited, even when regulatory requirements or available deployment options change. 
+  Evaluation processes that are neither documented nor repeatable, so teams reach different conclusions and workloads with similar requirements land in different options. 
+  Trade-off decisions made without input from both compliance and operations stakeholders, which satisfy one concern and create problems for the other. 