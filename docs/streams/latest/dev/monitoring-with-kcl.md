# Monitor the Kinesis Client Library with

Amazon CloudWatch

The [Kinesis Client Library](../../../kinesis/latest/dev/developing-consumers-with-kcl.md "../../../kinesis/latest/dev/developing-consumers-with-kcl.md") (KCL) for Amazon Kinesis Data Streams publishes custom Amazon CloudWatch metrics on your
behalf, using the name of your KCL application as the namespace. You can view these
metrics by navigating to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/") and choosing **Custom
Metrics**. For more information about custom metrics, see [Publish Custom Metrics](../../../AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.md "../../../AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.md") in the
_Amazon CloudWatch User Guide_.

There is a nominal charge for the metrics uploaded to CloudWatch by the KCL; specifically,
_Amazon CloudWatch Custom Metrics_ and _Amazon CloudWatch API Requests_ charges apply. For more information,
see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Topics

- [Metrics and namespace](#metrics-namespace "#metrics-namespace")
- [Metric levels and dimensions](#metric-levels "#metric-levels")
- [Metric configuration](#metrics-config "#metrics-config")
- [List of metrics](#kcl-metrics-list "#kcl-metrics-list")

## Metrics and namespace

The namespace that is used to upload metrics is the application name that you
specify when you launch the KCL.

## Metric levels and dimensions

There are two options to control which metrics are uploaded to CloudWatch:

metric levels

Every metric is assigned an individual level. When you set a metrics
reporting level, metrics with an individual level below the reporting
level are not sent to CloudWatch. The levels are: `NONE`, `SUMMARY`, and `DETAILED`. The default setting is `DETAILED`; that is, all metrics are sent to CloudWatch.
A reporting level of `NONE` means that no metrics
are sent at all. For information about which levels are assigned to what
metrics, see [List of metrics](#kcl-metrics-list "#kcl-metrics-list").

enabled dimensions

Every KCL metric has associated dimensions that also get sent to
CloudWatch. In KCL 2.x, if KCL is configured to process a single data stream,
all the metrics dimensions (`Operation`,
`ShardId`, and `WorkerIdentifier`) are enabled by
default. Also, in KCL 2.x, if KCL is configured to process a single data
stream, `Operation` dimension cannot be disabled. In KCL 2.x,
if KCL is configured to process multiple data streams, all the metrics
dimensions (`Operation`, `ShardId`,
`StreamId`, and `WorkerIdentifier`) are
enabled by default. Also, in KCL 2.x, if KCL is configured to process
multiple data streams, the `Operation` and the
`StreamId` dimensions cannot be disabled.
`StreamId` dimension is available only for the per-shard
metrics.

In KCL 1.x, only the `Operation` and the
`ShardId` dimensions are enabled by default, and the
`WorkerIdentifier` dimension is disabled. In KCL 1.x, the
`Operation` dimension cannot be disabled.

For more information about CloudWatch metric dimensions, see the [Dimensions](../../../AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.md#Dimension") section in the Amazon CloudWatch Concepts topic, in the
_Amazon CloudWatch User Guide_.

When the `WorkerIdentifier` dimension is enabled, if a
different value is used for the worker ID property every time a
particular KCL worker restarts, new sets of metrics with new
`WorkerIdentifier` dimension values are sent to CloudWatch. If
you need the `WorkerIdentifier` dimension value to be the
same across specific KCL worker restarts, you must explicitly specify
the same worker ID value during initialization for each worker. Note
that the worker ID value for each active KCL worker must be unique
across all KCL workers.

## Metric configuration

Metric levels and enabled dimensions can be configured using the
KinesisClientLibConfiguration instance, which is passed to Worker when launching the
KCL application. In the MultiLangDaemon case, the `metricsLevel` and
`metricsEnabledDimensions` properties can be specified in the
.properties file used to launch the MultiLangDaemon KCL application.

Metric levels can be assigned one of three values: NONE, SUMMARY, or DETAILED.
Enabled dimensions values must be comma-separated strings with the list of
dimensions that are allowed for the CloudWatch metrics. The dimensions used by the KCL
application are `Operation`, `ShardId`, and
`WorkerIdentifier`.

## List of metrics

The following tables list the KCL metrics, grouped by scope and
operation.

###### Topics

- [Per-KCL-application metrics](#kcl-metrics-per-app "#kcl-metrics-per-app")
- [Per-worker metrics](#kcl-metrics-per-worker "#kcl-metrics-per-worker")
- [Per-shard metrics](#kcl-metrics-per-shard "#kcl-metrics-per-shard")

### Per-KCL-application metrics

These metrics are aggregated across all KCL workers within the scope of the
application, as defined by the Amazon CloudWatch namespace.

###### Topics

- [LeaseAssignmentManager](#lease-assignment-manager "#lease-assignment-manager")
- [InitializeTask](#init-task "#init-task")
- [ShutdownTask](#shutdown-task "#shutdown-task")
- [ShardSyncTask](#shard-sync-task "#shard-sync-task")
- [BlockOnParentTask](#block-parent-task "#block-parent-task")
- [PeriodicShardSyncManager](#periodic-task "#periodic-task")
- [MultistreamTracker](#multi-task "#multi-task")

#### LeaseAssignmentManager

The `LeaseAssignmentManager` operation is responsible for
assigning leases to workers and rebalancing leases among workers to achieve
even utilization of worker resources. The logic for this operation includes
reading the lease related metadata from the lease table and metrics from the
worker metrics table, and performing lease assignments.

| Metric                               | Description                                                                                                                                                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| LeaseAndWorkerMetricsLoad.Time       | Time taken to load all leases and worker metrics entry<br>in the lease assignment manager (LAM), the new lease<br>assignment and load balancing algorithm introduced in<br>KCL 3.x.<br>Metric level: Detailed<br>Units: Milliseconds |
| TotalLeases                          | Total number of leases for the current KCL<br>application.<br>Metric level: Summary<br>Units: Count                                                                                                                                  |
| NumWorkers                           | Total number of workers in the current KCL<br>application.<br>Metric level: Summary<br>Units: Count                                                                                                                                  |
| AssignExpiredOrUnassignedLeases.Time | Time to perform in-memory assignment of expired<br>leases.<br>Metric level: Detailed<br>Units: Milliseconds                                                                                                                          |
| LeaseSpillover                       | Number of leases that were not assigned due to hitting<br>the limit on the maximum number of leases or maximum<br>throughput per worker.<br>Metric level: Summary<br>Units: Count                                                    |
| BalanceWorkerVariance.Time           | Time to perform in-memory balancing of leases between<br>workers.<br>Metric level: Detailed<br>Units: Milliseconds                                                                                                                   |
| NumOfLeasesReassignment              | Total number of lease reassignments made in the<br>current reassignment iteration.<br>Metric level: Summary<br>Units: Count                                                                                                          |
| FailedAssignmentCount                | Number of failures in AssignLease calls to the DynamoDB<br>lease table.<br>Metric level: Detailed<br>Units: Count                                                                                                                    |
| ParallelyAssignLeases.Time           | Time to flush new assignments to the DynamoDB lease<br>table.<br>Metric level: Detailed<br>Units: Milliseconds                                                                                                                       |
| ParallelyAssignLeases.Success        | Number of successful flush of new assignments.<br>Metric level: Detailed<br>Units: Count                                                                                                                                             |
| TotalStaleWorkerMetricsEntry         | Total number of worker metrics entries that must be<br>cleaned up.<br>Metric level: Detailed<br>Units: Count                                                                                                                         |
| StaleWorkerMetricsCleanup.Time       | Time to perform worker metrics entry deletion from the<br>DynamoDB worker metrics table.<br>Metric level: Detailed<br>Units: Milliseconds                                                                                            |
| Time                                 | Time taken by the `LeaseAssignmentManager`<br>operation.<br>Metric level: Summary<br>Units: Milliseconds                                                                                                                             |
| Success                              | Number of times the<br>`LeaseAssignmentManager` operation<br>successfully completed.<br>Metric level: Summary<br>Units: Count                                                                                                        |
| ForceLeaderRelease                   | Indicates that the lease assignment manager has failed<br>3 times consecutively and the leader worker is releasing<br>the leadership.<br>Metric level: Summary<br>Units: Count                                                       |
| NumWorkersWithInvalidEntry           | Number of worker metrics entries which are considered<br>invalid.<br>Metric level: Summary<br>Units: Count                                                                                                                           |
| NumWorkersWithFailingWorkerMetric    | Number of worker metrics entries which has -1<br>(representing worker metric value is not available) as<br>one of the value for worker metrics.<br>Metric level: Summary<br>Units: Count                                             |
| LeaseDeserializationFailureCount     | Lease entry from the lease table which failed to<br>deserialize.<br>Metric level: Summary<br>Units: Count                                                                                                                            |

#### InitializeTask

The `InitializeTask` operation is responsible for initializing
the record processor for the KCL application. The logic for this operation
includes getting a shard iterator from Kinesis Data Streams and initializing the record
processor.

| Metric                                 | Description                                                                                                                    |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| KinesisDataFetcher.getIterator.Success | Number of successful `GetShardIterator`<br>operations per KCL application.<br>Metric level: Detailed<br>Units: Count           |
| KinesisDataFetcher.getIterator.Time    | Time taken per `GetShardIterator` operation<br>for the given KCL application.<br>Metric level: Detailed<br>Units: Milliseconds |
| RecordProcessor.initialize.Time        | Time taken by the record processor’s initialize<br>method.<br>Metric level: Summary<br>Units: Milliseconds                     |
| Success                                | Number of successful record processor initializations.<br>Metric level: Summary<br>Units: Count                                |
| Time                                   | Time taken by the KCL worker for the record<br>processor initialization.<br>Metric level: Summary<br>Units: Milliseconds       |

#### ShutdownTask

The `ShutdownTask` operation initiates the shutdown sequence
for shard processing. This can occur because a shard is split or merged, or
when the shard lease is lost from the worker. In both cases, the record
processor `shutdown()` function is invoked. New shards are also
discovered in the case where a shard was split or merged, resulting in the
creation of one or two new shards.

| Metric                        | Description                                                                                                                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CreateLease.Success           | Number of times that new child shards are successfully<br>added into the KCL application DynamoDB table following<br>parent shard shutdown.<br>Metric level: Detailed<br>Units: Count |
| CreateLease.Time              | Time taken for adding new child shard information in<br>the KCL application DynamoDB table.<br>Metric level: Detailed<br>Units: Milliseconds                                          |
| UpdateLease.Success           | Number of successful final checkpoints during the<br>record processor shutdown.<br>Metric level: Detailed<br>Units: Count                                                             |
| UpdateLease.Time              | Time taken by the checkpoint operation during the<br>record processor shutdown.<br>Metric level: Detailed<br>Units: Milliseconds                                                      |
| RecordProcessor.shutdown.Time | Time taken by the record processor’s shutdown<br>method.<br>Metric level: Summary<br>Units: Milliseconds                                                                              |
| Success                       | Number of successful shutdown tasks.<br>Metric level: Summary<br>Units: Count                                                                                                         |
| Time                          | Time taken by the KCL worker for the shutdown<br>task.<br>Metric level: Summary<br>Units: Milliseconds                                                                                |

#### ShardSyncTask

The `ShardSyncTask` operation discovers changes to shard
information for the Kinesis data stream, so new shards can be processed by the KCL
application.

| Metric              | Description                                                                                                                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| CreateLease.Success | Number of successful attempts to add new shard<br>information into the KCL application DynamoDB<br>table.<br>Metric level: Detailed<br>Units: Count |
| CreateLease.Time    | Time taken for adding new shard information in the<br>KCL application DynamoDB table.<br>Metric level: Detailed<br>Units: Milliseconds              |
| Success             | Number of successful shard sync operations.<br>Metric level: Summary<br>Units: Count                                                                |
| Time                | Time taken for the shard sync operation.<br>Metric level: Summary<br>Units: Milliseconds                                                            |

#### BlockOnParentTask

If the shard is split or merged with other shards, then new child shards
are created. The `BlockOnParentTask` operation ensures that
record processing for the new shards does not start until the parent shards
are completely processed by the KCL.

| Metric  | Description                                                                                          |
| ------- | ---------------------------------------------------------------------------------------------------- |
| Success | Number of successful checks for parent shard<br>completion.<br>Metric level: Summary<br>Units: Count |
| Time    | Time taken for parent shards completion.<br>Metric level: Summary<br>Unit: Milliseconds              |

#### PeriodicShardSyncManager

The `PeriodicShardSyncManager` is responsible for examining the
data streams that are being processed by the KCL consumer application,
identifying data streams with partial leases and handing them off for
synchronization.

The following metrics are available when KCL is configured to process a
single data stream (then the value of NumStreamsToSync and
NumStreamsWithPartialLeases is set to 1) and also when KCL is configured
to process multiple data streams.

| Metric                      | Description                                                                                                                                                                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NumStreamsToSync            | The number of data streams (per AWS account) being<br>processed by the consumer application that contains<br>partial leases and that must be handed off for<br>synchronization.<br>Metric level: Summary<br>Units: Count                                                                        |
| NumStreamsWithPartialLeases | The number of data streams (per AWS account) that<br>the consumer application is processing that contains<br>partial leases.<br>Metric level: Summary<br>Units: Count                                                                                                                           |
| Success                     | The number of times<br>`PeriodicShardSyncManager` was able to<br>successfully identify partial leases in the data streams<br>that the consumer application is processing.<br>Metric level: Summary<br>Units: Count                                                                              |
| Time                        | The amount of the time (in milliseconds) that the<br>`PeriodicShardSyncManager` takes to<br>examine the data streams that the consumer application<br>is processing, in order to determine which data streams<br>require shard synchronization.<br>Metric level: Summary<br>Units: Milliseconds |

#### MultistreamTracker

The `MultistreamTracker` interface enables you to build KCL
consumer applications that can process multiple data streams at the same
time.

| Metric                       | Description                                                                                                                                         |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| DeletedStreams.Count         | The number of data streams deleted at this time<br>period.<br>Metric level: Summary<br>Units: Count                                                 |
| ActiveStreams.Count          | The number of active data streams being<br>processed.<br>Metric level: Summary<br>Units: Count                                                      |
| StreamsPendingDeletion.Count | The number of data streams that are pending deletion<br>based on<br>`FormerStreamsLeasesDeletionStrategy`.<br>Metric level: Summary<br>Units: Count |

### Per-worker metrics

These metrics are aggregated across all record processors consuming data from
a Kinesis data stream, such as an Amazon EC2 instance.

###### Topics

- [WorkerMetricStatsReporter](#worker-metrics-stats "#worker-metrics-stats")
- [LeaseDiscovery](#lease-discovery "#lease-discovery")
- [RenewAllLeases](#renew-leases "#renew-leases")
- [TakeLeases](#take-leases "#take-leases")

#### WorkerMetricStatsReporter

The `WorkerMetricStatReporter` operation is responsible for
periodically publishing metrics of the current worker to the worker metrics
table. These metrics are used by the `LeaseAssignmentManager`
operation to perform lease assignments.

| Metric                             | Description                                                                                                                                            |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| InMemoryMetricStatsReporterFailure | Number of failures to capture the in-memory worker<br>metric value, due to failure of some worker<br>metrics.<br>Metric level: Summary<br>Units: Count |
| WorkerMetricStatsReporter.Time     | Time taken by the `WorkerMetricsStats`<br>operation.<br>Metric level: Summary<br>Units: Milliseconds                                                   |
| WorkerMetricStatsReporter.Success  | Number of times the `WorkerMetricsStats`<br>operation successfully completed.<br>Metric level: Summary<br>Units: Count                                 |

#### LeaseDiscovery

The `LeaseDiscovery` operation is responsible for identifying
the new leases assigned to the current worker by the
`LeaseAssignmentManager` operation. The logic for this
operation involves identifying leases assigned to the current worker by
reading the global secondary index of the lease table.

| Metric                      | Description                                                                                                                                                          |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ListLeaseKeysForWorker.Time | Time to call the global secondary index on the lease<br>table and get lease keys assigned to the current<br>worker.<br>Metric level: Detailed<br>Units: Milliseconds |
| FetchNewLeases.Time         | Time to fetch all new leases from the lease table.<br>Metric level: Detailed<br>Units: Milliseconds                                                                  |
| NewLeasesDiscovered         | Total number of new leases assigned to workers.<br>Metric level: Detailed<br>Units: Count                                                                            |
| Time                        | Time taken by the `LeaseDiscovery`<br>operation.<br>Metric level: Summary<br>Units: Milliseconds                                                                     |
| Success                     | Number of times the `LeaseDiscovery`<br>operation successfully completed.<br>Metric level: Summary<br>Units: Count                                                   |
| OwnerMismatch               | Number of owner mismatches from GSI response and lease<br>table consistent read.<br>Metric level: Detailed<br>Units: Count                                           |

#### RenewAllLeases

The `RenewAllLeases` operation periodically renews shard leases
owned by a particular worker instance.

| Metric             | Description                                                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| RenewLease.Success | Number of successful lease renewals by the<br>worker.<br>Metric level: Detailed<br>Units: Count                                                 |
| RenewLease.Time    | Time taken by the lease renewal operation.<br>Metric level: Detailed<br>Units: Milliseconds                                                     |
| CurrentLeases      | Number of shard leases owned by the worker after all<br>leases are renewed.<br>Metric level: Summary<br>Units: Count                            |
| LostLeases         | Number of shard leases that were lost following an<br>attempt to renew all leases owned by the worker.<br>Metric level: Summary<br>Units: Count |
| Success            | Number of times the lease renewal operation was<br>successful for the worker.<br>Metric level: Summary<br>Units: Count                          |
| Time               | Time taken for renewing all leases for the<br>worker.<br>Metric level: Summary<br>Units: Milliseconds                                           |

#### TakeLeases

The `TakeLeases` operation balances record processing between
all KCL workers. If the current KCL worker has fewer shard leases than
required, it takes shard leases from another worker that is
overloaded.

| Metric             | Description                                                                                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ListLeases.Success | Number of times all shard leases were successfully<br>retrieved from the KCL application DynamoDB table.<br>Metric level: Detailed<br>Units: Count   |
| ListLeases.Time    | Time taken to retrieve all shard leases from the KCL<br>application DynamoDB table.<br>Metric level: Detailed<br>Units: Milliseconds                 |
| TakeLease.Success  | Number of times the worker successfully took shard<br>leases from other KCL workers.<br>Metric level: Detailed<br>Units: Count                       |
| TakeLease.Time     | Time taken to update the lease table with leases taken<br>by the worker.<br>Metric level: Detailed<br>Units: Milliseconds                            |
| NumWorkers         | Total number of workers, as identified by a specific<br>worker.<br>Metric level: Summary<br>Units: Count                                             |
| NeededLeases       | Number of shard leases that the current worker needs<br>for a balanced shard-processing load.<br>Metric level: Detailed<br>Units: Count              |
| LeasesToTake       | Number of leases that the worker will attempt to<br>take.<br>Metric level: Detailed<br>Units: Count                                                  |
| TakenLeases        | Number of leases taken successfully by the<br>worker.<br>Metric level: Summary<br>Units: Count                                                       |
| TotalLeases        | Total number of shards that the KCL application is<br>processing.<br>Metric level: Detailed<br>Units: Count                                          |
| ExpiredLeases      | Total number of shards that are not being processed by<br>any worker, as identified by the specific worker.<br>Metric level: Summary<br>Units: Count |
| Success            | Number of times the `TakeLeases` operation<br>successfully completed.<br>Metric level: Summary<br>Units: Count                                       |
| Time               | Time taken by the `TakeLeases` operation<br>for a worker.<br>Metric level: Summary<br>Units: Milliseconds                                            |

### Per-shard metrics

These metrics are aggregated across a single record processor.

#### ProcessTask

The `ProcessTask` operation calls [GetRecords](../../../kinesis/latest/APIReference/API_GetRecords.md "../../../kinesis/latest/APIReference/API_GetRecords.md") with
the current iterator position to retrieve records from the stream and
invokes the record processor `processRecords` function.

| Metric                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| KinesisDataFetcher.getRecords.Success | Number of successful `GetRecords`<br>operations per Kinesis data stream shard.<br>Metric level: Detailed<br>Units: Count                                                                                                                                                                                                                                                                                                                                                                                      |
| KinesisDataFetcher.getRecords.Time    | Time taken per `GetRecords` operation for<br>the Kinesis data stream shard.<br>Metric level: Detailed<br>Units: Milliseconds                                                                                                                                                                                                                                                                                                                                                                                  |
| UpdateLease.Success                   | Number of successful checkpoints made by the record<br>processor for the given shard.<br>Metric level: Detailed<br>Units: Count                                                                                                                                                                                                                                                                                                                                                                               |
| UpdateLease.Time                      | Time taken for each checkpoint operation for the given<br>shard.<br>Metric level: Detailed<br>Units: Milliseconds                                                                                                                                                                                                                                                                                                                                                                                             |
| DataBytesProcessed                    | Total size of records processed in bytes on each<br>`ProcessTask` invocation.<br>Metric level: Summary<br>Units: Byte                                                                                                                                                                                                                                                                                                                                                                                         |
| RecordsProcessed                      | Number of records processed on each<br>`ProcessTask` invocation.<br>Metric level: Summary<br>Units: Count                                                                                                                                                                                                                                                                                                                                                                                                     |
| ExpiredIterator                       | Number of ExpiredIteratorException received when<br>calling `GetRecords`.<br>Metric level: Summary<br>Units: Count                                                                                                                                                                                                                                                                                                                                                                                            |
| MillisBehindLatest                    | Time that the current iterator is behind from the latest<br>record (tip) in the shard. This value is less than or equal<br>to the difference in time between the latest record in a<br>response and the current time. This is a more accurate<br>reflection of how far a shard is from the tip than comparing<br>timestamps in the last response record. This value applies<br>to the latest batch of records, not an average of all<br>timestamps in each record.Metric level:<br>SummaryUnits: Milliseconds |
| RecordProcessor.processRecords.Time   | Time taken by the record processor’s<br>`processRecords` method.<br>Metric level: Summary<br>Units: Milliseconds                                                                                                                                                                                                                                                                                                                                                                                              |
| Success                               | Number of successful process task operations.<br>Metric level: Summary<br>Units: Count                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Time                                  | Time taken for the process task operation.<br>Metric level: Summary<br>Units: Milliseconds                                                                                                                                                                                                                                                                                                                                                                                                                    |
