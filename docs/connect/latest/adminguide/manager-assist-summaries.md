

# Summaries
<a name="manager-assist-summaries"></a>

You can generate operational summaries that consolidate multiple metrics into a single narrative response. Instead of reading through individual dashboard widgets, you can request an overview and receive a short summary that highlights key trends and anomalies across your metrics.

**Note**  
Documentation for this capability is expanded as the capability matures during preview.

## Ways to get a summary
<a name="manager-assist-summary-sources"></a>

There are two ways to get a summary:
+ **Dashboard summary panel** – supported dashboards, such as the [Queue and agent performance dashboard](queue-performance-dashboard.md), include a **Dashboard summary** panel that generates an AI-generated summary when you open the dashboard. The summary reflects the saved configuration of the dashboard and your current view, and shows the date and time when it was generated. Choose the refresh icon to generate the summary again, for example after you change the time range or when new data arrives. Choose **Learn more** to continue the conversation about the summary in the assistant panel.
+ **Manager assist chat** – request a summary in plain language, as described in the following sections.

Summaries reflect the same underlying data as the corresponding dashboard, scoped by the configuration of that dashboard. You can summarize only the dashboards that you have permission to view.

![A dashboard with the Dashboard summary panel expanded next to the assistant panel. The summary panel includes the generation time, a refresh icon, and a Learn more button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-dashboard-summary.png)


## Request a summary
<a name="manager-assist-request-summary"></a>

To request a summary in the assistant panel, ask questions such as the following:
+ Give me a summary of today's performance across all queues.
+ Summarize the Support queue performance for this week.
+ What are the key highlights from today?

## Customize the scope of a summary
<a name="manager-assist-summary-scope"></a>

In the chat, you can scope a summary by specifying the following:
+ **Time range** – for example, today, this week, or last shift.
+ **Queues or teams** – for example, for the Sales queue, or across all queues.
+ **Metrics focus** – for example, focusing on service level and abandonment.
+ **Time zone** – summaries use your local time zone by default. You can request a different time zone.

For the **Dashboard summary** panel, the saved configuration of the dashboard, including its widgets, filters, and time ranges, defines the scope. If you have unsaved changes to the dashboard, the summary might not reflect them, and the panel indicates when this is the case. Save your changes and refresh the summary to include them.

## Summary format
<a name="manager-assist-summary-format"></a>

Summaries are delivered as short narrative paragraphs rather than as lists of numbers. Summaries highlight notable trends, outliers, and anomalies instead of restating every data point. The following image shows an example summary.

![An example Dashboard summary that describes agent error states, contacts handled, average handle time, and available capacity for a queue.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-summary-example.png)


**Important**  
Summaries are generated from the available metrics data, and might not capture every operational nuance. Always cross-reference summaries with your Connect Customer dashboards and reports for critical decisions.