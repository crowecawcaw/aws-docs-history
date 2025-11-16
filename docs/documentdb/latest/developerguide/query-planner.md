# Query planner v2

The new query planner for Amazon DocumentDB (planner version 2.0) features advanced query optimization capabilities and improved performance.
Planner version 2.0 for Amazon DocumentDB 5.0 delivers up to 10x performance improvement over the prior version when using `find` and `update` operators with indexes.
Performance improvements primarily come from using more optimal index plans and enabling index scan support for operators such as negation operators (`$neq`, `$nin`) and nested `$elementMatch`.
Planner version 2.0 queries run faster through better cost estimation techniques, optimized algorithms, and enhanced stability.
Planner version 2.0 supports plan cache filter APIs as well, which enhances planner stability.
With this feature, Amazon DocumentDB 5.0 now offers the ability to select from the different versions of query planner.

###### Topics

- [Prerequisites](#nqp-prerequisites "#nqp-prerequisites")
- [Selecting planner version 2.0 as the default query planner](#second-concept-chapter "#second-concept-chapter")
- [Best practices](#nqp-best-practices "#nqp-best-practices")
- [Limitations](#nqp-limitations "#nqp-limitations")
- [Improvements to Find and Update Operators](#operator-improvements "#operator-improvements")
- [Plan cache filter API](#plan-cache-filter-api "#plan-cache-filter-api")
- [Potential behavior differences between planner version 1.0, 2.0, and MongoDB](#planner-behavior-differences "#planner-behavior-differences")
- [Planner version 2.0 bridges behavior gap with MongoDB](#planner-v2-mongo-gap-bridge "#planner-v2-mongo-gap-bridge")

## Prerequisites

The following prerequisites apply to planner version 2.0:

- Planner version 2.0 is available in all regions where engine version 5.0 is available.
- To opt for using version 2.0 as the default query planner, your cluster needs to be on engine patch version 3.0.15902 or later of Amazon DocumentDB version 5.0.
  For steps to update to the latest engine version patch, see [Performing a patch update to a cluster's engine version](db-cluster-version-upgrade.md "db-cluster-version-upgrade.md").
- To set planner version 2.0 as the default query planner, you need IAM permissions to update cluster parameter groups.

## Selecting planner version 2.0 as the default query planner

Use the following steps to select 2.0 as the default query planner from the console or CLI:

- Follow the steps in [Modifying Amazon DocumentDB cluster parameters](cluster_parameter_groups-parameters.md "cluster_parameter_groups-parameters.md") to modify your cluster’s parameter group.
- For the parameter titled ‘plannerVersion’, change the value to 2.0 indicating planner version 2.0.
- Select **Apply immediately** (selecting **Apply at reboot** will render the selection ineffective until next reboot of the cluster).

## Best practices

For expected results, use the following best practices when applying planner version 2.0:

- In a global cluster, select the same `plannerVersion` value (1.0 or 2.0) in the cluster parameter groups for both regions.
  Note that selecting different planner versions in primary and secondary regions may cause inconsistent query behavior and performance.
- Updating to planner version 2.0 during a scheduled maintenance windows or during reduced traffic periods will be the least disruptive, as there may be increased error rates if the planner version is changed when workloads are actively running.
- Planner version 2.0 works most optimally with MongoDB shell version 5.0.

## Limitations

The following limitations apply to planner version 2.0:

- Planner version 2.0 is not supported in elastic clusters, which will fall back to planner version 1.0.
- Planner version 2.0 is not supported for aggregation and distinct commands, which will fall back to planner version 1.0.
- Queries that contain regex, text search, geospatial, jsonschema or `$expr` in filters are not supported with plan cache filter in planner version 2.0.

## Improvements to `Find` and `Update` Operators

Planner version 2.0 optimizes fundamental operations including `find`, `update`, `delete`, and `find-and-modify` commands.
The following tabbed sections show enhanced capabilities for indexes, as well as the query performance improvements with planner version 2.0:

Enhanced index support

- Planner version 2.0 adds index support for negation operators including `$nin`, `$ne`, `$not {eq}`, and `$not {in}`, as well as `$type` and `$elemMatch`.

```
Sample Document: { "x": 10, "y": [1, 2, 3] }

db.foo.createIndex({ "x": 1, "y": 1 })
db.foo.find({ "x": {$nin: [20, 30] }})
db.foo.find({"x":{ $type: "string" }})

db.foo.createIndex({"x.y": 1})
db.foo.find({"x":{$elemMatch:{"y":{$elemMatch:{"$gt": 3 }}}}})
```

- Planner version 2.0 utilizes sparse or partial indexes even when `$exists` is not present in the query expression.

```
Sample Document: {"name": "Bob", "email": "example@fake.com" }

*Using Planner Version 1.0, you can specify the command as shown below:*
db.foo.find({email: "example@fake.com", email: {$exists: true}})

*Using Planner Version 2.0, you can specify command without $exists:*
db.foo.find({ email: "example@fake.com" })
```

- Planner version 2.0 will utilize partial indexes even when the query condition doesn't exactly match the partial index filter expression.

```
Sample Document: {"name": "Bob", "age": 34}
db.foo.createIndex({"age":1},{partialFilterExpression:{"age":{$lt:50}}})

*With Planner Version 1.0, index is used only when the query condition meets the partial
 index filter criterion:*
     db.foo.find({"age":{$lt:50}})

*With Planner Version 2.0, index is used even when the query condition doesn’t meet the index
criterion:*
db.foo.find({"age":{$lt:30}})
```

- Planner version 2.0 utilizes partial index scan with $elemMatch queries.

```
Sample Document: {"name": "Bob", "age": [34,35,36]}
db.foo.createIndex({"age":1},{partialFilterExpression:{"age":{$lt:50,$gt:20}}})
db.foo.find({age:{$elemMatch:{$lt:50,$gt:20}}})
```

- Planner version 2.0 includes index scan support for `$regex`, without the need of providing `$hint` in your application code.
  `$regex` supports index on prefix searches only.

```
Sample Document: { "x": [1, 2, 3], "y": "apple" }
db.foo.createIndex({ "x": 1, "y": 1 })
db.foo.find({"y":{ $regex: "^a" }})
```

- Planner version 2.0 improves the performance of queries involving multi-key indexes, with equality conditions on multi-key field.

```
Sample Document: {"x": [1, 2, 3],
"y": 5}
db.foo.createIndex({"x": 1, "y":1})
db.foo.find({"x": 2,
"y": {$gt: 1}}).limit(1)
```

- Planner version 2.0 improves the performance of queries that involve multiple filters, especially on collections with documents greater than 8 KB.

```
Sample Document: {"x": 2,
"y": 4,
"z": 9,
"t": 99}
db.foo.find({$and: [{"x": {$gt : 1}, "y": {$gt : 3}, "z": {$lt : 10},
"t":{$lt : 100}}]})
```

- Planner version 2.0 improves the performance of queries when using the `$in` operator with a compound index by eliminating the sort stage.

```
Sample Document: {"x": 2,
"y": 4,
"z": 9,
"t": 99}
db.foo.createIndex({"x":1, "y":1})
db.foo.find({"x":2,
"y":$in:[1,2,3,4]}).sort({x:1,y:1})
```

It also improves the performance of queries that use multi-key indexes with `$in` elements.

```
Sample Document: {"x": [1, 2, 3]}
db.foo.createIndex({"x": 1})
db.foo.find("x":{$in:[>100 elements]})

```

Query performance improvements

- Planner version 2.0 improves the performance of queries that involve multiple filters, especially on collections with documents greater than 8 KB.

```
Sample Document: {"x": 2,
"y": 4,
"z": 9,
"t": 99}
db.foo.find({$and: [{"x": {$gt : 1}, "y": {$gt : 3}, "z": {$lt : 10},
"t":{$lt : 100}}]})
```

- Planner version 2.0 improves the performance of queries when using the `$in` operator with a compound index by eliminating the sort stage.

```
Sample Document: {"x": 2,
"y": 4,
"z": 9,
"t": 99}
db.foo.createIndex({"x":1, "y":1})
db.foo.find({"x":2,
"y":$in:[1,2,3,4]}).sort({x:1,y:1})
```

It also improves the performance of queries that use multikey indexes with `$in` elements.

```
Sample Document: {"x": [1, 2, 3]}
db.foo.createIndex({"x": 1})
db.foo.find("x":{$in:[>100 elements]})

```

## Plan cache filter API

###### Note

Text index is not supported with plan cache filter.

- Planner version 2.0 adds support for the index filter feature that allows you to specify a list of indexes that a specific query shape can use.
  This feature is accessible through the API and can be controlled from the server side.
  If you experience a query regression, this feature gives you a faster and more flexible option to mitigate the issue without having to modify your application code.

```
db.runCommand({ planCacheSetFilter: <collection>, query: <query>,
sort: <sort>, // optional,
indexes: [ <index1>, <index2>, ...],
comment: <any> // optional})
```

To list all filters on the collection, use the following command:

```
db.runCommand(
{
planCacheListFilters: <collection>
}
)
```

This command shows all index filters on the collection.
Example output:

```
{
"filters" : [
{
"query" : {a: "@", b: "@"},
"sort" : {a: 1},
"indexes" : [
<index1>,
...
]
},
...
],
"ok": 1
}
```

- You can use two new fields from the `explain` command output to analyze planner version 2.0’s index filtering: `indexFilterSet` and `indexFilterApplied`.
  `indexFilterSet` is set to "true" if there’s an index filter set on the collection that matches the query shape.
  `indexFilterApplied` is set to "true" if, and only if the query applied index filter and chose a plan using an index in the filter list.

You can clear the index filter with the following command:

```
db.runCommand(
{
planCacheClearFilters: <collection>>
query: <query pattern>, // optional
sort: <sort specification>, // optional
comment: <any>. //optional
}
)
```

To clear all filters on collection "foo", use the following command:

```
db.runCommand({planCacheClearFilters: "foo"})
```

To clear a specific query shape with any sort, you can copy and paste the query shape from the output of `planCacheListFilters`:

```

db.runCommand({planCacheClearFilters: "foo", query: {a: @}})
```

To clear a specific query shape with a specified field to sort by, you can copy and paste the query shape from the output of `planCacheListFilters`:

```
db.runCommand({planCacheClearFilters: "foo", query: {a: @},sort: {a: 1}})
```

## Potential behavior differences between planner version 1.0, 2.0, and MongoDB

In some edge cases, it is possible that planner version 2.0 may produce results that slightly vary from results in MongoDB.
This section walks through some examples of these possibilities.

$(update) and $(projection)

- In some cases, `$(update)` and `$(projection)` operators in MongoDB may behave differently from Amazon DocumentDB's planner version 1.0.
  Below are some examples:

```
db.students_list.insertMany( [ { _id: 5, student_ids: [ 100, 200 ], grades: [ 95, 100 ], grad_year: [ 2024, 2023 ] } ] )
```

```
db.students_list.updateOne({ student_ids: 100, grades: 100, grad_year: 2024 },
{ $set: { “grad_year.$”: 2025 } }
```

    + **Planner version 1.0** — Updates field 2022
    + **MongoDB** — Updates field 2022
    + **Planner version 2.0** — Updates field 2021

- ```
  db.col.insert({x:[1,2,3]})
  db.col.update({$and:[{x:1},{x:3}]},{$set:{"x.$":500}})
  ```

````



	+ **Planner version 1.0** — Randomly updates the first element matched
	+ **MongoDB** — Randomly updates the first element matched
	+ **Planner version 2.0** — Does not make updates
* ```
db.col.insert({x:[1,2,3]})
db.col.find()

````

    + **Planner version 1.0** — Randomly selects the matched element
    + **MongoDB** — Randomly selects the matched element
    + **Planner version 2.0** — Does not make a selection

- ```
  db.col.insert({x:100})
  db.col.update({x:100},{x:100})
  ```

```



	+ **Planner version 1.0** — nModified count changes
	+ **MongoDB** — nModified count changes
	+ **Planner version 2.0** — nModified count does not change when updated with the same value.
* When `$(update)` operator is used with `$setOnInsert`, planner version 1.0 and MongoDB throw an error, but planner version 2.0 does not.
* Renaming a non-existing field to `$field` throws an error in planner version 2.0, whereas does not produce updates in planner version 1.0 and MongoDB.


Index behavior

* Planner version 2.0 throws an error when `$hint` is applied with an unsuitable index, whereas planner version 1.0 and MongoDB do not.



```

// Insert
db.col.insert({x:1})
db.col.insert({x:2})
db.col.insert({x:3})

// Create index on x with partialFilter Expression {x:{$gt:2}}
db.col.createIndex({x:1},{partialFilterExpression:{x:{$gt:2}}})

// Mongodb allows hint on the following queries
db.col.find({x:1}).hint("x_1")
// result is no documents returned because {x:1} is not indexed by the partial index
// Without $hint mongo should return {x:1}, thus the difference in result between COLSCAN and IXSCAN

DocumentDB will error out when $hint is applied on such cases.
db.col.find({x:1}).hint("x_1")
Error: error: {
"ok" : 0,
"operationTime" : Timestamp(1746473021, 1),
"code" : 2,
"errmsg" : "Cannot use Hint for this Query. Index is multi key index , partial index or sparse index and query is not optimized to use this index."
}

rs0:PRIMARY> db.runCommand({"planCacheSetFilter": "col", "query": { location: {$nearSphere: {$geometry: {type: "Point", coordinates: [1, 1]}}}}, "indexes": ["name_1"]})
{
"ok" : 0,
"operationTime" : Timestamp(1750815778, 1),
"code" : 303,
"errmsg" : "Unsupported query shape for index filter $nearSphere"
}

```
* `$near` cannot use `$hint({“$natural”:1})` in planner version 2.0.



```

// indexes present are index on x and geo index

rs0:PRIMARY> db.usarestaurants.getIndexes()
[
{
"v" : 4,
"key" : {
"_id" : 1
},
"name" : "_id_",
"ns" : "test.usarestaurants"
},
{
"v" : 4,
"key" : {
"location" : "2dsphere"
},
"name" : "location_2dsphere",
"ns" : "test.usarestaurants",
"2dsphereIndexVersion" : 1
}
]

// Planner Version 2.0 will throw an error when $hint is applied with index "x_1"
rs0:PRIMARY> db.usarestaurants.find({    "location":{       "$nearSphere":{ "$geometry":{             "type":"Point",             "coordinates":[                -122.3516,                47.6156             ]          },          "$minDistance":1, "$maxDistance":2000       }    } }, {    "name":1 }).hint({"$natural": 1})
Error: error: {
"ok" : 0,
"operationTime" : Timestamp(1746475524, 1),
"code" : 291,
"errmsg" : "unable to find index for $geoNear query"
}

// Planner Version 1.0 and MongoDB will not throw an error
db.usarestaurants.find({ "location":{ "$nearSphere":{          "$geometry":{ "type":"Point", "coordinates":[ -122.3516, 47.6156 ] }, "$minDistance":1,          "$maxDistance":2000 } } }, { "name":1 }).hint({"$natural": 1})
{ "\_id" : ObjectId("681918e087dadfd99b7f0172"), "name" : "Noodle House" }

```
* While MongoDB supports complete regex index scans, planner version 2.0 supports regex index scan on prefix fields only.



```

// index on x
db.col.createIndex({x:1})

// index scan is used only for prefix regexes
rs0:PRIMARY> db.col.find({x: /^x/}).explain()
{
"queryPlanner" : {
"plannerVersion" : 2,
"namespace" : "test.col",
"winningPlan" : {
"stage" : "IXSCAN",
"indexName" : "x_1",
"direction" : "forward",
"indexCond" : {
"$and" : [
                    {
                        "x" : {
                            "$regex" : /^x/
}
}
]
},
"filter" : {
"x" : {
"$regex" : /^x/
}
}
}
},
"indexFilterSet" : false,
"indexFilterApplied" : false,
"ok" : 1,
"operationTime" : Timestamp(1746474527, 1)
}

// COLSCAN is used for non-prefix regexes
rs0:PRIMARY> db.col.find({x: /x$/}).explain()
{
    "queryPlanner" : {
        "plannerVersion" : 2,
        "namespace" : "test.col",
        "winningPlan" : {
            "stage" : "COLLSCAN",
            "filter" : {
                "x" : {
                    "$regex" : /x$/
}
}
}
},
"indexFilterSet" : false,
"indexFilterApplied" : false,
"ok" : 1,
"operationTime" : Timestamp(1746474575, 1)

```
* There are some inherent differences in using plan cache filters with planner version 2.0 as compared to MongoDB.
 While planner version 2.0 does not support specifying “projection” and “collation” with plan cache filters, MongoDB does.
 However, MongoDB index filter is in-memory only and is lost after restart.
 Planner version 2.0 persists index filters through restarts and patches.


Others

* The format of DML audit logs when using planner version 2.0 varies slightly from that of planner version 1.0.



```

command - db.col.find({x:1})

******\*\******* Audit logs generated ********\*\*********

// v1 format for dml audit logs
{"atype":"authCheck","ts":1746473479983,"timestamp_utc":"2025-05-05 19:31:19.983","remote_ip":"127.0.0.1:47022","users":[{"user":"serviceadmin","db":"test"}],"param":{"command":"find","ns":"test.col","args":{"batchSize":101,"filter":{"x":1},"find":"col","limit":18446744073709551615,"lsid":{"id":{"$binary":"P6RCGz9ZS4iWBSSHWXW15A==","$type":"4"},"uid":{"$binary":"6Jo8PisnEi3dte03+pJFjdCyn/5cGQL8V2KqaoWsnk8=","$type":"0"}},"maxScan":18446744073709551615,"singleBatch":false,"skip":0,"startTransaction":false},"result":0}}

// v2 formal for dml audit logs
{"atype":"authCheck","ts":1746473583711,"timestamp_utc":"2025-05-05 19:33:03.711","remote_ip":"127.0.0.1:37754","users":[{"user":"serviceadmin","db":"test"}],"param":{"command":"find","ns":"test.col","args":{"find":"col","filter":{"x":1},"lsid":{"id":{"$binary":"nJ88TGCSSd+BeD2+ZtrhQg==","$type":"4"}},"$db":"test"},"result":0}}

```
* The index condition as part of the explain plan:



```

rs0:PRIMARY> db.col.createIndex({index1:1})
{
"createdCollectionAutomatically" : false,
"numIndexesBefore" : 1,
"numIndexesAfter" : 2,
"ok" : 1,
"operationTime" : Timestamp(1761149251, 1)
}

```

Planner version 2.0 explain plan output displaying index condition and filter:



```

rs0:PRIMARY> db.col.find({$and:[{price:{$eq:300}},{item:{$eq:"apples"}}]}).explain()
{
	"queryPlanner" : {
		"plannerVersion" : 2,
		"namespace" : "test.col",
		"winningPlan" : {
			"stage" : "IXSCAN",
			"indexName" : "price_1",
			"direction" : "forward",
			"indexCond" : {
				"$and" : [
{
"price" : {
"$eq" : 300
}
}
]
},
"filter" : {
"$and" : [
					{
						"item" : {
							"$eq" : "apples"
}
}
]
}
}
},
"indexFilterSet" : false,
"indexFilterApplied" : false,
"ok" : 1,
"operationTime" : Timestamp(1761149497, 1)
}

```

Planner version 1.0 explain plan output:



```

rs0:PRIMARY> db.col.find({$and:[{price:{$eq:300}},{item:{$eq:"apples"}}]}).explain()
{
"queryPlanner" : {
"plannerVersion" : 1,
"namespace" : "test.col",
"winningPlan" : {
"stage" : "IXSCAN",
"indexName" : "price_1",
"direction" : "forward"
}
},
"ok" : 1,
"operationTime" : Timestamp(1761149533, 1)
}

```



## Planner version 2.0 bridges behavior gap with MongoDB


There are some areas where planner version 2.0 closes the behavior gaps from MongoDB:



* Planner version 2.0 allows numeric index lookup on flattened arrays for `$elemMatch`:



```

doc: {"x" : [ [ { "y" : 1 } ] ] }

// Planner Version 2 and mongo

> db.bar.find({"x.0": {$elemMatch: {y: 1}}})
{ "_id" : ObjectId("68192947945e5846634c455a"), "x" : [ [ { "y" : 1 } ] ] }
> db.bar.find({"x": {$elemMatch: {"0.y": 1}}})
> { "\_id" : ObjectId("68192947945e5846634c455a"), "x" : [ [ { "y" : 1 } ] ] }

//Whereas Planner Version 1 wouldn't return any results.

> db.bar.find({"x.0": {$elemMatch: {y: 1}}})
> db.bar.find({"x": {$elemMatch: {"0.y": 1}}})

```
* While planner version 1.0 excluded strings in projection, planner version 2.0's behavior aligns with MongoDB and treats them as literal values"



```

// Planner V2/ MongoDB

> db.col.find()
> { "\_id" : ObjectId("681537738aa101903ed2fe05"), "x" : 1, "y" : 1 }
> db.col.find({},{x:"string"})
> { "\_id" : ObjectId("681537738aa101903ed2fe05"), "x" : "string" }

// Planner V1 treats strings as exclude in projection
rs0:PRIMARY> db.col.find()
{ "\_id" : ObjectId("68153744d42969f11d5cca72"), "x" : 1, "y" : 1 }
rs0:PRIMARY> db.col.find({},{x:"string"})
{ "\_id" : ObjectId("68153744d42969f11d5cca72"), "y" : 1 }

```
* Planner version 2.0, like MongoDB, does not allow projection on same fields “x” and “x.a”:



```

// Planner version 2/MongoDB will error out

> db.col.find()
> { "\_id" : ObjectId("68153da2012265816bc9ba23"), "x" : [ { "a" : 1 }, 3 ] }
> db.col.find({},{"x.a":1,"x":1}) // error

// Planner Version 1 does not error out
db.col.find()
{ "\_id" : ObjectId("68153da2012265816bc9ba23"), "x" : [ { "a" : 1 }, 3 ] }

db.col.find({},{"x.a":1,"x":1})
{ "\_id" : ObjectId("68153d60143af947c720d099"), "x" : [ { "a" : 1 }, 3 ] }

```
* Planner version 2.0, like MongoDB, allows projection on subdocuments:



```

// Planner Version2/MongoDB supports projections on subdocuments
db.col.find()
{ "\_id" : ObjectId("681542d8f35ace71f0a50004"), "x" : [ { "y" : 100 } ] }

> db.col.find({},{"x":{"y":1}})
> { "\_id" : ObjectId("681542b7a22d548e4ac9ddea"), "x" : [ { "y" : 100 } ] }

// Planner V1 throws error if projection is subdocument
db.col.find()
{ "\_id" : ObjectId("681542d8f35ace71f0a50004"), "x" : [ { "y" : 100 } ] }
rs0:PRIMARY> db.col.find({},{"x":{"y":1}})
Error: error: {
"ok" : 0,
"operationTime" : Timestamp(1746223914, 1),
"code" : 2,
"errmsg" : "Unknown projection operator y"
}

```
* With Planner version 2.0, like MongoDB, projection does not support fields after the `$` operator:



```

// Mongo and Planner Version 2 will error out
db.col.find()
{ "\_id" : ObjectId("68155fa812f843439b593f3f"), "x" : [ { "a" : 100 } ] }
db.col.find({"x.a":100},{"x.$.a":1}) - // error

// v1 will not error out
db.col.find()
{ "\_id" : ObjectId("68155fa812f843439b593f3f"), "x" : [ { "a" : 100 } ] }
db.col.find({"x.a":100},{"x.$.a":1})
{ "\_id" : ObjectId("68155dee13b051d58239cd0a"), "x" : [ { "a" : 100 } ] }

```
* Planner version 2.0, like MongoDB, allows `$hint` usage:



```

// v1 will error out on $hint if there are no filters
db.col.find({}).hint("x_1")
Error: error: {
"ok" : 0,
"operationTime" : Timestamp(1746466616, 1),
"code" : 2,
"errmsg" : "Cannot use Hint for this Query. Index is multi key index , partial index or sparse index and query is not optimized to use this index."
}

// Mongo and Planner Version 2 will allow $hint usage
db.col.find({}).hint("x_1")
{ "\_id" : ObjectId("6818f790d5ba9359d68169cf"), "x" : 1 }

```

```
