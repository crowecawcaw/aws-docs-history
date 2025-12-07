# Spark Result Fragment

Caching

Amazon EMR 6.6.0 and higher include the optional Spark Result Fragment Caching feature that
automatically caches result fragments. These result fragments are parts of results from
subtrees of queries that are stored in an Amazon S3 bucket of your choosing. The stored query
result fragments are reused on subsequent query executions, resulting in faster
queries.

Result Fragment Caching analyzes your Spark queries, and caches eligible result
fragments in your specified S3 location. On subsequent query runs, the usable query
result fragments are automatically detected and fetched from S3. Result Fragment Caching
differs from Result Set Caching, where subsequent queries have to exactly match the
original query to return results from the cache. When used for queries that repeatedly
target a static subset of your data, result fragment caching speeds performance
significantly.

Consider the following query, which counts orders until the year 2022:

```
select
    l_returnflag,
    l_linestatus,
    count(*) as count_order
from
    lineitem
where
    l_shipdate <= current_date
    and year(l_shipdate) == '2022'
group by
    l_returnflag,
    l_linestatus
```

As time progresses, this query needs to run every day to report the total sales for
the year. Without Result Fragment Caching, the results for all days of the year will
need to be recomputed every day. The query will get slower over time and will be slowest
at the end of the year, when all 365 days of results will need to be recomputed.

When you activate Result Fragment Caching, you use results for the all previous days
of the year from the cache. Each day, the feature must recompute only one day of
results. After the feature computes the result fragment, the feature caches the
fragment. As a result, cache-enabled query times are fast and they remain constant for
each subsequent query.

## Enabling Spark Result Fragment

Caching

To enable Spark Result Fragment Caching, perform the following steps:

1. Create a cache bucket in Amazon S3 and authorize read/write access for EMRFS.
   For more information, see [Authorizing access to EMRFS data in Amazon S3](emr-plan-credentialsprovider.md "emr-plan-credentialsprovider.md").
2. Set Amazon EMR Spark config to enable the feature.

```
spark.subResultCache.enabled = true
spark.subResultCache.fs.root.path = s3://&example-s3-bucket;/cache_dir/
```

3. Enable S3 lifecycle management for the bucket to automatically clean cache
   files.
4. Optionally, configure the reductionRationThreshold and maxBufferSize
   properties to further tune the feature.

```
spark.sql.subResultCache.reductionRatioThreshold
spark.sql.subResultCache.maxBufferSize
```

## Considerations when using Result

Fragment Caching

The cost savings when you use results already cached in Amazon S3 rather than recompute
them grows with the number of times the same cached results can be used. Queries
with large table scans followed by filters or hash aggregations that reduce the
result size by factor of at least 8 (that is, a ratio of at least 8:1 in input
size:results) will benefit most from this feature. The greater the reduction ratio
between the input and the results, the greater is the cost benefit. Queries with
smaller reduction ratios, but that contain expensive computation steps between the
table scan and filter or aggregations will also benefit, as long as the cost to
produce the results is greater than the cost to fetch them from Amazon S3. By default,
Result Fragment Caching takes effect only when it detects that a reduction ratio
will be at least 8:1.

When your queries repeatedly reuse cached results, the benefits of this feature
are greatest. Rolling and incremental window queries are good examples. For
instance, a 30-day rolling window query that has already run for 29 days, would only
need to pull 1/30th of the target data from its original input source and would use
cached result fragments for the 29 previous days. An incremental window query would
benefit even more, since the start of the window remains fixed: on every invocation
of the query, a smaller percentage of the processing will require reading from the
input source.

The following are additional considerations when using Result Fragment
Caching:

- Queries that don't target the same data with the same query fragments will
  have a low cache hit rate, hence will not benefit from this feature.
- Queries with low reduction ratios that do not contain expensive
  computation steps will result in cached results that are roughly as
  expensive to read as they were to initially process.
- The first query will always demonstrate a minor regression due to the cost
  of writing to cache.
- The Result Fragment Caching feature works exclusively with Parquet files.
  Other file formats are not supported.
- The Result Fragment Caching feature buffers will only attempt to cache
  scans with file split sizes of 128 MB or larger. With the default Spark
  configuration, Result Fragment Caching will be disabled if the scan size
  (total size across all files being scanned) divided by the number of
  executor cores is less than 128 MB. When any of the Spark configurations
  listed below are set, the file split size will be:

```
min(maxPartitionBytes, max(openCostInBytes, scan size / minPartitionNum))
```

    + spark.sql.leafNodeDefaultParallelism (default value is
     spark.default.parallelism)
    + spark.sql.files.minPartitionNum (default value is
     spark.sql.leafNodeDefaultParallelism)
    + spark.sql.files.openCostInBytes
    + spark.sql.files.maxPartitionBytes

- The Result Fragment Caching feature caches at the RDD partition
  granularity. The previously described reduction ratio that defaults to 8:1
  is assessed per RDD partition. Workloads with per-RDD reduction ratios both
  greater and less than 8:1 may see smaller performance benefits than
  workloads with per-RDD reduction ratios that are consistently less than
  8:1.
- The Result Fragment Caching feature uses a 16MB write buffer by default
  for each RDD partition being cached.If more than 16mb will be cached per RDD
  partition, the cost of determining that a write is not possible may result
  in a performance regression.
- While, by default, Result Fragment Caching will not attempt to cache RDD
  partition results with a reduction ratio smaller than 8:1 and will cap its
  write buffer at 16MB, both of these values are tunable through the following
  configurations:

```
spark.sql.subResultCache.reductionRatioThreshold (default: 8.0)
spark.sql.subResultCache.maxBufferSize (default: 16MB, max: 64MB)
```

- Multiple clusters using the same Amazon EMR release can share the same cache
  location. To ensure result correctness, Result Fragment Caching will not use
  cache results written by different releases of Amazon EMR .
- Result Fragment Caching will be disabled automatically for Spark Streaming
  use cases or when RecordServer, Apache Ranger, or AWS Lake Formation is used.
- The result fragment cache read/writes use EMRFS / S3A and Amazon S3 buckets.
  CSE (only with EMRFS)/ SSE S3/ SSE KMS encryption are supported. For
  context, S3A provides a Hadoop implementation to enable a cluster to read
  and write data to and from Amazon S3. Note that support for S3A is available with
  EMR-7.4.0 and higher.
