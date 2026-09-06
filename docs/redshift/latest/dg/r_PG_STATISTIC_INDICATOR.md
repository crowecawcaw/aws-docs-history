

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# PG\_STATISTIC\_INDICATOR
<a name="r_PG_STATISTIC_INDICATOR"></a>

Stores information about the number of rows inserted or deleted since the last ANALYZE. The PG\_STATISTIC\_INDICATOR table is updated frequently following DML operations, so statistics are approximate.

PG\_STATISTIC\_INDICATOR is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_PG_STATISTIC_INDICATOR-table-columns"></a>


| Column name | Data type  | Description  | 
| --- | --- | --- | 
| stairelid | oid | Table ID | 
| stairows | float | Total number of rows in the table. | 
| staiins | float  | Number of rows inserted since the last ANALYZE. | 
| staidels | float | Number of rows deleted or updated since the last ANALYZE. | 

## Example
<a name="r_PG_STATISTIC_INDICATOR-example"></a>

The following example returns information for table changes since the last ANALYZE. 

```
select * from pg_statistic_indicator;

stairelid | stairows | staiins | staidels
----------+----------+---------+---------
   108271 |       11 |       0 |        0
   108275 |      365 |       0 |        0
   108278 |     8798 |       0 |        0
   108280 |    91865 |       0 |   100632
   108267 |    89981 |   49990 |     9999
   108269 |      808 |     606 |      374
   108282 |   152220 |   76110 |   248566
```