

# Analytics dashboard
<a name="analytics"></a>

The analytics dashboard provides operational visibility into your AI agent performance and business impact. You can view key performance indicators (KPIs), track trends over time, and export detailed task metrics for further analysis.

![The analytics dashboard showing KPI summary cards and charts](http://docs.aws.amazon.com/connecthealth/latest/userguide/images/full-dashboard.png)


## Viewing the analytics dashboard
<a name="viewing-analytics"></a>

To access the analytics dashboard, choose **Analytics** in the console sidebar navigation.

## KPI summary cards
<a name="analytics-kpi-cards"></a>

The dashboard displays four KPI summary cards at the top of the page. These cards provide a high-level overview of AI agent activity for the selected date range.
+  **Human hours saved** – The estimated staff hours saved through AI automation.
+  **Tasks handled** – The total number of AI agent interactions in the selected period.
+  **Task containment rate** – The percentage of tasks resolved without transferring to a human agent.
+  **Task escalation rate** – The percentage of tasks that required escalation to a human agent.

## Charts
<a name="analytics-charts"></a>

The dashboard includes the following charts to help you analyze AI agent performance trends:
+  **Task containment rate** – A line chart that shows the containment rate over time.
+  **Tasks handled** – A bar chart that shows daily task volume.
+  **Task escalation volume** – A bar chart that shows the number of escalated tasks over time.
+  **Task escalation rate** – A line chart that shows the escalation rate over time.
+  **Why tasks escalate** – A donut chart that breaks down escalations by reason.
+  **AI usage by type** – A donut chart that shows the distribution of AI usage across types.
+  **Intent distribution** – A horizontal bar chart that shows task volume by detected intent.
+  **Intent containment rate** – A horizontal bar chart that shows the percentage of tasks resolved per intent.

## Filtering by date range
<a name="analytics-date-range"></a>

You can filter all dashboard data by date range. Choose from the following presets:
+ Last 7 days
+ Last 14 days
+ Last 30 days

You can also specify a custom relative range in days or weeks, or select an absolute date range. The following limits apply:
+ The maximum date range is 30 days.
+ The start date must be within the last 90 days.

![The date range picker showing date range options](http://docs.aws.amazon.com/connecthealth/latest/userguide/images/relative-date-view.png)


## Exporting task metrics
<a name="analytics-export"></a>

To export task metrics, choose **Export AI task metrics**. The dashboard downloads a CSV file with the following columns:
+ Timestamp
+ Agent Session
+ Agent Type
+ Intent
+ Status
+ Escalation Reason
+ Duration (ms)

You can use the exported data for further analysis or reporting outside the console.