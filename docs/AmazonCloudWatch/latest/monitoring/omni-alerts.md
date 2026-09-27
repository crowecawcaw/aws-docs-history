

# Alerts
<a name="omni-alerts"></a>

An alert monitors your telemetry and notifies you when it crosses a threshold you set. You write a query to select what to monitor, set a condition that compares the query result against a threshold, and choose how often CloudWatch Omni evaluates it. When the condition is met, CloudWatch Omni sends a notification to the destinations you specify. Alerts read the same telemetry as the rest of CloudWatch Omni, so one alerting system covers both your applications and your AI agents: error rates and latency alongside evaluation scores and token usage.

**Note**  
Omni alerts are separate from CloudWatch alarms. Your existing CloudWatch alarms keep working unchanged, and you manage them in the CloudWatch console. See [CloudWatch Omni](cloudwatch-omni.md).

**Alert query**

An alert monitors the results of a query that you provide. You write the query in the same languages you use in CloudWatch Omni: SQL for logs and traces, and PromQL for metrics. You can alert on anything you can query in Explore. Start from a query you have already run there.

**Thresholds and alert states**

Each evaluation compares the query result against a threshold. You set a warning threshold, a critical threshold, or both. A single alert carries both tiers: a result that crosses the warning threshold puts the alert in the `WARNING` state, and a result that crosses the critical threshold escalates it to `CRITICAL`. At any moment an alert is in one of four states: `OK`, `WARNING`, `CRITICAL`, or `NODATA` (the last when the query returned nothing to evaluate). You choose how missing data is treated (as breaching at a state you set, or not), so a pipeline that stops sending data can itself raise the alert.

A threshold applies to either the values a query returns or the number of rows it returns. You choose which comparison the alert makes when you set the threshold.
+ **Field value** — the alert reads a column that you name from each row the query returns and compares that value against the threshold.
+ **Row count** — the alert compares the number of rows the query returned and reads no column. Use this to alert on how many items match a condition.

**Evaluation timing**

Three settings control when the alert changes state:
+ **Evaluation interval** — how often the query runs.
+ **Pending duration** — how long results must stay past the threshold before the alert fires, so a single spike does not notify anyone.
+ **Recovery duration** — how long results must stay clear before the alert returns to OK, so a flapping signal does not resolve and re-fire repeatedly.

**One alert, many series**

When the query returns one result per service, agent, or other grouping, the alert tracks each series as a **contributor** with its own state. The alert's state reflects its worst contributors, and its detail view shows which series are breaching. One alert monitors a whole fleet without a copy per service.

**Create an alert**

You can create an alert in three ways, depending on where you start:
+ **From Explore.** Run the query, then create the alert directly from it: the query you ran becomes the alert's query. See [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md).
+ **From the Alerts page.** Choose **Create alert**. A query editor opens in place: write and run the query, and the alert configuration form appears with a preview of your thresholds against recent data.
+ **Ask the Omni agent.** Describe what you want to be alerted on in plain language. The agent bases the threshold on your data, shows you the alert it intends to create, and creates it only after you confirm. See [Ask the Omni agent](omni-ask-the-omni-agent.md).

Then name the alert, set the thresholds and evaluation timing, and add destinations. Choose the name deliberately: an alert cannot be renamed later.

Every alert also carries an **access profile** (the identity it evaluates its query and sends notifications as), and Omni selects one for you by default. You can select a different profile for finer-grained control. If an alert reports no data from the moment you create it, rather than going quiet after working, check its profile before the query. See [Access profiles](omni-access-profiles.md).

Creating an alert requires permission to create alerts in the space and access to a profile that carries the grants below. Whichever profile the alert uses, it must carry these grants:
+ Grants that allow the alert and you, its creator, to assume the profile.
+ A grant that allows the query actions, `cloudwatch:StartTelemetryQuery` and `cloudwatch:GetTelemetryQueryResults`.
+ If the alert notifies a Slack channel, a grant that allows the Slack integration, scoped to that channel. See [Connect Slack](omni-connect-slack.md).

For how to author grants, see [Custom grant actions](omni-custom-grant-actions.md).

**Send notifications**

Notification rules route by state: send warning notifications to one destination and critical notifications to another, and notify on recovery to OK so the person who was notified knows the alert cleared. A destination is a Slack channel (connected through the Slack integration, see [Connect Slack](omni-connect-slack.md)) or an Amazon SNS topic.

Delivery to a Slack channel also requires that the Region's Amazon CloudWatch bot has been invited to that channel. For the invite command and the bot names by Region, see [Connect Slack](omni-connect-slack.md).

A new alert sends nothing until you add a notification rule, and you can disable an alert's notifications without deleting it. The alert keeps evaluating and showing state.

**Manage your alerts**

The **Alerts** page lists every alert in the space with its state and recent state changes. From the list you can open an alert's detail view (the query result charted with the thresholds drawn on it, the alert's state timeline, and its contributors), edit the alert, disable or re-enable its notifications, tag it, or delete it. Deleting cannot be undone.

Every state change, configuration change, and notification an alert sends is recorded as telemetry in your space and kept for 90 days. Query it with the same SQL you use for the rest of your telemetry (how often an alert fired last quarter, which contributors breach most often, whether a notification was delivered), and join it against your application telemetry in a single query. See [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md).

An alert evaluates against your space's CloudWatch Dataset, so it can fire on telemetry from a centralized source account. See [Set up Omni for your organization](omni-set-up-omni-for-your-organization.md).

**Investigate a firing alert**

Investigations are manual: an alert never starts one automatically when it fires. When your space is connected to the AWS DevOps Agent, you start the investigation yourself from a firing alert's **Investigate** action. The investigation is scoped to that alert and seeded with the alert's context: its state and what fired. See [Investigate with the AWS DevOps Agent](omni-investigate-with-the-aws-devops-agent.md).