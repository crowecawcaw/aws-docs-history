For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Using scheduled queries in Timestream for LiveAnalytics

The scheduled query feature in Amazon Timestream for LiveAnalytics is a fully managed, serverless, and scalable
solution for calculating and storing aggregates, rollups, and other forms of preprocessed
data typically used for operational dashboards, business reports, ad-hoc analytics, and
other applications. Scheduled queries make real-time analytics more performant and
cost-effective, so you can derive additional insights from your data, and can continue to
make better business decisions.

With scheduled queries, you define the real-time analytics queries that compute
aggregates, rollups, and other operations on the data—and Amazon Timestream for LiveAnalytics periodically and
automatically runs these queries and reliably writes the query results into a separate
table. The data is typically calculated and updated into these tables within a few minutes.

You can then point your dashboards and reports to query the tables that contain aggregated
data instead of querying the considerably larger source tables. This leads to performance
and cost gains that can exceed orders of magnitude. This is because the tables with
aggregated data contain much less data than the source tables, so they offer faster queries
and cheaper data storage.

Additionally, tables with scheduled queries offer all of the existing functionality of a
Timestream for LiveAnalytics table. For example, you can query the tables using SQL. You can visualize the data
stored in the tables using Grafana. You can also ingest data into the table using Amazon
Kinesis, Amazon MSK, AWS IoT Core, and Telegraf. You can configure data retention policies
on these tables for automatic data lifecycle management.

Because the data retention of the tables that contain aggregated data is fully decoupled
from that of source tables, you can also choose to reduce the data retention of the source
tables and keep the aggregate data for a much longer duration, at a fraction of the data
storage cost. Scheduled queries make real-time analytics faster, cheaper, and therefore more
accessible to many more customers, so they can monitor their applications and drive better
data-driven business decisions.

###### Topics

- [Benefits](#scheduledqueries-benifits "#scheduledqueries-benifits")
- [Use cases](#scheduledqueries-usescases "#scheduledqueries-usescases")
- [Example](#scheduledqueries-example "#scheduledqueries-example")
- [Concepts](scheduledqueries-concepts.md "scheduledqueries-concepts.md")
- [Schedule expressions](scheduledqueries-schedule.md "scheduledqueries-schedule.md")
- [Data model mappings](scheduledqueries-mappings.md "scheduledqueries-mappings.md")
- [Notification messages](scheduledqueries-notification.md "scheduledqueries-notification.md")
- [Error reports](scheduledqueries-errorreport.md "scheduledqueries-errorreport.md")
- [Patterns and examples](scheduledqueries-examplesandpatterns.md "scheduledqueries-examplesandpatterns.md")

## Scheduled query benefits

The following are the benefits of scheduled queries:

- Operational ease – Scheduled queries are
  serverless and fully managed.
- Performance and cost – Because scheduled
  queries precompute the aggregates, rollups, or other real-time analytics
  operations for your data and store the results in a table, queries that access
  tables populated by scheduled queries contain less data than the source tables.
  Therefore, queries that are run on these tables are faster and cheaper. Tables
  populated by scheduled computations contain less data than their source tables,
  and therefore help reduce the storage cost. You can also retain this data for a
  longer duration in the memory store at a fraction of the cost of retaining the
  source data in the memory store.
- Interoperability – Tables populated by
  scheduled queries offer all of the existing functionality of Timestream for LiveAnalytics tables and can
  be used with all of the services and tools that work with Timestream for LiveAnalytics. See [Working with Other
  Services](OtherServices.md "OtherServices.md") for details.

## Scheduled query use cases

You can use scheduled queries for business reports that summarize the end-user
activity from your applications, so you can train machine learning models for
personalization. You can also use scheduled queries for alarms that detect anomalies,
network intrusions, or fraudulent activity, so you can take immediate remedial actions.

Additionally, you can use scheduled queries for more effective data governance. You
can do this by granting source table access exclusively to the scheduled queries, and
providing your developers access to only the tables populated by scheduled queries. This
minimizes the impact of unintentional, long-running queries.

## Example: Using real-time analytics to detect

fraudulent payments and make better business decisions

Consider a payment system that processes transactions sent from multiple point-of-sale
terminals distributed across major metropolitan cities in the United States. You want to
use Amazon Timestream for LiveAnalytics to store and analyze the transaction data, so you can detect fraudulent
transactions and run real-time analytics queries. These queries can help you answer
business questions such as identifying the busiest and least used point-of-sale
terminals per hour, the busiest hour of the day for each city, and the city with most
transactions per hour.

The system process ~100K transactions per minute. Each transaction stored in Amazon Timestream for LiveAnalytics
is 100 bytes. You've configured 10 queries that run every minute to detect various kinds
of fraudulent payments. You've also created 25 queries that aggregate and slice/dice
your data along various dimensions to help answer your business questions. Each of these
queries processes the last hour's data.

You've created a dashboard to display the data generated by these queries. The
dashboard contains 25 widgets, it is refreshed every hour, and it is typically accessed
by 10 users at any given time. Finally, your memory store is configured with a 2-hour
data retention period and the magnetic store is configured to have a 6-month data
retention period.

In this case, you can use real-time analytics queries that recompute the data every
time the dashboard is accessed and refreshed, or use derived tables for the dashboard.
The query cost for dashboards based on real-time analytics queries will be $120.70 per
month. In contrast, the cost of dashboarding queries powered by derived tables will be
$12.27 per month (see [Amazon Timestream for LiveAnalytics
pricing](https://aws.amazon.com/timestream/pricing/ "https://aws.amazon.com/timestream/pricing/")). In this case, using derived tables reduces the query cost by ~10
times.
