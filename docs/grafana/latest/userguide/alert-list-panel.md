# Alert list panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The alert list panel displays your dashboards alerts. You can configure the list to
show current state or recent state changes. For more information about alerts, see [Grafana alerting](alerts-overview.md "alerts-overview.md").

Use these settings to refine your visualization.

## Options

- Show – Choose whether the panel should
  display the current alert state or recent alert state changes.
- Max Items – Set the maximum number of
  alerts to list.
- Sort order – Select how to order the
  alerts displayed.
  - Alphabetical (asc) –
    Alphabetical order
  - Alphabetical (desc) – Reverse
    alphabetical order
  - Importance – By importance
    according to the following values, with 1 being the highest:
    - alerting: 1
    - no_data: 2
    - pending: 3
    - ok: 4
    - paused: 5

- Alerts from this dashboard – Show
  alerts only from the dashboard that the alert list is in.

## Filter

Use the following options to filter the alerts to match the query, folder, or
tags that you choose:

- Alert name – Enter an alert name query.
- Dashboard title – Enter a dashboard
  title query.
- Folder – Select a folder. Only alerts
  from dashboards in the selected folder will be displayed.
- **Dashboard tags -** Select one or more tags.
  Only alerts from dashboards with one or more of the tags will be displayed.

## State filter

Choose which alert states to display in this panel.

- Ok
- Paused
- No data
- Execution error
- Alerting
- Pending
