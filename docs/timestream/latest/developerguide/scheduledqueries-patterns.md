For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Scheduled query patterns

In this section you will find some common patterns of how you can use Amazon Timestream for LiveAnalytics
Scheduled Queries to optimize your dashboards to load faster and at reduced costs. The
examples below use a DevOps application scenario to illustrate the key concepts which
apply to scheduled queries in general, irrespective of the application scenario.

Scheduled Queries in Timestream for LiveAnalytics allow you to express your queries using the full SQL surface
area of Timestream for LiveAnalytics. Your query can include one or more source tables, perform aggregations or
any other query allowed by Timestream for LiveAnalytics's SQL language, and then materialize the results of the
query in another destination table in Timestream for LiveAnalytics. For ease of exposition, this section refers
to this target table of a scheduled query as a _derived
table_.

The following are the key points that are covered in this section.

- Using a simple fleet-level aggregate to explain how you can define a scheduled
  query and understand some basic concepts.
- How you can combine results from the target of a scheduled query (the derived
  table) with the results from the source table to get the cost and performance
  benefits of scheduled query.
- What are your trade-offs when configuring the refresh period of the scheduled
  queries.
- Using scheduled queries for some common scenarios.
  - Tracking the last data point from every instance before a specific
    date.
  - Distinct values for a dimension to use for populating variables in a
    dashboard.

- How you handle late arriving data in the context of scheduled queries.
- How you can use one-off manual executions to handle a variety of scenarios not
  directly covered by automated triggers for scheduled queries.

###### Topics

- [Scenario](scheduledqueries-patterns-scenario.md "scheduledqueries-patterns-scenario.md")
- [Simple fleet-level
  aggregates](scheduledqueries-patterns-simplefleet.md "scheduledqueries-patterns-simplefleet.md")
- [Last point from each
  device](scheduledqueries-patterns-lastpointfromdevice.md "scheduledqueries-patterns-lastpointfromdevice.md")
- [Unique dimension
  values](scheduledqueries-patterns-uniquedimvalues.md "scheduledqueries-patterns-uniquedimvalues.md")
- [Handling late-arriving
  data](scheduledqueries-patterns-latearrive.md "scheduledqueries-patterns-latearrive.md")
- [Back-filling historical
  pre-computations](scheduledqueries-patterns-backfilling.md "scheduledqueries-patterns-backfilling.md")
