# View running queries or query history

You can view the queries currently in progress as well as your recent query
history.

Queries currently running includes queries you have added to a dashboard. You are
limited to 30 concurrent CloudWatch Logs Insights queries per account, including queries added to
dashboards. Only 15 of these 30 queries can use either OpenSearch Service PPL or OpenSearch Service SQL.

###### To view your recent query history

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then choose
   **Logs Insights**.
3. Choose **History**, if you are using the new design for the
   CloudWatch Logs console. If you are using the old design, choose
   **Actions**, **View query history for this
   account**.

A list of your recent queries appears. You can run any of them again by
selecting the query and choosing **Run**.

Under **Status**, CloudWatch Logs displays **In
progress** for any queries that are currently running.
