

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Identifying queries with nested loops
<a name="identify-queries-with-nested-loops"></a>

The following query identifies queries that have had alert events logged for nested loops. For information on how to fix the nested loop condition, see [Nested loop](query-performance-improvement-opportunities.md#nested-loop).

```
select query, trim(querytxt) as SQL, starttime 
from stl_query 
where query in (
select distinct query 
from stl_alert_event_log 
where event like 'Nested Loop Join in the query plan%') 
order by starttime desc;
```