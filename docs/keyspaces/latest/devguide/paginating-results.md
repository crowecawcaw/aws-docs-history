# Paginate results in Amazon Keyspaces

Amazon Keyspaces automatically _paginates_ the results from `SELECT` statements when the data read to process the `SELECT`
statement exceeds 1 MB. With pagination, the `SELECT` statement results are divided into "pages" of data that
are 1 MB in size (or less). An application can process the first page of
results, then the second page, and so on. Clients should always check for pagination tokens when processing `SELECT` queries that return
multiple rows.

If a client supplies a `PAGE SIZE` that requires reading more than 1 MB of data,
Amazon Keyspaces breaks up the results automatically into multiple pages based on the 1 MB data-read increments.

For example, if the average size of a row is 100 KB and you specify a `PAGE SIZE` of 20, Amazon Keyspaces paginates data automatically after it
reads 10 rows (1000 KB of data read).

Because Amazon Keyspaces paginates results based on the number of rows that it reads to process a
request and not the number of rows returned in the result set, some pages may not
contain any rows if you are running filtered queries.

For example, if you set `PAGE SIZE` to 10 and Keyspaces evaluates 30 rows
to process your `SELECT` query, Amazon Keyspaces will return three pages. If only a
subset of the rows matched your query, some pages may have less than 10 rows. For an
example how the `PAGE SIZE` of `LIMIT` queries can affect read
capacity, see [Estimate the read capacity consumption of limit queries](limit_queries.md "limit_queries.md").

For a comparison with Apache Cassandra pagination, see [Pagination](functional-differences.md#functional-differences.paging "functional-differences.md#functional-differences.paging").
