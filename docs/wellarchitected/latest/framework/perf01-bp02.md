

# PERF01-BP02 Evaluate the trade-offs between performance and other non-functional requirements

 Every performance improvement has a cost in another dimension: consistency, durability, cost, operational simplicity, or security. Weigh each trade-off against business priorities and record the reasoning. 

 **Desired outcome:** 
+  You have a repeatable method to weigh performance against other non-functional requirements. 
+  You understand how a performance decision affects cost, operational excellence, reliability, security, and sustainability. 
+  You record the alternatives you considered and the reasons you rejected them. 
+  Your decisions optimize overall efficiency while preserving the integrity of the other pillars. 

 **Common anti-patterns:** 
+  Teams decide based on a single performance metric without weighing the broader impact. 
+  Teams improve performance in one area without checking whether another pillar degrades as a result. 
+  Teams fail to record the alternatives they considered and why they rejected them. 
+  Teams evaluate options without a repeatable method and skip edge cases and exceptional scenarios. 

 **Benefits of establishing this best practice:** 
+  Decisions improve because a structured framework accounts for every pillar, not performance alone. 
+  Teams avoid over-optimizing performance at the expense of cost, reliability, or security. 
+  Recorded reasoning makes decisions auditable and cheaper to revisit when conditions change. 
+  Systems stay maintainable because trade-offs are deliberate rather than accidental. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Caching cuts read latency but adds a consistency problem and requires an invalidation strategy. Read replicas raise throughput but increase cost and operational load. Compressing payloads saves network time but spends CPU. 

 The other Well-Architected pillars list the second-order effects of a performance change. Review each candidate design against every pillar to surface the compromises a performance-only view hides. 

 To weigh competing trade-offs, use a decision matrix. List candidate options on one axis and evaluation criteria, such as performance gain, cost, operability, reliability, security, and sustainability, on the other. Assign each criterion a weight and score every option. 

 Some decisions are one-way doors. Changes to a data store engine or core communication protocol are expensive to reverse and deserve deeper analysis than reversible configuration changes. Record significant decisions in an [Architectural Decision Record (ADR)](https://adr.github.io/) so you can revisit the context, alternatives, and reasoning. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify the competing requirements:** Document the performance requirements for your workload alongside the other non-functional requirements it must satisfy, such as cost ceilings, availability targets, and security controls. Note which requirements are fixed constraints and which are negotiable. 

1.  **Build a decision matrix:** Create a matrix to compare your options objectively. List candidate approaches on one axis and evaluation criteria on the other, assign a weight to each criterion based on its importance to your use case, and score each option against every criterion. 

1.  **Analyze the pillar trade-offs:** For each leading option, assess the effect on the other pillars: 
   +  **Cost:** regional footprint, scaling configuration, component count, and supply-and-demand balance. 
   +  **Operational excellence:** impact on observability and operational complexity. 
   +  **Reliability:** whether the pattern preserves simplicity and failure mitigation. 
   +  **Security:** whether it reduces controls or widens the attack surface. 

1.  **Decide and prioritize:** Choose the option that best serves the most critical requirements for your use case, accepting the compromises that choice implies on lower-priority criteria. Confirm the decision against your fixed constraints before committing. 

1.  **Record the decision:** Capture the choice, the alternatives considered, and the reasoning in an ADR so the trade-off is traceable and can be revisited. 

1.  **Review as conditions change:** Reassess your trade-offs on a cadence as business needs, traffic patterns, and available services evolve, and update the affected ADRs when a decision no longer holds. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF01-BP01 Validate requirements align to business needs](perf01-bp01.md) 
+  [PERF01-BP03 Derive and establish KPIs that validate adherence to your performance requirements](perf01-bp03.md) 
+  [PERF02-BP01 Select the best compute options for your workload](perf02-bp01.md) 

 **Related documents:** 
+  [Understand resiliency patterns and trade-offs to architect efficiently in the cloud](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/) 
+  [Using architectural decision records to streamline technical decision-making](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/introduction.html) 
+  [Architectural Decision Records](https://adr.github.io/) 