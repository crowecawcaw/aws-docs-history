# Transporting PostgreSQL databases between

DB instances

By using PostgreSQL transportable databases for Amazon RDS, you can move a PostgreSQL
database between two DB instances. This is a very fast way to migrate large
databases between different DB instances. To use this approach, your DB
instances must both run the same major version of PostgreSQL.

This capability requires that you install the `pg_transport` extension on both the source
and the destination DB instance. The `pg_transport`
extension provides a physical transport mechanism that moves the
database files with minimal processing. This mechanism moves data much faster than
traditional dump and load processes, with less downtime.

###### Note

PostgreSQL transportable databases are available in RDS for PostgreSQL 11.5 and higher, and RDS for PostgreSQL
version 10.10 and higher.

To transport a PostgreSQL DB instance from one RDS for PostgreSQL DB instance to another, you first
set up the source and destination instances as detailed in [Setting up a DB instance for transport](PostgreSQL.TransportableDB.md "PostgreSQL.TransportableDB.md"). You can then transport the database by
using the function described in [Transporting a PostgreSQL database](PostgreSQL.TransportableDB.md "PostgreSQL.TransportableDB.md").

###### Topics

- [What happens during database transport](#PostgreSQL.TransportableDB.DuringTransport "#PostgreSQL.TransportableDB.DuringTransport")
- [Limitations for using PostgreSQL
  transportable databases](#PostgreSQL.TransportableDB.Limits "#PostgreSQL.TransportableDB.Limits")
- [Setting up to transport a PostgreSQL
  database](PostgreSQL.TransportableDB.md "PostgreSQL.TransportableDB.md")
- [Transporting a PostgreSQL database to the destination from the source](PostgreSQL.TransportableDB.md "PostgreSQL.TransportableDB.md")
- [Transportable databases function reference](PostgreSQL.TransportableDB.transport.md "PostgreSQL.TransportableDB.transport.md")
- [Transportable databases parameter reference](PostgreSQL.TransportableDB.md "PostgreSQL.TransportableDB.md")

## What happens during database transport

The PostgreSQL transportable databases feature uses a pull model to import the database from
the source DB instance to the destination. The `transport.import_from_server` function creates the in-transit database
on the destination DB instance. The in-transit database is inaccessible on the
destination DB instance for the duration of the transport.

When transport begins, all current sessions on the source database are ended. Any
databases other than the source database on the source DB instance aren't affected
by the transport.

The source database is put into a special read-only mode. While it's in this
mode, you can connect to the source database and run read-only queries. However,
write-enabled queries and some other types of commands are blocked. Only the specific
source database that is being transported is affected by these restrictions.

During transport, you can't restore the destination DB instance to a point in
time. This is because the transport isn't transactional and doesn't use the
PostgreSQL write-ahead log to record changes. If the destination DB instance has
automatic backups enabled, a backup is automatically taken after transport completes.
Point-in-time restores are available for times _after_ the backup finishes.

If the transport fails, the `pg_transport` extension attempts to undo all
changes to the source and destination DB instances. This includes removing the
destination's partially transported database. Depending on the type of failure, the
source database might continue to reject write-enabled queries. If this happens, use the
following command to allow write-enabled queries.

```
ALTER DATABASE `db-name` SET default_transaction_read_only = false;
```

## Limitations for using PostgreSQL

transportable databases

Transportable databases have the following limitations:

- **Read replicas** – You can't use transportable
  databases on read replicas or parent instances of read replicas.
- **Unsupported column types** – You
  can't use the `reg` data types in any database tables that you
  plan to transport with this method. These types depend on system catalog object
  IDs (OIDs), which often change during transport.
- **Tablespaces** – All source database
  objects must be in the default `pg_default` tablespace.
- **Compatibility** – Both the source and
  destination DB instances must run the same major version of PostgreSQL.
- **Extensions** – The source DB instance
  can have only the `pg_transport` installed.
- **Roles and ACLs** – The source database's
  access privileges and ownership information aren't carried over to the
  destination database. All database objects are created and owned by the local
  destination user of the transport.
- **Concurrent transports** – A single
  DB instance can support up to 32 concurrent transports, including both imports and
  exports, if worker processes have been configured properly.
- **RDS for PostgreSQL DB instances only** – PostgreSQL
  transportable databases are supported on RDS for PostgreSQL DB instances only. You can't
  use it with on-premises databases or databases running on Amazon EC2.
