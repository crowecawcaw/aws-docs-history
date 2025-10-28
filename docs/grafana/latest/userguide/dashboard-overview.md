# Dashboards

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

A _dashboard_ is a set of one or more panels organized and arranged
into one or more rows. Amazon Managed Grafana ships with a variety of panels. Amazon Managed Grafana makes it easy to
construct the right queries and customize the display properties so that you can create the
dashboard you need. Each panel can interact with data from any configured data source.

## Manage dashboards

To control the time period for the dashboard, you can use the [Time range controls](dashboard-time-range-controls.md "dashboard-time-range-controls.md") in the upper right of the dashboard.

Dashboards can use templates and variables to make them more dynamic and interactive.
For more information, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

Dashboards can use [Annotations](dashboard-annotations.md "dashboard-annotations.md") to display event data across panels. This
can help correlate the time series data in the panel with other events.

Dashboards can be shared easily in a variety of ways. For more information, see [Sharing a dashboard](share-a-dashboard.md "share-a-dashboard.md").

Dashboards can be tagged, and the dashboard picker provides quick, searchable access
to all dashboards in a particular organization.

## Rows

A _row_ is a logical divider within a dashboard. It is used to
group panels together.

Rows are always 12 _units_ wide. These units are automatically
scaled based on the horizontal resolution of your browser. You can control the relative
width of panels within a row by setting their specific width.

Amazon Managed Grafana uses a unit abstraction to optimize appearance on all screen sizes.

###### Note

With MaxDataPoint functionality, Amazon Managed Grafana can display the required number of
data points, regardless of resolution or time range.

To collapse a row, choose the row title. If you save a dashboard with a row
collapsed, the dashboard is saved in that state, and those graphs do not load until
you expand the row.

Use the repeating rows functionality to dynamically create or remove entire rows of
panels, based on the template variables selected.
