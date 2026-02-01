Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_ANALYZE

Records details for [ANALYZE](r_ANALYZE.md "r_ANALYZE.md")
operations.

STL_ANALYZE is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_ANALYZE_HISTORY](SYS_ANALYZE_HISTORY.md "SYS_ANALYZE_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name            | Data type      | Description                                                                                                                                                               |
| ---------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid                 | integer        | The ID of the user who generated the entry.                                                                                                                               |
| xid                    | long           | The transaction ID.                                                                                                                                                       |
| database               | char(30)       | The database name.                                                                                                                                                        |
| table_id               | integer        | The table ID.                                                                                                                                                             |
| status                 | char(15)       | The result of the analyze command. Possible values<br>are `Full`, `Skipped`, and<br>`PredicateColumn`.                                                                    |
| rows                   | double         | The total number of rows in the table.                                                                                                                                    |
| modified_rows          | double         | The total number of rows that were modified since the<br>last ANALYZE operation.                                                                                          |
| threshold_percent      | integer        | The value of the<br>`analyze_threshold_percent` parameter.                                                                                                                |
| is_auto                | char(1)        | The value is true (`t`) if the operation included an Amazon Redshift analyze operation by default.<br>The value is false (`f`) if the ANALYZE command was run explicitly. |
| starttime              | timestamp      | The time in UTC that the analyze operation started<br>running.                                                                                                            |
| endtime                | timestamp      | The time in UTC that the analyze operation finished<br>running.                                                                                                           |
| prevtime               | timestamp      | The time in UTC that the table was previously<br>analyzed.                                                                                                                |
| num_predicate_cols     | integer        | The current number of predicate columns in the<br>table.                                                                                                                  |
| num_new_predicate_cols | integer        | The number of new predicate columns in the table since<br>the previous analyze operation.                                                                                 |
| is_background          | character(1)   | The value is true (`t`) if the analysis<br>was run by an automatic analyze operation. Otherwise, the value is<br>false (`f`).                                             |
| auto_analyze_phase     | character(100) | Reserved for internal use.                                                                                                                                                |
| schema_name            | char(128)      | The schema name for the table.                                                                                                                                            |
| table_name             | char(136)      | The name of the table.                                                                                                                                                    |

## Sample queries

The following example joins STV_TBL_PERM to show the table name and execution
details.

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
