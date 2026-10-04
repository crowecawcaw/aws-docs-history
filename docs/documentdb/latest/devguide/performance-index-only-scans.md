

# Index-only scans (covered queries)
<a name="performance-index-only-scans"></a>

An **index-only scan** (also called a **covered query**) is an optimization in which Amazon DocumentDB answers a query entirely from the fields stored in an index, without reading the underlying documents. Because the values a query needs are already present in the index, Amazon DocumentDB can skip fetching each matching document, avoiding the random I/O and decoding cost of reading full documents. In the query plan, an index-only scan appears as the `IXONLYSCAN` stage instead of an `IXSCAN` (index scan) or `COLLSCAN` (collection scan). This reduces I/O and can significantly lower query latency for supported queries.

A query is a good candidate for an index-only scan when it touches only a small number of fields that all exist in a single index, especially when the documents themselves are large. Common examples are dashboards, analytics rollups, and lookups that read a few fields from a wider compound index.

The results of a query are the same whether or not an index-only scan is used. Only the query plan, and the amount of I/O it performs, change.

**Note**  
Index-only scan support depends on your Amazon DocumentDB engine version:  
Covered `find` projections that include **more than one** non-`_id` field require engine version 8.0.2 or later. In earlier versions, a covered `find` projection can include at most one non-`_id` field. A projection with two or more fields falls back to a normal index scan or collection scan.
Index-only scans for aggregation pipelines, such as a covered `$group`, require engine version 8.0.2 or later.

## When Amazon DocumentDB uses an index-only scan
<a name="index-only-scans-when"></a>

Amazon DocumentDB considers an index-only scan for the following operations when a single index contains every field the operation reads.

### Covered `find` projections
<a name="index-only-scans-find"></a>

A `find` query qualifies when its projection is a simple inclusion of one or more top-level fields and every projected field is present in a single index. For example, given a compound index on `{ customerId: 1, status: 1, total: 1 }`, the following query is covered. All three projected fields live in the index, and `_id` is explicitly excluded. (Covering a projection with more than one non-`_id` field requires engine version 8.0.2 or later.)

```
db.orders.createIndex({ customerId: 1, status: 1, total: 1 })

db.orders.find(
  { customerId: 42 },
  { _id: 0, customerId: 1, status: 1, total: 1 }
)
```

The winning plan uses an `IXONLYSCAN` stage and never fetches the matching documents from storage:

```
{
  "stage": "IXONLYSCAN",
  "indexName": "customerId_1_status_1_total_1",
  "direction": "forward",
  "indexCond": { "$and": [ { "customerId": { "$eq": 42 } } ] }
}
```

**Note**  
In a covered `find` query, the fields in the result are returned in **index order** (the order the fields appear in the index definition), not the order they were listed in the projection or the order they are stored in the document. This matches MongoDB behavior for covered queries. A query that is answered by a collection scan instead returns fields in stored-document order.

### Covered `$group` aggregations
<a name="index-only-scans-group"></a>

A `$group` stage typically reads only a few fields (the group key and the inputs to its accumulators) but is often run without a leading `$match`. Without a covering index, Amazon DocumentDB reads and decodes every full document in the collection just to feed those few fields into the grouping.

Index-only scans for aggregation pipelines, including covered `$group` stages, are available in engine version 8.0.2 and later.

When a single index contains every field the pipeline prefix reads, Amazon DocumentDB can place an index-only scan beneath the group and read those fields directly from the index. Consider a pipeline that groups orders by status and sums their totals, with a compound index on `{ status: 1, total: 1 }`:

```
db.orders.createIndex({ status: 1, total: 1 })

db.orders.aggregate([
  { $group: { _id: "$status", revenue: { $sum: "$total" } } }
])
```

The pipeline reads only `status` and `total`, both of which are in the index, so the group is fed from an `IXONLYSCAN` instead of a collection scan:

```
// Without a covering index
$group  <-  COLLSCAN     (reads and decodes every full document)

// With a covering index on { status, total }
$group  <-  IXONLYSCAN over { status, total }   (reads only the referenced fields)
```

A leading `$match`, `$sort`, `$skip`, or `$limit` before the `$group` is supported. However, every field these stages reference (for example, a `$match` filter field or a `$sort` key) must also be present in the same index for the pipeline to be covered. If any referenced field is missing from the index, Amazon DocumentDB falls back to a collection or index scan.

**Note**  
Unlike a `find` projection, a `$group` does not implicitly include the document `_id`. The `_id` in a `$group` is the group key, not the document identifier, so the index does not need to contain the document `_id` to cover the pipeline.

## Requirements for a covered query
<a name="index-only-scans-requirements"></a>

For Amazon DocumentDB to use an index-only scan, all of the following must hold:
+ **A single index contains every field the query reads.** This includes projected fields for `find`, and the group key, accumulator inputs, and any filter or sort fields for a covered `$group` pipeline. If even one field is missing from the index, the query cannot be covered.
+ **The projection is an inclusion of top-level fields** (for `find`). Exclusion projections, computed fields, and projection operators such as `$slice` and `$elemMatch` are not eligible.
+ **The `_id` field is accounted for** (for `find`). Because `_id` is included by default, a common compound index such as `{ a: 1, b: 1 }` does *not* cover `find({}, { a: 1, b: 1 })`: the implicit `_id` is not in the index. Either exclude `_id` from the projection (`{ _id: 0, a: 1, b: 1 }`) or add `_id` to the index.
+ **The filter is fully satisfied by the index.** If Amazon DocumentDB cannot turn part of the query predicate into an index bound, it keeps that part as a residual filter, reads the document to evaluate it, and does not convert the scan to an index-only scan. Operators such as `$mod`, `$ne`, `$nin`, and `$exists` leave a residual filter.
+ **No projected field is a multikey (array) column.** See [Restrictions](#index-only-scans-restrictions).

## Restrictions
<a name="index-only-scans-restrictions"></a>

The following cases cannot use an index-only scan and fall back to a normal index scan or collection scan. This is expected behavior and never affects the correctness of results.
+ **Multikey (array) fields.** If a field has ever held an array value in any document, its index column is multikey. A multikey index stores one entry per array element, so the original array cannot be reconstructed from the index. Any query that reads such a field is not covered.
+ **Dotted or nested paths.** A projection or field reference on a nested path such as `"address.city"` is not eligible, even if the index contains that path.
+ **Exclusion, computed, or operator projections.** Projections such as `{ b: 0 }`, `{ total: { $add: ["$price", "$tax"] } }`, or `{ a: { $slice: 5 } }` require the full document and are not covered.
+ **Whole-document references in aggregation.** A `$group` that references the entire document (for example, `{ $push: "$$ROOT" }`) cannot be covered, because no index can reconstruct the whole document.
+ **Reshaping stages before `$group`.** A stage that reshapes documents (such as `$project`, `$addFields`, `$unwind`, or `$lookup`) appearing before the `$group` disqualifies the pipeline from being covered.
+ **Collation mismatch on string predicates.** If the query's collation differs from the index's collation, string predicates cannot be served by the index and leave a residual filter, which forces a document fetch. Numeric and type-based predicates are unaffected.

## Confirming an index-only scan
<a name="index-only-scans-confirming"></a>

Use the `explain("executionStats")` output to confirm that a query is served by an index-only scan and that it is not touching documents. Look for two things:
+ The winning plan uses the `IXONLYSCAN` stage.
+ The `docsExamined` value on that stage is `0` (and `totalDocsExamined` is `0`), which means the query was answered entirely from the index without reading any documents.

```
db.orders.find(
  { customerId: 42 },
  { _id: 0, customerId: 1, status: 1, total: 1 }
).explain("executionStats").executionStats
```

```
{
    "executionSuccess": true,
    "nReturned": "2",
    "executionTimeMillis": "0.714",
    "totalDocsExamined": "0",
    "executionStages": {
        "stage": "IXONLYSCAN",
        "nReturned": "2",
        "indexName": "customerId_1_status_1_total_1",
        "direction": "forward",
        "docsExamined": "0"
    }
}
```

**Note**  
A non-zero `docsExamined` value on an `IXONLYSCAN` stage means the index contained the data, but Amazon DocumentDB still checked storage to confirm that each document version was visible. This can happen when the collection has recent writes whose obsolete document versions garbage collection has not yet reclaimed. Once garbage collection processes those documents, `docsExamined` drops to `0`. At that point, the query realizes the full benefit of the covered scan. For more information about garbage collection, see [Garbage collection in Amazon DocumentDB](garbage-collection.md). For more information about the `docsExamined` metric, see [Query plan analysis](performance-query-plan-analysis.md).

## Best practices
<a name="index-only-scans-best-practices"></a>
+ Design compound indexes that contain the fields your most frequent queries project or group on, so those queries can be covered.
+ Exclude `_id` from `find` projections (`{ _id: 0, ... }`) unless `_id` is part of the covering index.
+ Avoid indexing array (multikey) fields when you intend a query to be covered, because multikey columns disqualify the index-only path.
+ Allow garbage collection to keep up with your write workload so that covered scans skip document access and `docsExamined` stays at `0`. For more information, see [Garbage collection in Amazon DocumentDB](garbage-collection.md).