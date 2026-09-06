

# Compound index with more than 3 attributes
<a name="anti-pattern-compound-index"></a>

## Overview
<a name="compound-index-overview"></a>

A compound or composite index maintains references to multiple fields within a single index structure. These indexes optimize performance for queries that filter on multiple fields simultaneously or combine filtering with sorting operations. They're also effective for single-condition queries on the leftmost indexed fields. The database leverages these index entries to efficiently locate matching documents without performing full collection scans.

Amazon DocumentDB can use compound index to support queries that include any leading subset of the indexed fields, a concept known as Index Prefixes. For example, if you have a compound index on `{state: 1, city: 1, zipcode: 1}`, Amazon DocumentDB can efficiently process queries that use field 'state' alone, fields 'state' and 'city' together, or all three fields 'state', 'city', and 'zipcode'. However, queries must use the fields from left to right without skipping any fields in between. This means queries using only field 'city' or 'zipcode', or combinations like 'state' and 'zipcode' (skipping 'city'), cannot fully utilize the index.

In most real-world scenarios, compound indexes with three or fewer attributes typically achieve optimal performance and resource efficiency. While it's feasible to have more than 3 attributes in the composite index, it often leads to increased resource consumption, outweighing the benefits.

## Impact on the cluster
<a name="compound-index-impact"></a>

While it is tempting to create an index covering all the conditions in a query to achieve maximum theoretical performance, most data filtering occurs through the first 1-3 attributes in a composite index. Additional fields beyond this threshold contribute primarily to index size rather than meaningful query optimization.

**Storage and I/O Overhead**: Composite indexes with many attributes consume significantly more storage space than simpler alternatives. The size is directly proportional to the number of indexed attributes, and the size of the indexed values themselves.

**Memory footprint**: The large storage footprint of composite indexes with many attributes creates a corresponding footprint in memory, making your working set larger and displacing other frequently accessed data from the buffer pool.

**Write Operations**: Each document modification affecting multiple indexed fields requires updating the entire composite index entry, multiplying the work required to complete the write operation.

## How to identify
<a name="compound-index-identify"></a>

Start by reviewing all indexes in your collection to identify composite indexes with more than three attributes:

```
// List all indexes for the collection
db.collection.getIndexes()

// Look for indexes with 3+ fields like:

// { "userId": 1, "status": 1, "category": 1, "priority": 1, "region": 1 }
// { "orderId": 1, "customerId": 1, "productId": 1, "timestamp": 1, "warehouse": 1 }
```

## Remediation
<a name="compound-index-remediation"></a>

If a composite index with more than three attributes is being used, identify the queries that utilize it and look for optimization opportunities. Consider replacing these indexes with more efficient ones containing three or fewer attributes. After implementing the new indexes, remove the old indexes that contain more than three attributes.

**Note**  
Always coordinate with stakeholders and validate performance impact before dropping any indexes.

Follow the Equality, Sort, Range (ESR) rule when creating composite indexes.

**Equality Sort Range (ESR) Rule**: This ordering maximizes index efficiency by filtering the dataset first with equality conditions, then applying sort operations on the reduced set, and finally performing range scans on the smallest possible subset
+ order fields as Equality (exact matches),
+ Sort (ordering),
+ Range (>, <, $in).

```
// Query pattern
db.orders.find({ 
  userId: "user123",                    // Equality
  price: { $gte: 50, $lte: 200 }      // Range
}).sort({ createdAt: -1 })             // Sort

// Optimal index following ESR rule
db.orders.createIndex({ userId: 1, createdAt: -1, price: 1 })
//                      Equality   Sort         Range
```