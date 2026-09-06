

# Master user account privileges
<a name="UsingWithRDS.MasterAccounts"></a>

When you create a new DB cluster, the default master user that you use gets certain privileges for that DB cluster. You can't change the master user name after the DB cluster is created.

**Important**  
We strongly recommend that you do not use the master user directly in your applications. Instead, adhere to the best practice of using a database user created with the minimal privileges required for your application.

**Note**  
If you accidentally delete the permissions for the master user, you can restore them by modifying the DB cluster and setting a new master user password. For more information about modifying a DB cluster, see  [Modifying an Amazon Aurora DB cluster](Aurora.Modifying.md) . 

The following table shows the privileges and database roles the master user gets for each of the database engines. 

<a name="master-user-account-privileges"></a>

- ** Aurora MySQL **
  - **System privilege:** Version 2:<br /> `ALTER`,`ALTER ROUTINE`, `CREATE`,`CREATE ROUTINE`,`CREATE TEMPORARY TABLES`,`CREATE USER`,`CREATE VIEW`,`DELETE`,`DROP`, `EVENT`,`EXECUTE`,`GRANT OPTION`,`INDEX`,`INSERT`, `LOAD FROM S3`,`LOCK TABLES`, `PROCESS`,`REFERENCES`, `RELOAD`,`REPLICATION CLIENT`, `REPLICATION SLAVE`,`SELECT`, `SELECT INTO S3`,`SHOW DATABASES`, `SHOW VIEW`,`TRIGGER`, `UPDATE`  / **Database role:** —
  - **System privilege:** Version 3:<br /> `ALTER`,`APPLICATION_PASSWORD_ADMIN`, `ALTER ROUTINE`,`CONNECTION_ADMIN`, `CREATE`,`CREATE ROLE`,`CREATE ROUTINE`,`CREATE TEMPORARY TABLES`, `CREATE USER`,`CREATE VIEW`, `DELETE`,`DROP`,`DROP ROLE`, `EVENT`,`EXECUTE`,`INDEX`, `INSERT`,`LOCK TABLES`, `PROCESS`,`REFERENCES`, `RELOAD`,`REPLICATION CLIENT`, `REPLICATION SLAVE`,`ROLE_ADMIN`, `SET_USER_ID`,`SELECT`,`SHOW DATABASES`,`SHOW VIEW`,`TRIGGER`, `UPDATE`,`XA_RECOVER_ADMIN` <br />Starting with Aurora MySQL version 3.04.0, the master user also gets the `SHOW_ROUTINE` privilege.<br />Starting with Aurora MySQL version 3.09.0, the master user also gets the `FLUSH_OPTIMIZER_COSTS`,`FLUSH_STATUS`,`FLUSH_TABLES`, and `FLUSH_USER_RESOURCES` privileges. / **Database role:**  `rds_superuser_role` <br />For more information about rds\_superuser\_role, see [Role-based privilege model](AuroraMySQL.Compare-80-v3.md#AuroraMySQL.privilege-model) .
  - **System privilege:** Version 8.4:<br /> `ALTER`,`ALLOW_NONEXISTENT_DEFINER`, `APPLICATION_PASSWORD_ADMIN`, `ALTER ROUTINE`,`CONNECTION_ADMIN`, `CREATE`,`CREATE ROLE`,`CREATE ROUTINE`,`CREATE TEMPORARY TABLES`, `CREATE USER`,`CREATE VIEW`, `DELETE`,`DROP`,`DROP ROLE`, `EVENT`,`EXECUTE`, `FLUSH_OPTIMIZER_COSTS`,`FLUSH_PRIVILEGES`, `FLUSH_STATUS`,`FLUSH_TABLES`, `FLUSH_USER_RESOURCES`, `INDEX`,`INSERT`, `LOCK TABLES`,`OPTIMIZE_LOCAL_TABLE`, `PROCESS`,`REFERENCES`, `RELOAD`,`REPLICATION CLIENT`, `REPLICATION SLAVE`,`ROLE_ADMIN`, `SELECT`,`SET_ANY_DEFINER`, `SHOW DATABASES`,`SHOW_ROUTINE`, `SHOW VIEW`,`TRIGGER`, `UPDATE`,`XA_RECOVER_ADMIN`  / **Database role:**  `rds_superuser_role` <br />For more information about rds\_superuser\_role, see [Role-based privilege model](AuroraMySQL.Compare-80-v3.md#AuroraMySQL.privilege-model) .

- ** Aurora PostgreSQL **
  - **System privilege:**  `LOGIN`,`NOSUPERUSER`, `INHERIT`,`CREATEDB`, `CREATEROLE`,`NOREPLICATION`,`VALID UNTIL 'infinity'` 
  - **Database role:**  `RDS_SUPERUSER` <br />For more information about RDS\_SUPERUSER, see [Understanding PostgreSQL roles and permissions](Appendix.PostgreSQL.CommonDBATasks.Roles.md) .

