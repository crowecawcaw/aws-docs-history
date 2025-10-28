# Gremlin query hints for using the results cache

The following query hints can be used when the [query
results cache](gremlin-results-cache.md "gremlin-results-cache.md") is enabled.

## Gremlin `enableResultCache` query hint

The `enableResultCache` query hint with a value of `true`
causes query results to be returned from the cache if they have already been cached.
If not, it returns new results and caches them until such time as they are cleared
from the cache. For example:

```
g.with('Neptune#enableResultCache', true)
 .V().has('genre','drama').in('likes')
```

Later, you can access the cached results by issuing exactly the same query again.

If the value of this query hint is `false`, or if it isn't present, query
results are not cached. However, setting it to `false` does not clear
existing cached results. To clear cached results, use the `invalidateResultCache`
or `invalidateResultCachekey` hint.

## Gremlin `enableResultCacheWithTTL` query hint

The `enableResultCacheWithTTL` query hint also returns cached results
if there are any, without affecting the TTL of results already in the cache. If there
are currently no cached results, the query returns new results and caches them for the
time to live (TTL) specified by the `enableResultCacheWithTTL` query hint.
That time to live is specified in seconds. For example, the following query specifies
a time to live of sixty seconds:

```
g.with('Neptune#enableResultCacheWithTTL', 60)
 .V().has('genre','drama').in('likes')
```

Before the 60-second time-to-live is over, you can use the same query (here,
`g.V().has('genre','drama').in('likes')`) with either the `enableResultCache`
or the `enableResultCacheWithTTL` query hint to access the cached results.

###### Note

The time to live specified with `enableResultCacheWithTTL` does not
affect results that have already been cached.

- If results were previously cached using `enableResultCache`,
  the cache must first be explicitly cleared before `enableResultCacheWithTTL`
  generates new results and caches them for the TTL that it specifies.
- If results were previously cached using `enableResultCachewithTTL`,
  that previous TTL must first expire before `enableResultCacheWithTTL` generates
  new results and caches them for the TTL that it specifies.

After the time to live has passed, the cached results for the query are cleared, and
a subsequent instance of the same query then returns new results. If `enableResultCacheWithTTL`
is attached to that subsequent query, the new results are cached with the TTL that it
specifies.

## Gremlin `invalidateResultCacheKey` query hint

The `invalidateResultCacheKey` query hint can take a `true` or
`false` value. A `true` value causes cached results for the
the query to which `invalidateResultCacheKey` is attached to be cleared.
For example, the following example causes results cached for the query key
`g.V().has('genre','drama').in('likes')` to be cleared:

```
g.with('Neptune#invalidateResultCacheKey', true)
 .V().has('genre','drama').in('likes')
```

The example query above does not cause its new results to be cached.
You can include `enableResultCache` (or
`enableResultCacheWithTTL`) in the same query if you want to cache
the new results after clearing the existing cached ones:

```
g.with('Neptune#enableResultCache', true)
 .with('Neptune#invalidateResultCacheKey', true)
 .V().has('genre','drama').in('likes')
```

## Gremlin `invalidateResultCache` query hint

The `invalidateResultCache` query hint can take a `true` or
`false` value. A `true` value causes all results in the results
cache to be cleared. For example:

```
g.with('Neptune#invalidateResultCache', true)
 .V().has('genre','drama').in('likes')
```

The example query above does not cause its results to be cached.
You can include `enableResultCache` (or
`enableResultCacheWithTTL`) in the same query if you want to cache
new results after completely clearing the existing cache:

```
g.with('Neptune#enableResultCache', true)
 .with('Neptune#invalidateResultCache', true)
 .V().has('genre','drama').in('likes')
```

## Gremlin `numResultsCached` query hint

The `numResultsCached` query hint can only be used with queries that
contain `iterate()`, and it specifies the maximum number of
results to cache for the query to which it is attached. Note that the results cached
when `numResultsCached` is present are not returned, only cached.

For example, the following query specifies that up to 100 of its results should
be cached, but none of those cached results returned:

```
g.with('Neptune#enableResultCache', true)
 .with('Neptune#numResultsCached', 100)
 .V().has('genre','drama').in('likes').iterate()
```

You can then use a query like the following to retrieve a range of the cached
results (here, the first ten):

```
g.with('Neptune#enableResultCache', true)
 .with('Neptune#numResultsCached', 100)
 .V().has('genre','drama').in('likes').range(0, 10)
```

## Gremlin `noCacheExceptions` query hint

The `noCacheExceptions` query hint can take a `true` or
`false` value. A `true` value causes any exceptions related
to the results cache to be suppressed. For example:

```
g.with('Neptune#enableResultCache', true)
 .with('Neptune#noCacheExceptions', true)
 .V().has('genre','drama').in('likes')
```

In particular, this suppresses the `QueryLimitExceededException`,
which is raised if the results of a query are too large to fit in the results
cache.
