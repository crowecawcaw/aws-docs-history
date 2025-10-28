# What's new in Grafana alerting

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Grafana alerting has several enhancements over classic dashboard alerting.

## Create multidimensional alerting

You can now create a single alerting rule that gives you system-wide visibility,
generating multiple alert instances from a single alert rule. For example, you can
create a rule to monitor the disk usage of multiple mount points on a single host.
The evaluation engine returns multiple time series from a single query, with each
time series identified by its label set.

###### Note

Each alert instance counts toward the alert quota. Multidimensional rules that
create more instances than can be accommodated within the alert quota are not
evaluated and return a quota error. For more information, see [Quota reached errors](alert-rules.md#rule-quota-reached "alert-rules.md#rule-quota-reached").

## Create alerts outside of

dashboards

Unlike classic dashboard alerts, with Grafana alerting you can create queries and
expressions that combine data from multiple sources in unique ways. You can still
link dashboards and panels to alerting rules using their ID and quickly troubleshoot
the system under observation.

Since unified alerts are no longer directly tied to panel queries, they do not
include images or query values in the notification email. You can use customized
notification templates to view query values.

## Create Loki and Cortex alerting

rules

In Grafana alerting, you can manage Loki and Cortex alerting rules using the same
UI and API as your Grafana managed alerts.

## View and search alerts from Amazon Managed Service for Prometheus and

other Prometheus compatible data sources

Alerts for Amazon Managed Service for Prometheus and Prometheus compatible data sources are now listed in the
Alerting interface. You can search for labels across multiple data sources to
quickly find relevant alerts.

## Special alerts for alert state NoData and

Error

Grafana alerting generates special alerts that have the following labels, when
evaluation of an alerting rule produces state `NoData` or
`Error`:

- `alertname` with value `DatasourceNoData` or
  `DatasourceError` depending on the state.
- `rulename` with the name of the alert rule the special alert
  belongs to.
- `datasource_uid` has the UID of the data source that caused the
  state.
- All labels and annotations of the original rule.

You can handle these alerts the same as regular alerts, for example, by adding a
silence, or routing to a contact point.

###### Note

If the rule uses multiple data sources and one or more returns no data, the
special alert is created for each data source that caused the alert
state.
