# Aurora PostgreSQL Limitless Database architecture

Limitless Database achieves scale with a two-layer architecture consisting of multiple database nodes. Nodes are either routers or
shards.

- Shards are Aurora PostgreSQL DB instances that each store a subset of the data for your database, allowing for simultaneous processing to
  achieve higher write throughput.
- Routers manage the distributed nature of the database and present a single database image to database clients. Routers maintain metadata
  about where data is stored, parse incoming SQL commands and send those commands to shards. Then they aggregate data from shards to return a
  single result to the client, and manage distributed transactions to maintain consistency across the entire distributed database.
  Aurora PostgreSQL Limitless Database differs from standard [Aurora DB clusters](Aurora.md "Aurora.md") by having a DB shard group instead of a
  writer DB instance and reader DB instances. All of the nodes that make up your Limitless Database architecture are contained in the DB shard group. The
  individual shards and routers in the DB shard group aren't visible in your AWS account. You use the DB cluster endpoint to access Limitless Database.

The following figure shows the high-level architecture of Aurora PostgreSQL Limitless Database.

![High-level architecture of Aurora PostgreSQL Limitless Database showing primary cluster, shard groups, and data distribution.](images/limitless_high_level_arch_GA.png)
For more information on the architecture of Aurora PostgreSQL Limitless Database and how you can use it, see this video on the AWS
Events channel on YouTube:

For more information on the architecture of a standard Aurora DB cluster, see [Amazon Aurora DB clusters](Aurora.md "Aurora.md").

## Key terms for Aurora PostgreSQL Limitless Database

**DB shard group**

A container for Limitless Database nodes (shards and routers).

**Router**

A node that accepts SQL connections from clients, sends SQL commands to shards, maintains system-wide
consistency, and returns results to clients.

**Shard**

A node that stores a subset of sharded tables, full copies of reference tables, and standard tables. Accepts queries from routers,
but can't be connected to directly by the clients.

**Sharded table**

A table with its data partitioned across shards.

**Shard key**

A column or set of columns in a sharded table that's used to determine partitioning across shards.

**Collocated tables**

Two sharded tables that share the same shard key and are explicitly declared as collocated. All data for the same shard key value
is sent to the same shard.

**Reference table**

A table with its data copied in full on every shard.

**Standard table**

The default table type in Limitless Database. You can convert standard tables into sharded and reference tables.

All standard tables are stored on the same shard selected by the system, enabling joins between standard tables to be performed
within a single shard. However, standard tables are limited by the shard's maximum capacity (128 TiB). This shard also stores data
from sharded and reference tables, so the effective limit for standard tables is lower than 128 TiB.

## Table types for Aurora PostgreSQL Limitless Database

Aurora PostgreSQL Limitless Database supports three types of table: _sharded_, _reference_, and
_standard_.

Sharded tables have their data distributed across all of the shards in the DB shard group. Limitless Database does this automatically by using a
_shard key_, which is a column or set of columns that you specify when partitioning the table. All of the
data with the same value for the shard key is sent to the same shard. Sharding is hash-based, not range- or list-based.

The following are good use cases for sharded tables:

- The application works with a distinct subset of data.
- The table is very large.
- The table potentially grows faster than other tables.

Sharded tables can be _collocated_, meaning that they share the same shard key, and that all of the data from
both tables with the same shard key value is sent to the same shard. If you collocate tables and join them using the shard key, the join can be
performed on a single shard because all of the necessary data is present on that shard.

Reference tables have a full copy of all their data on every shard in the DB shard
group. Reference tables are commonly used for smaller tables with a lower write
volume, but that still need to be joined frequently and don't lend themselves to
sharding. Examples of reference tables include date tables, and tables of geographic
data such as state, city, and postal code.

Standard tables are the default table type in Aurora PostgreSQL Limitless Database. They aren't distributed tables. Aurora PostgreSQL Limitless Database supports joins between standard tables and
standard, sharded, and reference tables.

## Billing for Aurora PostgreSQL Limitless Database

For information on how you're charged for Aurora PostgreSQL Limitless Database, see [DB instance billing for Aurora](User_DBInstanceBilling.md "User_DBInstanceBilling.md").

For Aurora pricing information, see the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing "https://aws.amazon.com/rds/aurora/pricing").
