For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Timeseries views

Timestream for LiveAnalytics supports the following functions for transforming your data to the
`timeseries` data type:

###### Topics

- [CREATE_TIME_SERIES](#timeseries-specific-constructs.views.CREATE_TIME_SERIES "#timeseries-specific-constructs.views.CREATE_TIME_SERIES")
- [UNNEST](#timeseries-specific-constructs.views.UNNEST "#timeseries-specific-constructs.views.UNNEST")

## CREATE_TIME_SERIES

**CREATE_TIME_SERIES** is an aggregation function that takes all
the raw measurements of a time series (time and measure values) and returns a
timeseries data type. The syntax of this function is as follows:

```
CREATE_TIME_SERIES(time, measure_value::`<data_type>`)
```

where `<data_type>` is the data type of the measure value
and can be one of bigint, boolean, double, or varchar. The second parameter cannot
be null.

Consider the CPU utilization of EC2 instances stored in a table named
**metrics** as shown below:

| Time                          | region    | az         | vpc          | instance_id         | measure_name    | measure_value::double |
| ----------------------------- | --------- | ---------- | ------------ | ------------------- | --------------- | --------------------- |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1d | vpc-1a2b3c4d | i-1234567890abcdef0 | cpu_utilization | 35.0                  |
| 2019-12-04 19:00:01.000000000 | us-east-1 | us-east-1d | vpc-1a2b3c4d | i-1234567890abcdef0 | cpu_utilization | 38.2                  |
| 2019-12-04 19:00:02.000000000 | us-east-1 | us-east-1d | vpc-1a2b3c4d | i-1234567890abcdef0 | cpu_utilization | 45.3                  |
| 2019-12-04 19:00:00.000000000 | us-east-1 | us-east-1d | vpc-1a2b3c4d | i-1234567890abcdef1 | cpu_utilization | 54.1                  |
| 2019-12-04 19:00:01.000000000 | us-east-1 | us-east-1d | vpc-1a2b3c4d | i-1234567890abcdef1 | cpu_utilization | 42.5                  |
| 2019-12-04 19:00:02.000000000 | us-east-1 | us-east-1d | vpc-1a2b3c4d | i-1234567890abcdef1 | cpu_utilization | 33.7                  |

Running the query:

```
SELECT region, az, vpc, instance_id, CREATE_TIME_SERIES(time, measure_value::double) as cpu_utilization FROM metrics
    WHERE measure_name=’cpu_utilization’
    GROUP BY region, az, vpc, instance_id
```

will return all series that have `cpu_utilization` as a measure value.
In this case, we have two series:

| region    | az         | vpc          | instance_id         | cpu_utilization                                                                                                                                                                                                          |
| --------- | ---------- | ------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| us-east-1 | us-east-1d | vpc-1a2b3c4d | i-1234567890abcdef0 | [{time: 2019-12-04 19:00:00.000000000, measure\_value::double:<br>35.0}, {time: 2019-12-04 19:00:01.000000000,<br>measure\_value::double: 38.2}, {time: 2019-12-04<br>19:00:02.000000000, measure\_value::double: 45.3}] |
| us-east-1 | us-east-1d | vpc-1a2b3c4d | i-1234567890abcdef1 | [{time: 2019-12-04 19:00:00.000000000, measure\_value::double:<br>35.1}, {time: 2019-12-04 19:00:01.000000000,<br>measure\_value::double: 38.5}, {time: 2019-12-04<br>19:00:02.000000000, measure\_value::double: 45.7}] |

## UNNEST

`UNNEST` is a table function that enables you to transform
`timeseries` data into the flat model. The syntax is as follows:

`UNNEST` transforms a `timeseries` into two columns, namely,
`time` and `value`. You can also use aliases with UNNEST
as shown below:

```
UNNEST(timeseries) AS `<alias_name>` (`time_alias`, `value_alias`)
```

where `<alias_name>` is the alias for the flat table,
`time_alias` is the alias for the `time` column and
`value_alias` is the alias for the `value` column.

For example, consider the scenario where some of the EC2 instances in your fleet
are configured to emit metrics at a 5 second interval, others emit metrics at a 15
second interval, and you need the average metrics for all instances at a 10 second
granularity for the past 6 hours. To get this data, you transform your metrics to
the time series model using **CREATE_TIME_SERIES**. You can then
use **INTERPOLATE_LINEAR** to get the missing values at 10 second
granularity. Next, you transform the data back to the flat model using
**UNNEST**, and then use **AVG** to get the
average metrics across all instances.

```
WITH interpolated_timeseries AS (
    SELECT region, az, vpc, instance_id,
        INTERPOLATE_LINEAR(
            CREATE_TIME_SERIES(time, measure_value::double),
                SEQUENCE(ago(6h), now(), 10s)) AS interpolated_cpu_utilization
    FROM timestreamdb.metrics
    WHERE measure_name= ‘cpu_utilization’ AND time >= ago(6h)
    GROUP BY region, az, vpc, instance_id
)
SELECT region, az, vpc, instance_id, avg(t.cpu_util)
FROM interpolated_timeseries
CROSS JOIN UNNEST(interpolated_cpu_utilization) AS t (time, cpu_util)
GROUP BY region, az, vpc, instance_id

```

The query above demonstrates the use of **UNNEST** with an
alias. Below is an example of the same query without using an alias for
**UNNEST**:

```
WITH interpolated_timeseries AS (
    SELECT region, az, vpc, instance_id,
        INTERPOLATE_LINEAR(
            CREATE_TIME_SERIES(time, measure_value::double),
                SEQUENCE(ago(6h), now(), 10s)) AS interpolated_cpu_utilization
    FROM timestreamdb.metrics
    WHERE measure_name= ‘cpu_utilization’ AND time >= ago(6h)
    GROUP BY region, az, vpc, instance_id
)
SELECT region, az, vpc, instance_id, avg(value)
FROM interpolated_timeseries
CROSS JOIN UNNEST(interpolated_cpu_utilization)
GROUP BY region, az, vpc, instance_id

```
