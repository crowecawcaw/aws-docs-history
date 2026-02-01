Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# wlm_query_slot_count

## Values (default in bold)

**1**, 1 to 50 (cannot exceed number of available slots
(concurrency level) for the service class)

## Description

Sets the number of query slots that a query uses.

Workload management (WLM) reserves slots in a service class according to the
concurrency level set for the queue. For example, if concurrency level is set to 5, then
the service class has 5 slots. WLM allocates the available memory for a service class
equally to each slot. For more information, see [Workload
management](cm-c-implementing-workload-management.md "cm-c-implementing-workload-management.md").

###### Note

If the value of wlm_query_slot_count is larger than the number of available slots
(concurrency level) for the service class, the query fails. If you encounter an
error, decrease wlm_query_slot_count to an allowable value.

For operations where performance is heavily affected by the amount of memory
allocated, such as vacuuming, increasing the value of wlm_query_slot_count can improve
performance. In particular, for slow vacuum commands, inspect the corresponding record
in the SVV_VACUUM_SUMMARY view. If you see high values (close to or higher than 100) for
sort_partitions and merge_increments in the SVV_VACUUM_SUMMARY view, consider increasing
the value for wlm_query_slot_count the next time you run Vacuum against that
table.

Increasing the value of wlm_query_slot_count limits the number of concurrent queries
that can be run. For example, suppose that the service class has a concurrency level of
5 and wlm_query_slot_count is set to 3. While a query is running within the session with
wlm_query_slot_count set to 3, a maximum of 2 more concurrent queries can be run within
the same service class. Subsequent queries wait in the queue until currently running
queries complete and slots are freed.

## Examples

Use the SET command to set the value of wlm_query_slot_count for the duration of the
current session.

```
set wlm_query_slot_count to 3;
```
