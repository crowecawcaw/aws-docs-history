

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_HASHJOIN
<a name="r_STL_HASHJOIN"></a>

Analyzes hash join execution steps for queries.

STL\_HASHJOIN is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

**Note**  
STL\_HASHJOIN only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters or on serverless namespaces. To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view [SYS\_QUERY\_DETAIL](SYS_QUERY_DETAIL.md) . The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns
<a name="r_STL_HASHJOIN-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | ID of the user who generated the entry. | 
| query | integer | Query ID. The query column can be used to join other system tables and views. | 
| slice | integer | Number that identifies the slice where the query was running. | 
| segment | integer | Number that identifies the query segment. | 
| step | integer | Query step that ran. | 
| starttime | timestamp | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: 2009-06-12 11:29:19.131358. | 
| endtime | timestamp | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: 2009-06-12 11:29:19.131358. | 
| tasknum | integer | Number of the query task process that was assigned to run the step. | 
| rows | bigint | Total number of rows that were processed. | 
| tbl | integer | Table ID. | 
| num\_parts | integer | Total number of partitions that a hash table was divided into during a hash step.  | 
| join\_type | integer | The type of join for the step: +  0. The query used an inner join. <br />+  1. The query used a left outer join. <br />+  2. The query used a full outer join. <br />+  3. The query used a right outer join. <br />+  4. The query used a UNION operator. <br />+  5. The query used an IN condition. <br />+  6. This information is for internal use only. <br />+  7. This information is for internal use only. <br />+  8. This information is for internal use only. <br />+  9. This information is for internal use only. <br />+  10. This information is for internal use only. <br />+  11. This information is for internal use only. <br />+  12. This information is for internal use only.   | 
| hash\_looped | character(1) | This information is for internal use only. | 
| switched\_parts | character(1) | Indicates whether the build (or outer) and probe (or inner) sides have switched. | 
| used\_prefetching | character(1) | This information is for internal use only. | 
| hash\_segment | integer | The segment of the corresponding hash step. | 
| hash\_step  | integer | The step number of the corresponding hash step. | 
| checksum | bigint | This information is for internal use only. | 
| distribution  | integer | This information is for internal use only. | 

## Sample queries
<a name="r_STL_HASHJOIN-sample-queries"></a>

The following example returns the number of partitions used in a hash join for query 720. 

```
select query, slice, tbl, num_parts
from stl_hashjoin
where query=720 limit 10;
```

```
 query | slice | tbl | num_parts
-------+-------+-----+-----------
   720 |     0 | 243 |         1
   720 |     1 | 243 |         1
(2 rows)
```