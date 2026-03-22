# Deleting files on the RDS DB instance

To delete the files available on the DB instance, use the Amazon RDS stored procedure
`msdb.dbo.rds_delete_from_filesystem` with the following parameters.

| Parameter name   | Data type | Default | Required | Description                                                                                                                                            |
| ---------------- | --------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `@rds_file_path` | NVARCHAR  | –       | Required | The file path of the file to delete. Absolute and relative paths are supported.                                                                        |
| `@force_delete`  | INT       | 0       | Optional | To delete a directory, this flag must be included and set to `1`.<br>`1` = delete a directory<br>This parameter is ignored if you are deleting a file. |

To delete a directory, the `@rds_file_path` must end with a backslash (`\`) and
`@force_delete` must be set to `1`.

The following example deletes the file `D:\S3\delete_me.txt`.

```
exec msdb.dbo.rds_delete_from_filesystem
    @rds_file_path='D:\S3\`delete_me.txt`';
```

The following example deletes the directory `D:\S3\example_folder\`.

```
exec msdb.dbo.rds_delete_from_filesystem
    @rds_file_path='D:\S3\`example_folder`\',
    @force_delete=1;
```
