# MySQL Endpoint Troubleshooting

This section contains replication scenarios specific to MySQL. AWS DMS scans the MySQL binary log periodically
to replicate changes. This process can increase latency in the following scenarios:

###### Topics

- [Long-running transaction on source](#CHAP_Troubleshooting_Latency_Source_MySQL_Longrunning "#CHAP_Troubleshooting_Latency_Source_MySQL_Longrunning")
- [High workload on source](#CHAP_Troubleshooting_Latency_Source_MySQL_Highworkload "#CHAP_Troubleshooting_Latency_Source_MySQL_Highworkload")
- [Binary log contention](#CHAP_Troubleshooting_Latency_Source_MySQL_Binarylog "#CHAP_Troubleshooting_Latency_Source_MySQL_Binarylog")

## Long-running transaction on source

Since MySQL only writes committed transactions to the binary log, long-running transactions cause latency
spikes proportional to the query run time.

To identify long-running transactions, use the following query, or use the slow query log:

```
SHOW FULL PROCESSLIST;
```

For information about using the slow query log, see
[The Slow Query Log](https://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html "https://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html")
in the [MySQL documentation](https://dev.mysql.com/doc/ "https://dev.mysql.com/doc/").

To avoid latency spikes from long-running transactions, restructure your source transactions to either reduce the query
run time or increase your commit frequency.

## High workload on source

Because DMS CDC is single-threaded, a large number of transactions can increase source latency.
To identify if source latency is due to a heavy workload, compare the number and size of the binary logs
generated during the latency period to the logs generated before the latency. To check the binary logs,
and DMS CDC thread status, use the following queries:

```
SHOW BINARY LOGS;
SHOW PROCESSLIST;
```

For more information about CDC binary log dump thread states, see
[Replication Source Thread States](https://dev.mysql.com/doc/refman/8.0/en/source-thread-states.html "https://dev.mysql.com/doc/refman/8.0/en/source-thread-states.html") .

You can determine the latency by comparing the latest binary log position generated on the source with the
event DMS is currently processing. To identify the latest binary log on the source, do the following:

- Enable debug logs on the SOURCE_CAPTURE component.
- Retrieve the DMS processing binary log and position details from the the task debug logs.
- Use the following query to identify the latest binary log on the source:

```
SHOW MASTER STATUS;
```

To further optimize performance, tune the `EventsPollInterval`. By default, DMS polls
the binary log every 5 seconds, but you may improve performance by reducing this value. For more information
about the `EventsPollInterval` setting, see
[Endpoint settings
when using MySQL as a source for AWS DMS](CHAP_Source.md#CHAP_Source.MySQL.ConnectionAttrib "CHAP_Source.md#CHAP_Source.MySQL.ConnectionAttrib").

## Binary log contention

When migrating multiple tables with a large amount of data, we recommend splitting tables into separate
tasks for MySQL 5.7.2 or later. In MySQL versions 5.7.2 and later, the master dump thread creates fewer lock
contentions and improves throughput. As a result, the dump thread no longer locks the binary log whenever it reads an event. This
means that multiple dump threads can read the binary log file concurrently. This also means that
dump threads can read the binary log while clients write to it. For more information about dump threads, see
[Replication Threads](https://dev.mysql.com/doc/refman/8.0/en/replication-threads.html "https://dev.mysql.com/doc/refman/8.0/en/replication-threads.html")
and the [MySQL 5.7.2 release notes](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-2.html "https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-2.html").

To improve replication performance for MySQL sources versions prior to 5.7.2, try consolidating tasks with
CDC components.
