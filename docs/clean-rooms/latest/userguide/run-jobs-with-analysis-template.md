

# Running a PySpark job on a configured table using a PySpark analysis template
<a name="run-jobs-with-analysis-template"></a>

This procedure demonstrates how to use a PySpark analysis template in the AWS Clean Rooms console to analyze configured tables with the **Custom** analysis rule. 

**To run a PySpark job on a configured table using a PySpark analysis template**

Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration that has **Your member abilities** status of **Run jobs**.

1. On the **Analysis** tab, under the **Tables** section, view the tables and their associated analysis rule type (**Custom analysis rule**).
**Note**  
If you don’t see the tables that you expect in the list, it might be for the following reasons:  
The tables haven't been [associated](associate-configured-table.md).
The tables don't have an [analysis rule configured](add-analysis-rule.md).

1. Under the **Analysis** section, for **Analysis mode**, select **Run analysis templates**.

1. Choose the PySpark analysis template from the **Analysis template** dropdown list.

   The parameters from the PySpark analysis template will automatically populate in the **Definition**.

1. If the analysis template has parameters defined, under **Parameters**, provide values for the parameters:

   1. For each parameter, view the **Parameter name** and **Default value** (if configured).

   1. Enter a **Value** for each parameter you want to override.
**Note**  
If you don't provide a value but a default value exists, the default value will be used.
**Important**  
Parameter values can be up to 1,000 characters and support UTF-8 encoding. All parameter values are treated as strings and passed to your user script through the context object.  
Ensure that your user script validates and handles parameter values safely. For more information about secure parameter handling, see [Working with parameters in PySpark analysis templates](pyspark-parameter-handling.md).

1. Specify the supported **Worker type** and the **Number of workers**. 

   Use the following table to determine the type and number or workers you need for your use case.


<table>
<thead>
  <tr><th>Worker type</th><th>vCPU</th><th>Memory (GB)</th><th>Storage (GB)</th><th>Number of workers</th><th>Total Clean Rooms Processing Units (CRPU)</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2"><b>CR.1X</b> (default)</td><td rowspan="2">4</td><td rowspan="2">30</td><td rowspan="2">100</td><td>4</td><td>8</td></tr>
  <tr><td>128</td><td>256</td></tr>
  <tr><td rowspan="2"><b>CR.4X</b></td><td rowspan="2">16</td><td rowspan="2">120</td><td rowspan="2">400</td><td>4</td><td>32</td></tr>
  <tr><td>32</td><td>256</td></tr>
</tbody>
</table>

**Note**  
Different worker types and number of workers have associated costs. To learn more about the pricing, see [AWS Clean Rooms pricing](https://aws.amazon.com/clean-rooms/pricing/).

1. Specify the supported **Spark properties**.

   1. Select **Add Spark properties**.

   1. On the **Spark properties** dialog box, choose a **Property name** from the dropdown list and enter a **Value**.

   The following tables provide a definition for each property.

   For more information about Spark properties, see [Spark Properties](https://spark.apache.org/docs/latest/configuration.html#spark-properties) in the Apache Spark documentation. 
**Note**  
You can configure a maximum of 50 Spark properties. Each property value can be up to 500 characters.


<table>
<thead>
  <tr><th>Property Name</th><th>Description</th><th>Default Value</th></tr>
</thead>
<tbody>
  <tr><td>spark.task.maxFailures</td><td>Controls how many consecutive times a task can fail before the job fails. Requires a value greater than or equal to 1. The number of allowed retries equals this value minus 1. The failure count resets if any attempt succeeds. Failures across different tasks don't accumulate toward this limit.</td><td>4</td></tr>
  <tr><td>spark.sql.files.maxPartitionBytes</td><td>Sets the maximum number of bytes to pack into a single partition when reading from file-based sources such as Parquet, JSON, and ORC.</td><td>128MB</td></tr>
  <tr><td>spark.hadoop.fs.s3.maxRetries</td><td>Sets the maximum number of retry attempts for Amazon S3 file operations.</td><td>(none)</td></tr>
  <tr><td>spark.network.timeout</td><td>Sets the default timeout for all network interactions. Overrides the following timeout settings if they aren't configured:<ul><li> spark.storage.blockManagerHeartbeatTimeoutMs </li><li> spark.shuffle.io.connectionTimeout </li><li> spark.rpc.askTimeout </li><li> spark.rpc.lookupTimeout </li></ul></td><td>120s</td></tr>
  <tr><td>spark.rdd.compress</td><td>Specifies whether to compress serialized RDD partitions using spark.io.compression.codec. Applies to StorageLevel.MEMORY_ONLY_SER in Java and Scala, or StorageLevel.MEMORY_ONLY in Python. Reduces storage space but requires additional CPU processing time.</td><td>false</td></tr>
  <tr><td>spark.shuffle.spill.compress</td><td>Specifies whether to compress shuffle spill data using spark.io.compression.codec.</td><td>true</td></tr>
  <tr><td>spark.shuffle.compress</td><td>Specifies whether to compress map output files. Compression uses spark.io.compression.codec.</td><td>true</td></tr>
  <tr><td>spark.shuffle.service.index.cache.size</td><td>Sets the cache size limit, in bytes unless otherwise specified.</td><td>100m</td></tr>
  <tr><td>spark.shuffle.io.maxRetries</td><td>Sets the maximum number of retries for fetches that fail due to IO-related exceptions.</td><td>3</td></tr>
  <tr><td>spark.shuffle.io.retryWait</td><td>Sets the wait time between retries of fetches. The maximum delay caused by retrying is 15 seconds by default, calculated as maxRetries * retryWait.</td><td>5s</td></tr>
  <tr><td>spark.shuffle.io.connectionTimeout</td><td>Sets the timeout for established connections between shuffle servers and clients to be marked as idle and closed if there are still outstanding fetch requests but no traffic on the channel.</td><td>(value of spark.network.timeout)</td></tr>
  <tr><td>spark.driver.maxResultSize</td><td>Sets the total size limit of serialized results of all partitions for each Spark action, in bytes. Should be at least 1M, or 0 for unlimited.</td><td>1g</td></tr>
  <tr><td>spark.memory.fraction</td><td>Sets the fraction of (heap space - 300MB) used for execution and storage. The lower this value, the more frequently spills and cached data eviction occur. Leaving this at the default value is recommended.</td><td>0.6</td></tr>
  <tr><td>spark.scheduler.mode</td><td>Sets the scheduling mode between jobs submitted to the same SparkContext. Can be set to FAIR to use fair sharing instead of queueing jobs one after another. Supported values: FAIR, FIFO.</td><td>FIFO</td></tr>
  <tr><td>spark.sql.adaptive.advisoryPartitionSizeInBytes</td><td>Sets the target size in bytes for shuffle partitions during adaptive optimization when spark.sql.adaptive.enabled is true. Controls partition size when coalescing small partitions or splitting skewed partitions.</td><td>(value of spark.sql.adaptive.shuffle.targetPostShuffleInputSize)</td></tr>
  <tr><td>spark.sql.adaptive.autoBroadcastJoinThreshold</td><td>Sets the maximum table size in bytes for broadcasting to worker nodes during joins. Applies only in adaptive framework. Uses the same default value as spark.sql.autoBroadcastJoinThreshold. Set to -1 to disable broadcasting.</td><td>(none)</td></tr>
  <tr><td>spark.sql.adaptive.coalescePartitions.enabled</td><td>Specifies whether to coalesce contiguous shuffle partitions based on spark.sql.adaptive.advisoryPartitionSizeInBytes to optimize task size. Requires spark.sql.adaptive.enabled to be true.</td><td>true</td></tr>
  <tr><td>spark.sql.adaptive.coalescePartitions.initialPartitionNum</td><td>Defines the initial number of shuffle partitions before coalescing. Requires both spark.sql.adaptive.enabled and spark.sql.adaptive.coalescePartitions.enabled to be true. Defaults to the value of spark.sql.shuffle.partitions.</td><td>(none)</td></tr>
  <tr><td>spark.sql.adaptive.coalescePartitions.minPartitionSize</td><td>Sets the minimum size for coalesced shuffle partitions to prevent partitions from becoming too small during adaptive optimization.</td><td>1 MB</td></tr>
  <tr><td>spark.sql.adaptive.coalescePartitions.parallelismFirst</td><td>Specifies whether to calculate partition sizes based on cluster parallelism instead of spark.sql.adaptive.advisoryPartitionSizeInBytes during partition coalescing. Generates smaller partition sizes than the configured target size to maximize parallelism. We recommend setting this to false on busy clusters to improve resource utilization by preventing excessive small tasks.</td><td>true</td></tr>
  <tr><td>spark.sql.adaptive.enabled</td><td>Specifies whether to enable adaptive query execution to re-optimize query plans during query execution, based on accurate runtime statistics.</td><td>true</td></tr>
  <tr><td>spark.sql.adaptive.forceOptimizeSkewedJoin</td><td>Specifies whether to force enable OptimizeSkewedJoin even if it introduces extra shuffle.</td><td>false</td></tr>
  <tr><td>spark.sql.adaptive.localShuffleReader.enabled</td><td>Specifies whether to use local shuffle readers when shuffle partitioning isn't required, such as after converting from sort-merge joins to broadcast-hash joins. Requires spark.sql.adaptive.enabled to be true.</td><td>true</td></tr>
  <tr><td>spark.sql.adaptive.maxShuffledHashJoinLocalMapThreshold</td><td>Sets the maximum partition size in bytes for building local hash maps. Prioritizes shuffled hash joins over sort-merge joins when:<ul><li> This value equals or exceeds spark.sql.adaptive.advisoryPartitionSizeInBytes </li><li> All partition sizes are within this limit </li></ul><br />Overrides spark.sql.join.preferSortMergeJoin setting.</td><td>0 bytes</td></tr>
  <tr><td>spark.sql.adaptive.optimizeSkewsInRebalancePartitions.enabled</td><td>Specifies whether to optimize skewed shuffle partitions by splitting them into smaller partitions based on spark.sql.adaptive.advisoryPartitionSizeInBytes. Requires spark.sql.adaptive.enabled to be true.</td><td>true</td></tr>
  <tr><td>spark.sql.adaptive.rebalancePartitionsSmallPartitionFactor</td><td>Defines the size threshold factor for merging partitions during splitting. Partitions smaller than this factor multiplied by spark.sql.adaptive.advisoryPartitionSizeInBytes are merged.</td><td>0.2</td></tr>
  <tr><td>spark.sql.adaptive.skewJoin.enabled</td><td>Specifies whether to handle data skew in shuffled joins by splitting and optionally replicating skewed partitions. Applies to sort-merge and shuffled hash joins. Requires spark.sql.adaptive.enabled to be true.</td><td>true</td></tr>
  <tr><td>spark.sql.adaptive.skewJoin.skewedPartitionFactor</td><td>Determines the size factor that determines partition skew. A partition is skewed when its size exceeds both:<ul><li> This factor multiplied by the median partition size </li><li> The value of spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes </li></ul></td><td>5</td></tr>
  <tr><td>spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes</td><td>Sets the size threshold in bytes for identifying skewed partitions. A partition is skewed when its size exceeds both:<ul><li> This threshold </li><li> The median partition size multiplied by spark.sql.adaptive.skewJoin.skewedPartitionFactor </li></ul><br />We recommend setting this value larger than spark.sql.adaptive.advisoryPartitionSizeInBytes.</td><td>256MB</td></tr>
  <tr><td>spark.sql.broadcastTimeout</td><td>Controls the timeout period in seconds for the broadcast operations during broadcast joins.</td><td>300 seconds</td></tr>
  <tr><td>spark.sql.cbo.enabled</td><td>Specifies whether to enable cost-based optimization (CBO) for plan statistics estimation.</td><td>false</td></tr>
  <tr><td>spark.sql.cbo.joinReorder.dp.star.filter</td><td>Specifies whether to apply star-join filter heuristics during cost-based join enumeration.</td><td>false</td></tr>
  <tr><td>spark.sql.cbo.joinReorder.dp.threshold</td><td>Sets the maximum number of joined nodes allowed in the dynamic programming algorithm.</td><td>12</td></tr>
  <tr><td>spark.sql.cbo.joinReorder.enabled</td><td>Specifies whether to enable join reordering in cost-based optimization (CBO).</td><td>false</td></tr>
  <tr><td>spark.sql.cbo.planStats.enabled</td><td>Specifies whether to fetch row counts and column statistics from the catalog during logical plan generation.</td><td>false</td></tr>
  <tr><td>spark.sql.cbo.starSchemaDetection</td><td>Specifies whether to enable join reordering based on star schema detection.</td><td>false</td></tr>
  <tr><td>spark.sql.files.maxPartitionNum</td><td>Sets the target maximum number of split file partitions for file-based sources (Parquet, JSON, and ORC). Rescales partitions when the initial count exceeds this value. This is a suggested target, not a guaranteed limit.</td><td>(none)</td></tr>
  <tr><td>spark.sql.files.maxRecordsPerFile</td><td>Sets the maximum number of records to write to a single file. No limit applies when set to zero or a negative value.</td><td>0</td></tr>
  <tr><td>spark.sql.files.minPartitionNum</td><td>Sets the target minimum number of split file partitions for file-based sources (Parquet, JSON, and ORC). Defaults to spark.sql.leafNodeDefaultParallelism. This is a suggested target, not a guaranteed limit.</td><td>(none)</td></tr>
  <tr><td>spark.sql.inMemoryColumnarStorage.batchSize</td><td>Controls the batch size for columnar caching. Increasing the size improves memory utilization and compression but increases the risk of out-of-memory errors.</td><td>10000</td></tr>
  <tr><td>spark.sql.inMemoryColumnarStorage.compressed</td><td>Specifies whether to automatically select compression codecs for columns based on data statistics.</td><td>true</td></tr>
  <tr><td>spark.sql.inMemoryColumnarStorage.enableVectorizedReader</td><td>Specifies whether to enable vectorized reading for columnar caching.</td><td>true</td></tr>
  <tr><td>spark.sql.legacy.allowHashOnMapType</td><td>Specifies whether to allow hash operations on map type data structures. This legacy setting maintains compatibility with older Spark versions' map type handling.</td><td>(none)</td></tr>
  <tr><td>spark.sql.legacy.allowNegativeScaleOfDecimal</td><td>Specifies whether to allow negative scale values in decimal type definitions. This legacy setting maintains compatibility with older Spark versions that supported negative decimal scales.</td><td>(none)</td></tr>
  <tr><td>spark.sql.legacy.castComplexTypesToString.enabled</td><td>Specifies whether to enable legacy behavior for casting complex types to strings. Maintains compatibility with older Spark versions' type conversion rules.</td><td>(none)</td></tr>
  <tr><td>spark.sql.legacy.charVarcharAsString</td><td>Specifies whether to treat CHAR and VARCHAR types as STRING types. This legacy setting provides compatibility with older Spark versions' string type handling.</td><td>(none)</td></tr>
  <tr><td>spark.sql.legacy.createEmptyCollectionUsingStringType</td><td>Specifies whether to create empty collections using string type elements. This legacy setting maintains compatibility with older Spark versions' collection initialization behavior.</td><td>(none)</td></tr>
  <tr><td>spark.sql.legacy.exponentLiteralAsDecimal.enabled</td><td>Specifies whether to interpret exponential literals as decimal types. This legacy setting maintains compatibility with older Spark versions' numeric literal handling.</td><td>(none)</td></tr>
  <tr><td>spark.sql.legacy.json.allowEmptyString.enabled</td><td>Specifies whether to allow empty strings in JSON processing. This legacy setting maintains compatibility with older Spark versions' JSON parsing behavior.</td><td>(none)</td></tr>
  <tr><td>spark.sql.legacy.parquet.int96RebaseModeInRead</td><td>Specifies whether to use legacy INT96 timestamp rebase mode when reading Parquet files. This legacy setting maintains compatibility with older Spark versions' timestamp handling.</td><td>(none)</td></tr>
  <tr><td>spark.sql.legacy.timeParserPolicy</td><td>Controls the time parsing behavior for backwards compatibility. This legacy setting determines how timestamps and dates are parsed from strings.</td><td>(none)</td></tr>
  <tr><td>spark.sql.legacy.typeCoercion.datetimeToString.enabled</td><td>Specifies whether to enable legacy type coercion behavior when converting datetime values to strings. Maintains compatibility with older Spark versions' datetime conversion rules.</td><td>(none)</td></tr>
  <tr><td>spark.sql.maxSinglePartitionBytes</td><td>Sets the maximum partition size in bytes. The planner introduces shuffle operations for larger partitions to improve parallelism.</td><td>128m</td></tr>
  <tr><td>spark.sql.metadataCacheTTLSeconds</td><td>Controls the time-to-live (TTL) for metadata caches. Applies to partition file metadata and session catalog caches. Requires:<ul><li> A positive value greater than zero </li><li> spark.sql.catalogImplementation set to hive </li><li> spark.sql.hive.filesourcePartitionFileCacheSize greater than zero </li><li> spark.sql.hive.manageFilesourcePartitions set to true </li></ul></td><td>-1000ms</td></tr>
  <tr><td>spark.sql.optimizer.collapseProjectAlwaysInline</td><td>Specifies whether to collapse adjacent projections and inline expressions, even when it causes duplication.</td><td>false</td></tr>
  <tr><td>spark.sql.optimizer.dynamicPartitionPruning.enabled</td><td>Specifies whether to generate predicates for partition columns used as join keys.</td><td>true</td></tr>
  <tr><td>spark.sql.optimizer.enableCsvExpressionOptimization</td><td>Specifies whether to optimize CSV expressions in SQL optimizer by pruning unnecessary columns from from_csv operations.</td><td>true</td></tr>
  <tr><td>spark.sql.optimizer.enableJsonExpressionOptimization</td><td>Specifies whether to optimize JSON expressions in SQL optimizer by:<ul><li> Pruning unnecessary columns from from_json operations </li><li> Simplifying from_json and to_json combinations </li><li> Optimizing named_struct operations </li></ul></td><td>true</td></tr>
  <tr><td>spark.sql.optimizer.excludedRules</td><td>Defines optimizer rules to disable, identified by comma-separated rule names. Some rules cannot be disabled as they are required for correctness. The optimizer logs which rules are successfully disabled.</td><td>(none)</td></tr>
  <tr><td>spark.sql.optimizer.runtime.bloomFilter.applicationSideScanSizeThreshold</td><td>Sets the minimum aggregated scan size in bytes required to inject a Bloom filter on the application side.</td><td>10GB</td></tr>
  <tr><td>spark.sql.optimizer.runtime.bloomFilter.creationSideThreshold</td><td>Defines the maximum size threshold for injecting a Bloom filter on the creation side.</td><td>10MB</td></tr>
  <tr><td>spark.sql.optimizer.runtime.bloomFilter.enabled</td><td>Specifies whether to insert a Bloom filter to reduce shuffle data when one side of a shuffle join has a selective predicate.</td><td>true</td></tr>
  <tr><td>spark.sql.optimizer.runtime.bloomFilter.expectedNumItems</td><td>Defines the default number of expected items in the runtime Bloom filter.</td><td>1000000</td></tr>
  <tr><td>spark.sql.optimizer.runtime.bloomFilter.maxNumBits</td><td>Sets the maximum number of bits allowed in the runtime Bloom filter.</td><td>67108864</td></tr>
  <tr><td>spark.sql.optimizer.runtime.bloomFilter.maxNumItems</td><td>Sets the maximum number of expected items allowed in the runtime Bloom filter.</td><td>4000000</td></tr>
  <tr><td>spark.sql.optimizer.runtime.bloomFilter.numBits</td><td>Defines the default number of bits used in the runtime Bloom filter.</td><td>8388608</td></tr>
  <tr><td>spark.sql.optimizer.runtime.rowLevelOperationGroupFilter.enabled</td><td>Specifies whether to enable runtime group filtering for row-level operations. Allows data sources to:<ul><li> Prune entire groups of data (such as files or partitions) using data source filters </li><li> Execute runtime queries to identify matching records </li><li> Discard unnecessary groups to avoid expensive rewrites </li></ul><br />Limitations:<ul><li> Not all expressions can convert to data source filters </li><li> Some expressions require Spark evaluation (such as subqueries) </li></ul></td><td>true</td></tr>
  <tr><td>spark.sql.optimizer.runtimeFilter.number.threshold</td><td>Sets the total number of injected runtime filters (non-DPP). This is to prevent driver OOMs with too many Bloom filters.</td><td>10</td></tr>
  <tr><td>spark.sql.optimizer.runtimeFilter.semiJoinReduction.enabled</td><td>Specifies whether to insert a semi-join to reduce shuffle data when one side of a shuffle join has a selective predicate.</td><td>false</td></tr>
  <tr><td>spark.sql.parquet.aggregatePushdown</td><td>Specifies whether to push down aggregates to Parquet for optimization. Supports:<ul><li> MIN and MAX for boolean, integer, float, and date types </li><li> COUNT for all data types </li></ul><br />Throws an exception if statistics are missing from any Parquet file footer.</td><td>false</td></tr>
  <tr><td>spark.sql.parquet.columnarReaderBatchSize</td><td>Controls the number of rows in each Parquet vectorized reader batch. Choose a value that balances performance overhead and memory usage to prevent out-of-memory errors.</td><td>4096</td></tr>
  <tr><td>spark.sql.parquet.enableVectorizedReader</td><td>Specifies whether to enable vectorized Parquet decoding.</td><td>true</td></tr>
  <tr><td>spark.sql.shuffle.partitions</td><td>Sets the default number of partitions for data shuffling during joins or aggregations. Cannot be modified between structured streaming query restarts from the same checkpoint location.</td><td>200</td></tr>
  <tr><td>spark.sql.shuffledHashJoinFactor</td><td>Defines the multiplication factor used to determine shuffle hash join eligibility. A shuffle hash join is selected when the small-side data size multiplied by this factor is less than the large-side data size.</td><td>3</td></tr>
  <tr><td>spark.sql.sources.parallelPartitionDiscovery.threshold</td><td>Sets the maximum number of paths for driver-side file listing with file-based sources (Parquet, JSON, and ORC). When exceeded during partition discovery, files are listed using a separate Spark distributed job.</td><td>32</td></tr>
  <tr><td>spark.sql.statistics.histogram.enabled</td><td>Specifies whether to generate equi-height histograms during column statistics computation to improve estimation accuracy. Requires an additional table scan beyond the one needed for basic column statistics.</td><td>false</td></tr>
  <tr><td>spark.dynamicAllocation.executorIdleTimeout</td><td>Sets the duration an executor must be idle before it is removed when dynamic allocation is enabled.</td><td>60s</td></tr>
  <tr><td>spark.dynamicAllocation.schedulerBacklogTimeout</td><td>Sets the duration that pending tasks must be backlogged before new executors are requested when dynamic allocation is enabled.</td><td>1s</td></tr>
  <tr><td>spark.dynamicAllocation.sustainedSchedulerBacklogTimeout</td><td>Same as spark.dynamicAllocation.schedulerBacklogTimeout, but used only for subsequent executor requests.</td><td>(value of spark.dynamicAllocation.schedulerBacklogTimeout)</td></tr>
  <tr><td>spark.scheduler.minRegisteredResourcesRatio</td><td>Sets the minimum ratio of registered resources (registered resources / total expected resources) to wait for before scheduling begins. Specified as a double between 0.0 and 1.0. Regardless of whether the minimum ratio of resources has been reached, the maximum amount of time it will wait before scheduling begins is controlled by spark.scheduler.maxRegisteredResourcesWaitingTime.</td><td>0.8</td></tr>
  <tr><td>spark.scheduler.maxRegisteredResourcesWaitingTime</td><td>Sets the maximum amount of time to wait for resources to register before scheduling begins.</td><td>30s</td></tr>
  <tr><td>spark.sql.hive.metastorePartitionPruningFallbackOnException</td><td>Specifies whether to fall back to getting all partitions from Hive metastore and perform partition pruning on the Spark client side when encountering MetaException from the metastore.</td><td>false</td></tr>
  <tr><td>spark.sql.crossJoin.enabled</td><td>Specifies whether to allow queries that contain a cartesian product without explicit CROSS JOIN syntax.</td><td>true</td></tr>
  <tr><td>spark.sql.analyzer.maxIterations</td><td>Sets the maximum number of iterations the query analyzer runs before giving up. Higher values allow the analyzer to process very large or deeply nested queries.</td><td>100</td></tr>
  <tr><td>spark.sql.dataprefetch.filescan.maxParallelismPerTask</td><td>Sets the maximum number of file splits to pre-fetch concurrently for each task when scanning files.</td><td>4</td></tr>
  <tr><td>spark.sql.iceberg.data-prefetch.enabled</td><td>Specifies whether to enable data pre-fetch optimization when reading Iceberg tables.</td><td>true</td></tr>
  <tr><td>spark.sql.legacy.nullValueWrittenAsQuotedEmptyStringCsv</td><td>Specifies whether to restore the legacy behavior of writing nulls as quoted empty strings in CSV output. When false, Spark writes nulls as unquoted empty strings.</td><td>false</td></tr>
  <tr><td>spark.maxRemoteBlockSizeFetchToMem</td><td>Sets the size threshold above which Spark fetches remote blocks to disk instead of memory. This avoids a single large request consuming too much memory.</td><td>200m</td></tr>
  <tr><td>spark.emr-serverless.allocation.batch.size</td><td>Sets the number of executors to request at once in each round of executor allocation.</td><td>20</td></tr>
</tbody>
</table>



<table>
<thead>
  <tr><th>Property Name</th><th>Description</th><th>Default Value</th></tr>
</thead>
<tbody>
  <tr><td>spark.sql.autoBroadcastJoinThreshold</td><td>Sets the maximum table size in bytes for broadcasting to worker nodes during joins. Set to -1 to disable broadcasting.</td><td>10MB</td></tr>
  <tr><td>spark.io.compression.codec</td><td>Sets the codec used to compress internal data such as RDD partitions, event log, broadcast variables, and shuffle outputs. Supported values: lz4, snappy, zstd, gzip.</td><td>lz4</td></tr>
  <tr><td>spark.sql.session.timeZone</td><td>Defines the session time zone for handling timestamps in string literals and Java object conversion. Accepts:<ul><li> Region-based IDs in area/city format (such as America/Los_Angeles) </li><li> Zone offsets in (+/-)HH, (+/-)HH:mm, or (+/-)HH:mm:ss format (such as -08 or +01:00) </li><li> UTC or Z as aliases for +00:00 </li></ul></td><td>(value of local timezone)</td></tr>
  <tr><td>spark.cleanrooms.executor.memoryOverheadFactor</td><td>Sets the fraction of total executor memory used to determine the split between spark.executor.memory and spark.executor.memoryOverhead. Specified as a double between 0.0 and less than 1.0.</td><td>0.1</td></tr>
  <tr><td>spark.cleanrooms.driver.memoryOverheadFactor</td><td>Sets the fraction of total driver memory used to determine the split between spark.driver.memory and spark.driver.memoryOverhead. Specified as a double between 0.0 and less than 1.0.</td><td>0.1</td></tr>
  <tr><td>spark.memory.storageFraction</td><td>Sets the amount of storage memory immune to eviction, expressed as a fraction of the size of the region set aside by spark.memory.fraction. The higher this is, the less working memory may be available to execution and tasks may spill to disk more often. Leaving this at the default value is recommended.</td><td>0.5</td></tr>
  <tr><td>spark.rpc.askTimeout</td><td>Sets the duration for an RPC ask operation to wait before timing out.</td><td>(value of spark.network.timeout)</td></tr>
  <tr><td>spark.executor.heartbeatInterval</td><td>Sets the interval between each executor's heartbeats to the driver. Heartbeats let the driver know that the executor is still alive and update it with metrics for in-progress tasks. spark.executor.heartbeatInterval should be significantly less than spark.network.timeout.</td><td>10s</td></tr>
  <tr><td>spark.stage.maxConsecutiveAttempts</td><td>Sets the number of consecutive stage attempts allowed before a stage is aborted.</td><td>4</td></tr>
  <tr><td>spark.task.cpus</td><td>Sets the number of cores to allocate for each task.</td><td>1</td></tr>
  <tr><td>spark.shuffle.file.buffer</td><td>Sets the size of the in-memory buffer for each shuffle file output stream, in KiB unless otherwise specified. These buffers reduce the number of disk seeks and system calls made in creating intermediate shuffle files.</td><td>32k</td></tr>
  <tr><td>spark.reducer.maxSizeInFlight</td><td>Sets the maximum size of map outputs to fetch simultaneously from each reduce task, in MiB unless otherwise specified. Since each output requires a buffer to receive it, this represents a fixed memory overhead per reduce task, so keep it small unless you have a large amount of memory.</td><td>48m</td></tr>
</tbody>
</table>


1. (Optional) For **Compute payer**, select the collaboration member who pays for job compute costs.
**Note**  
If there is only one payer candidate for job compute in the collaboration, it defaults to that payer.

1. Choose **Run**.
**Note**  
You can't run the job if the member who can receive results hasn’t configured the job results settings.

1. Continue to adjust parameters and run your job again, or choose the **\+** button to start a new job in a new tab.