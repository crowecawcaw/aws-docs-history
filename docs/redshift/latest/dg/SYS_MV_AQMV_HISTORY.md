

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_MV\_AQMV\_HISTORY

SYS\_MV\_AQMV\_HISTORY records automatic-query-rewrite decisions for user-created materialized views. Use this view to determine whether Amazon Redshift used a matched materialized view for a query or why the materialized view wasn't used.

SYS\_MV\_AQMV\_HISTORY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_MV_AQMV_HISTORY-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_id | integer | Identifier of the user who ran the query. | 
| query\_id | bigint | Identifier of the user query for which the decision was made. | 
| database\_name | character(128) | Database containing the materialized view. | 
| schema\_name | character(128) | Schema containing the materialized view. | 
| mv\_name | character(128) | Name of the materialized view. | 
| decision | character(128) | Description of whether the materialized view was used or why it wasn't used. | 
| detail | character(128) | Additional information for the decision. For a sort-key decision, this value identifies the column whose sort-key coverage caused the rewrite to be rejected. The value is empty for other decision types. | 

## Decision values
<a name="SYS_MV_AQMV_HISTORY-decision-values"></a>

Answering queries using materialized views (AQMV) is the automatic query rewriting process.

The `decision` column can contain the following values.
+ `Materialized view was used`
+ `Materialized view was used without cost evaluation because it is small`
+ `Materialized view was not used because its sort keys do not cover the partition key predicate`
+ `Materialized view was not used because its sort keys do not cover a predicate used for dynamic partition elimination`
+ `Materialized view was not used because the rewrite would lose dynamic partition elimination`
+ `Materialized view was not used because the rewrite would lose aggregate pushdown below join`
+ `Materialized view was not used because the rewrite was estimated to be slower`
+ `Materialized view was not used because AQMV timed out`
+ `Materialized view was not used because of an internal error`
+ `Unknown AQMV decision`

## Usage notes
<a name="SYS_MV_AQMV_HISTORY-usage-notes"></a>

This system view records decisions only for materialized views that match a query. If you don't see a materialized view in `SYS_MV_AQMV_HISTORY`, it might be stale or might not have been evaluated before automatic query rewriting timed out.

When you run a query, Amazon Redshift uses heuristics and cost estimates to decide whether to rewrite the query to use a materialized view. Because estimates can differ from actual performance, Amazon Redshift might occasionally skip a beneficial rewrite.

Use `SVV_MV_INFO.autorewrite` and `SVV_MV_INFO.is_stale` together with `SYS_MV_AQMV_HISTORY` when diagnosing automatic query rewriting.

## Sample query
<a name="SYS_MV_AQMV_HISTORY-sample-queries"></a>

The following query displays decisions for a specific query.

```sql
SELECT query_id,
       database_name,
       schema_name,
       mv_name,
       decision,
       detail
FROM sys_mv_aqmv_history
WHERE query_id = 123456789
ORDER BY schema_name, mv_name;
```

The query returns the following sample output:

```
 query_id | database_name | schema_name | mv_name  | decision                   | detail
----------+---------------+-------------+----------+----------------------------+-------
123456789 | dev           | public      | sales_mv | Materialized view was used |
```