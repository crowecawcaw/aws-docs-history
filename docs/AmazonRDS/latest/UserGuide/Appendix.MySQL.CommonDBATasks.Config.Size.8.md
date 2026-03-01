# Configuring buffer pool size and redo log capacity in MySQL 8.4

In MySQL 8.4, Amazon RDS enables the `innodb_dedicated_server` parameter by
default. With the `innodb_dedicated_server` parameter, the database engine
calculates the `innodb_buffer_pool_size` and
`innodb_redo_log_capacity` parameters. For information about how these
parameters are calculated, see [Configuring InnoDB Buffer Pool Size](https://dev.mysql.com/doc/refman/8.4/en/innodb-buffer-pool-resize.html "https://dev.mysql.com/doc/refman/8.4/en/innodb-buffer-pool-resize.html") and [Redo Log](https://dev.mysql.com/doc/refman/8.4/en/innodb-redo-log.html "https://dev.mysql.com/doc/refman/8.4/en/innodb-redo-log.html")
in the MySQL documentation.

With `innodb_dedicated_server` enabled, the
`innodb_buffer_pool_size` parameter is calculated based on the DB
instance class memory. The following table shows the detected server memory and the
corresponding buffer pool size.

| Detected server memory | Buffer pool size                    |
| ---------------------- | ----------------------------------- |
| < 1 GB                 | Default value of 128 MB             |
| 1 GB to 4 GB           | `Detected server memory` \<br>• 0.5 |
| > 4 GB                 | `Detected server memory` \*<br>0.75 |

The `innodb_redo_log_capacity` parameter automatically scales with the
instance class to (number of vCPUs / 2) GB up to a maximum of 16 GB. Larger instance
classes have a larger redo log capacity, which can improve performance and resilience
for write-intensive workloads.

Before upgrading from MySQL 8.0 to MySQL 8.4, be sure to increase your storage space
to accommodate a potential increase in the size of the redo logs that might occur after
the upgrade completes. For more information, see [Increasing DB instance storage capacity](USER_PIOPS.md "USER_PIOPS.md").

If you don't want the `innodb_dedicated_server` parameter to calculate the
values for the `innodb_buffer_pool_size` and
`innodb_redo_log_capacity` parameters, you can override these values by
setting specific values for them in a custom parameter group. Alternatively, you can
disable the `innodb_dedicated_server` parameter and set values for the
`innodb_buffer_pool_size` and `innodb_redo_log_capacity`
parameters in a custom parameter group. For more information, see [Default and custom parameter groups](parameter-groups-overview.md#parameter-groups-overview.custom "parameter-groups-overview.md#parameter-groups-overview.custom").

If you disable the `innodb_dedicated_server` parameter by setting it to
`0` and don't set values for the `innodb_buffer_pool_size` and
`innodb_redo_log_capacity` parameters, then Amazon RDS sets the latter two
parameters to 128 MB and 100 MB, respectively. These defaults result in poor performance
on larger instance classes.
