Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_VACUUM_PROGRESS

This view returns an estimate of how much time it will take to complete a vacuum
operation that is currently in progress.

SVV_VACUUM_PROGRESS is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_VACUUM_HISTORY](SYS_VACUUM_HISTORY.md "SYS_VACUUM_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

For information about SVV_VACUUM_SUMMARY, see [SVV_VACUUM_SUMMARY](r_SVV_VACUUM_SUMMARY.md "r_SVV_VACUUM_SUMMARY.md").

For information about SVL_VACUUM_PERCENTAGE, see [SVL_VACUUM_PERCENTAGE](r_SVL_VACUUM_PERCENTAGE.md "r_SVL_VACUUM_PERCENTAGE.md").

###### Note

This view is only available when querying provisioned clusters.

## Table columns

| Column name             | Data type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| table_name              | text      | Name of the table currently being vacuumed, or the<br>table that was last vacuumed if no operation is in progress.                                                                                                                                                                                                                                                                                                                                                  |
| status                  | text      | Description of the current activity being done as<br>part of the vacuum operation:<br>• Initialize<br>• Sort<br>• Merge<br>• Delete<br>• Select<br>• Failed<br>• Complete<br>• Skipped<br>• Building INTERLEAVED SORTKEY order                                                                                                                                                                                                                                      |
| time_remaining_estimate | text      | Estimated time left for the current vacuum<br>operation to complete, in minutes and seconds: `5m<br>10s`, for example. An estimated time is not returned<br>until the vacuum completes its first sort operation. If no vacuum is<br>in progress, the last vacuum that was performed is displayed with<br>`Completed` in the STATUS column and an<br>empty TIME_REMAINING_ESTIMATE column. The estimate typically becomes<br>more accurate as the vacuum progresses. |

## Sample queries

The following queries, run a few minutes apart, show that a large table named
SALESNEW is being vacuumed.

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

The following query shows that no vacuum operation is currently in progress. The
last table to be vacuumed was the SALES table.

```
select * from svv_vacuum_progress;

table_name   |  status  | time_remaining_estimate
-------------+----------+-------------------------
  sales      | Complete |
(1 row)
```
