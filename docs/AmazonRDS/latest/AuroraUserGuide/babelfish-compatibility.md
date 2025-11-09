# Differences between Babelfish for Aurora PostgreSQL and SQL

Server

Babelfish is an evolving Aurora PostgreSQL feature, with new functionality added in
each release since the initial offering in Aurora PostgreSQL 13.4. It's designed to
provide T-SQL semantics on top of PostgreSQL through the T-SQL dialect using the TDS
port. Each new version of Babelfish adds features and functions that better align
with T-SQL functionality and behavior, as shown in the [Supported
functionalities in Babelfish by version](babelfish-compatibility.md "babelfish-compatibility.md") table. For
best results when working with Babelfish, we recommend that you understand the
differences that currently exist between the T-SQL supported by SQL Server and
Babelfish for the latest version. To learn more, see [T-SQL differences in
Babelfish](babelfish-compatibility.tsql.md "babelfish-compatibility.tsql.md").

In addition to the differences between T-SQL supported by Babelfish and SQL
Server, you might also need to consider interoperability issues between Babelfish
and PostgreSQL in the context of the Aurora PostgreSQL DB cluster. As mentioned previously,
Babelfish supports T-SQL semantics on top of PostgreSQL through the T-SQL dialect
using the TDS port. At the same time, the Babelfish database can also be accessed
through the standard PostgreSQL port with PostgreSQL SQL statements. If you're
considering using both PostgreSQL and Babelfish functionality in a production
deployment, you need to be aware of the potential interoperability issues between schema
names, identifiers, permissions, transactional semantics, multiple result sets, default
collations, and so on. In simple terms, when PostgreSQL statements or PostgreSQL access
occur in the context of Babelfish, interference between PostgreSQL and
Babelfish can occur and can potentially affecting syntax, semantics, and
compatibility when new versions of Babelfish are released. For complete
information and guidance about all the considerations, see the [Guidance on
Babelfish Interoperability](https://babelfishpg.org/docs/usage/interoperability/ "https://babelfishpg.org/docs/usage/interoperability/") in the Babelfish for PostgreSQL
documentation.

###### Note

Before using both PostgreSQL native functionality and Babelfish
functionality in the same application context, we strongly recommend that you
consider the issues discussed in the [Guidance on
Babelfish Interoperability](https://babelfishpg.org/docs/usage/interoperability/ "https://babelfishpg.org/docs/usage/interoperability/") in the Babelfish for PostgreSQL
documentation. These interoperability issues (Aurora PostgreSQL and Babelfish)
are relevant only if you plan to use the PostgreSQL database instance in the same
application context as Babelfish.

###### Topics

- [Babelfish dump and
  restore](#babelfish-compatibility.dumprestore "#babelfish-compatibility.dumprestore")
- [T-SQL differences in
  Babelfish](babelfish-compatibility.tsql.md "babelfish-compatibility.tsql.md")
- [Transaction isolation levels in Babelfish](babelfish-transaction.md "babelfish-transaction.md")

## Babelfish dump and

restore

Starting with version 4.0.0 and 3.4.0, Babelfish users can now utilize the
dump and restore utilities to backup and restore their databases. For more
information, see [Babelfish dump and restore](https://github.com/babelfish-for-postgresql/babelfish-for-postgresql/wiki/Babelfish-Dump-and-Restore "https://github.com/babelfish-for-postgresql/babelfish-for-postgresql/wiki/Babelfish-Dump-and-Restore"). This feature is built on top of PostgreSQL
dump and restore utilities. For more information, see [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html "https://www.postgresql.org/docs/current/app-pgdump.html")
and see [pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html "https://www.postgresql.org/docs/current/app-pgrestore.html"). In order to effectively use this feature in
Babelfish, you need to use PostgreSQL-based tools that are specifically
adapted for Babelfish. The backup and restore feature for Babelfish
differs significantly from that of SQL Server. For more information on these
differences, see [Dump and restore functionality differences : Babelfish and SQL
Server](https://github.com/babelfish-for-postgresql/babelfish-for-postgresql/wiki/Babelfish-Dump-and-Restore#differences "https://github.com/babelfish-for-postgresql/babelfish-for-postgresql/wiki/Babelfish-Dump-and-Restore#differences"). Babelfish for Aurora PostgreSQL provides additional capabilities for backing up
and restoring Amazon Aurora PostgreSQL DB clusters. For more information, see [Backing up and restoring an Amazon Aurora DB cluster](BackupRestoreAurora.md "BackupRestoreAurora.md").
