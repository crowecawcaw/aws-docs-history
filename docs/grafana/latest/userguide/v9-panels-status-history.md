# Status history panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The Status history visualization shows periodic states over time. Each field or
series is rendered as a horizontal row. Boxes are rendered and centered around each
value.

Status history visualization works with string, boolean, and numerical fields or time
series. A time field is required. You can use value mappings to color strings or assign
text values to numerical ranges.

## Display options

Use these options to refine your visualizations:

**Show values**

Controls whether values are rendered inside the value boxes. Auto will render
values if there is sufficient space.

**Column width** controls the width of boxes. 1=max
and 0=Min width.

**Line width** controls line width of state
regions.

**Fill opacity** controls the fill opacity of state
regions.

## Value mappings

To assign colors to boolean or string values, use [Configure value mappings](v9-panels-configure-value-mappings.md "v9-panels-configure-value-mappings.md").

## Time series data with thresholds

The panel can be used with time series data as well. In this case, the thresholds
are used to color the boxes. You can also use gradient color schemes to color
values.

## Legend options

When the legend option is enabled, it can show either the value mappings or the
threshold brackets. To show the value mappings in the legend, it’s important that
the Color scheme option under Standard options is set to Single color or Classic
palette. To see the threshold brackets in the legend set the Color scheme to From
thresholds.

**Legend mode** Use these settings to refine how the
legend appears in your visualization.

- List – Displays the legend as a list.
  This is a default display mode of the legend.
- Table – Displays the legend as a
  table.
- Hidden – Hides the legend.

**Legend placement** Choose where to place the
legend.

- Bottom – Below the graph.
- Right – To the right of the
  graph.

**Legend values**

Choose which of the [standard
calculations](v9-panels-calculation-types.md "v9-panels-calculation-types.md") to show in the legend. You can have more than one.
