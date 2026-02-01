Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_CLASS_INFO

PG_CLASS_INFO is an Amazon Redshift system view built on the PostgreSQL catalog tables PG_CLASS
and PG_CLASS_EXTENDED. PG_CLASS_INFO includes details about table creation time and the
current distribution style. For more information, see [Data distribution for query optimization](t_Distributing_data.md "t_Distributing_data.md").

PG_CLASS_INFO is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

PG_CLASS_INFO shows the following columns in addition to the columns in
PG_CLASS. The `oid` column in PG_CLASS is called `reloid` in the PG_CLASS_INFO table.

| Column name           | Data type | Description                                                                                                                                       |
| --------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| relcreationtime       | timestamp | Time in UTC that the table was created.                                                                                                           |
| releffectivediststyle | integer   | The distribution style of a table or, if the table<br>uses automatic distribution, the current distribution style assigned<br>by Amazon Redshift. |

The RELEFFECTIVEDISTSTYLE column in PG_CLASS_INFO indicates the current
distribution style for the table. If the table uses automatic distribution,
RELEFFECTIVEDISTSTYLE is 10, 11, or 12, which indicates whether the effective
distribution style is AUTO (ALL), AUTO (EVEN), or AUTO (KEY). If the table uses automatic
distribution, the distribution style might initially show AUTO (ALL), then change to
AUTO (EVEN) when the table grows or AUTO (KEY) if a column is found to be useful as a distribution key.

The following table gives the distribution style for each value in
RELEFFECTIVEDISTSTYLE column:

| RELEFFECTIVEDISTSTYLE | Current distribution style |
| --------------------- | -------------------------- |
| 0                     | EVEN                       |
| 1                     | KEY                        |
| 8                     | ALL                        |
| 10                    | AUTO (ALL)                 |
| 11                    | AUTO (EVEN)                |
| 12                    | AUTO (KEY)                 |

## Example

The following query returns the current distribution style of tables in the catalog.

```
select reloid as tableid,trim(nspname) as schemaname,trim(relname) as tablename,reldiststyle,releffectivediststyle,
CASE WHEN "reldiststyle" = 0 THEN 'EVEN'::text
     WHEN "reldiststyle" = 1 THEN 'KEY'::text
     WHEN "reldiststyle" = 8 THEN 'ALL'::text
     WHEN "releffectivediststyle" = 10 THEN 'AUTO(ALL)'::text
     WHEN "releffectivediststyle" = 11 THEN 'AUTO(EVEN)'::text
     WHEN "releffectivediststyle" = 12 THEN 'AUTO(KEY)'::text ELSE '<<UNKNOWN>>'::text END as diststyle,relcreationtime
from pg_class_info a left join pg_namespace b on a.relnamespace=b.oid;
```

```

 tableid | schemaname | tablename | reldiststyle | releffectivediststyle | diststyle  |      relcreationtime
---------+------------+-----------+--------------+-----------------------+------------+----------------------------
 3638033 | public     | customer  |            0 |                     0 | EVEN       | 2019-06-13 15:02:50.666718
 3638037 | public     | sales     |            1 |                     1 | KEY        | 2019-06-13 15:03:29.595007
 3638035 | public     | lineitem  |            8 |                     8 | ALL        | 2019-06-13 15:03:01.378538
 3638039 | public     | product   |            9 |                    10 | AUTO(ALL)  | 2019-06-13 15:03:42.691611
 3638041 | public     | shipping  |            9 |                    11 | AUTO(EVEN) | 2019-06-13 15:03:53.69192
 3638043 | public     | support   |            9 |                    12 | AUTO(KEY)  | 2019-06-13 15:03:59.120695
(6 rows)

```
