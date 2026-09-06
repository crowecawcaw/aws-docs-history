

# Search features and limits
<a name="search-features-limits"></a>

## Search availability
<a name="search-availability"></a>

ElastiCache Valkey version 9.0 and above provides support for pure non vector, vector, and hybrid workloads including Numeric, Tag (exact-match), Full-text, Vector searches, and Aggregations on node-based clusters in all AWS Regions at no additional cost.

ElastiCache Valkey version 8.2 provides support for Vector Search on node-based clusters in all AWS Regions at no additional cost.

You can also use search on your existing clusters by upgrading from any version of Valkey, or Redis OSS to Valkey versions mentioned above, in a [few clicks with no downtime](VersionManagement.HowTo.md).

Search is currently available on all ElastiCache instance types other than nodes with data tiering. Using search on t2, t3, and t4g instances requires increasing the memory reserve to at least 50% for micro and 30% for small instances. See [this page](redis-memory-management.md) to find out more.

## Parametric restrictions
<a name="parametric-restrictions"></a>

The following table shows limits for various search items:


**Search limits**  

| Item | Maximum value (9.0\+) | Maximum value (8.2) | 
| --- | --- | --- | 
| Number of dimensions in a vector | 32768 | 32768 | 
| Number of indexes that can be created | 1000 | 10 | 
| Number of fields in an index | 1000 | 50 | 
| FT.SEARCH TIMEOUT clause (milliseconds) | 60000 | 60000 | 
| Maximum number of prefixes allowed per index | 16 | 16 | 
| Maximum length of a tag field | 10000 | 10000 | 
| Maximum length of a numeric field | 256 | 256 | 
| HNSW M parameter | 2000000 | 2000000 | 
| HNSW EF\_CONSTRUCTION parameter | 1000000 | 4096 | 
| HNSW EF\_RUNTIME parameter | 1000000 | 4096 | 
| Number of terms allowed to be used in a query string in FT.SEARCH/FT.AGGREGATE commands | 1000 | 16 | 
| Number of text attributes allowed per index | 64 | NA | 
| Maximum text word expansions in Prefix, Suffix, Fuzzy, and Stem Term Searches | 200 | NA | 

## Operational restrictions
<a name="operational-restrictions"></a>

### Index Persistence and Backfilling
<a name="index-persistence-backfilling"></a>

You can read more about this at [Valkey search index creation and backfill](https://valkey.io/topics/search/#index-creation-and-backfill).

### Scaling limits
<a name="scaling-limits"></a>

In ElastiCache Valkey version 9.0, during scaling events, the write RPS may reduce for the duration of the event. In ElastiCache Valkey version 8.2, during scaling events, the index may undergo backfill as data is migrated and this will result in a reduced recall for search queries.

### Snapshot import/export and Live Migration
<a name="snapshot-import-export"></a>

The RDB files from the one cluster with search indexes can be imported to another ElastiCache Valkey cluster with version 8.2 or higher. The new cluster will rebuild the index content on loading the RDB file. However, the presence of search indexes in an RDB file limits the compatibility of that data with prior versions of Valkey. The format of the search indexes defined by the vector search functionality is only understood by another ElastiCache cluster with Valkey version 8.2 or higher. However, RDB files that do not contain indexes are not restricted in this fashion.

### Out of Memory during backfill
<a name="out-of-memory-backfill"></a>

Similar to Valkey OSS write operations, an index backfill is subjected to out-of-memory limitations. If engine memory is filled up while a backfill is in progress, all backfills are paused. If memory becomes available, the backfill process is resumed. It is possible to delete an index when backfill is paused due to out of memory.

### Write throttling with durability enabled
<a name="search-write-throttling-durability"></a>

When durability is enabled and search indexes are configured, write commands targeting indexed keys may be throttled to maintain transactional log performance. For details, see [Search write throttling](Durability.SearchThrottling.md).

### Transactions
<a name="transactions"></a>

The commands `FT.CREATE` and `FT.DROPINDEX`, cannot be executed in a transactional context, i.e., not within a `MULTI/EXEC` block or within a LUA or FUNCTION script. Additionally, the `FT.SEARCH` and `FT.AGGREGATE` commands cannot be executed in a transactional context in a ElastiCache Valkey Cluster operating in Cluster Mode.

## Search security
<a name="search-security"></a>

[Valkey ACL (Access Control Lists)](https://valkey.io/topics/acl/) security mechanisms for both command and data access are extended to control the search facility. ACL control of individual search commands is fully supported. A new ACL category, `@search`, is provided and many of the existing categories (`@fast`, `@read`, `@write`, etc.) are updated to include the new commands. Search commands do not modify key data, meaning that the existing ACL machinery for write access is preserved. The access rules for `HASH` and `JSON` operations are not modified by the presence of an index; normal key-level access control is still applied to those commands.

Search commands with an index also have their access controlled through ACL. Access checks are performed at the whole-index level, not at the per-key level. This means that access to an index is granted to a user only if that user has permission to access all possible keys within the keyspace prefix list of that index. In other words, the actual contents of an index don't control the access. Rather, it is the theoretical contents of an index as defined by the prefix list which is used for the security check. Situations where a user has read and/or write access to a key but is unable to access an index containing that key are possible. Note that only read access to the keyspace is required to create or use an index – the presence or absence of write access is not considered.