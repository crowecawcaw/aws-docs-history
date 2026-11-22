

# OPS02-BP02 Create actionable insights with dashboards

 Use dashboards to give operators and stakeholders a shared, real-time view of system and business health. Dashboards complement alerts: alerts tell you when something breaks, and dashboards show you what is happening and why. 

 **Desired outcome:** 
+  Your dashboards present system health and business KPIs together, so viewers see technical state and its business impact in one place. 
+  Each of your dashboards has a clear audience and purpose, and shows only the metrics that audience needs to act. 
+  Your dashboards include context that lets a viewer interpret the data without prior knowledge, such as descriptions and links to related tools. 
+  You revise your dashboards as the workload changes, so they keep reflecting current architecture and priorities. 

 **Common anti-patterns:** 
+  Teams crowd a single dashboard with every available metric, which buries the few that matter. 
+  Organizations treat dashboards as a substitute for alerting and assume continuous human monitoring when a problem starts. 
+  Dashboards show technical counters with no business context, so non-engineers cannot tell whether anything is wrong. 
+  Teams build dashboards once and leave them unchanged as the workload evolves, until the views no longer match reality. 

 **Benefits of establishing this best practice:** 
+  Operators reach the state of the system quickly during an incident because the relevant signals are already arranged. 
+  Business stakeholders understand operational health without reading raw metrics or asking an engineer. 
+  A shared view shortens the time to agree on what is happening and what the impact is. 
+  Dashboards that pair KPIs with technical metrics show the business effect of an issue as it develops. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Design each dashboard for a specific audience, as the audience determines what data should be shown. An operator responding to a page needs latency, error rates, and saturation for a specific service, while a product owner needs the business KPIs that show whether customers are affected. A single dashboard cannot serve both audiences well. A workload typically needs several dashboards: customer experience, the system and its services, and infrastructure and dependencies. 

 An alert is a machine watching a threshold so a human doesn't have to. A dashboard is a human interpreting context a threshold cannot capture. Use alerts to catch defined failure conditions, and use dashboards to investigate, correlate, and communicate after an alert. 

 Every extra widget you add to a dashboard creates additional noise and competition for attention. Keep the dashboard focused, and only choose widgets that support a decision or an action. Include a short description of what the dashboard covers and links to related runbooks so a newcomer can interpret it. 

 Connect business outcomes on the dashboard to the technical signals connected to your metrics. When a business KPI dips, a viewer can follow the same dashboard down to the latency or error rate that explains it. Assign an owner to each dashboard so that it stays current. 

 [Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) provide customizable views of metrics, logs, and alarms on a single page, including resources across Regions and accounts. Because CloudWatch holds both infrastructure metrics and custom business metrics, you can build a layered view that ties a KPI to its technical drivers without switching tools. 

 CloudWatch provides [automatic dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingStarted.html) for the AWS services you use, and each service team builds its dashboard around the metrics that team considers most important. Use them directly, and treat those metric choices as a guide for your own dashboards. 

 When you enable [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html), it constructs service-level views from your trace data: the [Services page](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services-page.html) shows each service's RED metrics (rate, errors, and duration) and its service level objective status, and the [application map](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceMap.html) arranges your services as an interactive dashboard. The map groups services by tags or OpenTelemetry resource attributes, supports filtering from application tiles to individual service health, and can be set to an earlier time frame to examine a past state. Manually build dashboards for the business KPIs and layered views only you can define while Application Signals keeps the service views current. 

 For workloads instrumented with OpenTelemetry, you can use [CloudWatch Omni dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-dashboards.html) to arrange the service views discovered by Omni, explore query results, and trace views, alert status, and AI agent quality trends as panels on one shared page. You can also describe your desired dashboard in plain language and refine what the Omni agent builds. Omni dashboards are separate from CloudWatch dashboards, which continue to work unchanged. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define the audience and purpose:** Decide who each dashboard serves and what decision it supports before choosing metrics. Create separate dashboards for distinct audiences rather than combining them. Record the purpose so future editors keep the dashboard focused. 

1.  **Create the dashboard and add context:** [Create a dashboard in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html) with a descriptive name. Add [text widgets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-and-work-with-widgets.html) at the top that explain what the dashboard covers and link to related dashboards and troubleshooting tools. 

1.  **Add metric and KPI widgets:** Start from the [automatic dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingStarted.html) for each AWS service in the workload, both as a ready-made view and as a guide to which of that service's metrics matter most. Then [add metric widgets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-and-work-with-widgets.html) that show system health alongside the business KPIs the audience cares about. Arrange them so a viewer can move from a business signal to the technical metric that explains it, place the most important signals at the top, where they render first, and annotate graphs with their alarm thresholds and goals so a viewer can judge a value without remembering the target. Use [dashboard variables](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html) to make one dashboard serve several resources or environments. 

1.  **Adopt the service views built from trace data:** With Application Signals enabled, use the [application map](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceMap.html) and [Services page](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services-page.html) as the service-level dashboard, and group its tiles to match how your organization thinks about its applications. The [metrics beneath these views](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AppSignals-MetricsCollected.html) are ordinary CloudWatch metrics in the ApplicationSignals namespace, so a service's RED metrics can also sit on your hand-built dashboards, directly beside the business KPIs they explain. Reserve those hand-built dashboards for the business KPIs and layered views these pages cannot know about. For OpenTelemetry workloads monitored in CloudWatch Omni, save its service views and Explore queries as panels on an [Omni dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-dashboards.html) to view application and agent telemetry together. 

1.  **Surface insights from logs:** Use [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to derive metrics from log data and display them on the dashboard. Add [Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-ViewReports.html) to reveal the top contributors behind high-cardinality signals such as heavy callers or error sources. 

1.  **Show alarm state on the dashboard:** Add [alarm widgets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-and-work-with-widgets.html) so viewers see at a glance which metrics have breached their thresholds. This keeps the dashboard aligned with your alerting instead of duplicating it. When a widget surfaces an anomaly, you can start a [CloudWatch investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) from the metric or alarm behind it, so the follow-up begins where the signal appeared. 

1.  **Extend with custom and account-level views:** For needs that standard widgets do not meet, build [custom widgets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard.html) backed by your own data sources. Add the [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html) to track account events and planned changes that could affect your resources. 

1.  **Maintain dashboards as part of the workload:** Define dashboards as code, version them with the workload, and update them within the same change that alters the behavior they display, so a deployment never outruns its dashboards. Revisit each dashboard as the workload changes to confirm the metrics still match the architecture and priorities, and remove widgets that no longer drive a decision. When an incident review finds that a dashboard failed to show the impact or slowed the diagnosis, treat that as a dashboard defect and fix it alongside the code. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 
+  [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md) 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 
+  [OPS01-BP01 Develop application telemetry](ops01-bp01.md) 

 **Related documents:** 
+  [Building dashboards for operational visibility](https://builder.aws.com/content/3Ev2iw3R3ahQOM8BT4OUR0WP51z/building-dashboards-for-operational-visibility) 
+  [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) 
+  [View your application topology with the application map](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceMap.html) 
+  [Cross-account and cross-Region dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) 
+  [CloudWatch Omni dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-dashboards.html) 

 **Related examples:** 
+  [AWS Health Aware](https://github.com/aws-samples/aws-health-aware/) 
+  [Application Signals demo application](https://github.com/aws-observability/application-signals-demo) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US/intro) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 