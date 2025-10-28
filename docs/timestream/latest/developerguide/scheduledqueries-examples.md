For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Scheduled query examples

This section contains examples of how you can use Timestream for LiveAnalytics's Scheduled Queries to optimize
the costs and dashboard load times when visualizing fleet-wide statistics effectively
monitor your fleet of devices. Scheduled Queries in Timestream for LiveAnalytics allow you to express your
queries using the full SQL surface area of Timestream for LiveAnalytics. Your query can include one or more
source tables, perform aggregations or any other query allowed by Timestream for LiveAnalytics's SQL language,
and then store the results of the query in another destination table in Timestream for LiveAnalytics.

This section refers to the target table of a scheduled query as a _derived
table_.

As an example, we will use a DevOps application where you are monitoring a large fleet
of servers that are deployed across multiple deployments (such as regions, cells, and
silos), multiple microservices, and you're tracking the fleet-wide statistics using Timestream for LiveAnalytics.
The example schema we will use is described in [Scheduled Queries Sample Schema](scheduledqueries-common-schema-example.md "scheduledqueries-common-schema-example.md").

The following scenarios will be described.

- How to convert a dashboard, plotting aggregated statistics from the raw data
  you ingest into Timestream for LiveAnalytics into a scheduled query and then how to use your pre-computed
  aggregates to create a new dashboard showing aggregate statistics.
- How to combine scheduled queries to get an aggregate view and the raw granular
  data, to drill down into details. This allows you to store and analyze the raw
  data while optimizing your common fleet-wide operations using scheduled
  queries.
- How to optimize costs using scheduled queries by finding which aggregates are
  used in multiple dashboards and have the same scheduled query populate multiple
  panels in the same or multiple dashboards.

###### Topics

- [Converting an aggregate dashboard to scheduled
  query](scheduledqueries-example1.md "scheduledqueries-example1.md")
- [Using scheduled queries and raw data for drill
  downs](scheduledqueries-example2.md "scheduledqueries-example2.md")
- [Optimizing costs by sharing scheduled query
  across dashboards](scheduledqueries-example3.md "scheduledqueries-example3.md")
- [Comparing a query on a base
  table with a query of scheduled query results](scheduledqueries-example4-clickstream.md "scheduledqueries-example4-clickstream.md")
