# Supported MongoDB APIs, operations, and data types in Amazon DocumentDB

Amazon DocumentDB (with MongoDB compatibility) is a fast, scalable, highly-available, and fully managed document database service that supports MongoDB workloads.
Amazon DocumentDB is compatible with the MongoDB 3.6, 4.0, 5.0, and 8.0 APIs.
This section lists the supported functionality.
For support using MongoDB APIs and drivers, consult the MongoDB Community Forums.
For support using the Amazon DocumentDB service, contact the appropriate AWS support team.
For functional differences between Amazon DocumentDB and MongoDB, see [Functional differences: Amazon DocumentDB and MongoDB](functional-differences.md "functional-differences.md").

MongoDB commands and operators that are internal-only or not applicable to a fully-managed service are not supported and are not included in the list of supported functionality.

We have added over 50+ additional capabilities since launch, and will continue to work backwards from our customers to deliver the capabilities that they need. For information on the most recent launches, see [Amazon DocumentDB Announcements](https://aws.amazon.com/documentdb/resources/ "https://aws.amazon.com/documentdb/resources/").

If there is a feature that isn't supported that you'd like us to build,
let us know by sending an email with your accountID, the requested
features, and use case to the [Amazon DocumentDB service team](mailto:documentdb-feature-request@amazon.com "mailto:documentdb-feature-request@amazon.com").

###### Topics

- [Database commands](#mongo-apis-database "#mongo-apis-database")
- [Query and projection operators](#mongo-apis-query "#mongo-apis-query")
- [Update operators](#mongo-apis-update "#mongo-apis-update")
- [Geospatial](#mongo-apis-geospatial "#mongo-apis-geospatial")
- [Cursor methods](#mongo-apis-cursor "#mongo-apis-cursor")
- [Aggregation pipeline operators](#mongo-apis-aggregation-pipeline "#mongo-apis-aggregation-pipeline")
- [Data types](#mongo-apis-data-types "#mongo-apis-data-types")
- [Indexes](#mongo-apis-indexes "#mongo-apis-indexes")

## Database commands

###### Topics

- [Administrative commands](#mongo-apis-dababase-administrative "#mongo-apis-dababase-administrative")
- [Aggregation](#mongo-apis-dababase-aggregation "#mongo-apis-dababase-aggregation")
- [Authentication](#mongo-apis-dababase-authentication "#mongo-apis-dababase-authentication")
- [Diagnostic commands](#mongo-apis-dababase-diagnostics "#mongo-apis-dababase-diagnostics")
- [Query and write operations](#mongo-apis-dababase-query-write "#mongo-apis-dababase-query-write")
- [Role management commands](#mongo-apis-database-role-management "#mongo-apis-database-role-management")
- [Sessions commands](#mongo-apis-dababase-sessions "#mongo-apis-dababase-sessions")
- [User management](#mongo-apis-dababase-user-management "#mongo-apis-dababase-user-management")
- [Sharding commands](#mongo-apis-dababase-sharding "#mongo-apis-dababase-sharding")

### Administrative commands

| Command                     | 3.6     | 4.0     | 5.0     | 8.0          | Elastic cluster |
| --------------------------- | ------- | ------- | ------- | ------------ | --------------- |
| Capped Collections          | No      | No      | No      | No           | No              |
| cloneCollectionAsCapped     | No      | No      | No      | No           | No              |
| collMod                     | Partial | Partial | Partial | Partial      | Partial         |
| collMod: expireAfterSeconds | Yes     | Yes     | Yes     | Yes          | Yes             |
| collMod: hidden             | No      | No      | No      | Yes (8.0.1+) | No              |
| convertToCapped             | No      | No      | No      | No           | No              |
| copydb                      | No      | No      | No      | No           | No              |
| create                      | Yes     | Yes     | Yes     | Yes          | Yes             |
| createView                  | No      | No      | No      | Yes          | No              |
| createIndexes               | Yes     | Yes     | Yes     | Yes          | Yes             |
| currentOp                   | Yes     | Yes     | Yes     | Yes          | Yes             |
| drop                        | Yes     | Yes     | Yes     | Yes          | Yes             |
| dropDatabase                | Yes     | Yes     | Yes     | Yes          | Yes             |
| dropIndexes                 | Yes     | Yes     | Yes     | Yes          | Yes             |
| filemd5                     | No      | No      | No      | No           | No              |
| getAuditConfig              | No      | Yes     | Yes     | Yes          | No              |
| killCursors                 | Yes     | Yes     | Yes     | Yes          | Yes             |
| killOp                      | Yes     | Yes     | Yes     | Yes          | Yes             |
| listCollections\*           | Yes     | Yes     | Yes     | Yes          | Yes             |
| listDatabases               | Yes     | Yes     | Yes     | Yes          | Yes             |
| listIndexes                 | Yes     | Yes     | Yes     | Yes          | Yes             |
| reIndex                     | No      | No      | Yes     | Yes          | No              |
| renameCollection            | Yes     | Yes     | Yes     | Yes          | No              |
| setAuditConfig              | No      | Yes     | Yes     | Yes          | No              |

\* The `type` key in the filter option is not supported.

### Aggregation

| Command   | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| --------- | --- | --- | --- | --- | --------------- |
| aggregate | Yes | Yes | Yes | Yes | Yes             |
| count     | Yes | Yes | Yes | Yes | Yes             |
| distinct  | Yes | Yes | Yes | Yes | Yes             |
| mapReduce | No  | No  | No  | Yes | No              |

### Authentication

| Command      | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ------------ | --- | --- | --- | --- | --------------- |
| authenticate | Yes | Yes | Yes | Yes | Yes             |
| logout       | Yes | Yes | Yes | Yes | Yes             |

### Diagnostic commands

| Command                 | 3.6                                | 4.0                                | 5.0                                | 8.0                                | Elastic cluster |
| ----------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | --------------- |
| buildInfo               | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| collStats               | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| connPoolStats           | No                                 | No                                 | No                                 | No                                 | No              |
| connectionStatus        | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| dataSize                | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| dbHash                  | No                                 | No                                 | No                                 | No                                 | No              |
| dbStats                 | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| explain                 | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| explain: executionStats | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| features                | No                                 | No                                 | No                                 | No                                 | No              |
| hostInfo                | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| listCommands            | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| profiler                | [Yes](profiling.md "profiling.md") | [Yes](profiling.md "profiling.md") | [Yes](profiling.md "profiling.md") | [Yes](profiling.md "profiling.md") | No              |
| serverStatus            | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |
| top                     | Yes                                | Yes                                | Yes                                | Yes                                | Yes             |

### Query and write operations

| Command                | 3.6                                          | 4.0                                          | 5.0                                          | 8.0                                          | Elastic cluster |
| ---------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | --------------- |
| Change streams         | [Yes](change_streams.md "change_streams.md") | [Yes](change_streams.md "change_streams.md") | [Yes](change_streams.md "change_streams.md") | [Yes](change_streams.md "change_streams.md") | No              |
| delete                 | Yes                                          | Yes                                          | Yes                                          | Yes                                          | Yes             |
| find                   | Yes                                          | Yes                                          | Yes                                          | Yes                                          | Yes             |
| findAndModify          | Yes                                          | Yes                                          | Yes                                          | Yes                                          | Yes             |
| getLastError           | No                                           | No                                           | No                                           | No                                           | No              |
| getMore                | Yes                                          | Yes                                          | Yes                                          | Yes                                          | Yes             |
| getPrevError           | No                                           | No                                           | No                                           | No                                           | No              |
| GridFS                 | Yes                                          | Yes                                          | Yes                                          | Yes                                          | No              |
| insert                 | Yes                                          | Yes                                          | Yes                                          | Yes                                          | Yes             |
| parallelCollectionScan | No                                           | No                                           | No                                           | No                                           | No              |
| resetError             | No                                           | No                                           | No                                           | No                                           | No              |
| update                 | Yes                                          | Yes                                          | Yes                                          | Yes                                          | Yes             |
| ReplaceOne             | Yes                                          | Yes                                          | Yes                                          | Yes                                          | Yes             |

### Role management commands

| Command                  | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ------------------------ | --- | --- | --- | --- | --------------- |
| createRole               | Yes | Yes | Yes | Yes | No              |
| dropAllRolesFromDatabase | Yes | Yes | Yes | Yes | No              |
| dropRole                 | Yes | Yes | Yes | Yes | No              |
| grantRolesToRole         | Yes | Yes | Yes | Yes | No              |
| revokeRolesFromRole      | Yes | Yes | Yes | Yes | No              |
| revokePrivilegesFromRole | Yes | Yes | Yes | Yes | No              |
| rolesInfo                | Yes | Yes | Yes | Yes | No              |
| updateRole               | Yes | Yes | Yes | Yes | No              |

### Sessions commands

| Command                  | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ------------------------ | --- | --- | --- | --- | --------------- |
| abortTransaction         | No  | Yes | Yes | Yes | No              |
| commitTransaction        | No  | Yes | Yes | Yes | No              |
| endSessions              | No  | No  | No  | No  | No              |
| killAllSessions          | No  | Yes | Yes | Yes | No              |
| killAllSessionsByPattern | No  | No  | No  | No  | No              |
| killSessions             | No  | Yes | Yes | Yes | No              |
| refreshSessions          | No  | No  | No  | No  | No              |
| startSession             | No  | Yes | Yes | Yes | No              |

### User management

| Command                  | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ------------------------ | --- | --- | --- | --- | --------------- |
| createUser               | Yes | Yes | Yes | Yes | Yes             |
| dropAllUsersFromDatabase | Yes | Yes | Yes | Yes | Yes             |
| dropUser                 | Yes | Yes | Yes | Yes | Yes             |
| grantRolesToUser         | Yes | Yes | Yes | Yes | Yes             |
| revokeRolesFromUser      | Yes | Yes | Yes | Yes | Yes             |
| updateUser               | Yes | Yes | Yes | Yes | Yes             |
| usersInfo                | Yes | Yes | Yes | Yes | Yes             |

### Sharding commands

| Command                  | Elastic cluster |
| ------------------------ | --------------- |
| abortReshardCollection   | No              |
| addShard                 | No              |
| addShardToZone           | No              |
| balancerCollectionStatus | No              |
| balancerStart            | No              |
| balancerStatus           | No              |
| balancerStop             | No              |
| checkShardingIndex       | No              |
| clearJumboFlag           | No              |
| cleanupOrphaned          | No              |
| cleanupReshardCollection | No              |
| commitReshardCollection  | No              |
| enableSharding           | Yes             |
| flushRouterConfig        | No              |
| getShardMap              | No              |
| getShardVersion          | No              |
| isdbgrid                 | No              |
| listShards               | No              |
| medianKey                | No              |
| moveChunk                | No              |
| movePrimary              | No              |
| mergeChunks              | No              |
| refineCollectionShardKey | No              |
| removeShard              | No              |
| removeShardFromZone      | No              |
| reshardCollection        | No              |
| setAllowMigrations       | No              |
| setShardVersion          | No              |
| shardCollection          | Yes             |
| shardingState            | No              |
| split                    | No              |
| splitVector              | No              |
| unsetSharding            | No              |
| updateZoneKeyRange       | No              |

## Query and projection operators

###### Topics

- [Array operators](#mongo-apis-query-array-operators "#mongo-apis-query-array-operators")
- [Bitwise operators](#mongo-apis-query-bitwise-operators "#mongo-apis-query-bitwise-operators")
- [Comment operator](#mongo-apis-query-comment-operator "#mongo-apis-query-comment-operator")
- [Comparison operators](#mongo-apis-query-comparison-operators "#mongo-apis-query-comparison-operators")
- [Element operators](#mongo-apis-query-element-operators "#mongo-apis-query-element-operators")
- [Evaluation query operators](#mongo-apis-query-evaluation-operators "#mongo-apis-query-evaluation-operators")
- [Logical operators](#mongo-apis-query-logical-operators "#mongo-apis-query-logical-operators")
- [Projection operators](#mongo-apis-projection-operators "#mongo-apis-projection-operators")

### Array operators

| Command                                   | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------------- | --- | --- | --- | --- | --------------- |
| [$all](all.md "all.md")                   | Yes | Yes | Yes | Yes | Yes             |
| [$elemMatch](elemMatch.md "elemMatch.md") | Yes | Yes | Yes | Yes | Yes             |
| [$size](size-query.md "size-query.md")    | Yes | Yes | Yes | Yes | Yes             |

### Bitwise operators

| Command                                            | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| -------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$bitsAllSet](bitsAllSet.md "bitsAllSet.md")       | Yes | Yes | Yes | Yes | Yes             |
| [$bitsAnySet](bitsAnySet.md "bitsAnySet.md")       | Yes | Yes | Yes | Yes | Yes             |
| [$bitsAllClear](bitsAllClear.md "bitsAllClear.md") | Yes | Yes | Yes | Yes | Yes             |
| [$bitsAnyClear](bitsAnyClear.md "bitsAnyClear.md") | Yes | Yes | Yes | Yes | Yes             |

### Comment operator

| Command                             | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------- | --- | --- | --- | --- | --------------- |
| [$comment](comment.md "comment.md") | Yes | Yes | Yes | Yes | Yes             |

### Comparison operators

| Command                 | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------- | --- | --- | --- | --- | --------------- |
| [$eq](eq.md "eq.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$gt](gt.md "gt.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$gte](gte.md "gte.md") | Yes | Yes | Yes | Yes | Yes             |
| [$in](in.md "in.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$lt](lt.md "lt.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$lte](lte.md "lte.md") | Yes | Yes | Yes | Yes | Yes             |
| [$ne](ne.md "ne.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$nin](nin.md "nin.md") | Yes | Yes | Yes | Yes | Yes             |

### Element operators

| Command                          | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| -------------------------------- | --- | --- | --- | --- | --------------- |
| [$exists](exists.md "exists.md") | Yes | Yes | Yes | Yes | Yes             |
| [$type](type.md "type.md")       | Yes | Yes | Yes | Yes | Yes             |

### Evaluation query operators

| Command                                      | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| -------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$expr](expr.md "expr.md")                   | No  | Yes | Yes | Yes | No              |
| [$jsonSchema](jsonSchema.md "jsonSchema.md") | No  | Yes | Yes | Yes | No              |
| [$mod](mod-query.md "mod-query.md")          | Yes | Yes | Yes | Yes | Yes             |
| [$regex](regex.md "regex.md")                | Yes | Yes | Yes | Yes | Yes             |
| [$text](text.md "text.md")                   | No  | No  | Yes | Yes | No              |
| $where                                       | No  | No  | No  | No  | No              |

### Logical operators

| Command                 | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------- | --- | --- | --- | --- | --------------- |
| [$and](and.md "and.md") | Yes | Yes | Yes | Yes | Yes             |
| [$nor](nor.md "nor.md") | Yes | Yes | Yes | Yes | Yes             |
| [$not](not.md "not.md") | Yes | Yes | Yes | Yes | Yes             |
| [$or](or.md "or.md")    | Yes | Yes | Yes | Yes | Yes             |

### Projection operators

| Command                                             | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| --------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$](dollar-projection.md "dollar-projection.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$elemMatch](elemMatch.md "elemMatch.md")           | Yes | Yes | Yes | Yes | Yes             |
| [$meta](meta.md "meta.md")                          | No  | No  | Yes | Yes | No              |
| [$slice](slice-projection.md "slice-projection.md") | Yes | Yes | Yes | Yes | Yes             |

## Update operators

###### Topics

- [Array operators](#mongo-apis-update-array "#mongo-apis-update-array")
- [Bitwise operators](#mongo-apis-update-bitwise "#mongo-apis-update-bitwise")
- [Field operators](#mongo-apis-update-field "#mongo-apis-update-field")
- [Update modifiers](#mongo-apis-update-modifiers "#mongo-apis-update-modifiers")

### Array operators

| Command                                                                    | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| -------------------------------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$](dollar-update.md "dollar-update.md")                                   | Yes | Yes | Yes | Yes | Yes             |
| [$[]](dollarBrackets-update.md "dollarBrackets-update.md")                 | Yes | Yes | Yes | Yes | Yes             |
| [$[<identifier>]](dollarIdentifier-update.md "dollarIdentifier-update.md") | Yes | Yes | Yes | Yes | Yes             |
| [$addToSet](addToSet.md "addToSet.md")                                     | Yes | Yes | Yes | Yes | Yes             |
| [$pop](pop.md "pop.md")                                                    | Yes | Yes | Yes | Yes | Yes             |
| [$pullAll](pullAll.md "pullAll.md")                                        | Yes | Yes | Yes | Yes | Yes             |
| [$pull](pull.md "pull.md")                                                 | Yes | Yes | Yes | Yes | Yes             |
| [$push](push.md "push.md")                                                 | Yes | Yes | Yes | Yes | Yes             |

### Bitwise operators

| Command                 | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------- | --- | --- | --- | --- | --------------- |
| [$bit](bit.md "bit.md") | Yes | Yes | Yes | Yes | Yes             |

### Field operators

| Operator                                        | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$currentDate](currentDate.md "currentDate.md") | Yes | Yes | Yes | Yes | Yes             |
| [$inc](inc.md "inc.md")                         | Yes | Yes | Yes | Yes | Yes             |
| [$max](max-update.md "max-update.md")           | Yes | Yes | Yes | Yes | Yes             |
| [$min](min-update.md "min-update.md")           | Yes | Yes | Yes | Yes | Yes             |
| [$mul](mul.md "mul.md")                         | Yes | Yes | Yes | Yes | Yes             |
| [$rename](rename.md "rename.md")                | Yes | Yes | Yes | Yes | Yes             |
| [$set](set-update.md "set-update.md")           | Yes | Yes | Yes | Yes | Yes             |
| [$setOnInsert](setOnInsert.md "setOnInsert.md") | Yes | Yes | Yes | Yes | Yes             |
| [$unset](unset-update.md "unset-update.md")     | Yes | Yes | Yes | Yes | Yes             |

### Update modifiers

| Operator                                    | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$each](each.md "each.md")                  | Yes | Yes | Yes | Yes | Yes             |
| [$position](position.md "position.md")      | Yes | Yes | Yes | Yes | Yes             |
| [$slice](slice-update.md "slice-update.md") | Yes | Yes | Yes | Yes | Yes             |
| [$sort](sort-update.md "sort-update.md")    | Yes | Yes | Yes | Yes | Yes             |

## Geospatial

### Geometry specifiers

| Query Selectors                                 | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------------------- | --- | --- | --- | --- | --------------- |
| $box                                            | No  | No  | No  | No  | No              |
| $center                                         | No  | No  | No  | No  | No              |
| $centerSphere                                   | No  | No  | No  | No  | No              |
| [$geometry](geometry.md "geometry.md")          | Yes | Yes | Yes | Yes | Yes             |
| [$maxDistance](maxDistance.md "maxDistance.md") | Yes | Yes | Yes | Yes | Yes             |
| [$minDistance](minDistance.md "minDistance.md") | Yes | Yes | Yes | Yes | Yes             |
| [$nearSphere](nearSphere.md "nearSphere.md")    | Yes | Yes | Yes | Yes | Yes             |
| $polygon                                        | No  | No  | No  | No  | No              |
| $uniqueDocs                                     | No  | No  | No  | No  | No              |

### Query selectors

| Command                                               | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$geoIntersects](geoIntersects.md "geoIntersects.md") | Yes | Yes | Yes | Yes | Yes             |
| [$geoWithin](geoWithin.md "geoWithin.md")             | Yes | Yes | Yes | Yes | Yes             |
| [$near](near.md "near.md")                            | Yes | Yes | Yes | Yes | Yes             |
| [$nearSphere](nearSphere.md "nearSphere.md")          | Yes | Yes | Yes | Yes | Yes             |
| $polygon                                              | No  | No  | No  | No  | No              |
| $uniqueDocs                                           | No  | No  | No  | No  | No              |

## Cursor methods

| Command                  | 3.6 | 4.0 | 5.0 | 8.0          | Elastic cluster |
| ------------------------ | --- | --- | --- | ------------ | --------------- |
| cursor.batchSize()       | Yes | Yes | Yes | Yes          | Yes             |
| cursor.close()           | Yes | Yes | Yes | Yes          | Yes             |
| cursor.collation()       | No  | No  | No  | Yes          | No              |
| cursor.comment()         | Yes | Yes | Yes | Yes          | Yes             |
| cursor.count()           | Yes | Yes | Yes | Yes          | Yes             |
| cursor.explain()         | Yes | Yes | Yes | Yes          | No              |
| cursor.forEach()         | Yes | Yes | Yes | Yes          | Yes             |
| cursor.hasNext()         | Yes | Yes | Yes | Yes          | Yes             |
| cursor.hint()            | Yes | Yes | Yes | Yes          | Yes\*           |
| cursor.isClosed()        | Yes | Yes | Yes | Yes          | Yes             |
| cursor.isExhausted()     | Yes | Yes | Yes | Yes          | No              |
| cursor.itcount()         | Yes | Yes | Yes | Yes          | No              |
| cursor.limit()           | Yes | Yes | Yes | Yes          | No              |
| cursor.map()             | Yes | Yes | Yes | Yes          | No              |
| cursor.max()             | No  | No  | No  | Yes (8.0.1+) | No              |
| cursor.maxScan()         | Yes | Yes | Yes | Yes          | No              |
| cursor.maxTimeMS()       | Yes | Yes | Yes | Yes          | No              |
| cursor.min()             | No  | No  | No  | Yes (8.0.1+) | No              |
| cursor.next()            | Yes | Yes | Yes | Yes          | Yes             |
| cursor.noCursorTimeout() | No  | No  | No  | No           | No              |
| cursor.objsLeftInBatch() | Yes | Yes | Yes | Yes          | No              |
| cursor.pretty()          | Yes | Yes | Yes | Yes          | No              |
| cursor.readConcern()     | Yes | Yes | Yes | Yes          | No              |
| cursor.readPref()        | Yes | Yes | Yes | Yes          | No              |
| cursor.returnKey()       | No  | No  | No  | No           | No              |
| cursor.showRecordId()    | No  | No  | No  | No           | No              |
| cursor.size()            | Yes | Yes | Yes | Yes          | No              |
| cursor.skip()            | Yes | Yes | Yes | Yes          | No              |
| cursor.sort()            | Yes | Yes | Yes | Yes          | No              |
| cursor.tailable()        | No  | No  | No  | No           | No              |
| cursor.toArray()         | Yes | Yes | Yes | Yes          | No              |

\* Index `hint` is supported with index expressions. For example, `db.foo.find().hint({x:1})`.

## Aggregation pipeline operators

###### Topics

- [Accumulator expressions](#mongo-apis-aggregation-pipeline-accumulator-expressions "#mongo-apis-aggregation-pipeline-accumulator-expressions")
- [Arithmetic operators](#mongo-apis-aggregation-pipeline-arithmetic "#mongo-apis-aggregation-pipeline-arithmetic")
- [Array operators](#mongo-apis-aggregation-pipeline-array "#mongo-apis-aggregation-pipeline-array")
- [Boolean operators](#mongo-apis-aggregation-pipeline-boolean "#mongo-apis-aggregation-pipeline-boolean")
- [Comparison operators](#mongo-apis-aggregation-pipeline-comparison "#mongo-apis-aggregation-pipeline-comparison")
- [Conditional expression operators](#mongo-apis-aggregation-pipeline-conditional "#mongo-apis-aggregation-pipeline-conditional")
- [Data type operator](#mongo-apis-aggregation-pipeline-data-type "#mongo-apis-aggregation-pipeline-data-type")
- [Data size operator](#mongo-apis-aggregation-pipeline-data-size "#mongo-apis-aggregation-pipeline-data-size")
- [Date operators](#mongo-apis-aggregation-pipeline-date "#mongo-apis-aggregation-pipeline-date")
- [Literal operator](#mongo-apis-aggregation-pipeline-literal "#mongo-apis-aggregation-pipeline-literal")
- [Merge operator](#mongo-apis-aggregation-pipeline-merge "#mongo-apis-aggregation-pipeline-merge")
- [Natural operator](#mongo-apis-aggregation-pipeline-natural "#mongo-apis-aggregation-pipeline-natural")
- [Set operators](#mongo-apis-aggregation-pipeline-set "#mongo-apis-aggregation-pipeline-set")
- [Stage operators](#mongo-apis-aggregation-pipeline-stage "#mongo-apis-aggregation-pipeline-stage")
- [String operators](#mongo-apis-aggregation-pipeline-string "#mongo-apis-aggregation-pipeline-string")
- [System variables](#mongo-apis-aggregation-pipeline-system-variables "#mongo-apis-aggregation-pipeline-system-variables")
- [Text search operator](#mongo-apis-aggregation-pipeline-text-search "#mongo-apis-aggregation-pipeline-text-search")
- [Type conversion operators](#mongo-apis-aggregation-pipeline-type "#mongo-apis-aggregation-pipeline-type")
- [Variable operators](#mongo-apis-aggregation-pipeline-variable "#mongo-apis-aggregation-pipeline-variable")
- [Trigonometry operators](#mongo-apis-aggregation-pipeline-trigonometry "#mongo-apis-aggregation-pipeline-trigonometry")
- [Bitwise operators (aggregation)](#mongo-apis-aggregation-pipeline-bitwise "#mongo-apis-aggregation-pipeline-bitwise")
- [Timestamp operators](#mongo-apis-aggregation-pipeline-timestamp "#mongo-apis-aggregation-pipeline-timestamp")
- [Miscellaneous operators](#mongo-apis-aggregation-pipeline-misc "#mongo-apis-aggregation-pipeline-misc")

### Accumulator expressions

| Expression                                                     | 3.6 | 4.0 | 5.0 | 8.0          | Elastic cluster |
| -------------------------------------------------------------- | --- | --- | --- | ------------ | --------------- |
| $accumulator                                                   | -   | -   | No  | No           | No              |
| [$addToSet](addToSet-aggregation.md "addToSet-aggregation.md") | Yes | Yes | Yes | Yes          | Yes             |
| [$avg](avg.md "avg.md")                                        | Yes | Yes | Yes | Yes          | Yes             |
| [$bottom](bottom.md "bottom.md")                               | -   | -   | -   | Yes (8.0.1+) | No              |
| [$bottomN](bottomN.md "bottomN.md")                            | -   | -   | -   | Yes (8.0.1+) | No              |
| [$count](count-accumulator.md "count-accumulator.md")          | -   | -   | No  | Yes (8.0.1+) | No              |
| $covariancePop                                                 | No  | No  | No  | No           | No              |
| $covarianceSamp                                                | No  | No  | No  | No           | No              |
| $denseRank                                                     | No  | No  | No  | No           | No              |
| $derivative                                                    | No  | No  | No  | No           | No              |
| $documentNumber                                                | No  | No  | No  | No           | No              |
| $expMovingAvg                                                  | No  | No  | No  | No           | No              |
| [$first](first.md "first.md")                                  | Yes | Yes | Yes | Yes          | Yes             |
| [$firstN](firstN.md "firstN.md")                               | -   | -   | -   | Yes (8.0.1+) | No              |
| $integral                                                      | No  | No  | No  | No           | No              |
| [$last](last.md "last.md")                                     | Yes | Yes | Yes | Yes          | Yes             |
| [$lastN](lastN.md "lastN.md")                                  | -   | -   | -   | Yes (8.0.1+) | No              |
| [$max](max.md "max.md")                                        | Yes | Yes | Yes | Yes          | Yes             |
| [$maxN](maxN.md "maxN.md")                                     | -   | -   | -   | Yes (8.0.1+) | No              |
| [$median](median.md "median.md")                               | -   | -   | -   | Yes (8.0.1+) | No              |
| [$min](min.md "min.md")                                        | Yes | Yes | Yes | Yes          | Yes             |
| [$minN](minN.md "minN.md")                                     | -   | -   | -   | Yes (8.0.1+) | No              |
| [$percentile](percentile.md "percentile.md")                   | -   | -   | -   | Yes (8.0.1+) | No              |
| [$push](push-aggregation.md "push-aggregation.md")             | Yes | Yes | Yes | Yes          | Yes             |
| $rank                                                          | No  | No  | No  | No           | No              |
| $shift                                                         | No  | No  | No  | No           | No              |
| [$stdDevPop](stdDevPop.md "stdDevPop.md")                      | No  | No  | No  | Yes (8.0.1+) | No              |
| [$stdDevSamp](stdDevSamp.md "stdDevSamp.md")                   | No  | No  | No  | Yes (8.0.1+) | No              |
| [$sum](sum.md "sum.md")                                        | Yes | Yes | Yes | Yes          | Yes             |
| [$top](top-accumulator.md "top-accumulator.md")                | -   | -   | -   | Yes (8.0.1+) | No              |
| [$topN](topN.md "topN.md")                                     | -   | -   | -   | Yes (8.0.1+) | No              |

### Arithmetic operators

| Command                                | 3.6 | 4.0 | 5.0          | 8.0          | Elastic cluster |
| -------------------------------------- | --- | --- | ------------ | ------------ | --------------- |
| [$abs](abs.md "abs.md")                | Yes | Yes | Yes          | Yes          | Yes             |
| [$add](add.md "add.md")                | Yes | Yes | Yes          | Yes          | Yes             |
| [$ceil](ceil.md "ceil.md")             | No  | Yes | Yes          | Yes          | Yes             |
| [$divide](divide.md "divide.md")       | Yes | Yes | Yes          | Yes          | Yes             |
| [$exp](exp.md "exp.md")                | No  | Yes | Yes          | Yes          | Yes             |
| [$floor](floor.md "floor.md")          | No  | Yes | Yes          | Yes          | Yes             |
| [$ln](ln.md "ln.md")                   | No  | Yes | Yes          | Yes          | Yes             |
| [$log](log.md "log.md")                | No  | Yes | Yes          | Yes          | Yes             |
| [$log10](log10.md "log10.md")          | No  | Yes | Yes          | Yes          | Yes             |
| [$mod](mod.md "mod.md")                | Yes | Yes | Yes          | Yes          | Yes             |
| [$multiply](multiply.md "multiply.md") | Yes | Yes | Yes          | Yes          | Yes             |
| [$pow](pow.md "pow.md")                | No  | No  | Yes (5.0.1+) | Yes          | No              |
| [$round](round.md "round.md")          | -   | -   | No           | Yes (8.0.1+) | No              |
| [$sqrt](sqrt.md "sqrt.md")             | No  | Yes | Yes          | Yes          | Yes             |
| [$subtract](subtract.md "subtract.md") | Yes | Yes | Yes          | Yes          | Yes             |
| [$trunc](trunc.md "trunc.md")          | No  | No  | No           | Yes (8.0.1+) | No              |

### Array operators

| Command                                               | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$arrayElemAt](arrayElemAt.md "arrayElemAt.md")       | Yes | Yes | Yes | Yes | Yes             |
| [$arrayToObject](arrayToObject.md "arrayToObject.md") | Yes | Yes | Yes | Yes | Yes             |
| [$concatArrays](concatArrays.md "concatArrays.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$filter](filter.md "filter.md")                      | Yes | Yes | Yes | Yes | Yes             |
| [$first](first.md "first.md")                         | -   | -   | Yes | Yes | No              |
| [$in](in-aggregation.md "in-aggregation.md")          | Yes | Yes | Yes | Yes | Yes             |
| [$indexOfArray](indexOfArray.md "indexOfArray.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$isArray](isArray.md "isArray.md")                   | Yes | Yes | Yes | Yes | Yes             |
| [$last](last.md "last.md")                            | -   | -   | Yes | Yes | No              |
| [$objectToArray](objectToArray.md "objectToArray.md") | Yes | Yes | Yes | Yes | Yes             |
| [$range](range.md "range.md")                         | Yes | Yes | Yes | Yes | Yes             |
| [$reverseArray](reverseArray.md "reverseArray.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$sortArray](sortArray.md "sortArray.md")             | No  | No  | No  | Yes | No              |
| [$reduce](reduce.md "reduce.md")                      | Yes | Yes | Yes | Yes | Yes             |
| [$size](size.md "size.md")                            | Yes | Yes | Yes | Yes | Yes             |
| [$slice](slice.md "slice.md")                         | Yes | Yes | Yes | Yes | Yes             |
| [$zip](zip.md "zip.md")                               | Yes | Yes | Yes | Yes | Yes             |

### Boolean operators

| Command                                         | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$and](and-aggregation.md "and-aggregation.md") | Yes | Yes | Yes | Yes | Yes             |
| [$not](not-aggregation.md "not-aggregation.md") | Yes | Yes | Yes | Yes | Yes             |
| [$or](or-aggregation.md "or-aggregation.md")    | Yes | Yes | Yes | Yes | Yes             |

### Comparison operators

| Command                                         | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$cmp](cmp.md "cmp.md")                         | Yes | Yes | Yes | Yes | Yes             |
| [$eq](eq-aggregation.md "eq-aggregation.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$gt](gt-aggregation.md "gt-aggregation.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$gte](gte-aggregation.md "gte-aggregation.md") | Yes | Yes | Yes | Yes | Yes             |
| [$lt](lt-aggregation.md "lt-aggregation.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$lte](lte-aggregation.md "lte-aggregation.md") | Yes | Yes | Yes | Yes | Yes             |
| [$ne](ne-aggregation.md "ne-aggregation.md")    | Yes | Yes | Yes | Yes | Yes             |

### Conditional expression operators

| Command                          | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| -------------------------------- | --- | --- | --- | --- | --------------- |
| [$cond](cond.md "cond.md")       | Yes | Yes | Yes | Yes | Yes             |
| [$ifNull](ifNull.md "ifNull.md") | Yes | Yes | Yes | Yes | Yes             |
| [$switch](switch.md "switch.md") | No  | Yes | Yes | Yes | No              |

### Data type operator

| Command                                            | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| -------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$type](type-aggregation.md "type-aggregation.md") | Yes | Yes | Yes | Yes | Yes             |

### Data size operator

| Command                                      | 3.6 | 4.0 | 5.0 | 8.0          | Elastic cluster |
| -------------------------------------------- | --- | --- | --- | ------------ | --------------- |
| [$binarySize](binarySize.md "binarySize.md") | -   | -   | No  | Yes (8.0.1+) | No              |
| [$bsonSize](bsonSize.md "bsonSize.md")       | -   | -   | No  | Yes (8.0.1+) | No              |

### Date operators

| Command                                                  | 3.6 | 4.0 | 5.0          | 8.0 | Elastic cluster |
| -------------------------------------------------------- | --- | --- | ------------ | --- | --------------- |
| [$dateAdd](dateAdd.md "dateAdd.md")                      | No  | No  | Yes          | Yes | Yes             |
| [$dateDiff](dateDiff.md "dateDiff.md")                   | -   | -   | Yes          | Yes | No              |
| [$dateFromParts](dateFromParts.md "dateFromParts.md")    | No  | No  | Yes (5.0.1+) | No  | No              |
| [$dateFromString](dateFromString.md "dateFromString.md") | Yes | Yes | Yes          | Yes | Yes             |
| [$dateSubtract](dateSubtract.md "dateSubtract.md")       | No  | No  | Yes          | Yes | Yes             |
| [$dateToParts](dateToParts.md "dateToParts.md")          | No  | No  | Yes (5.0.1+) | No  | No              |
| [$dateToString](dateToString.md "dateToString.md")       | Yes | Yes | Yes          | Yes | Yes             |
| [$dateTrunc](dateTrunc.md "dateTrunc.md")                | -   | -   | No           | Yes | No              |
| [$dayOfMonth](dayOfMonth.md "dayOfMonth.md")             | Yes | Yes | Yes          | Yes | Yes             |
| [$dayOfWeek](dayOfWeek.md "dayOfWeek.md")                | Yes | Yes | Yes          | Yes | Yes             |
| [$dayOfYear](dayOfYear.md "dayOfYear.md")                | Yes | Yes | Yes          | Yes | Yes             |
| [$hour](hour.md "hour.md")                               | Yes | Yes | Yes          | Yes | Yes             |
| [$isoDayOfWeek](isoDayOfWeek.md "isoDayOfWeek.md")       | Yes | Yes | Yes          | Yes | Yes             |
| [$isoWeek](isoWeek.md "isoWeek.md")                      | Yes | Yes | Yes          | Yes | Yes             |
| [$isoWeekYear](isoWeekYear.md "isoWeekYear.md")          | Yes | Yes | Yes          | Yes | Yes             |
| [$millisecond](millisecond.md "millisecond.md")          | Yes | Yes | Yes          | Yes | Yes             |
| [$minute](minute.md "minute.md")                         | Yes | Yes | Yes          | Yes | Yes             |
| [$month](month.md "month.md")                            | Yes | Yes | Yes          | Yes | Yes             |
| [$second](second.md "second.md")                         | Yes | Yes | Yes          | Yes | Yes             |
| [$week](week.md "week.md")                               | Yes | Yes | Yes          | Yes | Yes             |
| [$year](year.md "year.md")                               | Yes | Yes | Yes          | Yes | Yes             |

### Literal operator

| Command                             | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------- | --- | --- | --- | --- | --------------- |
| [$literal](literal.md "literal.md") | Yes | Yes | Yes | Yes | Yes             |

### Merge operator

| Command                                            | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| -------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$mergeObjects](mergeObjects.md "mergeObjects.md") | Yes | Yes | Yes | Yes | Yes             |

### Natural operator

| Command                             | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------- | --- | --- | --- | --- | --------------- |
| [$natural](natural.md "natural.md") | Yes | Yes | Yes | Yes | Yes             |

### Set operators

| Command                                                     | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$allElementsTrue](allElementsTrue.md "allElementsTrue.md") | No  | Yes | Yes | Yes | Yes             |
| [$anyElementTrue](anyElementTrue.md "anyElementTrue.md")    | No  | Yes | Yes | Yes | Yes             |
| [$setDifference](setDifference.md "setDifference.md")       | No  | Yes | Yes | Yes | Yes             |
| [$setEquals](setEquals.md "setEquals.md")                   | Yes | Yes | Yes | Yes | Yes             |
| [$setIntersection](setIntersection.md "setIntersection.md") | Yes | Yes | Yes | Yes | Yes             |
| [$setIsSubset](setIsSubset.md "setIsSubset.md")             | Yes | Yes | Yes | Yes | Yes             |
| [$setUnion](setUnion.md "setUnion.md")                      | Yes | Yes | Yes | Yes | Yes             |
| $setWindowFields                                            | No  | No  | No  | No  | No              |

### Stage operators

| Command                                                           | 3.6 | 4.0 | 5.0 | 8.0          | Elastic cluster |
| ----------------------------------------------------------------- | --- | --- | --- | ------------ | --------------- |
| [$addFields](addFields.md "addFields.md")                         | Yes | Yes | Yes | Yes          | Yes             |
| [$bucket](bucket.md "bucket.md")                                  | No  | No  | No  | Yes          | No              |
| $bucketAuto                                                       | No  | No  | No  | No           |
| [$changeStream](changeStream.md "changeStream.md")                | Yes | Yes | Yes | Yes          | No              |
| [$collStats](collStats.md "collStats.md")                         | No  | Yes | Yes | Yes          | No              |
| [$count](count.md "count.md")                                     | Yes | Yes | Yes | Yes          | Yes             |
| [$currentOp](currentOp.md "currentOp.md")                         | Yes | Yes | Yes | Yes          | Yes             |
| $facet                                                            | No  | No  | No  | No           | No              |
| [$geoNear](geoNear.md "geoNear.md")                               | Yes | Yes | Yes | Yes          | Yes             |
| $graphLookup                                                      | No  | No  | No  | No           | No              |
| [$group](group.md "group.md")                                     | Yes | Yes | Yes | Yes          | Yes             |
| [$indexStats](indexStats.md "indexStats.md")                      | Yes | Yes | Yes | Yes          | Yes             |
| [$limit](limit.md "limit.md")                                     | Yes | Yes | Yes | Yes          | Yes             |
| $listLocalSessions                                                | No  | No  | No  | No           | No              |
| $listSessions                                                     | No  | No  | No  | No           | No              |
| [$lookup](lookup.md "lookup.md")                                  | Yes | Yes | Yes | Yes          | Yes             |
| [$match](match.md "match.md")                                     | Yes | Yes | Yes | Yes          | Yes             |
| [$merge](merge.md "merge.md")                                     | -   | -   | No  | Yes          | No              |
| [$out](out.md "out.md")                                           | Yes | Yes | Yes | Yes          | No              |
| $planCacheStats                                                   | -   | -   | No  | No           | No              |
| [$project](project.md "project.md")                               | Yes | Yes | Yes | Yes          | Yes             |
| [$redact](redact.md "redact.md")                                  | Yes | Yes | Yes | Yes          | Yes             |
| [$replaceRoot](replaceRoot.md "replaceRoot.md")                   | Yes | Yes | Yes | Yes          | Yes             |
| [$sample](sample.md "sample.md")                                  | Yes | Yes | Yes | Yes          | Yes             |
| [$set](set-stage.md "set-stage.md")                               | -   | -   | No  | Yes          | No              |
| $setWindowFields                                                  | -   | -   | No  | No           | No              |
| [$skip](skip.md "skip.md")                                        | Yes | Yes | Yes | Yes          | Yes             |
| [$sort](sort.md "sort.md")                                        | Yes | Yes | Yes | Yes          | Yes             |
| [$sortByCount](sortByCount.md "sortByCount.md")                   | No  | No  | No  | Yes (8.0.1+) | No              |
| $unionWith                                                        | -   | -   | No  | No           | No              |
| [$unset](unset-stage.md "unset-stage.md")                         | -   | -   | No  | Yes          | No              |
| [$unwind](unwind.md "unwind.md")                                  | Yes | Yes | Yes | Yes          | Yes             |
| [$replaceWith](replaceWith.md "replaceWith.md")                   | No  | No  | No  | Yes          | No              |
| [$vectorSearch](vectorSearch.md "vectorSearch.md")                | No  | No  | No  | Yes          | No              |
| [$listSearchIndexes](listSearchIndexes.md "listSearchIndexes.md") | -   | -   | -   | Yes (8.0.1+) | No              |

### String operators

| Command                                            | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| -------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$concat](concat.md "concat.md")                   | Yes | Yes | Yes | Yes | Yes             |
| [$indexOfBytes](indexOfBytes.md "indexOfBytes.md") | Yes | Yes | Yes | Yes | Yes             |
| [$indexOfCP](indexOfCP.md "indexOfCP.md")          | Yes | Yes | Yes | Yes | Yes             |
| [$ltrim](ltrim.md "ltrim.md")                      | No  | Yes | Yes | Yes | No              |
| [$regexFind](regexFind.md "regexFind.md")          | -   | -   | Yes | Yes | No              |
| [$regexFindAll](regexFindAll.md "regexFindAll.md") | -   | -   | Yes | Yes | No              |
| [$regexMatch](regexMatch.md "regexMatch.md")       | -   | -   | Yes | Yes | No              |
| [$replaceAll](replaceAll.md "replaceAll.md")       | -   | -   | Yes | Yes | No              |
| [$replaceOne](replaceOne.md "replaceOne.md")       | -   | -   | Yes | Yes | No              |
| [$rtrim](rtrim.md "rtrim.md")                      | No  | Yes | Yes | Yes | No              |
| [$split](split.md "split.md")                      | Yes | Yes | Yes | Yes | Yes             |
| [$strcasecmp](strcasecmp.md "strcasecmp.md")       | Yes | Yes | Yes | Yes | Yes             |
| [$strLenBytes](strLenBytes.md "strLenBytes.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$strLenCP](strLenCP.md "strLenCP.md")             | Yes | Yes | Yes | Yes | Yes             |
| [$substr](substr.md "substr.md")                   | Yes | Yes | Yes | Yes | Yes             |
| [$substrBytes](substrBytes.md "substrBytes.md")    | Yes | Yes | Yes | Yes | Yes             |
| [$substrCP](substrCP.md "substrCP.md")             | Yes | Yes | Yes | Yes | Yes             |
| [$toLower](toLower.md "toLower.md")                | Yes | Yes | Yes | Yes | Yes             |
| [$toUpper](toUpper.md "toUpper.md")                | Yes | Yes | Yes | Yes | Yes             |
| [$trim](trim.md "trim.md")                         | No  | Yes | Yes | Yes | No              |

### System variables

| Command                              | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ------------------------------------ | --- | --- | --- | --- | --------------- |
| $$CURRENT                            | No  | No  | No  | No  | No              |
| [$$DESCEND](DESCEND.md "DESCEND.md") | Yes | Yes | Yes | Yes | Yes             |
| [$$KEEP](KEEP.md "KEEP.md")          | Yes | Yes | Yes | Yes | Yes             |
| [$$PRUNE](PRUNE.md "PRUNE.md")       | Yes | Yes | Yes | Yes | Yes             |
| $$REMOVE                             | No  | No  | No  | No  | No              |
| [$ROOT](ROOT.md "ROOT.md")           | Yes | Yes | Yes | Yes | Yes             |

### Text search operator

| Command                                            | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| -------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [$meta](meta-aggregation.md "meta-aggregation.md") | No  | No  | Yes | Yes | No              |
| [$search](search.md "search.md")                   | No  | No  | Yes | Yes | No              |

### Type conversion operators

| Command                                      | 3.6 | 4.0 | 5.0 | 8.0          | Elastic cluster |
| -------------------------------------------- | --- | --- | --- | ------------ | --------------- |
| [$convert](convert.md "convert.md")          | No  | Yes | Yes | Yes          | Yes             |
| [$isNumber](isNumber.md "isNumber.md")       | -   | -   | No  | Yes (8.0.1+) | No              |
| [$toBool](toBool.md "toBool.md")             | No  | Yes | Yes | Yes          | Yes             |
| [$toDate](toDate.md "toDate.md")             | No  | Yes | Yes | Yes          | Yes             |
| [$toDecimal](toDecimal.md "toDecimal.md")    | No  | Yes | Yes | Yes          | Yes             |
| [$toDouble](toDouble.md "toDouble.md")       | No  | Yes | Yes | Yes          | Yes             |
| [$toInt](toInt.md "toInt.md")                | No  | Yes | Yes | Yes          | Yes             |
| [$toLong](toLong.md "toLong.md")             | No  | Yes | Yes | Yes          | Yes             |
| [$toObjectId](toObjectId.md "toObjectId.md") | No  | Yes | Yes | Yes          | Yes             |
| [$toString](toString.md "toString.md")       | No  | Yes | Yes | Yes          | Yes             |
| [$toUUID](toUUID.md "toUUID.md")             | -   | -   | -   | Yes (8.0.1+) | No              |

### Variable operators

| Command                 | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------- | --- | --- | --- | --- | --------------- |
| [$let](let.md "let.md") | Yes | Yes | Yes | Yes | Yes             |
| [$map](map.md "map.md") | Yes | Yes | Yes | Yes | Yes             |

### Trigonometry operators

| Command                                                        | 3.6 | 4.0 | 5.0 | 8.0          | Elastic cluster |
| -------------------------------------------------------------- | --- | --- | --- | ------------ | --------------- |
| [$acos](acos.md "acos.md")                                     | -   | -   | -   | Yes (8.0.1+) | No              |
| [$acosh](acosh.md "acosh.md")                                  | -   | -   | -   | Yes (8.0.1+) | No              |
| [$asin](asin.md "asin.md")                                     | -   | -   | -   | Yes (8.0.1+) | No              |
| [$asinh](asinh.md "asinh.md")                                  | -   | -   | -   | Yes (8.0.1+) | No              |
| [$atan](atan.md "atan.md")                                     | -   | -   | -   | Yes (8.0.1+) | No              |
| [$atan2](atan2.md "atan2.md")                                  | -   | -   | -   | Yes (8.0.1+) | No              |
| [$atanh](atanh.md "atanh.md")                                  | -   | -   | -   | Yes (8.0.1+) | No              |
| [$cos](cos.md "cos.md")                                        | -   | -   | -   | Yes (8.0.1+) | No              |
| [$cosh](cosh.md "cosh.md")                                     | -   | -   | -   | Yes (8.0.1+) | No              |
| [$degreesToRadians](degreesToRadians.md "degreesToRadians.md") | -   | -   | -   | Yes (8.0.1+) | No              |
| [$radiansToDegrees](radiansToDegrees.md "radiansToDegrees.md") | -   | -   | -   | Yes (8.0.1+) | No              |
| [$sin](sin.md "sin.md")                                        | -   | -   | -   | Yes (8.0.1+) | No              |
| [$sinh](sinh.md "sinh.md")                                     | -   | -   | -   | Yes (8.0.1+) | No              |
| [$tan](tan.md "tan.md")                                        | -   | -   | -   | Yes (8.0.1+) | No              |
| [$tanh](tanh.md "tanh.md")                                     | -   | -   | -   | Yes (8.0.1+) | No              |

### Bitwise operators (aggregation)

| Command                          | 3.6 | 4.0 | 5.0 | 8.0          | Elastic cluster |
| -------------------------------- | --- | --- | --- | ------------ | --------------- |
| [$bitAnd](bitAnd.md "bitAnd.md") | -   | -   | -   | Yes (8.0.1+) | No              |
| [$bitNot](bitNot.md "bitNot.md") | -   | -   | -   | Yes (8.0.1+) | No              |
| [$bitOr](bitOr.md "bitOr.md")    | -   | -   | -   | Yes (8.0.1+) | No              |
| [$bitXor](bitXor.md "bitXor.md") | -   | -   | -   | Yes (8.0.1+) | No              |

### Timestamp operators

| Command                                         | 3.6 | 4.0 | 5.0 | 8.0          | Elastic cluster |
| ----------------------------------------------- | --- | --- | --- | ------------ | --------------- |
| [$tsIncrement](tsIncrement.md "tsIncrement.md") | -   | -   | -   | Yes (8.0.1+) | No              |
| [$tsSecond](tsSecond.md "tsSecond.md")          | -   | -   | -   | Yes (8.0.1+) | No              |

### Miscellaneous operators

| Command                                      | 3.6 | 4.0 | 5.0          | 8.0          | Elastic cluster |
| -------------------------------------------- | --- | --- | ------------ | ------------ | --------------- |
| $getField                                    | -   | -   | No           | No           | No              |
| [$rand](rand.md "rand.md")                   | -   | -   | Yes (5.0.1+) | Yes          | No              |
| [$sampleRate](sampleRate.md "sampleRate.md") | -   | -   | No           | Yes (8.0.1+) | No              |
| [$sigmoid](sigmoid.md "sigmoid.md")          | -   | -   | -            | Yes (8.0.1+) | No              |

## Data types

| Command                 | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ----------------------- | --- | --- | --- | --- | --------------- |
| 32-bit Integer (int)    | Yes | Yes | Yes | Yes | Yes             |
| 64-bit Integer (long)   | Yes | Yes | Yes | Yes | Yes             |
| Array                   | Yes | Yes | Yes | Yes | Yes             |
| Binary Data             | Yes | Yes | Yes | Yes | Yes             |
| Boolean                 | Yes | Yes | Yes | Yes | Yes             |
| Date                    | Yes | Yes | Yes | Yes | Yes             |
| DBPointer               | No  | No  | No  | No  | No              |
| DBRefs                  | No  | No  | No  | No  | No              |
| Decimal128              | Yes | Yes | Yes | Yes | Yes             |
| Double                  | Yes | Yes | Yes | Yes | Yes             |
| JavaScript              | No  | No  | No  | No  | No              |
| JavaScript (with scope) | No  | No  | No  | No  | No              |
| MaxKey                  | Yes | Yes | Yes | Yes | Yes             |
| MinKey                  | Yes | Yes | Yes | Yes | Yes             |
| Null                    | Yes | Yes | Yes | Yes | Yes             |
| Object                  | Yes | Yes | Yes | Yes | Yes             |
| ObjectId                | Yes | Yes | Yes | Yes | Yes             |
| Regular Expression      | Yes | Yes | Yes | Yes | Yes             |
| String                  | Yes | Yes | Yes | Yes | Yes             |
| Symbol                  | No  | No  | No  | No  | No              |
| Timestamp               | Yes | Yes | Yes | Yes | Yes             |
| Undefined               | No  | No  | No  | No  | No              |

## Indexes and index properties

###### Topics

- [Indexes](#mongo-apis-indexes "#mongo-apis-indexes")
- [Index properties](#mongo-apis-index-properties "#mongo-apis-index-properties")

### Indexes

| Command            | 3.6 | 4.0 | 5.0 | 8.0 | Elastic cluster |
| ------------------ | --- | --- | --- | --- | --------------- |
| 2dsphere           | Yes | Yes | Yes | Yes | Yes             |
| 2d Index           | No  | No  | No  | No  | No              |
| Compound Index     | Yes | Yes | Yes | Yes | Yes             |
| Hashed Index       | No  | No  | No  | No  | No              |
| Multikey Index     | Yes | Yes | Yes | Yes | Yes             |
| Single Field Index | Yes | Yes | Yes | Yes | Yes             |
| Text Index         | No  | No  | Yes | Yes | No              |
| Wildcard           | No  | No  | No  | No  | No              |

### Index properties

| Command          | 3.6 | 4.0 | 5.0 | 8.0          | Elastic cluster |
| ---------------- | --- | --- | --- | ------------ | --------------- |
| Background       | Yes | Yes | Yes | Yes          | Yes             |
| Case Insensitive | No  | No  | No  | Yes          | No              |
| Hidden           | No  | No  | No  | Yes (8.0.1+) | No              |
| Partial          | No  | No  | Yes | Yes          | No              |
| Sparse           | Yes | Yes | Yes | Yes          | Yes             |
| Text             | No  | No  | Yes | Yes          | No              |
| TTL              | Yes | Yes | Yes | Yes          | Yes             |
| Unique           | Yes | Yes | Yes | Yes          | Yes             |
| Vector           | No  | No  | Yes | Yes          | No              |

For detailed information about specific MongoDB operators, see the following topics:

- [Aggregation pipeline operators](mongo-apis-aggregation-pipeline-operators.md "mongo-apis-aggregation-pipeline-operators.md")
- [Geospatial](mongo-apis-geospatial-operators.md "mongo-apis-geospatial-operators.md")
- [Projection operators](#mongo-apis-projection-operators "#mongo-apis-projection-operators")
- [Update operators](mongo-apis-update-operators.md "mongo-apis-update-operators.md")
