# Axis options

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Options under the axis category change how the X and Y axes are rendered. Some
options do not take effect until you click outside of the field option box you are
editing. You can also or press `Enter`.

**Placement**

Select the placement of the Y-axis. The options are:

- **Auto** – Grafana automatically
  assigns the Y-axis to the series. When there are two or more series with
  different units, Grafana assigns the left axis to the first unit, and the
  right axis to the units that follow.
- **Left** – Display all Y-axes on the
  left side.
- **Right** – Display all Y-axes on the
  right side.
- **Hidden** – Hide all Y-axes.
  To assign axes for each field or series, [add field overrides](v9-panels-configure-overrides.md "v9-panels-configure-overrides.md").

**Label**

Set a Y-axis text label. If you have more than one Y-axis, then you can assign
different labels using an override.

**Width**

Set a fixed width of the axis. By default, Grafana dynamically calculates the
width of an axis.

By setting the width of the axis, data with different axes types can share the
same display proportions. This setting makes it easier for you to compare more than
one graph’s worth of data because the axes are not shifted or stretched within
visual proximity to each other.

**Soft min and soft max**

Set a **Soft min** or **soft max** option for
better control of Y-axis limits. By default, Grafana sets the range for the Y-axis
automatically based on the dataset.

Soft min and soft max settings allow visibility into small changes when big
changes aren't present. Hard min or max derived from standard min and max field
options can prevent intermittent spikes from flattening useful detail by clipping
the spikes past a specific point.

To define hard limits of the Y-axis, You can set standard min/max options. For
more information, refer to [Configure standard options](v9-panels-configure-standard-options.md "v9-panels-configure-standard-options.md").

**Scale**

Set how the Y-axis scales. The choices are **Linear** or
**Logarithmic**. If you choose logarithmic, you can further
choose between base 2 or base 10 logarithmic scales.

**Transform**

You can override a series to apply a transform to values on a graph (without
affecting the underlying values or the values in tooltips, context menus, or
legends). You have two transform options:

- **Negative Y transform** – Flip the
  results to negative values on the Y axis.
- **Constant** – Show the first value as
  a constant line.
