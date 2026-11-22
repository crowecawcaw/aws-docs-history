

# Running PromQL queries in Query Studio

Query Studio is an interactive query environment in the CloudWatch console where you can write, run, and visualize PromQL queries against your CloudWatch metrics. You can use Query Studio to explore metrics ingested through OTLP and AWS vended metrics, create visualizations, set up alarms, and add widgets to your CloudWatch dashboards.

You can run PromQL queries programmatically using the CloudWatch API, or interactively in Query Studio.

## Running a PromQL query in Query Studio
<a name="CloudWatch-PromQL-QueryStudio-RunQuery"></a>

**To run a PromQL query in Query Studio**

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Query Studio**.

1. In the query editor tool, select **PromQL** from the drop-down menu.

1. To build the query in **Builder** mode, do the following:

   1. Select a metric name.

   1. (Optional) Select one or more labels and values to filter the time series that the query returns.

   1. (Optional) To aggregate the selected time series, choose the **More options** icon (three dots), and then choose **Add aggregation function**. Then choose a function such as `sum`, `avg`, `min`, or `max`.
**Note**  
An aggregation function applies to all of the time series that match your metric and label selection, and combines them into a single time series. Labels that you don't group by are removed from the result. To return one result per label value, such as one per host, group by that label.  
The `min` and `max` functions operate only on float samples. They skip histogram samples, which are common for durations and latencies, so the query returns an empty result. To get a statistic from a histogram metric, use a histogram function such as `histogram_quantile` or `histogram_avg`. For more information, see [Querying histogram metrics](CloudWatch-PromQL-Querying.md#CloudWatch-PromQL-Querying-Histograms).

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

## Saving and reusing queries
<a name="CloudWatch-PromQL-QueryStudio-SavedQueries"></a>

You can save a metrics query in Query Studio and reuse it later. Save a query when you want to run it again without rebuilding it. Saved queries are stored in your account in the current AWS Region, and you can save up to 1,000 queries in each Region.

Before you begin, make sure that you have the following permissions to save and manage queries:
+ `cloudwatch:PutMetricDataQueryDefinition`
+ `cloudwatch:GetMetricDataQueryDefinition`
+ `cloudwatch:ListMetricDataQueryDefinitions`
+ `cloudwatch:DeleteMetricDataQueryDefinition`

**To save queries**

1. Open the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Query Studio**.

1. In Query Studio, build or enter a query.

1. Choose **Save query**.

1. For **Name**, enter a name for the query. To group queries into a folder, use a forward slash (/) in the name, for example `team/errors`.

1. Choose **Save**.

To use a saved query, choose **Queries**, and then choose the **Saved** tab. You can search and sort your saved queries. Choose **Apply** or **Append** to add a saved query to Query Studio, or use its actions menu to **Edit** or **Delete** it. After you add a saved query to Query Studio and change it, choose **Update query** to save your changes.

Saved queries are available in the following Regions.
+ US East (N. Virginia) (`us-east-1`)
+ US East (Ohio) (`us-east-2`)
+ US West (N. California) (`us-west-1`)
+ US West (Oregon) (`us-west-2`)
+ Asia Pacific (Mumbai) (`ap-south-1`)
+ Asia Pacific (Osaka) (`ap-northeast-3`)
+ Asia Pacific (Seoul) (`ap-northeast-2`)
+ Asia Pacific (Singapore) (`ap-southeast-1`)
+ Asia Pacific (Sydney) (`ap-southeast-2`)
+ Asia Pacific (Tokyo) (`ap-northeast-1`)
+ Canada (Central) (`ca-central-1`)
+ Europe (Frankfurt) (`eu-central-1`)
+ Europe (Ireland) (`eu-west-1`)
+ Europe (London) (`eu-west-2`)
+ Europe (Paris) (`eu-west-3`)
+ Europe (Stockholm) (`eu-north-1`)
+ South America (São Paulo) (`sa-east-1`)