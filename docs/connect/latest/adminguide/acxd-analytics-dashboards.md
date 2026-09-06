

# Analytics dashboards
<a name="acxd-analytics-dashboards"></a>

Analytics dashboards help you view, organize, and monitor performance data for deployed agentic CX designer applications.

Review dashboards to understand how users are interacting with your conversational AI applications, whether flows are performing as expected, where users may be dropping off, and whether integrations or response times may be affecting the experience.

Analytics dashboards can help you:
+ Monitor application health and user behavior
+ Review conversation volume and traffic trends
+ Evaluate flow recognition and user experience
+ Track Data request performance and response time
+ Monitor analytics tags tied to key milestones
+ Identify drop-off points or opportunities for improvement
+ Compare performance before and after flow changes or A/B tests

Analytics dashboards can be reviewed from a deployed application's **Observe** tab.

After an application has been deployed for the first time, the **Observe** tab becomes available. From there, you can review predefined dashboard views that surface common performance metrics for that application.

You can also create custom analytics dashboards for metrics, panels, filters, and views that matter most to your team.

## Predefined dashboard views
<a name="acxd-analytics-dashboards-predefined"></a>

The **Observe** tab includes predefined analytics dashboard views to help you begin monitoring immediately after deployment.

Use the dropdown at the top of the Observe page to switch between dashboard views.

The default views include:


|  |  | 
| --- |--- |
| **Overview** | General application usage, conversation volume, traffic, and high-level outcomes. | 
| **Understanding** | How well the application understands users, invokes flows, and responds to common phrases. | 
| **Integrations** | Data request usage, success rates, response times, and technical performance indicators. | 

These dashboards provide a quick starting point for understanding deployed application health.

## Custom dashboards
<a name="acxd-analytics-dashboards-custom"></a>

Predefined dashboards provide a useful starting point, but you can also create custom analytics dashboards for your team's specific reporting needs.

Custom dashboards let you choose:
+ Metrics
+ Chart types
+ Filters
+ Aggregations
+ Date ranges
+ Analytics tags
+ Visibility settings

Use custom dashboards when your team needs to track specific milestones, flow outcomes, integration health, or business KPIs that are not fully covered by the predefined Observe views.

**To create a custom analytics dashboard**

1. Open **Analytics**.

1. Select **Create dashboard**.

1. Enter a dashboard name > choose visibility.

1. Choose a predefined template or start from a blank dashboard.

1. Add or edit chart panels.

1. Configure each panel with a chart type, metric, aggregation, and filters.

1. Save the dashboard.

A dashboard can contain one or more panels. Each panel tracks a specific metric or visualization.

Dashboards include two visibility settings.


|  |  | 
| --- |--- |
| **Private** | Visible only to the dashboard creator. | 
| **Public** | Visible to other users who have access to the workspace. | 

Use private dashboards for personal analysis or draft reporting. Use public dashboards for shared team monitoring.

**Important**  
If a dashboard is made public, it cannot be reverted to private later.

## Charts
<a name="acxd-analytics-dashboards-charts"></a>

A chart is an individual visualization inside a dashboard.

Each chart can be configured to show a metric in a specific format. For example, one chart may show total conversations over time, while another may show Data request response time or the number of conversations that reached a tagged node.

When configuring a chart, you may define:


|  |  | 
| --- |--- |
| **Title** | The title shown on the dashboard. | 
| **Description** | A short explanation of what the panel tracks. | 
| **Chart type** | The visual format used to display the metric. | 
| **Metric** | The data being measured. | 
| **Aggregation** | How the data is calculated, such as sum, average, minimum, or maximum. | 
| **Filters** | Conditions used to include or exclude specific data. | 
| **Time interval** | How data is grouped over time, when applicable. | 

Different chart types are useful for different kinds of data.


|  |  | 
| --- |--- |
| **Scorecard** | Shows a single number, such as total conversations. | 
| **Gauge** | Shows a value against a defined range. | 
| **Pie chart** | Shows proportions across a group. | 
| **Bar chart** | Compares values across categories or time intervals. | 
| **Line chart** | Shows trends over time. | 
| **Box plot** | Shows distribution, such as minimum, maximum, and median values. | 
| **Table** | Shows one or more metrics in rows and columns. | 
| **Funnel** | Shows how users move through staged steps or filtered conditions. | 

Some metrics are only compatible with certain chart types. If the metric you want is unavailable, try selecting a different chart type.

## Metrics
<a name="acxd-analytics-dashboards-metrics"></a>

Analytics dashboards can surface many types of metrics.

Common examples include:


|  |  | 
| --- |--- |
| **Conversation metrics** | Conversations, users, messages, messages per conversation, time spent per conversation. | 
| **Flow metrics** | Flows invoked, flows detected, confidence score, phrase occurrences, phrase trends. | 
| **Node metrics** | Time spent per flow, time spent per node, tagged milestones, completion or drop-off indicators. | 
| **Integration metrics** | Data requests invoked, percentage of successful Data requests, Data request response time. | 
| **Knowledge base metrics** | Knowledge base invoked, knowledge base confidence score, knowledge base response time. | 

Use the metric that most directly answers the question you are trying to investigate.

Aggregations determine how a metric is calculated.

For example, use Sum to count total conversations and Average to review average response time.


|  |  | 
| --- |--- |
| **Sum** | Total value. | 
| **Average** | Mean value. | 
| **Minimum** | Lowest value. | 
| **Maximum** | Highest value. | 
| **Median** | Middle value, when supported. | 

## Filters
<a name="acxd-analytics-dashboards-filters"></a>

Filters help include or exclude specific data from a chart.

Use filters to focus on a subset of conversations, such as:
+ One application
+ One channel
+ One flow
+ One language
+ One region
+ One Data request
+ One analytics tag
+ One date range
+ One status, such as successful or failed requests

When adding multiple filter values, settings such as **Any** or **All** may be available.


|  |  | 
| --- |--- |
| **Any** | Data is included if at least one selected filter value is present. | 
| **All** | Data is included only if every selected filter value is present. | 

Filters are useful when you want to compare specific experiences or remove unrelated data from a chart.

## Formulas
<a name="acxd-analytics-dashboards-formulas"></a>

Analytics dashboards can do more than display one metric at a time. For more advanced reporting, you can use formulas, multi-metric panels, and external analytics to calculate custom values, compare related trends, or bring in data from another system.

Use these options when a single metric does not fully answer the question you are trying to investigate.

Formulas let you transform or combine existing metrics into a new calculated metric.

Use formulas when you need to:
+ Convert values, such as seconds to milliseconds
+ Calculate percentages or rates
+ Compare two filtered metrics
+ Combine multiple datasets into one value
+ Create a custom KPI for your team

For example, you could calculate a completion rate by comparing conversations that reached a "task\_completed" analytics tag against conversations that reached a "task\_started" tag.

**To add a formula**

1. Create or edit a dashboard.

1. Add or edit a chart.

1. Choose a supported chart type, such as Scorecard, Line, or Bar.

1. Add one or more datasets or data columns.

1. Select **Add formula**.

1. Enter a name for the calculated metric.

1. In the **Formula** field, enter the expression you want to calculate.

1. To reference an existing metric, type an opening curly bracket { and choose from the available metrics.

1. Choose a **Display unit**, such as percentage, seconds, or another available display unit.

1. Save the panel.

Supported formula operations may include basic arithmetic, such as addition, subtraction, multiplication, and division, as well as common math functions such as absolute value, square root, ceiling, floor, and power.

**Important**  
A calculated metric cannot be referenced inside another formula.

## Multi-metric panels
<a name="acxd-analytics-dashboards-multi-metric"></a>

Multi-metric panels let you compare more than one dataset in the same chart.

Use multi-metric panels when you want to compare related trends side by side instead of creating separate panels for each metric.

Examples include:
+ Chat conversations vs. voice conversations
+ Successful Data requests vs. failed Data requests
+ Booking started vs. booking completed
+ Escalation requested vs. escalation completed

**To create a multi-metric panel**

1. Create or edit a dashboard.

1. Add or edit a chart.

1. Choose a supported chart type, such as Line, Bar, or Table.

1. Select **Add dataset** > Name the first dataset.

1. Choose the metric, aggregation, time interval, and filters for that dataset.

1. Select **Add dataset** again > Name the second dataset.

1. Choose the metric, aggregation, time interval, and filters for the second dataset.

1. Repeat as needed for additional datasets.

1. Save the panel.

## External analytics
<a name="acxd-analytics-dashboards-external"></a>

External analytics lets you display data from an external source inside an analytics dashboard.

Use external analytics when your team needs to compare agentic CX designer conversation metrics with data from another system, such as business reporting, operational data, or an internal service.

External data is available through the Table chart type.

**To add external analytics data**

1. Create or edit a dashboard.

1. Add or edit a chart.

1. Set the chart type to **Table**.

1. Choose **External** as the data source.

1. Select **URL** as the type.

1. Enter the endpoint URL.

1. Add any required headers.

1. Mark sensitive values appropriately so they are redacted where supported.

1. Save the panel.

The external endpoint must return a status code and a string body containing the data.

Example response:

```
{
  statusCode: 200,
  body: JSON.stringify("one,two\n1,2\n3,4\n5,6")
}
```

You can also use placeholders in the URL field to pass the dashboard's selected time range to your endpoint:
+ {startTimestampExtended}
+ {endTimestampExtended}

Use these placeholders when the external data source should return results for the same time window selected in the dashboard.

When using external analytics, follow your organization's security requirements for endpoint access, authentication, headers, and sensitive values.