# Change axis display

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

This section explains how to use Time series field options to control the display
of axes in the visualization and illustrates what the axis options do.

There are a variety of options for the axes.

- **Y-axis placement** – Set the
  placement of the y-axis. The choices are **Left**,
  **Right**, and **Hidden**.
- **Y-axis label** – Set a text label
  for the y-axis. If you have more than one y-axis, you can use the
  **Override** tab to assign them different
  labels.
- **Width** – Set the fixed width of the
  axis. By default, the Grafana workspace dynamically calculates the axis
  width. By setting the width of the axis, data whose axes types are different
  can share the same display proportions. This makes it easier to compare more
  than one graph’s worth of data because the axes are not shifted or stretched
  within visual proximity of each other.
- **Soft min and soft max** – Set a
  **Soft min** or **Soft max** for
  better control of y-axis limits. By default, the Grafana workspace sets the
  range for the y-axis automatically based on the data.

**Soft min** or **Soft max** settings
can prevent blips from appearing as mountains when the data is mostly flat,
and hard min or max derived from standard min and max field options can
prevent intermittent spikes from flattening useful detail by clipping the
spikes past a defined point.

- **Scale** – Set the scale to use for
  y-axis values. The choices are **Linear** and
  **Logarithmic**.
