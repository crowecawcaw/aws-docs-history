# Tuning with wait events for RDS for PostgreSQL

Wait events are an important tuning tool for RDS for PostgreSQL. When you can find out why
sessions are waiting for resources and what they are doing, you're better able to
reduce bottlenecks. You can use the information in this section to find possible causes and
corrective actions. This section also discusses basic PostgreSQL tuning concepts.

The wait events in this section are specific to RDS for PostgreSQL.

###### Topics

- [Essential concepts for
  RDS for PostgreSQL tuning](PostgreSQL.Tuning.md "PostgreSQL.Tuning.md")
- [RDS for PostgreSQL wait events](PostgreSQL.Tuning.concepts.md "PostgreSQL.Tuning.concepts.md")
- [Client:ClientRead](wait-event.md "wait-event.md")
- [Client:ClientWrite](wait-event.md "wait-event.md")
- [CPU](wait-event.md "wait-event.md")
- [IO:BufFileRead and IO:BufFileWrite](wait-event.md "wait-event.md")
- [IO:DataFileRead](wait-event.md "wait-event.md")
- [IO:WALWrite](wait-event.md "wait-event.md")
- [IPC:parallel wait events](rpg-ipc-parallel.md "rpg-ipc-parallel.md")
- [IPC:ProcArrayGroupUpdate](apg-rpg-ipcprocarraygroup.md "apg-rpg-ipcprocarraygroup.md")
- [Lock:advisory](wait-event.md "wait-event.md")
- [Lock:extend](wait-event.md "wait-event.md")
- [Lock:Relation](wait-event.md "wait-event.md")
- [Lock:transactionid](wait-event.md "wait-event.md")
- [Lock:tuple](wait-event.md "wait-event.md")
- [LWLock:BufferMapping (LWLock:buffer_mapping)](wait-event.md "wait-event.md")
- [LWLock:BufferIO (IPC:BufferIO)](wait-event.md "wait-event.md")
- [LWLock:buffer_content (BufferContent)](wait-event.md "wait-event.md")
- [LWLock:lock_manager (LWLock:lockmanager)](wait-event.md "wait-event.md")
- [LWLock:pg_stat_statements](apg-rpg-lwlockpgstat.md "apg-rpg-lwlockpgstat.md")
- [LWLock:SubtransSLRU](apg-rpg-lwlocksubtransslru.md "apg-rpg-lwlocksubtransslru.md")
- [Timeout:PgSleep](wait-event.md "wait-event.md")
- [Timeout:VacuumDelay](wait-event.md "wait-event.md")
