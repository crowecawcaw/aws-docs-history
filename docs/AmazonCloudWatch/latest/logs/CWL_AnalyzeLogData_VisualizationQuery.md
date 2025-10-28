# Tutorial: Run a

query that produces a time series visualization

When you run a query that uses the `bin()` function to group
the returned results by a time period, you can view the results as a line
graph, stacked area graph, pie chart, or bar chart. This helps you more
efficiently visualize trends in log events over time.

###### To run a query for visualization

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then
   choose **Logs Insights**.
3. Confirm that the **Logs Insights QL** tab is
   selected.
4. In the **Select log group(s)** drop down, choose
   one or more log groups to query.

If this is a monitoring account in CloudWatch cross-account
observability, you can select log groups in the source accounts as
well as the monitoring account. A single query can query logs from
different accounts at once.

You can filter the log groups by log group name, account ID, or
account label. 5. In the query editor, delete the current contents, enter the
following `stats` function, and then choose **Run
query**.

```
stats count(*) by bin(30s)
```

The results show the number of log events in the log group that
were received by CloudWatch Logs for each 30-second period. 6. Choose the **Visualization** tab.

The results are shown as a line graph. To switch to a bar chart,
pie chart, or stacked area chart, choose the arrow next to
**Line** at the upper left of the graph.
