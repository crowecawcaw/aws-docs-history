# Trend

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Trend visualizations should be used for datasets that have a sequential, numeric X
that is not time. Some examples are function graphs, rpm/torque curves, supply/demand
relationships, and elevation or heart rate plots along a race course (with x as
distance or duration from start).

Trend visualizations support all visual styles and options available in the [time series visualization](v10-panels-time-series.md "v10-panels-time-series.md") with the following
exceptions:

- No annotations or time regions
- No shared cursor (or crosshair)
- No multi-timezone x axis
- No ability to change the dashboard time range via drag-selection
  **X Field selection**

Use this option to select a field that contains increasing numeric values.

For example, you could represent engine power and torque versus speed where speed
is plotted on the x axis and power and torque are plotted on the y axes.
