# Estimate the read capacity consumption of table scans

Queries that result in full table scans, for example queries using the `ALLOW FILTERING` option, are another
example of queries that process more reads than what they return as results. And the read capacity consumption is based on the data
read, not the data returned.

For the table scan example we use the following example table in on-demand capacity mode.

```
`pk | ck | value
---+----+---------
pk | 10 | <any value that results in a row size larger than 4KB>
pk | 20 | value_1
pk | 30 | <any value that results in a row size larger than 4KB>`
```

Amazon Keyspaces creates a table in on-demand capacity mode with four partitions by default. In this example table,
all the data is stored in one partition and the remaining three partitions are empty.

Now run the following query on the table.

```
SELECT * from amazon_keyspaces.example_table_2;
```

This query results in a table scan operation where Amazon Keyspaces scans all four partitions of the table and consumes
6 RRUs in `LOCAL_QUORUM` consistency mode. First, Amazon Keyspaces consumes 3 RRUs for reading the three rows with `pk=‘pk’`. Then, Amazon Keyspaces consumes the
additional 3 RRUs for scanning the three empty partitions of the table. Because this query results in a table scan,
Amazon Keyspaces scans all the partitions in the table, including partitions without data.
