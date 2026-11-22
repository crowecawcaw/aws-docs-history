

# COST05-BP03 Analyze the total cost of ownership of each component

 A component's total cost includes more than its list price. Running it yourself adds operational work: patching, scaling, monitoring, incident response, and the staff hours to do it. Count these hidden costs when you compare managed and self-managed options, so the comparison reflects the real total. 

 **Desired outcome:** 
+  You understand the true cost of each component, including operational and management overhead. 
+  Your decisions between managed and self-managed options rest on total cost of ownership. 
+  Your resource allocation reflects the full cost of running each component, not only its infrastructure price. 

 **Common anti-patterns:** 
+  Teams count only direct infrastructure cost and ignore operational expense. 
+  Analysis omits the staff capacity and management overhead a component consumes. 
+  Managed alternatives are never evaluated against the self-managed option. 
+  Decisions rest on immediate savings while long-term operational cost is overlooked. 
+  The effect on team productivity and innovation capacity is left out of the comparison. 

 **Benefits of establishing this best practice:** 
+  Total operational cost falls as hidden expenses become visible and manageable. 
+  Managed services offload administrative burden so teams focus on differentiating work. 
+  Technical decisions align with business objectives because the full cost is known. 
+  Operational costs become more predictable. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Total cost of ownership is a component's infrastructure price plus its operational and management effort. Engineers who patch operating systems, tune databases, or respond to incidents aren't building differentiating features. Managed services shift much of that work to the provider. Once you count the hours returned to your team, a managed option can cost less than a self-managed one at a higher list price. Managed services also run at cloud scale, so they can lower cost per transaction without application changes. 

 Serverless and consumption-priced services reduce the need to size capacity or patch, and you pay only for what you use. That removes most operational overhead and shifts the cost question to usage. Request volume, duration, and throughput drive the bill, so your total-cost analysis has to include how those scale. 

 Managed services reduce your control and constrain workload tuning. Weigh those limits against the operational savings. Rehosting a database quickly and optimizing later can cost less than a slow migration to the lowest-cost end state. 

 Managed services still need tuning. Most expose capacity attributes. Leaving them at defaults produces idle spend or performance problems. Set and monitor these attributes to keep excess capacity low and performance stable. Wire the adjustments into a monitoring tool such as Amazon CloudWatch so the service tracks demand automatically. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish each component's total cost of ownership:** Starting from the prioritized component list in [COST05-BP02 Analyze all components of the workload](cost05-bp02.md), add the operational and management effort to each component's infrastructure price, including patching, scaling, monitoring, and incident response, along with the staff time they consume. This full-cost baseline is what the managed-versus-self-managed comparison rests on. 

1.  **Compare managed and self-managed options:** Create standardized metrics so managed and self-managed services are compared on the same terms. For example, weigh a database on [Amazon EC2](https://aws.amazon.com/ec2/) against [Amazon RDS](https://aws.amazon.com/rds/), or [Apache Spark on Amazon EC2](https://aws.amazon.com/emr/features/spark/) against [Amazon EMR](https://aws.amazon.com/emr/). When moving to a fully managed service, research the [type of managed service](https://aws.amazon.com/products/?&aws-products-all.q=managed) you want, the process to [migrate your data](https://aws.amazon.com/big-data/datalakes-and-analytics/migrations/), and the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). 

1.  **Evaluate operational impact:** Assess the operational requirements of each option, including maintenance, monitoring, and the expertise it demands. Calculate the true cost of operations by including incident response, updates, security management, and compliance. Weigh the effect on team capacity and the ability to focus on core business objectives. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST05-BP02 Analyze all components of the workload](cost05-bp02.md) 
+  [COST05-BP05 Select components for business-value-driven cost optimization](cost05-bp05.md) 
+  [COST06-BP04 Consider using shared resources](cost06-bp04.md) 

 **Related documents:** 
+  [AWS Pricing Calculator](https://calculator.aws/#/) 
+  [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) 