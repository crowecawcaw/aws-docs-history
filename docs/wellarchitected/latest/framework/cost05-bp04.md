

# COST05-BP04 Select software with cost-effective licensing

 Software licenses can rival infrastructure as a share of workload cost. Licenses tied to fixed attributes such as processor cores penalize cloud elasticity, because you pay for capacity whether it produces value. Favor open-source options and licenses priced by usage or business outcome, so licensing cost scales with the value the software delivers. 

 **Desired outcome:** 
+  You optimize software licensing costs across the organization. 
+  Your licensing cost scales with the value the software delivers. 
+  You reduce exposure to licenses bound to arbitrary attributes such as processor count. 

 **Common anti-patterns:** 
+  Teams pick software on familiarity alone without weighing alternatives. 
+  Processor-based licenses are chosen without evaluating usage-based models. 
+  Open-source options for standard functionality go unexamined. 
+  Licensing terms are not reviewed for how they behave as the workload scales. 
+  Total cost of ownership is left out of licensing decisions. 
+  License utilization is never reviewed after the initial purchase. 

 **Benefits of establishing this best practice:** 
+  Overall software cost drops. 
+  Infrastructure design and scaling choices gain flexibility once licenses stop constraining them. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Licenses bound to processor cores or sockets block elasticity. Scale out to meet demand and license cost rises with the hardware, even when the extra capacity sits idle for most of the day. Licenses priced by usage or business outcome scale cost with the value produced. 

 [Open-source software](https://aws.amazon.com/what-is/open-source/) removes license fees, so prioritize it for standard functions. Mature open-source projects often match or exceed commercial equivalents for common needs. The trade-off moves from license cost to operational responsibility and support, so weigh the support model alongside the saved fees. 

 License selection is a total-cost decision. Commercial agreements carry terms that surface later, including audit clauses, penalties for over-deployment, and renewal increases that can reshape the economics after you've committed. Evaluate licensing terms, vendor track record, and the full cost of ownership before you choose, and include license cost in unit-economics calculations. For example, running a Linux-based instance instead of an equivalent Windows-based instance can cut cost for the same workload. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Document your current licensing portfolio:** Review existing licenses and record their costs, terms, and usage patterns. Identify where licensing cost does not align with business value or where arbitrary constraints limit scalability. Create a detailed inventory of commercial licenses and their terms, including audit clauses and the penalties they impose. 

1.  **Evaluate open-source alternatives:** Review the licensing terms of the software you use. Look for open-source versions that provide the required functionality, and judge whether the benefits of the licensed product outweigh its cost. Favorable terms align the cost of the software with the value it delivers. 

1.  **Analyze commercial licensing models:** Compare the licensing models available for the commercial software you need. Prioritize models that tie cost to actual usage or business outcomes, and confirm the terms are designed for cloud environments with pay-per-use billing. 

1.  **Implement license monitoring and management:** Track license usage, cost, and compliance with [AWS License Manager](https://aws.amazon.com/license-manager) or tooling from your software vendors. Establish review processes that keep licensing aligned with business needs and cost objectives, automate license management where possible, and record licensing decisions and their rationale. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST05-BP03 Analyze the total cost of ownership of each component](cost05-bp03.md) 
+  [COST05-BP05 Select components for business-value-driven cost optimization](cost05-bp05.md) 

 **Related documents:** 
+  [What is open source?](https://aws.amazon.com/what-is/open-source/) 
+  [Open Source at AWS](https://aws.amazon.com/opensource/) 

 **Related examples:** 
+  [AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/) 
+  [AWS Open Source](https://aws.github.io/) 
+  [Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/) 

 **Related services:** 
+  [AWS License Manager](https://aws.amazon.com/license-manager) 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 