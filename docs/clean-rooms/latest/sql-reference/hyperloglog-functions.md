

# Hyperloglog functions
<a name="hyperloglog-functions"></a>

The HyperLogLog (HLL) functions in SQL provide a way to efficiently estimate the number of unique elements (cardinality) in a large dataset, even when the actual set of unique elements isn't stored. 

The main benefits of using HLL functions are:
+ **Memory efficiency**: HLL sketches require much less memory than storing the full set of unique elements, making them suitable for large datasets.
+ **Distributed computing**: HLL sketches can be combined across multiple data sources or processing nodes, allowing for efficient distributed unique count estimation.
+ **Approximate results**: HLL provides an approximate unique count estimation, with a tunable trade-off between accuracy and memory usage (via the precision parameter).

These functions are particularly useful in scenarios where you need to estimate the number of unique items, such as in analytics, data warehousing, and real-time stream processing applications.

AWS Clean Rooms supports the following HLL functions.

**Topics**
+ [HLL\_SKETCH\_AGG function](HLL_SKETCH_AGG.md)
+ [HLL\_SKETCH\_ESTIMATE function](HLL_SKETCH_ESTIMATE.md)
+ [HLL\_UNION function](HLL_UNION.md)
+ [HLL\_UNION\_AGG function](HLL_UNION_AGG.md)