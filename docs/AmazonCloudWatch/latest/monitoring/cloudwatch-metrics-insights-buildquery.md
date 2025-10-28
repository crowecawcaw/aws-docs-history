# Building your queries in

CloudWatch Metrics Insights

You can run a CloudWatch Metrics Insights query using the CloudWatch console, the AWS CLI, or the AWS SDKs. Queries
run in the console are free of charge. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

With CloudWatch Metrics Insights, you can analyze metric data across extended time periods of up to two weeks,
allowing for more comprehensive historical analysis and trend identification compared to
shorter retention periods. For optimal performance when querying longer time ranges, consider using larger periods
(such as 5 minutes or 1 hour) to reduce the number of data points returned. When analyzing
trends over the full two-week period, use aggregate functions like AVG() or MAX() in your
ORDER BY clauses to efficiently identify patterns.

For more information about using the AWS SDKs to perform a Metrics Insights query, see
[GetMetricData](../APIReference/API_GetMetricData.md "../APIReference/API_GetMetricData.md").

To run a query using the CloudWatch console, follow these steps:

###### To query your metrics using Metrics Insights

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, **All
   metrics**.
3. (Optional) To run a pre-built sample query, choose **Add query** and select the query to run.
   If you are satisfied with this query, you can skip the rest of this procedure.
   Or, you can choose **Editor** to edit the sample query and then choose **Run** to run
   the modified query.
4. To create your own query, choose **Multi source query**. You can then use the **Builder** view (default) to get a guided experience, or the **Editor**
   view if you prefer to see the query syntax. You can switch between the two views anytime and see your work in progress
   in both views.

In the **Builder** view, click on the namespace, metric name, filter, group, order, and limit fields to browse and select possible values. You can start typing any part
of the value you are looking for to filter the list presented by the builder. You can reference resource tags in the filter and group inputs.

In the **Editor** view, you can write the query using the subset of SQL supported by Metrics Insights. The editor offers auto-complete options based on the characters you have typed so far,
including name of resource tags for metrics that support them.

CloudWatch Metrics Insights supports querying metrics by AWS resource tags. You can use tags to filter and group your metric data for more targeted monitoring and analysis.

The following examples shows how you can use queries with tags.

To see the CPU utilization for Amazon EC2 instances within your production environment:

```
SELECT MAX(CPUUtilization) FROM SCHEMA("AWS/EC2") WHERE tag.env='prod'
```

To group the metrics by environment using the GROUP BY clause:

```
SELECT MAX(CPUUtilization) FROM SCHEMA("AWS/EC2") GROUP BY tag.env
```

To use the GROUP BY clause where you specify the tag name:

```
SELECT AVG(CPUUtilization) FROM "AWS/EC2" GROUP BY tag."aws:cloudformation:stack-name"
```

To combine tag queries with existing metric dimensions:

```
SELECT MAX(CPUUtilization) FROM SCHEMA("AWS/EC2") WHERE tag.env='prod' AND InstanceId='i-1234567890abcdef0'
```

5. When you are satisfied with your query, choose **Run**.
6. (Optional) Another way to edit a query that you have graphed is to choose the **Graphed metrics**
   tab and choose the edit icon next to the query formula in the **Details** column.
7. (Optional) To remove a query from the graph, choose **Graphed metrics** and choose
   the **X** icon at the right side of the row that displays your query.
