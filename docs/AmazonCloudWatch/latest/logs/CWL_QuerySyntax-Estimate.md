

# estimate
<a name="CWL_QuerySyntax-Estimate"></a>

Use the `estimate` command to return the estimated bytes that the query would scan over the selected log groups and time range, without running the query. Using the estimated bytes returned by this command, you can refine your log group selection, time range and filters before you run the query. The `estimate` command incurs no CloudWatch Logs Insights query charges.

The `estimate` command must be the last command in the query.

**Note**  
The value that `estimate` returns is approximate and can differ from the actual volume of data scanned when you run the query.

**Syntax**  


```
| estimate
```

**Example**  
The following query returns an estimate of the volume of data, in bytes, that the query would scan without running it.

```
fields @timestamp, @message
| filter @message like /error/
| estimate
```