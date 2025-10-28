For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Last point from each

device

Your application may require you to read the last measurement emitted by a device.
There can be more general use cases to obtain the last measurement for a device
before a given date/time or the first measurement for a device after a given
date/time. When you have millions of devices and years of data, this search might
require scanning large amounts of data.

Below you will see an example of how you can use scheduled queries to optimize
searching for the last point emitted by a device. You can use the same pattern to
optimize the first point query as well if your application needs them.

###### Topics

- [Computed from source table](#scheduledqueries-patterns-lastpointfromdevice-computedfromsrctable "#scheduledqueries-patterns-lastpointfromdevice-computedfromsrctable")
- [Derived table to precompute at daily granularity](#scheduledqueries-patterns-lastpointfromdevice-derivedttabletoprecompute "#scheduledqueries-patterns-lastpointfromdevice-derivedttabletoprecompute")
- [Computed from derived table](#scheduledqueries-patterns-lastpointfromdevice-computedfromderivedtable "#scheduledqueries-patterns-lastpointfromdevice-computedfromderivedtable")
- [Combining from source and derived table](#scheduledqueries-patterns-lastpointfromdevice-combinesourceandderived "#scheduledqueries-patterns-lastpointfromdevice-combinesourceandderived")

## Computed from source table

Below is an example query to find the last measurement emitted by the services
in a specific deployment (for example, servers for a given micro-service within a given
region, cell, silo, and availability_zone). In the example application, this
query will return the last measurement for hundreds of servers. Also note that
this query has an unbounded time predicate and looks for any data older than a
given timestamp.

###### Note

For information about the `max` and `max_by`
functions, see [Aggregate functions](aggregate-functions.md "aggregate-functions.md").

```
SELECT instance_name, MAX(time) AS time, MAX_BY(gc_pause, time) AS last_measure
FROM "raw_data"."devops"
WHERE time < from_milliseconds(1636685271872)
    AND measure_name = 'events'
    AND region = 'us-east-1'
    AND cell = 'us-east-1-cell-10'
    AND silo = 'us-east-1-cell-10-silo-3'
    AND availability_zone = 'us-east-1-1'
    AND microservice_name = 'hercules'
GROUP BY region, cell, silo, availability_zone, microservice_name,
    instance_name, process_name, jdk_version
ORDER BY instance_name, time DESC
```

## Derived table to precompute at daily granularity

You can convert the preceding use case into a scheduled computation. If your
application requirements are such that you may need to obtain these values for
your entire fleet across multiple regions, cells, silos, availability zones and
microservices, you can use one schedule computation to pre-compute the values
for your entire fleet. That is the power of Timestream for LiveAnalytics's serverless scheduled queries
that allows these queries to scale with your application's scaling
requirements.

Below is a query to pre-compute the last point across all the servers for a
given day. Note that the query only has a time predicate and not a predicate on
the dimensions. The time predicate limits the query to the past day from the
time when the computation is triggered based on the specified schedule
expression.

```
SELECT region, cell, silo, availability_zone, microservice_name,
    instance_name, process_name, jdk_version,
    MAX(time) AS time, MAX_BY(gc_pause, time) AS last_measure
FROM raw_data.devops
WHERE time BETWEEN bin(@scheduled_runtime, 1d) - 1d AND bin(@scheduled_runtime, 1d)
    AND measure_name = 'events'
GROUP BY region, cell, silo, availability_zone, microservice_name,
    instance_name, process_name, jdk_version
```

Below is a configuration for the scheduled computation using the preceding
query which executes that query at 01:00 hrs UTC every day to compute the
aggregate for the past day. The schedule expression cron(0 1 \* \* ? \*) controls
this behavior and runs an hour after the day has ended to consider any data
arriving up to a day late.

```
{
    "Name": "PT1DPerInstanceLastpoint",
    "QueryString": "SELECT region, cell, silo, availability_zone, microservice_name, instance_name, process_name, jdk_version, MAX(time) AS time, MAX_BY(gc_pause, time) AS last_measure FROM raw_data.devops WHERE time BETWEEN bin(@scheduled_runtime, 1d) - 1d AND bin(@scheduled_runtime, 1d) AND measure_name = 'events' GROUP BY region, cell, silo, availability_zone, microservice_name, instance_name, process_name, jdk_version",
    "ScheduleConfiguration": {
        "ScheduleExpression": "cron(0 1 * * ? *)"
    },
    "NotificationConfiguration": {
        "SnsConfiguration": {
            "TopicArn": "******"
        }
    },
    "TargetConfiguration": {
        "TimestreamConfiguration": {
            "DatabaseName": "derived",
            "TableName": "per_timeseries_lastpoint_pt1d",
            "TimeColumn": "time",
            "DimensionMappings": [
                {
                    "Name": "region",
                    "DimensionValueType": "VARCHAR"
                },
                {
                    "Name": "cell",
                    "DimensionValueType": "VARCHAR"
                },
                {
                    "Name": "silo",
                    "DimensionValueType": "VARCHAR"
                },
                {
                    "Name": "availability_zone",
                    "DimensionValueType": "VARCHAR"
                },
                {
                    "Name": "microservice_name",
                    "DimensionValueType": "VARCHAR"
                },
                {
                    "Name": "instance_name",
                    "DimensionValueType": "VARCHAR"
                },
                {
                    "Name": "process_name",
                    "DimensionValueType": "VARCHAR"
                },
                {
                    "Name": "jdk_version",
                    "DimensionValueType": "VARCHAR"
                }
            ],
            "MultiMeasureMappings": {
                "TargetMultiMeasureName": "last_measure",
                "MultiMeasureAttributeMappings": [
                    {
                        "SourceColumn": "last_measure",
                        "MeasureValueType": "DOUBLE"
                    }
                ]
            }
        }
    },
    "ErrorReportConfiguration": {
        "S3Configuration" : {
            "BucketName" : "******",
            "ObjectKeyPrefix": "errors",
            "EncryptionOption": "SSE_S3"
        }
    },
    "ScheduledQueryExecutionRoleArn": "******"
}
```

## Computed from derived table

Once you define the derived table using the preceding configuration and at
least one instance of the scheduled query has materialized data into the derived
table, you can now query the derived table to get the latest measurement. Below
is an example query on the derived table.

```
SELECT instance_name, MAX(time) AS time, MAX_BY(last_measure, time) AS last_measure
FROM "derived"."per_timeseries_lastpoint_pt1d"
WHERE time < from_milliseconds(1636746715649)
    AND measure_name = 'last_measure'
    AND region = 'us-east-1'
    AND cell = 'us-east-1-cell-10'
    AND silo = 'us-east-1-cell-10-silo-3'
    AND availability_zone = 'us-east-1-1'
    AND microservice_name = 'hercules'
GROUP BY region, cell, silo, availability_zone, microservice_name,
    instance_name, process_name, jdk_version
ORDER BY instance_name, time DESC
```

## Combining from source and derived table

Similar to the previous example, any data from the derived table will not have
the most recent writes. Therefore, you can again use a similar pattern as
earlier to merge the data from the derived table for the older data and use the
source data for the remaining tip. Below is an example of such a query using the
similar UNION approach. Since the application requirement is to find the latest
measurement before a time period, and this start time can be in past, the way
you write this query is to use the provided time, use the source data for up to
a day old from the specified time, and then use the derived table on the older
data. As you can see from the query example below, the time predicate on the
source data is bounded. That ensures efficient processing on the source table
which has significantly higher volume of data, and then the unbounded time
predicate is on the derived table.

```
WITH last_point_derived AS (
    SELECT instance_name, MAX(time) AS time, MAX_BY(last_measure, time) AS last_measure
    FROM "derived"."per_timeseries_lastpoint_pt1d"
    WHERE time < from_milliseconds(1636746715649)
        AND measure_name = 'last_measure'
        AND region = 'us-east-1'
        AND cell = 'us-east-1-cell-10'
        AND silo = 'us-east-1-cell-10-silo-3'
        AND availability_zone = 'us-east-1-1'
        AND microservice_name = 'hercules'
    GROUP BY region, cell, silo, availability_zone, microservice_name,
        instance_name, process_name, jdk_version
), last_point_source AS (
    SELECT instance_name, MAX(time) AS time, MAX_BY(gc_pause, time) AS last_measure
    FROM "raw_data"."devops"
    WHERE time < from_milliseconds(1636746715649) AND time > from_milliseconds(1636746715649) - 26h
        AND measure_name = 'events'
        AND region = 'us-east-1'
        AND cell = 'us-east-1-cell-10'
        AND silo = 'us-east-1-cell-10-silo-3'
        AND availability_zone = 'us-east-1-1'
        AND microservice_name = 'hercules'
    GROUP BY region, cell, silo, availability_zone, microservice_name,
        instance_name, process_name, jdk_version
)
SELECT instance_name, MAX(time) AS time, MAX_BY(last_measure, time) AS last_measure
FROM (
    SELECT * FROM last_point_derived
    UNION
    SELECT * FROM last_point_source
)
GROUP BY instance_name
ORDER BY instance_name, time DESC
```

The previous is just one illustration of how you can structure the derived
tables. If you have years of data, you can use more levels of aggregations. For
instance, you can have monthly aggregates on top of daily aggregates, and you
can have hourly aggregates before the daily. So you can merge together the most
recent to fill in the last hour, the hourly to fill in the last day, the daily
to fill in the last month, and monthly to fill in the older. The number of
levels you set up vs. the refresh schedule will be depending on your
requirements of how frequently these queries are issues and how many users are
concurrently issuing these queries.
