# Estimate capacity consumption for static columns in Amazon Keyspaces

In an Amazon Keyspaces table with clustering columns, you can use the `STATIC` keyword to
create a static column. The value stored in a static column
is shared between all rows in a logical partition. When you update the value of this
column, Amazon Keyspaces applies the change automatically to all rows in the partition.

This section describes how to calculate the encoded size of data when you're writing
to static columns. This process is handled separately from the process that writes data
to the nonstatic columns of a row. In addition to size quotas for static data, read and
write operations on static columns also affect metering and throughput capacity for
tables independently. For functional differences with Apache Cassandra when using static
columns and paginated range read results, see [Pagination](functional-differences.md#functional-differences.paging "functional-differences.md#functional-differences.paging").

###### Topics

- [Calculate the static column size per logical
  partition in Amazon Keyspaces](static-columns-estimate.md "static-columns-estimate.md")
- [Estimate capacity throughput requirements for read/write operations on static
  data in Amazon Keyspaces](static-columns-metering.md "static-columns-metering.md")
