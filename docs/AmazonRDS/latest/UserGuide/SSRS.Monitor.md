

# Monitoring the status of a task
<a name="SSRS.Monitor"></a>

To track the status of your granting or revoking task, call the `rds_fn_task_status` function. It takes two parameters. The first parameter should always be `NULL` because it doesn't apply to SSRS. The second parameter accepts a task ID. 

To see a list of all tasks, set the first parameter to `NULL` and the second parameter to `0`, as shown in the following example.

```
SELECT * FROM msdb.dbo.rds_fn_task_status(NULL,{{0}});
```

To get a specific task, set the first parameter to `NULL` and the second parameter to the task ID, as shown in the following example.

```
SELECT * FROM msdb.dbo.rds_fn_task_status(NULL,{{42}});
```

The `rds_fn_task_status` function returns the following information.


| Output parameter | Description | 
| --- | --- | 
| `task_id` | The ID of the task. | 
| `task_type` | For SSRS, tasks can have the following task types:+ `SSRS_GRANT_PORTAL_PERMISSION`<br />+ `SSRS_REVOKE_PORTAL_PERMISSION`<br />For PBIRS, tasks can have the following task types:+ `PBIRS_GRANT_PORTAL_PERMISSION`<br />+ `PBIRS_REVOKE_PORTAL_PERMISSION` | 
| `database_name` | Not applicable to SSRS or PBIRS tasks. | 
| `% complete` | The progress of the task as a percentage. | 
| `duration (mins)` | The amount of time spent on the task, in minutes. | 
| `lifecycle` | The status of the task. Possible statuses are the following:+  `CREATED` – After you call one of the SSRS stored procedures, a task is created and the status is set to `CREATED`. <br />+  `IN_PROGRESS` – After a task starts, the status is set to `IN_PROGRESS`. It can take up to five minutes for the status to change from `CREATED` to `IN_PROGRESS`. <br />+  `SUCCESS` – After a task completes, the status is set to `SUCCESS`. <br />+  `ERROR` – If a task fails, the status is set to `ERROR`. For more information about the error, see the `task_info` column. <br />+  `CANCEL_REQUESTED` – After you call the `rds_cancel_task` stored procedure, the status of the task is set to `CANCEL_REQUESTED`. <br />+  `CANCELLED` – After a task is successfully canceled, the status of the task is set to `CANCELLED`.   | 
| `task_info` | Additional information about the task. If an error occurs during processing, this column contains information about the error.  | 
| `last_updated` | The date and time that the task status was last updated.  | 
| `created_at` | The date and time that the task was created. | 
| `S3_object_arn` | Not applicable to SSRS or PBIRS tasks. | 
| `overwrite_S3_backup_file` | Not applicable to SSRS or PBIRS tasks. | 
| `KMS_master_key_arn` | Not applicable to SSRS or PBIRS tasks. | 
| `filepath` | Not applicable to SSRS or PBIRS tasks. | 
| `overwrite_file` | Not applicable to SSRS or PBIRS tasks. | 
| `task_metadata` | Metadata associated with the SSRS or PBIRS task. | 