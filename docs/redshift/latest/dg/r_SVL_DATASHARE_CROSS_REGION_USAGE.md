

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_DATASHARE\_CROSS\_REGION\_USAGE
<a name="r_SVL_DATASHARE_CROSS_REGION_USAGE"></a>

Use the SVL\_DATASHARE\_CROSS\_REGION\_USAGE view to get a summary of cross-Region data transferred usage caused by cross-Region datasharing query. SVL\_DATASHARE\_CROSS\_REGION\_USAGE aggregates details at the segment level.

SVL\_DATASHARE\_CROSS\_REGION\_USAGE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_DATASHARE\_CROSS\_REGION\_USAGE](r_SYS_DATASHARE_CROSS_REGION_USAGE.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_SVL_DATASHARE_CROSS_REGION_USAGE-table-rows"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| query | integer | The ID of the query. Use this value to join other system tables and views. | 
| segment | bigint | The number of the segment. A query consists of multiple segments, and each segment consists of one or more steps. | 
| start\_time | time | The time in UTC that the data transfer began. | 
| end\_time | time | The time in UTC that the data transfer ended. | 
| transferred\_data | bigint | The number of bytes of data transferred from a producer Region to a consumer Region. | 
| source\_region | char(25) | The producer Region that the query transferred data from. | 
| recordtime | timestamp | The time when the action is recorded. | 

## Sample queries
<a name="r_SVL_DATASHARE_CROSS_REGION_USAGE-sample-queries"></a>

The following example shows a SVL\_DATASHARE\_CROSS\_REGION\_USAGE view.

```
SELECT query, segment, transferred_data, source_region
from svl_datashare_cross_region_usage
where query = pg_last_query_id()
order by query,segment;

  query | segment | transferred_data | source_region 
--------+---------+------------------+---------------
 200048 |       2 |          4194304 |    us-west-1  
 200048 |       2 |          4194304 |    us-east-2
```