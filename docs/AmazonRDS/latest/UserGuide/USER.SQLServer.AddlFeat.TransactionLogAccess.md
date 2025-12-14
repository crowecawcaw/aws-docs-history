# Canceling a task

To cancel a running task, call the `rds_cancel_task` stored procedure.

###### Example usage:

```

exec msdb.dbo.rds_cancel_task @task_id=ID_number;

```

The following parameter is required:

- `@task_id` – The ID of the task to cancel.
  You can view the task ID by calling the `rds_task_status` stored procedure.
  For more information on viewing and canceling running tasks,
  see [Importing and exporting SQL Server databases using native
  backup and restore](SQLServer.Procedural.md "SQLServer.Procedural.md").
