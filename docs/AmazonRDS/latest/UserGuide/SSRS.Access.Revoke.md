# Revoking system-level permissions

The `RDS_SSRS_ROLE` system role doesn't have sufficient permissions to
delete system-level role assignments. To remove a user or user group from
`RDS_SSRS_ROLE`, use the same stored procedure that you used to grant the
role but use the `SSRS_REVOKE_PORTAL_PERMISSION` task type.

###### To revoke access from a domain user for the web portal

- Use the following stored procedure.

```
exec msdb.dbo.rds_msbi_task
@task_type='SSRS_REVOKE_PORTAL_PERMISSION',
@ssrs_group_or_username=N'`AD_domain`\`user`';
```

Doing this deletes the user from the `RDS_SSRS_ROLE` system role. It also deletes
the user from the `Content Manager` item-level role if the user has
it.
