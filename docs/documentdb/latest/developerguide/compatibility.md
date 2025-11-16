# Amazon DocumentDB compatibility with MongoDB

Amazon DocumentDB supports MongoDB compatibility including MongoDB 4.0, MongoDB 5.0, and MongoDB 8.0.
MongoDB compatibility means that a vast majority of the applications, drivers, and tools you already use today with your MongoDB databases can be used with Amazon DocumentDB with little or no change.
This section describes everything you need to know about Amazon DocumentDB compatibility with MongoDB including new capabilities and features, getting started, migrations paths, and functional differences.

###### Topics

- [MongoDB 8.0 compatibility](#mongodb-80 "#mongodb-80")
- [MongoDB 5.0 compatibility](#mongodb-50 "#mongodb-50")
- [MongoDB 4.0 compatibility](#mongodb-40 "#mongodb-40")

## MongoDB 8.0 compatibility

###### Topics

- [What's new in Amazon DocumentDB 8.0](#compatibility-whatsnew-8 "#compatibility-whatsnew-8")
- [Get started with Amazon DocumentDB](#compatibility-getstarted-5 "#compatibility-getstarted-5")
- [Upgrade or migrate to Amazon DocumentDB 5.0 or 8.0](#compatibility-upgrade-5 "#compatibility-upgrade-5")
- [Functional differences](#compatibility-differences-5 "#compatibility-differences-5")

### What's new in Amazon DocumentDB 8.0

Amazon DocumentDB 8.0 improves query performance by up to 7x, and improves compression ratio by up to 5x, enabling you to build high-performance applications at a lower cost.
Amazon DocumentDB 8.0 has full wire protocol compatibility with MongoDB 8.0.
The summary below introduces some of major features that were introduced in Amazon DocumentDB 8.0.
To see a full list of the new capabilities, see the [Release notes](release-notes.md "release-notes.md").

- Provides compatibility with MongoDB 8.0 by adding support for MongoDB 8.0 API drivers. Also supports applications that are built using MongoDB API versions 6.0 and 7.0.
- New query planner in Amazon DocumentDB 8.0 extends performance improvements to aggregation stage operators, along with supporting aggregation pipeline optimizations and distinct commands.
- Amazon DocumentDB 8.0 supports collation and views.
- Offers 6 new aggregation stages: $replaceWith, $vectorSearch, $merge, $set, $unset, $bucket, and 3 new aggregation operators $pow, $rand, $dateTrunc.
- A new version of text index: Text index v2 in Amazon DocumentDB 8.0 introduces additional tokens, enhancing text search capabilities.
- Through parallel vector index build, Amazon DocumentDB 8.0 reduces index build time by up to 30x.

### Get started with Amazon DocumentDB 8.0

To get started with Amazon DocumentDB 8.0, please see the [Get Started Guide](get-started-guide.md "get-started-guide.md").
You can create a new Amazon DocumentDB 8.0 cluster using the AWS Management Console or the AWS SDK, AWS CLI, or AWS CloudFormation.
When connecting to Amazon DocumentDB, it is required that you use a MongoDB driver or utility that is compatible with MongoDB 5.0 or higher.

###### Note

When using the AWS SDK, AWS CLI, or AWS CloudFormation, the engine version will default to 5.0.0.
You must explicitly specify the parameter `engineVersion = 8.0.0` to create a new Amazon DocumentDB 8.0 cluster or `engineVersion = 4.0.0` to create a new Amazon DocumentDB 4.0 cluster or `engineVersion = 3.6.0` to create a new Amazon DocumentDB 3.6 cluster.
For a given Amazon DocumentDB cluster, you can determine the cluster version using the AWS CLI to call `describe-db-clusters` or use the Amazon DocumentDB management console to view the engine version number for a particular cluster.

Amazon DocumentDB 5.0 supports the Amazon EC2 `r8g` Graviton4 processor and Graviton2 processors such as `r6g` and `t4.medium` instance types for your clusters and is available in all supported regions (see [Instances](what-is.md#what-is-db-instances "what-is.md#what-is-db-instances")).
For more information on pricing, see [Amazon DocumentDB (with MongoDB compatibility) Pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/").

### Upgrade or migrate to Amazon DocumentDB 5.0 or 8.0

You can migrate from MongoDB 3.6 or MongoDB 4.0 to Amazon DocumentDB 5.0 or Amazon DocumentDB 8.0 using the [AWS DMS](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/") or utilities like [`mongodump`, `mongorestore`, `mongoimport`, and `mongoexport`](backup_restore-dump_restore_import_export_data.md "backup_restore-dump_restore_import_export_data.md").
For instructions on how to migrate, see [Upgrading your Amazon DocumentDB cluster using AWS Database Migration Service](docdb-migration.md "docdb-migration.md").

### Functional differences

#### Functional differences between Amazon DocumentDB 5.0 and 8.0

With the release of Amazon DocumentDB 8.0, there are functional differences between Amazon DocumentDB 5.0 and Amazon DocumentDB 8.0:

- Planner v1 is the default query planner in Amazon DocumentDB 5.0, whereas the more performant Planner v3 is the default in Amazon DocumentDB 8.0.
- New features in Amazon DocumentDB 8.0 including Views, Collation and operators like $merge are compatible only with Planner v3.
- Compression is turned ON by default in Amazon DocumentDB 8.0 and is set to use Zstandard algorithm. Furthermore, in Amazon DocumentDB 8.0 'enabled' is no longer a valid choice; you may select from Zstd, LZ4 and none.
- Newer capabilities of Amazon DocumentDB 5.0 including Serverless and R8g instances are currently not available in Amazon DocumentDB 8.0.

## MongoDB 5.0 compatibility

###### Topics

- [What's new in Amazon DocumentDB 5.0](#compatibility-whatsnew-5 "#compatibility-whatsnew-5")
- [Get started with Amazon DocumentDB 5.0](#compatibility-getstarted-5 "#compatibility-getstarted-5")
- [Upgrade or migrate to Amazon DocumentDB 5.0](#compatibility-upgrade-5 "#compatibility-upgrade-5")
- [Functional differences](#compatibility-differences-5 "#compatibility-differences-5")

### What's new in Amazon DocumentDB 5.0

Amazon DocumentDB 5.0 introduces new features and capabilities that include storage limits and client-side field level encryption.
The summary below introduces some of major features that were introduced in Amazon DocumentDB 5.0.
To see a full list of the new capabilities, see the [Release notes](release-notes.md "release-notes.md").

- Increased storage limit to 128 TiB for all instance-based Amazon DocumentDB clusters and shard-based elastic clusters.
- Introduced Amazon DocumentDB 5.0 Engine Version 3.0.775)
  - Support for MongoDB 5.0 API drivers
  - Support for Client-side Field Level Encryption (FLE).
    You can now encrypt fields at the client-side before writing the data to Amazon DocumentDB cluster.
    For more information, see [Client-side field level encryption](field-level-encryption.md "field-level-encryption.md").
  - New aggregation operators: `$dateAdd`, `$dateSubtract`
  - Supports for indexes with `$elemMatch` operator.
    As a result, queries having `$elemMatch` will result in index scans.

Amazon DocumentDB does not support every MongoDB 5.0 feature.
When we built Amazon DocumentDB 5.0, we worked backwards from the feature and capabilities that our customers asked us to build the most.
We will continue to add additional MongoDB 5.0 capabilities based on what customers ask us to build.
For the latest list of supported APIs, please see [Supported MongoDB APIs, operations, and data types in Amazon DocumentDB](mongo-apis.md "mongo-apis.md").

### Get started with Amazon DocumentDB 5.0

To get started with Amazon DocumentDB 5.0, please see the [Get Started Guide](get-started-guide.md "get-started-guide.md").
You can create a new Amazon DocumentDB 5.0 cluster using the AWS Management Console or the AWS SDK, AWS CLI, or AWS CloudFormation.
When connecting to Amazon DocumentDB, it is required that you use a MongoDB driver or utility that is compatible with MongoDB 5.0 or higher.

###### Note

When using the AWS SDK, AWS CLI, or AWS CloudFormation, the engine version will default to 5.0.0.
You must explicitly specify the parameter `engineVersion = 4.0.0` to create a new Amazon DocumentDB 4.0 cluster or `engineVersion = 3.6.0` to create a new Amazon DocumentDB 3.6 cluster.
For a given Amazon DocumentDB cluster, you can determine the cluster version using the AWS CLI to call `describe-db-clusters` or use the Amazon DocumentDB management console to view the engine version number for a particular cluster.

Amazon DocumentDB 5.0 supports the Amazon EC2 `r8g` Graviton4 processor and Graviton2 processors such as `r6g` and `t4.medium` instance types for your clusters and is available in all supported regions (see [Instances](what-is.md#what-is-db-instances "what-is.md#what-is-db-instances")).
For more information on pricing, see [Amazon DocumentDB (with MongoDB compatibility) Pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/").

### Upgrade or migrate to Amazon DocumentDB 5.0

You can migrate from MongoDB 3.6 or MongoDB 4.0 to Amazon DocumentDB 5.0 using the [AWS DMS](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/") or utilities like [`mongodump`, `mongorestore`, `mongoimport`, and `mongoexport`](backup_restore-dump_restore_import_export_data.md "backup_restore-dump_restore_import_export_data.md").
For instructions on how to migrate, see [Upgrading your Amazon DocumentDB cluster using AWS Database Migration Service](docdb-migration.md "docdb-migration.md").

### Functional differences

#### Functional differences between Amazon DocumentDB 4.0 and 5.0

With the release of Amazon DocumentDB 5.0, there are functional differences between Amazon DocumentDB 4.0 and Amazon DocumentDB 5.0:

- The backup built-in role now supports `serverStatus`.
  Action - Developers and applications with backup role can collect statistics about the state of the Amazon DocumentDB cluster.
- The `SecondaryDelaySecs` field replaces `slaveDelay` in `replSetGetConfig` output.
- The **hello** command replaces `isMaster` - **hello** returns a document that describes the role of a Amazon DocumentDB cluster.
- Amazon DocumentDB 5.0 now supports index scans with the `$elemMatch` operator in the first nesting level.
  Index scans are supported when the query only filter has one level of the `$elemMatch` filter but are not supported if a nested `$elemMatch` query is included.

For example, in Amazon DocumentDB 5.0, if you include the `$elemMatch` operator in the nested level, it will not return a value as it does in Amazon DocumentDB 4.0:

```
db.foo.insert(
[
    {a: {b: 5}},
    {a: {b: [5]}},
    {a: {b: [3, 7]}},
    {a: [{b: 5}]},
    {a: [{b: 3}, {b: 7}]},
    {a: [{b: [5]}]},
    {a: [{b: [3, 7]}]},
    {a: [[{b: 5}]]},
    {a: [[{b: 3}, {b: 7}]]},
    {a: [[{b: [5]}]]},
    {a: [[{b: [3, 7]}]]}
]);

// DocumentDB 5.0
> db.foo.find({a: {$elemMatch: {b: {$elemMatch: {$lt: 6, $gt: 4}}}}}, {_id: 0})
{ "a" : [ { "b" : [ 5 ] } ] }

// DocumentDB 4.0
> db.foo.find({a: {$elemMatch: {b: {$elemMatch: {$lt: 6, $gt: 4}}}}}, {_id: 0})
{ "a" : [ { "b" : [ 5 ] } ] }
{ "a" : [ [ { "b" : [ 5 ] } ] ] }
```

- The "$" projection in Amazon DocumentDB 4.0 returns all documents with all fields. 
 With Amazon DocumentDB 5.0, the **find** command with a "$" projection returns documents that match the query parameter containing only the field that matched the "$" projection.
- In Amazon DocumentDB 5.0, the **find** commands with `$regex` and `$options` query parameters return an error: "Cannot set options in both `$regex` and `$options`".
- With Amazon DocumentDB 5.0, `$indexOfCP` now returns "-1" when:
  - the substring is not found in the string expression, or
  - start is a number greater than end, or
  - start is a number greater than the byte length of the string.

- In Amazon DocumentDB 4.0, `$indexOfCP` returns "0" when the start position is a number greater than end or the byte length of the string.
- With Amazon DocumentDB 5.0, projection operations in `_id fields`, for example `{"_id.nestedField" : 1}`, return documents that only include the projected field.
  Whereas in Amazon DocumentDB 4.0, nested field projection commands do not filter out any document.

## MongoDB 4.0 compatibility

###### Topics

- [Amazon DocumentDB 4.0 features](#compatibility-whatsnew "#compatibility-whatsnew")
- [Get started with Amazon DocumentDB 4.0](#compatibility-getstarted "#compatibility-getstarted")
- [Upgrade or migrate to Amazon DocumentDB 4.0](#compatibility-upgrade "#compatibility-upgrade")
- [Functional differences](#compatibility-differences "#compatibility-differences")

### Amazon DocumentDB 4.0 features

Amazon DocumentDB 4.0 introduced many new features and capabilities that included ACID transactions and improvements to change streams.
The summary below shows some of the major features that were introduced in Amazon DocumentDB 4.0.
To see a full list of the capabilities, see the [Release notes](release-notes.md "release-notes.md").

- **ACID Transactions**: Amazon DocumentDB now supports the ability to perform transactions across multiple documents, statements, collections, and databases. Transactions simplify application development by enabling you to perform atomic, consistent, isolated, and durable (ACID) operations across one or more documents within an Amazon DocumentDB cluster. For more information, see [Transactions in Amazon DocumentDB](transactions.md "transactions.md").
- **Change streams**: You now have the ability to open a change stream at the cluster level (`client.watch()` or `mongo.watch()`) and the database (`db.watch()`), you can specify a `startAtOperationTime` to open a change stream cursor, and lastly you can now extend your change stream retention period to 7 days (previously 24 hours). For more information, see [Using change streams with Amazon DocumentDB](change_streams.md "change_streams.md").
- **AWS Database Migration Service** (AWS DMS): You can now use AWS DMS to migrate your MongoDB 4.0 workloads to Amazon DocumentDB. AWS DMS now supports a MongoDB 4.0 source, Amazon DocumentDB 4.0 target, and an Amazon DocumentDB 3.6 source for performing upgrades between Amazon DocumentDB 3.6 and 4.0. For more information, see [AWS DMS Documentation.](../../../dms/latest/userguide/Welcome.md "../../../dms/latest/userguide/Welcome.md")
- **Performance and indexing**: You can now utilize an index with `$lookup`, find queries with a projection that contain one field or one field and the `_id` field can be served direct from the index and without needing to read from the collection (covered query), the ability to `hint()` with `findAndModify`, performance optimizations for `$addToSet`, and improvements to reduce overall index sizes. For more information, see [Release notes](release-notes.md "release-notes.md").
- **Operators**: Amazon DocumentDB 4.0 now supports a number of new aggregation operators: `$ifNull`, `$replaceRoot`, `$setIsSubset`, `$setIntersection`, `$setUnion`, `$setEquals`. You can see all the MongoDB APIs, Operations, and Data Types that we support at [Supported MongoDB APIs, operations, and data types in Amazon DocumentDB](mongo-apis.md "mongo-apis.md").
- **Role based access control** (RBAC): With both `ListCollection` and `ListDatabase` commands you can now optionally use the `authorizedCollections` and `authorizedDatabases` parameters to allow users to list the collections and databases that they have permission to access without requiring the `listCollections` and `listDatabase` roles, respectively. You also have the ability to kill your own cursors without requiring the `KillCursor` role.

Amazon DocumentDB does not support every MongoDB 4.0 feature. When we built Amazon DocumentDB 4.0, we worked backwards from the feature and capabilities that our customers asked us to build the most. We will continue to add additional MongoDB 4.0 capabilities based on what customers ask us to build. For example, Amazon DocumentDB 4.0 does not currently support the type conversion operators or the string operators that were introduced in MongoDB 4.0. For the latest list of supported APIs, please see [Supported MongoDB APIs, operations, and data types in Amazon DocumentDB](mongo-apis.md "mongo-apis.md").

### Get started with Amazon DocumentDB 4.0

To get started with Amazon DocumentDB 4.0, please see the [Get Started Guide](get-started-guide.md "get-started-guide.md"). You can create a new Amazon DocumentDB 4.0 cluster using the AWS Management Console or the AWS SDK, AWS CLI, or AWS CloudFormation. When connecting to Amazon DocumentDB, it is required that you use a MongoDB driver or utility that is compatible with MongoDB 4.0 or higher.

###### Note

When using the AWS SDK, AWS CLI, or AWS CloudFormation, the engine version will default to 5.0.0.
You must explicitly specify the parameter `engineVersion = 4.0.0` to create a new Amazon DocumentDB 4.0 cluster or `engineVersion = 3.6.0` to create a new Amazon DocumentDB 3.6 cluster.
For a given Amazon DocumentDB cluster, you can determine the cluster version using the AWS CLI to call `describe-db-clusters` or use the Amazon DocumentDB management console to view the engine version number for a particular cluster.

Amazon DocumentDB 4.0 supports `r5`, `r6g`, `t3.medium`, and `t4g.medium` instance types for your clusters and is available in all supported regions.
There is no additional cost for using Amazon DocumentDB 4.0. For more information on pricing, see [Amazon DocumentDB (with MongoDB compatibility) Pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/").

### Upgrade or migrate to Amazon DocumentDB 4.0

You can migrate from MongoDB 3.6 or MongoDB 4.0 to Amazon DocumentDB 4.0 utilizing the [AWS DMS](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/") or utilities like [`mongodump`, `mongorestore`, `mongoimport`, and `mongoexport`](backup_restore-dump_restore_import_export_data.md "backup_restore-dump_restore_import_export_data.md"). Similarly, you can use the same tools to upgrade from Amazon DocumentDB 3.6 to Amazon DocumentDB 4.0. For instructions on how to migrate, see [Upgrading your Amazon DocumentDB cluster using AWS Database Migration Service](docdb-migration.md "docdb-migration.md").

### Functional differences

#### Functional differences between Amazon DocumentDB 3.6 and 4.0

With the release of Amazon DocumentDB 4.0, there are functional differences between Amazon DocumentDB 3.6 and Amazon DocumentDB 4.0:

- **Projection for nested documents**: Amazon DocumentDB 3.6 considers the first field in a nested document when applying a projection. However, Amazon DocumentDB 4.0 will parse subdocuments and apply the projection to each sub document as well. For example: if the projection is `"a.b.c": 1`, then the behavior in both versions is identical. However, if the projection is `{a:{b:{c:1}}}` then Amazon DocumentDB 3.6 will only apply the projection to 'a' and not 'b' or 'c'.
- **Behavior for `minKey`, `maxKey`**: In Amazon DocumentDB 4.0, the behavior for `{x:{$gt:MaxKey}}` returns nothing, and for `{x:{$lt:MaxKey}}` returns everything.
- **Document comparison differences**: Comparing numerical values of different types (double, int, long) in subdocuments (e.g., `b` in `{"_id" :1, "a" :{"b":1}}`) now provides a consistent output across numerical data types and for each level of a document.

#### Functional differences between Amazon DocumentDB 4.0 and MongoDB 4.0

Below are functional differences between Amazon DocumentDB 4.0 and MongoDB 4.0.

- **Lookup with empty key in path**: When a collection contains a document with empty key inside the array (e.g. `{"x" : [ { "" : 10 }, { "b" : 20 } ]}`), and when the key used in the query ends in an empty string (e.g. `x.`), then Amazon DocumentDB will return that document since it traverses all the documents in the array whereas MongoDB will not return that document.
- **`$setOnInsert` along with `$` in the path**: The field operator `$setOnInsert` will not work in combination with `$` in the path in Amazon DocumentDB, which is also consistent with MongoDB 4.0.
