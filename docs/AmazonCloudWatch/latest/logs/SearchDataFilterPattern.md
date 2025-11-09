# Search log data using filter patterns

You can search your log data using the [Filter pattern syntax for metric filters, subscription filters, filter log events, and Live Tail](FilterAndPatternSyntax.md "FilterAndPatternSyntax.md"). You can search all the log streams within
a log group, or by using the AWS CLI you can also search specific log streams. When each search runs, it returns up to
the first page of data found and a token to retrieve the next page of data or to
continue searching. If no results are returned, you can continue searching.

You can set the time range you want to query to limit the scope of your search. You
could start with a larger range to see where the log lines you are interested in fall,
and then shorten the time range to scope the view to logs in the time range that
interest you.

You can also pivot directly from your logs-extracted metrics to the corresponding logs.

If you are signed in to an account set up as a monitoring account in CloudWatch cross-account
observability, you can search and filter log events from the source accounts linked to this monitoring account.
For more information, see [CloudWatch cross-account observability](../monitoring/CloudWatch-Unified-Cross-Account.md "../monitoring/CloudWatch-Unified-Cross-Account.md").

## Search log entries using the console

You can search for log entries that meet a specified criteria using the console.

###### To search your logs using the console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Log groups**.
3. For **Log Groups**, choose the name of the log group
   containing the log stream to search.
4. For **Log Streams**, choose the name of the log stream
   to search.
5. Under **Log events**, enter the filter syntax to use.

###### To search all log entries for a time range using the console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Log groups**.
3. For **Log Groups**, choose the name of the log group
   containing the log stream to search.
4. Choose **Search log group**.
5. For **Log events**, select the date and time range, and
   enter the filter syntax.

## Search log entries using the AWS CLI

You can search for log entries that meet a specified criteria using the AWS CLI.

###### To search log entries using the AWS CLI

At a command prompt, run the following [filter-log-events](../../../cli/latest/reference/logs/filter-log-events.md "../../../cli/latest/reference/logs/filter-log-events.md") command. Use `--filter-pattern` to limit the results
to the specified filter pattern and `--log-stream-names` to limit the results
to the specified log streams.

```
aws logs filter-log-events --log-group-name `my-group` [--log-stream-names `LIST_OF_STREAMS_TO_SEARCH`] [--filter-pattern `VALID_METRIC_FILTER_PATTERN`]
```

###### To search log entries over a given time range using the AWS CLI

At a command prompt, run the following [filter-log-events](../../../cli/latest/reference/logs/filter-log-events.md "../../../cli/latest/reference/logs/filter-log-events.md") command:

```
aws logs filter-log-events --log-group-name `my-group` [--log-stream-names `LIST_OF_STREAMS_TO_SEARCH`] [--start-time `1482197400000`] [--end-time `1482217558365`] [--filter-pattern `VALID_METRIC_FILTER_PATTERN`]
```

## Pivot from metrics to logs

You can get to specific log entries from other parts of the console.

###### To get from dashboard widgets to logs

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**.
3. Choose a dashboard.
4. On the widget, choose the **View logs** icon, and then
   choose **View logs in this time range**. If there is more
   than one metric filter, select one from the list. If there are more metric
   filters than we can display in the list, choose **More metric filters**
   and select or search for a metric filter.

###### To get from metrics to logs

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. In the search field on the **All metrics** tab, type
   the name of the metric and press Enter.
4. Select one or more metrics from the results of your search.
5. Choose **Actions**, **View logs**.
   If there is more than one metric filter, select one from the list.
   If there are more metric filters than we can display in the list, choose
   **More metric filters** and select or search for a
   metric filter.

## Troubleshooting

**Search takes too long to complete**

If you have a lot of log data, search might take a long time to complete. To
speed up a search, you can do the following:

- If you are using the AWS CLI, you can limit the search to just the log streams you are interested in. For
  example, if your log group has 1000 log streams, but you just want to see
  three log streams that you know are relevant, you can use the AWS CLI to limit your search to
  only those three log streams within the log group.
- Use a shorter, more granular time range, which reduces the amount of data
  to be searched and speeds up the query.
