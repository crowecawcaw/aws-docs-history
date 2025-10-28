# Using the lookup cache

The lookup cache is only available on an `R5d` instance type, where
it is automatically enabled by default. Neptune `R5d` instances have the
same specifications as `R5` instances, plus up to 1.8 TB of local NVMe-based
SSD storage. Lookup caches are instance-specific, and workloads that benefit can be
directed specifically to `R5d` instances in a Neptune cluster, while other
workloads can be directed to `R5` or other instance types.

To use the lookup cache on a Neptune instance, simply upgrade that instance
to the `R5d` instance type. When you do, Neptune automatically
sets the [neptune_lookup_cache](parameters.md#parameters-db-cluster-parameters-neptune_lookup_cache "parameters.md#parameters-db-cluster-parameters-neptune_lookup_cache")
DB cluster parameter to `1` (enabled), and creates the lookup cache on
that particular instance. You can then use the [Instance Status](access-graph-status.md "access-graph-status.md") API to confirm that the cache has
been enabled.

Similarly, to disable the lookup cache on a given instance, scale the instance
down from an `R5d` instance type to an equivalent `R5`
instance type.

When an `R5d` instance is launched, the lookup cache is enabled and
in cold-start mode, meaning that it is empty. Neptune first checks in the lookup
cache for property values or RDF literals while processing queries, and adds them
if they are not yet present. This gradually warm up the cache.

When you direct the read queries that require property-value or RDF-literal lookups
to an R5d _reader_ instance, read performance degrades slightly
while its cache is warming up. When the cache is warmed up, however, read performance
speeds up significantly and you may also see a drop in I/O costs related to lookups
hitting the cache rather than cluster storage. Memory utilization also improves.

If your _writer_ instance is an `R5d`, it warms
up its lookup cache automatically on every write operation. This approach does increase
latency for write queries slightly, but warms up the lookup cache more efficiently.
Then if you direct the read queries that require property-value or RDF-literal lookups
to the writer instance, you start getting improved read performance immediately,
since the values have already been cached there.

Also, if you are running the bulk loader on an `R5d` writer instance,
you may notice that its performance is slightly degraded because of the cache.

Because the lookup cache is specific to each node, host replacement resets the
cache to a cold start.

You can temporarily disable the lookup cache on all instances in your DB cluster
by setting the [neptune_lookup_cache](parameters.md#parameters-db-cluster-parameters-neptune_lookup_cache "parameters.md#parameters-db-cluster-parameters-neptune_lookup_cache")
DB cluster parameter to `0` (disabled). In general, however, it makes more
sense to disable the cache on specific instances by scaling them down from
`R5d` to `R5` instance types.
