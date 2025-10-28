# Oracle Endpoint Troubleshooting

This section contains replication scenarios specific to Oracle.

## Source reading paused

AWS DMS pauses reading from an Oracle source in the following scenarios. This behavior is by design. You
can investigate the causes for this using the task log. Look for messages similar to the following in the task log.
For information about working with the task log, see
[Viewing and managing AWS DMS task logs](CHAP_Monitoring.md#CHAP_Monitoring.ManagingLogs "CHAP_Monitoring.md#CHAP_Monitoring.ManagingLogs").

- **SORTER message**: This indicates that DMS is caching transactions
  on the replication instance. For more information, see [SORTER message in task log](CHAP_Troubleshooting_Latency_Target.md#CHAP_Troubleshooting_Latency_Target_Sorter "CHAP_Troubleshooting_Latency_Target.md#CHAP_Troubleshooting_Latency_Target_Sorter") following.
- **Debug task logs**: If DMS interrupts the read process, your task
  repeatedly writes the following message to the debug task logs, without a change to the context field or timestamp:
  - **Binary reader**:

  ```
  [SOURCE_CAPTURE  ]T:  Produce CTI event:
  context '00000020.f23ec6e5.00000002.000a.00.0000:190805.3477731.16'
  xid [00000000001e0018] timestamp '2021-07-19 06:57:55'
  thread 2  (oradcdc_oralog.c:817)

  ```

  - **Logminer**:

  ```
  [SOURCE_CAPTURE  ]T:  Produce INSERT event:
  object id 1309826 context '000000000F2CECAA010000010005A8F500000275016C0000000000000F2CEC58'
  xid [000014e06411d996] timestamp '2021-08-12 09:20:32' thread 1  (oracdc_reader.c:2269)
  ```

- AWS DMS logs the following message for every new redo or archived log operation.

```
00007298: 2021-08-13T22:00:34 [SOURCE_CAPTURE ]I: Start processing archived Redo log sequence 14850 thread 2 name XXXXX/XXXXX/ARCHIVELOG/2021_08_14/thread_2_seq_14850.22977.1080547209 (oradcdc_redo.c:754)
```

If the source has new redo or archived log operations, and AWS DMS is not writing these messages to the log,
this means that the task is not processing events.

## High redo generation

If your task is processing redo or archived logs, but the source latency remains high, try to identify
the redo log generation rate and generation patterns. If you have a high level of redo log generation, this increases
source latency, because your task reads all of the redo and archive logs in order to fetch changes related to the
replicated tables.

To determine the redo generation rate, use the following queries.

- Per-day redo generation rate:

```
select trunc(COMPLETION_TIME,'DD') Day, thread#,
round(sum(BLOCKS*BLOCK_SIZE)/1024/1024/1024) GB,
count(*) Archives_Generated from v$archived_log
where completion_time > sysdate- 1
group by trunc(COMPLETION_TIME,'DD'),thread# order by 1;
```

- Per-hour redo generation rate:

```
Alter session set nls_date_format = 'DD-MON-YYYY HH24:MI:SS';
select trunc(COMPLETION_TIME,'HH') Hour,thread# ,
round(sum(BLOCKS*BLOCK_SIZE)/1024/1024) "REDO PER HOUR (MB)",
count(*) Archives from v$archived_log
where completion_time > sysdate- 1
group by trunc(COMPLETION_TIME,'HH'),thread#  order by 1 ;
```

To troubleshoot latency in this scenario, check the following:

- Check the network bandwidth and single-thread performance of your replication to ensure that your
  underlying network can support the source redo generation rate. For information about how network bandwidth can affect
  replication performance, see [Network speed and bandwidth](CHAP_Troubleshooting_Latency.md#CHAP_Troubleshooting_Latency_Causes_Replication_Network "CHAP_Troubleshooting_Latency.md#CHAP_Troubleshooting_Latency_Causes_Replication_Network") prior.
- Check if you set up supplemental logging correctly. Avoid extra logging on the source, such as
  enabling logging on all columns of a table. For information about
  setting up supplemental logging, see [Setting up supplemental logging](CHAP_Source.md#CHAP_Source.Oracle.Self-Managed.Configuration.SupplementalLogging "CHAP_Source.md#CHAP_Source.Oracle.Self-Managed.Configuration.SupplementalLogging").
- Verify that you are using the correct API to read the redo or archved logs. You can use
  either Oracle LogMiner or AWS DMS Binary Reader. While LogMiner reads the online redo logs and archived
  redo log files, Binary Reader reads and parses the raw redo log files directly. As a result, Binary Reader
  is more performant. We recommend that you use Binary Reader if your redo log generation is more than 10 GB/ hour.
  For more information, see [Using Oracle LogMiner or AWS DMS Binary
  Reader for CDC](CHAP_Source.md#CHAP_Source.Oracle.CDC "CHAP_Source.md#CHAP_Source.Oracle.CDC").
- Check if you set `ArchivedLogsOnly` to `Y`. If this endpoint setting is set,
  AWS DMS reads from the archived redo logs. This increases source latency, because AWS DMS waits for the online redo log
  to be archived before reading. For more information, see [ArchivedLogsOnly](../APIReference/API_OracleSettings.md#DMS-Type-OracleSettings-ArchivedLogsOnly "../APIReference/API_OracleSettings.md#DMS-Type-OracleSettings-ArchivedLogsOnly").
- If your Oracle source uses Automatic Storage Management (ASM), see
  [Storing REDO on Oracle ASM
  when using Oracle as a source for AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.REDOonASM "CHAP_Source.md#CHAP_Source.Oracle.REDOonASM") for information about
  how to properly configure your data store. You may also be able to optimize reading performance further
  by using the `asmUsePLSQLArray` extra connection attrribute (ECA). For information about using
  `asmUsePLSQLArray`, see [Endpoint settings
  when using Oracle as a source for AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.ConnectionAttrib "CHAP_Source.md#CHAP_Source.Oracle.ConnectionAttrib").
