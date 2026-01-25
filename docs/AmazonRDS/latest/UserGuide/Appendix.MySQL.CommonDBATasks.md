# Skipping the current

replication error for RDS for MySQL

You can skip an error on your read replica if the error is causing your read replica
to stop responding and the error doesn't affect the integrity of your data.

###### Note

First verify that the error in question can be safely skipped. In a MySQL utility,
connect to the read replica and run the following MySQL command.

```
SHOW REPLICA STATUS\G
```

For information about the values returned, see [the MySQL
documentation](https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html "https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html").

Previous versions of and MySQL used `SHOW SLAVE STATUS` instead of
`SHOW REPLICA STATUS`. If you are using a MySQL version before
8.0.23, then use `SHOW SLAVE STATUS`.

You can skip an error on your read replica in the following ways.

###### Topics

- [Calling the
  mysql.rds_skip_repl_error procedure](#Appendix.MySQL.CommonDBATasks.SkipError.procedure "#Appendix.MySQL.CommonDBATasks.SkipError.procedure")
- [Setting the
  slave_skip_errors parameter](#Appendix.MySQL.CommonDBATasks.SkipError.parameter "#Appendix.MySQL.CommonDBATasks.SkipError.parameter")

## Calling the

mysql.rds_skip_repl_error procedure

Amazon RDS provides a stored procedure that you can call to skip an error on your read
replicas. First connect to your read replica, then issue the appropriate commands as
shown following. For more information, see [Connecting to your MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md").

To skip the error, issue the following command.

```
CALL mysql.rds_skip_repl_error;
```

This command has no effect if you run it on the source DB instance, or on a read
replica that hasn't encountered a replication error.

For more information, such as the versions of MySQL that support
`mysql.rds_skip_repl_error`, see [mysql.rds_skip_repl_error](mysql-stored-proc-replicating.md#mysql_rds_skip_repl_error "mysql-stored-proc-replicating.md#mysql_rds_skip_repl_error").

###### Important

If you attempt to call `mysql.rds_skip_repl_error` and encounter
the following error: `ERROR 1305 (42000): PROCEDURE
 mysql.rds_skip_repl_error does not exist`, then upgrade your MySQL DB
instance to the latest minor version or one of the minimum minor versions listed
in [mysql.rds_skip_repl_error](mysql-stored-proc-replicating.md#mysql_rds_skip_repl_error "mysql-stored-proc-replicating.md#mysql_rds_skip_repl_error").

## Setting the

slave_skip_errors parameter

To skip one or more errors, you can set the `slave_skip_errors` static
parameter on the read replica. You can set this parameter to skip one or more
specific replication error codes. Currently, you can set this parameter only for
RDS for MySQL 5.7 DB instances. After you change the setting for this parameter, make
sure to reboot your DB instance for the new setting to take effect. For information
about setting this parameter, see the [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/replication-options-replica.html#sysvar_slave_skip_errors "https://dev.mysql.com/doc/refman/5.7/en/replication-options-replica.html#sysvar_slave_skip_errors").

We recommend setting this parameter in a separate DB parameter group. You can
associate this DB parameter group only with the read replicas that need to skip
errors. Following this best practice reduces the potential impact on other DB
instances and read replicas.

###### Important

Setting a nondefault value for this parameter can lead to replication
inconsistency. Only set this parameter to a nondefault value if you have
exhausted other options to resolve the problem and you are sure of the potential
impact on your read replica's data.
