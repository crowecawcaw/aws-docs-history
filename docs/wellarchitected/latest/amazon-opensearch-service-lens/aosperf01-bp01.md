

# AOSPERF01-BP01 Maintain shard sizes at recommended ranges
<a name="aosperf01-bp01"></a>

 Shard size is recommended in a range of 10 GiB to 50 GiB. 

 **Level of risk exposed if this best practice is not established:** High 

 **Desired outcome:** Shards fall within the recommended size range of 10 GiB to 50 GiB, for efficient indexing, querying and relocation performance. 

 **Benefits of establishing this best practice:** 
+  Reduced CPU and memory utilization 
+  Enhanced domain stability by avoiding shard contention and node overload 

## Implementation guidance
<a name="implementation-guidance-29"></a>

 Shard sizes depend on the workload, and the distribution of shards to data nodes significantly influences a domain's performance. 
+  Verify that the ideal shard size range is between 10GB and 30GB for *search-intensive* workloads, and 30GB to 50GB for *log analytics* and *time-series* data processing. Use `GET _cat/shards` to view shard size. 
+  If your indices have excessively small shards (less than 10GB in size), consider reindexing the data with a reduced number shards for that index to potentially boost performance and reduce CPU utilization. You can reindex the data from source into a new index or use the `_reindex` API to copy data from an existing index to a new one within the same domain. 
+  Verify shard to Java heap memory ratio. Verify that you have no more than 25 shards per GiB of Java heap. 
+  Verify that you don't have more than 1,000 shards per data node. 
+  You can implement ISM policies to roll over your indices when the shards reach a certain size. 
+  Consider OpenSearch's [aliasing](https://opensearch.org/docs/latest/im-plugin/index-alias/) capability, which you can use to quickly update your indices without requiring modifications to your application. 

## Resources
<a name="resources-28"></a>
+  [Sharding strategy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp.html#bp-sharding-strategy) 
+  [Index aliases](https://opensearch.org/docs/latest/im-plugin/index-alias/) 