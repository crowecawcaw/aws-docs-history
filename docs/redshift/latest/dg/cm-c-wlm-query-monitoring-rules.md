Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# WLM query monitoring rules

In Amazon Redshift workload management (WLM), query monitoring rules define metrics-based
performance boundaries for WLM queues and specify what action to take when a query goes
beyond those boundaries. For example, for a queue dedicated to short running queries, you
might create a rule that cancels queries that run for more than 60 seconds. To track poorly
designed queries, you might have another rule that logs queries that contain nested loops.

You define query monitoring rules as part of your workload management (WLM)
configuration. You can define up to 25 rules for each queue, with a limit of 25 rules for
all queues. Each rule includes up to three conditions, or predicates, and one action. A
_predicate_ consists of a metric, a comparison condition (=, <, or

> ), and a value. If all of the predicates for any rule are met, that rule's action is
> triggered. Possible rule actions are log, hop, and abort, as discussed following.

The rules in a given queue apply only to queries running in that queue. A rule is
independent of other rules.

WLM evaluates metrics every 10 seconds. Amazon Redshift applies query monitoring rules at the child query level
when queries are automatically rewritten. If more than one rule is triggered during the
same period, WLM chooses the rule with the most severe action.
If the action for two rules has the same severity, WLM runs the rules in alphabetical order, based on the rule name.
If the action is hop or abort, the action is logged and the query is evicted from the queue. If
the action is log, the query continues to run in the queue. WLM initiates only one log
action per query per rule. If the queue contains other rules, those rules remain in effect.
If the action is hop and the query is routed to another queue, the rules for the new queue
apply. For more information about query monitoring and tracking actions taken on specific queries, see the collection of samples at [Short query
acceleration](wlm-short-query-acceleration.md "wlm-short-query-acceleration.md").

When all of a rule's predicates are met, WLM writes a row to the [STL_WLM_RULE_ACTION](r_STL_WLM_RULE_ACTION.md "r_STL_WLM_RULE_ACTION.md") system table. In
addition, Amazon Redshift records query metrics for currently running queries to [STV_QUERY_METRICS](r_STV_QUERY_METRICS.md "r_STV_QUERY_METRICS.md"). Metrics for
completed queries are stored in [STL_QUERY_METRICS](r_STL_QUERY_METRICS.md "r_STL_QUERY_METRICS.md").

###### Note

For Amazon Redshift Serverless, you can configure query queues and monitoring rules using the `wlm_json_configuration` parameter.
This allows you to create multiple queues with different user roles, query groups, and monitoring rules.
For more information about configuring serverless query queues, see
[Setting query queues](../mgmt/serverless-workgroup-query-queues.md "../mgmt/serverless-workgroup-query-queues.md")
in the _Amazon Redshift Management Guide_.

## Defining a query monitoring

rule

You create query monitoring rules as part of your WLM configuration, which you define
as part of your cluster's parameter group definition.

You can create rules using the AWS Management Console or programmatically using JSON.

###### Note

If you choose to create rules programmatically, we strongly recommend using the
console to generate the JSON that you include in the parameter group definition. For
more information, see

[Creating a query monitoring rule](../mgmt/parameter-group-modify-qmr-console.md "../mgmt/parameter-group-modify-qmr-console.md")

and
[Configuring Parameter Values Using the AWS CLI](../mgmt/working-with-parameter-groups.md#configure-parameters-using-the-cli "../mgmt/working-with-parameter-groups.md#configure-parameters-using-the-cli") in the
_Amazon Redshift Management Guide_.

To define a query monitoring rule, you specify the following elements:

- A rule name – Rule names must be unique within the WLM configuration.
  Rule names can be up to 32 alphanumeric characters or underscores, and can't
  contain spaces or quotation marks. You can have up to 25 rules per queue, and the
  total limit for all queues is 25 rules.
- One or more predicates – You can have up to three predicates per rule.
  If all the predicates for any rule are met, the associated action is triggered. A
  predicate is defined by a metric name, an operator ( =, <, or > ), and a
  value. An example is `query_cpu_time > 100000`. For a list of
  metrics and examples of values for different metrics, see [Query monitoring metrics for Amazon Redshift provisioned](#cm-c-wlm-query-monitoring-metrics "#cm-c-wlm-query-monitoring-metrics") following in this section.
- An action – If more than one rule is triggered, WLM chooses the rule
  with the most severe action. Possible actions, in ascending order of severity,
  are:
  - Log – Record information about the query in the
    STL_WLM_RULE_ACTION system table. Use the Log action when you want to only
    write a log record. WLM creates at most one log per query, per rule.
    Following a log action, other rules remain in force and WLM continues to
    monitor the query.
  - Hop (only available with manual WLM) – Log the action and hop the query to the next matching queue.
    If there isn't another matching queue, the query is canceled. QMR hops only
    [CREATE TABLE AS](r_CREATE_TABLE_AS.md "r_CREATE_TABLE_AS.md")
    (CTAS) statements and read-only queries, such as SELECT statements. For more
    information, see [WLM query queue hopping](wlm-queue-hopping.md "wlm-queue-hopping.md").
  - Abort – Log the action and cancel the query. QMR doesn't stop
    COPY statements and maintenance operations, such as ALTER, ANALYZE and VACUUM.
  - Change priority (only available with automatic WLM) – Change the priority of a query.

To limit the runtime of queries, we recommend creating a query monitoring rule
instead of using WLM timeout. For example, you can set `max_execution_time`
to 50,000 milliseconds as shown in the following JSON snippet.

```
"max_execution_time": 50000
```

But we recommend instead that you define an equivalent query monitoring rule.
The following example demonstrates a query monitoring rule that
sets `query_execution_time` to 50 seconds:

```
"rules":
[
    {
        "rule_name": "rule_query_execution",
        "predicate": [
            {
                "metric_name": "query_execution_time",
                "operator": ">",
                "value": 50
            }
        ],
        "action": "abort"
    }
]
```

For steps to create or modify a query monitoring rule, see

[Creating a query monitoring rule](../mgmt/parameter-group-modify-qmr-console.md "../mgmt/parameter-group-modify-qmr-console.md")

and [Properties in
the wlm_json_configuration Parameter](../mgmt/workload-mgmt-config.md#wlm-json-config-properties "../mgmt/workload-mgmt-config.md#wlm-json-config-properties") in the
_Amazon Redshift Management Guide_.

You can find more information about query monitoring rules in the following topics:

- [Query monitoring metrics for Amazon Redshift provisioned](#cm-c-wlm-query-monitoring-metrics "#cm-c-wlm-query-monitoring-metrics")
- [Query monitoring rules
  templates](#cm-c-wlm-query-monitoring-templates "#cm-c-wlm-query-monitoring-templates")
- [Creating a query monitoring rule](../mgmt/parameter-group-modify-qmr-console.md "../mgmt/parameter-group-modify-qmr-console.md")
- [Configuring Workload
  Management](../mgmt/workload-mgmt-config.md "../mgmt/workload-mgmt-config.md")
- [System tables and views for query
  monitoring rules](#cm-c-wlm-qmr-tables-and-views "#cm-c-wlm-qmr-tables-and-views")

## Query monitoring metrics for Amazon Redshift provisioned

The following table describes the metrics used in query monitoring rules. (These
metrics are distinct from the metrics stored in the [STV_QUERY_METRICS](r_STV_QUERY_METRICS.md "r_STV_QUERY_METRICS.md") and [STL_QUERY_METRICS](r_STL_QUERY_METRICS.md "r_STL_QUERY_METRICS.md") system tables.)

For a given metric, the performance threshold is tracked either at the query level or
the segment level. For more information about segments and steps, see [Query planning and execution workflow](c-query-planning.md "c-query-planning.md").

###### Note

The [WLM timeout](cm-c-defining-query-queues.md#wlm-timeout "cm-c-defining-query-queues.md#wlm-timeout") parameter is
distinct from query monitoring rules.

| Metric                     | Name                         | Description                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Query CPU time             | `query_cpu_time`             | CPU time used by the query, in seconds. `CPU<br>time` is distinct from `Query execution time`.<br>Valid values are 0–999,999.                                                                                                                                            |
| Blocks read                | `query_blocks_read`          | Number of 1 MB data blocks read by the query.Valid<br>values are 0–1,048,575.                                                                                                                                                                                            |
| Scan row count             | `scan_row_count`             | The number of rows in a scan step. The row count is the total number<br>of rows emitted before filtering rows marked for deletion (ghost rows)<br>and before applying user-defined query filters.<br>Valid values are 0–999,999,999,999,999.                             |
| Query execution time       | `query_execution_time`       | Elapsed execution time for a query, in seconds. Execution<br>time doesn't include time spent waiting in a queue.Valid values are 0–86,399.                                                                                                                               |
| Query queue time           | `query_queue_time`           | Time spent waiting in a queue, in seconds. Valid values are 0–86,399.                                                                                                                                                                                                    |
| CPU usage                  | `query_cpu_usage_percent`    | Percent of CPU capacity used by the query.Valid<br>values are 0–6,399.                                                                                                                                                                                                   |
| Memory to disk             | `query_temp_blocks_to_disk`  | Temporary disk space used to write intermediate results,<br>in 1 MB blocks.Valid values are 0–319,815,679.                                                                                                                                                               |
| CPU skew                   | `cpu_skew`                   | The ratio of maximum CPU usage for any slice to average<br>CPU usage for all slices. This metric is defined at the segment<br>level.Valid values are 0–99.                                                                                                               |
| I/O skew                   | `io_skew`                    | The ratio of maximum blocks read (I/O) for any slice to<br>average blocks read for all slices. This metric is defined at the segment<br>level.Valid values are 0–99.                                                                                                     |
| Rows joined                | `join_row_count`             | The number of rows processed in a join step.Valid<br>values are 0–999,999,999,999,999.                                                                                                                                                                                   |
| Nested loop join row count | `nested_loop_join_row_count` | The number or rows in a nested loop join.Valid<br>values are 0–999,999,999,999,999.                                                                                                                                                                                      |
| Return row count           | `return_row_count`           | The number of rows returned by the query. Valid<br>values are 0–999,999,999,999,999.                                                                                                                                                                                     |
| Segment execution time     | `segment_execution_time`     | Elapsed execution time for a single segment, in seconds.<br>To avoid or reduce sampling errors, include `segment_execution_time<br>> 10` in your rules.Valid values are 0–86,388.                                                                                        |
| Spectrum scan row count    | `spectrum_scan_row_count`    | The number of rows of data in Amazon S3 scanned by an<br>Amazon Redshift Spectrum query. Valid values are 0–999,999,999,999,999.                                                                                                                                         |
| Spectrum scan size         | `spectrum_scan_size_mb`      | The size of data in Amazon S3, in MB, scanned by an Amazon Redshift<br>Spectrum query.Valid values are 0–999,999,999,999,999.                                                                                                                                            |
| Query priority             | `query_priority`             | The priority of the query.<br>Valid values are `HIGHEST`, `HIGH`, `NORMAL`, `LOW`, and `LOWEST`.<br>When comparing `query_priority` using greater than (>) and less than (<) operators, `HIGHEST` is greater than `HIGH`,<br>`HIGH` is greater than `NORMAL`, and so on. |

###### Note

- The hop action is not supported with the `query_queue_time` predicate.
  That is, rules defined to hop when a `query_queue_time` predicate is met are ignored.
- Short segment execution times can result in sampling errors with some metrics,
  such as `io_skew` and `query_cpu_usage_percent`. To avoid or reduce
  sampling errors, include segment execution time in your rules. A good starting point
  is `segment_execution_time > 10`.

The [SVL_QUERY_METRICS](r_SVL_QUERY_METRICS.md "r_SVL_QUERY_METRICS.md") view
shows the metrics for completed queries. The [SVL_QUERY_METRICS_SUMMARY](r_SVL_QUERY_METRICS_SUMMARY.md "r_SVL_QUERY_METRICS_SUMMARY.md") view shows the maximum values of
metrics for completed queries. Use the values in these views as an aid to determine
threshold values for defining query monitoring rules.

## Query monitoring metrics for Amazon Redshift Serverless

The following table describes the metrics used in query monitoring rules for Amazon Redshift Serverless.

| Metric                     | WLM Predicate Name           | Name                             | Description                                                                                                                                                                                                                                  |
| -------------------------- | ---------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Blocks read                | `query_blocks_read`          | `max_query_blocks_read`          | Number of 1 MB data blocks read by the query.Valid<br>values are 0–1,048,575.                                                                                                                                                                |
| Scan row count             | `scan_row_count`             | `max_scan_row_count`             | The number of rows in a scan step. The row count is the total number<br>of rows emitted before filtering rows marked for deletion (ghost rows)<br>and before applying user-defined query filters.<br>Valid values are 0–999,999,999,999,999. |
| Query execution time       | `query_execution_time`       | max_query_execution_time         | Elapsed execution time for a query, in seconds.<br>Execution time doesn't include time spent waiting in a queue. If a query exceeds the set execution time, Amazon Redshift Serverless stops the query.<br>Valid values are 0–86,399.        |
| Query queue time           | `query_queue_time`           | `max_query_queue_time`           | Time spent waiting in a queue, in seconds. Valid values are 0–86,399.                                                                                                                                                                        |
| Memory to disk             | `query_temp_blocks_to_disk`  | `max_query_temp_blocks_to_disk`  | Temporary disk space used to write intermediate results,<br>in 1 MB blocks.Valid values are 0–319,815,679.                                                                                                                                   |
| Rows joined                | `join_row_count`             | `max_join_row_count`             | The number of rows processed in a join step.Valid<br>values are 0–999,999,999,999,999.                                                                                                                                                       |
| Nested loop join row count | `nested_loop_join_row_count` | `max_nested_loop_join_row_count` | The number or rows in a nested loop join.Valid<br>values are 0–999,999,999,999,999.                                                                                                                                                          |

###### Note

- The hop action is not supported with the `max_query_queue_time` predicate.
  That is, rules defined to hop when a `max_query_queue_time` predicate is met are ignored.
- Short segment execution times can result in sampling errors with some metrics,
  such as `max_io_skew` and `max_query_cpu_usage_percent`.

For Amazon Redshift Serverless, you can configure query queues and monitoring rules using the `wlm_json_configuration` parameter.
This allows you to create multiple queues with different user roles, query groups, and monitoring rules using the metrics listed above.
For more information about configuring serverless query queues, see
[WLM JSON configuration structure](../mgmt/serverless-workgroup-query-queues.md#serverless-wlm-json-configuration "../mgmt/serverless-workgroup-query-queues.md#serverless-wlm-json-configuration")
in the _Amazon Redshift Management Guide_.

## Query monitoring rules

templates

When you add a rule using the Amazon Redshift console, you can choose to create a rule from
a predefined template. Amazon Redshift creates a new rule with a set of predicates and
populates the predicates with default values. The default action is log. You can modify
the predicates and action to meet your use case.

The following table lists available templates.

| Template Name                                     | Predicates                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nested loop join                                  | `nested_loop_join_row_count > 100`                     | A nested loop join might indicate an incomplete join<br>predicate, which often results in a very large return set (a Cartesian<br>product). Use a low row count to find a potentially runaway query<br>early.                                                                                                                                                                                                                                                                                                        |
| Query returns a high number of rows               | `return_row_count > 1000000`                           | If you dedicate a queue to simple, short running queries,<br>you might include a rule that finds queries returning a high row count. The<br>template uses a default of 1 million rows. For some systems, you might<br>consider one million rows to be high, or in a larger system, a billion or<br>more rows might be high.                                                                                                                                                                                          |
| Join with a high number of rows                   | `join_row_count > 1000000000`                          | A join step that involves an unusually high number of<br>rows might indicate a need for more restrictive filters. The template uses a<br>default of 1 billion rows. For an ad hoc (one-time) queue that's<br>intended for quick, simple queries, you might use a lower number.                                                                                                                                                                                                                                       |
| High disk usage when writing intermediate results | `query_temp_blocks_to_disk > 100000`                   | When currently executing queries use more than the<br>available system RAM, the query execution engine writes intermediate results<br>to disk (spilled memory). Typically, this condition is the result of a rogue<br>query, which usually is also the query that uses the most disk space. The<br>acceptable threshold for disk usage varies based on the cluster node type<br>and number of nodes. The template uses a default of 100,000 blocks, or 100<br>GB. For a small cluster, you might use a lower number. |
| Long running query with high I/O skew             | `segment_execution_time > 120` and<br>`io_skew > 1.30` | I/O skew occurs when one node slice has a much higher I/O<br>rate than the other slices. As a starting point, a skew of 1.30 (1.3 times<br>average) is considered high. High I/O skew is not always a problem, but when<br>combined with a long running query time, it might indicate a problem with<br>the distribution style or sort key.                                                                                                                                                                          |

## System tables and views for query

monitoring rules

When all of a rule's predicates are met, WLM writes a row to the [STL_WLM_RULE_ACTION](r_STL_WLM_RULE_ACTION.md "r_STL_WLM_RULE_ACTION.md") system table.
This row contains details for the query that triggered the rule and the resulting
action.

In addition, Amazon Redshift records query metrics the following system tables and views.

- The [STV_QUERY_METRICS](r_STV_QUERY_METRICS.md "r_STV_QUERY_METRICS.md")
  table displays the metrics for currently running queries.
- The [STL_QUERY_METRICS](r_STL_QUERY_METRICS.md "r_STL_QUERY_METRICS.md")
  table records the metrics for completed queries.
- The [SVL_QUERY_METRICS](r_SVL_QUERY_METRICS.md "r_SVL_QUERY_METRICS.md")
  view shows the metrics for completed queries.
- The [SVL_QUERY_METRICS_SUMMARY](r_SVL_QUERY_METRICS_SUMMARY.md "r_SVL_QUERY_METRICS_SUMMARY.md") view shows the maximum values of
  metrics for completed queries.
