Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Workload

management

You can configure Amazon Redshift WLM to run with either automatic WLM or manual WLM.

With Amazon Redshift, you can manage and prioritize concurrent queries and user workloads to optimize performance and resource
utilization. Workload management (WLM) allows you to define queues, user groups, and other constructs to control the
resources allocated to different types of queries or users.

The following sections outline the specific workload management features in Amazon Redshift, and guide you through their
configuration and monitoring.

**Automatic WLM**

To maximize system throughput and use resources effectively, you can enable Amazon Redshift to
manage how resources are divided to run concurrent queries with automatic WLM. _Automatic WLM_ manages the resources required to run queries.
Amazon Redshift determines how many queries run concurrently and how much memory is allocated to
each dispatched query. Use Auto WLM when you want Amazon Redshift to manage how resources are divided to run concurrent queries. For more information, see [Implementing automatic WLM](automatic-wlm.md "automatic-wlm.md").

Working with concurrency scaling and automatic WLM, you can support virtually
unlimited concurrent users and concurrent queries, with consistently fast query
performance. For more information, see [Concurrency scaling](concurrency-scaling.md "concurrency-scaling.md").

###### Note

In most cases we recommend that you use automatic WLM. If
you're using manual WLM and you want to migrate from to automatic WLM, see [Migrating from manual WLM to automatic
WLM](#wlm-manual-to-automatic "#wlm-manual-to-automatic").

With Auto WLM, it's possible to define query priorities for workloads in a queue. For more information about
query priority, see [Query priority](query-priority.md "query-priority.md").

**Manual WLM**

You might have multiple sessions or users running queries at the same time.
Some queries might consume cluster resources for long periods and
affect the performance of others. Manual WLM can help manage this for specialized use cases. Use Manual WLM when you want more control over concurrency.

You can manage system performance by
modifying your WLM configuration to create separate queues for long-running queries
and short-running queries. At runtime, you can route queries to these queues
according to user groups or query groups.

You can set up rules to route queries to particular
queues based on the user running the query or labels that you specify. You can also
configure the amount of memory allocated to each queue, so that large queries run in
queues with more memory than other queues. You can also configure a query monitoring
rule (QMR) to limit long-running queries.
For more information, see [Implementing manual WLM](cm-c-defining-query-queues.md "cm-c-defining-query-queues.md").

###### Note

We recommend configuring your manual WLM query queues with a total of 15 or fewer
query slots. For more information, see [Concurrency level](cm-c-defining-query-queues.md#cm-c-defining-query-queues-concurrency-level "cm-c-defining-query-queues.md#cm-c-defining-query-queues-concurrency-level").

Note that in regards to a manual WLM configuration, the maximum slots you can allocate to a queue is 50.
However, this doesn't mean that in an automatic WLM configuration, a Amazon Redshift cluster always runs 50 queries
concurrently. This can change, based on the memory needs or other types of resource allocation on the cluster.

###### Topics

- [Switching WLM mode](#cm-c-switching-mode "#cm-c-switching-mode")
- [Modifying the WLM configuration](#cm-c-modifying-wlm-configuration "#cm-c-modifying-wlm-configuration")
- [Implementing automatic WLM](automatic-wlm.md "automatic-wlm.md")
- [Implementing manual WLM](cm-c-defining-query-queues.md "cm-c-defining-query-queues.md")
- [Concurrency scaling](concurrency-scaling.md "concurrency-scaling.md")
- [Short query
  acceleration](wlm-short-query-acceleration.md "wlm-short-query-acceleration.md")
- [WLM queue assignment rules](cm-c-wlm-queue-assignment-rules.md "cm-c-wlm-queue-assignment-rules.md")
- [Assigning queries to queues](cm-c-executing-queries.md "cm-c-executing-queries.md")
- [WLM dynamic and static configuration
  properties](cm-c-wlm-dynamic-properties.md "cm-c-wlm-dynamic-properties.md")
- [WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md "cm-c-wlm-query-monitoring-rules.md")
- [WLM system tables and views](cm-c-wlm-system-tables-and-views.md "cm-c-wlm-system-tables-and-views.md")

## Switching WLM mode

You can enable automatic or manual WLM using the Amazon Redshift console:

1. Choose
   **Switch WLM mode**.
2. To set it to automatic WLM, choose **Auto WLM**. With this choice, up to eight queues are used to
   manage queries, and the **Memory** and **Concurrency on main** fields are both set
   to **Auto**. Additionally, the default priority of queries is set to **Normal**.
3. To enable manual configuration using
   the Amazon Redshift console, switching to **Manual WLM**. With this choice, you specify the queues used to manage queries, and
   the **Memory** and **Concurrency on main** field values. With a manual configuration,
   you can configure up to eight query queues and set the number of queries that can run in each of those queues concurrently.

## Modifying the WLM configuration

The easiest way to modify the WLM configuration is by using the Amazon Redshift console. You
can also use the AWS CLI or the Amazon Redshift API.

When you switch your cluster between automatic and manual WLM, your cluster is put into
`pending reboot` state. The change doesn't take effect until the next
cluster reboot.

For detailed information about modifying WLM configurations, see [Configuring Workload Management](../mgmt/workload-mgmt-config.md "../mgmt/workload-mgmt-config.md") in
the _Amazon Redshift Management Guide._

### Migrating from manual WLM to automatic

WLM

To maximize system throughput and use resources most effectively, we recommend that
you set up automatic WLM for your queues. Consider taking the following approach to set
up a smooth transition from manual WLM to automatic WLM.

To migrate from manual WLM to automatic WLM and use query priorities, we recommend
that you create a new parameter
group,
and then attach that parameter group to your cluster. For more information, see [Amazon Redshift Parameter Groups](../mgmt/working-with-parameter-groups.md "../mgmt/working-with-parameter-groups.md")
in the _Amazon Redshift Management Guide._

###### Important

To change the parameter group or to switch from manual to automatic WLM requires a
cluster reboot. For more information, see [WLM dynamic and static configuration
properties](cm-c-wlm-dynamic-properties.md "cm-c-wlm-dynamic-properties.md").

Let's take an example where there are three manual WLM queues. One each for an
ETL workload, an analytics workload, and a data science workload. The ETL workload runs
every 6 hours, the analytics workload runs throughout the day, and the data science
workload can spike at any time. With manual WLM, you specify the memory and concurrency
that each workload queue gets based on your understanding of the importance of each
workload to the business. Specifying the memory and concurrency is not
only
hard to figure out,
it also
results in cluster resources being statically partitioned and thereby wasted when only a
subset of the workloads is running.

You can use automatic WLM with query priorities to indicate the relative priorities
of the workloads, avoiding the preceding issues. For this example, follow these
steps:

- Create a new parameter group and switch to **Auto WLM** mode.
- Add queues for each of the three workloads: ETL workload, analytics workload, and data science
  workload. Use the same user groups for each workload that was used with **Manual WLM** mode.
- Set the priority for the ETL workload to `High`, the analytics workload to `Normal`, and the data science to `Low`.
  These priorities reflect your business priorities for the different workloads or user groups.
- Optionally, enable concurrency scaling for the analytics or data science queue so that queries
  in these queues get consistent performance even when the ETL workload is
  running
  every 6 hours.

With query priorities, when only the analytics workload is running on the cluster, it
gets the entire system to
itself.
This
yields
high throughput with
better
system utilization. However, when the ETL workload starts, it gets the right of the way
since it has a higher priority. Queries running as part of the ETL workload get priority
during
admission,
in addition to preferential resource allocation after they are admitted. As a
consequence, the ETL workload performs predictably regardless of what else might be
running on the system. The predictable performance for a high priority workload comes at
the cost of other, lower priority workloads that run longer either because their queries
are waiting behind more important queries to complete. Or, because they are getting a
smaller fraction of resources when they are running concurrently with higher priority
queries. The scheduling algorithms used by Amazon Redshift
facilitate
that the lower priority queries do not suffer from starvation, but rather continue to
make progress albeit at a slower pace.

###### Note

- The timeout field is not available in automatic WLM. Instead, use the QMR rule, `query_execution_time`. For more information, see
  [WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md "cm-c-wlm-query-monitoring-rules.md").
- The QMR action, HOP, is not applicable to automatic WLM. Instead, use the `change priority` action. For more information, see
  [WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md "cm-c-wlm-query-monitoring-rules.md").
- Clusters use automatic WLM and manual WLM queues differently, which can lead to confusion with your configurations. For example, you can configure the priority
  property in automatic WLM queues but not in manual WLM queues. As such, avoid mixing automatic WLM queues and manual WLM queues within a parameter group.
  Instead, create a new parameter group when migrating to automatic WLM.
