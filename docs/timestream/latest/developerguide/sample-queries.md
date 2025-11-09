For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Simple queries

The following gets the 10 most recently added data points for a table.

```
SELECT * FROM `<database_name>`.`<table_name>`
ORDER BY time DESC
LIMIT 10

```

The following gets the 5 oldest data points for a specific measure.

```
SELECT * FROM `<database_name>`.`<table_name>`
WHERE measure_name = '`<measure_name>`'
ORDER BY time ASC
LIMIT 5

```

The following works with nanosecond granularity timestamps.

```
SELECT now() AS time_now
, now() - (INTERVAL '12' HOUR) AS twelve_hour_earlier -- Compatibility with ANSI SQL
, now() - 12h AS also_twelve_hour_earlier -- Convenient time interval literals
, ago(12h) AS twelve_hours_ago -- More convenience with time functionality
, bin(now(), 10m) AS time_binned -- Convenient time binning support
, ago(50ns) AS fifty_ns_ago -- Nanosecond support
, now() + (1h + 50ns) AS hour_fifty_ns_future

```

Measure values for multi-measure records are identified by column name. Measure values
for single-measure records are identified by
`measure_value::`<data_type>`, where
 `<data_type>``is one of
`double`, `bigint`, `boolean`, or `varchar`
as described in [Supported data types](supported-data-types.md "supported-data-types.md"). For more information about how measure values are modeled, see [Single table vs. multiple tables](data-modeling.md#data-modeling-multiVsinglerecords "data-modeling.md#data-modeling-multiVsinglerecords").

The following retrieves values for a measure called `speed` from
multi-measure records with a `measure_name` of
`IoTMulti-stats`.

```
SELECT speed FROM `<database_name>`.`<table_name>` where measure_name = 'IoTMulti-stats'
```

The following retrieves `double` values from single-measure records with a
`measure_name` of `load`.

```
SELECT measure_value::double FROM `<database_name>`.`<table_name>` WHERE measure_name = 'load'
```
