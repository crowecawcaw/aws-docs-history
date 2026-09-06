

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Reviewing queue wait times for queries
<a name="review-queue-wait-times-for-queries"></a>

The following query shows how long recent queries waited for an open slot in a query queue before running. If you see a trend of high wait times, you might want to modify your query queue configuration for better throughput. For more information, see [Implementing manual WLM](cm-c-defining-query-queues.md).

```
select trim(database) as DB , w.query, 
substring(q.querytxt, 1, 100) as querytxt,  w.queue_start_time, 
w.service_class as class, w.slot_count as slots, 
w.total_queue_time/1000000 as queue_seconds, 
w.total_exec_time/1000000 exec_seconds, (w.total_queue_time+w.total_Exec_time)/1000000 as total_seconds 
from stl_wlm_query w 
left join stl_query q on q.query = w.query and q.userid = w.userid 
where w.queue_start_Time >= dateadd(day, -7, current_Date) 
and w.total_queue_Time > 0  and w.userid >1   
and q.starttime >= dateadd(day, -7, current_Date) 
order by w.total_queue_time desc, w.queue_start_time desc limit 35;
```