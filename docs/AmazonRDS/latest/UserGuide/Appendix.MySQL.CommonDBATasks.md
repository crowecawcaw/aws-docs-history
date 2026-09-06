

# Common DBA tasks for MySQL DB instances
<a name="Appendix.MySQL.CommonDBATasks"></a>

In the following content, you can find descriptions of the Amazon RDS-specific implementations of some common DBA tasks for DB instances running the MySQL database engine. To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB instances. Also, it restricts access to certain system procedures and tables that require advanced privileges. 

For information about working with MySQL log files on Amazon RDS, see [MySQL database log files](USER_LogAccess.Concepts.MySQL.md).

## Understanding predefined users
<a name="Appendix.MySQL.CommonDBATasks.users"></a>

Amazon RDS automatically creates several predefined users with new RDS for MySQL DB instances. Predefined users and their privileges can't be changed. You can't drop, rename, or modify privileges for these predefined users. Attempting to do so results in an error. 
+ **rdsadmin** – A user that's created to handle many of the management tasks that the administrator with `superuser` privileges would perform on a standalone MySQL database. This user is used internally by RDS for MySQL for many management tasks. 
+ **rdsrepladmin** – A user that's used internally by Amazon RDS to support replication activities on RDS for MySQL DB instances and clusters. 

For information about other common DBA tasks, see the following topics.

**Topics**
+ [Understanding predefined users](#Appendix.MySQL.CommonDBATasks.users)
+ [Role-based privilege model for RDS for MySQL](Appendix.MySQL.CommonDBATasks.privilege-model.md)
+ [Dynamic privileges for RDS for MySQL](Appendix.MySQL.CommonDBATasks.dynamic-privileges.md)
+ [Ending a session or query for RDS for MySQL](Appendix.MySQL.CommonDBATasks.End.md)
+ [Skipping the current replication error for RDS for MySQL](Appendix.MySQL.CommonDBATasks.SkipError.md)
+ [Working with InnoDB tablespaces to improve crash recovery times for RDS for MySQL](Appendix.MySQL.CommonDBATasks.Tables.md)
+ [Managing the Global Status History for RDS for MySQL](Appendix.MySQL.CommonDBATasks.GoSH.md)
+ [Configuring buffer pool size and redo log capacity in MySQL 8.4](Appendix.MySQL.CommonDBATasks.Config.Size.8.4.md)