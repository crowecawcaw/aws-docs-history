

# State and health of alerting rules
<a name="v12-alerting-explore-state"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 12.x**.  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

The state and health of alerting rules help you understand several key status indicators about your alerts.

There are three key components: *alert rule state*, *alert instance state*, and *alert rule health*. Although related, each component conveys subtly different information.

**Important**  
**Alert rule evaluation result limit** – Beginning in Grafana version 12, the number of query evaluation results per alert rule is limited to 500. If the condition query of an alert rule produces more results than this limit, the evaluation results in an error. To receive alerts when this error occurs, configure `Alert state if execution error or timeout` to `Error` under the alert rule's settings.

**Alert rule state**

An alert rule can be in one of the following states:


| State | Description | 
| --- | --- | 
| Normal | None of the time series returned by the evaluation engine is in a `Pending` or `Firing` state. | 
| Pending | At least one time series returned by the evaluation engine is `Pending`. | 
| Firing | At least one time series returned by the evaluation engine is `Firing`. | 
| Recovering | The alert condition is no longer firing but has not yet returned to normal. | 

**Note**  
Alerts will transition first to `pending` and then `firing`, thus it will take at least two evaluation cycles before an alert is fired.

**Alert instance state**

An alert instance can be in one of the following states:


| State | Description | 
| --- | --- | 
| Normal | The state of an alert that is neither firing nor pending, everything is working correctly. | 
| Pending | The state of an alert that has been active for less than the configured threshold duration. | 
| Alerting | The state of an alert that has been active for longer than the configured threshold duration. | 
| Recovering | The state of an alert that was previously firing but the alert condition is no longer met. The alert has not yet returned to normal. | 
| NoData | No data has been received for the configured time window. | 
| Error | The error that occurred when attempting to evaluate an alerting rule. | 

**Keep last state**

An alert rule can be configured to keep the last state when `NoData` or `Error` state is encountered. This will both prevent alerts from firing, and from resolving and re-firing. Just like normal evaluation, the alert rule will transition from `Pending` to `Firing` after the pending period has elapsed.

**Alert rule health**

An alert rule can have one the following health statuses:


| State | Description | 
| --- | --- | 
| Ok | No error when evaluating an alerting rule. | 
| Error | An error occurred when evaluating an alerting rule. | 
| NoData | The absence of data in at least one time series returned during a rule evaluation. | 

**Special alerts for `NoData` and `Error`**

When evaluation of an alerting rule produces state `NoData` or `Error`, Grafana Alerting will generate alert instances that have the following additional labels:


| Label | Description | 
| --- | --- | 
| alertname | Either `DatasourceNoData` or `DatasourceError` depending on the state. | 
| datasource\_uid | The UID of the data source that caused the state. | 

You can handle these alerts the same way as regular alerts by adding a silence, route to a contact point, and so on.