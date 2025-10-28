# Estimate capacity consumption of lightweight transactions in Amazon Keyspaces

Lightweight transactions (LWT) allow you to perform conditional write
operations against your table data. Conditional update operations are useful when inserting, updating and deleting records
based on conditions that evaluate the current state.

In Amazon Keyspaces, all write operations require LOCAL_QUORUM consistency and there is no additional charge for using LWTs. The difference
for LWTs is that when a LWT condition check results in `FALSE`, Amazon Keyspaces consumes write capacity units (WCUs) or write request units (WRUs).
The number of WCUs/WRUs consumed depends on the size of the row.

For example, if the row size is 2 KB, the failed conditional write consumes two WCUs/WRUs.
If the row doesn’t currently exist in the table, the operation consumes one WCUs/WRUs.

To determine the number of requests that resulted in condition check failures, you can monitor the
`ConditionalCheckFailed` metric in CloudWatch.

## Estimate LWT costs for tables with Time to Live (TTL)

LWTs can require additional read capacity units (RCUs) or read request units (RRUs) for tables configured with TTL that don't use client-side timestamps.
When using `IF EXISTS` or `IF NOT EXISTS` keywords condition check results in `FALSE`, the following capacity
units are consumed:

- RCUs/RRUs – If the row exists, the RCUs/RRUs consumed are based on the size of the existing row.
- RCUs/RRUs – If the row doesn't exist, a single RCU/RRU is consumed.

If the evaluated condition results in a successful write operation, WCUs/WRUs are consumed based on the size of the new row.
