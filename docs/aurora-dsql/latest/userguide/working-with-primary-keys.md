# Primary keys in Aurora DSQL

In Aurora DSQL, a _primary key_ is a feature that physically organizes
table data. It's similar to the `CLUSTER` operation in PostgreSQL or a clustered index
in other databases. When you define a primary key, Aurora DSQL creates an index that includes all
columns in the table. The primary key structure in Aurora DSQL ensures efficient data access and
management.

## Data structure and storage

When you define a primary key, Aurora DSQL stores table data in primary key order. This
index-organized structure allows a primary key lookup to retrieve all column values directly,
instead of following a pointer to the data as in a traditional B-tree index. Unlike the
`CLUSTER` operation in PostgreSQL, which reorganizes data only once, Aurora DSQL maintains
this order automatically and continuously. This approach improves the performance of queries that rely on
primary key access.

Aurora DSQL also uses the primary key to generate a cluster-wide unique key for each row in
tables and indexes. This unique key also underpins
distributed data management. It enables automatic partitioning of data across multiple
nodes, supporting scalable storage and high concurrency. As a result, the primary key
structure helps Aurora DSQL scale automatically and manage concurrent workloads
efficiently.

## Guidelines for choosing a primary key

When choosing and using a primary key in Aurora DSQL, consider the following
guidelines:

- Define a primary key when you create a table. You can't change this key or add a new
  primary key later. The primary key becomes part of the cluster-wide key used for data
  partitioning and automatic scaling of write throughput. If you don't specify a primary
  key, Aurora DSQL assigns a synthetic hidden ID.
- For tables with high write volumes, avoid using monotonically increasing integers as
  primary keys. This can lead to performance issues by directing all new inserts to a
  single partition. Instead, use primary keys with random distribution to ensure even
  distribution of writes across storage partitions.
- For tables that change infrequently or are read-only, you can use an ascending key.
  Examples of ascending keys are timestamps or sequence numbers. A dense key has many
  closely spaced or duplicate values. You can use an ascending key even if it is dense
  because write performance is less critical.
- If a full table scan doesn't meet your performance requirements, choose a more
  efficient access method. In most cases, this means using a primary key that matches your
  most common join and lookup key in queries.
- The maximum combined size of columns in a primary key is 1 kibibyte. For more
  information, see [Database
  limits in Aurora DSQL](CHAP_quotas.md#SECTION_database-limits "CHAP_quotas.md#SECTION_database-limits") and [Supported data types in Aurora DSQL](working-with-postgresql-compatibility-supported-data-types.md "working-with-postgresql-compatibility-supported-data-types.md").
- You can include up to 8 columns in a primary key or a secondary index. For more
  information, see [Database
  limits in Aurora DSQL](CHAP_quotas.md#SECTION_database-limits "CHAP_quotas.md#SECTION_database-limits") and [Supported data types in Aurora DSQL](working-with-postgresql-compatibility-supported-data-types.md "working-with-postgresql-compatibility-supported-data-types.md").
