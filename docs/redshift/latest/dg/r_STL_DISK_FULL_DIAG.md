

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_DISK\_FULL\_DIAG
<a name="r_STL_DISK_FULL_DIAG"></a>

Logs information about errors recorded when the disk is full.

STL\_DISK\_FULL\_DIAG is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_STL_DISK_FULL_DIAG-table-columns"></a>


| Column name  | Data type  | Description | 
| --- | --- | --- | 
| currenttime | bigint | The day and time the error was generated in microseconds since January 1, 2000. | 
| node\_num | bigint | The identifier for the node. | 
| query\_id | bigint | The identifier for the query that caused the error. | 
| temp\_blocks | bigint | The number of temporary blocks created by the query. | 

## Sample queries
<a name="r_STL_DISK_FULL_DIAG-sample-queries"></a>

The following example returns details about the data stored when there is a disk-full error. 

```
select * from stl_disk_full_diag
```

The following example converts the `currenttime` to a timestamp. 

```
select '2000-01-01'::timestamp + (currenttime/1000000.0)* interval '1 second' as currenttime,node_num,query_id,temp_blocks from pg_catalog.stl_disk_full_diag;
```

```
        currenttime         | node_num | query_id | temp_blocks 
----------------------------+----------+----------+-------------
 2019-05-18 19:19:18.609338 |        0 |   569399 |       70982
 2019-05-18 19:37:44.755548 |        0 |   569580 |       70982
 2019-05-20 13:37:20.566916 |        0 |   597424 |       70869
```