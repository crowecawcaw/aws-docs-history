# SQL Server Agent and PostgreSQL

This topic provides reference information about the differences between SQL Server Agent and PostgreSQL in the context of migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. You can understand the key functions of SQL Server Agent, including scheduling automated maintenance jobs and alerting, and how these features are utilized in SQL Server.

## SQL Server Usage

SQL Server Agent provides two main functions: scheduling automated maintenance jobs and alerting.

###### Note

Other SQL Server built-in frameworks such as replication, also use SQL Server Agent jobs.

For more information, see [Maintenance Plans](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md") and [Alerting](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md").

## PostgreSQL Usage

Currently, there is no equivalent in Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) for scheduling tasks but you can create scheduled AWS Lambda that will run a stored procedure. Find an example in [Database Mail](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md").
