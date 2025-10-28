# View and filter by alert

groups

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Alert groups show grouped alerts from an Alertmanager instance. By default, alert
rules are grouped by the label keys for the root policy in notification policies.
Grouping common alert rules into a single alert group prevents duplicate alert rules
from being fired.

You can view alert groups and also filter for alert rules that match specific
criteria.

###### To view alert groups

1. In the Grafana menu, click the **Alerting** (bell)
   icon to open the Alerting page listing existing alerts.
2. Click **Alert groups** to open the page listing
   existing groups.
3. From the **Alertmanager** dropdown, select an
   external Alertmanager as your data source.
4. From **custom group by** dropdown, select a
   combination of labels to view a grouping other than the default.
   This is useful for debugging and verifying your grouping of
   notification policies.
   If an alert does not contain labels specified either in the grouping of the
   root policy or the custom grouping, then the alert is added to a catch all group
   with a header of `No grouping`.

###### To filter by label

- In **Search**, enter an existing label to
  view alerts matching the label.

For example,
`environment=production,region=~US|EU,severity!=warning`.

###### To filter by state

- In **States**, select from Active,
  Suppressed, or Unprocessed states to view alerts matching your selected
  state. All other alerts are hidden.
