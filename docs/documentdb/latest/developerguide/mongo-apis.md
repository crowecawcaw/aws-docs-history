# Supported MongoDB APIs, operations, and data types in Amazon DocumentDB

Amazon DocumentDB (with MongoDB compatibility) is a fast, scalable, highly-available, and fully managed document database service that supports MongoDB workloads.
Amazon DocumentDB is compatible with the MongoDB 3.6, 4.0, and 5.0 APIs.
This section lists the supported functionality.
For support using MongoDB APIs and drivers, please consult the MongoDB Community Forums.
For support using the Amazon DocumentDB service, please contact the appropriate AWS support team.
For functional differences between Amazon DocumentDB and MongoDB, please see [Functional differences: Amazon DocumentDB and MongoDB](functional-differences.md "functional-differences.md").

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
- [Indexes and index properties](#mongo-apis-index "#mongo-apis-index")

## Database commands

###### Topics

- [Administrative Commands](#mongo-apis-dababase-administrative "#mongo-apis-dababase-administrative")
- [Aggregation](#mongo-apis-dababase-aggregation "#mongo-apis-dababase-aggregation")
- [Authentication](#mongo-apis-dababase-authentication "#mongo-apis-dababase-authentication")
- [Diagnostic commands](#mongo-apis-dababase-diagnostics "#mongo-apis-dababase-diagnostics")
- [Query and write operations](#mongo-apis-dababase-query-write "#mongo-apis-dababase-query-write")
- [Role management commands](#mongo-apis-database-role-management "#mongo-apis-database-role-management")
- [Sessions commands](#mongo-apis-dababase-sessions "#mongo-apis-dababase-sessions")
- [User management](#mongo-apis-dababase-user-management "#mongo-apis-dababase-user-management")
- [Sharding commands](#mongo-apis-dababase-sharding "#mongo-apis-dababase-sharding")

### Administrative Commands

| Command                     | 3.6     | 4.0     | 5.0     | Elastic cluster |
| --------------------------- | ------- | ------- | ------- | --------------- |
| Capped Collections          | No      | No      | No      | No              |
| cloneCollectionAsCapped     | No      | No      | No      | No              |
| collMod                     | Partial | Partial | Partial | Partial         |
| collMod: expireAfterSeconds | Yes     | Yes     | Yes     | Yes             |
| convertToCapped             | No      | No      | No      | No              |
| copydb                      | No      | No      | No      | No              |
| create                      | Yes     | Yes     | Yes     | Yes             |
| createView                  | No      | No      | No      | No              |
| createIndexes               | Yes     | Yes     | Yes     | Yes             |
| currentOp                   | Yes     | Yes     | Yes     | Yes             |
| drop                        | Yes     | Yes     | Yes     | Yes             |
| dropDatabase                | Yes     | Yes     | Yes     | Yes             |
| dropIndexes                 | Yes     | Yes     | Yes     | Yes             |
| filemd5                     | No      | No      | No      | No              |
| getAuditConfig              | No      | Yes     | Yes     | No              |
| killCursors                 | Yes     | Yes     | Yes     | Yes             |
| killOp                      | Yes     | Yes     | Yes     | Yes             |
| listCollections\*           | Yes     | Yes     | Yes     | Yes             |
| listDatabases               | Yes     | Yes     | Yes     | Yes             |
| listIndexes                 | Yes     | Yes     | Yes     | Yes             |
| reIndex                     | No      | No      | Yes     | No              |
| renameCollection            | Yes     | Yes     | Yes     | No              |
| setAuditConfig              | No      | Yes     | Yes     | No              |

\* The `type` key in the filter option is not supported.

### Aggregation

| Command   | 3.6 | 4.0 | 5.0 | Elastic cluster |
| --------- | --- | --- | --- | --------------- |
| aggregate | Yes | Yes | Yes | Yes             |
| count     | Yes | Yes | Yes | Yes             |
| distinct  | Yes | Yes | Yes | Yes             |
| mapReduce | No  | No  | No  | No              |

### Authentication

| Command      | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------ | --- | --- | --- | --------------- |
| authenticate | Yes | Yes | Yes | Yes             |
| logout       | Yes | Yes | Yes | Yes             |

### Diagnostic commands

| Command                 | 3.6                                | 4.0                                | 5.0                                | Elastic cluster |
| ----------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | --------------- |
| buildInfo               | Yes                                | Yes                                | Yes                                | Yes             |
| collStats               | Yes                                | Yes                                | Yes                                | Yes             |
| connPoolStats           | No                                 | No                                 | No                                 | No              |
| connectionStatus        | Yes                                | Yes                                | Yes                                | Yes             |
| dataSize                | Yes                                | Yes                                | Yes                                | Yes             |
| dbHash                  | No                                 | No                                 | No                                 | No              |
| dbStats                 | Yes                                | Yes                                | Yes                                | Yes             |
| explain                 | Yes                                | Yes                                | Yes                                | Yes             |
| explain: executionStats | Yes                                | Yes                                | Yes                                | Yes             |
| features                | No                                 | No                                 | No                                 | No              |
| hostInfo                | Yes                                | Yes                                | Yes                                | Yes             |
| listCommands            | Yes                                | Yes                                | Yes                                | Yes             |
| profiler                | [Yes](profiling.md "profiling.md") | [Yes](profiling.md "profiling.md") | [Yes](profiling.md "profiling.md") | No              |
| serverStatus            | Yes                                | Yes                                | Yes                                | Yes             |
| top                     | Yes                                | Yes                                | Yes                                | Yes             |

### Query and write operations

| Command                | 3.6                                          | 4.0                                          | 5.0                                          | Elastic cluster |
| ---------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | --------------- |
| Change streams         | [Yes](change_streams.md "change_streams.md") | [Yes](change_streams.md "change_streams.md") | [Yes](change_streams.md "change_streams.md") | No              |
| delete                 | Yes                                          | Yes                                          | Yes                                          | Yes             |
| find                   | Yes                                          | Yes                                          | Yes                                          | Yes             |
| findAndModify          | Yes                                          | Yes                                          | Yes                                          | Yes             |
| getLastError           | No                                           | No                                           | No                                           | No              |
| getMore                | Yes                                          | Yes                                          | Yes                                          | Yes             |
| getPrevError           | No                                           | No                                           | No                                           | No              |
| GridFS                 | Yes                                          | Yes                                          | Yes                                          | No              |
| insert                 | Yes                                          | Yes                                          | Yes                                          | Yes             |
| parallelCollectionScan | No                                           | No                                           | No                                           | No              |
| resetError             | No                                           | No                                           | No                                           | No              |
| update                 | Yes                                          | Yes                                          | Yes                                          | Yes             |
| ReplaceOne             | Yes                                          | Yes                                          | Yes                                          | Yes             |

### Role management commands

| Command                  | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------------------ | --- | --- | --- | --------------- |
| createRole               | Yes | Yes | Yes | No              |
| dropAllRolesFromDatabase | Yes | Yes | Yes | No              |
| dropRole                 | Yes | Yes | Yes | No              |
| grantRolesToRole         | Yes | Yes | Yes | No              |
| revokeRolesFromRole      | Yes | Yes | Yes | No              |
| revokePrivilegesFromRole | Yes | Yes | Yes | No              |
| rolesInfo                | Yes | Yes | Yes | No              |
| updateRole               | Yes | Yes | Yes | No              |

### Sessions commands

| Command                  | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------------------ | --- | --- | --- | --------------- |
| abortTransaction         | No  | Yes | Yes | No              |
| commitTransaction        | No  | Yes | Yes | No              |
| endSessions              | No  | No  | No  | No              |
| killAllSessions          | No  | Yes | Yes | No              |
| killAllSessionsByPattern | No  | No  | No  | No              |
| killSessions             | No  | Yes | Yes | No              |
| refreshSessions          | No  | No  | No  | No              |
| startSession             | No  | Yes | Yes | No              |

### User management

| Command                  | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------------------ | --- | --- | --- | --------------- |
| createUser               | Yes | Yes | Yes | Yes             |
| dropAllUsersFromDatabase | Yes | Yes | Yes | Yes             |
| dropUser                 | Yes | Yes | Yes | Yes             |
| grantRolesToUser         | Yes | Yes | Yes | Yes             |
| revokeRolesFromUser      | Yes | Yes | Yes | Yes             |
| updateUser               | Yes | Yes | Yes | Yes             |
| usersInfo                | Yes | Yes | Yes | Yes             |

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

- [Array Operators](#mongo-apis-query-array-operators "#mongo-apis-query-array-operators")
- [Bitwise operators](#mongo-apis-query-bitwise-operators "#mongo-apis-query-bitwise-operators")
- [Comment operator](#mongo-apis-query-comment-operator "#mongo-apis-query-comment-operator")
- [Comparison operators](#mongo-apis-query-comparison-operators "#mongo-apis-query-comparison-operators")
- [Element operators](#mongo-apis-query-element-operators "#mongo-apis-query-element-operators")
- [Evaluation query operators](#mongo-apis-query-evaluation-operators "#mongo-apis-query-evaluation-operators")
- [Logical operators](#mongo-apis-query-logical-operators "#mongo-apis-query-logical-operators")
- [Projection operators](#mongo-apis-query-projection-operators "#mongo-apis-query-projection-operators")

### Array Operators

| Command    | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ---------- | --- | --- | --- | --------------- |
| $all       | Yes | Yes | Yes | Yes             |
| $elemMatch | Yes | Yes | Yes | Yes             |
| $size      | Yes | Yes | Yes | Yes             |

### Bitwise operators

| Command       | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------- | --- | --- | --- | --------------- |
| $bitsAllSet   | Yes | Yes | Yes | Yes             |
| $bitsAnySet   | Yes | Yes | Yes | Yes             |
| $bitsAllClear | Yes | Yes | Yes | Yes             |
| $bitsAnyClear | Yes | Yes | Yes | Yes             |

### Comment operator

| Command  | 3.6 | 4.0 | 5.0 | Elastic cluster |
| -------- | --- | --- | --- | --------------- |
| $comment | Yes | Yes | Yes | Yes             |

### Comparison operators

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $eq     | Yes | Yes | Yes | Yes             |
| $gt     | Yes | Yes | Yes | Yes             |
| $gte    | Yes | Yes | Yes | Yes             |
| $in     | Yes | Yes | Yes | Yes             |
| $lt     | Yes | Yes | Yes | Yes             |
| $lte    | Yes | Yes | Yes | Yes             |
| $ne     | Yes | Yes | Yes | Yes             |
| $nin    | Yes | Yes | Yes | Yes             |

### Element operators

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $exists | Yes | Yes | Yes | Yes             |
| $type   | Yes | Yes | Yes | Yes             |

### Evaluation query operators

| Command                                                              | 3.6 | 4.0 | 5.0 | Elastic cluster |
| -------------------------------------------------------------------- | --- | --- | --- | --------------- |
| $expr                                                                | No  | Yes | Yes | No              |
| [$jsonSchema](json-schema-validation.md "json-schema-validation.md") | No  | Yes | Yes | No              |
| $mod                                                                 | Yes | Yes | Yes | Yes             |
| $regex                                                               | Yes | Yes | Yes | Yes             |
| $text                                                                | No  | No  | Yes | No              |
| $where                                                               | No  | No  | No  | No              |

### Logical operators

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $and    | Yes | Yes | Yes | Yes             |
| $nor    | Yes | Yes | Yes | Yes             |
| $not    | Yes | Yes | Yes | Yes             |
| $or     | Yes | Yes | Yes | Yes             |

### Projection operators

| Command    | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ---------- | --- | --- | --- | --------------- |
| $          | Yes | Yes | Yes | Yes             |
| $elemMatch | Yes | Yes | Yes | Yes             |
| $meta      | No  | No  | Yes | No              |
| $slice     | Yes | Yes | Yes | Yes             |

## Update operators

###### Topics

- [Array operators](#mongo-apis-update-array "#mongo-apis-update-array")
- [Bitwise operators](#mongo-apis-update-bitwise "#mongo-apis-update-bitwise")
- [Field operators](#mongo-apis-update-field "#mongo-apis-update-field")
- [Update modifiers](#mongo-apis-update-modifiers "#mongo-apis-update-modifiers")

### Array operators

| Command         | 3.6 | 4.0 | 5.0 | Elastic cluster |
| --------------- | --- | --- | --- | --------------- |
| $               | Yes | Yes | Yes | Yes             |
| $[]             | Yes | Yes | Yes | Yes             |
| $[<identifier>] | Yes | Yes | Yes | Yes             |
| $addToSet       | Yes | Yes | Yes | Yes             |
| $pop            | Yes | Yes | Yes | Yes             |
| $pullAll        | Yes | Yes | Yes | Yes             |
| $pull           | Yes | Yes | Yes | Yes             |
| $push           | Yes | Yes | Yes | Yes             |

### Bitwise operators

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $bit    | Yes | Yes | Yes | Yes             |

### Field operators

| Operator     | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------ | --- | --- | --- | --------------- |
| $currentDate | Yes | Yes | Yes | Yes             |
| $inc         | Yes | Yes | Yes | Yes             |
| $max         | Yes | Yes | Yes | Yes             |
| $min         | Yes | Yes | Yes | Yes             |
| $mul         | Yes | Yes | Yes | Yes             |
| $rename      | Yes | Yes | Yes | Yes             |
| $set         | Yes | Yes | Yes | Yes             |
| $setOnInsert | Yes | Yes | Yes | Yes             |
| $unset       | Yes | Yes | Yes | Yes             |

### Update modifiers

| Operator  | 3.6 | 4.0 | 5.0 | Elastic cluster |
| --------- | --- | --- | --- | --------------- |
| $each     | Yes | Yes | Yes | Yes             |
| $position | Yes | Yes | Yes | Yes             |
| $slice    | Yes | Yes | Yes | Yes             |
| $sort     | Yes | Yes | Yes | Yes             |

## Geospatial

### Geometry specifiers

| Query Selectors | 3.6 | 4.0 | 5.0 | Elastic cluster |
| --------------- | --- | --- | --- | --------------- |
| $box            | No  | No  | No  | No              |
| $center         | No  | No  | No  | No              |
| $centerSphere   | No  | No  | No  | No              |
| $geometry       | Yes | Yes | Yes | Yes             |
| $maxDistance    | Yes | Yes | Yes | Yes             |
| $minDistance    | Yes | Yes | Yes | Yes             |
| $nearSphere     | Yes | Yes | Yes | Yes             |
| $polygon        | No  | No  | No  | No              |
| $uniqueDocs     | No  | No  | No  | No              |

### Query selectors

| Command        | 3.6 | 4.0 | 5.0 | Elastic cluster |
| -------------- | --- | --- | --- | --------------- |
| $geoIntersects | Yes | Yes | Yes | Yes             |
| $geoWithin     | Yes | Yes | Yes | Yes             |
| $near          | Yes | Yes | Yes | Yes             |
| $nearSphere    | Yes | Yes | Yes | Yes             |
| $polygon       | No  | No  | No  | No              |
| $uniqueDocs    | No  | No  | No  | No              |

## Cursor methods

| Command                  | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------------------ | --- | --- | --- | --------------- |
| cursor.batchSize()       | Yes | Yes | Yes | Yes             |
| cursor.close()           | Yes | Yes | Yes | Yes             |
| cursor.collation()       | No  | No  | No  | No              |
| cursor.comment()         | Yes | Yes | Yes | Yes             |
| cursor.count()           | Yes | Yes | Yes | Yes             |
| cursor.explain()         | Yes | Yes | Yes | No              |
| cursor.forEach()         | Yes | Yes | Yes | Yes             |
| cursor.hasNext()         | Yes | Yes | Yes | Yes             |
| cursor.hint()            | Yes | Yes | Yes | Yes\*           |
| cursor.isClosed()        | Yes | Yes | Yes | Yes             |
| cursor.isExhausted()     | Yes | Yes | Yes | No              |
| cursor.itcount()         | Yes | Yes | Yes | No              |
| cursor.limit()           | Yes | Yes | Yes | No              |
| cursor.map()             | Yes | Yes | Yes | No              |
| cursor.max()             | No  | No  | No  | No              |
| cursor.maxScan()         | Yes | Yes | Yes | No              |
| cursor.maxTimeMS()       | Yes | Yes | Yes | No              |
| cursor.min()             | No  | No  | No  | No              |
| cursor.next()            | Yes | Yes | Yes | Yes             |
| cursor.noCursorTimeout() | No  | No  | No  | No              |
| cursor.objsLeftInBatch() | Yes | Yes | Yes | No              |
| cursor.pretty()          | Yes | Yes | Yes | No              |
| cursor.readConcern()     | Yes | Yes | Yes | No              |
| cursor.readPref()        | Yes | Yes | Yes | No              |
| cursor.returnKey()       | No  | No  | No  | No              |
| cursor.showRecordId()    | No  | No  | No  | No              |
| cursor.size()            | Yes | Yes | Yes | No              |
| cursor.skip()            | Yes | Yes | Yes | No              |
| cursor.sort()            | Yes | Yes | Yes | No              |
| cursor.tailable()        | No  | No  | No  | No              |
| cursor.toArray()         | Yes | Yes | Yes | No              |

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
- [Miscellaneous operators](#mongo-apis-aggregation-pipeline-misc "#mongo-apis-aggregation-pipeline-misc")

### Accumulator expressions

| Expression      | 3.6 | 4.0 | 5.0 | Elastic cluster |
| --------------- | --- | --- | --- | --------------- |
| $accumulator    | -   | -   | No  | No              |
| $addToSet       | Yes | Yes | Yes | Yes             |
| $avg            | Yes | Yes | Yes | Yes             |
| $count          | -   | -   | No  | No              |
| $covariancePop  | No  | No  | No  | No              |
| $covarianceSamp | No  | No  | No  | No              |
| $denseRank      | No  | No  | No  | No              |
| $derivative     | No  | No  | No  | No              |
| $documentNumber | No  | No  | No  | No              |
| $expMovingAvg   | No  | No  | No  | No              |
| $first          | Yes | Yes | Yes | Yes             |
| $integral       | No  | No  | No  | No              |
| $last           | Yes | Yes | Yes | Yes             |
| $max            | Yes | Yes | Yes | Yes             |
| $min            | Yes | Yes | Yes | Yes             |
| $push           | Yes | Yes | Yes | Yes             |
| $rank           | No  | No  | No  | No              |
| $shift          | No  | No  | No  | No              |
| $stdDevPop      | No  | No  | No  | No              |
| $stdDevSamp     | No  | No  | No  | No              |
| $sum            | Yes | Yes | Yes | Yes             |

### Arithmetic operators

| Command   | 3.6 | 4.0 | 5.0 | Elastic cluster |
| --------- | --- | --- | --- | --------------- |
| $abs      | Yes | Yes | Yes | Yes             |
| $add      | Yes | Yes | Yes | Yes             |
| $ceil     | No  | Yes | Yes | Yes             |
| $divide   | Yes | Yes | Yes | Yes             |
| $exp      | No  | Yes | Yes | Yes             |
| $floor    | No  | Yes | Yes | Yes             |
| $ln       | No  | Yes | Yes | Yes             |
| $log      | No  | Yes | Yes | Yes             |
| $log10    | No  | Yes | Yes | Yes             |
| $mod      | Yes | Yes | Yes | Yes             |
| $multiply | Yes | Yes | Yes | Yes             |
| $pow      | No  | No  | No  | No              |
| $round    | -   | -   | No  | No              |
| $sqrt     | No  | Yes | Yes | Yes             |
| $subtract | Yes | Yes | Yes | Yes             |
| $trunc    | No  | No  | No  | No              |

### Array operators

| Command        | 3.6 | 4.0 | 5.0 | Elastic cluster |
| -------------- | --- | --- | --- | --------------- |
| $arrayElemAt   | Yes | Yes | Yes | Yes             |
| $arrayToObject | Yes | Yes | Yes | Yes             |
| $concatArrays  | Yes | Yes | Yes | Yes             |
| $filter        | Yes | Yes | Yes | Yes             |
| $first         | -   | -   | Yes | No              |
| $in            | Yes | Yes | Yes | Yes             |
| $indexOfArray  | Yes | Yes | Yes | Yes             |
| $isArray       | Yes | Yes | Yes | Yes             |
| $last          | -   | -   | Yes | No              |
| $objectToArray | Yes | Yes | Yes | Yes             |
| $range         | Yes | Yes | Yes | Yes             |
| $reverseArray  | Yes | Yes | Yes | Yes             |
| $reduce        | Yes | Yes | Yes | Yes             |
| $size          | Yes | Yes | Yes | Yes             |
| $slice         | Yes | Yes | Yes | Yes             |
| $zip           | Yes | Yes | Yes | Yes             |

### Boolean operators

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $and    | Yes | Yes | Yes | Yes             |
| $not    | Yes | Yes | Yes | Yes             |
| $or     | Yes | Yes | Yes | Yes             |

### Comparison operators

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $cmp    | Yes | Yes | Yes | Yes             |
| $eq     | Yes | Yes | Yes | Yes             |
| $gt     | Yes | Yes | Yes | Yes             |
| $gte    | Yes | Yes | Yes | Yes             |
| $lt     | Yes | Yes | Yes | Yes             |
| $lte    | Yes | Yes | Yes | Yes             |
| $ne     | Yes | Yes | Yes | Yes             |

### Conditional expression operators

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $cond   | Yes | Yes | Yes | Yes             |
| $ifNull | Yes | Yes | Yes | Yes             |
| $switch | No  | Yes | Yes | No              |

### Data type operator

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $type   | Yes | Yes | Yes | Yes             |

### Data size operator

| Command     | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ----------- | --- | --- | --- | --------------- |
| $binarySize | -   | -   | No  | No              |
| $bsonSize   | -   | -   | No  | No              |

### Date operators

| Command         | 3.6 | 4.0 | 5.0 | Elastic cluster |
| --------------- | --- | --- | --- | --------------- |
| $dateAdd        | No  | No  | Yes | Yes             |
| $dateDiff       | -   | -   | No  | No              |
| $dateFromParts  | No  | No  | No  | No              |
| $dateFromString | Yes | Yes | Yes | Yes             |
| $dateSubtract   | No  | No  | Yes | Yes             |
| $dateToParts    | No  | No  | No  | No              |
| $dateToString   | Yes | Yes | Yes | Yes             |
| $dateTrunc      | -   | -   | No  | No              |
| $dayOfMonth     | Yes | Yes | Yes | Yes             |
| $dayOfWeek      | Yes | Yes | Yes | Yes             |
| $dayOfYear      | Yes | Yes | Yes | Yes             |
| $hour           | Yes | Yes | Yes | Yes             |
| $isoDayOfWeek   | Yes | Yes | Yes | Yes             |
| $isoWeek        | Yes | Yes | Yes | Yes             |
| $isoWeekYear    | Yes | Yes | Yes | Yes             |
| $millisecond    | Yes | Yes | Yes | Yes             |
| $minute         | Yes | Yes | Yes | Yes             |
| $month          | Yes | Yes | Yes | Yes             |
| $second         | Yes | Yes | Yes | Yes             |
| $week           | Yes | Yes | Yes | Yes             |
| $year           | Yes | Yes | Yes | Yes             |

### Literal operator

| Command  | 3.6 | 4.0 | 5.0 | Elastic cluster |
| -------- | --- | --- | --- | --------------- |
| $literal | Yes | Yes | Yes | Yes             |

### Merge operator

| Command       | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------- | --- | --- | --- | --------------- |
| $mergeObjects | Yes | Yes | Yes | Yes             |

### Natural operator

| Command  | 3.6 | 4.0 | 5.0 | Elastic cluster |
| -------- | --- | --- | --- | --------------- |
| $natural | Yes | Yes | Yes | Yes             |

### Set operators

| Command          | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ---------------- | --- | --- | --- | --------------- |
| $allElementsTrue | No  | Yes | Yes | Yes             |
| $anyElementTrue  | No  | Yes | Yes | Yes             |
| $setDifference   | No  | Yes | Yes | Yes             |
| $setEquals       | Yes | Yes | Yes | Yes             |
| $setIntersection | Yes | Yes | Yes | Yes             |
| $setIsSubset     | Yes | Yes | Yes | Yes             |
| $setUnion        | Yes | Yes | Yes | Yes             |
| $setWindowFields | No  | No  | No  | No              |

### Stage operators

| Command            | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------------ | --- | --- | --- | --------------- |
| $addFields         | Yes | Yes | Yes | Yes             |
| $bucket            | No  | No  | No  | No              |
| $bucketAuto        | No  | No  | No  | No              |
| $changeStream      | Yes | Yes | Yes | No              |
| $collStats         | No  | Yes | Yes | No              |
| $count             | Yes | Yes | Yes | Yes             |
| $currentOp         | Yes | Yes | Yes | Yes             |
| $facet             | No  | No  | No  | No              |
| $geoNear           | Yes | Yes | Yes | Yes             |
| $graphLookup       | No  | No  | No  | No              |
| $group             | Yes | Yes | Yes | Yes             |
| $indexStats        | Yes | Yes | Yes | Yes             |
| $limit             | Yes | Yes | Yes | Yes             |
| $listLocalSessions | No  | No  | No  | No              |
| $listSessions      | No  | No  | No  | No              |
| $lookup            | Yes | Yes | Yes | Yes             |
| $match             | Yes | Yes | Yes | Yes             |
| $merge             | -   | -   | No  | No              |
| $out               | Yes | Yes | Yes | No              |
| $planCacheStats    | -   | -   | No  | No              |
| $project           | Yes | Yes | Yes | Yes             |
| $redact            | Yes | Yes | Yes | Yes             |
| $replaceRoot       | Yes | Yes | Yes | Yes             |
| $sample            | Yes | Yes | Yes | Yes             |
| $set               | -   | -   | No  | No              |
| $setWindowFields   | -   | -   | No  | No              |
| $skip              | Yes | Yes | Yes | Yes             |
| $sort              | Yes | Yes | Yes | Yes             |
| $sortByCount       | No  | No  | No  | No              |
| $unionWith         | -   | -   | No  | No              |
| $unset             | -   | -   | No  | No              |
| $unwind            | Yes | Yes | Yes | Yes             |

### String operators

| Command       | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------- | --- | --- | --- | --------------- |
| $concat       | Yes | Yes | Yes | Yes             |
| $indexOfBytes | Yes | Yes | Yes | Yes             |
| $indexOfCP    | Yes | Yes | Yes | Yes             |
| $ltrim        | No  | Yes | Yes | No              |
| $regexFind    | -   | -   | Yes | No              |
| $regexFindAll | -   | -   | Yes | No              |
| $regexMatch   | -   | -   | Yes | No              |
| $replaceAll   | -   | -   | Yes | No              |
| $replaceOne   | -   | -   | Yes | No              |
| $rtrim        | No  | Yes | Yes | No              |
| $split        | Yes | Yes | Yes | Yes             |
| $strcasecmp   | Yes | Yes | Yes | Yes             |
| $strLenBytes  | Yes | Yes | Yes | Yes             |
| $strLenCP     | Yes | Yes | Yes | Yes             |
| $substr       | Yes | Yes | Yes | Yes             |
| $substrBytes  | Yes | Yes | Yes | Yes             |
| $substrCP     | Yes | Yes | Yes | Yes             |
| $toLower      | Yes | Yes | Yes | Yes             |
| $toUpper      | Yes | Yes | Yes | Yes             |
| $trim         | No  | Yes | Yes | No              |

### System variables

| Command   | 3.6 | 4.0 | 5.0 | Elastic cluster |
| --------- | --- | --- | --- | --------------- |
| $$CURRENT | No  | No  | No  | No              |
| $$DESCEND | Yes | Yes | Yes | Yes             |
| $$KEEP    | Yes | Yes | Yes | Yes             |
| $$PRUNE   | Yes | Yes | Yes | Yes             |
| $$REMOVE  | No  | No  | No  | No              |
| $$ROOT    | Yes | Yes | Yes | Yes             |

### Text search operator

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $meta   | No  | No  | Yes | No              |
| $search | No  | No  | Yes | No              |

### Type conversion operators

| Command     | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ----------- | --- | --- | --- | --------------- |
| $convert    | No  | Yes | Yes | Yes             |
| $isNumber   | -   | -   | No  | No              |
| $toBool     | No  | Yes | Yes | Yes             |
| $toDate     | No  | Yes | Yes | Yes             |
| $toDecimal  | No  | Yes | Yes | Yes             |
| $toDouble   | No  | Yes | Yes | Yes             |
| $toInt      | No  | Yes | Yes | Yes             |
| $toLong     | No  | Yes | Yes | Yes             |
| $toObjectId | No  | Yes | Yes | Yes             |
| $toString   | No  | Yes | Yes | Yes             |

### Variable operators

| Command | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------- | --- | --- | --- | --------------- |
| $let    | Yes | Yes | Yes | Yes             |
| $map    | Yes | Yes | Yes | Yes             |

### Miscellaneous operators

| Command     | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ----------- | --- | --- | --- | --------------- |
| $getField   | -   | -   | No  | No              |
| $rand       | -   | -   | No  | No              |
| $sampleRate | -   | -   | No  | No              |

## Data types

| Command                 | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ----------------------- | --- | --- | --- | --------------- |
| 32-bit Integer (int)    | Yes | Yes | Yes | Yes             |
| 64-bit Integer (long)   | Yes | Yes | Yes | Yes             |
| Array                   | Yes | Yes | Yes | Yes             |
| Binary Data             | Yes | Yes | Yes | Yes             |
| Boolean                 | Yes | Yes | Yes | Yes             |
| Date                    | Yes | Yes | Yes | Yes             |
| DBPointer               | No  | No  | No  | No              |
| DBRefs                  | No  | No  | No  | No              |
| Decimal128              | Yes | Yes | Yes | Yes             |
| Double                  | Yes | Yes | Yes | Yes             |
| JavaScript              | No  | No  | No  | No              |
| JavaScript (with scope) | No  | No  | No  | No              |
| MaxKey                  | Yes | Yes | Yes | Yes             |
| MinKey                  | Yes | Yes | Yes | Yes             |
| Null                    | Yes | Yes | Yes | Yes             |
| Object                  | Yes | Yes | Yes | Yes             |
| ObjectId                | Yes | Yes | Yes | Yes             |
| Regular Expression      | Yes | Yes | Yes | Yes             |
| String                  | Yes | Yes | Yes | Yes             |
| Symbol                  | No  | No  | No  | No              |
| Timestamp               | Yes | Yes | Yes | Yes             |
| Undefined               | No  | No  | No  | No              |

## Indexes and index properties

###### Topics

- [Indexes](#mongo-apis-indexes "#mongo-apis-indexes")
- [Index properties](#mongo-apis-index-properties "#mongo-apis-index-properties")

### Indexes

| Command            | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ------------------ | --- | --- | --- | --------------- |
| 2dsphere           | Yes | Yes | Yes | Yes             |
| 2d Index           | No  | No  | No  | No              |
| Compound Index     | Yes | Yes | Yes | Yes             |
| Hashed Index       | No  | No  | No  | No              |
| Multikey Index     | Yes | Yes | Yes | Yes             |
| Single Field Index | Yes | Yes | Yes | Yes             |
| Text Index         | No  | No  | Yes | No              |
| Wildcard           | No  | No  | No  | No              |

### Index properties

| Command          | 3.6 | 4.0 | 5.0 | Elastic cluster |
| ---------------- | --- | --- | --- | --------------- |
| Background       | Yes | Yes | Yes | Yes             |
| Case Insensitive | No  | No  | No  | No              |
| Hidden           | No  | No  | No  | No              |
| Partial          | No  | No  | Yes | No              |
| Sparse           | Yes | Yes | Yes | Yes             |
| Text             | No  | No  | Yes | No              |
| TTL              | Yes | Yes | Yes | Yes             |
| Unique           | Yes | Yes | Yes | Yes             |
| Vector           | No  | No  | Yes | No              |
