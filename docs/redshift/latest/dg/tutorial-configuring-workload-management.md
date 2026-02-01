Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Tutorial: Configuring manual

workload management (WLM) queues

With Amazon Redshift, you can configure manual workload management (WLM) queues to prioritize and allocate
resources for different types of queries and users. Manual WLM queues allow you to control the
memory and concurrency settings for specific queues, ensuring that critical workloads receive
the necessary resources while preventing low-priority queries from monopolizing the system.
The following sections guide you through the process of creating and configuring manual WLM queues
in Amazon Redshift to meet your workload management requirements.

## Overview

We recommend configuring automatic workload management (WLM)
in Amazon Redshift. For more information about automatic WLM, see
[Workload
management](cm-c-implementing-workload-management.md "cm-c-implementing-workload-management.md").
However, if you need multiple WLM queues,
this tutorial walks you through the process of configuring manual workload management (WLM)
in Amazon Redshift. By configuring manual WLM, you can improve query performance and resource
allocation in your cluster.

Amazon Redshift routes user queries to queues for processing. WLM defines how those queries
are routed to the queues. By default, Amazon Redshift has two queues available for queries: one
for superusers, and one for users. The superuser queue cannot be configured and can only
process one query at a time. You should reserve this queue for troubleshooting purposes
only. The user queue can process up to five queries at a time, but you can configure
this by changing the concurrency level of the queue if needed.

When you have several users running queries against the database, you might find
another configuration to be more efficient. For example, if some users run
resource-intensive operations, such as VACUUM, these might have a negative impact on
less-intensive queries, such as reports. You might consider adding additional queues and
configuring them for different workloads.

**Estimated time:** 75 minutes

**Estimated cost:** 50 cents

### Prerequisites

You need an Amazon Redshift cluster, the sample TICKIT database, and the Amazon Redshift RSQL client
tool. If you do not already have these set up, go to [Amazon Redshift Getting Started Guide](../gsg/new-user.md "../gsg/new-user.md") and [Amazon Redshift RSQL](../mgmt/rsql-query-tool.md "../mgmt/rsql-query-tool.md").

### Sections

- [Section 1: Understanding
  the default queue processing behavior](#tutorial-wlm-understanding-default-processing "#tutorial-wlm-understanding-default-processing")
- [Section 2: Modifying the WLM
  query queue configuration](#tutorial-wlm-modifying-wlm-configuration "#tutorial-wlm-modifying-wlm-configuration")
- [Section 3: Routing queries to
  queues based on user groups and query groups](#tutorial-wlm-routing-queries-to-queues "#tutorial-wlm-routing-queries-to-queues")
- [Section 4: Using wlm_query_slot_count to
  temporarily override the concurrency level in a queue](#tutorial-wlm-query-slot-count "#tutorial-wlm-query-slot-count")
- [Section 5: Cleaning up your
  resources](#tutorial-wlm-cleaning-up-resources "#tutorial-wlm-cleaning-up-resources")

## Section 1: Understanding

the default queue processing behavior

Before you start to configure manual WLM, it’s useful to understand the default behavior of
queue processing in Amazon Redshift. In this section, you create two database views that
return information from several system tables. Then you run some test queries to see
how queries are routed by default. For more information about system tables, see [System tables and views reference](cm_chap_system-tables.md "cm_chap_system-tables.md").

### Step 1: Create the

WLM_QUEUE_STATE_VW view

In this step, you create a view called WLM_QUEUE_STATE_VW. This view returns
information from the following system tables.

- [STV_WLM_CLASSIFICATION_CONFIG](r_STV_WLM_CLASSIFICATION_CONFIG.md "r_STV_WLM_CLASSIFICATION_CONFIG.md")
- [STV_WLM_SERVICE_CLASS_CONFIG](r_STV_WLM_SERVICE_CLASS_CONFIG.md "r_STV_WLM_SERVICE_CLASS_CONFIG.md")
- [STV_WLM_SERVICE_CLASS_STATE](r_STV_WLM_SERVICE_CLASS_STATE.md "r_STV_WLM_SERVICE_CLASS_STATE.md")

You use this view throughout the tutorial to monitor what happens to queues
after you change the WLM configuration. The following table describes the data that
the WLM_QUEUE_STATE_VW view returns.

| Column             | Description                                                                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| queue              | The number associated with the row that represents a queue. Queue<br>number determines the order of the queues in the database.            |
| description        | A value that describes whether the queue is available only to<br>certain user groups, to certain query groups, or all types of<br>queries. |
| slots              | The number of slots allocated to the queue.                                                                                                |
| mem                | The amount of memory, in MB per slot, allocated to the<br>queue.                                                                           |
| max_execution_time | The amount of time a query is allowed to run before it is<br>terminated.                                                                   |
| user\_\*           | A value that indicates whether wildcard characters are allowed in<br>the WLM configuration to match user groups.                           |
| query\_\*          | A value that indicates whether wildcard characters are allowed in<br>the WLM configuration to match query groups.                          |
| queued             | The number of queries that are waiting in the queue to be<br>processed.                                                                    |
| executing          | The number of queries that are currently running.                                                                                          |
| executed           | The number of queries that have been run.                                                                                                  |

#### To create the

WLM_QUEUE_STATE_VW view

1. Open [Amazon Redshift RSQL](../mgmt/rsql-query-tool.md "../mgmt/rsql-query-tool.md") and connect to your TICKIT sample database. If you do not
   have this database, see [Prerequisites](#tutorial-wlm-prereq "#tutorial-wlm-prereq").
2. Run the following query to create the WLM_QUEUE_STATE_VW view.

```
create view WLM_QUEUE_STATE_VW as
select (config.service_class-5) as queue
, trim (class.condition) as description
, config.num_query_tasks as slots
, config.query_working_mem as mem
, config.max_execution_time as max_time
, config.user_group_wild_card as "user_*"
, config.query_group_wild_card as "query_*"
, state.num_queued_queries queued
, state.num_executing_queries executing
, state.num_executed_queries executed
from
STV_WLM_CLASSIFICATION_CONFIG class,
STV_WLM_SERVICE_CLASS_CONFIG config,
STV_WLM_SERVICE_CLASS_STATE state
where
class.action_service_class = config.service_class
and class.action_service_class = state.service_class
and config.service_class > 4
order by config.service_class;
```

3. Run the following query to see the information that the view
   contains.

```
select * from wlm_queue_state_vw;
```

The following is an example result.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (querytype:any)                           |     5 | 836 |        0 |  false | false   |      0 |         1 |      160
```

### Step 2: Create the

WLM_QUERY_STATE_VW view

In this step, you create a view called WLM_QUERY_STATE_VW. This view returns
information from the [STV_WLM_QUERY_STATE](r_STV_WLM_QUERY_STATE.md "r_STV_WLM_QUERY_STATE.md") system table.

You use this view throughout the tutorial to monitor the queries that are
running. The following table describes the data that the WLM_QUERY_STATE_VW view
returns.

| Column     | Description                                                          |
| ---------- | -------------------------------------------------------------------- |
| query      | The query ID.                                                        |
| queue      | The queue number.                                                    |
| slot_count | The number of slots allocated to the query.                          |
| start_time | The time that the query started.                                     |
| state      | The state of the query, such as executing.                           |
| queue_time | The number of microseconds that the query has spent in the<br>queue. |
| exec_time  | The number of microseconds that the query has been<br>running.       |

#### To create the

WLM_QUERY_STATE_VW view

1. In RSQL, run the following query to create the WLM_QUERY_STATE_VW
   view.

```
create view WLM_QUERY_STATE_VW as
select query, (service_class-5) as queue, slot_count, trim(wlm_start_time) as start_time, trim(state) as state, trim(queue_time) as queue_time, trim(exec_time) as exec_time
from stv_wlm_query_state;
```

2. Run the following query to see the information that the view
   contains.

```
select * from wlm_query_state_vw;
```

The following is an example result.

```
query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 1249 |     1 |          1 | 2014-09-24 22:19:16 | Executing | 0          | 516
```

### Step 3: Run test queries

In this step, you run queries from multiple connections in RSQL and review the
system tables to determine how the queries were routed for processing.

For this step, you need two RSQL windows open:

- In RSQL window 1, you run queries that monitor the state of the queues and
  queries using the views you already created in this tutorial.
- In RSQL window 2, you run long-running queries to change the results you
  find in RSQL window 1.

#### To run the test queries

1. Open two RSQL windows. If you already have one window open, you only
   need to open a second window. You can use the same user account for both
   of these connections.
2. In RSQL window 1, run the following query.

```
select * from wlm_query_state_vw;
```

The following is an example result.

```
query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 1258 |     1 |          1 | 2014-09-24 22:21:03 | Executing | 0          | 549
```

This query returns a self-referential result. The query that is
currently running is the SELECT statement from this view. A query on
this view always returns at least one result. Compare this result with
the result that occurs after starting the long-running query in the next
step. 3. In RSQL window 2, run a query from the TICKIT sample database. This
query should run for approximately a minute so that you have time to
explore the results of the WLM_QUEUE_STATE_VW view and the
WLM_QUERY_STATE_VW view that you created earlier. In some cases, you
might find that the query doesn't run long enough for you to query both
views. In these cases, you can increase the value of the filter on
`l.listid` to make it run longer.

###### Note

To reduce query execution time and improve system performance,
Amazon Redshift caches the results of certain types of queries in memory on the
leader node. When result caching is enabled, subsequent queries run
much faster. To prevent the query from running to quickly, disable
result caching for the current session.

To turn off result caching for the current session, set the [enable_result_cache_for_session](r_enable_result_cache_for_session.md "r_enable_result_cache_for_session.md") parameter to
`off`, as shown following.

```
set enable_result_cache_for_session to off;
```

In RSQL window 2, run the following query.

```
select avg(l.priceperticket*s.qtysold) from listing l, sales s where l.listid < 100000;
```

4. In RSQL window 1, query WLM_QUEUE_STATE_VW and WLM_QUERY_STATE_VW and
   compare the results to your earlier results.

```
select * from wlm_queue_state_vw;
select * from wlm_query_state_vw;
```

The following are example results.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (querytype:any)                           |     5 | 836 |        0 |  false | false   |      0 |         2 |      163

query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 1267 |     1 |          1 | 2014-09-24 22:22:30 | Executing | 0          | 684
 1265 |     1 |          1 | 2014-09-24 22:22:36 | Executing | 0          | 4080859
```

Note the following differences between your previous queries and the results
in this step:

- There are two rows now in WLM_QUERY_STATE_VW. One result is the
  self-referential query for running a SELECT operation on this view. The
  second result is the long-running query from the previous step.
- The executing column in WLM_QUEUE_STATE_VW has increased from 1 to 2.
  This column entry means that there are two queries running in the
  queue.
- The executed column is incremented each time you run a query in the
  queue.

The WLM_QUEUE_STATE_VW view is useful for getting an overall view of the
queues and how many queries are being processed in each queue. The
WLM_QUERY_STATE_VW view is useful for getting a more detailed view of the
individual queries that are currently running.

## Section 2: Modifying the WLM

query queue configuration

Now that you understand how queues work by default, you can learn how to configure
query queues using manual WLM. In this section, you create and configure a new parameter
group for your cluster. You create two additional user queues and configure them to
accept queries based on the queries' user group or query group labels. Any queries
that don't get routed to one of these two queues are routed to the default queue at
runtime.

###### To create a manual WLM configuration in a parameter group

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Configurations**, then choose **Workload management** to display the
   **Workload management** page.
3. Choose **Create** to display the **Create parameter group** window.
4. Enter `WLMTutorial` for both **Parameter
   group name** and **Description**, and then
   choose **Create** to create the parameter group.

###### Note

The **Parameter group name** is converted to all lower case format when created. 5. On the **Workload management** page, choose the parameter group `wlmtutorial` to display the details page
with tabs for **Parameters** and **Workload management**. 6. Confirm that you're on the **Workload management** tab, then
choose **Switch WLM mode** to display the **Concurrency
settings** window. 7. Choose **Manual WLM**, then choose **Save** to switch to manual WLM. 8. Choose **Edit workload queues**. 9. Choose **Add queue** twice to add two queues. Now there are three queues:
**Queue 1**, **Queue 2**, and **Default queue**. 10. Enter information for each queue as follows:

    * For **Queue 1**, enter `30` for **Memory
     (%)**, `2` for **Concurrency on
     main**, and `test` for **Query
     groups**. Leave the other settings with their default
     values.
    * For **Queue 2**, enter `40` for **Memory
     (%)**, `3` for **Concurrency on
     main**, and `admin` for **User
     groups**. Leave the other settings with their default
     values.
    * Set the **Concurrency on
     main** value for the default queue to a value greater than or equal to 1.
     Don't make any other changes to the **Default queue**. WLM assigns unallocated memory to the default queue.

11. Choose **Save** to save your settings.

Next, associate the parameter group that has the manual WLM configuration with
a cluster.

###### To associate a parameter group with a manual WLM configuration with a

cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then
   choose **Clusters** to display a list of your clusters.
3. Choose your cluster, such as `examplecluster` to display the details of the cluster.
   Then choose the **Properties** tab to display the properties of that cluster.
4. In the **Database configurations** section, choose **Edit**,
   **Edit parameter group** to display the parameter groups window.
5. For **Parameter groups** choose
   the `wlmtutorial` parameter group that you previously created.
6. Choose **Save changes** to associate the parameter group.

The cluster is modified with the changed parameter group.
However, you need to reboot the cluster for the changes to also be applied to the database. 7. Choose your cluster, and then choose **Reboot** for **Actions**.

After the cluster is rebooted, its status returns to **Available**.

## Section 3: Routing queries to

queues based on user groups and query groups

Now you have your cluster associated with a new parameter group and you've
configured WLM. Next, run some queries to see how Amazon Redshift routes queries into queues
for processing.

### Step 1: View query queue

configuration in the database

First, verify that the database has the WLM configuration that you expect.

#### To view the query queue

configuration

1. Open RSQL and run the following query. The query uses the
   WLM_QUEUE_STATE_VW view you created in [Step 1: Create the
   WLM_QUEUE_STATE_VW view](#tutorial-wlm-create-queue-state-view "#tutorial-wlm-create-queue-state-view"). If you
   already had a session connected to the database prior to the cluster
   reboot, you need to reconnect.

```
select * from wlm_queue_state_vw;
```

The following is an example result.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (query group: test)                       |     2 | 627 |        0 |  false | false   |      0 |         0 |        0
    2 | (suser group: admin)                      |     3 | 557 |        0 |  false | false   |      0 |         0 |        0
    3 | (querytype:any)                           |     5 | 250 |        0 |  false | false   |      0 |         1 |        0
```

Compare these results to the results you received in [Step 1: Create the
WLM_QUEUE_STATE_VW view](#tutorial-wlm-create-queue-state-view "#tutorial-wlm-create-queue-state-view"). Notice that
there are now two additional queues. Queue 1 is now the queue for the
test query group, and queue 2 is the queue for the admin user
group.

Queue 3 is now the default queue. The last queue in the list is always
the default queue. That's the queue to which queries are routed by
default if no user group or query group is specified in a query. 2. Run the following query to confirm that your query now runs in queue 3.

```
select * from wlm_query_state_vw;
```

The following is an example result.

```
query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 2144 |     3 |          1 | 2014-09-24 23:49:59 | Executing | 0          | 550430
```

### Step 2: Run a query using the query group

queue

#### To run a query using the query group

queue

1. Run the following query to route it to the `test` query
   group.

```
set query_group to test;
select avg(l.priceperticket*s.qtysold) from listing l, sales s where l.listid <40000;
```

2. From the other RSQL window, run the following query.

```
select * from wlm_query_state_vw;
```

The following is an example result.

```
query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 2168 |     1 |          1 | 2014-09-24 23:54:18 | Executing | 0          | 6343309
 2170 |     3 |          1 | 2014-09-24 23:54:24 | Executing | 0          | 847
```

The query was routed to the test query group, which is queue 1
now. 3. Select all from the queue state view.

```
select * from wlm_queue_state_vw;
```

You see a result similar to the following.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (query group: test)                       |     2 | 627 |        0 |  false | false   |      0 |         1 |        0
    2 | (suser group: admin)                      |     3 | 557 |        0 |  false | false   |      0 |         0 |        0
    3 | (querytype:any)                           |     5 | 250 |        0 |  false | false   |      0 |         1 |        0
```

4. Now, reset the query group and run the long query again:

```
reset query_group;
select avg(l.priceperticket*s.qtysold) from listing l, sales s where l.listid <40000;
```

5. Run the queries against the views to see the results.

```
select * from wlm_queue_state_vw;
select * from wlm_query_state_vw;
```

The following are example results.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (query group: test)                       |     2 | 627 |        0 |  false | false   |      0 |         0 |        1
    2 | (suser group: admin)                      |     3 | 557 |        0 |  false | false   |      0 |         0 |        0
    3 | (querytype:any)                           |     5 | 250 |        0 |  false | false   |      0 |         2 |        5

query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 2186 |     3 |          1 | 2014-09-24 23:57:52 | Executing | 0          | 649
 2184 |     3 |          1 | 2014-09-24 23:57:48 | Executing | 0          | 4137349
```

The result should be that the query is now running in queue 3
again.

### Step 3: Create a database

user and group

Before you can run any
queries in this queue, you need to create the user group in the database and add a
user to the group. Then you log in with RSQL using the new user’s credentials and
run queries. You need to run queries as a superuser, such as the admin user, to
create database users.

#### To create a new database

user and user group

1. In the database, create a new database user named
   `adminwlm` by running the following command in an RSQL
   window.

```
create user adminwlm createuser password '123Admin';
```

2. Then, run the following commands to create the new user group and add
   your new `adminwlm` user to it.

```
create group admin;
alter group admin add user adminwlm;
```

### Step 4: Run a query using the user

group queue

Next you run a query and route it to the user group queue. You do this when you
want to route your query to a queue that is configured to handle the type of query
you want to run.

#### To run a query using the user

group queue

1. In RSQL window 2, run the following queries to switch to the
   `adminwlm` account and run a query as that user.

```
set session authorization 'adminwlm';
select avg(l.priceperticket*s.qtysold) from listing l, sales s where l.listid <40000;
```

2. In RSQL window 1, run the following query to see the query queue that
   the queries are routed to.

```
select * from wlm_query_state_vw;
select * from wlm_queue_state_vw;
```

The following are example results.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (query group: test)                       |     2 | 627 |        0 |  false | false   |      0 |         0 |        1
    2 | (suser group: admin)                      |     3 | 557 |        0 |  false | false   |      0 |         1 |        0
    3 | (querytype:any)                           |     5 | 250 |        0 |  false | false   |      0 |         1 |        8

query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 2202 |     2 |          1 | 2014-09-25 00:01:38 | Executing | 0          | 4885796
 2204 |     3 |          1 | 2014-09-25 00:01:43 | Executing | 0          | 650
```

The queue that this query ran in is queue 2, the `admin`
user queue. Anytime you run queries logged in as this user, they run in
queue 2 unless you specify a different query group to use.
The chosen queue depends on
the queue assignment rules. For more information, see [WLM queue assignment rules](cm-c-wlm-queue-assignment-rules.md "cm-c-wlm-queue-assignment-rules.md"). 3. Now run the following query from RSQL window 2.

```
set query_group to test;
select avg(l.priceperticket*s.qtysold) from listing l, sales s where l.listid <40000;
```

4. In RSQL window 1, run the following query to see the query queue that
   the queries are routed to.

```
select * from wlm_queue_state_vw;
select * from wlm_query_state_vw;
```

The following are example results.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (query group: test)                       |     2 | 627 |        0 |  false | false   |      0 |         1 |        1
    2 | (suser group: admin)                      |     3 | 557 |        0 |  false | false   |      0 |         0 |        1
    3 | (querytype:any)                           |     5 | 250 |        0 |  false | false   |      0 |         1 |       10

query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 2218 |     1 |          1 | 2014-09-25 00:04:30 | Executing | 0          | 4819666
 2220 |     3 |          1 | 2014-09-25 00:04:35 | Executing | 0          | 685
```

5. When you’re done, reset the query group.

```
reset query_group;
```

## Section 4: Using wlm_query_slot_count to

temporarily override the concurrency level in a queue

Sometimes, users might temporarily need more resources for a particular query. If so,
they can use the wlm_query_slot_count configuration setting to temporarily override the
way slots are allocated in a query queue. _Slots_ are units of memory
and CPU that are used to process queries. You might override the slot count when you
have occasional queries that take a lot of resources in the cluster, such as when you
perform a VACUUM operation in the database.

You might find that users often need to set wlm_query_slot_count for certain types of
queries. If so, consider adjusting the WLM configuration and giving users a queue that
better suits the needs of their queries. For more information about temporarily
overriding the concurrency level by using slot count, see [wlm_query_slot_count](r_wlm_query_slot_count.md "r_wlm_query_slot_count.md").

### Step 1: Override the concurrency

level using wlm_query_slot_count

For the purposes of this tutorial, we run the same long-running SELECT query.
We run it as the `adminwlm` user using wlm_query_slot_count to
increase the number of slots available for the query.

#### To override the concurrency

level using wlm_query_slot_count

1. Increase the limit on the query to make sure that you have enough time
   to query the WLM_QUERY_STATE_VW view and see a result.

```
set wlm_query_slot_count to 3;
select avg(l.priceperticket*s.qtysold) from listing l, sales s where l.listid <40000;
```

2. Now, query WLM_QUERY_STATE_VW with the admin user to see how
   the query is running.

```
select * from wlm_query_state_vw;
```

The following is an example result.

```
query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 2240 |     2 |          1 | 2014-09-25 00:08:45 | Executing | 0          | 3731414
 2242 |     3 |          1 | 2014-09-25 00:08:49 | Executing | 0          | 596
```

Notice that the slot count for the query is 3. This count means that
the query is using all three slots to process the query, allocating all
of the resources in the queue to that query. 3. Now, run the following query.

```
select * from WLM_QUEUE_STATE_VW;
```

The following is an example result.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (query group: test)                       |     2 | 627 |        0 |  false | false   |      0 |         0 |        4
    2 | (suser group: admin)                      |     3 | 557 |        0 |  false | false   |      0 |         1 |        3
    3 | (querytype:any)                           |     5 | 250 |        0 |  false | false   |      0 |         1 |       25
```

The wlm_query_slot_count configuration setting is valid for the
current session only. If that session expires, or another user runs a
query, the WLM configuration is used. 4. Reset the slot count and rerun the test.

```
reset wlm_query_slot_count;
select avg(l.priceperticket*s.qtysold) from listing l, sales s where l.listid <40000;
```

The following are example results.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (query group: test)                       |     2 | 627 |        0 |  false | false   |      0 |         0 |        2
    2 | (suser group: admin)                      |     3 | 557 |        0 |  false | false   |      0 |         1 |        2
    3 | (querytype:any)                           |     5 | 250 |        0 |  false | false   |      0 |         1 |       14

query | queue | slot_count | start_time          | state     | queue_time | exec_time
------+-------+------------+---------------------+-----------+------------+-----------
 2260 |     2 |          1 | 2014-09-25 00:12:11 | Executing | 0          | 4042618
 2262 |     3 |          1 | 2014-09-25 00:12:15 | Executing | 0          | 680
```

### Step 2: Run

queries from different sessions

Next, run queries from different sessions.

#### To run queries

from different sessions

1. In RSQL window 1 and 2, run the following to use the test query
   group.

```
set query_group to test;
```

2. In RSQL window 1, run the following long-running query.

```
select avg(l.priceperticket*s.qtysold) from listing l, sales s where l.listid <40000;
```

3. As the long-running query is still going in RSQL window 1, run the
   following. These commands increase the slot count to use all the slots
   for the queue and then start running the long-running query.

```
set wlm_query_slot_count to 2;
select avg(l.priceperticket*s.qtysold) from listing l, sales s where l.listid <40000;
```

4. Open a third RSQL window and query the views to see the
   results.

```
select * from wlm_queue_state_vw;
select * from wlm_query_state_vw;
```

The following are example results.

```
query | description                               | slots | mem | max_time | user_* | query_* | queued | executing | executed
------+-------------------------------------------+-------+-----+----------+--------+---------+--------+-----------+----------
    0 | (super user) and (query group: superuser) |     1 | 357 |        0 |  false | false   |      0 |         0 |        0
    1 | (query group: test)                       |     2 | 627 |        0 |  false | false   |      1 |         1 |        2
    2 | (suser group: admin)                      |     3 | 557 |        0 |  false | false   |      0 |         0 |        3
    3 | (querytype:any)                           |     5 | 250 |        0 |  false | false   |      0 |         1 |       18

query | queue | slot_count | start_time          | state         | queue_time | exec_time
------+-------+------------+---------------------+---------------+------------+-----------
 2286 |     1 |          2 | 2014-09-25 00:16:48 | QueuedWaiting | 3758950    | 0
 2282 |     1 |          1 | 2014-09-25 00:16:33 | Executing     | 0          | 19335850
 2288 |     3 |          1 | 2014-09-25 00:16:52 | Executing     | 0          | 666
```

Notice that the first query is using one of the slots allocated to
queue 1 to run the query. In addition, notice that there is one query
that is waiting in the queue (where `queued` is
`1` and `state` is
`QueuedWaiting`). After the first query completes, the second
one begins running. This execution happens because both queries are
routed to the `test` query group, and the second query must
wait for enough slots to begin processing.

## Section 5: Cleaning up your

resources

Your cluster continues to accrue charges as long as it is running. When you have
completed this tutorial, return your environment to the previous state by following the
steps in [Find Additional Resources
and Reset Your Environment](../gsg/rs-gsg-clean-up-tasks.md "../gsg/rs-gsg-clean-up-tasks.md") in _Amazon Redshift Getting Started Guide_.

For more information about WLM, see [Workload
management](cm-c-implementing-workload-management.md "cm-c-implementing-workload-management.md").
