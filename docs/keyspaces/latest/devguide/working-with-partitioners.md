# Working with partitioners in Amazon Keyspaces

In Apache Cassandra, partitioners control which nodes data is stored on in the cluster.
Partitioners create a numeric token using a hashed value of the partition key. Cassandra
uses this token to distribute data across nodes. Clients can also use these tokens in
`SELECT` operations and `WHERE` clauses to optimize read and write
operations. For example, clients can efficiently perform parallel queries on large tables by
specifying distinct token ranges to query in each parallel job.

Amazon Keyspaces provides three different partitioners.

**Murmur3Partitioner (Default)**

Apache Cassandra-compatible `Murmur3Partitioner`. The `Murmur3Partitioner` is the default Cassandra partitioner in Amazon Keyspaces and in Cassandra 1.2 and later versions.

**RandomPartitioner**

Apache Cassandra-compatible `RandomPartitioner`. The `RandomPartitioner` is the default Cassandra partitioner for versions earlier than Cassandra 1.2.

**Keyspaces Default Partitioner**
The `DefaultPartitioner` returns the same `token` function results as the `RandomPartitioner`.

The partitioner setting is applied per Region at the account level. For example, if you change the partitioner in US East (N. Virginia), the change
is applied to all tables in the same account in this Region. You can safely change your partitioner at any time. Note that the configuration change takes
approximately 10 minutes to complete. You do not need to
reload your Amazon Keyspaces data when you change the partitioner setting. Clients will automatically
use the new partitioner setting the next time they connect.
