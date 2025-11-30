# Common DBA tasks for Amazon RDS for Microsoft SQL Server

This section describes the Amazon RDS-specific implementations of some common DBA tasks for DB
instances that are running the Microsoft SQL Server database engine. In order to deliver a
managed service experience, Amazon RDS does not provide shell access to DB instances, and it
restricts access to certain system procedures and tables that require advanced privileges.

###### Note

When working with a SQL Server DB instance, you can run scripts to modify a newly
created database, but you cannot modify the [model] database, the database used as the
model for new databases.

###### Topics

- [Accessing the tempdb database on Microsoft SQL Server DB
  instances on Amazon RDS](SQLServer.md "SQLServer.md")
- [Analyzing your database workload on an Amazon RDS for SQL Server DB instance with Database
  Engine Tuning Advisor](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Changing the
  db_owner to the rdsa account for your Amazon RDS for SQL Server database](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Managing collations and
  character sets for Amazon RDS for Microsoft SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Creating a database user for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Determining a
  recovery model for your Amazon RDS for SQL Server database](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Determining the last failover time for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Troubleshooting point-in-time-recovery failures due to a log sequence number gap](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Deny or allow viewing database names for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Disabling fast inserts during bulk loading for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Dropping a database in an Amazon RDS for Microsoft SQL Server DB instance](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Renaming a Amazon RDS for Microsoft SQL Server database in a Multi-AZ deployment](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Resetting the db_owner role
  membership for master user for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Restoring
  license-terminated DB instances for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Transitioning a
  Amazon RDS for SQL Server database from OFFLINE to ONLINE](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Using change data capture for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Using SQL Server Agent for Amazon RDS](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Working with Amazon RDS for Microsoft SQL Server logs](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Working with trace and
  dump files for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
