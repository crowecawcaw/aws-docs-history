

# Overview of PostgreSQL logical replication with Aurora
<a name="AuroraPostgreSQL.Replication.Logical"></a>

By using PostgreSQL's logical replication feature with your Aurora PostgreSQL DB cluster, you can replicate and synchronize individual tables rather than the entire database instance. Logical replication uses a publish and subscribe model to replicate changes from a source to one or more recipients. It works by using change records from the PostgreSQL write-ahead log (WAL). The source, or *publisher*, sends WAL data for the specified tables to one or more recipients (*subscriber*), thus replicating the changes and keeping a subscriber's table synchronized with the publisher's table. The set of changes from the publisher are identified using a *publication*. Subscribers get the changes by creating a *subscription* that defines the connection to the publisher's database and its publications. A *replication slot* is the mechanism used in this scheme to track progress of a subscription. 

For Aurora PostgreSQL DB clusters, the WAL records are saved on Aurora storage. The Aurora PostgreSQL DB cluster that's acting as the publisher in a logical replication scenario reads the WAL data from Aurora storage, decodes it, and sends it to the subscriber so that the changes can be applied to the table on that instance. The publisher uses a *logical decoder* to decode the data for use by subscribers. By default, Aurora PostgreSQL DB clusters use the native PostgreSQL `pgoutput` plugin when sending data. Other logical decoders are available. For example, Aurora PostgreSQL also supports the `[wal2json](https://github.com/eulerto/wal2json)` plugin that converts WAL data to JSON. 

As of Aurora PostgreSQL version 14.5, 13.8, 12.12, and 11.17, Aurora PostgreSQL augments the PostgreSQL logical replication process with a *write-through cache* to improve performance. The WAL transaction logs are cached locally, in a buffer, to reduce the amount of disk I/O, that is, reading from Aurora storage during logical decoding. The write-through cache is used by default whenever you use logical replication for your Aurora PostgreSQL DB cluster. Aurora provides several functions that you can use to manage the cache. For more information, see [Monitoring the Aurora PostgreSQL logical replication write-through cache](AuroraPostgreSQL.Replication.Logical-monitoring.md#AuroraPostgreSQL.Replication.Logical-write-through-cache). 

Logical replication is supported by all currently available Aurora PostgreSQL versions. For more information, [Amazon Aurora PostgreSQL updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html) in the *Release Notes for Aurora PostgreSQL*. 

Logical replication is supported by Babelfish for Aurora PostgreSQL from the following versions:
+ 15.7 and higher versions
+ 16.3 and higher versions

**Note**  
In addition to the native PostgreSQL logical replication feature introduced in PostgreSQL 10, Aurora PostgreSQL also supports the `pglogical` extension. For more information, see [Using pglogical to synchronize data across instances](Appendix.PostgreSQL.CommonDBATasks.pglogical.md).

For more information about PostgreSQL logical replication, see [Logical replication](https://www.postgresql.org/docs/current/logical-replication.html) and [Logical decoding concepts](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html) in the PostgreSQL documentation.

**Note**  
PostgreSQL 16 added support for logical decoding from read replicas. This feature isn't supported on Aurora PostgreSQL.