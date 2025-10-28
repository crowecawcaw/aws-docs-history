# Caching query results in Amazon Neptune Gremlin

Starting in [engine release 1.0.5.1](engine-releases-1.0.5.md "engine-releases-1.0.5.md"),
Amazon Neptune supports a results cache for Gremlin queries.

You can enable the query results cache and then use a query hint
to cache the results of a Gremlin read-only query.

Any re-run of the query then retrieves the cached results with low latency and no
I/O costs, as long as they are still in the cache. This works for queries submitted
both on an HTTP endpoint and using Websockets, either as byte-code or in string form.

###### Note

Queries sent to the profile endpoint are not cached even when the query
cache is enabled.

You can control how the Neptune query results cache behaves in several ways.
For example:

- You can get cached results paginated, in blocks.
- You can specify the time-to-live (TTL) for specified queries.
- You can clear the cache for specified queries.
- You can clear the entire cache.
- You can set up to be notified if results exceed the cache size.
  The cache is maintained using a least-recently-used (LRU) policy, meaning that once the
  space allotted to the cache is full, the least-recently-used results are removed to make
  room when new results are being cached.

###### Important

The query-results cache is not available on `t3.medium` or
`t4.medium` instance types.

## Enabling the query results cache in Neptune

The query results cache can be enabled across all instances in a cluster or per-instance. To enable the results cache
on all instances in a cluster, set the `neptune_result_cache` parameter in the cluster's
`cluster-parameter-group` to `1`. To enable this on a specific instance, set the
`neptune_result_cache` parameter in the instance's `instance-parameter-group` to `1`.
The cluster parameter group setting will override the instance parameter group value.

A restart is required on any affected instances for the results cache parameter settings to be applied. While you can
enable the results cache across all instances in a cluster via the `cluster-parameter-group`, each instance
maintains its own cache. The query results cache feature is not a cluster-wide cache.

Once the results cache is enabled, Neptune sets aside a portion of current
memory for caching query results. The larger the instance type you're using and the
more memory is available, the more memory Neptune sets aside for the cache.

If the results cache memory fills up, Neptune automatically drops
least-recently-used (LRU) cached results to make way for new ones.

You can check the current status of the results cache using the [Instance Status](access-graph-status.md "access-graph-status.md") command.

## Using hints to cache query results

Once the query results cache is enabled, you use query hints to control query
caching. All the examples below apply to the same query traversal, namely:

```
g.V().has('genre','drama').in('likes')
```

### Using `enableResultCache`

With the query results cache enabled, you can cache the results of a Gremlin
query using the `enableResultCache` query hint, as follows:

```
g.with('Neptune#enableResultCache', true)
 .V().has('genre','drama').in('likes')
```

Neptune then returns the query results to you, and also caches them.
Later, you can access the cached results by issuing exactly the same query again:

```
g.with('Neptune#enableResultCache', true)
 .V().has('genre','drama').in('likes')
```

The cache key that identifies the cached results is the query string itself,
namely:

```
g.V().has('genre','drama').in('likes')
```

### Using `enableResultCacheWithTTL`

You can specify how long the query results should be cached for by using the
`enableResultCacheWithTTL` query hint. For example, the following query
specifies that the query results should expire after 120 seconds:

```
g.with('Neptune#enableResultCacheWithTTL', 120)
 .V().has('genre','drama').in('likes')
```

Again, the cache key that identifies the cached results is the base query string:

```
g.V().has('genre','drama').in('likes')
```

And again, you can access the cached results using that query string with the
`enableResultCache` query hint:

```
g.with('Neptune#enableResultCache', true)
 .V().has('genre','drama').in('likes')
```

If 120 or more seconds have passed since the results were cached, that
query will return new results, and cache them, without any time-to-live.

You can also access the cached results by issuing the same query again with
the `enableResultCacheWithTTL` query hint. For example:

```
g.with('Neptune#enableResultCacheWithTTL', 140)
 .V().has('genre','drama').in('likes')
```

Until 120 seconds have passed (that is, the TTL currently in effect),
this new query using the `enableResultCacheWithTTL` query hint
returns the cached results. After 120 seconds, it would return new results
and cache them with a time-to-live of 140 seconds.

###### Note

If results for a query key are already cached, then the same query key with
`enableResultCacheWithTTL` does not generate new results and has no
effect on the time-to-live of the currently cached results.

- If results were previously cached using `enableResultCache`,
  the cache must first be cleared before `enableResultCacheWithTTL` generates
  new results and caches them for the TTL that it specifies.
- If results were previously cached using `enableResultCachewithTTL`,
  that previous TTL must first expire before `enableResultCacheWithTTL` generates
  new results and caches them for the TTL that it specifies.

### Using `invalidateResultCacheKey`

You can use the `invalidateResultCacheKey` query hint to clear
cached results for one particular query. For example:

```
g.with('Neptune#invalidateResultCacheKey', true)
 .V().has('genre','drama').in('likes')
```

That query clears the cache for the query key, `g.V().has('genre','drama').in('likes')`,
and returns new results for that query.

You can also combine `invalidateResultCacheKey` with
`enableResultCache` or `enableResultCacheWithTTL`.
For example, the following query clears the current cached results,
caches new results, and returns them:

```
g.with('Neptune#enableResultCache', true)
 .with('Neptune#invalidateResultCacheKey', true)
 .V().has('genre','drama').in('likes')
```

### Using `invalidateResultCache`

You can use the `invalidateResultCache` query hint to clear
all cached results in the query result cache. For example:

```
g.with('Neptune#invalidateResultCache', true)
 .V().has('genre','drama').in('likes')
```

That query clears the entire result cache and returns new results for
the query.

You can also combine `invalidateResultCache` with
`enableResultCache` or `enableResultCacheWithTTL`.
For example, the following query clears the entire results cache,
caches new results for this query, and returns them:

```
g.with('Neptune#enableResultCache', true)
 .with('Neptune#invalidateResultCache', true)
 .V().has('genre','drama').in('likes')
```

## Paginating cached query results

Suppose you have already cached a large number of results like this:

```
g.with('Neptune#enableResultCache', true)
 .V().has('genre','drama').in('likes')
```

Now suppose you issue the following range query:

```
g.with('Neptune#enableResultCache', true)
 .V().has('genre','drama').in('likes').range(0,10)
```

Neptune first looks for the full cache key, namely
`g.V().has('genre','drama').in('likes').range(0,10)`.
If that key doesn't exist, Neptune next looks to see if there is a key for that
query string without the range (namely `g.V().has('genre','drama').in('likes')`).
When it finds that key, Neptune then fetches the first ten results from its cache,
as the range specifies.

###### Note

If you use the `invalidateResultCacheKey` query hint
with a query that has a range at the end, Neptune clears the cache for
a query without the range if it doesn't find an exact match for the query
with the range.

### Using `numResultsCached` with `.iterate()`

Using the `numResultsCached` query hint, you can populate
the results cache without returning all the results being cached, which can
be useful when you prefer to paginate a large number of results.

The `numResultsCached` query hint only works with queries
that end with `iterate()`.

For example, if you want to cache the first 50 results of the sample query:

```
g.with("Neptune#enableResultCache", true)
 .with("Neptune#numResultsCached", 50)
 .V().has('genre','drama').in('likes').iterate()
```

In this case the query key in the cache is:
`g.with("Neptune#numResultsCached", 50).V().has('genre','drama').in('likes')`.
You can now retrieve the first ten of the cached results with this query:

```
g.with("Neptune#enableResultCache", true)
 .with("Neptune#numResultsCached", 50)
 .V().has('genre','drama').in('likes').range(0, 10)
```

And, you can retrieve the next ten results from the query as follows:

```
g.with("Neptune#enableResultCache", true)
 .with("Neptune#numResultsCached", 50)
 .V().has('genre','drama').in('likes').range(10, 20)
```

Don't forget to include the `numResultsCached` hint! It is
an essential part of the query key and must therefore be present in order
to access the cached results.

###### Some things to keep in mind when using `numResultsCached`

- **The number you supply with `numResultsCached`
  is applied at the end of the query.**  
  This means, for example, that the following query actually caches results
  in the range `(1000, 1500)`:

```
g.with("Neptune#enableResultCache", true)
 .with("Neptune#numResultsCached", 500)
 .V().range(1000, 2000).iterate()
```

- **The number you supply with `numResultsCached`
  specifies the maximum number of results to cache.**  
  This means, for example, that the following query actually caches results
  in the range `(1000, 2000)`:

```
g.with("Neptune#enableResultCache", true)
 .with("Neptune#numResultsCached", 100000)
 .V().range(1000, 2000).iterate()
```

- **Results cached by queries that end with
  `.range().iterate()` have their own range.**  
  For example, suppose you cache results using a query like this:

```
g.with("Neptune#enableResultCache", true)
 .with("Neptune#numResultsCached", 500)
 .V().range(1000, 2000).iterate()
```

To retrieve the first 100 results from the cache, you would
write a query like this:

```
g.with("Neptune#enableResultCache", true)
 .with("Neptune#numResultsCached", 500)
 .V().range(1000, 2000).range(0, 100)
```

Those hundred results would be equivalent to results from the
base query in the range `(1000, 1100)`.

## The query cache keys used to locate cached results

After the results of a query have been cached, subsequent queries with the same
_query cache key_ retrieve results from the cache rather than
generating new ones. The query cache key of a query is evaluated as follows:

1. All the cache-related query hints are ignored, except for `numResultsCached`.
2. A final `iterate()` step is ignored.
3. The rest of the query is ordered according to its byte-code representation.

The resulting string is matched against an index of the query results already
in the cache to determine whether there is a cache hit for the query.

For example, take this query:

```
g.withSideEffect('Neptune#typePromotion', false).with("Neptune#enableResultCache", true)
 .with("Neptune#numResultsCached", 50)
 .V().has('genre','drama').in('likes').iterate()
```

It will be stored as the byte-code version of this:

```
g.withSideEffect('Neptune#typePromotion', false)
 .with("Neptune#numResultsCached", 50)
 .V().has('genre','drama').in('likes')
```

## Exceptions related to the results cache

If the results of a query that you are trying to cache are too large to fit
in the cache memory even after removing everything previously cached, Neptune raises
a `QueryLimitExceededException` fault. No results are returned, and the
exception generates the following error message:

```
The result size is larger than the allocated cache,
      please refer to results cache best practices for options to rerun the query.
```

You can supress this message using the `noCacheExceptions` query
hint, as follows:

```
g.with('Neptune#enableResultCache', true)
 .with('Neptune#noCacheExceptions', true)
 .V().has('genre','drama').in('likes')
```
