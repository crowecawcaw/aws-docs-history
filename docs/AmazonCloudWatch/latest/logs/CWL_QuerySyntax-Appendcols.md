

# appendcols
<a name="CWL_QuerySyntax-Appendcols"></a>

Use the `appendcols` command to append a sub-query's columns to the current results by positional row matching.

**Syntax**  


```
| appendcols [override=true|false] [max={{n}}] ( {{subquery}} )
```

The command uses the following arguments:
+ `override` (Optional) – Whether to overwrite existing fields. Default: `false`.
+ `max` (Optional) – Maximum rows to process (1–100000, default 10000).
+ `{{subquery}}` – A complete CloudWatch Logs Insights query enclosed in parentheses.

**Example**  
The following query appends average latency per service from another log group.

```
fields svc
| stats count(*) as cnt by svc
| appendcols override=true ( SOURCE lg | stats avg(latency) as avgLat by svc )
```