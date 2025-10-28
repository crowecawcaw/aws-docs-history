# pattern

Use `pattern` to automatically cluster your log data into
patterns.

A pattern is shared text structure that recurs among your log fields. You
can use `pattern` to surface emerging trends, monitor known
errors, and identify frequently occurring or high-cost log lines. CloudWatch Logs Insights
also provides a console experience you can use to find and further analyze
patterns in your log events. For more information, see [Pattern analysis](CWL_AnalyzeLogData_Patterns.md "CWL_AnalyzeLogData_Patterns.md").

Because the `pattern` command automatically identifies common
patterns, you can use it as a starting point to search and analyze yours
logs. You can also combine `pattern` with the `filter`, `parse`, or `sort` commands to
identify patterns in more fine-tuned queries.

**Pattern Command Input**

The `pattern` command expects one of the following inputs: the
`@message` field, an extracted field created using the `parse` command, or a
string manipulated using one or more [String functions](CWL_QuerySyntax-operations-functions.md#CWL_QuerySyntax-string-functions "CWL_QuerySyntax-operations-functions.md#CWL_QuerySyntax-string-functions").

If CloudWatch Logs can't infer the type of data that a dynamic token represents,
displays it as <Token-`number`>, and
`number` indicates where in the pattern this
token appears, compared to the other dynamic tokens.

Common examples of dynamic tokens include error codes, IP addresses,
timestamps, and request IDs.

**Pattern Command Output**

The `pattern` command produces the following output:

- `@pattern`: A shared text structure that recurs among
  your log event fields. Fields that vary within a pattern, such as a
  request ID or timestamp, are represented by
  _tokens_. If CloudWatch Logs can determine the type of
  data that a dynamic token represents, it displays the token as
  `<`string`-`number`>`.
  The `string` is a description of the type
  of data that the token represents. The
  `number` shows where in the pattern
  this token appears, compared to the other dynamic tokens.

CloudWatch Logs assigns the string part of the name based on analyzing the
content of the log events that contain it.

If CloudWatch Logs can't infer the type of data that a dynamic token
represents, displays it as
<Token-`number`>, and
`number` indicates where in the pattern
this token appears, compared to the other dynamic tokens.

For example, `[INFO] Request time: <Time-1> ms`
is a potential output for the log message `[INFO] Request time:
 327 ms`.

- `@ratio`: The ratio of log events from a selected time
  period and specified log groups that match an identified pattern.
  For example, if half of the log events in the selected log groups
  and time period match the pattern, `@ratio` returns
  `0.50`
- `@sampleCount`: A count of the number of log events
  from a selected time period and specified log groups that match an
  identified pattern.
- `@severityLabel`: The log severity or level, which
  indicates the type of information contained in a log. For example,
  `Error`, `Warning`, `Info`, or
  `Debug`.
  **Examples**

The following command identifies logs with similar structures in specified
log group(s) over the selected time range, grouping them by pattern and
count

```
pattern @message
```

The `pattern` command can be used in combination with the `filter`
command

````
filter @message like /ERROR/
| pattern @message ``` The `pattern` command can be use with the `parse` and `sort` commands ``` filter @message like /ERROR/
| parse @message 'Failed to do: *' as cause
| pattern cause
| sort @sampleCount asc ```
````
