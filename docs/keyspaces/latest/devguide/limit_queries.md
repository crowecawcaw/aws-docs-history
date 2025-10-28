# Estimate the read capacity consumption of limit queries

When processing a query that uses the `LIMIT` clause, Amazon Keyspaces reads rows up
to the maximum page size when trying to match the condition specified in the query. If
Amazon Keyspaces can't find sufficient matching data that meets the `LIMIT` value on the
first page, one or more paginated calls could be needed. To continue reads on the next
page, you can use a pagination token. The default page size is 1MB. To consume less read
capacity when using `LIMIT` clauses, you can reduce the page size. For more
information about pagination, see [Paginate results in Amazon Keyspaces](paginating-results.md "paginating-results.md").

For an example, let's look at the following query.

```
SELECT * FROM my_table WHERE partition_key=1234 LIMIT 1;
```

If you don’t set the page size, Amazon Keyspaces reads 1MB of data even though it returns only 1 row to you.
To only have Amazon Keyspaces read one row, you can set the page size to 1 for this query. In this case, Amazon Keyspaces would only read one row
provided you don’t have expired rows based on Time-to-live settings or client-side timestamps.

The `PAGE SIZE` parameter determines how many rows Amazon Keyspaces scans from disk for each request,
not how many rows Amazon Keyspaces returns to the client. Amazon Keyspaces applies the filters you provide, for example inequality on non-key columns
or a `LIMIT` after it scans the data on disk. If you don’t explicitly set the
`PAGE SIZE`, Amazon Keyspaces reads up to 1MB of data before applying filters. For example, if you're using `LIMIT 1`
without specifying the `PAGE SIZE`, Amazon Keyspaces could read thousands of rows from disk before applying the
limit clause and returning only a single row.

To avoid over-reading, reduce the `PAGE SIZE` which reduces the number of rows Amazon Keyspaces scans for each fetch. For example,
if you define `LIMIT 5` in your query, set the `PAGE SIZE` to a value between 5 - 10 so that Amazon Keyspaces only
scans 5 - 10 rows on each paginated call. You can modify this number to reduce the number of fetches. For limits that are larger than
the page size, Amazon Keyspaces maintains the total result count with pagination state. In the case of a `LIMIT` of 10,000 rows, Amazon Keyspaces can fetch these
results in two pages of 5,000 rows each. The 1MB limit is the upper bound for any page size set.
