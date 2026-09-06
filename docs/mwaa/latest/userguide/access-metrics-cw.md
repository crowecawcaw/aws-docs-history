

# Apache Airflow environment metrics in CloudWatch
<a name="access-metrics-cw"></a>

Apache Airflow v2 and v3 are already set-up to collect and send [StatsD](https://github.com/etsy/statsd) metrics for an Amazon Managed Workflows for Apache Airflow environment to Amazon CloudWatch. The complete list of metrics Apache Airflow sends is available on the [Metrics](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html) page in the *Apache Airflow reference guide*. This page describes the Apache Airflow metrics available in CloudWatch and how to access metrics in the CloudWatch console.

**Contents**
+ [Terms](#access-metrics-cw-terms)
+ [Dimensions](#metrics-dimensions)
+ [Accessing metrics in the CloudWatch console](#access-metrics-cw-console)
+ [Apache Airflow metrics available in CloudWatch](#available-metrics-cw)
  + [Apache Airflow Counters](#counters-metrics)
  + [Apache Airflow Gauges](#gauges-metrics)
  + [Apache Airflow Timers](#timers-metrics)
+ [Choosing which metrics are reported](#choosing-metrics)
+ [What's next?](#mwaa-metrics202-next-up)

## Terms
<a name="access-metrics-cw-terms"></a>

**Namespace**  
A namespace is a container for the CloudWatch metrics of an AWS service. For Amazon MWAA, the namespace is *AmazonMWAA*.

**CloudWatch metrics**  
A CloudWatch metric represents a time-ordered set of data points that are specific to CloudWatch.

**Apache Airflow metrics**  
The [Metrics](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html ) specific to Apache Airflow.

**Dimension**  
A dimension is a name/value pair that is part of the identity of a metric.

**Unit**  
A statistic has a unit of measure. For Amazon MWAA, units include *Count*, *Seconds*, and *Milliseconds*. For Amazon MWAA, units are set based on the units in the original Airflow metrics.

## Dimensions
<a name="metrics-dimensions"></a>

This section describes the CloudWatch *Dimensions* grouping for Apache Airflow metrics in CloudWatch.


| Dimension | Description | 
| --- | --- | 
| DAG | Indicates a specific Apache Airflow DAG name. | 
| DAG Filename | Indicates a specific Apache Airflow DAG file name. | 
| Function | This dimension is used to improve the grouping of metrics in CloudWatch. | 
| Job | Indicates an Apache Airflow job run by the scheduler. Always has a value of `Job`. | 
| Operator | Indicates a specific Apache Airflow operator. | 
| Pool | Indicates a specific Apache Airflow worker pool. | 
| Task | Indicates a specific Apache Airflow task. | 
| HostName | Indicates the hostname for a specific running Apache Airflow process. | 

## Accessing metrics in the CloudWatch console
<a name="access-metrics-cw-console"></a>

This section describes how to access performance metrics in CloudWatch for a specific DAG.

**To access performance metrics for a dimension**

1. Open the [Metrics page](https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~()) on the CloudWatch console.

1. Select your AWS Region.

1. Choose the **AmazonMWAA** namespace.

1. In the **All metrics** tab, select a dimension. For example, *DAG, Environment*.

1. Choose a CloudWatch metric for a dimension. For example, *TaskInstanceSuccesses* or *TaskInstanceDuration*. Choose **Graph all search results**.

1. Choose the **Graphed metrics** tab to access performance statistics for Apache Airflow metrics, such as *DAG, Environment, Task*.

## Apache Airflow metrics available in CloudWatch
<a name="available-metrics-cw"></a>

This section describes the Apache Airflow metrics and dimensions sent to CloudWatch.

### Apache Airflow Counters
<a name="counters-metrics"></a>

The Apache Airflow metrics in this section contain data about [Apache Airflow *Counters*](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html#counters).


| CloudWatch metric | Apache Airflow metric | Unit | Dimension | 
| --- | --- | --- | --- | 
| SLAMissed Only available for Apache Airflow v2.4.3 to v2.10.3.  | sla\_missed | Count | Function, Scheduler | 
| FailedSLACallback Only available for Apache Airflow v2.4.3 to v2.10.3.  | sla\_callback\_notification\_failure | Count | Function, Scheduler | 
| Updates Available for Apache Airflow v2.6.3 and later.  | dataset.updates | Count | Function, Scheduler | 
| Orphaned Available for Apache Airflow v2.6.3 and later.  | dataset.orphaned | Count | Function, Scheduler | 
| FailedCeleryTaskExecution Available for Apache Airflow v2.4.3 and later.  | celery.execute\_command.failure | Count | Function, Celery | 
| FilePathQueueUpdateCount Available for Apache Airflow v2.6.3 and later.  | dag\_processing.file\_path\_queue\_update\_count | Count | Function, Scheduler | 
| CriticalSectionBusy | scheduler.critical\_section\_busy | Count | Function, Scheduler | 
| DagBagSize | dagbag\_size | Count | Function, DAG Processing | 
| DagCallbackExceptions | dag.callback\_exceptions | Count | DAG, All | 
| FailedSLAEmailAttempts Not available for Apache Airflow v3.0.6 and later.  | sla\_email\_notification\_failure | Count | Function, Scheduler | 
| TaskInstanceFinished | ti.finish.{dag\_id}.{task\_id}.{state} | Count | DAG, {dag\_id}<br />Task, {task\_id}<br />State, {state} | 
| JobEnd | {job\_name}\_end | Count | Job, {job\_name} | 
| JobHeartbeatFailure | {job\_name}\_heartbeat\_failure | Count | Job, {job\_name} | 
| JobStart | {job\_name}\_start | Count | Job, {job\_name} | 
| ManagerStalls | dag\_processing.manager\_stalls | Count | Function, DAG Processing | 
| OperatorFailures | operator\_failures\_{operator\_name} | Count | Operator, {operator\_name} | 
| OperatorSuccesses | operator\_successes\_{operator\_name} | Count | Operator, {operator\_name} | 
| OtherCallbackCount Available in Apache Airflow v2.6.3 and later.  | dag\_processing.other\_callback\_count | Count | Function, Scheduler | 
| Processes | dag\_processing.processes | Count | Function, DAG Processing | 
| SchedulerHeartbeat | scheduler\_heartbeat | Count | Function, Scheduler | 
| StartedTaskInstances | ti.start.{dag\_id}.{task\_id} | Count | DAG, All<br />Task, All | 
| SlaCallbackCount | dag\_processing.sla\_callback\_count Available for Apache Airflow v2.6.3 and later.  | Count | Function, Scheduler | 
| TasksKilledExternally | scheduler.tasks.killed\_externally | Count | Function, Scheduler | 
| TaskTimeoutError | celery.task\_timeout\_error | Count | Function, Celery | 
| TaskInstanceCreatedUsingOperator | task\_instance\_created-{operator\_name} | Count | Operator, {operator\_name} | 
| TaskInstancePreviouslySucceeded | previously\_succeeded | Count | DAG, All<br />Task, All | 
| TaskInstanceFailures | ti\_failures | Count | DAG, All<br />Task, All | 
| TaskInstanceSuccesses | ti\_successes | Count | DAG, All<br />Task, All | 
| TaskRemovedFromDAG | task\_removed\_from\_dag.{dag\_id} | Count | DAG, {dag\_id} | 
| TaskRestoredToDAG | task\_restored\_to\_dag.{dag\_id} | Count | DAG, {dag\_id} | 
| TriggersSucceeded Available for Apache Airflow v2.7.2 and later.  | triggers.succeeded | Count | Function, Trigger | 
| TriggersFailed Available for Apache Airflow v2.7.2 and later.  | triggers.failed | Count | Function, Trigger | 
| TriggersBlockedMainThread Available for Apache Airflow v2.7.2 and later.  | triggers.blocked\_main\_thread | Count | Function, Trigger | 
| TriggerHeartbeat Available for Apache Airflow v2.8.1 and later.  | triggerer\_heartbeat | Count | Function, Triggerer | 
| TaskInstanceCreatedUsingOperator | airflow.task\_instance\_created\_`{operator_name}` Available for Apache Airflow v2.7.2 and later.  | Count | Operator, `{operator_name}` | 
| ZombiesKilled | zombies\_killed | Count | DAG, All<br />Task, All | 

### Apache Airflow Gauges
<a name="gauges-metrics"></a>

The Apache Airflow metrics in this section contain data about [Apache Airflow *Gauges*](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html#gauges).


| CloudWatch metric | Apache Airflow metric | Unit | Dimension | 
| --- | --- | --- | --- | 
| DAGFileRefreshError | dag\_file\_refresh\_error | Count | Function, DAG Processing | 
| ImportErrors | dag\_processing.import\_errors | Count | Function, DAG Processing | 
| ExceptionFailures | smart\_sensor\_operator.exception\_failures | Count | Function, Smart Sensor Operator | 
| ExecutedTasks | smart\_sensor\_operator.executed\_tasks | Count | Function, Smart Sensor Operator | 
| InfraFailures | smart\_sensor\_operator.infra\_failures | Count | Function, Smart Sensor Operator | 
| LoadedTasks | smart\_sensor\_operator.loaded\_tasks | Count | Function, Smart Sensor Operator | 
| TotalParseTime | dag\_processing.total\_parse\_time | Seconds | Function, DAG Processing | 
| TriggeredDagRuns Available in Apache Airflow v2.6.3 and later.  | dataset.triggered\_dagruns | Count | Function, Scheduler | 
| TriggersRunning Available in Apache Airflow v2.7.2 and later.  | triggers.running.{{{hostname}}} | Count | Function, Trigger<br />HostName, {{{hostname}}} | 
| PoolDeferredSlots Available in Apache Airflow v2.7.2 and later.  | pool.deferred\_slots.`{pool_name}` | Count | Pool, {pool\_name} | 
| DAGFileProcessingLastRunSecondsAgo | dag\_processing.last\_run.seconds\_ago.{dag\_filename} | Seconds | DAG Filename, {dag\_filename} | 
| OpenSlots | executor.open\_slots | Count | Function, Executor | 
| OrphanedTasksAdopted | scheduler.orphaned\_tasks.adopted | Count | Function, Scheduler | 
| OrphanedTasksCleared | scheduler.orphaned\_tasks.cleared | Count | Function, Scheduler | 
| PokedExceptions | smart\_sensor\_operator.poked\_exception | Count | Function, Smart Sensor Operator | 
| PokedSuccess | smart\_sensor\_operator.poked\_success | Count | Function, Smart Sensor Operator | 
| PokedTasks | smart\_sensor\_operator.poked\_tasks | Count | Function, Smart Sensor Operator | 
| PoolFailures | pool.open\_slots.{pool\_name} | Count | Pool, {pool\_name} | 
| PoolStarvingTasks | pool.starving\_tasks.{pool\_name} | Count | Pool, {pool\_name} | 
| PoolOpenSlots | pool.open\_slots.{pool\_name} | Count | Pool, {pool\_name} | 
| PoolQueuedSlots | pool.queued\_slots.{pool\_name} | Count | Pool, {pool\_name} | 
| PoolRunningSlots | pool.running\_slots.{pool\_name} | Count | Pool, {pool\_name} | 
| ProcessorTimeouts | dag\_processing.processor\_timeouts | Count | Function, DAG Processing | 
| QueuedTasks | executor.queued\_tasks | Count | Function, Executor | 
| RunningTasks | executor.running\_tasks | Count | Function, Executor | 
| TasksExecutable | scheduler.tasks.executable | Count | Function, Scheduler | 
| TasksPending Does not apply to Apache Airflow v2.2 and later.  | scheduler.tasks.pending | Count | Function, Scheduler | 
| TasksRunning | scheduler.tasks.running | Count | Function, Scheduler | 
| TasksStarving | scheduler.tasks.starving | Count | Function, Scheduler | 
| TasksWithoutDagRun | scheduler.tasks.without\_dagrun | Count | Function, Scheduler | 
| DAGFileProcessingLastNumOfDbQueries Available in Apache Airflow v2.10.1 and later.  | dag\_processing.last\_num\_of\_db\_queries.{dag\_filename} | Count | DAG Filename, {dag\_filename} | 
| PoolScheduledSlots Available in Apache Airflow v2.10.1 and later.  | pool.scheduled\_slots.{pool\_name} | Count | Pool, {pool\_name} | 
| TaskCpuUsage Available in Apache Airflow v2.10.1 and later.  | cpu.usage.{dag\_id}.{task\_id} | Percent | DAG, {dag\_id}<br />Task, {task\_id} | 
| TaskMemoryUsage Available in Apache Airflow v2.10.1 and later.  | mem.usage.{dag\_id}.{task\_id} | Percent | DAG, {dag\_id}<br />Task, {task\_id} | 

### Apache Airflow Timers
<a name="timers-metrics"></a>

The Apache Airflow metrics in this section contain data about [Apache Airflow *Timers*](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html#timers).


| CloudWatch metric | Apache Airflow metric | Unit | Dimension | 
| --- | --- | --- | --- | 
| CollectDBDags | collect\_db\_dags | Milliseconds | Function, DAG Processing | 
| CriticalSectionDuration | scheduler.critical\_section\_duration | Milliseconds | Function, Scheduler | 
| CriticalSectionQueryDuration Available for Apache Airflow v2.5.1 and later.  | scheduler.critical\_section\_query\_duration | Milliseconds | Function, Scheduler | 
| DAGDependencyCheck | dagrun.dependency-check.{dag\_id} | Milliseconds | DAG, {dag\_id} | 
| DAGDurationFailed | dagrun.duration.failed.{dag\_id} | Milliseconds | DAG, {dag\_id} | 
| DAGDurationSuccess | dagrun.duration.success.{dag\_id} | Milliseconds | DAG, {dag\_id} | 
| DAGFileProcessingLastDuration | dag\_processing.last\_duration.{dag\_filename} | Seconds | DAG Filename, {dag\_filename} | 
| DAGScheduleDelay | dagrun.schedule\_delay.{dag\_id} | Milliseconds | DAG, {dag\_id} | 
| FirstTaskSchedulingDelay | dagrun.{dag\_id}.first\_task\_scheduling\_delay | Milliseconds | DAG, {dag\_id} | 
| SchedulerLoopDuration Available for Apache Airflow v2.5.1 and later.  | scheduler.scheduler\_loop\_duration | Milliseconds | Function, Scheduler | 
| TaskInstanceDuration | dag.{dag\_id}.{task\_id}.duration | Milliseconds | DAG, {dag\_id}<br />Task, {task\_id} | 
| TaskInstanceQueuedDuration | dag.`{dag_id}`.`{task_id}`.queued\_duration Available for Apache Airflow v2.7.2 and later.  | Milliseconds | DAG, {dag\_id}<br />Task, {task\_id} | 
| TaskInstanceScheduledDuration Available for Apache Airflow v2.7.2 and later.  | dag.`{dag_id}`.`{task_id}`.scheduled\_duration | Milliseconds | DAG, {dag\_id}<br />Task, {task\_id} | 

## Choosing which metrics are reported
<a name="choosing-metrics"></a>

You can choose which Apache Airflow metrics are emitted to CloudWatch, or blocked by Apache Airflow, using the following Amazon MWAA [configuration options](configuring-env-variables.md):
+ **`metrics.metrics_allow_list`** — A list of comma-separated prefixes you can use to select which metrics are emitted to CloudWatch by your environment. Use this option if you want Apache Airflow to not send all available metrics and instead select a subset of elements. For example, `scheduler,executor,dagrun`.
+ **`metrics.metrics_block_list`** — A list of comma-separated prefixes to filter out metrics that start with the elements of the list. For example, `scheduler,executor,dagrun`.

If you configure both `metrics.metrics_allow_list` and `metrics.metrics_block_list`, Apache Airflow ignores `metrics.metrics_block_list`. If you configure `metrics.metrics_block_list` but not `metrics.metrics_allow_list`, Apache Airflow filters out the elements you specify in `metrics.metrics_block_list`.

**Note**  
The `metrics.metrics_allow_list` and `metrics.metrics_block_list` configuration options only apply to Apache Airflow v2.6.3 and later. For previous version of Apache Airflow use `metrics.statsd_allow_list` and `metrics.statsd_block_list` instead.

## What's next?
<a name="mwaa-metrics202-next-up"></a>
+ Explore the Amazon MWAA API operation used to publish environment health metrics at [PublishMetrics](https://docs.aws.amazon.com/mwaa/latest/API/API_PublishMetrics.html).