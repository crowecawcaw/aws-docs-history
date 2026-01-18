Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION

Use SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION to view the usage periods in which
Amazon Redshift ran automatic optimization tasks using extra compute resources. For more
information on automatic optimization, see [Automatic database optimization](c_autonomics.md "c_autonomics.md"). For more information on automatic
optimizations run using extra compute resources, see [Allocating extra compute resources for automatic database optimization](t_extra-compute-autonomics.md "t_extra-compute-autonomics.md").

SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION is available only for provisioned clusters.

SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table

columns

| Column name     | Data type                   | Description                                                                                                                                    |
| --------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| start_time      | timestamp without time zone | The time that the extra compute optimization<br>period starts.                                                                                 |
| end_time        | timestamp without time zone | The time that the extra compute optimization<br>period ends.                                                                                   |
| query_count     | bigint                      | The number of automatic optimization queries run<br>during the usage period.                                                                   |
| compute_seconds | numeric(27,0)               | The number of seconds<br>in the usage period that Amazon Redshift spent running automatic<br>optimization tasks using extra compute resources. |

## Examples

Following is an example query looking for automatic optimizations performed on
September 16, 2025.

```
`SELECT *
FROM sys_extra_compute_for_automatic_optimization
WHERE start_time BETWEEN '2025-09-16 00:00:00' AND '2025-09-16 23:59:59';`

`start_time | end_time | query_count | compute_seconds
---------------------+---------------------+-------------+-----------------
 2025-09-16 00:00:00 | 2025-09-16 00:00:59 | 1 | 59
 2025-09-16 00:01:05 | 2025-09-16 00:01:58 | 2 | 53`
```
