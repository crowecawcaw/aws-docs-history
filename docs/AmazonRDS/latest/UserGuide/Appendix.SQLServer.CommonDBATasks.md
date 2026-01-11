# Deny or allow viewing database names for Amazon RDS for SQL Server

The master user cannot set `DENY VIEW ANY DATABASE TO `LOGIN``  
to hide databases from a user.  
To change this permission, use the following stored procedure instead:

- Denying database view access to `LOGIN`:

```
EXEC msdb.dbo.rds_manage_view_db_permission @permission=‘DENY’, @server_principal=`‘LOGIN’` 
go
```

- Allowing database view access to `LOGIN`:

```
EXEC msdb.dbo.rds_manage_view_db_permission @permission='GRANT', @server_principal=`'LOGIN'`
 go
```

Consider the following when using this stored procedure:

- Database names are hidden from the SSMS and internal DMV (dynamic management views).
  However, database names are still visible from audit, logs and metadata tables.
  These are secured `VIEW ANY DATABASE` server permissions. For more information, see
  [DENY Server Permissions](https://learn.microsoft.com/en-us/sql/t-sql/statements/deny-server-permissions-transact-sql?view=sql-server-ver16#permissions "https://learn.microsoft.com/en-us/sql/t-sql/statements/deny-server-permissions-transact-sql?view=sql-server-ver16#permissions").
- Once the permission is reverted to `GRANT` (allowed), the `LOGIN` can view all databases.
- If you delete and recreate `LOGIN`, the view permission related to the LOGIN is reset to `ALLOW`.
- For Multi-AZ instances, set the `DENY` or `GRANT` permission only for the `LOGIN` on the primary host.
  The changes are propagated to the secondary host automatically.
- This permission only changes whether a login can view the database names.
  However, access to databases and objects within are managed separately.
