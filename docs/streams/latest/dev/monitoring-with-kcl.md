

# Monitor the Kinesis Client Library with Amazon CloudWatch
<a name="monitoring-with-kcl"></a>

The [Kinesis Client Library](https://docs.aws.amazon.com/kinesis/latest/dev/developing-consumers-with-kcl.html) (KCL) for Amazon Kinesis Data Streams publishes custom Amazon CloudWatch metrics on your behalf, using the name of your KCL application as the namespace. You can view these metrics by navigating to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/) and choosing **Custom Metrics**. For more information about custom metrics, see [Publish Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html) in the *Amazon CloudWatch User Guide*.

There is a nominal charge for the metrics uploaded to CloudWatch by the KCL; specifically, *Amazon CloudWatch Custom Metrics* and *Amazon CloudWatch API Requests* charges apply. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Topics**
+ [Metrics and namespace](#metrics-namespace)
+ [Metric levels and dimensions](#metric-levels)
+ [Metric configuration](#metrics-config)
+ [List of metrics](#kcl-metrics-list)

## Metrics and namespace
<a name="metrics-namespace"></a>

The namespace that is used to upload metrics is the application name that you specify when you launch the KCL.

## Metric levels and dimensions
<a name="metric-levels"></a>

There are two options to control which metrics are uploaded to CloudWatch:

metric levels  
Every metric is assigned an individual level. When you set a metrics reporting level, metrics with an individual level below the reporting level are not sent to CloudWatch. The levels are: `NONE`, `SUMMARY`, and `DETAILED`. The default setting is `DETAILED`; that is, all metrics are sent to CloudWatch. A reporting level of `NONE` means that no metrics are sent at all. For information about which levels are assigned to what metrics, see [List of metrics](#kcl-metrics-list).

enabled dimensions  
Every KCL metric has associated dimensions that also get sent to CloudWatch. In KCL 2.x, if KCL is configured to process a single data stream, all the metrics dimensions (`Operation`, `ShardId`, and `WorkerIdentifier`) are enabled by default. Also, in KCL 2.x, if KCL is configured to process a single data stream, `Operation` dimension cannot be disabled. In KCL 2.x, if KCL is configured to process multiple data streams, all the metrics dimensions (`Operation`, `ShardId`, `StreamId`, and `WorkerIdentifier`) are enabled by default. Also, in KCL 2.x, if KCL is configured to process multiple data streams, the `Operation` and the `StreamId` dimensions cannot be disabled. `StreamId` dimension is available only for the per-shard metrics.  
 In KCL 1.x, only the `Operation` and the `ShardId` dimensions are enabled by default, and the `WorkerIdentifier` dimension is disabled. In KCL 1.x, the `Operation` dimension cannot be disabled.  
For more information about CloudWatch metric dimensions, see the [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Dimension) section in the Amazon CloudWatch Concepts topic, in the *Amazon CloudWatch User Guide*.  
When the `WorkerIdentifier` dimension is enabled, if a different value is used for the worker ID property every time a particular KCL worker restarts, new sets of metrics with new `WorkerIdentifier` dimension values are sent to CloudWatch. If you need the `WorkerIdentifier` dimension value to be the same across specific KCL worker restarts, you must explicitly specify the same worker ID value during initialization for each worker. Note that the worker ID value for each active KCL worker must be unique across all KCL workers.

## Metric configuration
<a name="metrics-config"></a>

Metric levels and enabled dimensions can be configured using the KinesisClientLibConfiguration instance, which is passed to Worker when launching the KCL application. In the MultiLangDaemon case, the `metricsLevel` and `metricsEnabledDimensions` properties can be specified in the .properties file used to launch the MultiLangDaemon KCL application.

Metric levels can be assigned one of three values: NONE, SUMMARY, or DETAILED. Enabled dimensions values must be comma-separated strings with the list of dimensions that are allowed for the CloudWatch metrics. The dimensions used by the KCL application are `Operation`, `ShardId`, and `WorkerIdentifier`.

## List of metrics
<a name="kcl-metrics-list"></a>

The following tables list the KCL metrics, grouped by scope and operation.

**Topics**
+ [Per-KCL-application metrics](#kcl-metrics-per-app)
+ [Per-worker metrics](#kcl-metrics-per-worker)
+ [Per-shard metrics](#kcl-metrics-per-shard)

### Per-KCL-application metrics
<a name="kcl-metrics-per-app"></a>

These metrics are aggregated across all KCL workers within the scope of the application, as defined by the Amazon CloudWatch namespace.

**Topics**
+ [LeaseAssignmentManager](#lease-assignment-manager)
+ [InitializeTask](#init-task)
+ [ShutdownTask](#shutdown-task)
+ [ShardSyncTask](#shard-sync-task)
+ [BlockOnParentTask](#block-parent-task)
+ [PeriodicShardSyncManager](#periodic-task)
+ [MultistreamTracker](#multi-task)

#### LeaseAssignmentManager
<a name="lease-assignment-manager"></a>

The `LeaseAssignmentManager` operation is responsible for assigning leases to workers and rebalancing leases among workers to achieve even utilization of worker resources. The logic for this operation includes reading the lease related metadata from the lease table and metrics from the worker metrics table, and performing lease assignments.


| Metric | Description | 
| --- | --- | 
| LeaseAndWorkerMetricsLoad.Time | Time taken to load all leases and worker metrics entry in the lease assignment manager (LAM), the new lease assignment and load balancing algorithm introduced in KCL 3.x.<br />Metric level: Detailed<br />Units: Milliseconds | 
| TotalLeases | Total number of leases for the current KCL application.<br />Metric level: Summary<br />Units: Count | 
| NumWorkers | Total number of workers in the current KCL application.<br />Metric level: Summary<br />Units: Count | 
| AssignExpiredOrUnassignedLeases.Time | Time to perform in-memory assignment of expired leases.<br />Metric level: Detailed<br />Units: Milliseconds | 
| LeaseSpillover | Number of leases that were not assigned due to hitting the limit on the maximum number of leases or maximum throughput per worker.<br />Metric level: Summary<br />Units: Count | 
| BalanceWorkerVariance.Time | Time to perform in-memory balancing of leases between workers.<br />Metric level: Detailed<br />Units: Milliseconds | 
| NumOfLeasesReassignment | Total number of lease reassignments made in the current reassignment iteration.<br />Metric level: Summary<br />Units: Count | 
| FailedAssignmentCount | Number of failures in AssignLease calls to the DynamoDB lease table. <br />Metric level: Detailed<br />Units: Count | 
| ParallelyAssignLeases.Time | Time to flush new assignments to the DynamoDB lease table.<br />Metric level: Detailed<br />Units: Milliseconds | 
| ParallelyAssignLeases.Success | Number of successful flush of new assignments.<br />Metric level: Detailed<br />Units: Count | 
| TotalStaleWorkerMetricsEntry | Total number of worker metrics entries that must be cleaned up.<br />Metric level: Detailed<br />Units: Count | 
| StaleWorkerMetricsCleanup.Time | Time to perform worker metrics entry deletion from the DynamoDB worker metrics table.<br />Metric level: Detailed<br />Units: Milliseconds | 
| Time | Time taken by the `LeaseAssignmentManager` operation.<br />Metric level: Summary<br />Units: Milliseconds | 
| Success | Number of times the `LeaseAssignmentManager` operation successfully completed.<br />Metric level: Summary<br />Units: Count | 
| ForceLeaderRelease | Indicates that the lease assignment manager has failed 3 times consecutively and the leader worker is releasing the leadership.<br />Metric level: Summary<br />Units: Count | 
| NumWorkersWithInvalidEntry | Number of worker metrics entries which are considered invalid. <br />Metric level: Summary<br />Units: Count | 
| NumWorkersWithFailingWorkerMetric | Number of worker metrics entries which has -1 (representing worker metric value is not available) as one of the value for worker metrics.<br />Metric level: Summary<br />Units: Count | 
| LeaseDeserializationFailureCount | Lease entry from the lease table which failed to deserialize.<br />Metric level: Summary<br />Units: Count | 

#### InitializeTask
<a name="init-task"></a>

The `InitializeTask` operation is responsible for initializing the record processor for the KCL application. The logic for this operation includes getting a shard iterator from Kinesis Data Streams and initializing the record processor.


| Metric | Description | 
| --- | --- | 
| KinesisDataFetcher.getIterator.Success | Number of successful `GetShardIterator` operations per KCL application. <br />Metric level: Detailed<br />Units: Count | 
| KinesisDataFetcher.getIterator.Time | Time taken per `GetShardIterator` operation for the given KCL application.<br />Metric level: Detailed<br />Units: Milliseconds | 
| RecordProcessor.initialize.Time | Time taken by the record processor’s initialize method.<br />Metric level: Summary<br />Units: Milliseconds | 
| Success | Number of successful record processor initializations. <br />Metric level: Summary<br />Units: Count | 
| Time | Time taken by the KCL worker for the record processor initialization.<br />Metric level: Summary<br />Units: Milliseconds | 

#### ShutdownTask
<a name="shutdown-task"></a>

The `ShutdownTask` operation initiates the shutdown sequence for shard processing. This can occur because a shard is split or merged, or when the shard lease is lost from the worker. In both cases, the record processor `shutdown()` function is invoked. New shards are also discovered in the case where a shard was split or merged, resulting in the creation of one or two new shards.


| Metric | Description | 
| --- | --- | 
| CreateLease.Success | Number of times that new child shards are successfully added into the KCL application DynamoDB table following parent shard shutdown.<br />Metric level: Detailed<br />Units: Count | 
| CreateLease.Time | Time taken for adding new child shard information in the KCL application DynamoDB table.<br />Metric level: Detailed<br />Units: Milliseconds | 
| UpdateLease.Success | Number of successful final checkpoints during the record processor shutdown.<br />Metric level: Detailed<br />Units: Count | 
| UpdateLease.Time | Time taken by the checkpoint operation during the record processor shutdown.<br />Metric level: Detailed<br />Units: Milliseconds | 
| RecordProcessor.shutdown.Time | Time taken by the record processor’s shutdown method.<br />Metric level: Summary<br />Units: Milliseconds | 
| Success | Number of successful shutdown tasks.<br />Metric level: Summary<br />Units: Count | 
| Time | Time taken by the KCL worker for the shutdown task.<br />Metric level: Summary<br />Units: Milliseconds | 

#### ShardSyncTask
<a name="shard-sync-task"></a>

The `ShardSyncTask` operation discovers changes to shard information for the Kinesis data stream, so new shards can be processed by the KCL application.


| Metric | Description | 
| --- | --- | 
| CreateLease.Success | Number of successful attempts to add new shard information into the KCL application DynamoDB table.<br />Metric level: Detailed<br />Units: Count | 
| CreateLease.Time | Time taken for adding new shard information in the KCL application DynamoDB table.<br />Metric level: Detailed<br />Units: Milliseconds | 
| Success | Number of successful shard sync operations.<br />Metric level: Summary<br />Units: Count | 
| Time | Time taken for the shard sync operation.<br />Metric level: Summary<br />Units: Milliseconds | 

#### BlockOnParentTask
<a name="block-parent-task"></a>

If the shard is split or merged with other shards, then new child shards are created. The `BlockOnParentTask` operation ensures that record processing for the new shards does not start until the parent shards are completely processed by the KCL.


| Metric | Description | 
| --- | --- | 
| Success | Number of successful checks for parent shard completion.<br />Metric level: Summary<br />Units: Count | 
| Time | Time taken for parent shards completion.<br />Metric level: Summary<br />Unit: Milliseconds | 

#### PeriodicShardSyncManager
<a name="periodic-task"></a>

The `PeriodicShardSyncManager` is responsible for examining the data streams that are being processed by the KCL consumer application, identifying data streams with partial leases and handing them off for synchronization.

The following metrics are available when KCL is configured to process a single data stream (then the value of NumStreamsToSync and NumStreamsWithPartialLeases is set to 1) and also when KCL is configured to process multiple data streams.


| Metric | Description | 
| --- | --- | 
| NumStreamsToSync | The number of data streams (per AWS account) being processed by the consumer application that contains partial leases and that must be handed off for synchronization. <br />Metric level: Summary<br />Units: Count | 
| NumStreamsWithPartialLeases | The number of data streams (per AWS account) that the consumer application is processing that contains partial leases. <br />Metric level: Summary<br />Units: Count | 
| Success | The number of times `PeriodicShardSyncManager` was able to successfully identify partial leases in the data streams that the consumer application is processing. <br />Metric level: Summary<br />Units: Count | 
| Time | The amount of the time (in milliseconds) that the `PeriodicShardSyncManager` takes to examine the data streams that the consumer application is processing, in order to determine which data streams require shard synchronization. <br />Metric level: Summary<br />Units: Milliseconds | 

#### MultistreamTracker
<a name="multi-task"></a>

The `MultistreamTracker` interface enables you to build KCL consumer applications that can process multiple data streams at the same time.


| Metric | Description | 
| --- | --- | 
| DeletedStreams.Count | The number of data streams deleted at this time period.<br />Metric level: Summary<br />Units: Count | 
| ActiveStreams.Count | The number of active data streams being processed.<br />Metric level: Summary<br />Units: Count | 
| StreamsPendingDeletion.Count | The number of data streams that are pending deletion based on `FormerStreamsLeasesDeletionStrategy`. <br />Metric level: Summary<br />Units: Count | 

### Per-worker metrics
<a name="kcl-metrics-per-worker"></a>

These metrics are aggregated across all record processors consuming data from a Kinesis data stream, such as an Amazon EC2 instance.

**Topics**
+ [WorkerMetricStatsReporter](#worker-metrics-stats)
+ [LeaseDiscovery](#lease-discovery)
+ [RenewAllLeases](#renew-leases)
+ [TakeLeases](#take-leases)

#### WorkerMetricStatsReporter
<a name="worker-metrics-stats"></a>

The `WorkerMetricStatReporter` operation is responsible for periodically publishing metrics of the current worker to the worker metrics table. These metrics are used by the `LeaseAssignmentManager` operation to perform lease assignments.


| Metric | Description | 
| --- | --- | 
| InMemoryMetricStatsReporterFailure | Number of failures to capture the in-memory worker metric value, due to failure of some worker metrics.<br />Metric level: Summary<br />Units: Count | 
| WorkerMetricStatsReporter.Time | Time taken by the `WorkerMetricsStats` operation.<br />Metric level: Summary<br />Units: Milliseconds | 
| WorkerMetricStatsReporter.Success | Number of times the `WorkerMetricsStats` operation successfully completed.<br />Metric level: Summary<br />Units: Count | 

#### LeaseDiscovery
<a name="lease-discovery"></a>

The `LeaseDiscovery` operation is responsible for identifying the new leases assigned to the current worker by the `LeaseAssignmentManager` operation. The logic for this operation involves identifying leases assigned to the current worker by reading the global secondary index of the lease table.


| Metric | Description | 
| --- | --- | 
| ListLeaseKeysForWorker.Time | Time to call the global secondary index on the lease table and get lease keys assigned to the current worker.<br />Metric level: Detailed<br />Units: Milliseconds | 
| FetchNewLeases.Time | Time to fetch all new leases from the lease table. <br />Metric level: Detailed<br />Units: Milliseconds | 
| NewLeasesDiscovered | Total number of new leases assigned to workers.<br />Metric level: Detailed<br />Units: Count | 
| Time | Time taken by the `LeaseDiscovery` operation.<br />Metric level: Summary<br />Units: Milliseconds | 
| Success | Number of times the `LeaseDiscovery` operation successfully completed.<br />Metric level: Summary<br />Units: Count | 
| OwnerMismatch | Number of owner mismatches from GSI response and lease table consistent read.<br />Metric level: Detailed<br />Units: Count | 

#### RenewAllLeases
<a name="renew-leases"></a>

The `RenewAllLeases` operation periodically renews shard leases owned by a particular worker instance. 


| Metric | Description | 
| --- | --- | 
| RenewLease.Success | Number of successful lease renewals by the worker.<br />Metric level: Detailed<br />Units: Count | 
| RenewLease.Time | Time taken by the lease renewal operation.<br />Metric level: Detailed<br />Units: Milliseconds | 
| CurrentLeases | Number of shard leases owned by the worker after all leases are renewed.<br />Metric level: Summary<br />Units: Count | 
| LostLeases | Number of shard leases that were lost following an attempt to renew all leases owned by the worker.<br />Metric level: Summary<br />Units: Count | 
| Success | Number of times the lease renewal operation was successful for the worker.<br />Metric level: Summary<br />Units: Count | 
| Time | Time taken for renewing all leases for the worker.<br />Metric level: Summary<br />Units: Milliseconds | 

#### TakeLeases
<a name="take-leases"></a>

The `TakeLeases` operation balances record processing between all KCL workers. If the current KCL worker has fewer shard leases than required, it takes shard leases from another worker that is overloaded.


| Metric | Description | 
| --- | --- | 
| ListLeases.Success | Number of times all shard leases were successfully retrieved from the KCL application DynamoDB table.<br />Metric level: Detailed<br />Units: Count | 
| ListLeases.Time | Time taken to retrieve all shard leases from the KCL application DynamoDB table.<br />Metric level: Detailed<br />Units: Milliseconds | 
| TakeLease.Success | Number of times the worker successfully took shard leases from other KCL workers.<br />Metric level: Detailed<br />Units: Count | 
| TakeLease.Time | Time taken to update the lease table with leases taken by the worker.<br />Metric level: Detailed<br />Units: Milliseconds | 
| NumWorkers | Total number of workers, as identified by a specific worker.<br />Metric level: Summary<br />Units: Count | 
| NeededLeases | Number of shard leases that the current worker needs for a balanced shard-processing load.<br />Metric level: Detailed<br />Units: Count | 
| LeasesToTake | Number of leases that the worker will attempt to take.<br />Metric level: Detailed<br />Units: Count | 
| TakenLeases | Number of leases taken successfully by the worker.<br />Metric level: Summary<br />Units: Count  | 
| TotalLeases | Total number of shards that the KCL application is processing.<br />Metric level: Detailed<br />Units: Count | 
| ExpiredLeases | Total number of shards that are not being processed by any worker, as identified by the specific worker.<br />Metric level: Summary<br />Units: Count | 
| Success | Number of times the `TakeLeases` operation successfully completed.<br />Metric level: Summary<br />Units: Count | 
| Time | Time taken by the `TakeLeases` operation for a worker.<br />Metric level: Summary<br />Units: Milliseconds | 

### Per-shard metrics
<a name="kcl-metrics-per-shard"></a>

These metrics are aggregated across a single record processor.

#### ProcessTask
<a name="process-task"></a>

The `ProcessTask` operation calls [GetRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html) with the current iterator position to retrieve records from the stream and invokes the record processor `processRecords` function.


| Metric | Description | 
| --- | --- | 
| KinesisDataFetcher.getRecords.Success | Number of successful `GetRecords` operations per Kinesis data stream shard. <br />Metric level: Detailed<br />Units: Count | 
| KinesisDataFetcher.getRecords.Time | Time taken per `GetRecords` operation for the Kinesis data stream shard.<br />Metric level: Detailed<br />Units: Milliseconds | 
| UpdateLease.Success | Number of successful checkpoints made by the record processor for the given shard.<br />Metric level: Detailed<br />Units: Count | 
| UpdateLease.Time | Time taken for each checkpoint operation for the given shard.<br />Metric level: Detailed<br />Units: Milliseconds | 
| DataBytesProcessed | Total size of records processed in bytes on each `ProcessTask` invocation.<br />Metric level: Summary<br />Units: Byte | 
| RecordsProcessed | Number of records processed on each `ProcessTask` invocation.<br />Metric level: Summary<br />Units: Count | 
| ExpiredIterator | Number of ExpiredIteratorException received when calling `GetRecords`.<br />Metric level: Summary<br />Units: Count | 
| MillisBehindLatest | Time that the current iterator is behind from the latest record (tip) in the shard. This value is less than or equal to the difference in time between the latest record in a response and the current time. This is a more accurate reflection of how far a shard is from the tip than comparing timestamps in the last response record. This value applies to the latest batch of records, not an average of all timestamps in each record.Metric level: Summary<br />Units: Milliseconds | 
| RecordProcessor.processRecords.Time | Time taken by the record processor’s `processRecords` method.<br />Metric level: Summary<br />Units: Milliseconds | 
| Success | Number of successful process task operations.<br />Metric level: Summary<br />Units: Count | 
| Time | Time taken for the process task operation.<br />Metric level: Summary<br />Units: Milliseconds | 