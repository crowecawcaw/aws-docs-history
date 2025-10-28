# State and health of alerting

rules

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The state and health of alerting rules help you understand several key status
indicators about your alerts.

There are three key components: _alert rule state_,
_alert instance state_, and _alert rule
health_. Although related, each component conveys subtly
different information.

**Alert rule state**

An alert rule can be in one of the following states:

| State          | Description                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Normal         | None of the time series returned by the evaluation engine is in a `Pending` or `Firing` state. |
| Pending        | At least one time series returned by the evaluation engine is `Pending`.                       |
| Firing         | At least one time series returned by the evaluation engine is `Firing`.                        | ###### Note Alerts will transition first to `pending` and then `firing`, thus it will take at least two evaluation cycles before an alert is fired. **Alert instance state** An alert instance can be in one of the following states:                                                                                                                                                                               |
| State          | Description                                                                                    |
| ---            | ---                                                                                            |
| Normal         | The state of an alert that is neither firing nor pending, everything is working correctly.     |
| Pending        | The state of an alert that has been active for less than the configured threshold duration.    |
| Alerting       | The state of an alert that has been active for longer than the configured threshold duration.  |
| NoData         | No data has been received for the configured time window.                                      |
| Error          | The error that occurred when attempting to evaluate an alerting rule.                          | **Keep last state** An alert rule can be configured to keep the last state when `NoData` or `Error` state is encountered. This will both prevent alerts from firing, and from resolving and re-firing. Just like normal evaluation, the alert rule will transition from `Pending` to `Firing` after the pending period has elapsed. **Alert rule health** An alert rule can have one the following health statuses: |
| State          | Description                                                                                    |
| ---            | ---                                                                                            |
| Ok             | No error when evaluating an alerting rule.                                                     |
| Error          | An error occurred when evaluating an alerting rule.                                            |
| NoData         | The absence of data in at least one time series returned during a rule evaluation.             | **Special alerts for `NoData` and `Error`** When evaluation of an alerting rule produces state `NoData` or `Error`, Grafana Alerting will generate alert instances that have the following additional labels:                                                                                                                                                                                                       |
| Label          | Description                                                                                    |
| ---            | ---                                                                                            |
| alertname      | Either `DatasourceNoData` or `DatasourceError` depending on the state.                         |
| datasource_uid | The UID of the data source that caused the state.                                              | You can handle these alerts the same way as regular alerts by adding a silence, route to a contact point, and so on.                                                                                                                                                                                                                                                                                                |
