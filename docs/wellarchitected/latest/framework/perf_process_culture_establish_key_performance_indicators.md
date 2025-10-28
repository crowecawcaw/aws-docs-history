# PERF05-BP01 Establish key performance indicators (KPIs) to

measure workload health and performance

Identify the KPIs that quantitatively and qualitatively measure
workload performance. KPIs help you measure the health and
performance of a workload related to a business goal.

**Common anti-patterns:**

- You only monitor system-level metrics to gain insight into your
  workload and don’t understand business impacts to those metrics.
- You assume that your KPIs are already being published and shared
  as standard metric data.
- You do not define a quantitative, measurable KPI.
- You do not align KPIs with business goals or strategies.

**Benefits of establishing this best
practice:** Identifying specific KPIs that represent
workload health and performance helps align teams on their
priorities and define successful business outcomes. Sharing those
metrics with all departments provides visibility and alignment on
thresholds, expectations, and business impact.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

KPIs allow business and engineering teams to align on the
measurement of goals and strategies and how these factors combine
to produce business outcomes. For example, a website workload
might use page load time as an indication of overall performance.
This metric would be one of multiple data points that measures user experience. In addition to identifying the page load time
thresholds, you should document the expected outcome or business
risk if ideal performance is not met. A long page load time
affects your end users directly, decreases their user experience
rating, and can lead to a loss of customers. When you define your
KPI thresholds, combine both industry benchmarks and your end user
expectations. For example, if the current industry benchmark is a
webpage loading within a two-second time period, but your end
users expect a webpage to load within a one-second time period,
then you should take both of these data points into consideration
when establishing the KPI.

Your team must evaluate your workload KPIs using real-time
granular data and historical data for reference and create
dashboards that perform metric math on your KPI data to derive
operational and utilization insights. KPIs should be documented
and include thresholds that support business goals and strategies,
and should be mapped to metrics being monitored. KPIs should be
revisited when business goals, strategies, or end user
requirements change.  

## Implementation steps

- **Identify stakeholders:** Identify and document key business stakeholders, including development and operation teams.
- **Define objectives:**
  Work with these stakeholders to define and document objectives
  of your workload. Consider the critical performance aspects of your workloads, such as throughput, response time, and cost, as well as business goals, such as user satisfaction.
- **Review industry best practices:**
  Review industry best practices to identify relevant KPIs
  aligned with your workload objectives.
- **Identify metrics:** Identify metrics that are aligned with your workload objectives and can help you measure performance and business goals. Establish KPIs based on these metrics. Example metrics are measurements like average response time or number of concurrent users.
- **Define and document KPIs:**
  Use industry best practices and your workload objectives to
  set targets for your workload KPI. Use this information to set
  KPI thresholds for severity or alarm level. Identify and document the risk and impact of a KPI is not met.
- **Implement monitoring:**
  Use monitoring tools such as
  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") or
  [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") to collect metrics and measure KPIs.
- **Visually communicate KPIs:**
  Use dashboard tools like [Amazon Quick Suite](https://aws.amazon.com/pm/quicksight/ "https://aws.amazon.com/pm/quicksight/") to visualize and communicate KPIs with
  stakeholders.
- **Analyze and optimize:**
  Regularly review and analyze KPIs to identify areas of your
  workload that need to be improved. Work with stakeholders to implement these improvements.
- **Revisit and refine:**
  Regularly review metrics and KPIs to assess their effectiveness, especially when business goals or workload performance change.

## Resources

**Related documents:**

- [CloudWatch
  documentation](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
- [Monitoring,
  Logging, and Performance AWS Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance "https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance")
- [AWS observability tools](../management-and-governance-guide/aws-observability-tools.md "../management-and-governance-guide/aws-observability-tools.md")
- [The Importance of Key Performance Indicators (KPIs) for Large-Scale Cloud Migrations](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/ "https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/")
- [How to track your cost optimization KPIs with the KPI Dashboard](https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-track-your-cost-optimization-kpis-with-the-kpi-dashboard/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-track-your-cost-optimization-kpis-with-the-kpi-dashboard/")
- [X-Ray
  Documentation](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md")
- [Using
  Amazon CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md")
- [Quick Suite KPIs](../../../quicksight/latest/user/kpi.md "../../../quicksight/latest/user/kpi.md")

**Related videos:**

- [AWS re:Invent 2023 - Optimize cost and performance and track progress toward mitigation](https://www.youtube.com/watch?v=keAfy8f84E0 "https://www.youtube.com/watch?v=keAfy8f84E0")
- [AWS re:Invent 2023 - Manage resource lifecycle events at scale with AWS Health](https://www.youtube.com/watch?v=VoLLNL5j9NA "https://www.youtube.com/watch?v=VoLLNL5j9NA")
- [AWS re:Invent 2023 - Performance & efficiency at Pinterest: Optimizing the latest instances](https://www.youtube.com/watch?v=QSudpowE_Hs "https://www.youtube.com/watch?v=QSudpowE_Hs")
- [AWS re:Invent 2022 - AWS optimization: Actionable steps for immediate results](https://www.youtube.com/watch?v=0ifvNf2Tx3w "https://www.youtube.com/watch?v=0ifvNf2Tx3w")
- [AWS re:Invent 2023 - Building an effective observability strategy](https://www.youtube.com/watch?v=7PQv9eYCJW8 "https://www.youtube.com/watch?v=7PQv9eYCJW8")
- [AWS Summit SF 2022 - Full-stack observability and application monitoring with AWS](https://www.youtube.com/watch?v=or7uFFyHIX0 "https://www.youtube.com/watch?v=or7uFFyHIX0")
- [AWS re:Invent 2023 - Scaling on AWS for the first 10 million users](https://www.youtube.com/watch?v=JzuNJ8OUht0 "https://www.youtube.com/watch?v=JzuNJ8OUht0")
- [AWS re:Invent 2022 - How Amazon uses better metrics for improved website performance](https://www.youtube.com/watch?v=_uaaCiyJCFA "https://www.youtube.com/watch?v=_uaaCiyJCFA")
- [Creating an Effective Metrics Strategy for Your Business | AWS Events](https://www.youtube.com/watch?v=zBO-K4RvbtM "https://www.youtube.com/watch?v=zBO-K4RvbtM")

**Related examples:**

- [Creating
  a dashboard with Quick Suite](https://github.com/aws-samples/amazon-quicksight-sdk-proserve "https://github.com/aws-samples/amazon-quicksight-sdk-proserve")
