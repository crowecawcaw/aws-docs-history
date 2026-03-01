# Tracking the status of tasks

To track the status of your copy tasks, call the `rds_task_status` stored procedure.
If you don't provide any parameters, the stored procedure returns the status of all tasks.

###### Example usage:

```

exec msdb.dbo.rds_task_status
  @db_name='database_name',
  @task_id=ID_number;

```

The following parameters are optional:

- `@db_name` – The name of the database to show the task status for.
- `@task_id` – The ID of the task to show the task status for.

###### Example of listing the status for a specific task ID:

```

exec msdb.dbo.rds_task_status @task_id=5;

```

###### Example of listing the status for a specific database and task:

```

exec msdb.dbo.rds_task_status@db_name='my_database',@task_id=5;

```

###### Example of listing all tasks and their status for a specific database:

```

exec msdb.dbo.rds_task_status @db_name='my_database';

```

###### Example of listing all tasks and their status on the current DB instance:

```

exec msdb.dbo.rds_task_status;

```
