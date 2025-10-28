# Expenditure and usage awareness

The increased flexibility and agility that the cloud provides encourages innovation and
fast-paced development and deployment. It decreases the manual processes and time
associated with provisioning on-premises infrastructure, including identifying hardware
specifications, negotiating price quotations, managing purchase orders, scheduling
shipments, and then deploying the resources. However, the ease of use and virtually
unlimited on-demand capacity requires a new way of thinking about expenditures.

Many businesses are composed of multiple systems run by various
teams. The capability to attribute resource costs to the
individual organization or product owners drives efficient usage
behavior and helps reduce waste. Accurate cost attribution permits
you to know which products are truly profitable, and permits you to
make more informed decisions about where to allocate budget.

In AWS, you create an account structure with AWS Organizations or
AWS Control Tower, which provides separation and assists in
allocation of your costs and usage. You can also use resource
tagging to apply business and organization information to your
usage and cost. Use AWS Cost Explorer for visibility into your
cost and usage, or create customized dashboards and analytics with
Amazon Athena and Amazon QuickSight. Controlling your cost and
usage is done by notifications through AWS Budgets, and controls
using AWS Identity and Access Management (IAM), and Service Quotas.

The following questions focus on these considerations for cost
optimization.

| COST 2:  How do you govern usage?                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Establish policies and mechanisms to validate that appropriate costs are incurred while objectives are achieved. By employing a checks-and-balances approach, you can innovate without overspending. |
| COST 3:  How do you monitor usage and cost?                                                                                                                                                          |
| ---                                                                                                                                                                                                  |
| Establish policies and procedures to monitor and appropriately allocate your costs. This permits you to measure and improve the cost efficiency of this workload.                                    |
| COST 4:  How do you decommission resources?                                                                                                                                                          |
| ---                                                                                                                                                                                                  |
| Implement change control and resource management from project inception to end-of-life. This facilitates shutting down unused resources to reduce waste.                                             | You can use cost allocation tags to categorize and track your AWS usage and costs. When you apply tags to your AWS resources (such as EC2 instances or S3 buckets), AWS generates a cost and usage report with your usage and your tags. You can apply tags that represent organization categories (such as cost centers, workload names, or owners) to organize your costs across multiple services. Verify that you use the right level of detail and granularity in cost and usage reporting and monitoring. For high level insights and trends, use daily granularity with AWS Cost Explorer. For deeper analysis and inspection use hourly granularity in AWS Cost Explorer, or Amazon Athena and Amazon Quick Suite with the Cost and Usage Report (CUR) at an hourly granularity. Combining tagged resources with entity lifecycle tracking (employees, projects) makes it possible to identify orphaned resources or projects that are no longer generating value to the organization and should be decommissioned. You can set up billing alerts to notify you of predicted overspending. |
