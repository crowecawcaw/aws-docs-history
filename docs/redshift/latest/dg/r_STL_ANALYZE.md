

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_ANALYZE
<a name="r_STL_ANALYZE"></a>

Records details for [ANALYZE](r_ANALYZE.md) operations.

STL\_ANALYZE is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_ANALYZE\_HISTORY](SYS_ANALYZE_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_STL_ANALYZE-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | The ID of the user who generated the entry. | 
| xid | long | The transaction ID. | 
| database | char(30) | The database name. | 
| table\_id | integer | The table ID. | 
| status | char(15) | The result of the analyze command. Possible values are Full, Skipped, and PredicateColumn. | 
| rows  | double | The total number of rows in the table. | 
| modified\_rows | double | The total number of rows that were modified since the last ANALYZE operation. | 
| threshold\_percent | integer | The value of the analyze\_threshold\_percent parameter. | 
| is\_auto | char(1) | The value is true (t) if the operation included an Amazon Redshift analyze operation by default. The value is false (f) if the ANALYZE command was run explicitly. | 
| starttime | timestamp | The time in UTC that the analyze operation started running. | 
| endtime | timestamp | The time in UTC that the analyze operation finished running. | 
| prevtime | timestamp | The time in UTC that the table was previously analyzed. | 
| num\_predicate\_cols | integer | The current number of predicate columns in the table. | 
| num\_new\_predicate\_cols | integer | The number of new predicate columns in the table since the previous analyze operation. | 
| is\_background | character(1) | The value is true (t) if the analysis was run by an automatic analyze operation. Otherwise, the value is false (f). | 
| auto\_analyze\_phase | character(100) | Reserved for internal use. | 
| schema\_name | char(128) | The schema name for the table. | 
| table\_name | char(136) | The name of the table. | 

## Sample queries
<a name="r_STL_ANALYZE-sample-queries2"></a>

The following example joins STV\_TBL\_PERM to show the table name and execution details. 

```
select distinct a.xid, trim(t.name) as name, a.status, a.rows, a.modified_rows, a.starttime, a.endtime
from stl_analyze a 
join stv_tbl_perm t  on t.id=a.table_id
where name = 'users'
order by starttime;

xid    | name  | status          | rows  | modified_rows | starttime           | endtime            
-------+-------+-----------------+-------+---------------+---------------------+--------------------
  1582 | users | Full            | 49990 |         49990 | 2016-09-22 22:02:23 | 2016-09-22 22:02:28
244287 | users | Full            | 24992 |         74988 | 2016-10-04 22:50:58 | 2016-10-04 22:51:01
244712 | users | Full            | 49984 |         24992 | 2016-10-04 22:56:07 | 2016-10-04 22:56:07
245071 | users | Skipped         | 49984 |             0 | 2016-10-04 22:58:17 | 2016-10-04 22:58:17
245439 | users | Skipped         | 49984 |          1982 | 2016-10-04 23:00:13 | 2016-10-04 23:00:13
(5 rows)
```