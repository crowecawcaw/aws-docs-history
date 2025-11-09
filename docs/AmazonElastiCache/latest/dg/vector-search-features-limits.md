# Vector search features and limits

## Vector search availability

Vector search for Amazon ElastiCache is available with Valkey version 8.2 on node-based clusters in all AWS Regions at no additional cost. You can also use vector search on your existing clusters by upgrading from any version of Valkey, or Redis OSS to Valkey 8.2, in a [few clicks with no downtime](VersionManagement.md "VersionManagement.md").

Vector search is available on all ElastiCache supported instance types. Using vector search on t2, t3, and t4g instances requires increasing the memory reserve to at least 50% for micro and 30% for small instances. See [this page](redis-memory-management.md "redis-memory-management.md") to find out more.

## Parametric restrictions

The following table shows limits for various vector search items:

| Vector search limits                         | Item    | Maximum value |
| -------------------------------------------- | ------- | ------------- |
| Number of dimensions in a vector             | 32768   |
| Number of indexes that can be created        | 10      |
| Number of fields in an index                 | 50      |
| FT.SEARCH TIMEOUT clause (milliseconds)      | 60000   |
| Maximum number of prefixes allowed per index | 16      |
| Maximum length of a tag field                | 10000   |
| Maximum length of a numeric field            | 256     |
| HNSW M parameter                             | 2000000 |
| HNSW EF_CONSTRUCTION parameter               | 4096    |
| HNSW EF_RUNTIME parameter                    | 4096    |

## Operational restrictions

### Index Persistence and Backfilling

The update process has three steps. In the first step, the HASH or JSON key is modified and the requesting client is blocked. The second step is performed in the background and updates each of the indexes that contain the modified key. In the third step, the client is unblocked. Thus, for query operations performed on the same connection as a mutation, that change is immediately visible in the search results. However, an insert or update of a key may not be visible in search results for other clients for a short period of time. During periods of heavy system load and/or heavy mutation of data, the visibility delay can become longer.

The vector search feature persists the definition of indexes, and the content of the indexes. Indexes for vector fields are saved but the indexes for TAGS and NUMERIC are not saved, meaning that they must be rebuilt when loaded externally (full sync or a reload). This means that during any operational request or event that causes a node to start or restart, the index definition and content for vectors are restored from the latest snapshot. No user action is required to initiate this. However for TAGS and NUMERIC indexes the rebuild is performed as a backfill operation as soon as data is restored. This is functionally equivalent to the system automatically executing an FT.CREATE command for each defined index. Note that the node becomes available for application operations as soon as the data is restored, but likely before index backfill has completed, meaning that backfill operations will again become visible to applications.

The completion of index backfill is not synchronized between a primary and a replica. This lack of synchronization can unexpectedly become visible to applications, so it is recommended that applications verify backfill completion on primaries and all replicas before initiating search operations.

### Scaling limits

During scaling events, the index may undergo backfill as data is migrated. This will result in a reduced recall for search queries.

### Snapshot import/export and Live Migration

The RDB files from the one cluster with search indexes can be imported to another ElastiCache Valkey cluster with version 8.2 or higher. The new cluster will rebuild the index content on loading the RDB file. However, the presence of search indexes in an RDB file limits the compatibility of that data with prior versions of Valkey. The format of the search indexes defined by the vector search functionality is only understood by another ElastiCache cluster with Valkey version 8.2 or higher. However, RDB files that do not contain indexes are not restricted in this fashion.

### Out of Memory during backfill

Similar to Valkey OSS write operations, an index backfill is subjected to out-of-memory limitations. If engine memory is filled up while a backfill is in progress, all backfills are paused. If memory becomes available, the backfill process is resumed. It is possible to delete an index when backfill is paused due to out of memory.

### Transactions

The commands `FT.CREATE`, `FT.DROPINDEX`, `FT.ALIASADD`, `FT.ALIASDEL`, and `FT.ALIASUPDATE` cannot be executed in a transactional context, i.e., not within a `MULTI/EXEC` block or within a LUA or FUNCTION script.
