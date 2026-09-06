

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_VACUUM\_PROGRESS
<a name="r_SVV_VACUUM_PROGRESS"></a>

This view returns an estimate of how much time it will take to complete a vacuum operation that is currently in progress.

SVV\_VACUUM\_PROGRESS is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_VACUUM\_HISTORY](SYS_VACUUM_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

For information about SVV\_VACUUM\_SUMMARY, see [SVV\_VACUUM\_SUMMARY](r_SVV_VACUUM_SUMMARY.md).

For information about SVL\_VACUUM\_PERCENTAGE, see [SVL\_VACUUM\_PERCENTAGE](r_SVL_VACUUM_PERCENTAGE.md).

**Note**  
This view is only available when querying provisioned clusters.

## Table columns
<a name="sub-r_SVV_VACUUM_PROGRESS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| table\_name  | text  | Name of the table currently being vacuumed, or the table that was last vacuumed if no operation is in progress.  | 
| status  | text  | Description of the current activity being done as part of the vacuum operation: +  Initialize <br />+  Sort <br />+  Merge <br />+  Delete <br />+  Select <br />+  Failed <br />+  Complete <br />+  Skipped <br />+  Building INTERLEAVED SORTKEY order  | 
| time\_remaining\_estimate  | text  | Estimated time left for the current vacuum operation to complete, in minutes and seconds: 5m 10s, for example. An estimated time is not returned until the vacuum completes its first sort operation. If no vacuum is in progress, the last vacuum that was performed is displayed with Completed in the STATUS column and an empty TIME\_REMAINING\_ESTIMATE column. The estimate typically becomes more accurate as the vacuum progresses.  | 

## Sample queries
<a name="r_SVV_VACUUM_PROGRESS-sample-queries"></a>

The following queries, run a few minutes apart, show that a large table named SALESNEW is being vacuumed. 

```
select * from svv_vacuum_progress;

table_name    |            status             | time_remaining_estimate
--------------+-------------------------------+-------------------------
salesnew      |  Vacuum: initialize salesnew  |
(1 row)
...
select * from svv_vacuum_progress;

table_name   |         status         | time_remaining_estimate
-------------+------------------------+-------------------------
salesnew     |  Vacuum salesnew sort  | 33m 21s
(1 row)
```

The following query shows that no vacuum operation is currently in progress. The last table to be vacuumed was the SALES table. 

```
select * from svv_vacuum_progress;

table_name   |  status  | time_remaining_estimate
-------------+----------+-------------------------
  sales      | Complete |
(1 row)
```