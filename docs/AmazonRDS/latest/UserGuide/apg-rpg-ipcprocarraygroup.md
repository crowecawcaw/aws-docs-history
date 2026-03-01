# IPC:ProcArrayGroupUpdate

The `IPC:ProcArrayGroupUpdate` event occurs when a session is waiting for the
group leader to update the transaction status at the end of that operation. While PostgreSQL
generally associates IPC type wait events with parallel query operations, this particular
wait event is not specific to parallel queries.

###### Topics

- [Supported engine versions](#apg-rpg-ipcprocarraygroup.supported "#apg-rpg-ipcprocarraygroup.supported")
- [Context](#apg-rpg-ipcprocarraygroup.context "#apg-rpg-ipcprocarraygroup.context")
- [Likely causes of increased waits](#apg-rpg-ipcprocarraygroup.causes "#apg-rpg-ipcprocarraygroup.causes")
- [Actions](#apg-rpg-ipcprocarraygroup.actions "#apg-rpg-ipcprocarraygroup.actions")

## Supported engine versions

This wait event information is supported for all versions of RDS for PostgreSQL.

## Context

Understanding the process array – The process
(proc) array is a shared memory structure in PostgreSQL. It holds information about all
running processes, including transaction details. During transaction completion
(`COMMIT` or `ROLLBACK`), the ProcArray needs to be updated to
reflect the change and clear the transactionID from the array. The session attempting to
finish its transaction must acquire an exclusive lock on the ProcArray. This prevents
other processes from obtaining shared or exclusive locks on it.

Group update mechanism – While performing a
COMMIT or ROLLBACK, if a backend process cannot obtain a ProcArrayLock in exclusive
mode, it updates a special field called ProcArrayGroupMember. This adds the transaction
to the list of sessions that intend to end. This backend process then sleeps and the
time it sleeps is instrumented as the ProcArrayGroupUpdate wait event. The first process
in the ProcArray with procArrayGroupMember, referred to as the leader process, acquires
the ProcArrayLock in exclusive mode. It then clears the list of processes waiting for
group transactionID clearing. Once this completes, the leader releases the ProcArrayLock
and then wakes up all processes in this list, notifying them that their transaction is
completed.

## Likely causes of increased waits

The more processes that are running, the longer a leader will hold on to a
procArrayLock in exclusive mode. Consequently, the more write transactions end up in a
group update scenario causing a potential pile up of processes waiting on the
`ProcArrayGroupUpdate` wait event. In Database Insights' Top SQL view,
you will see that COMMIT is the statement with the majority of this wait event. This is
expected but will require deeper investigation into the specific write SQL being run to
determine what appropriate action to take.

## Actions

We recommend different actions depending on the causes of your wait event. Identify
`IPC:ProcArrayGroupUpdate` events by using Amazon RDS Performance Insights or
by querying the PostgreSQL system view `pg_stat_activity`.

###### Topics

- [Monitoring transaction commit and rollback operations](#apg-rpg-ipcprocarraygroup.actions.monitor "#apg-rpg-ipcprocarraygroup.actions.monitor")
- [Reducing concurrency](#apg-rpg-ipcprocarraygroup.actions.concurrency "#apg-rpg-ipcprocarraygroup.actions.concurrency")
- [Implementing connection pooling](#apg-rpg-ipcprocarraygroup.actions.pooling "#apg-rpg-ipcprocarraygroup.actions.pooling")
- [Using faster storage](#apg-rpg-ipcprocarraygroup.actions.storage "#apg-rpg-ipcprocarraygroup.actions.storage")

### Monitoring transaction commit and rollback operations

Monitor commits and rollbacks – An increased
number of commits and rollbacks can lead to increased pressure on the ProcArray. For
example, if a SQL statement begins to fail due to increased duplicate key
violations, you may see an increase in rollbacks which can increase ProcArray
contention and table bloat.

Amazon RDS Database Insights provides the PostgreSQL metrics `xact_commit`
and `xact_rollback` to report the number of commits and rollbacks per
second.

### Reducing concurrency

Batching transactions – Where possible,
batch operations in single transactions to reduce commit/rollback operations.

Limit concurrency – Reduce the number of
concurrently active transactions to alleviate lock contention on the ProcArray.
While it will require some testing, reducing the total number of concurrent
connections can reduce contention and maintain throughput.

### Implementing connection pooling

Connection pooling solutions – Use
connection pooling to manage database connections efficiently, reducing the total
number of backends and therefore the workload on the ProcArray. While it will
require some testing, reducing the total number of concurrent connections can reduce
contention and maintain throughput.

Reduce connection storms – Similarly, a
pattern of frequently creating and terminating connections causes additional
pressure on the ProcArray. By reducing this pattern, overall contention is
reduced.

### Using faster storage

Dedicated log volume – If the
`IPC:ProcArrayGroupUpdate` wait event is accompanied with high
`IO:WALWrite` wait events, setting up a dedicated log volume can
reduce the bottleneck writing to WAL. In turn, this improves the performance of
commits.

For more information, see [Dedicated log volume](USER_PIOPS.md "USER_PIOPS.md").
