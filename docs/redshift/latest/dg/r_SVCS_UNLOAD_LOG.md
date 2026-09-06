

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVCS\_UNLOAD\_LOG
<a name="r_SVCS_UNLOAD_LOG"></a>

Use the SVCS\_UNLOAD\_LOG to get details of UNLOAD operations.

SVCS\_UNLOAD\_LOG records one row for each file created by an UNLOAD statement. For example, if an UNLOAD creates 12 files, SVCS\_UNLOAD\_LOG contains 12 corresponding rows. This view is derived from the STL\_UNLOAD\_LOG system table but doesn't show slice-level for queries run on a concurrency scaling cluster. 

**Note**  
System views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters. The views are similar to the tables with the prefix STL except that the STL tables provide information only for queries run on the main cluster.

SVCS\_UNLOAD\_LOG is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SVCS_UNLOAD_LOG-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | The ID of the user who generated the entry. | 
| query  | integer  | The query ID.  | 
| pid | integer | The process ID associated with the query statement. | 
| path | character(1280) | The complete Amazon S3 object path for the file. | 
| start\_time | timestamp  | The start time for the UNLOAD operation.  | 
| end\_time | timestamp  | The end time for the UNLOAD operation.  | 
| line\_count | bigint | The number of lines (rows) unloaded to the file. | 
| transfer\_size | bigint | The number of bytes transferred. | 
| file\_format | character(10) | The format of unloaded file. | 

## Sample query
<a name="r_SVCS_UNLOAD_LOG-sample-query"></a>

To get a list of the files that were written to Amazon S3 by an UNLOAD command, you can call an Amazon S3 list operation after the UNLOAD completes; however, depending on how quickly you issue the call, the list might be incomplete because an Amazon S3 list operation is eventually consistent. To get a complete, authoritative list immediately, query SVCS\_UNLOAD\_LOG.

The following query returns the path name for files that were created by an UNLOAD for the last query completed:

```
select query, substring(path,0,40) as path
from svcs_unload_log
where query = pg_last_query_id()
order by path;
```

This command returns the following sample output: 

```
 
 query |             path
 ------+---------------------------------------------
  2320 | s3://amzn-s3-demo-bucket/venue0000_part_00
  2320 | s3://amzn-s3-demo-bucket/venue0001_part_00
  2320 | s3://amzn-s3-demo-bucket/venue0002_part_00
  2320 | s3://amzn-s3-demo-bucket/venue0003_part_00
(4 rows)
```