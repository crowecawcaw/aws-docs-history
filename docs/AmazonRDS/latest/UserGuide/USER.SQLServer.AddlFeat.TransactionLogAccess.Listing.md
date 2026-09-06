

# Listing available transaction log backups
<a name="USER.SQLServer.AddlFeat.TransactionLogAccess.Listing"></a>

With RDS for SQL Server, databases configured to use the full recovery model and a DB instance backup retention set to one or more days have transaction log backups automatically enabled. By enabling access to transaction log backups, up to seven days of those transaction log backups are made available for you to copy into your Amazon S3 bucket.

After you have enabled access to transaction log backups, you can start using it to list and copy available transaction log backup files.

**Listing transaction log backups**

To list all transaction log backups available for an individual database, call the `rds_fn_list_tlog_backup_metadata` function. You can use an `ORDER BY` or a `WHERE` clause when calling the function.

**Example of listing and filtering available transaction log backup files**  

```
SELECT * from msdb.dbo.rds_fn_list_tlog_backup_metadata('mydatabasename');
SELECT * from msdb.dbo.rds_fn_list_tlog_backup_metadata('mydatabasename') WHERE rds_backup_seq_id = 3507;
SELECT * from msdb.dbo.rds_fn_list_tlog_backup_metadata('mydatabasename') WHERE backup_file_time_utc > '2022-09-15 20:44:01' ORDER BY backup_file_time_utc DESC;
```

![Output from rds_fn_list_tlog_backup_metadata.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/sql_accesstransactionlogs_func.png)


The `rds_fn_list_tlog_backup_metadata` function returns the following output:



| Column name | Data type | Description | 
| --- | --- | --- | 
| `db_name` | sysname | The database name provided to list the transaction log backups for. | 
| `db_id` | int | The internal database identifier for the input parameter `db_name`. | 
| `family_guid` | uniqueidentifier | The unique ID of the original database at creation. This value remains the same when the database is restored, even to a different database name. | 
| `rds_backup_seq_id` | int | The ID that RDS uses internally to maintain a sequence number for each transaction log backup file. | 
| `backup_file_epoch` | bigint | The epoch time that a transaction backup file was generated. | 
| `backup_file_time_utc` | datetime | The UTC time-converted value for the `backup_file_epoch` value. | 
| `starting_lsn` | numeric(25,0) | The log sequence number of the first or oldest log record of a transaction log backup file. | 
| `ending_lsn` | numeric(25,0) | The log sequence number of the last or next log record of a transaction log backup file. | 
| `is_log_chain_broken` | bit | A boolean value indicating if the log chain is broken between the current transaction log backup file and the previous transaction log backup file. | 
| `file_size_bytes` | bigint | The size of the transactional backup set in bytes. | 
| `Error` | varchar(4000) | Error message if the `rds_fn_list_tlog_backup_metadata` function throws an exception. NULL if no exceptions. | 