For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Back-filling historical

pre-computations

When you create a scheduled computation, Timestream for LiveAnalytics manages executions of the queries
moving forward where the refresh is governed by the schedule expression you provide.
Depending of how much historical data your source table, you may want to update your
derived table with aggregates corresponding to the historical data. You can use the
preceding logic for manual triggers to back-fill the historical aggregates.

For instance, if we consider the derived table per_timeseries_lastpoint_pt1d, then
the scheduled computation is updated once a day for the past day. If your source
table has a year of data, you can use the ARN for this scheduled computation and
trigger it manually for every day up to a year old so that the derived table has all
the historical queries populated. Notes that all the caveats for manual triggers
apply here. Moreover, if the derived table is set up in a way that the historical
ingestion will write to magnetic store on the derived table, be aware of the [best practices](best-practices.md "best-practices.md") and [limits for writes](ts-limits.md "ts-limits.md")
to the magnetic store.
