For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# The IF statement

The **IF** statement evaluates a condition to be true or false and returns
the appropriate value. Timestream supports the following two syntax representations for
**IF**:

```
if(condition, true_value)
```

This syntax evaluates and returns `true_value` if condition is `true`;
otherwise `null` is returned and `true_value` is not evaluated.

```
if(condition, true_value, false_value)
```

This syntax evaluates and returns `true_value` if condition is `true`,
otherwise evaluates and returns `false_value`.

## Examples

```
SELECT
  if(true, 'example 1'),
  if(false, 'example 2'),
  if(true, 'example 3 true', 'example 3 false'),
  if(false, 'example 4 true', 'example 4 false')
```

| \_col0      | \_col1        | \_col2           | \_col3            |
| ----------- | ------------- | ---------------- | ----------------- |
| `example 1` | `-`<br>`null` | `example 3 true` | `example 4 false` |
