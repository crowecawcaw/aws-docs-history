

# Create a new widget from a SQL query with the CloudTrail console
<a name="lake-dashboard-custom-widgets-new"></a>

This section describes how to create a new widget by writing or pasting a SQL query and choosing a chart type. You can add a maximum of 10 widgets to a custom dashboard.

**To create a new widget from a SQL query**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1.  In the left navigation pane, under **Lake**, choose **Dashboard**. 

1. Choose the **Managed and custom dashboards** tab.

1. In **Custom dashboards**, choose the dashboard that you want to create a widget for.

1. From **Actions**, choose **Edit dashboard**.

1. From **Actions**, choose **Create new widget**.

1. Choose the event data store you'd like to run the query on. You can query across multiple event data stores as long as the event data stores exist in your account.

1. Write or copy the SQL query.

   You can also provide a natural language prompt in English and choose **Generate query** to produce a SQL query from your prompt. For more information, see [Create CloudTrail Lake queries from natural language prompts](lake-query-generator.md).

1. Choose **Run** to run the query and preview the query results.
**Note**  
When you run queries, you incur charges based on the amount of optimized and compressed data scanned. To help control costs, we recommend that you constrain queries by adding starting and ending `eventTime` timestamps to queries.

1. Choose the **Visualizer** tab to select the chart type for the widget. You can choose from these chart types: table, bar chart, line chart, and pie chart.

1. Choose **Add to dashboard** to add the widget to the dashboard.

1. Choose **Save** to save the dashboard.