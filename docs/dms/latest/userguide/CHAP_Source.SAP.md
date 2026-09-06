

# Using an SAP ASE database as a source for AWS DMS
<a name="CHAP_Source.SAP"></a>

You can migrate data from an SAP Adaptive Server Enterprise (ASE) database—formerly known as Sybase—using AWS DMS. With an SAP ASE database as a source, you can migrate data to any of the other supported AWS DMS target databases. 

For information about versions of SAP ASE that AWS DMS supports as a source, see [Sources for AWS DMS](CHAP_Introduction.Sources.md).

For additional details on working with SAP ASE databases and AWS DMS, see the following sections.

**Topics**
+ [Prerequisites for using an SAP ASE database as a source for AWS DMS](#CHAP_Source.SAP.Prerequisites)
+ [Limitations on using SAP ASE as a source for AWS DMS](#CHAP_Source.SAP.Limitations)
+ [Permissions required for using SAP ASE as a source for AWS DMS](#CHAP_Source.SAP.Security)
+ [Removing the truncation point](#CHAP_Source.SAP.Truncation)
+ [Endpoint settings when using SAP ASE as a source for AWS DMS](#CHAP_Source.SAP.ConnectionAttrib)
+ [Source data types for SAP ASE](#CHAP_Source.SAP.DataTypes)

## Prerequisites for using an SAP ASE database as a source for AWS DMS
<a name="CHAP_Source.SAP.Prerequisites"></a>

For an SAP ASE database to be a source for AWS DMS, do the following:
+ Enable SAP ASE replication for tables by using the `sp_setreptable` command. For more information, see [Sybase Infocenter Archive]( http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.dc32410_1501/html/refman/X37830.htm). 
+ Disable `RepAgent` on the SAP ASE database. For more information, see [Stop and disable the RepAgent thread in the primary database](http://infocenter-archive.sybase.com/help/index.jsp?topic=/com.sybase.dc20096_1260/html/mra126ag/mra126ag65.htm). 
+ To replicate to SAP ASE version 15.7 on an Windows EC2 instance configured for non-Latin characters (for example, Chinese), install SAP ASE 15.7 SP121 on the target computer.

**Note**  
For ongoing change data capture (CDC) replication, DMS runs `dbcc logtransfer` and `dbcc log` to read data from the transaction log.

## Limitations on using SAP ASE as a source for AWS DMS
<a name="CHAP_Source.SAP.Limitations"></a>

The following limitations apply when using an SAP ASE database as a source for AWS DMS:
+ You can run only one AWS DMS task with ongoing replication or CDC for each SAP ASE database. You can run multiple full-load-only tasks in parallel.
+ You can't rename a table. For example, the following command fails.

  ```
  sp_rename 'Sales.SalesRegion', 'SalesReg;
  ```
+ You can't rename a column. For example, the following command fails.

  ```
  sp_rename 'Sales.Sales.Region', 'RegID', 'COLUMN';
  ```
+ Zero values located at the end of binary data type strings are truncated when replicated to the target database. For example, `0x0000000000000000000000000100000100000000` in the source table becomes `0x00000000000000000000000001000001` in the target table.
+ If the database default is set not to allow NULL values, AWS DMS creates the target table with columns that don't allow NULL values. Consequently, if a full load or CDC replication task contains empty values, AWS DMS throws an error. You can prevent these errors by allowing NULL values in the source database by using the following commands.

  ```
  sp_dboption {{database_name}}, 'allow nulls by default', 'true'
  go
  use {{database_name}}
  CHECKPOINT
  go
  ```
+ The `reorg rebuild` index command isn't supported.
+ AWS DMS does not support clusters or using MSA (Multi-Site Availability)/Warm Standby as a source.
+ When `AR_H_TIMESTAMP` transformation header expression is used in mapping rules, the milliseconds won't be captured for an added column.
+ Running Merge operations during CDC will result in a non-recoverable error. To bring the target back in sync, run a full load.
+ Rollback trigger events are not supported for tables that use a data row locking scheme.
+ AWS DMS can't resume a replication task after dropping a table within the task scope from a source SAP database. If the DMS replication task was stopped and performed any DML operation (INSERT,UPDATE,DELETE) followed by dropping the table, you must restart the replication task.

## Permissions required for using SAP ASE as a source for AWS DMS
<a name="CHAP_Source.SAP.Security"></a>

To use an SAP ASE database as a source in an AWS DMS task, you need to grant permissions. Grant the user account specified in the AWS DMS database definitions the following permissions in the SAP ASE database: 
+ sa\_role
+ replication\_role
+ sybase\_ts\_role
+ By default, where you need to have permission to run the `sp_setreptable` stored procedure, AWS DMS enables the SAP ASE replication option. If you want to run `sp_setreptable` on a table directly from the database endpoint and not through AWS DMS itself, you can use the `enableReplication` extra connection attribute. For more information, see [Endpoint settings when using SAP ASE as a source for AWS DMS](#CHAP_Source.SAP.ConnectionAttrib).

## Removing the truncation point
<a name="CHAP_Source.SAP.Truncation"></a>

When a task starts, AWS DMS establishes a `$replication_truncation_point` entry in the `syslogshold` system view, indicating that a replication process is in progress. While AWS DMS is working, it advances the replication truncation point at regular intervals, according to the amount of data that has already been copied to the target.

After the `$replication_truncation_point` entry is established, keep the AWS DMS task running to prevent the database log from becoming excessively large. If you want to stop the AWS DMS task permanently, remove the replication truncation point by issuing the following command:

```
dbcc settrunc('ltm','ignore')
```

After the truncation point is removed, you can't resume the AWS DMS task. The log continues to be truncated automatically at the checkpoints (if automatic truncation is set).

## Endpoint settings when using SAP ASE as a source for AWS DMS
<a name="CHAP_Source.SAP.ConnectionAttrib"></a>

You can use endpoint settings to configure your SAP ASE source database similar to using extra connection attributes. You specify the settings when you create the source endpoint using the AWS DMS console, or by using the `create-endpoint` command in the [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/dms/index.html), with the `--sybase-settings '{"{{EndpointSetting"}}: {{"value"}}, {{...}}}'` JSON syntax.

The following table shows the endpoint settings that you can use with SAP ASE as a source.


| Name | Description | 
| --- | --- | 
| Charset | Set this attribute to the SAP ASE name that corresponds to the international character set. Some character sets require the endpoint setting `Provider` to be set to `Adaptive Server Enterprise 16.0.02.00 Full`.<br />Default value: `iso_1`<br />Example: `--sybase-settings '{"Charset": "utf8"}'`<br />Valid values:+  `acsii_8` <br />+  `big5hk` <br />+  `cp437` <br />+  `cp850` <br />+  `cp852` <br />+  `cp852` <br />+  `cp855` <br />+  `cp857` <br />+  `cp858` <br />+  `cp860` <br />+  `cp864` <br />+  `cp866` <br />+  `cp869` <br />+  `cp874` <br />+  `cp932` <br />+  `cp936` <br />+  `cp950` <br />+  `cp1250` <br />+  `cp1251` <br />+  `cp1252` <br />+  `cp1253` <br />+  `cp1254` <br />+  `cp1255` <br />+  `cp1256` <br />+  `cp1257` <br />+  `cp1258` <br />+  `deckanji` <br />+  `euccns` <br />+  `eucgb` <br />+  `eucjis` <br />+  `eucksc` <br />+  `gb18030` <br />+  `greek8` <br />+  `iso_1` <br />+  `iso88592` <br />+  `iso88595` <br />+  `iso88596` <br />+  `iso88597` <br />+  `iso88598` <br />+  `iso88599` <br />+  `iso15` <br />+  `kz1048` <br />+  `koi8` <br />+  `roman8` <br />+  `iso88599` <br />+  `sjis` <br />+  `tis620` <br />+  `turkish8` <br />+  `utf8` <br />For any further questions about supported character sets in a SAP ASE database, see [Adaptive Server Enterprise: Supported character sets](http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc35823.1550/html/uconfig/X29127.htm). | 
| EnableReplication | Set this attribute if you want to enable `sp_setreptable` on tables from the database end and not through AWS DMS.<br />Default value: `true`<br />Valid values: `true` or `false`<br />Example: `--sybase-settings '{"EnableReplication": false}'` | 
| EncryptPassword | Set this attribute if you have enabled `"net password encryption reqd"` at the source database.<br />Default value: `0`<br />Valid values: `0`, `1`, or `2`<br />Example: `--sybase-settings '{"EncryptPassword": 1}'`<br />For more information on these parameter values, see [Adaptive Server Enterprise: Using the EncryptPassword Connection string property](http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc20155.1500/html/newfesd/CBHEDGHB.htm). | 
| Provider | Set this attribute if you want to use Transport Layer Security (TLS) 1.2 for versions of ASE 15.7 and higher. Note that AWS requires TLS version 1.2 or later, and recommends version 1.3.<br />Default value: `Adaptive Server Enterprise`<br />Valid values: `Adaptive Server Enterprise 16.03.06`, `Adaptive Server Enterprise 16.0.02.00 Full`<br />Example: `--sybase-settings '{"Provider": "Adaptive Server Enterprise 16.03.06"}'` | 

## Source data types for SAP ASE
<a name="CHAP_Source.SAP.DataTypes"></a>

For a list of the SAP ASE source data types that are supported when using AWS DMS and the default mapping from AWS DMS data types, see the following table. AWS DMS doesn't support SAP ASE source tables with columns of the user-defined type (UDT) data type. Replicated columns with this data type are created as NULL. 

For information on how to view the data type that is mapped in the target, see the [Targets for data migration](CHAP_Target.md) section for your target endpoint.

For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.DataTypes.md).


|  SAP ASE data types  |  AWS DMS data types  | 
| --- | --- | 
| BIGINT | INT8 | 
| UNSIGNED BIGINT | UINT8 | 
| INT | INT4 | 
| UNSIGNED INT | UINT4 | 
| SMALLINT | INT2 | 
| UNSIGNED SMALLINT | UINT2 | 
| TINYINT | UINT1 | 
| DECIMAL | NUMERIC | 
| NUMERIC | NUMERIC | 
| FLOAT | REAL8 | 
| DOUBLE | REAL8 | 
| REAL | REAL4 | 
| MONEY | NUMERIC | 
| SMALLMONEY | NUMERIC | 
| DATETIME | DATETIME | 
| BIGDATETIME | DATETIME(6) | 
| SMALLDATETIME | DATETIME | 
| DATE | DATE | 
| TIME | TIME | 
| BIGTIME | TIME | 
| CHAR | STRING | 
| UNICHAR | WSTRING | 
| NCHAR | WSTRING | 
| VARCHAR | STRING | 
| UNIVARCHAR | WSTRING | 
| NVARCHAR | WSTRING | 
| BINARY | BYTES | 
| VARBINARY | BYTES | 
| BIT | BOOLEAN | 
| TEXT | CLOB | 
| UNITEXT | NCLOB | 
| IMAGE | BLOB | 