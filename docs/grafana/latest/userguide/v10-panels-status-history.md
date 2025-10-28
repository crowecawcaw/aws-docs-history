# Status history

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Status histories show periodic states over time. Each field or series is rendered as
a horizontal row. Boxes are rendered and centered around each value.

## Supported data

A status history works with string, boolean, and numerical fields or time series. A
time field is required. You can use value mappings to color strings or assign text
values to numerical ranges.

## Display options

Use these options to refine the visualization.

**Show values**

Controls whether values are rendered inside the value boxes.
**Auto** will render values if there is sufficient space.

**Column width**

Controls the width of boxes. 1 = maximum space and 0 = minimum space.

**Line width**

Controls line width of state regions.

**Fill opacity**

Controls the fill opacity of state regions.

## Value mappings

To assign colors to boolean or string values, use [Configure value mappings](v10-panels-configure-value-mappings.md "v10-panels-configure-value-mappings.md").

## Time series data with thresholds

The panel can be used with time series data as well. In this case, the thresholds
are used to color the boxes. You can also use gradient color schemes to color
values.

## Legend options

When the legend option is enabled, it can show either the value mappings or the
threshold brackets. To show the value mappings in the legend, it’s important that
the **Color scheme** option under Standard options is set to
**Single color** or **Classic palette**. To see
the threshold brackets in the legend, set the **Color scheme** to
**From thresholds**.

**Legend mode**

Use these settings to define how the legend appears in your visualization. For
more information about the legend, refer to [Configure a legend](v10-panels-configure-legend.md "v10-panels-configure-legend.md").

- **List** – Displays the legend as a list.
  This is the default mode.
- **Table** – Displays the legend as a
  table.
- **Hidden** – Hides the legend.

**Legend placement**

Choose where to display the legend.

- **Bottom** – Below the graph.
- **Right** – To the right of the graph.

**Legend values**

Choose which of the [standard
calculations](v10-panels-calculation-types.md "v10-panels-calculation-types.md") to show in the legend. You can have more than one.
