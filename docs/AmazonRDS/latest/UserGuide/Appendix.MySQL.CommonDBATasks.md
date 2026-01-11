# Managing the Global Status

History for RDS for MySQL

###### Tip

To analyze database performance, you can also use Performance Insights on Amazon RDS. For more
information, see [Monitoring DB load with Performance Insights on Amazon RDS](USER_PerfInsights.md "USER_PerfInsights.md").

MySQL maintains many status variables that provide information about its operation.
Their value can help you detect locking or memory issues on a DB instance. The values of
these status variables are cumulative since last time the DB instance was started. You
can reset most status variables to 0 by using the `FLUSH STATUS` command.

To allow for monitoring of these values over time, Amazon RDS provides a set of procedures
that will snapshot the values of these status variables over time and write them to a
table, along with any changes since the last snapshot. This infrastructure, called
Global Status History (GoSH), is installed on all MySQL DB instances starting with
versions 5.5.23. GoSH is disabled by default.

To enable GoSH, you first enable the event scheduler from a DB parameter group by
setting the parameter `event_scheduler` to `ON`. For MySQL DB
instances running MySQL 5.7, also set the parameter `show_compatibility_56`
to `1`. For information about creating and modifying a DB parameter group,
see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). For information about the side
effects of enabling this parameter, see [show_compatibility_56](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_show_compatibility_56 "https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_show_compatibility_56") in the _MySQL 5.7 Reference
Manual_.

You can then use the procedures in the following table to enable and configure GoSH.
First connect to your MySQL DB instance, then issue the appropriate commands as shown
following. For more information, see [Connecting to your MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md"). For each procedure, run the following
command and replace _`procedure-name`_:

```
CALL `procedure-name`;
```

The following table lists all of the procedures that you can use for _`procedure-name`_ in the previous
command.

| Procedure                                 | Description                                                                                                                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mysql.rds_enable_gsh_collector`          | Enables GoSH to take default snapshots at intervals specified by<br>`rds_set_gsh_collector`.                                                                                        |
| `mysql.rds_set_gsh_collector`             | Specifies the interval, in minutes, between snapshots. Default<br>value is 5.                                                                                                       |
| `mysql.rds_disable_gsh_collector`         | Disables snapshots.                                                                                                                                                                 |
| `mysql.rds_collect_global_status_history` | Takes a snapshot on demand.                                                                                                                                                         |
| `mysql.rds_enable_gsh_rotation`           | Enables rotation of the contents of the<br>`mysql.rds_global_status_history` table to<br>`mysql.rds_global_status_history_old` at intervals<br>specified by `rds_set_gsh_rotation`. |
| `mysql.rds_set_gsh_rotation`              | Specifies the interval, in days, between table rotations. Default<br>value is 7.                                                                                                    |
| `mysql.rds_disable_gsh_rotation`          | Disables table rotation.                                                                                                                                                            |
| `mysql.rds_rotate_global_status_history`  | Rotates the contents of the<br>`mysql.rds_global_status_history` table to<br>`mysql.rds_global_status_history_old` on demand.                                                       |

When GoSH is running, you can query the tables that it writes to. For example, to
query the hit ratio of the Innodb buffer pool, you would issue the following query:

```
select a.collection_end, a.collection_start, (( a.variable_Delta-b.variable_delta)/a.variable_delta)*100 as "HitRatio"
    from mysql.rds_global_status_history as a join mysql.rds_global_status_history as b on a.collection_end = b.collection_end
    where a. variable_name = 'Innodb_buffer_pool_read_requests' and b.variable_name = 'Innodb_buffer_pool_reads'
```
