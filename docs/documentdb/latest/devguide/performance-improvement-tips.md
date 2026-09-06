

# Performance improvement tips
<a name="performance-improvement-tips"></a>

This section provides five performance optimization strategies for Amazon DocumentDB to improve application efficiency and query execution.

## 1. Use $match as First Stage in Aggregation Pipelines
<a name="tip-match-first-stage"></a>

Always place $match as the first stage for filtering in your aggregation pipeline to maximize performance. Amazon DocumentDB will utilize indexes effectively when $match leads the pipeline, allowing the database to filter data early and reduce processing overhead.

```
// Optimized approach
db.orders.aggregate([
  { $match: { status: "active", category: "electronics" } }, // Index utilization
  { $group: { _id: "$category", total: { $sum: "$price" } } },
  { $sort: { total: -1 } }
])
```

**Impact:** Early filtering reduces the number of documents processed in subsequent pipeline stages, resulting in faster query execution and lower resource consumption.

## 2. Use $project in Aggregation Pipeline to Minimize Pipeline Data Size
<a name="tip-project-minimize-data"></a>

Carry only essential fields through your aggregation pipeline stages to minimize data size and improve performance. Use $project strategically to include just the data you need.

```
// Efficient pipeline design
db.orders.aggregate([
  { $match: { orderDate: { $gte: new Date("2024-01-01") } } },
  { $project: { customerId: 1, totalAmount: 1, status: 1 } }, // Only needed fields
  { $group: { _id: "$customerId", totalSpent: { $sum: "$totalAmount" } } }
])
```

**Impact:** Smaller documents reduce memory usage and improve pipeline processing efficiency, resulting in enhanced overall query performance.

## 3. Enable Document Compression for Lower Storage Costs, I/O Costs, and Improved Query Performance
<a name="tip-document-compression"></a>

Enable document compression from cluster parameter group to lower storage costs, I/O costs, and boost query performance. Amazon DocumentDB stores compressed documents on disk as well as in RAM, reducing memory footprint and I/O costs.

**Impact:**
+ More documents fit in available memory
+ Faster data access with reduced disk reads
+ Lower storage costs, I/O costs, and improved query performance

**Note**  
Amazon DocumentDB doesn't enable compression by default for version 5.0. You can [enable compression](doc-compression.md) at collection or cluster level for 5.0 cluster. Use Amazon DocumentDB's compression review utility to analyze compression ratios for your collections.  
For Amazon DocumentDB 8.0, [compression is enabled by default](dict-compression.md).

## 4. Leverage Indexes for Optimal Query Performance
<a name="tip-leverage-indexes"></a>

Ensure your queries always utilize indexes for optimal performance. Amazon DocumentDB offers multiple index types to match different use cases.

**Indexing principles:**
+ Every query should leverage an appropriate index
+ Amazon DocumentDB provides multiple [index types](index-types.md)
+ Compound indexes offer the most flexibility by supporting various query shapes with a single index
+ Design indexes to support sorting and filtering operations together

**Understanding Index Prefixes:** Compound indexes work through index prefixes - Amazon DocumentDB can use any left-to-right subset of the index fields. For example, the index `{ category: 1, price: -1, inStock: 1 }` creates these usable prefixes:
+ `{ category: 1 }` - supports queries filtering by category only
+ `{ category: 1, price: -1 }` - supports queries filtering by category and sorting/filtering by price
+ `{ category: 1, price: -1, inStock: 1 }` - supports the full compound query

Queries on price, inStock, or inStock alone will not use this index since they don't start with the first field (category).

**How to Identify Queries Not Using Indexes:** Use the explain() method to analyze query execution and identify queries performing collection scans instead of using indexes.

**Impact:** Queries without index utilization result in collection scans, causing increased memory and CPU pressure on the instance and elevated query latency.

## 5. Optimize Data Models Based on Query Patterns
<a name="tip-optimize-data-models"></a>

Align your data model with how your application queries and updates data. Data modeling is the foundation of high-performance Amazon DocumentDB applications.

**Optimization strategies:**

**Embedding for Performance**
+ Store related data together when it's frequently accessed as a unit
+ Embed documents that are always retrieved together
+ Suitable for one-to-few relationships

```
// Embedded approach for frequently accessed data
{
  _id: ObjectId("..."),
  customerName: "John Doe",
  address: {
    street: "123 Main St",
    city: "Seattle",
    zipCode: "98101"
  },
  recentOrders: [
    { orderId: "ORD001", amount: 99.99, date: "2024-01-15" }
  ]
}
```

**Referencing for Flexibility**
+ Use references for large or infrequently accessed data
+ Recommended for one-to-many relationships with large datasets
+ Prevents document bloat and improves update performance

**Collection Splitting Strategy**

When only a few fields in large documents get updated frequently, or when large infrequently accessed data bloats documents, consider splitting collections:
+ Keep frequently updated fields in a separate, smaller collection
+ Store static or infrequently accessed data in another collection
+ Link them with references when needed

```
// Before: Large document with mixed access patterns
{
  _id: ObjectId("..."),
  productId: "PROD123",
  name: "Wireless Headphones",        // Frequently accessed
  price: 99.99,                      // Frequently accessed
  inventory: 45,                     // Updated frequently
  lastSold: "2024-01-15",           // Updated frequently
  detailedSpecs: { /* large object */ }, // Infrequently accessed
  manualPDF: "base64...",           // Large, rarely accessed
  reviewHistory: [/* large array */] // Infrequently accessed
}

// After: Split into collections based on access patterns
// products collection (frequently accessed data)
{
  _id: ObjectId("..."),
  productId: "PROD123",
  name: "Wireless Headphones",
  price: 99.99,
  inventory: 45,
  lastSold: "2024-01-15"
}

// product_details collection (infrequently accessed data)
{
  _id: ObjectId("..."),
  productId: "PROD123",           // Reference to products collection
  detailedSpecs: { /* large object */ },
  manualPDF: "base64...",
  reviewHistory: [/* large array */]
}
```

**Performance gain:** Smaller documents mean faster updates, reduced memory usage, and improved cache efficiency.

**Impact:** Inefficient data modeling results in suboptimal queries, increased document sizes, and elevated memory usage, leading to degraded application performance and higher operational costs.