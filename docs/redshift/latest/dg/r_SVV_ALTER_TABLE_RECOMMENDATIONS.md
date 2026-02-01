Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ALTER_TABLE_RECOMMENDATIONS

Records the current Amazon Redshift Advisor recommendations for tables. This view shows
recommendations for all tables, whether they are defined for automatic optimization or
not. To view if a table is defined for automatic optimization, see [SVV_TABLE_INFO](r_SVV_TABLE_INFO.md "r_SVV_TABLE_INFO.md"). Entries appear only
for tables visible in the current session's database. After a recommendation has been
applied (either by Amazon Redshift or by you), it no longer appears in the view.

SVV_ALTER_TABLE_RECOMMENDATIONS is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name   | Data type       | Description                                                                                                                                                                                                                                                    |
| ------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type          | character(30)   | The type of recommendation. Possible values are<br>distkey and sortkey.                                                                                                                                                                                        |
| database      | character(128)  | The database name.                                                                                                                                                                                                                                             |
| table_id      | integer         | The table identifier.                                                                                                                                                                                                                                          |
| group_id      | integer         | The group number of a set of recommendations. All<br>recommendations in a group should be applied to see the maximum<br>benefit. Possible values are -1 for a sort key recommendation, and a<br>number larger than zero for a distribution key recommendation. |
| ddl           | character(1024) | The SQL statement that must run to apply the<br>recommendation.                                                                                                                                                                                                |
| auto_eligible | character(1)    | The value indicates if the recommendation is<br>eligible for Amazon Redshift to run automatically. If this value is<br>`t`, then the indication is true, if `f`<br>then false.                                                                                 |

## Sample queries

In the following example, the rows in the result show recommendations for
distribution key and sort key. The rows also show whether the recommendations are
eligible for Amazon Redshift to automatically apply them.

```
select type, database, table_id, group_id, ddl, auto_eligible
from svv_alter_table_recommendations;
```

```

 type      | database | table_id | group_id | ddl                                                                                                                                                 | auto_eligible
 diststyle | db0      | 117884   | 2        | ALTER TABLE "sch"."dp21235_tbl_1" ALTER DISTSTYLE KEY DISTKEY "c0"                                                                                  | f
 diststyle | db0      | 117892   | 2        | ALTER TABLE "sch"."dp21235_tbl_1" ALTER DISTSTYLE KEY DISTKEY "c0"                                                                                  | f
 diststyle | db0      | 117885   | 1        | ALTER TABLE "sch"."catalog_returns" ALTER DISTSTYLE KEY DISTKEY "cr_sold_date_sk", ALTER COMPOUND SORTKEY ("cr_sold_date_sk","cr_returned_time_sk") | t
 sortkey   | db0      | 117890   | -1       | ALTER TABLE "sch"."customer_addresses" ALTER COMPOUND SORTKEY ("ca_address_sk")                                                                     | t

```
