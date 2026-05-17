# limit

Use `limit` to specify the number of log events that you want
your query to return. If you omit `limit`, the query defaults to
returning up to 10,000 log events. You can specify a `limit` value
of up to 100,000.

For example, the following example returns only the 25 most recent log
events

```
fields @timestamp, @message | sort @timestamp desc | limit 25
```
