# Listing files on the RDS DB instance

To list the files available on the DB instance, use both a stored procedure and a function. First, run the following stored
procedure to gather file details from the files in `D:\S3\`.

```
exec msdb.dbo.rds_gather_file_details;
```

The stored procedure returns the ID of the task. Like other tasks, this stored procedure runs asynchronously. As soon as the
status of the task is `SUCCESS`, you can use the task ID in the `rds_fn_list_file_details` function to
list the existing files and directories in D:\S3\, as shown following.

```
SELECT * FROM msdb.dbo.rds_fn_list_file_details(`TASK_ID`);
```

The `rds_fn_list_file_details` function returns a table with the following columns.

| Output parameter    | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| `filepath`          | Absolute path of the file (for example, `D:\S3\mydata.csv`)            |
| `size_in_bytes`     | File size (in bytes)                                                   |
| `last_modified_utc` | Last modification date and time in UTC format                          |
| `is_directory`      | Option that indicates whether the item is a directory (`true`/`false`) |
