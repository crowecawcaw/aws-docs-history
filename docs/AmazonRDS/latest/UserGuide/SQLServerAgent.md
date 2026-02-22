# Deleting a SQL Server Agent job

You use the `sp_delete_job` stored procedure to delete SQL Server Agent jobs on Amazon RDS for Microsoft SQL Server.

You can't use SSMS to delete SQL Server Agent jobs. If you try to do so, you get an error message similar to the
following:

```
The EXECUTE permission was denied on the object 'xp_regread', database 'mssqlsystemresource', schema 'sys'.
```

As a managed service, RDS is restricted from running procedures that access the Windows registry. When you use SSMS, it
tries to run a process (`xp_regread`) for which RDS isn't authorized.

###### Note

On RDS for SQL Server, only members of the sysadmin role are allowed to update or delete jobs owned by a different login.
For more information,
see [Leveraging SQLAgentOperatorRole in RDS SQL Server](https://aws.amazon.com/blogs/database/leveraging-sqlagentoperatorrole-in-rds-sql-server/ "https://aws.amazon.com/blogs/database/leveraging-sqlagentoperatorrole-in-rds-sql-server/").

###### To delete a SQL Server Agent job

- Run the following T-SQL statement:

```
EXEC msdb..sp_delete_job @job_name = '`job_name`';
```
