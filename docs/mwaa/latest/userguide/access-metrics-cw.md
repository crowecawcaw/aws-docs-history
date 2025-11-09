# Apache Airflow environment metrics in CloudWatch

Apache Airflow v2 and v3 are already set-up to collect and send [StatsD](https://github.com/etsy/statsd "https://github.com/etsy/statsd") metrics for an Amazon Managed Workflows for Apache Airflow environment to Amazon CloudWatch.
The complete list of metrics Apache Airflow sends is available on the [Metrics](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html "https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html")
page in the _Apache Airflow reference guide_. This page describes the Apache Airflow metrics available in CloudWatch and how to access metrics in the CloudWatch console.

###### Contents

- [Terms](access-metrics-cw.md#access-metrics-cw-terms "access-metrics-cw.md#access-metrics-cw-terms")
- [Dimensions](access-metrics-cw.md#metrics-dimensions "access-metrics-cw.md#metrics-dimensions")
- [Accessing metrics in the CloudWatch console](access-metrics-cw.md#access-metrics-cw-console "access-metrics-cw.md#access-metrics-cw-console")
- [Apache Airflow metrics available in CloudWatch](access-metrics-cw.md#available-metrics-cw "access-metrics-cw.md#available-metrics-cw")
  - [Apache Airflow Counters](access-metrics-cw.md#counters-metrics "access-metrics-cw.md#counters-metrics")
  - [Apache Airflow Gauges](access-metrics-cw.md#gauges-metrics "access-metrics-cw.md#gauges-metrics")
  - [Apache Airflow Timers](access-metrics-cw.md#timers-metrics "access-metrics-cw.md#timers-metrics")

- [Choosing which metrics are reported](access-metrics-cw.md#choosing-metrics "access-metrics-cw.md#choosing-metrics")
- [What's next?](access-metrics-cw.md#mwaa-metrics202-next-up "access-metrics-cw.md#mwaa-metrics202-next-up")

## Terms

**Namespace**

A namespace is a container for the CloudWatch metrics of an AWS service. For Amazon MWAA, the namespace is _AmazonMWAA_.

**CloudWatch metrics**

A CloudWatch metric represents a time-ordered set of data points that are specific to CloudWatch.

**Apache Airflow metrics**

The [Metrics](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html "https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html ") specific to Apache Airflow.

**Dimension**

A dimension is a name/value pair that is part of the identity of a metric.

**Unit**

A statistic has a unit of measure. For Amazon MWAA, units include _Count_, _Seconds_, and _Milliseconds_. For Amazon MWAA, units are set based on the units in the original Airflow metrics.

## Dimensions

This section describes the CloudWatch _Dimensions_ grouping for Apache Airflow metrics in CloudWatch.

| Dimension    | Description                                                                        |
| ------------ | ---------------------------------------------------------------------------------- |
| DAG          | Indicates a specific Apache Airflow DAG name.                                      |
| DAG Filename | Indicates a specific Apache Airflow DAG file name.                                 |
| Function     | This dimension is used to improve the grouping of metrics in CloudWatch.           |
| Job          | Indicates an Apache Airflow job run by the scheduler. Always has a value of `Job`. |
| Operator     | Indicates a specific Apache Airflow operator.                                      |
| Pool         | Indicates a specific Apache Airflow worker pool.                                   |
| Task         | Indicates a specific Apache Airflow task.                                          |
| HostName     | Indicates the hostname for a specific running Apache Airflow process.              |

## Accessing metrics in the CloudWatch console

This section describes how to access performance metrics in CloudWatch for a specific DAG.

###### To access performance metrics for a dimension

1. Open the [Metrics page](<https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~()> "https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~()") on the CloudWatch console.
2. Select your AWS Region.
3. Choose the **AmazonMWAA** namespace.
4. In the **All metrics** tab, select a dimension. For example, _DAG, Environment_.
5. Choose a CloudWatch metric for a dimension. For example, _TaskInstanceSuccesses_ or _TaskInstanceDuration_. Choose **Graph all search results**.
6. Choose the **Graphed metrics** tab to access performance statistics for Apache Airflow metrics, such as _DAG, Environment, Task_.

## Apache Airflow metrics available in CloudWatch

This section describes the Apache Airflow metrics and dimensions sent to CloudWatch.

### Apache Airflow Counters

The Apache Airflow metrics in this section contain data about [Apache Airflow _Counters_](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html#counters "https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html#counters").

| CloudWatch metric                                                                | Apache Airflow metric                                                                                  | Unit  | Dimension                                          |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----- | -------------------------------------------------- |
| SLAMissed<br>NoteOnly available for Apache Airflow v2.4.3 to v2.10.3.            | sla_missed                                                                                             | Count | Function, Scheduler                                |
| FailedSLACallback<br>NoteOnly available for Apache Airflow v2.4.3 to v2.10.3.    | sla_callback_notification_failure                                                                      | Count | Function, Scheduler                                |
| Updates<br>NoteAvailable for Apache Airflow v2.6.3 and later.                    | dataset.updates                                                                                        | Count | Function, Scheduler                                |
| Orphaned<br>NoteAvailable for Apache Airflow v2.6.3 and later.                   | dataset.orphaned                                                                                       | Count | Function, Scheduler                                |
| FailedCeleryTaskExecution<br>NoteAvailable for Apache Airflow v2.4.3 and later.  | celery.execute_command.failure                                                                         | Count | Function, Celery                                   |
| FilePathQueueUpdateCount<br>NoteAvailable for Apache Airflow v2.6.3 and later.   | dag_processing.file_path_queue_update_count                                                            | Count | Function, Scheduler                                |
| CriticalSectionBusy                                                              | scheduler.critical_section_busy                                                                        | Count | Function, Scheduler                                |
| DagBagSize                                                                       | dagbag_size                                                                                            | Count | Function, DAG Processing                           |
| DagCallbackExceptions                                                            | dag.callback_exceptions                                                                                | Count | DAG, All                                           |
| FailedSLAEmailAttempts<br>NoteNot available for Apache Airflow v3.0.6 and later. | sla_email_notification_failure                                                                         | Count | Function, Scheduler                                |
| TaskInstanceFinished                                                             | ti.finish.{dag_id}.{task_id}.{state}                                                                   | Count | DAG, {dag_id}<br>Task, {task_id}<br>State, {state} |
| JobEnd                                                                           | {job_name}\_end                                                                                        | Count | Job, {job_name}                                    |
| JobHeartbeatFailure                                                              | {job_name}\_heartbeat_failure                                                                          | Count | Job, {job_name}                                    |
| JobStart                                                                         | {job_name}\_start                                                                                      | Count | Job, {job_name}                                    |
| ManagerStalls                                                                    | dag_processing.manager_stalls                                                                          | Count | Function, DAG Processing                           |
| OperatorFailures                                                                 | operator_failures\_{operator_name}                                                                     | Count | Operator, {operator_name}                          |
| OperatorSuccesses                                                                | operator_successes\_{operator_name}                                                                    | Count | Operator, {operator_name}                          |
| OtherCallbackCount<br>NoteAvailable in Apache Airflow v2.6.3 and later.          | dag_processing.other_callback_count                                                                    | Count | Function, Scheduler                                |
| Processes                                                                        | dag_processing.processes                                                                               | Count | Function, DAG Processing                           |
| SchedulerHeartbeat                                                               | scheduler_heartbeat                                                                                    | Count | Function, Scheduler                                |
| StartedTaskInstances                                                             | ti.start.{dag_id}.{task_id}                                                                            | Count | DAG, All<br>Task, All                              |
| SlaCallbackCount                                                                 | dag_processing.sla_callback_count<br>NoteAvailable for Apache Airflow v2.6.3 and later.                | Count | Function, Scheduler                                |
| TasksKilledExternally                                                            | scheduler.tasks.killed_externally                                                                      | Count | Function, Scheduler                                |
| TaskTimeoutError                                                                 | celery.task_timeout_error                                                                              | Count | Function, Celery                                   |
| TaskInstanceCreatedUsingOperator                                                 | task_instance_created-{operator_name}                                                                  | Count | Operator, {operator_name}                          |
| TaskInstancePreviouslySucceeded                                                  | previously_succeeded                                                                                   | Count | DAG, All<br>Task, All                              |
| TaskInstanceFailures                                                             | ti_failures                                                                                            | Count | DAG, All<br>Task, All                              |
| TaskInstanceSuccesses                                                            | ti_successes                                                                                           | Count | DAG, All<br>Task, All                              |
| TaskRemovedFromDAG                                                               | task_removed_from_dag.{dag_id}                                                                         | Count | DAG, {dag_id}                                      |
| TaskRestoredToDAG                                                                | task_restored_to_dag.{dag_id}                                                                          | Count | DAG, {dag_id}                                      |
| TriggersSucceeded<br>NoteAvailable for Apache Airflow v2.7.2 and later.          | triggers.succeeded                                                                                     | Count | Function, Trigger                                  |
| TriggersFailed<br>NoteAvailable for Apache Airflow v2.7.2 and later.             | triggers.failed                                                                                        | Count | Function, Trigger                                  |
| TriggersBlockedMainThread<br>NoteAvailable for Apache Airflow v2.7.2 and later.  | triggers.blocked_main_thread                                                                           | Count | Function, Trigger                                  |
| TriggerHeartbeat<br>NoteAvailable for Apache Airflow v2.8.1 and later.           | triggerer_heartbeat                                                                                    | Count | Function, Triggerer                                |
| TaskInstanceCreatedUsingOperator                                                 | airflow.task_instance_created\_`{operator_name}`<br>NoteAvailable for Apache Airflow v2.7.2 and later. | Count | Operator, `{operator_name}`                        |
| ZombiesKilled                                                                    | zombies_killed                                                                                         | Count | DAG, All<br>Task, All                              |

### Apache Airflow Gauges

The Apache Airflow metrics in this section contain data about [Apache Airflow _Gauges_](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html#gauges "https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html#gauges").

| CloudWatch metric                                                                         | Apache Airflow metric                                | Unit    | Dimension                                   |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------- | ------------------------------------------- |
| DAGFileRefreshError                                                                       | dag_file_refresh_error                               | Count   | Function, DAG Processing                    |
| ImportErrors                                                                              | dag_processing.import_errors                         | Count   | Function, DAG Processing                    |
| ExceptionFailures                                                                         | smart_sensor_operator.exception_failures             | Count   | Function, Smart Sensor Operator             |
| ExecutedTasks                                                                             | smart_sensor_operator.executed_tasks                 | Count   | Function, Smart Sensor Operator             |
| InfraFailures                                                                             | smart_sensor_operator.infra_failures                 | Count   | Function, Smart Sensor Operator             |
| LoadedTasks                                                                               | smart_sensor_operator.loaded_tasks                   | Count   | Function, Smart Sensor Operator             |
| TotalParseTime                                                                            | dag_processing.total_parse_time                      | Seconds | Function, DAG Processing                    |
| TriggeredDagRuns<br>NoteAvailable in Apache Airflow v2.6.3 and later.                     | dataset.triggered_dagruns                            | Count   | Function, Scheduler                         |
| TriggersRunning<br>NoteAvailable in Apache Airflow v2.7.2 and later.                      | triggers.running.`{hostname}`                        | Count   | Function, Trigger<br>HostName, `{hostname}` |
| PoolDeferredSlots<br>NoteAvailable in Apache Airflow v2.7.2 and later.                    | pool.deferred_slots.`{pool_name}`                    | Count   | Pool, {pool_name}                           |
| DAGFileProcessingLastRunSecondsAgo                                                        | dag_processing.last_run.seconds_ago.{dag_filename}   | Seconds | DAG Filename, {dag_filename}                |
| OpenSlots                                                                                 | executor.open_slots                                  | Count   | Function, Executor                          |
| OrphanedTasksAdopted                                                                      | scheduler.orphaned_tasks.adopted                     | Count   | Function, Scheduler                         |
| OrphanedTasksCleared                                                                      | scheduler.orphaned_tasks.cleared                     | Count   | Function, Scheduler                         |
| PokedExceptions                                                                           | smart_sensor_operator.poked_exception                | Count   | Function, Smart Sensor Operator             |
| PokedSuccess                                                                              | smart_sensor_operator.poked_success                  | Count   | Function, Smart Sensor Operator             |
| PokedTasks                                                                                | smart_sensor_operator.poked_tasks                    | Count   | Function, Smart Sensor Operator             |
| PoolFailures                                                                              | pool.open_slots.{pool_name}                          | Count   | Pool, {pool_name}                           |
| PoolStarvingTasks                                                                         | pool.starving_tasks.{pool_name}                      | Count   | Pool, {pool_name}                           |
| PoolOpenSlots                                                                             | pool.open_slots.{pool_name}                          | Count   | Pool, {pool_name}                           |
| PoolQueuedSlots                                                                           | pool.queued_slots.{pool_name}                        | Count   | Pool, {pool_name}                           |
| PoolRunningSlots                                                                          | pool.running_slots.{pool_name}                       | Count   | Pool, {pool_name}                           |
| ProcessorTimeouts                                                                         | dag_processing.processor_timeouts                    | Count   | Function, DAG Processing                    |
| QueuedTasks                                                                               | executor.queued_tasks                                | Count   | Function, Executor                          |
| RunningTasks                                                                              | executor.running_tasks                               | Count   | Function, Executor                          |
| TasksExecutable                                                                           | scheduler.tasks.executable                           | Count   | Function, Scheduler                         |
| TasksPending<br>NoteDoes not apply to Apache Airflow v2.2 and later.                      | scheduler.tasks.pending                              | Count   | Function, Scheduler                         |
| TasksRunning                                                                              | scheduler.tasks.running                              | Count   | Function, Scheduler                         |
| TasksStarving                                                                             | scheduler.tasks.starving                             | Count   | Function, Scheduler                         |
| TasksWithoutDagRun                                                                        | scheduler.tasks.without_dagrun                       | Count   | Function, Scheduler                         |
| DAGFileProcessingLastNumOfDbQueries<br>NoteAvailable in Apache Airflow v2.10.1 and later. | dag_processing.last_num_of_db_queries.{dag_filename} | Count   | DAG Filename, {dag_filename}                |
| PoolScheduledSlots<br>NoteAvailable in Apache Airflow v2.10.1 and later.                  | pool.scheduled_slots.{pool_name}                     | Count   | Pool, {pool_name}                           |
| TaskCpuUsage<br>NoteAvailable in Apache Airflow v2.10.1 and later.                        | cpu.usage.{dag_id}.{task_id}                         | Percent | DAG, {dag_id}<br>Task, {task_id}            |
| TaskMemoryUsage<br>NoteAvailable in Apache Airflow v2.10.1 and later.                     | mem.usage.{dag_id}.{task_id}                         | Percent | DAG, {dag_id}<br>Task, {task_id}            |

### Apache Airflow Timers

The Apache Airflow metrics in this section contain data about [Apache Airflow _Timers_](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html#timers "https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html#timers").

| CloudWatch metric                                                                   | Apache Airflow metric                                                                            | Unit         | Dimension                        |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------ | -------------------------------- |
| CollectDBDags                                                                       | collect_db_dags                                                                                  | Milliseconds | Function, DAG Processing         |
| CriticalSectionDuration                                                             | scheduler.critical_section_duration                                                              | Milliseconds | Function, Scheduler              |
| CriticalSectionQueryDuration<br>NoteAvailable for Apache Airflow v2.5.1 and later.  | scheduler.critical_section_query_duration                                                        | Milliseconds | Function, Scheduler              |
| DAGDependencyCheck                                                                  | dagrun.dependency-check.{dag_id}                                                                 | Milliseconds | DAG, {dag_id}                    |
| DAGDurationFailed                                                                   | dagrun.duration.failed.{dag_id}                                                                  | Milliseconds | DAG, {dag_id}                    |
| DAGDurationSuccess                                                                  | dagrun.duration.success.{dag_id}                                                                 | Milliseconds | DAG, {dag_id}                    |
| DAGFileProcessingLastDuration                                                       | dag_processing.last_duration.{dag_filename}                                                      | Seconds      | DAG Filename, {dag_filename}     |
| DAGScheduleDelay                                                                    | dagrun.schedule_delay.{dag_id}                                                                   | Milliseconds | DAG, {dag_id}                    |
| FirstTaskSchedulingDelay                                                            | dagrun.{dag_id}.first_task_scheduling_delay                                                      | Milliseconds | DAG, {dag_id}                    |
| SchedulerLoopDuration<br>NoteAvailable for Apache Airflow v2.5.1 and later.         | scheduler.scheduler_loop_duration                                                                | Milliseconds | Function, Scheduler              |
| TaskInstanceDuration                                                                | dag.{dag_id}.{task_id}.duration                                                                  | Milliseconds | DAG, {dag_id}<br>Task, {task_id} |
| TaskInstanceQueuedDuration                                                          | dag.`{dag_id}`.`{task_id}`.queued_duration<br>NoteAvailable for Apache Airflow v2.7.2 and later. | Milliseconds | DAG, {dag_id}<br>Task, {task_id} |
| TaskInstanceScheduledDuration<br>NoteAvailable for Apache Airflow v2.7.2 and later. | dag.`{dag_id}`.`{task_id}`.scheduled_duration                                                    | Milliseconds | DAG, {dag_id}<br>Task, {task_id} |

## Choosing which metrics are reported

You can choose which Apache Airflow metrics are emitted to CloudWatch, or blocked by Apache Airflow, using the following Amazon MWAA [configuration options](configuring-env-variables.md "configuring-env-variables.md"):

- **`metrics.metrics_allow_list`** — A list of comma-separated prefixes you can use to select which metrics are emitted to CloudWatch by your environment. Use this option if you want Apache Airflow to not send all available metrics and instead select a subset of elements.
  For example, `scheduler,executor,dagrun`.
- **`metrics.metrics_block_list`** — A list of comma-separated prefixes to filter out metrics that start with the elements of the list. For example, `scheduler,executor,dagrun`.

If you configure both `metrics.metrics_allow_list` and `metrics.metrics_block_list`, Apache Airflow ignores `metrics.metrics_block_list`. If you configure `metrics.metrics_block_list` but not `metrics.metrics_allow_list`, Apache Airflow
filters out the elements you specify in `metrics.metrics_block_list`.

###### Note

The `metrics.metrics_allow_list` and `metrics.metrics_block_list` configuration options only apply to Apache Airflow v2.6.3 and later. For previous version of Apache Airflow use `metrics.statsd_allow_list` and `metrics.statsd_block_list` instead.

## What's next?

- Explore the Amazon MWAA API operation used to publish environment health metrics at
  [PublishMetrics](../API/API_PublishMetrics.md "../API/API_PublishMetrics.md").
