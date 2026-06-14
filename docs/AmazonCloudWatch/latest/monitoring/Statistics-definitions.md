# Available statistics

`Average`, `Sum`, `Minimum`,
`Maximum`, `SampleCount`

For percentiles, use `--extended-statistics p99 p95 p50`.

## Syntax

When calling `GetMetricStatistics`, specify statistics as a list:

```
--statistics Average Maximum Minimum
```

For extended statistics (percentiles), use:

```
--extended-statistics p99 p95 p50
```
