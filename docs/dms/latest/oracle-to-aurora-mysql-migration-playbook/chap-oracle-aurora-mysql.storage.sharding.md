# Oracle sharding

With AWS DMS, you can shard an Oracle database across multiple data stores to scale write throughput and distribute data horizontally. Oracle sharding is a database architecture that partitions data across multiple Oracle databases, providing horizontal scalability and improved performance.

| Feature compatibility | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                 |
| --------------------- | ---------------------------------- | ------------------------- | ------------------------------- |
| No compatibility      | No automation                      | N/A                       | MySQL doesn’t support sharding. |

## Oracle usage

Sharding is a method of data architecture where table data is horizontally partitioned across independent databases. These databases are called shards. All of the shards make up a single logical database, which is referred to as a sharded database (SDB). Sharding a table is process of splitting this table between different shards where each shards will have sharded table with the same structure but different subset of rows.

Oracle 18c introduces following sharding enhancements:

- User-defined sharding. Before Oracle 18c data was redirected across shards by system. With user-defined sharding, users are now able to explicitly redirect sharded table data to specific individual shards.
- Using JSON, BLOB, CLOB and spatial objects functionality in a sharded environment. You can now use these objects in sharded tables.

For more information, see [Overview of Oracle Sharding](https://docs.oracle.com/en/database/oracle/oracle-database/18/shard/sharding-overview.html#GUID-0F39B1FB-DCF9-4C8A-A2EA-88705B90C5BF "https://docs.oracle.com/en/database/oracle/oracle-database/18/shard/sharding-overview.html#GUID-0F39B1FB-DCF9-4C8A-A2EA-88705B90C5BF") in the _Oracle documentation_.

## MySQL usage

There is no equivalent option in MySQL. The most equivalent option will be to create application level sharding management that will interact with data that is spread across multiple instances.

Another option will be to assess the requirements and probably use another data store such as Amazon Redshift, Amazon EMR, or Amazon DynamoDB.
