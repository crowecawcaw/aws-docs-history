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

- [Accessing the tempdb database on Microsoft SQL Server DB instances on Amazon RDS](SQLServer.TempDB.md "SQLServer.TempDB.md")
- [Analyzing your database workload on an Amazon RDS for SQL Server DB instance with Database Engine Tuning Advisor](Appendix.SQLServer.CommonDBATasks.Workload.md "Appendix.SQLServer.CommonDBATasks.Workload.md")
- [Changing the db\_owner to the rdsa account for your Amazon RDS for SQL Server database](Appendix.SQLServer.CommonDBATasks.ChangeDBowner.md "Appendix.SQLServer.CommonDBATasks.ChangeDBowner.md")
- [Managing collations and character sets for Amazon RDS for Microsoft SQL Server](Appendix.SQLServer.CommonDBATasks.Collation.md "Appendix.SQLServer.CommonDBATasks.Collation.md")
- [Creating a database user for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.CreateUser.md "Appendix.SQLServer.CommonDBATasks.CreateUser.md")
- [Determining a recovery model for your Amazon RDS for SQL Server database](Appendix.SQLServer.CommonDBATasks.DatabaseRecovery.md "Appendix.SQLServer.CommonDBATasks.DatabaseRecovery.md")
- [Determining the last failover time for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.LastFailover.md "Appendix.SQLServer.CommonDBATasks.LastFailover.md")
- [Troubleshooting point-in-time-recovery failures due to a log sequence number gap](Appendix.SQLServer.CommonDBATasks.PITR-LSN-Gaps.md "Appendix.SQLServer.CommonDBATasks.PITR-LSN-Gaps.md")
- [Deny or allow viewing database names for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.ManageView.md "Appendix.SQLServer.CommonDBATasks.ManageView.md")
- [Disabling fast inserts during bulk loading for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.DisableFastInserts.md "Appendix.SQLServer.CommonDBATasks.DisableFastInserts.md")
- [Dropping a database in an Amazon RDS for Microsoft SQL Server DB instance](Appendix.SQLServer.CommonDBATasks.DropMirrorDB.md "Appendix.SQLServer.CommonDBATasks.DropMirrorDB.md")
- [Renaming a Amazon RDS for Microsoft SQL Server database in a Multi-AZ deployment](Appendix.SQLServer.CommonDBATasks.RenamingDB.md "Appendix.SQLServer.CommonDBATasks.RenamingDB.md")
- [Resetting the db\_owner role membership for master user for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.ResetPassword.md "Appendix.SQLServer.CommonDBATasks.ResetPassword.md")
- [Restoring license-terminated DB instances for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.RestoreLTI.md "Appendix.SQLServer.CommonDBATasks.RestoreLTI.md")
- [Transitioning a Amazon RDS for SQL Server database from OFFLINE to ONLINE](Appendix.SQLServer.CommonDBATasks.TransitionOnline.md "Appendix.SQLServer.CommonDBATasks.TransitionOnline.md")
- [Using change data capture for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.CDC.md "Appendix.SQLServer.CommonDBATasks.CDC.md")
- [Using SQL Server Agent for Amazon RDS](Appendix.SQLServer.CommonDBATasks.Agent.md "Appendix.SQLServer.CommonDBATasks.Agent.md")
- [Working with Amazon RDS for Microsoft SQL Server logs](Appendix.SQLServer.CommonDBATasks.Logs.md "Appendix.SQLServer.CommonDBATasks.Logs.md")
- [Working with trace and dump files for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.TraceFiles.md "Appendix.SQLServer.CommonDBATasks.TraceFiles.md")
- [Setting trace flags in RDS for Microsoft SQL Server](Appendix.SQLServer.CommonDBATasks.TraceFlags.md "Appendix.SQLServer.CommonDBATasks.TraceFlags.md")
