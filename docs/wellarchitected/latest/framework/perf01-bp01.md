

# PERF01-BP01 Validate requirements align to business needs

 Performance efficiency depends on knowing what the business needs from a workload. When requirements are vague or assumed, teams optimize the wrong things and spend effort where it returns little value. A structured process to identify, document, validate, and manage performance requirements keeps engineering work aligned with business outcomes and gives every stakeholder a shared definition of fast enough. 

 **Desired outcome:** 
+  Your performance requirements are specific, measurable, and traced to a business objective. 
+  Your stakeholders agree on the requirements and share the same understanding of the performance the workload must deliver. 
+  Your requirements guide development priorities and provide objective criteria for judging whether the workload meets its goals. 
+  You review and update requirements as business needs change, and each requirement has a named owner. 

 **Common anti-patterns:** 
+  Teams apply the same performance requirements to every component, ignoring the distinct needs of each one. 
+  Teams state performance goals in qualitative terms without quantifiable targets that can be tested. 
+  Teams treat performance as an afterthought behind functional requirements rather than a core requirement. 
+  Teams gather requirements once and never revisit them as the business evolves. 

 **Benefits of establishing this best practice:** 
+  Development effort aligns with business priorities because each requirement traces to an objective. 
+  Measurable targets remove ambiguity and allow objective evaluation of workload performance. 
+  Documented, agreed requirements reduce conflict and misunderstanding among stakeholders. 
+  Clear acceptance criteria let teams confirm the workload meets its goals before release. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A performance requirement is a non-functional requirement that specifies how well a workload runs. A usable performance requirement names three things: a metric, a target value, and the condition under which the target applies. For example, The checkout page loads in under two seconds at the 95th percentile during peak traffic is testable. The checkout page is fast is not. 

 Stakeholders value performance differently: business owners focus on cost or conversion, engineers on technical feasibility. Gather input from every stakeholder, and validate each proposed target against technical feasibility before you commit to it. 

 Over-specifying performance has a cost. An aggressive latency target on a component that doesn't need one drives up spend, adds complexity, and diverts engineering time from higher-value work. Rank requirements by business impact so teams invest effort where performance affects the outcome, and accept looser targets where it does not. 

 Requirements drift as the business changes. Treat them as living artifacts with defined ownership and a change history, and update them when business direction shifts. Figure 1 shows an example process flow for validating requirements against business needs. <a name="perf01-bp01-fig1"></a>

![Flow diagram showing an iterative process for validating performance requirements against business needs.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/bp01.png)

*Example process for validating performance requirements against business needs*


### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify stakeholders and users:** List the business owners, project managers, developers, end users, and subject matter experts who have a stake in workload performance. Gather context from industry analysis, user feedback, and comparable workloads so that you understand what each group values before you write a single requirement. 

1.  **Define performance objectives:** Work with stakeholders to set high-level performance objectives that map to business goals and user experience expectations. Confirm each objective is technically feasible in your environment and budget before you refine it into a requirement. 

1.  **Gather measurable requirements:** Run interviews, workshops, or surveys to turn objectives into specific, testable requirements. Express each one as a metric, a target value, and the condition under which it applies, and avoid ambiguous language. 

1.  **Prioritize requirements and set acceptance criteria:** Rank requirements by business impact, urgency, and alignment with your objectives. Define the acceptance criteria that determine when each requirement is met, so evaluation is objective rather than a matter of opinion. 

1.  **Validate requirements:** Confirm each requirement is clear, measurable, and achievable. Plan experiments and performance tests that check the assumptions behind the targets, and adjust any requirement that testing shows to be unrealistic. 

1.  **Document, communicate, and manage change:** Record the validated requirements with their rationale, priority, acceptance criteria, constraints, and dependencies. Assign an owner to each, track changes across the workload lifecycle, and confirm that stakeholders understand and agree to the final set. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF01-BP02 Evaluate the trade-offs between performance and other non-functional requirements](perf01-bp02.md) 
+  [PERF01-BP03 Derive and establish KPIs that validate adherence to your performance requirements](perf01-bp03.md) 
+  [PERF01-BP04 Establish criteria for performance degradation alerts and tolerances](perf01-bp04.md) 

 **Related documents:** 
+  [A phased approach for performance engineering in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/introduction.html) 