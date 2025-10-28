Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Implementing manual WLM

With manual WLM, you can manage system performance and your users' experience by
modifying the WLM configuration to create separate queues for the long-running queries
and short-running queries.

When users run queries in Amazon Redshift, the queries are routed to query queues. Each query
queue contains a number of query slots. Each queue is allocated a portion of the cluster's
available memory. A queue's memory is divided among the queue's query slots. You can
enable Amazon Redshift to manage query concurrency with automatic WLM.
For more information, see [Implementing automatic WLM](automatic-wlm.md "automatic-wlm.md").

Or you can configure WLM properties for each query queue. You do so to specify the way
that memory is allocated among slots and how queries can be routed to specific queues at
runtime. You can also configure WLM properties to cancel long-running queries.

By default, Amazon Redshift configures the following query queues:

- **One superuser queue**

The superuser queue is reserved for superusers only and it can't be configured.
Use this queue only when you need to run queries that affect the system or for
troubleshooting purposes. For example, use this queue when you need to cancel a
user's long-running query or to add users to the database. Don't use it to
perform routine queries. The queue doesn't appear in the console, but it does appear
in the system tables in the database as the fifth queue. To run a query in the
superuser queue, a user must be logged in as a superuser, and must run the query
using the predefined `superuser` query group.

- **One default user queue**

The default queue is initially configured to run five queries concurrently. When you use manual WLM, you
can change the concurrency, timeout, and memory allocation properties for the default
queue, but you cannot specify user groups or query groups. The default queue must be
the last queue in the WLM configuration. Any queries that are not routed to other
queues run in the default queue.
Query queues are defined in the WLM configuration. The WLM configuration is an editable
parameter (`wlm_json_configuration`) in a parameter group, which can be
associated with one or more clusters.
For more information, see [Configuring Workload
Management](../mgmt/workload-mgmt-config.md "../mgmt/workload-mgmt-config.md") in the _Amazon Redshift Management Guide_.

You can add additional query queues to the default WLM configuration, up to a total of
eight user queues. You can configure the following for each query queue:

- Concurrency scaling mode
- Concurrency level
- User groups
- Query groups
- WLM memory percent to use
- WLM timeout
- WLM query queue hopping
- Query monitoring rules

## Concurrency scaling mode

When concurrency scaling is enabled, Amazon Redshift automatically adds additional cluster
capacity when you need it to process an increase in concurrent read and write queries. Users see the most current data,
whether the queries run on the main cluster or on a concurrency scaling cluster.

You manage which queries are sent to the concurrency scaling cluster by configuring
WLM queues. When you enable concurrency scaling for a queue, eligible queries are sent
to the concurrency scaling cluster instead of waiting in a queue. For more information, see
[Concurrency scaling](concurrency-scaling.md "concurrency-scaling.md").

## Concurrency level

Queries in a queue run concurrently until they reach the WLM query slot count, or
_concurrency_ level, defined for that queue. Subsequent queries
then wait in the queue.

###### Note

WLM concurrency level is different from the number of concurrent user connections
that can be made to a cluster.

For more information, see [Connecting to a Cluster](../mgmt/connecting-to-cluster.md "../mgmt/connecting-to-cluster.md") in the
_Amazon Redshift Management Guide_.

In an automatic WLM configuration, which is recommended, the concurrency level is set to
**Auto**. Amazon Redshift dynamically allocates memory to queries, which subsequently determines how many to
run concurrently. This is based on the resources required for both running and queued queries. Auto WLM isn't
configurable. For more information, see [Implementing automatic WLM](automatic-wlm.md "automatic-wlm.md").

In a manual WLM configuration, Amazon Redshift statically allocates a fixed amount of memory to each
queue. The queue's memory is split evenly among the query slots. To illustrate, if a queue is
allocated 20% of a cluster's memory and has 10 slots, each query is allocated 2% of the cluster's
memory. The memory allocation remains fixed regardless of the number
of queries running concurrently. Because of this fixed memory allocation, queries that run
entirely in memory when the slot count is 5 might write intermediate results to disk if the slot count is increased
to 20. In this instance each query's share of the queue's memory is reduced from 1/5th
to 1/20th. The additional disk I/O could degrade performance.

The maximum slot count across all user-defined queues is 50. This limits the total slots for all
queues, including the default queue. The only queue that
isn't subject to the limit is the reserved superuser queue.

By default, manual WLM queues have a concurrency level of 5. Your workload might benefit
from a higher concurrency level in certain cases, such as the following:

- If many small queries are forced to wait for long-running queries, create a
  separate queue with a higher slot count and assign the smaller queries to that
  queue. A queue with a higher concurrency level has less memory allocated to each
  query slot, but the smaller queries require less memory.

###### Note

If you enable short-query acceleration (SQA), WLM automatically prioritizes
short queries over longer-running queries, so you don't need a separate queue
for short queries for most workflows. For more information, see [Short query
acceleration](wlm-short-query-acceleration.md "wlm-short-query-acceleration.md").

- If you have multiple queries that each access data on a single slice, set up a
  separate WLM queue to run those queries concurrently. Amazon Redshift assigns
  concurrent queries to separate slices, which allows multiple queries to run in
  parallel on multiple slices. For example, if a query is a simple aggregate with a
  predicate on the distribution key, the data for the query is located on a single
  slice.

### A manual WLM example

This example is a simple, manual WLM scenario to show how slots and memory can be allocated. You implement manual WLM with three queues, which are the following:

- _data-ingestion queue_ – This is set up for ingesting data. It's allocated 20% of the
  cluster's memory and it has 5 slots. Subsequently, 5 queries can run concurrently in the queue and each is allocated
  4% of the memory.
- _data-scientist queue_ – This is designed for memory-intensive queries. It's
  allocated 40% of the cluster's memory and it has 5 slots. Subsequently, 5 queries can run concurrently and each is
  allocated 8% of the memory.
- _default queue_ – This is designed for the majority of
  the users in the organization. This includes sales and accounting groups that typically have short
  or medium running queries that aren't complicated. It's allocated 40% of the cluster's memory and it has
  40 slots. 40 queries can run concurrently in this queue, with each query allocated 1% of the memory. This is the
  maximum number of slots that can be allocated for this queue because between all queues the limit is 50.

If you're running automatic WLM and your workload requires more than 15 queries to run in parallel, we recommend
turning on concurrency scaling. This is because increasing the query slot count above 15 might create contention for
system resources and limit the overall throughput of a single cluster. With concurrency scaling, you can run hundreds
of queries in parallel, up to a configured number of concurrency scaling clusters.
The number of concurrency scaling clusters is controlled by
[max_concurrency_scaling_clusters](r_max_concurrency_scaling_clusters.md "r_max_concurrency_scaling_clusters.md").
For more information about concurrency scaling, see [Concurrency scaling](concurrency-scaling.md "concurrency-scaling.md").

For more information, see [Query performance improvement](query-performance-improvement-opportunities.md "query-performance-improvement-opportunities.md").

## User groups

You can assign a set of user groups to a queue by specifying each user group name or
by using wildcards. When a member of a listed user group runs a query, that query runs
in the corresponding queue. There is no set limit on the number of user groups that can
be assigned to a queue. For more information, see
[Assigning queries to queues based on user groups](cm-c-executing-queries.md#cm-c-executing-queries-assigning-queries-to-queues-based-on-user-groups "cm-c-executing-queries.md#cm-c-executing-queries-assigning-queries-to-queues-based-on-user-groups").

## User roles

You can assign a set of user roles to a queue by specifying each user role name or
by using wildcards. When a member of a listed user role runs a query, that query runs
in the corresponding queue. There is no set limit on the number of user roles that can
be assigned to a queue. For more information, see
[Assigning queries to queues based on user roles](cm-c-executing-queries.md#cm-c-executing-queries-assigning-queries-to-queues-based-on-user-roles "cm-c-executing-queries.md#cm-c-executing-queries-assigning-queries-to-queues-based-on-user-roles").

## Query groups

You can assign a set of query groups to a queue by specifying each query group name
or by using wildcards. A query group is simply a label. At runtime, you can assign the
query group label to a series of queries. Any queries that are assigned to a listed
query group run in the corresponding queue. There is no set limit to the number of query
groups that can be assigned to a queue. For more
information, see [Assigning a
query to a query group](cm-c-executing-queries.md#cm-c-executing-queries-assigning-a-query-to-a-query-group "cm-c-executing-queries.md#cm-c-executing-queries-assigning-a-query-to-a-query-group").

## Wildcards

If wildcards are enabled in the WLM queue configuration, you can assign user groups
and query groups to a queue either individually or by using Unix shell-style wildcards.
The pattern matching is case-insensitive.

For example, the '\*' wildcard character matches any number of characters. Thus, if
you add `dba_*` to the list of user groups for a queue, any user-run query
that belongs to a group with a name that begins with `dba_` is assigned to
that queue. Examples are `dba_admin` or `DBA_primary`, . The '?'
wildcard character matches any single character. Thus, if the queue includes user-group
`dba?1`, then user groups named `dba11` and `dba21`
match, but `dba12` doesn't match.

Wildcards are turned off by default.

## WLM memory percent to use

In an automatic WLM configuration, memory percent is set to `auto`. For more information, see
[Implementing automatic WLM](automatic-wlm.md "automatic-wlm.md").

In a manual WLM configuration, to specify the amount of available memory that is allocated to a query, you can set
the `WLM Memory Percent to Use` parameter. By default, each user-defined
queue is allocated an equal portion of the memory that is available for user-defined
queries. For example, if you have four user-defined queues, each queue is allocated 25
percent of the available memory. The superuser queue has its own allocated memory and
cannot be modified. To change the allocation, you assign an integer percentage of memory
to each queue, up to a total of 100 percent. Any unallocated memory is managed by
Amazon Redshift and can be temporarily given to a queue if the queue requests additional memory
for processing.

For example, if you configure four queues, you can allocate memory as follows: 20
percent, 30 percent, 15 percent, 15 percent. The remaining 20 percent is unallocated and
managed by the service.

## WLM timeout

WLM timeout (`max_execution_time`) is deprecated.
Instead, create a query monitoring rule (QMR) using `query_execution_time` to limit the elapsed execution time for a query.
For more information, see [WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md "cm-c-wlm-query-monitoring-rules.md").

To limit the amount of time that queries in a given WLM queue are permitted to use,
you can set the WLM timeout value for each queue. The timeout parameter specifies the
amount of time, in milliseconds, that Amazon Redshift waits for a query to run before
either canceling or hopping the query. The timeout is based on query execution time and
doesn't include time spent waiting in a queue.

WLM attempts to hop [CREATE TABLE AS](r_CREATE_TABLE_AS.md "r_CREATE_TABLE_AS.md") (CTAS) statements and read-only queries, such as
SELECT statements. Queries that can't be hopped are canceled. For more information, see
[WLM query queue hopping](wlm-queue-hopping.md "wlm-queue-hopping.md").

WLM timeout doesn't apply to a query that has reached the returning state. To view
the state of a query, see the [STV_WLM_QUERY_STATE](r_STV_WLM_QUERY_STATE.md "r_STV_WLM_QUERY_STATE.md") system table. COPY statements and maintenance
operations, such as ALTER, ANALYZE and VACUUM, are not subject to WLM timeout.

The function of WLM timeout is similar to the [statement_timeout](r_statement_timeout.md "r_statement_timeout.md") configuration parameter. The difference is
that, where the `statement_timeout` configuration parameter applies to the
entire cluster, WLM timeout is specific to a single queue in the WLM configuration.

If [statement_timeout](r_statement_timeout.md "r_statement_timeout.md") is also
specified, the lower of statement_timeout and WLM timeout (max_execution_time) is used.

## Query monitoring rules

Query monitoring rules define metrics-based performance boundaries for WLM queues and
specify what action to take when a query goes beyond those boundaries. For example, for
a queue dedicated to short running queries, you might create a rule that cancels queries
that run for more than 60 seconds. To track poorly designed queries, you might have
another rule that logs queries that contain nested loops. For more information, see
[WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md "cm-c-wlm-query-monitoring-rules.md").
