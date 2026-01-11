# Overview of PostgreSQL logical

replication with Aurora

By using PostgreSQL's logical replication feature with your Aurora PostgreSQL DB
cluster, you can replicate and synchronize individual tables rather than the entire
database instance. Logical replication uses a publish and subscribe model to replicate
changes from a source to one or more recipients. It works by using change records from
the PostgreSQL write-ahead log (WAL). The source, or _publisher_,
sends WAL data for the specified tables to one or more recipients
(_subscriber_), thus replicating the changes and keeping a
subscriber's table synchronized with the publisher's table. The set of changes
from the publisher are identified using a _publication_. Subscribers
get the changes by creating a _subscription_ that defines the
connection to the publisher's database and its publications. A
_replication slot_ is the mechanism used in this scheme to track
progress of a subscription.

For Aurora PostgreSQL DB clusters, the WAL records are saved on Aurora storage. The
Aurora PostgreSQL DB cluster that's acting as the publisher in a logical replication
scenario reads the WAL data from Aurora storage, decodes it, and sends it to the
subscriber so that the changes can be applied to the table on that instance. The
publisher uses a _logical decoder_ to decode the data for use by
subscribers. By default, Aurora PostgreSQL DB clusters use the native PostgreSQL
`pgoutput` plugin when sending data. Other logical decoders are
available. For example, Aurora PostgreSQL also supports the `wal2json` plugin that
converts WAL data to JSON.

As of Aurora PostgreSQL version 14.5, 13.8, 12.12, and 11.17, Aurora PostgreSQL augments the
PostgreSQL logical replication process with a _write-through cache_
to improve performance. The WAL transaction logs are cached locally, in a buffer, to
reduce the amount of disk I/O, that is, reading from Aurora storage during logical
decoding. The write-through cache is used by default whenever you use logical
replication for your Aurora PostgreSQL DB cluster. Aurora provides several functions that you
can use to manage the cache. For more information, see [Monitoring the Aurora PostgreSQL logical replication write-through cache](AuroraPostgreSQL.Replication.md#AuroraPostgreSQL.Replication.Logical-write-through-cache "AuroraPostgreSQL.Replication.md#AuroraPostgreSQL.Replication.Logical-write-through-cache").

Logical replication is supported by all currently available Aurora PostgreSQL versions.
For more information, [Amazon Aurora PostgreSQL updates](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md") in the _Release Notes for Aurora PostgreSQL_.

Logical replication is supported by Babelfish for Aurora PostgreSQL from the following
versions:

- 15.7 and higher versions
- 16.3 and higher versions

###### Note

In addition to the native PostgreSQL logical replication feature introduced in
PostgreSQL 10, Aurora PostgreSQL also supports the `pglogical` extension. For
more information, see [Using pglogical to synchronize
data across instances](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").

For more information about PostgreSQL logical replication, see [Logical
replication](https://www.postgresql.org/docs/current/logical-replication.html "https://www.postgresql.org/docs/current/logical-replication.html") and [Logical decoding concepts](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html "https://www.postgresql.org/docs/current/logicaldecoding-explanation.html") in the PostgreSQL documentation.

###### Note

PostgreSQL 16 added support for logical decoding from read replicas. This feature isn't supported on Aurora PostgreSQL.
