# OPS10-BP06 Communicate status through dashboards

Use dashboards as a strategic tool to convey real-time operational status and key metrics to different audiences, including internal technical teams, leadership, and customers. These dashboards offer a centralized, visual representation of system health and business performance, enhancing transparency and decision-making efficiency.

**Desired outcome:**

- Your dashboards provide a comprehensive view of the system and business metrics relevant to different stakeholders.
- Stakeholders can proactively access operational information, reducing the need for frequent status requests.
- Real-time decision-making is enhanced during normal operations and incidents.

**Common anti-patterns:**

- Engineers joining an incident management call require status updates to get up to speed.
- Relying on manual reporting for management, which leads to delays and potential inaccuracies.
- Operations teams are frequently interrupted for status updates during incidents.

**Benefits of establishing this best
practice:**

- Empowers stakeholders with immediate access to critical information, promoting informed decision-making.
- Reduces operational inefficiencies by minimizing manual reporting and frequent status inquiries.
- Increases transparency and trust through real-time visibility into system performance and business metrics.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Dashboards effectively communicate the status of your system and business metrics and can be tailored to the needs of different audience groups. Tools like Amazon CloudWatch dashboards and Amazon Quick Suite help you create interactive, real-time dashboards for system monitoring and business intelligence.

### Implementation steps

1. **Identify stakeholder needs:** Determine the specific information needs of different audience groups, such as technical teams, leadership, and customers.
2. **Choose the right tools:** Select appropriate tools like [Amazon CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") for system monitoring and [Amazon Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/") for interactive business intelligence. [AWS Health](../../../health/latest/ug/what-is-aws-health.md "../../../health/latest/ug/what-is-aws-health.md") provides a ready-to-use experience in the [AWS Health Dashboard](https://health.aws.amazon.com/health/home "https://health.aws.amazon.com/health/home"), or you can use Health events in Amazon EventBridge or through the AWS Health API to augment your own dashboards.
3. **Design effective dashboards:**
   - Design dashboards to clearly present relevant metrics and KPIs, ensuring they are understandable and actionable.
   - Incorporate system-level and business-level views as needed.
   - Include both high-level (for broad overviews) and low-level (for detailed analysis) dashboards.
   - Integrate automated alarms within dashboards to highlight critical issues.
   - Annotate dashboards with important metrics thresholds and goals for immediate visibility.

4. **Integrate data sources:**
   - Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to aggregate and display metrics from various AWS services and [query metrics from other data sources](../../../AmazonCloudWatch/latest/monitoring/MultiDataSourceQuerying.md "../../../AmazonCloudWatch/latest/monitoring/MultiDataSourceQuerying.md"), creating a unified view of your system's health and business metrics.
   - Use features like [CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") to query and visualize log data from different applications and services.
   - Use AWS Health events to stay informed about the operational status and confirmed operational issues from AWS services through the [AWS Health API](../../../health/latest/APIReference/Welcome.md "../../../health/latest/APIReference/Welcome.md") or [AWS Health events on Amazon EventBridge](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md").

5. **Provide self-service access:**
   - Share CloudWatch dashboards with relevant stakeholders for self-service information access using [dashboard sharing features](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md").
   - Ensure that dashboards are easily accessible and provide real-time, up-to-date information.

6. **Regularly update and refine:**
   - Continually update and refine dashboards to align with evolving business needs and stakeholder feedback.
   - Regularly review the dashboards to keep them relevant and effective for conveying the necessary information.

## Resources

**Related best practices:**

- [OPS08-BP05 Create dashboards](ops_workload_observability_create_dashboards.md "ops_workload_observability_create_dashboards.md")

**Related documents:**

- [Building dashboards for operational visibility](https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/ "https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/")
- [Using Amazon CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md")
- [Create flexible dashboards with dashboard variables](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.md")
- [Sharing CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md")
- [Query metrics from other data sources](../../../AmazonCloudWatch/latest/monitoring/MultiDataSourceQuerying.md "../../../AmazonCloudWatch/latest/monitoring/MultiDataSourceQuerying.md")
- [Add a custom widget to a CloudWatch dashboard](../../../AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard.md")

**Related examples:**

- [One Observability Workshop - Dashboards](https://catalog.us-east-1.prod.workshops.aws/workshops/31676d37-bbe9-4992-9cd1-ceae13c5116c/en-US/aws-native/dashboards "https://catalog.us-east-1.prod.workshops.aws/workshops/31676d37-bbe9-4992-9cd1-ceae13c5116c/en-US/aws-native/dashboards")
