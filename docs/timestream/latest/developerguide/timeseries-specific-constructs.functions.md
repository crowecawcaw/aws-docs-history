For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Interpolation

functions

If your time series data is missing values for events at certain points in time,
you can estimate the values of those missing events using interpolation. Amazon
Timestream supports four variants of interpolation: linear interpolation, cubic
spline interpolation, last observation carried forward (locf) interpolation, and
constant interpolation. This section provides usage information for the Timestream for LiveAnalytics
interpolation functions, as well as sample queries.

## Usage information

| Function                                                    | Output data type | Description                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `interpolate_linear(timeseries,<br>array[timestamp])`       | timeseries       | Fills in missing data using [linear interpolation](https://wikipedia.org/wiki/Linear_interpolation "https://wikipedia.org/wiki/Linear_interpolation").                                                                                                                                                                                                                             |
| `interpolate_linear(timeseries,<br>timestamp)`              | double           | Fills in missing data using [linear interpolation](https://wikipedia.org/wiki/Linear_interpolation "https://wikipedia.org/wiki/Linear_interpolation").                                                                                                                                                                                                                             |
| `interpolate_spline_cubic(timeseries,<br>array[timestamp])` | timeseries       | Fills in missing data using [cubic spline interpolation](https://wikiversity.org/wiki/Cubic_Spline_Interpolation#:~:text=Cubic%20spline%20interpolation%20is%20a,Lagrange%20polynomial%20and%20Newton%20polynomial. "https://wikiversity.org/wiki/Cubic_Spline_Interpolation#:~:text=Cubic%20spline%20interpolation%20is%20a,Lagrange%20polynomial%20and%20Newton%20polynomial."). |
| `interpolate_spline_cubic(timeseries,<br>timestamp)`        | double           | Fills in missing data using [cubic spline interpolation](https://wikiversity.org/wiki/Cubic_Spline_Interpolation#:~:text=Cubic%20spline%20interpolation%20is%20a,Lagrange%20polynomial%20and%20Newton%20polynomial. "https://wikiversity.org/wiki/Cubic_Spline_Interpolation#:~:text=Cubic%20spline%20interpolation%20is%20a,Lagrange%20polynomial%20and%20Newton%20polynomial."). |
| `interpolate_locf(timeseries,<br>array[timestamp])`         | timeseries       | Fills in missing data using the last sampled value.                                                                                                                                                                                                                                                                                                                                |
| `interpolate_locf(timeseries,<br>timestamp)`                | double           | Fills in missing data using the last sampled value.                                                                                                                                                                                                                                                                                                                                |
| `interpolate_fill(timeseries, array[timestamp],<br>double)` | timeseries       | Fills in missing data using a constant value.                                                                                                                                                                                                                                                                                                                                      |
| `interpolate_fill(timeseries, timestamp,<br>double)`        | double           | Fills in missing data using a constant value.                                                                                                                                                                                                                                                                                                                                      |

## Query examples

Find the average CPU utilization binned at 30 second intervals for a
specific EC2 host over the past 2 hours, filling in the missing values using
linear interpolation:

```
WITH binned_timeseries AS (
SELECT hostname, BIN(time, 30s) AS binned_timestamp, ROUND(AVG(measure_value::double), 2) AS avg_cpu_utilization
FROM "sampleDB".DevOps
WHERE measure_name = 'cpu_utilization'
    AND hostname = 'host-Hovjv'
    AND time > ago(2h)
GROUP BY hostname, BIN(time, 30s)
), interpolated_timeseries AS (
SELECT hostname,
    INTERPOLATE_LINEAR(
        CREATE_TIME_SERIES(binned_timestamp, avg_cpu_utilization),
            SEQUENCE(min(binned_timestamp), max(binned_timestamp), 15s)) AS interpolated_avg_cpu_utilization
FROM binned_timeseries
GROUP BY hostname
)
SELECT time, ROUND(value, 2) AS interpolated_cpu
FROM interpolated_timeseries
CROSS JOIN UNNEST(interpolated_avg_cpu_utilization)

```

Find the average CPU utilization binned at 30 second intervals for a
specific EC2 host over the past 2 hours, filling in the missing values using
interpolation based on the last observation carried forward:

```
WITH binned_timeseries AS (
SELECT hostname, BIN(time, 30s) AS binned_timestamp, ROUND(AVG(measure_value::double), 2) AS avg_cpu_utilization
FROM "sampleDB".DevOps
WHERE measure_name = 'cpu_utilization'
    AND hostname = 'host-Hovjv'
    AND time > ago(2h)
GROUP BY hostname, BIN(time, 30s)
), interpolated_timeseries AS (
SELECT hostname,
    INTERPOLATE_LOCF(
        CREATE_TIME_SERIES(binned_timestamp, avg_cpu_utilization),
            SEQUENCE(min(binned_timestamp), max(binned_timestamp), 15s)) AS interpolated_avg_cpu_utilization
FROM binned_timeseries
GROUP BY hostname
)
SELECT time, ROUND(value, 2) AS interpolated_cpu
FROM interpolated_timeseries
CROSS JOIN UNNEST(interpolated_avg_cpu_utilization)

```
