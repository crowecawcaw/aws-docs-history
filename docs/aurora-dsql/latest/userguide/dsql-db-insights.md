# Monitoring Aurora DSQL clusters with Aurora DSQL Database Insights

Aurora DSQL database insights provides access to per-second sampled data for every
active session on your cluster, collected by **DSQL Active Session
History (DASH)** sampler which records the wait state and normalized SQL statement
each session is running. Per-minute aggregated results from DASH are published as CloudWatch OpenTelemetry
(OTel) metrics. Use this data to understand your database load, find the queries that consume
the most resources, and diagnose performance issues.

You don't need to set up DASH. It is automatically enabled for every Aurora DSQL cluster, and per-minute
aggreated data is available through Amazon CloudWatch Database Insights and through Prometheus Query Language (PromQL)
queries run against CloudWatch OTel metrics at no additional cost.

###### Topics

- [What is DASH?](#dash-what-is "#dash-what-is")
- [DASH metrics and wait events](#dash-metrics-wait-events "#dash-metrics-wait-events")
- [Accessing DASH data](#dash-accessing-data "#dash-accessing-data")
- [Related resources](#dash-related-resources "#dash-related-resources")

## What is DASH?

An active session represents a single connection to your cluster that has an open
transaction. At any given moment, each active session is in one of three states:

- Using CPU
- Waiting for an external operation to complete, such as a storage read or a commit
  acknowledgment
- Idle in transaction, waiting for the next statement from your application in an open
  transaction

DASH tracks only sessions that have an open transaction. DASH captures this
activity by sampling all active sessions on your cluster once per second. Each sample records
two things:

- **The wait event** – the state the session was in at
  the moment of sampling. See [DASH wait events](#dash-wait-events "#dash-wait-events")
  for the full list.
- **The SQL statement** – the first 256 characters of
  the SQL the session was running, which is enough to identify most queries.

DASH aggregates these per-second samples and publishes them to CloudWatch once per minute,
broken down by wait event and by SQL statement. The result is a single time-series metric,
`db.active_sessions.avg`, that records the average number of active sessions over
each sample period. This value is also known as **Average Active Sessions
(AAS)**.

AAS is the foundational signal for Aurora DSQL performance analysis. The wait-event breakdown
shows what your sessions spend time on, not only how busy the cluster is. The SQL breakdown
attributes load to individual queries.

###### Tip

Aurora DSQL scales CPU elastically, so the most useful diagnostic signal is the shape of the
wait profile (the proportional distribution of session time across wait events) rather than
AAS against a fixed vCPU ceiling. Compare that shape against the baseline you observe during
normal operation. A change in those proportions indicates a shift in workload or system
behavior.

## DASH metrics and wait events

DASH exposes a single metric whose dimensions let you slice database load by wait event
and by SQL statement. The following table describes the DASH metric.

| Metric                   | Unit  | Description                                                                                                                                                  |
| ------------------------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `db.active_sessions.avg` | Count | The average number of active sessions on the cluster over the sample period (AAS).<br>Each active session is either running on CPU or in a named wait state. |

The metric carries the following dimensions (labels), which you use to group and filter
the data.

| Dimension                         | Description                                                                                                                                                                                                                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `db.wait.class`                   | The broader classification of wait events to identify the general type of resource<br>contributing to the database load. For example, `class:oncpu` means the<br>statement is actively running on the CPU, and `class:io` means that the<br>statement is waiting for an input/output operation to complete. |
| `db.wait.event`                   | The wait state the sampled sessions were in. See [DASH wait events](#dash-wait-events "#dash-wait-events") for the full list of values.                                                                                                                                                                     |
| `db.session.state`                | The session state – `active` (executing a statement) or `idle in<br>transaction` (waiting for the next command from the application while the<br>transaction remains open).                                                                                                                                 |
| `db.query.id`                     | The fingerprint of the normalized SQL text of the statement the sessions were<br>running.                                                                                                                                                                                                                   |
| `db.query.normalized_text`        | The normalized SQL text of the statement the sessions were running. DASH removes literal<br>values so that it groups statements that differ only in their parameters.                                                                                                                                       |
| `aws.auroradsql.session.role.arn` | The IAM role ARN assumed to connect to the Aurora DSQL cluster.                                                                                                                                                                                                                                             |
| `application.name`                | The application name that you set in connection parameters. You can override it at connect time.<br>DASH includes this dimension only when you explicitly set it.                                                                                                                                           |

### DASH wait events

Aurora DSQL sessions can experience the following wait events. The storage-related wait
events – `SequentialScanRead`, `ScatteredBatchRead`,
`SingleRead`, `UniqueConstraintCheck`, and
`FkExistenceCheck` – represent communication between the query processing
layer and the storage layer, and `Commit` represents communication with the
commit service. This list might expand over time as Aurora DSQL identifies new wait events.

| Wait event              | Wait class      | Description                                                                                                                                                                                                                                                                                      |
| ----------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `OnCpu`                 | `class:oncpu`   | The session isn't waiting for external input and is actively executing on CPU –<br>parsing, planning, evaluating expressions, or processing results.                                                                                                                                             |
| `ClientRead`            | `class:client`  | The session is idle within an open transaction, waiting for the application to send<br>the next SQL statement or a commit/rollback command. Frequent or long<br>`ClientRead` waits often indicate excessive application round-trips or<br>transactions that you hold open longer than necessary. |
| `ClientWrite`           | `class:client`  | The database sends results to the application over the network. High<br>`ClientWrite` can indicate large result sets or network latency between the<br>application and the database.                                                                                                             |
| `SequentialScanRead`    | `class:io`      | The session is reading a contiguous range of keys from storage. This isn't<br>necessarily a full table scan – it might cover a relatively small range of<br>contiguous keys.                                                                                                                     |
| `ScatteredBatchRead`    | `class:io`      | The session is performing batched reads from storage, retrieving multiple<br>non-contiguous keys in a single call to storage.                                                                                                                                                                    |
| `SingleRead`            | `class:io`      | The session is reading a single tuple (point lookup) from storage.<br>`ScatteredBatchRead` with a batch size of 1 largely replaces this event, which<br>is uncommon in current Aurora DSQL versions.                                                                                             |
| `UniqueConstraintCheck` | `class:io`      | The session is validating unique key constraints, which requires storage reads to<br>check for duplicates. This applies to both unique constraints on non-primary-key columns<br>and primary key constraints during the insertion of new rows.                                                   |
| `FkExistenceCheck`      | `class:io`      | The session is validating that a referenced foreign key row exists, which requires<br>reads to confirm the relationship.                                                                                                                                                                         |
| `StartTransaction`      | `class:io`      | The session is preparing for the distributed transaction to begin.                                                                                                                                                                                                                               |
| `Commit`                | `class:io`      | The session has initiated a commit and is waiting for acknowledgment from the commit<br>service. The response is either a success or an abort (serialization error); a<br>`Commit` wait precedes both outcomes.                                                                                  |
| `PgSleep`               | `class:timeout` | The session is sleeping because the application explicitly called<br>`pg_sleep()`. This is an application-initiated wait, not a database-imposed<br>one.                                                                                                                                         |

## Accessing DASH data

You can access DASH data in three ways:

- **Amazon CloudWatch Database Insights** – A curated, no-code
  user interface (UI) for exploring database load and top SQL. This is the starting point for
  most investigations.
- **PromQL** – Query the underlying
  `db.active_sessions.avg` metric programmatically for integration with
  third-party monitoring tools or for interactive exploration.
- **Aurora DSQL system diagnostics AI skill** – An artificial
  intelligence (AI)-powered health-check agent that automatically analyzes DASH data, compares
  wait event distributions across time frames, and generates diagnostic reports.

All of these access paths read from the same DASH dataset.

### Using CloudWatch Database Insights

Amazon CloudWatch Database Insights presents DASH data through a Aurora DSQL-specific curated
dashboard. Your Aurora DSQL clusters appear automatically in Database Insights – you don't
need any setup beyond creating the cluster and running transactions on it.

#### To view DASH data in Database Insights

1. Open the CloudWatch console and choose **Database Insights** in the left
   navigation pane.
2. In the **Fleet Health** view, locate your Aurora DSQL cluster in the list
   of **Database resources**. Alternatively, you can navigate directly to the
   **Database Instance** page and select your cluster from the left
   panel.
3. Choose the **DB Identifier** to open the **Database Instance
   Dashboard**.
4. Use the **DB Load** chart to view Average Active Sessions over time.
   The chart is a stacked visualization in which each colored band represents one wait event,
   so the total height shows how busy the cluster is and the bands show what sessions are
   spending their time on.
5. Use the **Slice By** control on the **DB Load** chart
   to toggle between **Wait Events** and **SQL Text**.
6. The **DB Load Analysis** section shows AAS by **Top Wait
   Events** and **Top SQL** ranked by their contribution to
   AAS.
7. Use the time range picker at the top of the page to focus on a specific monitoring
   window, such as the period of a reported slowdown.

### Using PromQL

DASH exposes data as the CloudWatch metric `db.active_sessions.avg`, which you
can query with PromQL in CloudWatch Query Studio.

The following examples work in Query Studio, where the active workspace already
scopes results to your account and Region, and the time picker drives the evaluation window.
Because the metric name contains dots, the examples use the PromQL quoted-name selector
form, `{"db.active_sessions.avg"}`.

###### Note

All examples include an `@resource.aws.auroradsql.cluster_id` label filter
to scope results to a single cluster. Replace `cluster-id` with
your cluster identifier. If you have only one cluster, you can omit this filter or use the
Query Studio UI filters instead. To discover all of the labels available on the metric in
your environment, run `{"db.active_sessions.avg"}` as a series query and inspect
the label set on each returned series.

###### Database load by wait event

Returns the average number of active sessions grouped by wait event – the same
AAS-by-wait-event view available in the Database Insights DB Load chart, but accessible
programmatically.

```
avg by ("db.wait.event") (
  {
    "db.active_sessions.avg",
    "@resource.aws.auroradsql.cluster_id"="`cluster-id`"
  }
)
```

The result has one series per distinct `db.wait.event` value, each carrying
the average AAS contribution of that wait state.

###### Top SQL by average active sessions

Ranks SQL statements by their average contribution to database load. This is the
PromQL equivalent of the Database Insights **Top SQL** view.

```
topk(5,
  avg by ("db.query.normalized_text") (
    {
      "db.active_sessions.avg",
      "@resource.aws.auroradsql.cluster_id"="`cluster-id`"
    }
  )
)
```

To see the top SQL statement and wait event combinations by their contribution to load,
add `db.wait.event` to the grouping clause. Because this ranks every
combination together, the results can include several wait events for the same
high-contributing statement:

```
topk(5,
  avg by ("db.query.normalized_text", "db.wait.event") (
    {
      "db.active_sessions.avg",
      "@resource.aws.auroradsql.cluster_id"="`cluster-id`"
    }
  )
)
```

###### SQL statements performing the most storage reads

Returns the top five SQL statements spending the most time on storage read operations, by
filtering to the storage-read wait events.

```
topk(5,
  sum by ("db.query.normalized_text") (
    {
      "db.active_sessions.avg",
      "db.wait.event"=~"S.*Read|.*Check",
      "@resource.aws.auroradsql.cluster_id"="`cluster-id`"
    }
  )
)
```

The regular expression `S.*Read` matches the storage-read events whose names
start with `S` and end with `Read` (`SequentialScanRead`,
`ScatteredBatchRead`, `SingleRead`). The pattern includes
`.*Check` explicitly because the `UniqueConstraintCheck` and
`FkExistenceCheck` wait events don't match the first pattern but are also
storage-read wait events.

### Using the Aurora DSQL system diagnostics AI skill

The Aurora DSQL system diagnostics AI skill automates health-check analysis of your Aurora DSQL
cluster by reading DASH data, comparing wait event distributions across time frames, and
generating a diagnostic report. The skill is part of the [databases-on-aws](https://github.com/awslabs/agent-plugins/tree/main/plugins/databases-on-aws "https://github.com/awslabs/agent-plugins/tree/main/plugins/databases-on-aws") plugin in Agent Plugins for AWS in the [awslabs/agent-plugins](https://github.com/awslabs/agent-plugins "https://github.com/awslabs/agent-plugins") repository and
works with any supported AI coding agent.

To analyze cluster health, issue a prompt such as:

_"Check the performance of my Aurora DSQL cluster
`cluster-id` in us-east-1 and write me a markdown
report."_

The skill uses the CloudWatch Model Context Protocol (MCP) server to analyze the
`db.active_sessions.avg` metric across a selection of time frames and returns a
Markdown report. You can direct this performance comparison window in the prompt:

_"Check performance for the last 4 hours and compare against last
Monday."_

When specific queries look problematic, the skill initiates a deeper SQL-focused
diagnostics workflow and reports potential solutions for that statement. It decides whether
to drill into a query based on the wait event shift it detects, so you don't need additional
prompting.

## Related resources

- [Query metrics with PromQL](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.md") – overview of PromQL support in CloudWatch.
- [Running PromQL
  queries in Query Studio](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-QueryStudio.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-QueryStudio.md") – the interactive query workbench in the CloudWatch
  console.
- [AWS vended metrics in
  OpenTelemetry format](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-OTelEnrichment.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-OTelEnrichment.md") – how AWS service metrics, including those for Aurora DSQL,
  are exposed as PromQL-queryable time series.
- [Amazon CloudWatch Database Insights](../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md "../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md") – the CloudWatch UI for monitoring database load and
  performance.
- [Agent Plugins for AWS](https://github.com/awslabs/agent-plugins "https://github.com/awslabs/agent-plugins") on
  the GitHub website – source repository for the
  `databases-on-aws` plugin containing the Aurora DSQL system diagnostics AI skill.
