# RDS for PostgreSQL

processes

RDS for PostgreSQL uses multiple processes.

###### Topics

- [Postmaster
  process](#PostgreSQL.Tuning.concepts.postmaster "#PostgreSQL.Tuning.concepts.postmaster")
- [Backend processes](#PostgreSQL.Tuning.concepts.backend "#PostgreSQL.Tuning.concepts.backend")
- [Background processes](#PostgreSQL.Tuning.concepts.vacuum "#PostgreSQL.Tuning.concepts.vacuum")

## Postmaster

process

The _postmaster process_ is the first process started when
you start RDS for PostgreSQL. The postmaster process has the following primary
responsibilities:

- Fork and monitor background processes
- Receive authentication requests from client processes, and
  authenticate them before allowing the database to service
  requests

## Backend processes

If the postmaster authenticates a client request, the postmaster forks a new
backend process, also called a postgres process. One client process connects to
exactly one backend process. The client process and the backend process
communicate directly without intervention by the postmaster process.

## Background processes

The postmaster process forks several processes that perform different backend
tasks. Some of the more important include the following:

- WAL writer

RDS for PostgreSQL writes data in the WAL (write ahead logging) buffer to
the log files. The principle of write ahead logging is that the database
can't write changes to the data files until after the database writes
log records describing those changes to disk. The WAL mechanism reduces
disk I/O, and allows RDS for PostgreSQL to use the logs to recover the
database after a failure.

- Background writer

This process periodically write dirty (modified) pages from the memory
buffers to the data files. A page becomes dirty when a backend process
modifies it in memory.

- Autovacuum daemon

The daemon consists of the following:

    + The autovacuum launcher
    + The autovacuum worker processes

When autovacuum is turned on, it checks for tables that have had a
large number of inserted, updated, or deleted tuples. The daemon has the
following responsibilities:

    + Recover or reuse disk space occupied by updated or deleted
     rows
    + Update statistics used by the planner
    + Protect against loss of old data because of transaction ID
     wraparound

The autovacuum feature automates the execution of `VACUUM`
and `ANALYZE` commands. `VACUUM` has the following
variants: standard and full. Standard vacuum runs in parallel with other
database operations. `VACUUM FULL` requires an exclusive lock
on the table it is working on. Thus, it can't run in parallel with
operations that access the same table. `VACUUM` creates a
substantial amount of I/O traffic, which can cause poor performance for
other active sessions.
