

# Running PromQL queries in Query Studio
<a name="CloudWatch-PromQL-QueryStudio"></a>

Query Studio is an interactive query environment in the CloudWatch console where you can write, run, and visualize PromQL queries against your CloudWatch metrics. You can use Query Studio to explore metrics ingested through OTLP and AWS vended metrics, create visualizations, set up alarms, and add widgets to your CloudWatch dashboards.

You can run PromQL queries programmatically using the CloudWatch API, or interactively in Query Studio.

## Running a PromQL query in Query Studio
<a name="CloudWatch-PromQL-QueryStudio-RunQuery"></a>

**To run a PromQL query in Query Studio**

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Query Studio**.

1. In the query editor tool, select **PromQL** from the drop-down menu.

1. Use the **Builder** mode to browse and select metric names, labels, and aggregation functions.

1. Or enter your PromQL query through the **Editor** mode, for example `{"http.server.active_requests"}`.

1. (Optional) Adjust the time range using the time interval selector at the top of the page.

1. Choose **Run** to execute the query and view the results.

Query Studio will display the results as a time series graph. You can switch between graph and table views to analyze your data.

## Creating alarms from Query Studio
<a name="CloudWatch-PromQL-QueryStudio-Alarms"></a>

After running a PromQL query that returns a single time series, you can create a CloudWatch Alarm directly from Query Studio. Choose **Create alarm** from the actions menu to configure alarm thresholds, evaluation periods, and notification actions based on your query results. For more information, see [Using PromQL in alarms](CloudWatch-PromQL-Alarms.md).

## Adding visualizations to dashboards
<a name="CloudWatch-PromQL-QueryStudio-Dashboards"></a>

You can add any Query Studio visualization to a CloudWatch dashboard. After running a query and viewing the results, choose **Add to dashboard** to save the visualization as a dashboard widget. The widget continues to run the PromQL query at the dashboard's refresh interval, keeping your dashboard up to date.