# View the state and health of

alert rules

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The state and health of alert rules gives you several key status indicators
about your alerts.

There are three components:

- [Alert rule state](#v10-alerting-manage-rulestate-state "#v10-alerting-manage-rulestate-state")
- [Alert instance state](#v10-alerting-manage-rulestate-instance "#v10-alerting-manage-rulestate-instance")
- [Alert rule health](#v10-alerting-manage-rulestate-health "#v10-alerting-manage-rulestate-health")
  Although related, each component conveys subtly different information.

###### To view the state and health of your alert rules

1. From your Grafana console, in the Grafana menu, choose
   **Alerting**.
2. Choose **Alert rules** to view the list of existing
   alerts.
3. Choose an alert rule to view its state and health.

## Alert rule state

An alert rule can be in any of the following states:

| State                  | Description                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Normal**             | None of the time series returned by the evaluation engine is in a `pending` or `firing` state.            |
| **Pending**            | At least one time series returned by the evaluation engine is `pending`.                                  |
| **Firing**             | At least one time series returned by the evaluation engine is `firing`.                                   | ###### Note Alerts transition first to `pending` and then `firing`, thus it takes at least two evaluation cycles before an alert is fired. ## Alert instance state An alert instance can be in any of the following states:                                                                                                                                                                                                       |
| State                  | Description                                                                                               |
| ---                    | ---                                                                                                       |
| **Normal**             | The state of an alert that is neither `pending` nor `firing`. Everything is working as expected.          |
| **Pending**            | The state of an alert that has been active for less than the configured threshold duration.               |
| **Alerting**           | The state of an alert that has been active for longer than the configured threshold duration.             |
| **No data**            | No data has been received for the configured time window.                                                 |
| **Alerting**           | An error occurred when attempting to evaluate an alerting rule.                                           | ## Keep last state An alert rule can be configured to keep the last state when a `NoData` or `Error` state is encountered. This will both prevent alerts from firing, and from resolving and re-firing. Just like normal evaluation, the alert rule will transition from `pending` to `firing` after the pending period has elapsed. ## Alert rule health An alert rule can have one of the following health statuses.            |
| State                  | Description                                                                                               |
| ---                    | ---                                                                                                       |
| **Ok**                 | No errors when evaluating the alert rule.                                                                 |
| **Error**              | An error occurred when evaluating the alert rule.                                                         |
| **NoData**             | The absence of data in at least one time series returned during a rule evaluation.                        |
| **{status}, KeepLast** | The rule would have received another status, but was configured to keep the last state of the alert rule. | ## Special alerts for NoData and Error When evaluation of an alert rule produces the state `NoData` or `Error`, Grafana alerting will generate alert instances that have the following additional labels.                                                                                                                                                                                                                         |
| Label                  | Description                                                                                               |
| ---                    | ---                                                                                                       |
| **alertname**          | Either `DatasourceNoData` or `DatasourceError`, depending on the state.                                   |
| **datasource_uid**     | The UID of the data source that caused the state.                                                         | ###### Note You will need to set the no data or error handling to `NoData` or `Error` in the alert rule, as described in the [Configure Grafana managed alert rules](v10-alerting-configure-grafanamanaged.md "v10-alerting-configure-grafanamanaged.md") topic, to generate the additional labels. You can handle these alerts the same way as regular alerts, including adding silences, routing to a contact point, and so on. |
