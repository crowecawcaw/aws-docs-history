

# Analytics dashboard

The analytics dashboard provides operational visibility into your AI agent performance and business impact. You can view key performance indicators (KPIs), track trends over time, and export detailed metrics for further analysis.

The dashboard shows data about 10 minutes after a task ends. Charts group data by day in Coordinated Universal Time (UTC).

In the Amazon Connect Health app, the **Analytics** page has a tab for each agentic capability. Each tab shows the task resolution rate, tasks handled, and task escalation rate for that capability. You can export task metrics as a CSV file. For more information, see [Set up agents in the Amazon Connect Health web app](setting-up-pe-web-app.md).

![The analytics dashboard showing KPI summary cards and charts](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/full-dashboard.png)


## Viewing the analytics dashboard
<a name="viewing-analytics"></a>

To access the analytics dashboard, choose **Analytics** in the app console sidebar navigation.

## KPI summary cards
<a name="analytics-kpi-cards"></a>

The dashboard displays three KPI summary cards at the top of the page. These cards provide a high-level overview of AI agent performance for the selected date range.
+  **Task resolution rate** – The percentage of tasks that the AI agent resolved, including escalations to a person that your workflow expects, such as transferring a verified patient. The fully self-served value shows the percentage of tasks resolved with no transfer.
+  **Tasks handled** – The total number of tasks that the AI agent handled in the selected period. One call can include several tasks, such as verification and then scheduling.
+  **Task escalation rate** – The percentage of tasks that required escalation to a human agent.

## Charts
<a name="analytics-charts"></a>

The dashboard includes the following charts to help you analyze AI agent performance trends:
+  **Task resolution rate** – A line chart that shows the resolution rate over time.
+  **Tasks handled** – A bar chart that shows task volume.
+  **Task escalation volume** – A bar chart that shows the number of escalated tasks over time.
+  **Task escalation rate** – A line chart that shows the escalation rate over time.
+  **Why tasks escalate** – A donut chart that breaks down escalations by reason category.
+  **Intent distribution** – A horizontal bar chart that shows task volume by detected intent.
+  **Intent resolution rate** – A horizontal bar chart that shows the percentage of tasks resolved per intent.

Some charts appear only on certain tabs:
+  **Intent distribution** and **Intent resolution rate** appear only for appointment management and prescription management.
+ The patient verification dashboard includes a **Callers who couldn’t be matched** donut chart that breaks down all the callers who couldn’t be verified.
+ The information assistance tab includes **Usage by info source** and **Unanswered questions by category** widgets. They show how info sources are used to answer questions and which categories unanswered questions fall into.

## Filtering by date range
<a name="analytics-date-range"></a>

You can filter all dashboard data by date range. Choose from the following presets:
+ Last 7 days
+ Last 14 days
+ Last 30 days

You can also specify a custom relative range in days or weeks, or select an absolute date range. The following limits apply:
+ The maximum date range is 30 days.
+ The start date must be within the last 90 days.

![The date range picker showing date range options](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/relative-date-view.png)


## Exporting metrics
<a name="analytics-export"></a>

To export metrics, choose **Export** in one of the dashboards. This downloads a CSV file that includes the following columns:
+ Timestamp
+ Agent Session
+ Agent Type
+ Intent
+ Status
+ Escalation Reason
+ Escalation Detail
+ Duration (ms)

You can use the exported data for further analysis or reporting outside the console.