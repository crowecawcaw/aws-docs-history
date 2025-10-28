# Troubleshooting out-of-memory issues for Aurora MySQL databases

The Aurora MySQL `aurora_oom_response` instance-level parameter can enable the DB instance to monitor the system memory and estimate
the memory consumed by various statements and connections. If the system runs low on memory, it can perform a list of actions to attempt to
release that memory. It does so in an attempt to avoid a database restart due to out-of-memory (OOM) issues. The instance-level parameter takes
a string of comma-separated actions that a DB instance performs when its memory is low. The `aurora_oom_response` parameter is
supported for Aurora MySQL versions 2 and 3.

The following values, and combinations of them, can be used for the `aurora_oom_response` parameter. An empty string means that no
action is taken, and effectively turns off the feature, leaving the database prone to OOM restarts.

- `decline` – Declines new queries when the DB instance is low on memory.
- `kill_connect` – Closes database connections that are consuming a large amount of memory, and ends current
  transactions and Data Definition Language (DDL) statements. This response isn't supported for Aurora MySQL version 2.

For more information, see [KILL statement](https://dev.mysql.com/doc/refman/8.0/en/kill.html "https://dev.mysql.com/doc/refman/8.0/en/kill.html") in the MySQL
documentation.

- `kill_query` – Ends queries in descending order of memory consumption until the instance memory surfaces above the
  low threshold. DDL statements aren't ended.

For more information, see [KILL statement](https://dev.mysql.com/doc/refman/8.0/en/kill.html "https://dev.mysql.com/doc/refman/8.0/en/kill.html") in the MySQL
documentation.

- `print` – Only prints the queries that are consuming a large amount of memory.
- `tune` – Tunes the internal table caches to release some memory back to the system. Aurora MySQL decreases the memory
  used for caches such as `table_open_cache` and `table_definition_cache` in low-memory conditions. Eventually,
  Aurora MySQL sets their memory usage back to normal when the system is no longer low on memory.

For more information, see [table_open_cache](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_table_open_cache "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_table_open_cache") and [table_definition_cache](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_table_definition_cache "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_table_definition_cache") in the MySQL documentation.

- `tune_buffer_pool` – Decreases the size of the buffer pool to release some memory and make it available for the
  database server to process connections. This response is supported for Aurora MySQL version 3.06 and higher.

You must pair `tune_buffer_pool` with either `kill_query` or `kill_connect` in the
`aurora_oom_response` parameter value. If not, buffer pool resizing won't happen, even when you include
`tune_buffer_pool` in the parameter value.
In Aurora MySQL versions lower than 3.06, for DB instance classes with memory less than or equal to 4 GiB, when the instance is under memory
pressure, the default actions include `print`, `tune`, `decline`, and `kill_query`. For DB instance
classes with memory greater than 4 GiB, the parameter value is empty by default (disabled).

In Aurora MySQL version 3.06 and higher, for DB instance classes with memory less than or equal to 4 GiB, Aurora MySQL also closes the top
memory-consuming connections (`kill_connect`). For DB instance classes with memory greater than 4 GiB, the default parameter value is
`print`.

In Aurora MySQL version 3.09 and higher, for DB instance classes with memory greater than 4 GiB, the default parameter value is `print,decline,kill_connect`.

If you frequently run into out-of-memory issues, memory usage can be monitored using [memory summary tables](https://dev.mysql.com/doc/refman/8.3/en/performance-schema-memory-summary-tables.html "https://dev.mysql.com/doc/refman/8.3/en/performance-schema-memory-summary-tables.html") when
`performance_schema` is enabled.

For Amazon CloudWatch metrics related to OOM, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances"). For global status variables related to OOM, see [Aurora MySQL global status variables](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md").
