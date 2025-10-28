# Estimate capacity consumption of read and write throughput in Amazon Keyspaces

When you read or write data in Amazon Keyspaces, the amount of read/write request units (RRUs/WRUs) or read/write capacity units
(RCUs/WCUs) your query consumes depends on the total amount of data Amazon Keyspaces has to process to run the query. In
some cases, the data returned to the client can be a subset of the data that Amazon Keyspaces had to read
to process the query. For conditional writes, Amazon Keyspaces consumes write capacity even
if the conditional check fails.

To estimate the total amount of data being processed for a request, you have to consider the encoded size of
a row and the total number of rows. This topic covers some examples of common scenarios and access patterns to show
how Amazon Keyspaces processes queries and how that affects capacity consumption. You can follow the examples to estimate
the capacity requirements of your tables and use Amazon CloudWatch to observe the read and write capacity
consumption for these use cases.

For information on how to calculate the encoded size of rows in Amazon Keyspaces, see [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md").

###### Topics

- [Estimate the capacity consumption of range queries in Amazon Keyspaces](range_queries.md "range_queries.md")
- [Estimate the read capacity consumption of limit queries](limit_queries.md "limit_queries.md")
- [Estimate the read capacity consumption of table scans](table_scans.md "table_scans.md")
- [Estimate capacity consumption of lightweight transactions in Amazon Keyspaces](lightweight_transactions.md "lightweight_transactions.md")
- [Estimate capacity consumption for static columns in Amazon Keyspaces](static-columns.md "static-columns.md")
- [Estimate and provision capacity for a multi-Region table in Amazon Keyspaces](tables-multi-region-capacity.md "tables-multi-region-capacity.md")
- [Estimate read and write capacity consumption with Amazon CloudWatch in Amazon Keyspaces](estimate_consumption_cw.md "estimate_consumption_cw.md")
