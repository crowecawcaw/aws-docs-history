# Use write sharding to evenly distribute workloads across partitions

One way to better distribute writes across a partition in Amazon Keyspaces is to expand the space.
You can do this in several different ways. You can add an additional partition key column to
which you write random numbers to distribute the rows among partitions. Or you can use a
number that is calculated based on something that you're querying on.

## Sharding using compound partition keys and random values

One strategy for distributing loads more evenly across a partition is to add an
additional partition key column to which you write random numbers. Then you randomize
the writes across the larger space.

For example, consider the following table which has a single partition key
representing a date.

```
CREATE TABLE IF NOT EXISTS tracker.blogs (
   publish_date date,
   title text,
   description int,
   PRIMARY KEY (publish_date));
```

To more evenly distribute this table across partitions, you could include an
additional partition key column `shard` that stores random numbers. For
example:

```
CREATE TABLE IF NOT EXISTS tracker.blogs (
   publish_date date,
   shard int,
   title text,
   description int,
   PRIMARY KEY ((publish_date, shard)));
```

When inserting data you might choose a random number between `1` and `200` for the `shard` column. This yields compound
partition key values
like `(2020-07-09, 1)`, `(2020-07-09, 2)`, and so on, through `(2020-07-09, 200)`.
Because you are randomizing the partition key, the writes to
the table on each day are spread evenly across multiple partitions. This results in better parallelism and higher overall throughput.

However, to read all the rows for a given day, you would have to query the rows for
all the shards and then merge the results. For example, you would first issue a
`SELECT` statement for the partition key value `(2020-07-09,
 1)`. Then issue another `SELECT` statement for `(2020-07-09,
 2)`, and so on, through `(2020-07-09, 200)`. Finally, your application
would have to merge the results from all those `SELECT` statements.

## Sharding using compound partition keys and calculated values

A randomizing strategy can greatly improve write throughput. But it's difficult to
read a specific row because you don't know which value was written to the
`shard` column when the row was written. To make it easier to read
individual rows, you can use a different strategy. Instead of using a random number to
distribute the rows among partitions, use a number that you can calculate based upon
something that you want to query on.

Consider the previous example, in which a table uses today's date in the partition
key. Now suppose that each row has an accessible `title` column, and that you
most often need to find rows by title in addition to date. Before your application
writes the row to the table, it could calculate a hash value based on the title and use
it to populate the `shard` column. The calculation might generate a number
between 1 and 200 that is fairly evenly distributed, similar to what the random strategy
produces.

A simple calculation would likely suffice, such as the product of the UTF-8 code point
values for the characters in the title, modulo 200, + 1. The compound partition key
value would then be the combination of the date and calculation result.

With this strategy, the writes are spread evenly across the partition key values, and thus
across the physical partitions. You can easily perform a `SELECT` statement for a
particular row and date because you can calculate the partition key value for a specific
`title` value.

To read all the rows for a given day, you still must `SELECT` each of the
`(2020-07-09, N)` keys (where `N` is 1–200), and your
application then has to merge all the results. The benefit is that you avoid having a
single "hot" partition key value taking all of the workload.
