For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Queries with time series

functions

###### Topics

- [Example dataset and
  queries](#sample-queries.devops-scenarios.example "#sample-queries.devops-scenarios.example")

## Example dataset and

queries

You can use Timestream for LiveAnalytics to understand and improve the performance and availability of
your services and applications. Below is an example table and sample queries run on that
table.

The table `ec2_metrics` stores telemetry data, such as CPU utilization and
other metrics from EC2 instances. You can view the table below.

| Time                          | region    | az         | Hostname   | measure_name       | measure_value::double | measure_value::bigint |
| ----------------------------- | --------- | ---------- | ---------- | ------------------ | --------------------- | --------------------- |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1a | frontend01 | cpu_utilization    | 35.1                  | null                  |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1a | frontend01 | memory_utilization | 55.3                  | null                  |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1a | frontend01 | network_bytes_in   | null                  | 1,500                 |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1a | frontend01 | network_bytes_out  | null                  | 6,700                 |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1b | frontend02 | cpu_utilization    | 38.5                  | null                  |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1b | frontend02 | memory_utilization | 58.4                  | null                  |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1b | frontend02 | network_bytes_in   | null                  | 23,000                |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1b | frontend02 | network_bytes_out  | null                  | 12,000                |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1c | frontend03 | cpu_utilization    | 45.0                  | null                  |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1c | frontend03 | memory_utilization | 65.8                  | null                  |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1c | frontend03 | network_bytes_in   | null                  | 15,000                |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1c | frontend03 | network_bytes_out  | null                  | 836,000               |
| 2019-12-04 19:00:05.000000000 | us-east-1 | us-east-1a | frontend01 | cpu_utilization    | 55.2                  | null                  |
| 2019-12-04 19:00:05.000000000 | us-east-1 | us-east-1a | frontend01 | memory_utilization | 75.0                  | null                  |
| 2019-12-04 19:00:05.000000000 | us-east-1 | us-east-1a | frontend01 | network_bytes_in   | null                  | 1,245                 |
| 2019-12-04 19:00:05.000000000 | us-east-1 | us-east-1a | frontend01 | network_bytes_out  | null                  | 68,432                |
| 2019-12-04 19:00:08.000000000 | us-east-1 | us-east-1b | frontend02 | cpu_utilization    | 65.6                  | null                  |
| 2019-12-04 19:00:08.000000000 | us-east-1 | us-east-1b | frontend02 | memory_utilization | 85.3                  | null                  |
| 2019-12-04 19:00:08.000000000 | us-east-1 | us-east-1b | frontend02 | network_bytes_in   | null                  | 1,245                 |
| 2019-12-04 19:00:08.000000000 | us-east-1 | us-east-1b | frontend02 | network_bytes_out  | null                  | 68,432                |
| 2019-12-04 19:00:20.000000000 | us-east-1 | us-east-1c | frontend03 | cpu_utilization    | 12.1                  | null                  |
| 2019-12-04 19:00:20.000000000 | us-east-1 | us-east-1c | frontend03 | memory_utilization | 32.0                  | null                  |
| 2019-12-04 19:00:20.000000000 | us-east-1 | us-east-1c | frontend03 | network_bytes_in   | null                  | 1,400                 |
| 2019-12-04 19:00:20.000000000 | us-east-1 | us-east-1c | frontend03 | network_bytes_out  | null                  | 345                   |
| 2019-12-04 19:00:10.000000000 | us-east-1 | us-east-1a | frontend01 | cpu_utilization    | 15.3                  | null                  |
| 2019-12-04 19:00:10.000000000 | us-east-1 | us-east-1a | frontend01 | memory_utilization | 35.4                  | null                  |
| 2019-12-04 19:00:10.000000000 | us-east-1 | us-east-1a | frontend01 | network_bytes_in   | null                  | 23                    |
| 2019-12-04 19:00:10.000000000 | us-east-1 | us-east-1a | frontend01 | network_bytes_out  | null                  | 0                     |
| 2019-12-04 19:00:16.000000000 | us-east-1 | us-east-1b | frontend02 | cpu_utilization    | 44.0                  | null                  |
| 2019-12-04 19:00:16.000000000 | us-east-1 | us-east-1b | frontend02 | memory_utilization | 64.2                  | null                  |
| 2019-12-04 19:00:16.000000000 | us-east-1 | us-east-1b | frontend02 | network_bytes_in   | null                  | 1,450                 |
| 2019-12-04 19:00:16.000000000 | us-east-1 | us-east-1b | frontend02 | network_bytes_out  | null                  | 200                   |
| 2019-12-04 19:00:40.000000000 | us-east-1 | us-east-1c | frontend03 | cpu_utilization    | 66.4                  | null                  |
| 2019-12-04 19:00:40.000000000 | us-east-1 | us-east-1c | frontend03 | memory_utilization | 86.3                  | null                  |
| 2019-12-04 19:00:40.000000000 | us-east-1 | us-east-1c | frontend03 | network_bytes_in   | null                  | 300                   |
| 2019-12-04 19:00:40.000000000 | us-east-1 | us-east-1c | frontend03 | network_bytes_out  | null                  | 423                   |

Find the average, p90, p95, and p99 CPU utilization for a specific EC2 host over the
past 2 hours:

```
SELECT region, az, hostname, BIN(time, 15s) AS binned_timestamp,
    ROUND(AVG(measure_value::double), 2) AS avg_cpu_utilization,
    ROUND(APPROX_PERCENTILE(measure_value::double, 0.9), 2) AS p90_cpu_utilization,
    ROUND(APPROX_PERCENTILE(measure_value::double, 0.95), 2) AS p95_cpu_utilization,
    ROUND(APPROX_PERCENTILE(measure_value::double, 0.99), 2) AS p99_cpu_utilization
FROM "sampleDB".DevOps
WHERE measure_name = 'cpu_utilization'
    AND hostname = 'host-Hovjv'
    AND time > ago(2h)
GROUP BY region, hostname, az, BIN(time, 15s)
ORDER BY binned_timestamp ASC
```

Identify EC2 hosts with CPU utilization that is higher by 10 % or more compared to
the average CPU utilization of the entire fleet for the past 2 hours:

```
WITH avg_fleet_utilization AS (
    SELECT COUNT(DISTINCT hostname) AS total_host_count, AVG(measure_value::double) AS fleet_avg_cpu_utilization
    FROM "sampleDB".DevOps
    WHERE measure_name = 'cpu_utilization'
        AND time > ago(2h)
), avg_per_host_cpu AS (
    SELECT region, az, hostname, AVG(measure_value::double) AS avg_cpu_utilization
    FROM "sampleDB".DevOps
    WHERE measure_name = 'cpu_utilization'
        AND time > ago(2h)
    GROUP BY region, az, hostname
)
SELECT region, az, hostname, avg_cpu_utilization, fleet_avg_cpu_utilization
FROM avg_fleet_utilization, avg_per_host_cpu
WHERE avg_cpu_utilization > 1.1 * fleet_avg_cpu_utilization
ORDER BY avg_cpu_utilization DESC
```

Find the average CPU utilization binned at 30 second intervals for a specific EC2
host over the past 2 hours:

```
SELECT BIN(time, 30s) AS binned_timestamp, ROUND(AVG(measure_value::double), 2) AS avg_cpu_utilization
FROM "sampleDB".DevOps
WHERE measure_name = 'cpu_utilization'
    AND hostname = 'host-Hovjv'
    AND time > ago(2h)
GROUP BY hostname, BIN(time, 30s)
ORDER BY binned_timestamp ASC
```

Find the average CPU utilization binned at 30 second intervals for a specific EC2
host over the past 2 hours, filling in the missing values using linear
interpolation:

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

Find the average CPU utilization binned at 30 second intervals for a specific EC2
host over the past 2 hours, filling in the missing values using interpolation based on
the last observation carried forward:

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
