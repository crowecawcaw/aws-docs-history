# Warming the InnoDB cache

The following stored procedures save, load, or cancel loading the InnoDB buffer pool on RDS for MySQL DB instances. For more
information, see [InnoDB cache warming for MySQL on Amazon RDS](MySQL.Concepts.FeatureSupport.md#MySQL.Concepts.InnoDBCacheWarming "MySQL.Concepts.FeatureSupport.md#MySQL.Concepts.InnoDBCacheWarming").

###### Topics

- [mysql.rds\_innodb\_buffer\_pool\_dump\_now](#mysql_rds_innodb_buffer_pool_dump_now "#mysql_rds_innodb_buffer_pool_dump_now")
- [mysql.rds\_innodb\_buffer\_pool\_load\_abort](#mysql_rds_innodb_buffer_pool_load_abort "#mysql_rds_innodb_buffer_pool_load_abort")
- [mysql.rds\_innodb\_buffer\_pool\_load\_now](#mysql_rds_innodb_buffer_pool_load_now "#mysql_rds_innodb_buffer_pool_load_now")

## mysql.rds\_innodb\_buffer\_pool\_dump\_now

Dumps the current state of the buffer pool to disk.

### Syntax

```
CALL mysql.rds_innodb_buffer_pool_dump_now();
```

### Usage notes

The master user must run the `mysql.rds_innodb_buffer_pool_dump_now`
procedure.

## mysql.rds\_innodb\_buffer\_pool\_load\_abort

Cancels a load of the saved buffer pool state while in progress.

### Syntax

```
CALL mysql.rds_innodb_buffer_pool_load_abort();
```

### Usage notes

The master user must run the `mysql.rds_innodb_buffer_pool_load_abort`
procedure.

## mysql.rds\_innodb\_buffer\_pool\_load\_now

Loads the saved state of the buffer pool from disk.

### Syntax

```
CALL mysql.rds_innodb_buffer_pool_load_now();
```

### Usage notes

The master user must run the `mysql.rds_innodb_buffer_pool_load_now` procedure.
