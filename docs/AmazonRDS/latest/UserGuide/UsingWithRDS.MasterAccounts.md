

# Master user account privileges
<a name="UsingWithRDS.MasterAccounts"></a>

When you create a new DB instance , the default master user that you use gets certain privileges for that DB instance . You can't change the master user name after the DB instance is created.

**Important**  
We strongly recommend that you do not use the master user directly in your applications. Instead, adhere to the best practice of using a database user created with the minimal privileges required for your application.

**Note**  
If you accidentally delete the permissions for the master user, you can restore them by modifying the DB instance and setting a new master user password. For more information about modifying a DB instance , see  [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md)  . 

The following table shows the privileges and database roles the master user gets for each of the database engines. 


|  Database engine  |  System privilege  |  Database role  | 
| --- | --- | --- | 
| RDS for Db2 | The master user is assigned to the `masterdba` group and assigned the `master_user_role`. <br /> `SYSMON`,`DBADM` with `DATAACCESS` AND `ACCCESSCTRL`, `BINDADD`,`CONNECT`, `CREATETAB`,`CREATE_SECURE_OBJECT`, `EXPLAIN`,`IMPLICIT_SCHEMA`, `LOAD`,`SQLADM`,`WLMADM`  |  `DBA`,`DBA_RESTRICTED`, `DEVELOPER`,`ROLE_NULLID_PACKAGES`, `ROLE_PROCEDURES`,`ROLE_TABLESPACES` <br />For more information, see [Amazon RDS for Db2 default roles](db2-default-roles.md) . | 
| RDS for MariaDB |  `SELECT`,`INSERT`,`UPDATE`,`DELETE`, `CREATE`,`DROP`,`RELOAD`, `PROCESS`,`REFERENCES`,`INDEX`, `ALTER`,`SHOW DATABASES`,`CREATE TEMPORARY TABLES`,`LOCK TABLES`, `EXECUTE`,`REPLICATION CLIENT`,`CREATE VIEW`,`SHOW VIEW`,`CREATE ROUTINE`, `ALTER ROUTINE`,`CREATE USER`, `EVENT`,`TRIGGER`,`REPLICATION SLAVE` <br />Starting with RDS for MariaDB version 11.4, the master user also gets the `SHOW CREATE ROUTINE` privilege. | — | 
| RDS for MySQL 8.0.36 and higher |  `SELECT`,`INSERT`,`UPDATE`, `DELETE`,`CREATE`,`DROP`, `RELOAD`,`PROCESS`, `REFERENCES`,`INDEX`,`ALTER`, `SHOW DATABASES`,`CREATE TEMPORARY TABLES`,`LOCK TABLES`,`EXECUTE`, `REPLICATION SLAVE`,`REPLICATION CLIENT`, `CREATE VIEW`,`SHOW VIEW`,`CREATE ROUTINE`,`ALTER ROUTINE`,`CREATE USER`,`EVENT`,`TRIGGER`, `CREATE ROLE`,`DROP ROLE`, `APPLICATION_PASSWORD_ADMIN`, `ROLE_ADMIN`,`SET_USER_ID`, `XA_RECOVER_ADMIN`  |  `rds_superuser_role` <br />For more information about `rds_superuser_role`, see [Role-based privilege model for RDS for MySQL](Appendix.MySQL.CommonDBATasks.privilege-model.md) . | 
| RDS for MySQL versions lower than 8.0.36 |  `SELECT`,`INSERT`,`UPDATE`, `DELETE`,`CREATE`,`DROP`, `RELOAD`,`PROCESS`, `REFERENCES`,`INDEX`,`ALTER`, `SHOW DATABASES`,`CREATE TEMPORARY TABLES`,`LOCK TABLES`,`EXECUTE`, `REPLICATION CLIENT`,`CREATE VIEW`, `SHOW VIEW`,`CREATE ROUTINE`,`ALTER ROUTINE`,`CREATE USER`,`EVENT`, `TRIGGER`,`REPLICATION SLAVE`  | — | 
| RDS for PostgreSQL |  `CREATE ROLE`,`CREATE DB`, `PASSWORD VALID UNTIL INFINITY`,`CREATE EXTENSION`,`ALTER EXTENSION`,`DROP EXTENSION`,`CREATE TABLESPACE`,`ALTER <OBJECT> OWNER`,`CHECKPOINT`, `PG_CANCEL_BACKEND()`, `PG_TERMINATE_BACKEND()`,`SELECT PG_STAT_REPLICATION`,`EXECUTE PG_STAT_STATEMENTS_RESET()`,`OWN POSTGRES_FDW_HANDLER()`,`OWN POSTGRES_FDW_VALIDATOR()`,`OWN POSTGRES_FDW`, `EXECUTE PG_BUFFERCACHE_PAGES()`,`SELECT PG_BUFFERCACHE`  |  `RDS_SUPERUSER` <br />For more information about RDS\_SUPERUSER, see [Understanding PostgreSQL roles and permissions](Appendix.PostgreSQL.CommonDBATasks.Roles.md) .  | 
| RDS for Oracle |  `ADMINISTER DATABASE TRIGGER`,`ALTER DATABASE LINK`,`ALTER PUBLIC DATABASE LINK`, `AUDIT SYSTEM`,`CHANGE NOTIFICATION`, `DROP ANY DIRECTORY`,`EXEMPT ACCESS POLICY`,`EXEMPT IDENTITY POLICY`,`EXEMPT REDACTION POLICY`,`FLASHBACK ANY TABLE`, `GRANT ANY OBJECT PRIVILEGE`,`RESTRICTED SESSION`,`SELECT ANY TABLE`,`UNLIMITED TABLESPACE`  |  `DBA`  The `DBA` role is exempt from the following privileges: <br /> `ALTER DATABASE`,`ALTER SYSTEM`, `CREATE ANY DIRECTORY`,`CREATE EXTERNAL JOB`,`CREATE PLUGGABLE DATABASE`, `GRANT ANY PRIVILEGE`,`GRANT ANY ROLE`,`READ ANY FILE GROUP`   | 
| Amazon RDS for Microsoft SQL Server |  `ADMINISTER BULK OPERATIONS`,`ALTER ANY CONNECTION`,`ALTER ANY CREDENTIAL`, `ALTER ANY EVENT SESSION`,`ALTER ANY LINKED SERVER`,`ALTER ANY LOGIN`,`ALTER ANY SERVER AUDIT`,`ALTER ANY SERVER ROLE`, `ALTER SERVER STATE`,`ALTER TRACE`, `CONNECT SQL`,`CREATE ANY DATABASE`, `VIEW ANY DATABASE`,`VIEW ANY DEFINITION`,`VIEW SERVER STATE`,`ALTER ON ROLE SQLAgentOperatorRole`  |  `DB_OWNER` (database-level role), `PROCESSADMIN` (server-level role), `SETUPADMIN` (server-level role), `SQLAgentUserRole` (database-level role), `SQLAgentReaderRole` (database-level role), and `SQLAgentOperatorRole` (database-level role) | 