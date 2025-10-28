# Pattern analysis

CloudWatch Logs Insights uses machine learning algorithms to find _patterns_ when
you query your logs. A pattern is a shared text structure that recurs among your log
fields. When you view the results of a query, you can choose the
**Patterns** tab to see the patterns that CloudWatch Logs found based on a
sample of your results. Alternatively, you can append the `pattern` command
to your query to analyze the patterns in the entire set of matching log events.

Patterns are useful for analyzing large log sets because a large number of log events
can often be compressed into a few patterns.

Consider the following sample of three log events.

```
2023-01-01 19:00:01 [INFO] Calling DynamoDB to store for resource id 12342342k124-12345
2023-01-01 19:00:02 [INFO] Calling DynamoDB to store for resource id 324892398123-12345
2023-01-01 19:00:03 [INFO] Calling DynamoDB to store for resource id 3ff231242342-12345
```

In the previous sample, all three log events follow one pattern:

```
<Time-1> [INFO] Calling DynamoDB to store for resource id <ID-2>
```

Fields within a pattern are called _tokens_. Fields that vary
within a pattern, such as a request ID or timestamp, are _dynamic
tokens_. Each dynamic token is represented by
`<`string`-`number`>`.
The `string` is a description of the type of data that the
token represents. The `number` shows where in the pattern this
token appears, compared to the other dynamic tokens.

Common examples of dynamic tokens include error codes, timestamps, and request IDs. A
_token value_ represents a particular value of a dynamic token.
For example, if a dynamic token represents an HTTP error code, then a token value could
be `501`.

Pattern detection is also used in the CloudWatch Logs anomaly detector and compare features. For
more information, see [Log anomaly detection](LogsAnomalyDetection.md "LogsAnomalyDetection.md") and [Compare (diff) with previous time
ranges](CWL_AnalyzeLogData_Compare.md "CWL_AnalyzeLogData_Compare.md").

## Getting started with

pattern analysis

Pattern detection is automatically performed in any CloudWatch Logs Insights query. Queries that
don't include the `pattern` command get both log events and patterns in
the results.

If you include the `pattern` command in your query, pattern analysis is
performed on the entire matched set of log events. This gives you more accurate
pattern results, but the raw log events are not returned when you use the
`pattern` command. When a query doesn't include `pattern`,
the pattern results are based either on the first 1000 returned log events, or on
the limit value you used in your query. If you include `pattern` in the
query, then the results displayed in the **Patterns** tab are
derived from all log events matched by the query.

###### To get started with pattern analysis in CloudWatch Logs Insights

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Logs
   Insights**.

On the **Logs Insights** page, the query editor contains
a default query that returns the 20 most recent log events. 3. Remove the `| limit 20` line in the query box, so that the
query looks like the following:

````
fields @timestamp, @message, @logStream, @log
| sort @timestamp desc ``` 4. In the **Select log group(s)** drop-down, choose one or more log groups to query. 5. (Optional) Use the time interval selector to select a time period that you want to query. You can choose between 5-minute and 30-minute intervals; 1-hour, 3-hour, and 12-hour intervals; or a custom time frame. 6. Choose **Run query** to start the query. When the query finishes running, the **Logs** tab displays a table of log events returned by the query. Above the table is a message about how many records matched the query, similar to **Showing 10,000 of 71,101 records matched**. 7. Choose the **Patterns** tab. 8. The table now displays the patterns found in the query. Because the query did not include the `pattern` command, this tab displays only the patterns discovered among the 10,000 log events that were shown in the table in the **Logs** tab. For each pattern, the following information is displayed: <br>• The **Pattern**, with each dynamic token displayed as `<`string`-`number`>`. The `string` is a description of the type of data that the token represents. The `number` shows where in the pattern this token appears, compared to the other dynamic tokens. <br>• The **Event count**, which is the number of times that the pattern appeared in the queried log events. Choose the **Event count** column heading to sort the patterns by frequency. <br>• The **Event ratio**, which is the percentage of the queried log events that contain this pattern. <br>• The **Severity type**, which will be one of the following: + **ERROR** if the pattern contains the word **Error**. + **WARN** if the pattern contains the word **Warn** but doesn't contain **Error**. + **INFO** if the pattern doesn't contain either **Warn** or **Error**. Choose the **Severity info** column heading to sort the patterns by severity. 9. Now change the query. Replace the `| sort @timestamp desc` line in the query with `| pattern @message`, so that the complete query is as follows: ``` fields @timestamp, @message, @logStream, @log
| pattern @message ``` 10. Choose **Run query**. When the query finishes, there are no results in the **Logs** tab. However, the **Patterns** tab likely has a larger number of patterns listed, depending on the total number of log events that were queried. 11. Regardless of whether you included `pattern` in your query, you can further inspect the patterns that the query returns. To do so, choose the icon in the **Inspect** column for one of the patterns. The **Pattern inspect** pane appears and displays the following: <br>• The **Pattern**. Select a token within the pattern to analyze that token's values. <br>• A histogram showing the number of occurrences of the pattern over the queried time range. This can help you to identify interesting trends such as a sudden increase in occurrence of a pattern. <br>• The **Log samples** tab displays a few of the log events that match the selected pattern. <br>• The **Token Values** tab displays the values of the selected dynamic token, if you have selected one. ###### Note A maximum of 10 token values is captured for each token. Token counts might not be precise. CloudWatch Logs uses a probabilistic counter to generate the token count, not the absolute value. <br>• The **Related patterns** tab displays other patterns that frequently occurred near the same time as the pattern that you are inspecting. For example, if a pattern for an `ERROR` message was usually accompanied by another log event marked as `INFO` with additional details, that pattern is displayed here. ## Details about the pattern command This section contains more details about the `pattern` command and its uses. <br>• In the previous tutorial, we removed the `sort` command when we added `pattern` because a query is not valid if it includes a `pattern` command after a `sort` command. It is valid to have a `pattern` before a `sort`. For more details about `pattern` syntax, see [pattern](CWL_QuerySyntax-Pattern.md "CWL_QuerySyntax-Pattern.md"). <br>• When you use `pattern` in a query, `@message` must be one of the fields selected in the `pattern` command. <br>• You can include the `filter` command before a `pattern` command to cause only the filtered set of log events to be used as input for pattern analysis. <br>• To see pattern results for a particular field, such as a field derived from the `parse` command, use `pattern @fieldname`. <br>• Queries with non-log output, such as queries with the `stats` command, do not return pattern results.
````
