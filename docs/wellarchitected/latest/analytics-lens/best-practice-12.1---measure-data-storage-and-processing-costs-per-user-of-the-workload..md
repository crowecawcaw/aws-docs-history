# Best practice 12.1 – Measure data storage and processing costs per user of the workload

Data analytics workloads have recurring stable costs and
per-use costs, for example, a weekly reporting job with
relatively static data storage fees or periodic
unpredictable processing runtime fees. Your organization
should establish a financial attribution mechanism that
captures data storage and workload usage when analytics
systems are run. Using this approach, your end users
(business unit, team, or individual) can be notified of their
consumption at regular intervals.

## Suggestion 12.1.1 – Use tagging or other attribution methods to identify workload and data storage ownership

Collaboration between business, IT, and finance team to
agree on cost allocation, cost ownership, cost charging,
and budget management. Create budget tracking policy for
storage and workload using tagging. Agree on the
governance approach to implement policy (that is, central
and decentralize), billing allocation, charge back, and
budget reporting.

For more details, refer to the following information:

- AWS Cloud Financial Management Blog: Cost
  [Tagging
  and Reporting with AWS Organizations](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-tagging-and-reporting-with-aws-organizations/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-tagging-and-reporting-with-aws-organizations/")
- AWS Billing and Cost Management and Cost Management User Guide:
  [Reporting
  your budget metrics with budget reports](../../../cost-management/latest/userguide/reporting-cost-budget.md "../../../cost-management/latest/userguide/reporting-cost-budget.md"),
  [Configuring
  AWS Budgets actions](../../../cost-management/latest/userguide/budgets-controls.md "../../../cost-management/latest/userguide/budgets-controls.md") and
  [Creating
  an Amazon SNS topic for budget notifications](../../../cost-management/latest/userguide/budgets-sns-policy.md "../../../cost-management/latest/userguide/budgets-sns-policy.md")

## Suggestion 12.1.2 – Implement cost-visibility and internal bill-back method to aggregate your teams' use of analytics resources

Notify teams of their analytics usage costs periodically. Build dashboards that provide teams visibility into how their work impacts costs to the business using a self-service approach.

You can view and optimize your costs through the AWS Cost and Usage Report and the Cost and Usage Dashboards Operations Solution (CUDOS) reports.
