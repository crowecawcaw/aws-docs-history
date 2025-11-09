# dedup

Use `dedup` to remove duplicate results based on specific
values in fields that you specify. You can use `dedup` with one
or more fields. If you specify one field with `dedup`, only one
log event is returned for each unique value of that field. If you specify
multiple fields, then one log event is returned for each unique combination
of values for those fields.

Duplicates are discarded based on the sort order, with only the first
result in the sort order being kept. We recommend that you sort your results
before putting them through the `dedup` command. If the results
are not sorted before being run through `dedup`, then the default
descending sort order using `@timestamp` is used.

Null values are not considered duplicates for evaluation. Log events with
null values for any of the specified fields are retained. To eliminate
fields with null values, use **`filter`** using
the `isPresent(field)` function.

The only query command that you can use in a query after the
`dedup` command is `limit`.

**Example: See only the most recent log event for each unique value
of the field named `server`**

The following example displays the `timestamp`,
`server`, `severity`, and `message`
fields for only the most recent event for each unique value of
`server`.

```
fields @timestamp, server, severity, message
| sort @timestamp desc
| dedup server
```

For more samples of CloudWatch Logs Insights queries, see [General queries](CWL_QuerySyntax-examples.md#CWL_QuerySyntax-examples-general "CWL_QuerySyntax-examples.md#CWL_QuerySyntax-examples-general").
