

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_LOAD\_STATE
<a name="r_STV_LOAD_STATE"></a>

Use the STV\_LOAD\_STATE table to find information about current state of ongoing COPY statements.

The COPY command updates this table after every million records are loaded.

STV\_LOAD\_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_STV_LOAD_STATE-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | ID of user who generated entry. | 
| session | integer | Session PID of process doing the load. | 
| query  | integer  | Query ID. Can be used to join various other system tables and views.  | 
| slice  | integer  | Node slice number. | 
| pid  | integer  | Process ID. All of the queries in a session are run in the same process, so this value remains constant if you run a series of queries in the same session. | 
| recordtime  | timestamp | Time the record is logged.  | 
| bytes\_to\_load | bigint | Total number of bytes to be loaded by this slice. This is 0 if the data being loaded is compressed  | 
| bytes\_loaded | bigint | Number of bytes loaded by this slice. If the data being loaded is compressed, this is the number of bytes loaded after the data is uncompressed. | 
| bytes\_to\_load\_compressed | bigint | Total number of bytes of compressed data to be loaded by this slice. This is 0 if the data being loaded is not compressed. | 
| bytes\_loaded\_compressed | bigint  | Number of bytes of compressed data loaded by this slice. This is 0 if the data being loaded is not compressed. | 
| lines  | integer | Number of lines loaded by this slice. | 
| num\_files | integer | Number of files to be loaded by this slice. | 
| num\_files\_complete | integer  | Number of files loaded by this slice. | 
| current\_file | character(256)  | Name of the file being loaded by this slice.  | 
| pct\_complete | integer | Percentage of data load completed by this slice. | 

## Sample query
<a name="r_STV_LOAD_STATE-sample-query2"></a>

To view the progress of each slice for a COPY command, type the following query. This example uses the PG\_LAST\_COPY\_ID() function to retrieve information for the last COPY command.

```
select slice , bytes_loaded, bytes_to_load , pct_complete from stv_load_state where query = pg_last_copy_id();

 slice | bytes_loaded | bytes_to_load | pct_complete 
-------+--------------+---------------+--------------
     2 |            0 |             0 |            0
     3 |     12840898 |      39104640 |           32
(2 rows)
```