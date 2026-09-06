

# limit
<a name="CWL_QuerySyntax-Limit"></a>

 Use `limit` to specify the number of log events that you want your query to return. If you omit `limit`, the query defaults to returning up to 10,000 log events. You can specify a `limit` value of up to 100,000. 

For example, the following example returns only the 25 most recent log events

```
fields @timestamp, @message | sort @timestamp desc | limit 25
```

## limit any
<a name="CWL_QuerySyntax-Limit-Any"></a>

Use `limit any {{N}}` to stop the query as soon as {{N}} matching log events are found, without scanning remaining data. This can significantly reduce the amount of data scanned and speed up queries when you need only a sample of matching events rather than a specific ordered set.

With a regular `limit`, the query scans all data in the time range and then returns the top {{N}} results. With `limit any`, the query completes early once enough results are found, which means the returned events may come from any portion of the time range.

For example, the following query returns 1 log event and stops scanning as soon as it finds a match:

```
fields @message | limit any 1
```

**Note**  
Because `limit any` stops scanning early, the results are not guaranteed to be in any particular order. If you need ordered results, use `limit` without `any` together with `sort`.