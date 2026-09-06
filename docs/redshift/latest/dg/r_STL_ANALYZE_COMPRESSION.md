

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_ANALYZE\_COMPRESSION
<a name="r_STL_ANALYZE_COMPRESSION"></a>

Records details for compression analysis operations during COPY or ANALYZE COMPRESSION commands.

STL\_ANALYZE\_COMPRESSION is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_ANALYZE\_COMPRESSION\_HISTORY](r_SYS_ANALYZE_COMPRESSION_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_STL_ANALYZE_COMPRESSION-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | The ID of the user who generated the entry. | 
| start\_time | timestamp | The time when the compression analysis operation started. | 
| xid | bigint | The transaction ID of the compression analysis operation. | 
| tbl | integer | The table ID of the table that was analyzed. | 
| tablename | character(128) | The name of the table that was analyzed. | 
| col | integer | The index of the column in the table that was analyzed to determine the compression encoding. | 
| old\_encoding | character(15) | The encoding type before compression analysis. | 
| new\_encoding | character(15) | The encoding type after compression analysis. | 
| mode | character(14) | **PRESET**<br /> Specifies that the `new_encoding` is determined by the Amazon Redshift COPY command based on the column data type. No data is sampled.  <br />**ON**<br /> Specifies that the `new_encoding` is determined by the Amazon Redshift COPY command based on an analysis of sample data. <br />**ANALYZE ONLY**<br /> Specifies that the `new_encoding` is determined by the Amazon Redshift ANALYZE COMPRESSION command based on an analysis of sample data. However, the encoding type of the analyzed column is not changed.   | 
| best\_compression\_encoding | character(15) | The encoding type that gives the best compression ratio. | 
| recommended\_bytes | character(15) | The bytes used by adopting the new encoding. | 
| best\_compression\_bytes | character(15) | The bytes used by adopting the best compression encoding. | 
| ndv | bigint | The number of distinct values in the sampled rows. | 

## Sample queries
<a name="r_STL_ANALYZE_COMPRESSION-sample-queries2"></a>

The following example inspects the details of compression analysis on the `lineitem` table by the last COPY command run in the same session. 

```
select xid, tbl, btrim(tablename) as tablename, col, old_encoding, new_encoding, best_compression_encoding, mode 
from stl_analyze_compression 
where xid = (select xid from stl_query where query = pg_last_copy_id()) order by col;

 xid  |  tbl   | tablename | col |  old_encoding   |  new_encoding   | best_compression_encoding |      mode      
------+--------+-----------+-----+-----------------+-----------------+---------------------------+----------------
 5308 | 158961 | $lineitem |   0 | mostly32        | az64            | delta                     | ON            
 5308 | 158961 | $lineitem |   1 | mostly32        | az64            | az64                      | ON            
 5308 | 158961 | $lineitem |   2 | lzo             | az64            | az64                      | ON            
 5308 | 158961 | $lineitem |   3 | delta           | az64            | az64                      | ON            
 5308 | 158961 | $lineitem |   4 | bytedict        | az64            | bytedict                  | ON            
 5308 | 158961 | $lineitem |   5 | mostly32        | az64            | az64                      | ON            
 5308 | 158961 | $lineitem |   6 | delta           | az64            | az64                      | ON            
 5308 | 158961 | $lineitem |   7 | delta           | az64            | az64                      | ON            
 5308 | 158961 | $lineitem |   8 | lzo             | lzo             | lzo                       | ON            
 5308 | 158961 | $lineitem |   9 | runlength       | runlength       | runlength                 | ON            
 5308 | 158961 | $lineitem |  10 | delta           | az64            | az64                      | ON            
 5308 | 158961 | $lineitem |  11 | delta           | az64            | az64                      | ON            
 5308 | 158961 | $lineitem |  12 | delta           | az64            | az64                      | ON            
 5308 | 158961 | $lineitem |  13 | bytedict        | bytedict        | bytedict                  | ON            
 5308 | 158961 | $lineitem |  14 | bytedict        | bytedict        | bytedict                  | ON            
 5308 | 158961 | $lineitem |  15 | text255         | text255         | text255                   | ON   
(16 rows)
```