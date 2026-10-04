

# Plan cache filters
<a name="plan-cache-filter"></a>

A plan cache filter, also called an index filter, restricts the set of indexes that the query planner is allowed to consider for a specific query shape. When a query matches a shape that has a filter, the planner chooses a plan only from the indexes named in that filter instead of evaluating every index on the collection.

A query shape is the combination of the query predicate, the sort specification, and the collection namespace, with the predicate values normalized. Two queries that differ only in their values share a shape, so a single filter covers all of them. In the output of `planCacheListFilters`, normalized values are shown as `"@"`.

A plan cache filter gives you a way to pin the plan, so that you can avoid choosing a slower index because of data distribution or index changes. Filters have the following properties:
+ **No application change is required.** Filters are set with a database command and applied on the server, so you can mitigate a regression without a code deployment. This is the main difference from a `hint`, which has to be added at every call site.
+ **The scope is one query shape.** A shape is defined by the collection, the predicate, and the sort, not by the full query, so a filter constrains only the queries that match that shape. Other queries on the same collection continue to be planned normally.
+ **The change is durable.** Filters persist across instance restarts and engine patching. Dropping the collection removes its filters.
+ **The change is reversible.** Clearing the filter returns the shape to normal cost-based planning, so a filter is a low-risk way to stabilize a workload while you investigate the underlying cause.

**Topics**
+ [Supported commands](#plan-cache-filter-support)
+ [Supported query shapes](#plan-cache-filter-shapes)
+ [Setting, listing, and clearing filters](#plan-cache-filter-api)
+ [Verifying that a filter is applied](#plan-cache-filter-explain)
+ [Examples](#plan-cache-filter-examples)
+ [Behavior with hints and index changes](#plan-cache-filter-behavior)

## Supported commands
<a name="plan-cache-filter-support"></a>

Plan cache filters require planner version 2.0 or later. The command that a filter can be applied to depends on the planner version and the Amazon DocumentDB minor version, as shown in the following table.


**Command support for plan cache filters**  

| Command | Minimum planner version | Minimum minor version | 
| --- | --- | --- | 
| `find` | 2.0 | 5.0.0, 8.0.0 | 
| `count` | 2.0 | 5.0.0, 8.0.0 | 
| `update` | 2.0 | 5.0.2, 8.0.2 | 
| `delete` | 2.0 | 5.0.2, 8.0.2 | 
| `findAndModify` | 2.0 | 5.0.2, 8.0.2 | 
| `distinct` | 3.0 | 8.0.0 | 
| `aggregate` | 3.0 | 8.0.2 | 

**Note**  
Planner version 3.0 is available only in Amazon DocumentDB 8.0. Because the `distinct` and `aggregate` commands require planner version 3.0, plan cache filters for those two commands are available only in Amazon DocumentDB 8.0. In Amazon DocumentDB 5.0, which supports planner version 2.0, filters apply to the `find`, `count`, `update`, `delete`, and `findAndModify` commands.

For the `aggregate` command, the shape is taken from the front of the pipeline: the leading `$match` supplies the filter, and a `$sort` immediately after it supplies the sort. `$skip` and `$limit` do not affect the shape, and neither do the stages beyond that point.

Amazon DocumentDB optimizes the pipeline before planning it, and a plan cache filter is matched against the optimized pipeline. The filter and sort that the planner sees can therefore differ from the stages you wrote. For example, two adjacent `$match` stages at the front of a pipeline are combined into a single `$and` predicate:

```
db.orders.aggregate([
  { $match: { status: "SHIPPED" } },
  { $match: { region: "us-east-1" } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } }
])
```

The planner sees one `$match` on `{$and: [{status: ...}, {region: ...}]}`, so the filter has to be set on that combined predicate.

```
db.runCommand({planCacheSetFilter: "orders",
query: { $and: [ { status: "SHIPPED" }, { region: "us-east-1" } ] },
indexes: [ "status_1_region_1" ]})
```

A filter set on the foreign collection of a `$lookup` or `$graphLookup` stage drives the index used to scan that foreign collection.

## Supported query shapes
<a name="plan-cache-filter-shapes"></a>

Starting with Amazon DocumentDB 5.0.2 and 8.0.2, the following operators can appear in a query shape that has a plan cache filter:
+ `$text`. The search string is normalized, so queries that differ only in the terms they search for share one shape.
+ `$near` and `$nearSphere`. Both operators normalize to the same shape. The coordinates, `$minDistance`, and `$maxDistance` are not part of the shape.
+ `$geoWithin` and `$geoIntersects`. The GeoJSON geometry type is part of the shape, so a `Polygon` query and a `MultiPolygon` query are different shapes. The coordinates are not part of the shape.
+ `$regex`, when used directly on a field. The pattern and options are normalized, so all regular expressions on the same field share one shape.

Setting a filter fails with error code 303 for a query shape that uses `$jsonSchema`, `$expr`, or `$sampleRate`. It also fails for the following shapes. A query that uses any of them is planned without a filter:
+ A `$regex` nested inside `$in`, `$nin`, or `$all`. An array that mixes regular expressions with literal values cannot be evaluated against an index, so a filter on that shape could never be applied.
+ A sort specification of `{$natural: 1}`. A `$natural` sort requests a collection scan, which is incompatible with restricting the planner to an index.

## Setting, listing, and clearing filters
<a name="plan-cache-filter-api"></a>

To set a plan cache filter, use the `planCacheSetFilter` command. The `query` and `sort` fields together specify the query shape, and `indexes` lists the index names that the planner is allowed to consider for that shape.

```
db.runCommand({
planCacheSetFilter: <collection>,
query: <query>,
sort: <sort>, // optional
indexes: [ <index1>, <index2>, ...],
comment: <any> // optional
})
```

For example, the following command restricts the planner to the `a_1` index for the shape `{a: {$eq: "@"}, b: {$eq: "@"}}` with no sort:

```
db.runCommand({planCacheSetFilter: "foo",
query: { a: 1, b: 1 },
sort: {},
indexes: [ "a_1" ]})
```

Setting a filter for a shape that already has one replaces the existing filter. After running the following two commands, the filter on the shape `{a: {$eq: "@"}, b: {$eq: "@"}}` is `["b_1"]`:

```
db.runCommand({planCacheSetFilter: "foo",
query: { a: 1, b: 1 },
sort: {},
indexes: [ "a_1" ]})

db.runCommand({planCacheSetFilter: "foo",
query: { a: 6, b: 10 },
sort: {},
indexes: [ "b_1" ]})
```

To list every filter on a collection, use the `planCacheListFilters` command:

```
db.runCommand({planCacheListFilters: <collection>})
```

The output shows each stored shape with its normalized values and its allowed index list:

```
{
"filters" : [
{
"query" : { "a" : { "$eq" : "@" } },
"sort" : { },
"indexes" : [ "a_1" ]
},
{
"query" : { "a" : { "$gt" : "@" } },
"sort" : { "a" : 1 },
"indexes" : [ "a_1_b_1" ]
}
],
"ok" : 1
}
```

The operator is preserved and only the value is replaced with `"@"`. An implicit equality such as `{a: 1}` is listed in its explicit form, `{"a": {"$eq": "@"}}`, and the elements of an `$in` array are replaced as a whole, as `{"a": {"$in": "@"}}`. A filter set without a sort is listed with an empty `sort` document.

To remove filters, use the `planCacheClearFilters` command.

```
db.runCommand({
planCacheClearFilters: <collection>,
query: <query pattern>, // optional
sort: <sort specification>, // optional
comment: <any> // optional
})
```

To clear every filter on the collection, omit both `query` and `sort`:

```
db.runCommand({planCacheClearFilters: "foo"})
```

Supplying both `query` and `sort` clears only the filter that has that exact sort. The values in `query` are normalized away, so any representative value works. To clear only the filter that was set without a sort, pass an empty `sort` document:

```
db.runCommand({planCacheClearFilters: "foo", query: {a: 1}, sort: {a: 1}})

db.runCommand({planCacheClearFilters: "foo", query: {a: 1}, sort: {}})
```

## Verifying that a filter is applied
<a name="plan-cache-filter-explain"></a>

The `explain` output includes two fields that report plan cache filter status:
+ `indexFilterSet` is `true` when a filter exists on the collection for the query's shape.
+ `indexFilterApplied` is `true` only when the query was planned using an index from that filter's list.

Starting with Amazon DocumentDB 5.0.2 and 8.0.2, these fields are reported for every command that supports plan cache filters, and in the profiler output for those commands. In earlier minor versions they were reported for the `find` command only. For more information about reading explain output, see [Query plan analysis](performance-query-plan-analysis.md).

A filter can match a query shape without being applied. If none of the indexes in the filter's list can serve the query, the planner replans without the filter and chooses an index on cost. In that case `indexFilterSet` is `true` and `indexFilterApplied` is `false`. This happens when the named indexes do not cover the query's fields, when the named indexes do not exist, or when a `$regex` shape cannot produce index bounds, such as an unanchored or case-insensitive pattern.

## Examples
<a name="plan-cache-filter-examples"></a>

The following examples use an `orders` collection, and a `customers` collection for the `$lookup` example, with these indexes:

```
db.orders.createIndex({ status: 1 })                         // status_1
db.orders.createIndex({ status: 1, orderDate: 1 })           // status_1_orderDate_1
db.orders.createIndex({ customerId: 1 })                     // customerId_1
db.customers.createIndex({ customerId: 1 })                  // customerId_1
```

### Example: pinning a `find` query to a compound index
<a name="plan-cache-filter-example-find"></a>

Consider a query that filters on `status` and sorts on `orderDate`:

```
db.orders.find({ status: "SHIPPED" }).sort({ orderDate: 1 })
```

The compound index `status_1_orderDate_1` satisfies both the predicate and the sort, so no separate sort is needed. If the planner instead chooses `status_1`, the query has to sort its results, which adds a `SORT` stage and gets more expensive as the number of matching orders grows. To restrict the planner to the compound index for this shape:

```
db.runCommand({planCacheSetFilter: "orders",
query: { status: "SHIPPED" },
sort: { orderDate: 1 },
indexes: [ "status_1_orderDate_1" ]})
```

Because values are normalized out of the shape, this one filter also covers `{ status: "PENDING" }`, `{ status: "CANCELLED" }`, and every other value of `status` with the same sort. It does not cover the same predicate with a different sort, or with no sort, which are separate shapes. Confirm the filter took effect with `explain`:

```
db.orders.find({ status: "SHIPPED" }).sort({ orderDate: 1 }).explain()
```

The output reports `indexFilterSet: true` and `indexFilterApplied: true`, and the `IXSCAN` stage names `status_1_orderDate_1`.

### Example: pinning an `update` to a selective index
<a name="plan-cache-filter-example-update"></a>

An update has to locate the documents to modify before it can write them, and that lookup uses an index in the same way a read does. When a predicate can be served by more than one index, the index the planner chooses determines how many documents the update examines.

```
db.orders.updateMany(
  { customerId: 4815, status: "PENDING" },
  { $set: { status: "CANCELLED" } }
)
```

Both `customerId_1` and `status_1` can serve this predicate. To pin the update to `customerId_1`:

```
db.runCommand({planCacheSetFilter: "orders",
query: { customerId: 4815, status: "PENDING" },
indexes: [ "customerId_1" ]})
```

Filters on write commands require Amazon DocumentDB 5.0.2 or 8.0.2 and planner version 2.0 or later. Verify with an `explain` of the update:

```
db.runCommand({explain: {update: "orders",
updates: [{ q: { customerId: 4815, status: "PENDING" },
             u: { $set: { status: "CANCELLED" } },
             multi: true }]}})
```

The winning plan is an `UPDATE` stage over an `IXSCAN` on `customerId_1`. The same filter applies to `delete` and `findAndModify` commands that use this query shape, because the shape does not include the type of write.

### Example: pinning an `aggregate` pipeline and a `$lookup` foreign collection
<a name="plan-cache-filter-example-aggregate"></a>

For an aggregation, the shape is taken from the leading `$match` stage and a `$sort` immediately after it. Stages beyond that, such as `$group` or `$project`, are not part of the shape.

```
db.orders.aggregate([
  { $match: { status: "SHIPPED" } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } }
])
```

A filter set on the `$match` predicate drives the index used to read `orders`:

```
db.runCommand({planCacheSetFilter: "orders",
query: { status: "SHIPPED" },
indexes: [ "status_1" ]})
```

Filters also apply to the collection that a `$lookup` or `$graphLookup` stage joins to. The filter is set on the foreign collection, not on the collection the pipeline runs against. In the following pipeline, `orders` is the outer collection and `customers` is the foreign collection:

```
db.orders.aggregate([
  { $lookup: { from: "customers",
               localField: "customerId",
               foreignField: "customerId",
               as: "customer" } }
])
```

The join probes `customers` once per outer document, so the index chosen there is applied repeatedly and its cost is multiplied across the pipeline. To pin that scan to a specific index, set the filter on `customers` for the join key's equality shape:

```
db.runCommand({planCacheSetFilter: "customers",
query: { customerId: 1 },
indexes: [ "customerId_1" ]})
```

Because values are normalized out of the shape, the value `1` above is a placeholder and any value produces the same filter. When a foreign-collection filter is applied, the top-level `indexFilterSet` and `indexFilterApplied` fields report `true`, and the index that the filter selected appears on the foreign side of the winning plan. Filters on `aggregate` require Amazon DocumentDB 8.0.2 and planner version 3.0.

## Behavior with hints and index changes
<a name="plan-cache-filter-behavior"></a>
+ A plan cache filter takes precedence over a `hint`. Amazon DocumentDB applies the filter first and then applies the hint within the filter's allowed index list. If the hint names an index that the filter permits, that index is used. If the hint names an index that the filter does not permit, the hint is ignored and the planner chooses among the permitted indexes on cost. Both hint forms behave the same way, whether you name the index or give its key pattern.

  For example, if the collection `foo` has the indexes `a_1`, `b_1`, and `a_1_b_1`, and you set a filter on the shape `{query: {a: {$eq: "@"}, b: {$eq: "@"}}, sort: {a: 1}}` with the index list `["a_1", "a_1_b_1"]`, then running `db.foo.find({ a: 10, b: 20 }).sort({a: 1}).hint({ a: 1 })` uses `a_1`, because it is named in the hint and permitted by the filter.
+ Dropping an index does not modify filters. The filter keeps the index name. While that index is missing, planning skips it. If another index in the filter's list can serve the query, the filter still applies. Only when none of the named indexes are available does `indexFilterApplied` report `false`. Recreating an index with the same name makes it eligible again.
+ Dropping a collection removes all of that collection's filters.