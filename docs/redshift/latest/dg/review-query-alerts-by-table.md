Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Reviewing query alerts by table

The following query identifies tables that have had alert events logged for them,
and also identifies what type of alerts are most frequently raised.

If the `minutes` value for a row with an identified table is high,
check that table to see if it needs routine
maintenance, such as having [ANALYZE](r_ANALYZE.md "r_ANALYZE.md") or [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md") run against
it.

If the `count` value is high for a row but the `table` value
is null, run a query against STL_ALERT_EVENT_LOG for the associated
`event` value to investigate why that alert is getting raised so
often.

```
select trim(s.perm_table_name) as table,
(sum(abs(datediff(seconds, s.starttime, s.endtime)))/60)::numeric(24,0) as minutes, trim(split_part(l.event,':',1)) as event,  trim(l.solution) as solution,
max(l.query) as sample_query, count(*)
from stl_alert_event_log as l
left join stl_scan as s on s.query = l.query and s.slice = l.slice
and s.segment = l.segment and s.step = l.step
where l.event_time >=  dateadd(day, -7, current_Date)
group by 1,3,4
order by 2 desc,6 desc;
```
