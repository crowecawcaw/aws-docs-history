# Compare (diff) with previous time

ranges

You can use CloudWatch Logs Insights with the Logs Insights QL to compare changes in your log
events over time. You can compare the log events ingested during a recent time
range with the logs from the immediately previous time period. Alternatively,
you can compare with similar past time periods. This can help you find whether
an error in your logs was recently introduced or was already occurring, and can
help you find other trends.

Comparison queries return only patterns in the results, not raw log events.
The patterns returned will help you quickly see the trends and changes in the
log events over time. After you run a comparison query and have the pattern
results, you can see sample raw log events for the patterns that you're
interested in. For more information about log patterns, see [Pattern analysis](CWL_AnalyzeLogData_Patterns.md "CWL_AnalyzeLogData_Patterns.md").

When you run a comparison query, your query is analyzed against two different
time periods: the original query period that you select, and the comparison
period. The comparison period is always of equal length to your original query
period. The default time intervals for the comparisons are the following.

- **Previous period**— Compares to
  the time period immediately before your query time period.
- **Previous day**— Compares to the
  time period one day before your query time period.
- **Previous week**— Compares to the
  time period one week before your query time period.
- **Previous month**— Compares to
  the time period one month before your query time period.

###### Note

Queries using comparisons incur charges similar to running a single
CloudWatch Logs Insights query over the combined time range. For more information, see [Amazon CloudWatch
Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### To run a comparison query

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**,
   **Logs Insights**.

A default query appears in the query box. 3. Confirm that the **Logs Insights QL** tab is
selected. 4. Keep the default query or enter a different query. 5. In the **Select log group(s)** drop-down, choose one
or more log groups to query. 6. (Optional) Use the time interval selector to select a time period that
you want to query. The default query is for the previous hour of log
data. 7. By the time range selector, choose **Compare**. Then
choose the previous time period that you want to compare the original
logs with, and choose **Apply**. 8. Choose **Run query**.

To cause the query to fetch the data from the comparison period, the
`diff` command is appended to your query. 9. Choose the **Patterns** tab to see the
results.

The table displays the following information:

    * Each **Pattern**, with variable parts of the
     pattern replaced by the dynamic token symbol
     `<`string`-`number`>`.
     The `string` is a description of the
     type of data that the token represents. The
     `number` shows where in the pattern
     this token appears, compared to the other dynamic tokens. For
     more information, see [Pattern analysis](CWL_AnalyzeLogData_Patterns.md "CWL_AnalyzeLogData_Patterns.md").
    * **Event count** is the number of log events
     with that pattern in the original, more current time
     period.
    * **Difference event count** is the difference
     between the number of matching log events in the current time
     period versus the comparison time period. A positive different
     means there are more such events in the current time
     period.
    * **Difference description** briefly summarizes
     the change in that pattern between the current time period and
     the comparison period.
    * **Severity type** is the probable severity of
     the logs events with this pattern, based on words found in the
     log events such as `FATAL`, `ERROR`, and
     `WARN`.

10. To further inspect one of the patterns in the list, choose the icon in
    the **Inspect** column for one of the patterns.

The **Pattern inspect** pane appears and displays the
following:

    * The **Pattern**. Select a token within the
     pattern to analyze that token's values.
    * A histogram showing the number of occurrences of the pattern
     over the queried time range. This can help you to identify
     interesting trends such as a sudden increase in occurrence of a
     pattern.
    * The **Log samples** tab displays a few of the
     log events that match the selected pattern.
    * The **Token Values** tab displays the values
     of the selected dynamic token, if you have selected one.


    ###### Note

    A maximum of 10 token values is captured for each token.
     Token counts might not be precise. CloudWatch Logs uses a
     probabilistic counter to generate the token count, not the
     absolute value.
    * The **Related patterns** tab displays other
     patterns that frequently occurred near the same time as the
     pattern that you are inspecting. For example, if a pattern for
     an `ERROR` message was usually accompanied by another
     log event marked as `INFO` with additional details,
     that pattern is displayed here.
