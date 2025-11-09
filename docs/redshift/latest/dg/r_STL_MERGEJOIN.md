Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_MERGEJOIN

Analyzes merge join execution steps for queries.

STL_MERGEJOIN is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_MERGEJOIN only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name | Data type | Description                                                                                                                                                                   |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid      | integer   | ID of the user who generated the entry.                                                                                                                                       |
| query       | integer   | Query ID. The query column can be used to join other system tables and views.                                                                                                 |
| slice       | integer   | Number that identifies the slice where the query was running.                                                                                                                 |
| segment     | integer   | Number that identifies the query segment.                                                                                                                                     |
| step        | integer   | Query step that ran.                                                                                                                                                          |
| starttime   | timestamp | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.  |
| endtime     | timestamp | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`. |
| tasknum     | integer   | Number of the query task process that was assigned to run the step.                                                                                                           |
| rows        | bigint    | Total number of rows that were processed.                                                                                                                                     |
| tbl         | integer   | Table ID. This is the ID for the inner<br>table that was used in the merge join.                                                                                              |
| checksum    | bigint    | This information is for internal use only.                                                                                                                                    |

## Sample queries

The following example returns merge join results for the most recent query.

```
select sum(s.qtysold), e.eventname
from event e, listing l, sales s
where e.eventid=l.eventid
and l.listid= s.listid
group by e.eventname;

select * from stl_mergejoin where query=pg_last_query_id();
```

```
 userid | query | slice | segment | step |         starttime   |          endtime    | tasknum | rows | tbl
--------+-------+-------+---------+------+---------------------+---------------------+---------+------+-----
    100 | 27399 |     3 |       4 |    4 | 2013-10-02 16:30:41 | 2013-10-02 16:30:41 |      19 |43428 | 240
    100 | 27399 |     0 |       4 |    4 | 2013-10-02 16:30:41 | 2013-10-02 16:30:41 |      19 |43159 | 240
    100 | 27399 |     2 |       4 |    4 | 2013-10-02 16:30:41 | 2013-10-02 16:30:41 |      19 |42778 | 240
    100 | 27399 |     1 |       4 |    4 | 2013-10-02 16:30:41 | 2013-10-02 16:30:41 |      19 |43091 | 240
```
