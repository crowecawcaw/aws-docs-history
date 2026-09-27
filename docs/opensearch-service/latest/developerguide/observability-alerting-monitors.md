

# Classic alerting with monitors
<a name="observability-alerting-monitors"></a>

Monitors are the original alerting mechanism for Amazon OpenSearch Service. A monitor is a job that runs on a defined schedule. It queries your data using OpenSearch DSL, PPL, or Painless scripts, and evaluates trigger conditions that generate alerts. When a trigger condition is met, the monitor runs actions that send notifications through configured channels.

You access monitors from the **Alerts** page in the Observability workspace. To find it, expand **More** in the left navigation and choose **Alerts**.

Monitors support advanced alerting patterns, including per-document matching, composite monitor workflows, per-cluster-metrics health checks, and Painless scripting for complex trigger logic.

For information about notification channels and actions, see [Notifications](observability-alerting-notifications.md).

**Note**  
Before you create monitors, configure the required permissions and data source access. For more information, see [Configuring alerting permissions](observability-alerting-permissions.md).

## Supported data sources
<a name="observability-alerting-monitors-data-sources"></a>

Select the data source that the monitor runs against. Each data source has its own setup steps, permission model, and considerations. Configure your data source before you create monitors. The following table lists the supported data sources and where to find their configuration steps.


| Data source | Configuration | 
| --- | --- | 
| Amazon OpenSearch Serverless collections | See [Configuring alerting for Amazon OpenSearch Serverless](serverless-configure-alerting.md). | 
| Amazon OpenSearch Service domains | See [Configuring alerts in Amazon OpenSearch Service](alerting.md). | 

**Note**  
Monitor type availability, index selection, and trigger limits depend on your data source.

The following table summarizes which monitor types are supported by data source.


| Monitor type | Amazon OpenSearch Service domains | Amazon OpenSearch Serverless | 
| --- | --- | --- | 
| Per-query | Yes | Yes | 
| Per-bucket | Yes | Yes (one trigger) | 
| PPL | Yes | Yes | 
| Per-document | Yes | No | 
| Per cluster metrics | Yes | No | 
| Composite | Yes | No | 

## Creating a monitor
<a name="observability-alerting-monitors-create"></a>

In the Observability workspace, expand **More** in the left navigation, choose **Alerts**, and then choose **Create monitor**. To create a monitor:

1. Select the data source and the index to monitor.

1. Enter a name and choose a monitor type. The type determines how you define the query and how triggers are evaluated, as described in the following sections.

1. Define the query or condition for the monitor.

1. Set the schedule and the look-back window. For more information, see [Schedules and the look-back window](#observability-alerting-monitors-schedule).

1. Add one or more triggers and actions. For more information, see [Triggers](#observability-alerting-monitors-triggers).

![The Create monitor page with the monitor name field, the Per query, Per bucket, and PPL monitor type options, and a schedule.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/alerting/create-monitor-type.png)


### Per-query monitors
<a name="observability-alerting-monitors-per-query"></a>

Per-query monitors run a query against your data source and evaluate the trigger conditions against the query results. A per-query monitor triggers one alert at a time. You define the query with the **Visual editor** or the **Extraction query editor**. For example, you might alert when the number of HTTP 5xx responses in the last 5 minutes exceeds a threshold. For more information, see [Per query and per bucket monitors](https://docs.opensearch.org/latest/observing-your-data/alerting/per-query-bucket-monitors/) on the OpenSearch website.

### Per-bucket monitors
<a name="observability-alerting-monitors-per-bucket"></a>

Per-bucket monitors run a query against your data source and evaluate trigger conditions against buckets of results (for example, grouped by hostname or status code). Each bucket that meets a condition generates its own alert. You define the query with the **Visual editor** or the **Extraction query editor**, and you specify at least one field to group by. For example, group by `host` and alert on each host whose error count exceeds a threshold. For more information, see [Per query and per bucket monitors](https://docs.opensearch.org/latest/observing-your-data/alerting/per-query-bucket-monitors/) on the OpenSearch website.

### PPL monitors
<a name="observability-alerting-monitors-ppl"></a>

PPL monitors define the monitor condition with a Piped Processing Language (PPL) query. For example:

```
source=application_logs | where status_code = 503 | stats count() by host
```

**Note**  
PPL command and function support depends on the engine that backs your data source. For PPL syntax, see [PPL](https://docs.opensearch.org/latest/sql-and-ppl/ppl/index/) on the OpenSearch website.

### Per-document monitors
<a name="observability-alerting-monitors-per-document"></a>

Per-document monitors run one or more queries that return the individual documents that match, and they can combine queries by using tags. They alert on the matching documents (findings) rather than on an aggregate, which is useful when you need the specific records that met the condition. For more information, see [Per document monitors](https://docs.opensearch.org/latest/observing-your-data/alerting/per-document-monitors/) on the OpenSearch website.

**Note**  
Per-document monitors aren't supported on Amazon OpenSearch Serverless.

### Per cluster metrics monitors
<a name="observability-alerting-monitors-cluster-metrics"></a>

Per cluster metrics monitors (also called cluster health monitors) run cluster and node API requests on a schedule and evaluate trigger conditions against the results. These requests include cluster health, cluster statistics, and node statistics. Use them to alert on the health of a domain. For more information, see [Per cluster metrics monitors](https://docs.opensearch.org/latest/observing-your-data/alerting/per-cluster-metrics-monitors/) on the OpenSearch website.

**Note**  
Because they call cluster and node APIs, per cluster metrics monitors apply to Amazon OpenSearch Service domains and aren't supported on Amazon OpenSearch Serverless.

### Composite monitors
<a name="observability-alerting-monitors-composite"></a>

Composite monitors chain multiple monitors together in a workflow and generate alerts based on the combined trigger conditions of the underlying monitors. For example, they can notify only when two related monitors both enter an alert state. For more information, see [Composite monitors](https://docs.opensearch.org/latest/observing-your-data/alerting/composite-monitors/) on the OpenSearch website.

**Note**  
Composite monitors aren't supported on Amazon OpenSearch Serverless.

### Schedules and the look-back window
<a name="observability-alerting-monitors-schedule"></a>

In the **Schedule** section, set how often the monitor runs: choose **By interval** (for example, every 5 minutes) or define a custom schedule with a cron expression. The look-back window (**Time range for the last**) sets the time range that each run evaluates, such as the last hour, so that each run covers a consistent slice of your data.

### Previewing a monitor
<a name="observability-alerting-monitors-preview"></a>

Before you save a monitor, you can preview it against recent data to validate the query and tune trigger thresholds. The preview shows a graph of the query results over time and how each trigger would evaluate, so you can adjust the conditions before the monitor runs on its schedule.

## Triggers
<a name="observability-alerting-monitors-triggers"></a>

Triggers define the conditions that generate alerts. A monitor can have more than one trigger, and each trigger generates its own alerts and runs its own actions. Available trigger configuration depends on the monitor type.


| Monitor type | Trigger condition | Example | 
| --- | --- | --- | 
| Per-query | Threshold on the query result (count or metric), evaluated once per execution. | count > 5 over the last hour | 
| Per-bucket | Condition evaluated per bucket. Each matching bucket generates a separate alert. | count > 100 for any host bucket | 
| PPL | Condition on the PPL result set. | rows > 0 | 

Each trigger has a name, a severity level from 1 (highest) to 5 (lowest), and a condition. In the **Visual editor**, you set the condition as a threshold by using an operator such as `IS ABOVE`, `IS BELOW`, or `IS EXACTLY`. You can also define the condition as a Painless script in the **Extraction query editor**. If a trigger condition isn't met on a run, the monitor doesn't generate an alert for that trigger.

PPL monitors use a result-count condition (for example, the number of returned rows is above a value) instead of a script, so their triggers are simpler to author than script-based triggers. For trigger condition examples and Painless script samples, see [Triggers](https://docs.opensearch.org/latest/observing-your-data/alerting/triggers/) on the OpenSearch website.

![A trigger configuration showing the trigger name, severity level 1 (Highest), and the condition IS ABOVE 10000.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/alerting/trigger.png)


## Notifications and actions
<a name="observability-alerting-monitors-notifications"></a>

To send notifications when a trigger condition is met, add one or more actions to the trigger. Each action sends to a notification channel, such as an Amazon SNS channel, Slack, Microsoft Teams, email, or a custom webhook. For information about creating channels and configuring actions, see [Notifications](observability-alerting-notifications.md).

## Managing monitors
<a name="observability-alerting-monitors-manage"></a>

From the **Monitors** list, you can search and filter your monitors and open a monitor to see its details, execution history, and current alerts. From the list or the details page, you can:
+ Edit a monitor's query, schedule, triggers, or actions.
+ Enable or disable a monitor to pause and resume its runs without deleting it.
+ Delete a monitor.

![The Monitors list showing monitor name, state, type, schedule, and last updated time, with filters and a Create button.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/alerting/monitors-list.png)


## Viewing and acknowledging alerts
<a name="observability-alerting-monitors-view"></a>

When a trigger condition is met, the monitor generates an *alert*. You can review alerts from your monitors in OpenSearch UI.

Each alert has a state that reflects where it is in its lifecycle:
+ **Active** – The trigger condition is currently met. The alert stays active across runs until the condition clears or you acknowledge it.
+ **Acknowledged** – Someone has taken ownership of the alert. Acknowledging stops the trigger's actions from notifying again for that alert while the condition persists.
+ **Completed** – The trigger condition is no longer met, so the alert resolved on its own.
+ **Error** – The monitor ran but couldn't evaluate the trigger (for example, a query or permissions error). In this case, investigate the monitor rather than your data.

To review alerts, open the **Alerts** view, where you can search and filter by monitor, severity, and state. Choose an alert to open its details, including the trigger that fired, the severity, the state, the time the alert started, and a link to the monitor.

![The Alerts list showing per-trigger alert counts, trigger and monitor details, with filters and acknowledge controls.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/alerting/alerts-list.png)


![Alert details showing the trigger name, severity, trigger start and last-updated times, and a link to the monitor.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/alerting/alert-details.png)


To acknowledge alerts, select one or more active alerts and choose **Acknowledge**. Acknowledging records that the alert is being handled and prevents repeat notifications for it while the condition remains active. You can acknowledge alerts individually or in bulk.

![The Alerts panel with several active alerts selected by using the row checkboxes and the Acknowledge button available.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/alerting/acknowledge-alerts.png)


**Note**  
While a trigger condition stays true across runs, the monitor keeps the existing active alert instead of creating a new one on each run.