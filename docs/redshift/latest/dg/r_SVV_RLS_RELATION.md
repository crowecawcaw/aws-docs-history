

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_RLS\_RELATION
<a name="r_SVV_RLS_RELATION"></a>

Use SVV\_RLS\_RELATION to view a list of all relations that are RLS-protected.

SVV\_RLS\_RELATION is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SVV_RLS_RELATION-table-columns"></a>


| Column name  | Data type  | Description | 
| --- | --- | --- | 
| datname | text | The name of the database containing the relation. | 
| relschema | text | The name of the schema containing the relation. | 
| relname | text | The name of the relation. | 
| relkind | text | The type of the relation, such as tables or views. | 
| is\_rls\_on | boolean | The parameter that indicates whether the relation is RLS-protected. | 
| is\_rls\_datashare\_on | boolean | The parameter that indicates whether the relation is RLS-protected over datashares. | 
| rls\_conjunction\_type | character(3) | The parameter that indicates whether relation combine RLS policies with and or or. | 
| rls\_datashare\_conjunction\_type | character(3) | The parameter that indicates whether relation combine RLS policies with and or or over datashares. | 

## Sample query
<a name="r_SVV_RLS_RELATION-sample-query"></a>

The following example displays the result of the SVV\_RLS\_RELATION.

```
ALTER TABLE tickit_category_redshift ROW LEVEL SECURITY ON FOR DATASHARES;       

            
--Inspect RLS state on the relations using SVV_RLS_RELATION.
SELECT datname, relschema, relname, relkind, is_rls_on, is_rls_datashare_on FROM svv_rls_relation ORDER BY relname;

  datname  | relschema |        relname           | relkind | is_rls_on | is_rls_datashare_on | rls_conjunction_type | rls_datashare_conjunction_type
-----------+-----------+--------------------------+---------+-----------+---------------------+----------------------+--------------------------------
 tickit_db |   public  | tickit_category_redshift |  table  |      t    |           t         |          and         |              and
(1 row)
```