

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Secure logging
<a name="db-auditing-secure-logging"></a>

When Amazon Redshift logs a query that references one or more AWS Glue Data Catalog views, Amazon Redshift automatically masks fields in certain system table and view columns when logging metadata about that query.

Secure log masking applies to all system table and view entries that Amazon Redshift generates while running a query that fits the masking conditions. The following table lists system views and columns that have secure logging applied, masking text with `******` and numbers with `-1`. The number of asterisks used to mask text matches the number of characters in the original text, up to 6 characters. Strings longer than 6 characters still appear as 6 asterisks.



| System table | Sensitive columns | 
| --- | --- | 
| [SYS\_EXTERNAL\_QUERY\_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_EXTERNAL_QUERY_DETAIL.html) | **Columns:** source\_type, total\_partitions, qualified\_partitions, scanned\_files, returned\_rows, returned\_bytes, file\_format, file\_location, external\_query\_text, warning\_message. | 
| [SYS\_EXTERNAL\_QUERY\_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/SYS_EXTERNAL_QUERY_ERROR.html) | **Columns:** file\_location, rowid, column\_name, original\_value, modified\_value, trigger, action, action\_value, error\_code. | 
| [SYS\_QUERY\_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_QUERY_DETAIL.html) | **Columns:** step\_id, step\_name, table\_id, table\_name, input\_bytes, input\_rows, output\_bytes, output\_rows, blocks\_read, blocks\_write, local\_read\_IO, remote\_read\_IO, spilled\_block\_local\_disk, spilled\_block\_remote\_disk, step\_attribute. | 
| [SYS\_QUERY\_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_QUERY_HISTORY.html) | **Columns:** returned\_rows, returned\_bytes. | 
| [STL\_AGGR](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_AGGR.html) | **Columns:** rows, bytes, tbl, type. | 
| [STL\_BCAST](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_BCAST.html) | **Columns:** rows, bytes, packets. | 
| [STL\_DDLTEXT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_DDLTEXT.html) | **Columns:** label, text. | 
| [STL\_DELETE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_DELETE.html) | **Columns:** rows, tbl. | 
| [STL\_DIST](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_DIST.html) | **Columns:** rows, bytes, packets. | 
| [STL\_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_ERROR.html) | **Columns:** file, linenum, context, error. | 
| [STL\_EXPLAIN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_EXPLAIN.html) | **Columns:** plannode, info. | 
| [STL\_FILE\_SCAN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_FILE_SCAN.html) | **Columns:** name, line, bytes. | 
| [STL\_HASH](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_HASH.html) | **Columns:** rows, bytes, tbl, est\_rows. | 
| [STL\_HASHJOIN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_HASHJOIN.html) | **Columns:** rows, tbl, num\_parts, join\_type. | 
| [STL\_INSERT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_INSERT.html) | **Columns:** rows, tbl. | 
| [STL\_LIMIT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_LIMIT.html) | **Columns:** rows. | 
| [STL\_MERGE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_MERGE.html) | **Columns:** rows. | 
| [STL\_MERGEJOIN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_MERGEJOIN.html) | **Columns:** rows, tbl. | 
| [STL\_NESTLOOP](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_NESTLOOP.html) | **Columns:** rows, tbl. | 
| [STL\_PARSE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_PARSE.html) | **Columns:** rows. | 
| [STL\_PLAN\_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_PLAN_INFO.html) | **Columns:** startupcost, totalcost, rows, bytes. | 
| [STL\_PROJECT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_PROJECT.html) | **Columns:** rows, tbl. | 
| [STL\_QUERY](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_QUERY.html) | **Columns:** querytxt. | 
| [STL\_QUERY\_METRICS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_QUERY_METRICS.html) | **Columns:** max\_rows, rows, max\_blocks\_read, blocks\_read, max\_blocks\_to\_disk, blocks\_to\_disk, max\_query\_scan\_size, query\_scan\_size. | 
| [STL\_QUERYTEXT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_QUERYTEXT.html) | **Columns:** text. | 
| [STL\_RETURN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_RETURN.html) | **Columns:** rows, bytes. | 
| [STL\_S3CLIENT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_S3CLIENT.html) | **Columns:** bucket, key, transfer\_size, data\_size. | 
| [STL\_S3CLIENT\_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_S3CLIENT_ERROR.html) | **Columns:** bucket, key, error, transfer\_size. | 
| [STL\_SAVE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SAVE.html) | **Columns:** rows, bytes, tbl. | 
| [STL\_SCAN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SCAN.html) | **Columns:** rows, bytes, fetches, type, tbl, rows\_pre\_filter, rows\_pre\_user\_filter, perm\_table\_name, scanned\_mega\_value. | 
| [STL\_SORT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SORT.html) | **Columns:** rows, bytes, tbl. | 
| [STL\_SSHCLIENT\_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SSHCLIENT_ERROR) | **Columns:** ssh\_username, endpoint, command, error. | 
| [STL\_TR\_CONFLICT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_TR_CONFLICT.html) | **Columns:** table\_id. | 
| [STL\_UNDONE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_UNDONE.html) | **Columns:** table\_id. | 
| [STL\_UNIQUE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_UNIQUE.html) | **Columns:** rows, type, bytes. | 
| [STL\_UTILITYTEXT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_UTILITYTEXT.html) | **Columns:** label, text. | 
| [STL\_WINDOW](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_WINDOW.html) | **Columns:** rows. | 
| [STV\_BLOCKLIST](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_BLOCKLIST.html) | **Columns:** col, tbl, num\_values, minvalue, maxvalue. | 
| [STV\_EXEC\_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_EXEC_STATE.html) | **Columns:** rows, bytes, label. | 
| [STV\_INFLIGHT](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_INFLIGHT.html) | **Columns:** label, text. | 
| [STV\_LOCKS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_LOCKS.html) | **Columns:** table\_id. | 
| [STV\_QUERY\_METRICS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_QUERY_METRICS.html) | **Columns:** rows, max\_rows, blocks\_read, max\_blocks\_read, max\_blocks\_to\_disk, blocks\_to\_disk, max\_query\_scan\_size, query\_scan\_size. | 
| [STV\_STARTUP\_RECOVERY\_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_STARTUP_RECOVERY_STATE.html) | **Columns:** table\_id, table\_name. | 
| [STV\_TBL\_PERM](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_TBL_PERM.html) | **Columns:** id, name, rows, sorted\_rows, temp, block\_count, query\_scan\_size. | 
| [STV\_TBL\_TRANS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_TBL_TRANS.html) | **Columns:** id, rows, size. | 
| [SVCS\_EXPLAIN](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_EXPLAIN.html) | **Columns:** plannode, info. | 
| [SVCS\_PLAN\_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_PLAN_INFO.html) | **Columns:** rows, bytes. | 
| [SVCS\_QUERY\_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_QUERY_SUMMARY.html) | **Columns:** step, rows, bytes, rate\_row, rate\_byte, label, rows\_pre\_filter. | 
| [SVCS\_S3LIST](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_S3LIST.html) | **Columns:** bucket, prefix, retrieved\_files, max\_file\_size, avg\_file\_size. | 
| [SVCS\_S3LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_S3LOG.html) | **Columns:** message. | 
| [SVCS\_S3PARTITION\_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_S3PARTITION_SUMMARY.html) | **Columns:** total\_partitions, qualified\_partitions, min\_assigned\_partitions, max\_assigned\_partitions, avg\_assigned\_partitions. | 
| [SVCS\_S3QUERY\_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_S3QUERY_SUMMARY.html) | **Columns:** external\_table\_name, file\_format, s3\_scanned\_rows, s3\_scanned\_bytes, s3query\_returned\_rows, s3query\_returned\_bytes. | 
| [SVL\_QUERY\_METRICS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_METRICS.html) | **Columns:** step\_label, scan\_row\_count, join\_row\_count, nested\_loop\_join\_row\_count, return\_row\_count, spectrum\_scan\_row\_count, spectrum\_scan\_size\_mb. | 
| [SVL\_QUERY\_METRICS\_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_METRICS_SUMMARY.html) | **Columns:** step\_label, scan\_row\_count, join\_row\_count, nested\_loop\_join\_row\_count, return\_row\_count, spectrum\_scan\_row\_count, spectrum\_scan\_size\_mb. | 
| [SVL\_QUERY\_REPORT](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_REPORT.html) | **Columns:** rows, bytes, label, rows\_pre\_filter. | 
| [SVL\_QUERY\_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_SUMMARY.html) | **Columns:** rows, bytes, rows\_pre\_filter. | 
| [SVL\_S3LIST](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3LIST.html) | **Columns:** bucket, prefix, retrieved\_files, max\_file\_size, avg\_file\_size. | 
| [SVL\_S3LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3LOG.html) | **Columns:** message. | 
| [SVL\_S3PARTITION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3PARTITION.html) | **Columns:** rows, bytes, label, rows\_pre\_filter. | 
| [SVL\_S3PARTITION\_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3PARTITION_SUMMARY.html) | **Columns:** total\_partitions, qualified\_partitions, min\_assigned\_partitions, max\_assigned\_partitions, avg\_assigned\_partitions. | 
| [SVL\_S3QUERY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3QUERY.html) | **Columns:** external\_table\_name, file\_format, s3\_scanned\_rows, s3\_scanned\_bytes, s3query\_returned\_rows, s3query\_returned\_bytes, files. | 
| [SVL\_S3QUERY\_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3QUERY_SUMMARY.html) | **Columns:** external\_table\_name, file\_format, s3\_scanned\_rows, s3\_scanned\_bytes, s3query\_returned\_rows, s3query\_returned\_bytes. | 
| [SVL\_S3RETRIES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3RETRIES.html) | **Columns:** file\_size, location, message. | 
| [SVL\_SPECTRUM\_SCAN\_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_SPECTRUM_SCAN_ERROR.html) | **Columns:** location, rowid, colname, original\_value, modified\_value, trigger, action, action\_value, error\_code. | 
| [SVL\_STATEMENTTEXT](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_STATEMENTTEXT.html) | **Columns:** type, text. | 
| [SVL\_STORED\_PROC\_CALL](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_STORED_PROC_CALL.html) | **Columns:** querytxt. | 
| [SVL\_STORED\_PROC\_MESSAGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_STORED_PROC_MESSAGES.html) | **Columns:** message, linenum, querytext. | 
| [SVL\_UDF\_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_UDF_LOG.html) | **Columns:** message, funcname. | 
| [SVV\_DISKUSAGE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DISKUSAGE.html) | **Columns:** name, col, tbl, blocknum, num\_values, minvalue, maxvalue. | 
| [SVV\_QUERY\_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_QUERY_STATE.html) | **Columns:** rows, bytes, label. | 
| [SVV\_TABLE\_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html) | **Columns:** table\_id, table. | 
| [SVV\_TRANSACTIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TRANSACTIONS.html) | **Columns:** relation. | 

For more information on system tables and views, see [ System tables and views reference](https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_system-tables.html) in the *Amazon Redshift Database Developer Guide*. For information on Amazon Redshift’s ability to dynamically mask query results, see [ Dynamic data masking](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm.html) in the *Amazon Redshift Database Developer Guide*. For information on creating views in the AWS Glue Data Catalog using Amazon Redshift, see [AWS Glue Data Catalog views](https://docs.aws.amazon.com/redshift/latest/dg/data-catalog-views-overview.html) in the *Amazon Redshift Database Developer Guide*.