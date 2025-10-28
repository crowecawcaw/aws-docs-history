# mysql.rds_execute_operation

Executes InnoDB operations to manage buffer pool states and temporary tablespace.
This procedure can be used to dynamically control InnoDB operations such as dumping and loading buffer pool states or truncating temporary tablespace.

## Syntax

```
CALL mysql.rds_execute_operation(*operation*);
```

## Parameters

_operation_

String. The InnoDB operations to execute. Valid values are:

- _innodb_buffer_pool_dump_now_ - Operation that dumps the current state of the buffer pool.
- _innodb_buffer_pool_load_now_ - Operation that loads the saved buffer pool state.
- _innodb_buffer_pool_load_abort_ - Operation that aborts a buffer pool load operation.
- _innodb_truncate_temporary_tablespace_now_ - Operation that truncates the temporary tablespace.

## Usage notes

This procedure is only supported for MariaDB DB instances running MariaDB version 11.8 and higher.

During execution, binary logging is temporarily disabled to prevent replication of these administrative commands.

The procedure maintains an audit trail by logging all operations in the [`mysql.rds_history`](https://mariadb.com/docs/server/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/securing-connections-for-client-and-server#requiring-tls "https://mariadb.com/docs/server/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/securing-connections-for-client-and-server#requiring-tls") table.

## Examples

The following example demonstrates temporary tablespace shrinking using `mysql.rds_execute_operation`:

To check current temporary tablespace size, run the following query:

````

SELECT FILE_SIZE FROM information_schema.innodb_sys_tablespaces WHERE name LIKE 'innodb_temporary';
+------------+
| FILE_SIZE  | +------------+
| 6723469312 |  -- 6.3 GB +------------+ ``` When you drop temporary tables, it doesn't reduce storage usage in the global tablespace. To reduce the size of the global tablespace, run the `mysql.rds_execute_operation` command to shrink the temporary tablespace. ``` CALL `mysql.rds_execute_operation('innodb_truncate_temporary_tablespace_now');` Query OK, 2 rows affected (0.004 sec) ``` After you run the procedure, verify that the space was reclaimed. ``` SELECT FILE_SIZE FROM information_schema.innodb_sys_tablespaces WHERE name LIKE 'innodb_temporary'; +-----------+
| FILE_SIZE | +-----------+
|  12582912 |  -- 12 MB +-----------+ ``` ###### Note The shrink operation might take time, depending on the temporary tablespace size and current workload. ###### Important The temporary tablespace shrinks only when all temporary tables that contributed to its size are no longer in use. We recommend that you run this procedure when there are no active temporary tablespaces on the instance.
````
