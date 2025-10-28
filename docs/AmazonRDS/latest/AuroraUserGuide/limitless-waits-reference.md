# Limitless Database wait events

The following wait events apply to Aurora PostgreSQL Limitless Database. You can monitor these wait events to identify bottlenecks in Aurora PostgreSQL Limitless Database processing.

###### Topics

- [IO:TwophaseFilePoolWrite wait event](#limitless-waits-TwophaseFilePoolWrite "#limitless-waits-TwophaseFilePoolWrite")
- [IO:TwophaseFilePoolRead wait event](#limitless-waits-TwophaseFilePoolRead "#limitless-waits-TwophaseFilePoolRead")
- [AuroraLimitless:Connect wait event](#limitless-waits-Connect "#limitless-waits-Connect")
- [AuroraLimitless:AsyncConnect wait event](#limitless-waits-AsyncConnect "#limitless-waits-AsyncConnect")
- [AuroraLimitless:RemoteStatementSetup wait event](#limitless-waits-RemoteStatementSetup "#limitless-waits-RemoteStatementSetup")
- [AuroraLimitless:RemoteDDLExecution wait event](#limitless-waits-RemoteDDLExecution "#limitless-waits-RemoteDDLExecution")
- [AuroraLimitless:RemoteStatementExecution wait event](#limitless-waits-RemoteStatementExecution "#limitless-waits-RemoteStatementExecution")
- [AuroraLimitless:FetchRemoteResults wait event](#limitless-waits-FetchRemoteResults "#limitless-waits-FetchRemoteResults")
- [AuroraLimitless:AsyncGetInitialResponse wait event](#limitless-waits-AsyncGetInitialResponse "#limitless-waits-AsyncGetInitialResponse")
- [AuroraLimitless:AsyncGetNextResponse wait event](#limitless-waits-AsyncGetNextResponse "#limitless-waits-AsyncGetNextResponse")
- [AuroraLimitless:AbortedCommandCleanup wait event](#limitless-waits-AbortedCommandCleanup "#limitless-waits-AbortedCommandCleanup")
- [AuroraLimitless:DistributedCommitPrepare wait event](#limitless-waits-DistributedCommitPrepare "#limitless-waits-DistributedCommitPrepare")
- [AuroraLimitless:DistributedCommit wait event](#limitless-waits-DistributedCommit "#limitless-waits-DistributedCommit")
- [AuroraLimitless:DistributedCommitPrepareThrottle wait event](#limitless-waits-DistributedCommitPrepareThrottle "#limitless-waits-DistributedCommitPrepareThrottle")
- [AuroraLimitless:PreparedTransactionResolution wait event](#limitless-waits-PreparedTransactionResolution "#limitless-waits-PreparedTransactionResolution")
- [AuroraLimitless:SendPreparedTransactionOutcome wait event](#limitless-waits-SendPreparedTransactionOutcome "#limitless-waits-SendPreparedTransactionOutcome")
- [AuroraLimitless:CommitClockBarrier wait event](#limitless-waits-CommitClockBarrier "#limitless-waits-CommitClockBarrier")
- [AuroraLimitless:SnapshotClockBarrier wait event](#limitless-waits-SnapshotClockBarrier "#limitless-waits-SnapshotClockBarrier")
- [AuroraLimitless:ReaderSnapshotClockBarrier wait event](#limitless-waits-ReaderSnapshotClockBarrier "#limitless-waits-ReaderSnapshotClockBarrier")
- [AuroraLimitless:GatherDistributedDeadlockGraph wait event](#limitless-waits-GatherDistributedDeadlockGraph "#limitless-waits-GatherDistributedDeadlockGraph")
- [AuroraLimitless:DistributedDeadlockDetection wait event](#limitless-waits-DistributedDeadlockDetection "#limitless-waits-DistributedDeadlockDetection")
- [AuroraLimitless:DistributedDeadlockAbort wait event](#limitless-waits-DistributedDeadlockAbort "#limitless-waits-DistributedDeadlockAbort")
- [AuroraLimitless:GatherRemoteStats wait event](#limitless-waits-GatherRemoteStats "#limitless-waits-GatherRemoteStats")
- [AuroraLimitless:GlobalSequenceRefresh wait event](#limitless-waits-GlobalSequenceRefresh "#limitless-waits-GlobalSequenceRefresh")
- [AuroraLimitless:GlobalVacuumTimeExchange wait event](#limitless-waits-GlobalVacuumTimeExchange "#limitless-waits-GlobalVacuumTimeExchange")
- [AuroraLimitless:DistributedTransactionMonitorGather wait event](#limitless-waits-DistributedTransactionMonitorGather "#limitless-waits-DistributedTransactionMonitorGather")
- [AuroraLimitlessActivity:AdminTaskSchedulerMain wait event](#limitless-waits-AdminTaskSchedulerMain "#limitless-waits-AdminTaskSchedulerMain")
- [AuroraLimitlessActivity:AdminTaskExecutorMain wait event](#limitless-waits-AdminTaskExecutorMain "#limitless-waits-AdminTaskExecutorMain")
- [AuroraLimitlessActivity:AdminTaskMonitorMain wait event](#limitless-waits-AdminTaskMonitorMain "#limitless-waits-AdminTaskMonitorMain")
- [AuroraLimitlessActivity:DatabaseCleanupMonitorMain wait event](#limitless-waits-DatabaseCleanupMonitorMain "#limitless-waits-DatabaseCleanupMonitorMain")
- [AuroraLimitlessActivity:TopologyCleanupMonitorMain wait event](#limitless-waits-TopologyCleanupMonitorMain "#limitless-waits-TopologyCleanupMonitorMain")
- [AuroraLimitlessActivity:ToplogyChangeMonitorMain wait event](#limitless-waits-ToplogyChangeMonitorMain "#limitless-waits-ToplogyChangeMonitorMain")
- [AuroraLimitlessActivity:DistributedTransactionMonitorMain wait event](#limitless-waits-DistributedTransactionMonitorMain "#limitless-waits-DistributedTransactionMonitorMain")
- [AuroraLimitlessActivity:GlobalVacuumMonitorMain wait event](#limitless-waits-GlobalVacuumMonitorMain "#limitless-waits-GlobalVacuumMonitorMain")

## IO:TwophaseFilePoolWrite wait event

Waiting for a write of a two-phase state file within the two-phase state file pool. This is an Aurora specific event.

### Causes

Processes executing a `PREPARED TRANSACTION` command, including participants in a Limitless Database distributed transaction, must persist transaction state in a two-phase file. Aurora uses a file pool to improve performance of this operation.

### Action

This is a synchronous write I/O operation and therefore a high latency in this event has similar causes to `IO:XactSync` and can be investigated in the same way. If using Limitless Database, you might need to reduce the number of distributed transactions being executed.

## IO:TwophaseFilePoolRead wait event

Waiting for a read of a two-phase state file within the two-phase state file pool.

### Causes

Processes executing a `COMMIT PREPARED` command against a previously prepared transaction, including participants in a Limitless Database distributed transaction, might need to read previosly persisted transaction state from a two-phase file. Aurora uses a file pool to improve performance of this operation.

### Action

This is a read I/O operation. Therefore, a high latency in this event has similar causes to `IO:DataFileRead` and can be investigated the same. If using Limitless Database, you might need to reduce the number of distributed transactions being executed.

## AuroraLimitless:Connect wait event

The process is waiting for a connection to another node in the cluster to be established.

### Causes

Connections are established between processes and remote nodes to execute queries, distributed transactions, and perform DDLs.

### Action

Reduce the number of simultaneous connections to the cluster or tune the use of cross-shard queries.

## AuroraLimitless:AsyncConnect wait event

This event is similar to `Connect`, but represents a process waiting for parallel connections to a set of nodes to be established.

### Causes

Parallel connection establishment is most commonly done when executing DDL statements.

### Action

Reduce the number of DDL statements or combine multiple DDLs in the same session to improve connection reuse.

## AuroraLimitless:RemoteStatementSetup wait event

The process is waiting for remote query execution setup, such as cursor open, close, or prepared statement creation.

### Causes

This wait event increases with the number of scans on sharded tables where the statement could not be single-shard optimized.

### Action

Optimize queries to reduce the number of scan operations or increase eligibility for single-shard optimization.

## AuroraLimitless:RemoteDDLExecution wait event

The process is waiting for a remote DDL command to finish.

### Causes

When you issue a DDL command on a DB shard group, it must be distributed to other router and shard nodes before confirming the operation. Some DDL operations can run for a long time, because data must be adapted to schema changes.

### Action

Identify long-running DDL commands so that you can optimize them.

## AuroraLimitless:RemoteStatementExecution wait event

A process is waiting for a remote command to finish.

### Causes

A SQL command is running on a remote node. This event will appear frequently for internal communications, such as `auto_analyze` and heartbeat checks.

### Action

Idenfify long-running commands using the limitless_stat_statements view. In many cases this is an expected event, especially for background workers or internal processes and no action is needed.

## AuroraLimitless:FetchRemoteResults wait event

A process is waiting to retrieve rows from a remote node.

### Causes

This wait event can increase when fetching a large number of rows from a remote table, such as a sharded or reference table.

### Action

Identify unoptimized `SELECT` queries using the `limitless_stat_statements` view. Optimize queries to retrieve only necessary data. You can also tune the `rds_aurora.limitless_maximum_adaptive_fetch_size` parameter.

## AuroraLimitless:AsyncGetInitialResponse wait event

The process is waiting for an initial response when pipeline mode is used in query execution.

### Causes

This will typically be seen during router to shard execution for queries with single-shard data placement and is an expected part of normal execution.

### Action

No further action is required.

## AuroraLimitless:AsyncGetNextResponse wait event

The process is waiting for an additional responses when pipeline mode is used in query execution.

### Causes

This will typically be seen during router to shard execution for queries with single-shard data placement and is an expected part of normal execution.

### Action

No further action is required.

## AuroraLimitless:AbortedCommandCleanup wait event

The process is waiting for the result of a remote cleanup query. Cleanup queries are issued to shard nodes to return them to an appropriate state when a distributed transaction is ended.

### Causes

Transaction cleanup is done when a transaction is aborted either because an error was found or because an user issued an explicit ABORT command or canceled the running query.

### Action

Investigate the cause for the transaction being canceled.

## AuroraLimitless:DistributedCommitPrepare wait event

The process is committing a distributed transaction and is waiting for all the participants to acknowledge the prepare command.

### Causes

Transactions that modify multiple nodes must perform a distributed commit. A long wait in `DistributedCommitPrepare` could be caused by long waits in the `IO:TwophaseFilePoolWrite` event on participating nodes.

### Action

Reduce the number of transactions that modify data on multiple nodes. Investigate `IO:TwophaseFilePoolWrite` events in other nodes of the cluster.

## AuroraLimitless:DistributedCommit wait event

The process is committing a distributed transaction and is waiting for the lead participant to acknowledge the commit command.

### Causes

Transactions that modify multiple nodes must perform a distributed commit. A long wait in `DistributedCommit` could be caused by long waits in the `IO:XactSync` event on the lead participant.

### Action

Reduce the number of transactions that modify data on multiple nodes. Investigate `IO:XactSync` events in other nodes of the cluster.

## AuroraLimitless:DistributedCommitPrepareThrottle wait event

The process is attempting to prepare a distributed transaction and is being throttled to due to existing prepared transactions.

### Causes

Transactions that modify multiple nodes must perform a distributed commit. Participants in these transactions must perform a prepare operation as part of the commit protocol. Aurora limits the number of concurrent prepares, and if this limit is exceeded the process will wait in the `DistributedCommitPrepareThrottle` event.

### Action

Reduce the number of transactions that modify data on multiple nodes. Investigate `IO:TwophaseFilePoolWrite` events as increased time in those events could cause existing prepared transactions to build up, resulting in throttling for new prepare attempts.

## AuroraLimitless:PreparedTransactionResolution wait event

The process has encountered a tuple modified by a distributed transaction that is in the prepared state. The process must determine if the distributed transaction will become visible in its snapshot.

### Causes

Transactions that modify multiple nodes must perform a distributed commit which includes a prepare phase. A high number of distributed transactions or increased latency on distributed commits can cause other processes to encounter the `PreparedTransactionResolution` wait event.

### Action

Reduce the number of transactions that modify data on multiple nodes. Investigate distributed commit related events as increased time in those events could increase latency in the commit path of distributed transactions. You might also wish to investigate network and CPU loads.

## AuroraLimitless:SendPreparedTransactionOutcome wait event

The process is executing on a node that is coordinating a distributed transaction and another process has inquired as to the state of that transaction, or the process has committed a distributed transaction and is sending the outcome to participants.

### Causes

Processes that encounter the `PreparedTransactionResolution` wait event will query the transaction coordinator. The response on the transaction coordinator will ecounter SendPreparedTransactionOutcome.

### Action

Reduce the number of transactions that modify data on multiple nodes. Investigate distributed commit related events and `IO:TwophaseFilePoolWrite` and `IO:TwophaseFilePoolRead` events as those events could increase latency in the commit path of distributed transactions. You might also wish to investigate network and CPU loads.

## AuroraLimitless:CommitClockBarrier wait event

The process is committing a transaction and must wait to ensure that the assigned commit time is guaranteed to be in the past for all nodes in the cluster.

### Causes

CPU or network staturation could cause increased clock drift, resulting in time spent in this wait event.

### Action

Investigate CPU or network saturation in your cluster.

## AuroraLimitless:SnapshotClockBarrier wait event

The process has received a snapshot time from another node with a clock in the future and is waiting for its own clock to reach that time.

### Causes

This typically occurs after the process has received results from a function that was pushed down to a shard and there is clock drift between the nodes. CPU or network staturation could cause increased clock drift, resulting in time spent in this wait event.

### Action

Investigate CPU or network staturation in your cluster.

## AuroraLimitless:ReaderSnapshotClockBarrier wait event

This event occurs on read nodes. The process is waiting for the read node to replay the write stream so that all writes that happened before the process snapshot time have been applied.

### Causes

An increase in Aurora replica lag can cause increased wait time in this event.

### Action

Investigate Aurora replica lag.

## AuroraLimitless:GatherDistributedDeadlockGraph wait event

The process is communicating with other nodes to collect lock graphs as part of distributed deadlock detection.

### Causes

When a process is waiting on a lock it will perform a distributed deadlock check after waiting longer than `rds_aurora.limitless_distributed_deadlock_timeout`.

### Action

Investigate causes of lock contention in your application and consider tuning `rds_aurora.limitless_distributed_deadlock_timeout`.

## AuroraLimitless:DistributedDeadlockDetection wait event

The process is communicating with other nodes to detect a distributed deadlock.

### Causes

When a process is waiting on a lock it will perform a distributed deadlock check after waiting longer than `rds_aurora.limitless_distributed_deadlock_timeout`.

### Action

Investigate causes of lock contention in your application and consider tuning `rds_aurora.limitless_distributed_deadlock_timeout`.

## AuroraLimitless:DistributedDeadlockAbort wait event

The process is communicating with another node to abort a session chosen as the victim in a distributed deadlock.

### Causes

Application patterns are resulting in distributed deadlocks.

### Action

Investigate application patterns resulting in distributed deadlocks.

## AuroraLimitless:GatherRemoteStats wait event

The process is gathering statistics from other nodes in the cluster.

### Causes

Monitoring or activty queries and views, such as `limitless_stat_activity`, will retrieve statistics from other nodes.

### Action

No further action is required.

## AuroraLimitless:GlobalSequenceRefresh wait event

The process is generating a new sequence value and must request a new chunk from the global sequence.

### Causes

A high rate of sequence value generation can result in stalls in this event if `rds_aurora.limitless_sequence_chunk_size` is insufficient.

### Action

This is a normal occurrence. If you see excessive time in this event consider tuning `rds_aurora.limitless_sequence_chunk_size`. See documentation on sequences in Limitless Database.

## AuroraLimitless:GlobalVacuumTimeExchange wait event

The process is exchanging snapshot data to support vacuum.

### Causes

Nodes in Limitless Database exchange oldest active snapshot time data with other nodes to compute the correct cutoff time for vacuum execution.

### Action

No further action is required.

## AuroraLimitless:DistributedTransactionMonitorGather wait event

The process is gathering transaction metadata from other nodes to support distributed transaction cleanup.

### Causes

Nodes in Limitless Database exchange transaction metadata with other nodes to determine when distributed transaction state can be purged.

### Action

No further action is required.

## AuroraLimitlessActivity:AdminTaskSchedulerMain wait event

Waiting in main loop of task scheduler process.

## AuroraLimitlessActivity:AdminTaskExecutorMain wait event

Waiting in main loop of task executor process.

## AuroraLimitlessActivity:AdminTaskMonitorMain wait event

Waiting in main loop of task monitor process.

## AuroraLimitlessActivity:DatabaseCleanupMonitorMain wait event

Waiting in main loop of database cleanup monitor process.

## AuroraLimitlessActivity:TopologyCleanupMonitorMain wait event

Waiting in main loop of topology cleanup monitor process.

## AuroraLimitlessActivity:ToplogyChangeMonitorMain wait event

Waiting in main loop of topology change monitor process.

## AuroraLimitlessActivity:DistributedTransactionMonitorMain wait event

Waiting in main loop of distributed transaction monitor process.

## AuroraLimitlessActivity:GlobalVacuumMonitorMain wait event

Waiting in main loop of global vacuum monitor process.
