Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_RLS_RELATION

Use SVV_RLS_RELATION to view a list of all relations that are RLS-protected.

SVV_RLS_RELATION is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name                    | Data type    | Description                                                                                            |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------ |
| datname                        | text         | The name of the database containing the<br>relation.                                                   |
| relschema                      | text         | The name of the schema containing the<br>relation.                                                     |
| relname                        | text         | The name of the relation.                                                                              |
| relkind                        | text         | The type of the relation, such as tables or<br>views.                                                  |
| is_rls_on                      | boolean      | The parameter that indicates whether the relation<br>is RLS-protected.                                 |
| is_rls_datashare_on            | boolean      | The parameter that indicates whether the relation is RLS-protected over datashares.                    |
| rls_conjunction_type           | character(3) | The parameter that indicates whether relation combine RLS policies with `and` or `or`.                 |
| rls_datashare_conjunction_type | character(3) | The parameter that indicates whether relation combine RLS policies with `and` or `or` over datashares. |

## Sample query

The following example displays the result of the SVV_RLS_RELATION.

```
ALTER TABLE tickit_category_redshift ROW LEVEL SECURITY ON FOR DATASHARES;


--Inspect RLS state on the relations using SVV_RLS_RELATION.
SELECT datname, relschema, relname, relkind, is_rls_on, is_rls_datashare_on FROM svv_rls_relation ORDER BY relname;

  datname  | relschema |        relname           | relkind | is_rls_on | is_rls_datashare_on | rls_conjunction_type | rls_datashare_conjunction_type
-----------+-----------+--------------------------+---------+-----------+---------------------+----------------------+--------------------------------
 tickit_db |   public  | tickit_category_redshift |  table  |      t    |           t         |          and         |              and
(1 row)
```
