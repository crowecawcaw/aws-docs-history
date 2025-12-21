# Cache warming for MariaDB on Amazon RDS

InnoDB cache warming can provide performance gains for your MariaDB DB instance by
saving the current state of the buffer pool when the DB instance is shut down, and
then reloading the buffer pool from the saved information when the DB instance
starts up. This approach bypasses the need for the buffer pool to "warm up" from
normal database use and instead preloads the buffer pool with the pages for known
common queries. For more information on cache warming, see [Dumping and restoring the buffer pool](http://mariadb.com/kb/en/mariadb/xtradbinnodb-buffer-pool/#dumping-and-restoring-the-buffer-pool "http://mariadb.com/kb/en/mariadb/xtradbinnodb-buffer-pool/#dumping-and-restoring-the-buffer-pool") in the MariaDB documentation.

Cache warming is enabled by default on MariaDB 10.3 and higher DB instances. To enable
it, set the `innodb_buffer_pool_dump_at_shutdown` and
`innodb_buffer_pool_load_at_startup` parameters to 1 in the parameter
group for your DB instance. Changing these parameter values in a parameter group affects
all MariaDB DB instances that use that parameter group. To enable cache warming for
specific MariaDB DB instances, you might need to create a new parameter group for those
DB instances. For information on parameter groups, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

Cache warming primarily provides a performance benefit for DB instances
that use standard storage. If you use PIOPS storage, you don't commonly see a
significant performance benefit.

###### Important

If your MariaDB DB instance doesn't shut down normally, such as during a
failover, then the buffer pool state isn't saved to disk. In this case, MariaDB
loads whatever buffer pool file is available when the DB instance is restarted. No
harm is done, but the restored buffer pool might not reflect the most recent state
of the buffer pool before the restart. To ensure that you have a recent state of the
buffer pool available to warm the cache on startup, we recommend that you
periodically dump the buffer pool "on demand." You can dump or load the buffer pool
on demand.

You can create an event to dump the buffer pool automatically and at a regular
interval. For example, the following statement creates an event named
`periodic_buffer_pool_dump` that dumps the buffer pool every
hour.

```
CREATE EVENT periodic_buffer_pool_dump
   ON SCHEDULE EVERY 1 HOUR
   DO CALL mysql.rds_innodb_buffer_pool_dump_now();
```

For more information, see [Events](http://mariadb.com/kb/en/mariadb/stored-programs-and-views-events/ "http://mariadb.com/kb/en/mariadb/stored-programs-and-views-events/") in the MariaDB documentation.

## Dumping and loading the buffer pool on demand

You can save and load the cache on demand using the following stored
procedures:

- To dump the current state of the buffer pool to disk, call the
  [mysql.rds_innodb_buffer_pool_dump_now](mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_dump_now "mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_dump_now")
  stored procedure.
- To load the saved state of the buffer pool from disk, call the
  [mysql.rds_innodb_buffer_pool_load_now](mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_load_now "mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_load_now")
  stored procedure.
- To cancel a load operation in progress, call the
  [mysql.rds_innodb_buffer_pool_load_abort](mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_load_abort "mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_load_abort")
  stored procedure.
