

# Time-series functions
<a name="CWL_QuerySyntax-timeseries-functions"></a>

Use time-series functions with the `stats` command to analyze metrics over time windows and compute rates of change.


|  Function |  Result type |  Description | 
| --- | --- | --- | 
| `rate(fieldName: NumericLogField, interval: Period)` | number | Computes the per-interval rate of change for a numeric field. | 
| `countOverTime(fieldName: LogField)` | number | Counts log events per time bin. Use with `by bin(interval)` to set the window. | 
| `sumOverTime(fieldName: NumericLogField)` | number | Sums field values per time bin. Use with `by bin(interval)` to set the window. | 
| `histogram(fieldName: NumericLogField, buckets: number)` | map | Bucketizes numeric field values into the specified number of equal-width ranges and returns the distribution. | 

## offset
<a name="CWL_QuerySyntax-timeseries-offset"></a>

Use `offset` at the end of a `stats ... by bin()` clause to shift time-series bins by a specified duration. This enables time-shifted comparisons, such as comparing current metrics against the same period in the previous hour or day.

**Syntax**

```
stats <aggregation> by bin(<period>) offset <duration>
```

**Examples**

```
stats count(*) by bin(5m) offset 1h
```

```
stats avg(latency) by bin(1m) offset 1d
```