# Alert list

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Use alert lists to display your alerts. You can configure the list to
show current state. For more information about alerts, see [Alerts in Grafana version 10](v10-alerts.md "v10-alerts.md").

Use these settings to refine your visualization.

## Options

- **Group mode** – Choose between **Default
  grouping** to show alert instances grouped by their alert rule,
  and **Custom grouping** to group alert instances by a
  custom set of labels.
- **Max Items** – Set the maximum number of
  alerts to list.
- **Sort order** – Select how to order the
  alerts displayed.
  - **Alphabetical (asc)** –
    Alphabetical order
  - **Alphabetical (desc)** – Reverse
    alphabetical order
  - **Importance** – By importance
    according to the following values, with 1 being the highest:
    - `alerting` or `firing`: 1
    - `no_data`: 2
    - `pending`: 3
    - `ok`: 4
    - `paused` or `inactive`: 5

  - **Time (asc)** – Newest active alert
    instances first.
  - **Time (desc)** – Oldest active alert
    instances first.

- **Alerts from this dashboard** – Show
  alerts only from the dashboard that the alert list is in.

## Filter

These options allow you to limit alerts shown to only those that match the
query, folder, or tags that you choose:

- **Alert name** – Enter an alert name query.
- **Alert instance label** – Filter alert
  instances using label querying. For example, `{severity="critical",
instance=~"cluster-us-.+"}`.
- **Folder** – Select a folder. Only alerts
  from dashboards in the selected folder will be displayed.
- **Datasource** – Filter alerts from the
  selected data source.

## State filter

Choose which alert states to display in this panel.

- Alerting / Firing
- Pending
- No data
- Normal
- Error
