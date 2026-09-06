

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ALTER\_TABLE\_RECOMMENDATIONS
<a name="r_SVV_ALTER_TABLE_RECOMMENDATIONS"></a>

Records the current Amazon Redshift Advisor recommendations for tables. This view shows recommendations for all tables, whether they are defined for automatic optimization or not. To view if a table is defined for automatic optimization, see [SVV\_TABLE\_INFO](r_SVV_TABLE_INFO.md). Entries appear only for tables visible in the current session's database. After a recommendation has been applied (either by Amazon Redshift or by you), it no longer appears in the view. 

SVV\_ALTER\_TABLE\_RECOMMENDATIONS is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SVV_ALTER_TABLE_RECOMMENDATIONS-table-rows"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| type  | character(30)  | The type of recommendation. Possible values are distkey and sortkey.  | 
| database  | character(128)  | The database name.  | 
| table\_id  | integer | The table identifier.  | 
| group\_id  | integer | The group number of a set of recommendations. All recommendations in a group should be applied to see the maximum benefit. Possible values are -1 for a sort key recommendation, and a number larger than zero for a distribution key recommendation.  | 
| ddl  | character(1024)  | The SQL statement that must run to apply the recommendation.  | 
| auto\_eligible | character(1)  | The value indicates if the recommendation is eligible for Amazon Redshift to run automatically. If this value is t, then the indication is true, if f then false.  | 

## Sample queries
<a name="r_SVV_ALTER_TABLE_RECOMMENDATIONS-sample-queries"></a>

In the following example, the rows in the result show recommendations for distribution key and sort key. The rows also show whether the recommendations are eligible for Amazon Redshift to automatically apply them. 

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