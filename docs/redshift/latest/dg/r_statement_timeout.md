Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# statement_timeout

## Values (default in bold)

**0 (turns off limitation)**, x milliseconds

## Description

Stops any statement that takes over the specified number of milliseconds.

The `statement_timeout` value is the maximum amount of time a query can
run before Amazon Redshift terminates it. This time includes planning, queueing in workload
management (WLM), and execution time. Compare this time to WLM timeout
(max_execution_time) and a QMR (query_execution_time), which include only execution
time.

If WLM timeout (max_execution_time) is also specified as part of a WLM configuration,
the lower of statement_timeout and max_execution_time is used. For more information, see
[WLM timeout](cm-c-defining-query-queues.md#wlm-timeout "cm-c-defining-query-queues.md#wlm-timeout").

## Example

Because the following query takes longer than 1 millisecond, it times out and is
canceled.

```
set statement_timeout = 1;

select * from listing where listid>5000;
ERROR:  Query (150) canceled on user's request
```
