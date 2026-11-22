

# FND06-BP05 Establish organizational metrics to track optimization efforts

 Implement organization-wide metrics, goals, and tracking mechanisms to measure and optimize cloud spending across your accounts. This includes establishing standardized key performance indicators (KPIs), implementing full monitoring and reporting frameworks, and creating feedback loops for continuous optimization. 

 **Desired outcome:** 
+  You have standardized cost optimization metrics across the organization that provide clear visibility into cost optimization progress and trends. 

 **Common anti-patterns:** 
+  Lacking standardized KPIs across accounts in an organization and missing organization-wide visibility into optimization efforts. 
+  Using inconsistent measurement methodologies and not establishing common baselines before optimization efforts. 
+  Focusing solely on technical or cost metrics without correlating them with business context and outcomes. 
+  Implementing tracking and cost visibility without clear goals and targets. 

 **Benefits of establishing this best practice:** 
+  Better visibility into organization-wide cost optimization improves the ability to demonstrate optimization ROI and supports better alignment between technical and business metrics. 
+  Data-driven decision making through full metrics helps identify optimization opportunities and prioritize efforts based on potential impact. 
+  Improved stakeholder communication and engagement results from clear, consistent metrics that connect cloud costs to business outcomes and show optimization progress. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A metrics framework must serve different stakeholders without losing consistency: executive-level KPIs for leaders, detailed technical metrics for foundation teams, and business outcome metrics for product owners. Every workload produces an output that matters to the business (transactions, active users, or features delivered). Cost per business output is the best measure of cost efficiency. 

 Goals and targets for your organization's [key performance indicators](https://aws.amazon.com/blogs/aws-cloud-financial-management/measuring-cloud-cost-efficiency-with-the-new-cost-efficiency-metric-by-aws/) make efficiency improvements visible over time. Examples include the percent of spend on On-Demand, adoption of optimized services such as AWS Graviton instances or gp3 EBS volumes, or a rule that every significant cloud usage increase produces only a minor, non-linear cost increase. A concrete target might be a 20 percent increase in cloud usage with less than a 5 percent increase in costs, or a 5 percent efficiency improvement every six months. Start with a manageable set and expand it as your organization matures. 

 *Cost efficiency* captures how well you use what you've paid for: commitment coverage, resource utilization, modernization rates (Graviton, gp3), unused resource costs, tag compliance, and cost per organizational unit. *Optimization progress* tracks how quickly you improve: cost reduction from optimization initiatives, time to implement recommendations, and cost anomaly response times. *Business value* connects spend to outcomes: cost per customer, revenue per cloud dollar, cost per transaction, cost per feature, innovation spend compared with operational spend, and return on cloud investment. Smaller organizations start with efficiency metrics and add business value metrics as FinOps practices mature. Larger enterprises need the full spectrum, differentiated by business unit. 

**Important**  
 Define clear responsibility for each metric category and match review cadences to purpose: weekly for operational metrics, monthly for optimization progress, and quarterly for strategic KPIs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select KPIs that connect cloud spending to business outcomes:** Work with finance, engineering, and business stakeholders to define KPIs that measure both cost efficiency and business value. Start with a manageable set and evolve as your organization matures. The following table provides example KPIs as a starting point: 


<table>
<thead>
  <tr><th> Category </th><th> KPI </th><th> Target Range </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td> Financial efficiency </td><td> Budget variance </td><td> ±5% </td><td> Variance between actual spend and planned budget </td></tr>
  <tr><td> Business value </td><td> Revenue per cloud dollar </td><td> &gt;3x </td><td> Revenue generated relative to cloud costs </td></tr>
  <tr><td> Operational efficiency </td><td> Resource utilization rate </td><td> &gt;70% </td><td> Effective use of provisioned resources </td></tr>
  <tr><td> Cost optimization </td><td> Optimization implementation rate </td><td> &gt;80% </td><td> Percentage of implemented cost optimization recommendations </td></tr>
  <tr><td> Risk management </td><td> Cost anomaly response time </td><td> &lt;4 hours </td><td> Time to respond to cost anomalies </td></tr>
  <tr><td> Governance </td><td> Tag compliance rate </td><td> &gt;95% </td><td> Resources properly tagged for cost allocation </td></tr>
  <tr><td> Modernization </td><td> Graviton adoption rate </td><td> &gt;30% </td><td> Workloads running on AWS Graviton processors </td></tr>
</tbody>
</table>


1.  **Configure AWS tools to track your KPIs:** Set up [AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/) to track costs by business context, and implement [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) aligned with your organizational structure. Create [Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) monitors for each major cost category so unexpected spending is flagged early. Consider implementing custom metrics using [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and the [KPI and Modernization Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/cudos-cid-kpi.html) from the AWS Cloud Intelligence Dashboard solutions. 

1.  **Deploy organization-wide monitoring and visibility:** Turn on [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) with hourly granularity to provide the raw data your KPIs depend on. Use [AWS Organizations](https://aws.amazon.com/organizations/) features for a consolidated view across all accounts. Turn on [AWS Config](https://aws.amazon.com/config/) with organization-wide rules to monitor tag policy compliance, track resource configurations, and automate compliance reporting. Implement [AWS Resource Explorer](https://aws.amazon.com/resourceexplorer/) for cross-Region resource visibility. Create custom dashboards tailored to different stakeholder groups. 

1.  **Assign metrics ownership and accountability:** Define clear ownership for each metric category so there is no ambiguity about who is responsible for tracking, reporting, and acting on results. Executive leadership owns strategic KPIs (cost to revenue ratio, return on cloud investment (ROCI)), the FinOps or Cloud Center of Excellence team owns operational metrics (commitment coverage, optimization rates), foundation teams own technical metrics (resource utilization, modernization adoption), and business units own business outcome metrics (cost per customer, feature delivery efficiency). Create [RACI matrices](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/) for metrics management, define escalation paths for metric violations, and establish ownership of the metric review and refinement process itself. 

1.  **Automate reporting and distribution:** Build automated reporting workflows using [AWS Quick](https://aws.amazon.com/quick/) and the [Cloud Intelligence Dashboards](https://docs.aws.amazon.com/solutions/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws/) that deliver the right level of detail to each audience. Create executive-level summaries that surface optimization progress and trends. Generate regular optimization recommendation reports for engineering teams that include specific actions and estimated savings. Configure automated distribution through email or integrated dashboards so reports reach stakeholders on a predictable cadence without manual effort. 

1.  **Establish feedback loops for continuous improvement:** Set up a structured review cadence: weekly operational reviews with foundation teams, monthly business unit performance reviews, quarterly executive business reviews (QBRs), and annual strategic planning and target setting. Include one-off reviews triggered by cost anomalies or significant changes. Integrate these reviews with existing operational processes so cost optimization becomes part of how teams already work, not a separate activity. Establish feedback channels for optimization initiatives and track performance against established targets to close the loop between measurement and action. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND06-BP02 Standardize cost attribution categories](fnd06-bp02.md) 
+  [FND06-BP03 Configure billing and cost management tools](fnd06-bp03.md) 
+  [FND06-BP06 Build strategies for commitment discounts and volume-based pricing](fnd06-bp06.md) 

 **Related documents:** 
+  [Measuring Cloud Cost Efficiency with the New Cost efficiency metric by AWS](https://aws.amazon.com/blogs/aws-cloud-financial-management/measuring-cloud-cost-efficiency-with-the-new-cost-efficiency-metric-by-aws/) 
+  [KPIs – Enterprise Journey from Technology to Business](https://aws.amazon.com/blogs/mt/kpis-enterprise-journey-from-technology-to-business/) 

 **Related workshops:** 
+  [The KPI and Modernization Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/cudos-cid-kpi.html) 