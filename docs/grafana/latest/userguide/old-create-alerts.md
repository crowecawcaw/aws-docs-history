# Creating alerts

This documentation topic discusses
legacy alerting in Grafana. This will not be supported in future versions
of Amazon Managed Grafana. You can migrate to Grafana alerting to use the latest
alerting features. For more information, see one of the following
topics.

For Grafana workspaces that support Grafana version 10.x, see
[Alerts in Grafana version 10](v10-alerts.md "v10-alerts.md").

For Grafana workspaces that support Grafana version 9.x, see
[Alerts in Grafana version 9](v9-alerts.md "v9-alerts.md").

For Grafana workspaces that support Grafana version 8.x, see
[Grafana alerting](alerts-overview.md "alerts-overview.md").

When you use Amazon Managed Grafana alerting, you can attach rules to your dashboard panels. When
you save the dashboard, Amazon Managed Grafana extracts the alert rules into a separate alert rule
storage and schedules them for evaluation.

On the **Alert** tab of the graph panel, you can configure how often
the alert rule should be evaluated and the conditions that must be met for the alert to
change state and initiate its notifications.

Currently, only the graph panel supports alert rules.

## Adding or editing an alert

rule

1. Navigate to the panel where add or edit an alert rule, choose the title,
   and then choose **Edit**.
2. On the **Alert** tab, choose **Create
   Alert**. If an alert already exists for this panel, you can
   edit the fields on the **Alert** tab.
3. Fill out the fields. For more information, see [Alert rule fields](#old-alert-rule-fields "#old-alert-rule-fields").
4. When you have finished writing your rule, choose **Save** in the upper right corner to save the alert rule and
   the dashboard.
5. (Optional but recommended) To make sure that the rule returns the results
   you expect, choose **Test rule**.

## Deleting an alert rule

To delete an alert, scroll to the bottom of the alert, and then choose **Delete**.

## Alert rule fields

This section describes the fields that you fill out to create an alert.

### Rule

- **Name** – Enter a descriptive name.
  The name will be displayed in the **Alert Rules** list.
- **Evaluate every** – Specify how
  often the scheduler should evaluate the alert rule. This is referred to
  as the _evaluation interval_.
- **For** – Specify how long the query
  must violate the configured thresholds before the alert notification
  triggers.

###### Warning

Do not use `For` with the `If no data or all values are
 null` setting set to `No Data`. The triggering of
`No Data` will trigger instantly and not take
`For` into consideration. This can also result in an OK
notification not being sent if alert transitions from `No Data ->
 Pending -> OK`.

If an alert rule has a configured `For` and the query violates the
configured threshold, it will first go from `OK` to
`Pending`. Going from `OK` to `Pending`,
Amazon Managed Grafana does not send any notifications. When the alert rule has been firing
for more than the `For` duration, it will change to
`Alerting` and send alert notifications.

Typically, we recommend using this setting because it’s often worse to get
false positive than to wait a few minutes before the alert notification
initiates. Looking at the `Alert list` or `Alert list
 panels`, you will be able to see alerts that are in the pending state.

### Conditions

Currently, the only existing condition type is a `Query` condition
that allows you to specify a query letter, a time range, and an aggregation
function.

#### Query condition

example

```

avg() OF query(A, 15m, now) IS BELOW 14

```

- `avg()` Controls how the values for **each** series should be reduced to a value that can be
  compared against the threshold. Choose the function to change it to
  another aggregation function.
- `query(A, 15m, now)` The letter defines what query to run
  from the **Metrics** tab. The second
  two parameters define the time range: `15m, now` means 15
  minutes ago to now. You can also use `10m, now-2m` to
  define a time range that will be 10 minutes ago to 2 minutes ago.
  This is useful if you want to ignore the last 2 minutes of data.
- `IS BELOW 14` Defines the type of threshold and the
  threshold value. You can choose `IS BELOW` to change the
  type of threshold.

The query used in an alert rule cannot contain any template variables.
Currently, we support only `AND` and `OR` operators
between conditions, and they are run serially. For example, we have three
conditions in the following order: _condition:A(evaluates to: TRUE)
OR condition:B(evaluates to: FALSE) AND condition:C(evaluates to:
TRUE)_ so the result will be calculated as ((TRUE OR FALSE)
AND TRUE) = TRUE.

#### Multiple series

If a query returns multiple series, the aggregation function and
threshold check will be evaluated for each series. Currently, Amazon Managed Grafana does
not track the alert rule state **per series**.
The implications of this are detailed in the following scenario.

- An alert condition with query that returns two series: **server1** and **server2**.
- The **server1** series causes the
  alert rule to fire and switch to state `Alerting`.
- Notifications are sent out with message: _load peaking
  (server1)_
- In a subsequent evaluation of the same alert rule, the **server2** series also causes the alert rule
  to fire.
- No new notifications are sent because the alert rule is already
  in state `Alerting`.

As you can see from the previous scenario, if the rule already is in state
`Alerting`, Grafana doesn't send out notifications when other
series cause the alert to fire.

###### Note

You can configure reminders to be sent for triggered alerts. This
will send additional notifications when an alert continues to fire. If
other series (such as server2 in the previous example) also cause the
alert rule to fire, they are included in the reminder notification.
Depending on which notification channel you’re using, you might be able
to take advantage of this feature for identifying new or existing series
that are causing alerts to fire.

### No data and error handling

The following table contains conditions for controlling how the rule
evaluation engine handles queries that return no data or only null values.

| No Data Option          | Description                                        |
| ----------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No Data                 | Set alert rule state to `NoData`.                  |
| Alerting                | Set alert rule state to `Alerting`.                |
| Keep Last State         | Keep the current alert rule state, whatever it is. |
| Ok                      | Supported, but usually not useful.                 | ### Execution errors or timeouts The following options tell Amazon Managed Grafana how to handle execution or timeout errors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Error or timeout option | Description                                        |
| ---                     | ---                                                |
| Alerting                | Set alert rule state to `Alerting`.                |
| Keep Last State         | Keep the current alert rule state, whatever it is. | If you have an unreliable time series store from which queries sometimes time out or fail randomly, you can set this option to `Keep Last State` to basically ignore them. ## Notifications On **Alert** tab, you can also specify alert rule notifications and a detailed message about the alert rule. The message can contain anything: information about how you might solve the issue, link to runbook, and so on. The actual notifications are configured and shared between multiple alerts. For information on how to configure and set up notifications, see [Alert notifications](old-alert-notifications.md "old-alert-notifications.md"). <br>• **Send to** – Select an alert notification channel if you have one set up. <br>• **Message** – Enter a text message to be sent on the notification channel. Some alert notifiers support transforming the text to HTML or other rich formats. <br>• **Tags** – Specify a list of tags (key-value) to be included in the notification. It is supported by only some notifiers. ## Alert state history and annotations Alert state changes are recorded in the internal annotation table in the Amazon Managed Grafana database. The state changes are visualized as annotations in the graph panel of the alert rulel. You can also go into the `State history` submenu on the **Alert** tab to view and clear state history. |
