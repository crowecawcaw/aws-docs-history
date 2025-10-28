# IPC:parallel wait events

The following `IPC:parallel wait events` indicate that a session is waiting for
inter-process communication related to parallel query execution operations.

- `IPC:BgWorkerStartup` - A process is waiting for a parallel worker process to
  complete its startup sequence. This happens when initializing workers for parallel
  query execution.
- `IPC:BgWorkerShutdown` - A process is waiting for a parallel worker process to
  complete its shutdown sequence. This occurs during the cleanup phase of parallel
  query execution.
- `IPC:ExecuteGather` - A process is waiting to receive data from parallel worker
  processes during query execution. This occurs when the leader process needs to
  gather results from its workers.
- `IPC:ParallelFinish` - A process is waiting for parallel workers to finish their
  execution and report their final results. This happens during the completion phase
  of parallel query execution.

###### Topics

- [Supported engine versions](#rpg-ipc-parallel-context-supported "#rpg-ipc-parallel-context-supported")
- [Context](#rpg-ipc-parallel-context "#rpg-ipc-parallel-context")
- [Likely causes of increased waits](#rpg-ipc-parallel-causes "#rpg-ipc-parallel-causes")
- [Actions](#rpg-ipc-parallel-actions "#rpg-ipc-parallel-actions")

## Supported engine versions

This wait event information is supported for all versions of Aurora PostgreSQL.

## Context

Parallel query execution in PostgreSQL involves multiple processes working together to
process a single query. When a query is determined to be suitable for parallelization, a
leader process coordinates with one or more parallel worker processes based on the
`max_parallel_workers_per_gather` parameter setting. The leader process
divides the work among workers, each worker processes its portion of data independently,
and results are gathered back to the leader process.

###### Note

Each parallel worker operates as a separate process with resource requirements
similar to a full user session. This means a parallel query with 4 workers can
consume up to 5 times the resources (CPU, memory, I/O bandwidth) compared to a
non-parallel query, as both the leader process and each worker process maintain
their own resource allocations. For instance, settings like `work_mem`
are applied individually to each worker, potentially multiplying the total memory
usage across all processes.

The parallel query architecture consists of three main components:

- Leader process: The main process that initiates the parallel operation,
  divides the workload, and coordinates with worker processes.
- Worker processes: Background processes that execute portions of the query in
  parallel.
- Gather/Gather merge: Operations that combine results from multiple worker
  processes back to the leader

During parallel execution, processes need to communicate with each other through
Inter-Process Communication (IPC) mechanisms. These IPC wait events occur during
different phases:

- Worker startup: When parallel workers are being initialized
- Data exchange: When workers are processing data and sending results to the
  leader
- Worker shutdown: When parallel execution completes and workers are being
  terminated
- Synchronization points: When processes need to coordinate or wait for other
  processes to complete their tasks

Understanding these wait events is crucial for diagnosing performance issues related
to parallel query execution, especially in high-concurrency environments where multiple
parallel queries may be executing simultaneously.

## Likely causes of increased waits

Several factors can contribute to an increase in parallel-related IPC wait
events:

**High concurrency of parallel queries**

When many parallel queries are running simultaneously, it can lead to
resource contention and increased waiting times for IPC operations. This is
particularly common in systems with high transaction volumes or analytical
workloads.

**Suboptimal parallel query plans**

If the query planner chooses inefficient parallel plans, it may result in
unnecessary parallelization or poor work distribution among workers. This
can lead to increased IPC waits, especially for `IPC:ExecuteGather` and
`IPC:ParallelFinish` events. These planning issues often stem from outdated
statistics and table/index bloat.

**Frequent startup and shutdown of parallel workers**

Short-lived queries that frequently initiate and terminate parallel
workers can cause an increase in `IPC:BgWorkerStartup` and
`IPC:BgWorkerShutdown` events. This is often seen in OLTP workloads with many
small, parallelizable queries.

**Resource constraints**

Limited CPU, memory, or I/O capacity can cause bottlenecks in parallel
execution, leading to increased wait times across all IPC events. For
example, if CPU is saturated, worker processes may take longer to start up
or process their portion of work.

**Complex query structures**

Queries with multiple levels of parallelism (e.g., parallel joins followed
by parallel aggregations) can lead to more complex IPC patterns and
potentially increased wait times, especially for `IPC:ExecuteGather`
events.

**Large result sets**

Queries that produce large result sets may cause increased
`IPC:ExecuteGather` wait times as the leader process spends more time
collecting and processing results from worker processes.

Understanding these factors can help in diagnosing and addressing performance issues
related to parallel query execution in Aurora PostgreSQL.

## Actions

When you see waits related to parallel query, it typically means that a backend
process is coordinating or waiting on parallel worker processes. These waits are common
during execution of parallel plans. You can investigate and mitigate the impact of these
waits by monitoring parallel worker usage, reviewing the parameter settings, and tuning
query execution and resource allocation.

###### Topics

- [Analyze query plans for inefficient
  parallelism](#rpg-ipc-parallel-analyze-plans "#rpg-ipc-parallel-analyze-plans")
- [Monitor parallel query usage](#rpg-ipc-parallel-monitor "#rpg-ipc-parallel-monitor")
- [Review and adjust parallel query
  settings](#rpg-ipc-parallel-adjust-settings "#rpg-ipc-parallel-adjust-settings")
- [Optimize resource
  allocation](#rpg-ipc-parallel-optimize-resources "#rpg-ipc-parallel-optimize-resources")
- [Investigate connection
  management](#rpg-ipc-parallel-connection-management "#rpg-ipc-parallel-connection-management")
- [Review and optimize maintenance
  operations](#rpg-ipc-parallel-maintenance "#rpg-ipc-parallel-maintenance")

### Analyze query plans for inefficient

parallelism

Parallel query execution can often lead to system instability, CPU spikes, and
unpredictable query performance variance. It's crucial to thoroughly analyze whether
parallelism actually improves your specific workload. Use EXPLAIN ANALYZE to review
parallel query execution plans.

Temporarily disable parallelism at the session level to compare plan
efficiency:

```

SET max_parallel_workers_per_gather = 0;
EXPLAIN ANALYZE <your_query>;

```

Re-enable parallelism and compare:

```

RESET max_parallel_workers_per_gather;
EXPLAIN ANALYZE <your_query>;

```

If disabling parallelism yields better or more consistent results, consider
disabling it for specific queries at the session level using SET commands. For a
broader impact, you might want to disable parallelism at the instance level by
adjusting the relevant parameters in your DB parameter group.
For more information, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Monitor parallel query usage

Use the following queries to gain visibility into parallel query activity and
capacity:

Check active parallel worker processes:

```

SELECT
    COUNT(*)
FROM
    pg_stat_activity
WHERE
    backend_type = 'parallel worker';

```

This query shows the number of active parallel worker processes. A high value may
indicate that your `max\_parallel\_workers` is configured with a high value and you
might want to consider reducing it.

Check concurrent parallel queries:

```

SELECT
    COUNT(DISTINCT leader_pid)
FROM
    pg_stat_activity
WHERE
    leader_pid IS NOT NULL;

```

This query returns the number of distinct leader processes that have launched
parallel queries. A high number here indicates that multiple sessions are running
parallel queries concurrently, which can increase demand on CPU and memory.

### Review and adjust parallel query

settings

Review the following parameters to ensure they align with your workload:

- `max_parallel_workers`: Total number of parallel workers across
  all sessions.
- `max_parallel_workers_per_gather`: Max workers per
  query.

For OLAP workloads, increasing these values can improve performance. For OLTP
workloads, lower values are generally preferred.

```

SHOW max_parallel_workers;
SHOW max_parallel_workers_per_gather;

```

### Optimize resource

allocation

Monitor CPU utilization and consider adjusting the number of vCPUs if consistently
high and if your application benefits from parallel queries. Ensure adequate memory
is available for parallel operations.

- Use Performance Insights metrics to determine if the system is
  CPU-bound.
- Each parallel worker uses its own `work_mem`. Ensure total
  memory usage is within instance limits.

The parallel queries may consume very substantially more resources than
non-parallel queries, because each worker process is a completely separate process
which has roughly the same impact on the system as an additional user session. This
should be taken into account when choosing a value for this setting, as well as when
configuring other settings that control resource utilization, such as
`work_mem`. For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM "https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM"). Resource limits such as `work_mem`
are applied individually to each worker, which means the total utilization may be
much higher across all processes than it would normally be for any single
process.

Consider increasing vCPUs or tuning memory parameters if your workload is heavily
parallelized.

### Investigate connection

management

If experiencing connection exhaustion, review application connection pooling
strategies. Consider implementing connection pooling at the application level if not
already in use.

### Review and optimize maintenance

operations

Coordinate index creation and other maintenance tasks to prevent resource
contention. Consider scheduling these operations during off-peak hours. Avoid
scheduling heavy maintenance (e.g., parallel index builds) during periods of high
user query load. These operations can consume parallel workers and impact
performance for regular queries.
