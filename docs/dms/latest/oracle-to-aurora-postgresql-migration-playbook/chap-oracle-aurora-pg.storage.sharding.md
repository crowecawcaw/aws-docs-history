# Oracle sharding

With AWS DMS, you can migrate data from an Oracle database to an Amazon Aurora cluster that utilizes the sharding feature. Oracle sharding refers to the partitioning of data across multiple databases to improve performance and availability.

| Feature compatibility    | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                      |
| ------------------------ | ---------------------------------- | ------------------------- | ------------------------------------ |
| No feature compatibility | No automation                      | N/A                       | PostgreSQL doesn’t support sharding. |

## Oracle usage

Sharding is a method of data architecture where table data is horizontally partitioned across independent databases. These databases are called shards. All of the shards make up a single logical database, which is referred to as a sharded database (SDB). Sharding a table is process of splitting this table between different shards where each shards will have sharded table with the same structure but different subset of rows.

Oracle 18c introduces following sharding enhancements:

- User-defined sharding. Before Oracle 18c, data was redirected across shards by system. With user-defined sharding, users are now able to explicitly redirect sharded table data to specific individual shards.
- Using `JSON`, `BLOB`, `CLOB`, and spatial objects functionality in a sharded environment. These objects can now be used in sharded tables.

For more information, see [Oracle Sharding Overview](https://docs.oracle.com/en/database/oracle/oracle-database/19/shard/sharding-overview.html#GUID-0F39B1FB-DCF9-4C8A-A2EA-88705B90C5BF "https://docs.oracle.com/en/database/oracle/oracle-database/19/shard/sharding-overview.html#GUID-0F39B1FB-DCF9-4C8A-A2EA-88705B90C5BF") in the _Oracle documentation_.
