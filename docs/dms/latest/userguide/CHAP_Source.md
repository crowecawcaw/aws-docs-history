# Using IBM Db2 for Linux, Unix, Windows, and Amazon RDS database

(Db2 LUW) as a source for AWS DMS

You can migrate data from an IBM Db2 for Linux, Unix, Windows, and Amazon RDS (Db2 LUW) database
to any supported target database using AWS Database Migration Service (AWS DMS).

For information about versions of Db2 on Linux, Unix, Windows, and RDS that AWS DMS supports as a source,
see [Sources for AWS DMS](CHAP_Introduction.md "CHAP_Introduction.md").

You can use Secure Sockets Layer (SSL) to encrypt connections between your Db2 LUW
endpoint and the replication instance. For more information on using SSL with a Db2 LUW
endpoint, see [Using SSL with AWS Database Migration Service](CHAP_Security.md "CHAP_Security.md").

When AWS DMS reads data from an IBM Db2 source database, it uses the default isolation level
CURSOR STABILITY (CS) for Db2 version 9.7 and above. For more information, see [IBM Db2 for Linux, UNIX and Windows](https://www.ibm.com/docs/en/db2/12.1.0 "https://www.ibm.com/docs/en/db2/12.1.0")
documentation.

## Prerequisites when using Db2 LUW as

a source for AWS DMS

The following prerequisites are required before you can use an Db2 LUW database as
a source.

To enable ongoing replication, also called change data capture (CDC), do the
following:

- Set the database to be recoverable, which AWS DMS requires to capture
  changes. A database is recoverable if either or both of the database
  configuration parameters `LOGARCHMETH1` and `LOGARCHMETH2`
  are set to `ON`.

If your database is recoverable, then AWS DMS can access the Db2
`ARCHIVE LOG` if needed.

- Ensure that the DB2 transaction logs are available, with a sufficient
  retention period to be processed by AWS DMS.
- DB2 requires `SYSADM` or `DBADM` authorization to
  extract transaction log records. Grant the user account the following
  permissions:
  - `SYSADM` or `DBADM`
  - `DATAACCESS`

###### Note

For full-load only tasks, the DMS user account needs DATAACCESS permission.

- When using IBM DB2 for LUW version 9.7 as a source, set the extra
  connection attribute (ECA), `CurrentLSN` as follows:

`CurrentLSN=`LSN`where
`LSN`` specifies a log sequence
 number (LSN) where you want the replication to start. Or,
 `CurrentLSN=`scan``.

- When using Amazon RDS for Db2 LUW as a source, ensure that the archive logs are available to AWS DMS.
  Because AWS-managed Db2 databases purge the archive logs as soon as possible, you should
  increase the length of time that the logs remain available. For example, to increase log
  retention to 24 hours, run the following command:

```
db2 "call rdsadmin.set_archive_log_retention( ?, 'TESTDB', '24')"
```

For more information about Amazon RDS for Db2 LUW procedures,
see the [Amazon RDS for Db2 stored procedure reference](../../../AmazonRDS/latest/UserGuide/db2-stored-procedures.md "../../../AmazonRDS/latest/UserGuide/db2-stored-procedures.md") in the _Amazon Relational Database Service User Guide_.

- Grant the following privileges if you use DB2 specific premigration
  assessments:

```
GRANT CONNECT ON DATABASE TO USER <DMS_USER>;
GRANT SELECT ON SYSIBM.SYSDUMMY1 TO USER <DMS_USER>;
GRANT SELECT ON SYSIBMADM.ENV_INST_INFO TO USER <DMS_USER>;
GRANT SELECT ON SYSIBMADM.DBCFG TO USER <DMS_USER>;
GRANT SELECT ON SYSCAT.SCHEMATA TO USER <DMS_USER>;
GRANT SELECT ON SYSCAT.COLUMNS TO USER <DMS_USER>;
GRANT SELECT ON SYSCAT.TABLES TO USER <DMS_USER>;
GRANT EXECUTE ON FUNCTION SYSPROC.AUTH_LIST_AUTHORITIES_FOR_AUTHID TO <DMS_USER>;
GRANT EXECUTE ON PACKAGE NULLID.SYSSH200 TO USER <DMS_USER>;
```

## Limitations when using Db2 LUW as a

source for AWS DMS

AWS DMS doesn't support clustered databases. However, you can define a separate
Db2 LUW for each of the endpoints of a cluster. For example, you can create a Full Load
migration task with any one of the nodes in the cluster, then create separate tasks from
each node.

AWS DMS doesn't support the `BOOLEAN` data type in your source Db2 LUW
database.

When using ongoing replication (CDC), the following limitations apply:

- When a table with multiple partitions is truncated, the number of DDL
  events shown in the AWS DMS console is equal to the number of partitions. This
  is because Db2 LUW records a separate DDL for each partition.
- The following DDL actions aren't supported on partitioned
  tables:
  - ALTER TABLE ADD PARTITION
  - ALTER TABLE DETACH PARTITION
  - ALTER TABLE ATTACH PARTITION

- AWS DMS doesn't support an ongoing replication migration from a DB2
  high availability disaster recovery (HADR) standby instance. The standby is
  inaccessible.
- The DECFLOAT data type isn't supported. Consequently, changes to
  DECFLOAT columns are ignored during ongoing replication.
- The RENAME COLUMN statement isn't supported.
- When performing updates to Multi-Dimensional Clustering (MDC) tables, each
  update is shown in the AWS DMS console as INSERT + DELETE.
- When the task setting **Include LOB columns in
  replication** isn't enabled, any table that has LOB
  columns is suspended during ongoing replication.
- For Db2 LUW versions 10.5 and higher, variable-length string columns with
  data that is stored out-of-row are ignored. This limitation only applies to
  tables created with extended row size for columns with data types like VARCHAR
  and VARGRAPHIC. To work around this limitation, move the table to a table space
  with a higher page size. For more information, see
  [What can I do if I want to change the pagesize of DB2 tablespaces](https://www.ibm.com/support/pages/what-can-i-do-if-i-want-change-pagesize-db2-tablespaces " https://www.ibm.com/support/pages/what-can-i-do-if-i-want-change-pagesize-db2-tablespaces ").
- For ongoing replication, DMS doesn't support migrating data loaded at
  the page level by the DB2 LOAD utility. Instead, use the IMPORT utility
  which uses SQL inserts. For more information, see [differences between the import and load utilities](https://www.ibm.com/docs/en/db2/11.1?topic=utilities-differences-between-import-load-utility " https://www.ibm.com/docs/en/db2/11.1?topic=utilities-differences-between-import-load-utility").
- While a replication task is running, DMS captures CREATE TABLE DDLs only
  if the tables were created with the DATA CAPTURE CHANGE attribute.
- DMS has the following limitations when using the Db2 Database Partition Feature (DPF):
  - DMS can't coordinate transactions across Db2 nodes in a DPF environment. This is due to constraints
    within the IBM DB2READLOG API interface. In DPF, transactions may span multiple Db2 nodes, depending upon how
    DB2 partitions the data. As a result, your DMS solution must capture transactions from each Db2 node independently.
  - DMS can capture local transactions from each Db2 node in the DPF cluster by setting `connectNode`
    to `1` on multiple DMS source endpoints. This configuration corresponds to logical node numbers defined
    in the DB2 server configuration file `db2nodes.cfg`.
  - Local transactions on individual Db2 nodes may be parts of a larger, global transaction.
    DMS applies each local transaction independently on the target, without coordination
    with transactions on other Db2 nodes. This independent processing can lead to complications, especially
    when rows are moved between partitions.
  - When DMS replicates from multiple Db2 nodes, there is no assurance of the correct order
    of operations on the target, because DMS applies operations independently for each Db2 node. You
    must ensure that capturing local transactions independently
    from each Db2 node works for your specific use case.
  - When migrating from a DPF environment, we recommend first running a Full Load task without
    cached events, and then running CDC-only tasks.
    We recommend running one task per Db2 node, starting from the Full Load start timestamp or LRI (log record
    identifier) you set using the
    `StartFromContext` endpoint setting. For information about determining your replication
    start point, see [Finding the LSN or LRI value for replication start](https://www.ibm.com/support/pages/db2-finding-lsn-or-lri-value-replication-start "https://www.ibm.com/support/pages/db2-finding-lsn-or-lri-value-replication-start") in the _IBM Support documentation_.

- For ongoing replication (CDC), if you plan to start replication from a specific timestamp,
  you must set the `StartFromContext` connection attribute to the required timestamp.
- Currently, DMS doesn't support the Db2 pureScale Feature, an extension of DB2 LUW that
  you can use to scale your database solution.
- The `DATA CAPTURE CHANGES` table option is a crucial prerequisite for DB2 data replication processes.
  Neglecting to enable this option when creating tables can cause missing data, especially for CDC (Change Data Capture) only
  replication tasks initiated from an earlier starting point. AWS DMS will enable this attribute by default when restarting a CDC or FULL+CDC task.
  However, any changes made in the source database before the task restart may be missed.

```
ALTER TABLE TABLE_SCHEMA.TABLE_NAME DATA CAPTURE CHANGES INCLUDE LONGVAR COLUMNS;
```

## Endpoint settings when

using Db2 LUW as a source for AWS DMS

You can use endpoint settings to configure your Db2 LUW source database similar to using
extra connection attributes. You specify the settings when you create the source
endpoint using the AWS DMS console, or by using the `create-endpoint` command in the
[AWS CLI](../../../cli/latest/reference/dms/index.md "../../../cli/latest/reference/dms/index.md"), with the
`--ibm-db2-settings '{"`EndpointSetting"`:
 `"value"`, `...`}'` JSON syntax.

The following table shows the endpoint settings that you can use with
Db2 LUW as a source.

| Name                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CurrentLSN`            | For ongoing replication (CDC), use `CurrentLSN` to<br>specify a log sequence number (LSN) where you want the<br>replication to start.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `ConnectionTimeout`     | Use this extra connection attribute (ECA) to set the endpoint<br>connection timeout for the Db2 LUW endpoint, in seconds. The default<br>value is 10 seconds. ECA Example:<br>`ConnectionTimeout=30`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `MaxKBytesPerRead`      | Maximum number of bytes per read, as a NUMBER value. The<br>default is 64 KB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `SetDataCaptureChanges` | Enables ongoing replication (CDC) as a BOOLEAN value. The<br>default is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `StartFromContext`      | For ongoing replication (CDC), use<br>`StartFromContext` to specify a log's lower limit<br>from where to start the replication.<br>`StartFromContext` accepts different forms of<br>values. Valid values include:<br>• `timestamp` (UTC). For example:<br>`<br>'{"StartFromContext": "timestamp:2021-09-21T13:00:00"}'<br>`<br>• `NOW`<br>For IBM DB2 LUW version 10.5 and higher, NOW combined<br>with CurrentLSN: scan, starts the task from the latest LSO. For example:<br>`<br>'{"CurrentLSN": "scan", "StartFromContext": "NOW"}'<br>`<br>• A specific LRI. For example:<br>`<br>'{"StartFromContext": "0100000000000022CC000000000004FB13"}'<br>`<br>To determine the LRI/LSN range of a log file, run the<br>`db2flsn` command as shown in the example<br>following.<br>``<br>db2flsn -db `SAMPLE` -lrirange 2<br>``<br>The output from that example is similar to the following.<br>`<br>S0000002.LOG: has LRI range 00000000000000010000000000002254000000000004F9A6 to<br>000000000000000100000000000022CC000000000004FB13<br>`<br>In that output, the log file is S0000002.LOG and the \*_StartFromContext_<br>• LRI value is the 34<br>bytes at the end of the range.<br>`<br>0100000000000022CC000000000004FB13<br>` |
| `executeTimeout`        | Extra connection attribute which sets the statement (query) timeout for the DB2 LUW endpoint, in seconds. The default value is 60 seconds. ECA Example: `executeTimeout=120;`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Source data types for IBM Db2

LUW

Data migration that uses Db2 LUW as a source for AWS DMS supports most Db2 LUW data
types. The following table shows the Db2 LUW source data types that are supported
when using AWS DMS and the default mapping from AWS DMS data types. For more information
about Db2 LUW data types, see the [Db2 LUW documentation](https://www.ibm.com/support/knowledgecenter/SSEPGG_10.5.0/com.ibm.db2.luw.sql.ref.doc/doc/r0008483.html "https://www.ibm.com/support/knowledgecenter/SSEPGG_10.5.0/com.ibm.db2.luw.sql.ref.doc/doc/r0008483.html").

For information on how to view the data type that is mapped in the target, see the
section for the target endpoint that you're using.

For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.md "CHAP_Reference.md").

| Db2 LUW data types        | AWS DMS data types                                                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| INTEGER                   | INT4                                                                                                                             |
| SMALLINT                  | INT2                                                                                                                             |
| BIGINT                    | INT8                                                                                                                             |
| DECIMAL (p,s)             | NUMERIC (p,s)                                                                                                                    |
| FLOAT                     | REAL8                                                                                                                            |
| DOUBLE                    | REAL8                                                                                                                            |
| REAL                      | REAL4                                                                                                                            |
| DECFLOAT (p)              | If precision is 16, then REAL8; if precision is 34, then<br>STRING                                                               |
| GRAPHIC (n)               | WSTRING, for fixed-length graphic strings of double byte chars<br>with a length greater than 0 and less than or equal to<br>127  |
| VARGRAPHIC (n)            | WSTRING, for varying-length graphic strings with a length<br>greater than 0 and less than or equal to16,352 double byte<br>chars |
| LONG VARGRAPHIC (n)       | CLOB, for varying-length graphic strings with a length greater<br>than 0 and less than or equal to16,352 double byte chars       |
| CHARACTER (n)             | STRING, for fixed-length strings of double byte chars with a<br>length greater than 0 and less than or equal to 255              |
| VARCHAR (n)               | STRING, for varying-length strings of double byte chars with a<br>length greater than 0 and less than or equal to 32,704         |
| LONG VARCHAR (n)          | CLOB, for varying-length strings of double byte chars with a<br>length greater than 0 and less than or equal to 32,704           |
| CHAR (n) FOR BIT DATA     | BYTES                                                                                                                            |
| VARCHAR (n) FOR BIT DATA  | BYTES                                                                                                                            |
| LONG VARCHAR FOR BIT DATA | BYTES                                                                                                                            |
| DATE                      | DATE                                                                                                                             |
| TIME                      | TIME                                                                                                                             |
| TIMESTAMP                 | DATETIME                                                                                                                         |
| BLOB (n)                  | BLOB<br>Maximum length is 2,147,483,647 bytes                                                                                    |
| CLOB (n)                  | CLOB<br>Maximum length is 2,147,483,647 bytes                                                                                    |
| DBCLOB (n)                | CLOB<br>Maximum length is 1,073,741,824 double byte chars                                                                        |
| XML                       | CLOB                                                                                                                             |
