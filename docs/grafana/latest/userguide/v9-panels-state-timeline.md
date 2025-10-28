# State timeline panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The state timeline panel visualization shows discrete state changes over time. Each
field or series is rendered as its unique horizontal band. State regions can either be
rendered with or without values. This panel works well with string or boolean states but
can also be used with time series. When used with time series, the thresholds are used
to turn the numerical values into discrete state regions.

## State timeline options

Use these options to refine your visualizations:

**Merge equal consecutive values**

Controls whether Grafana merges identical values if they are next to each
other.

**Show values**

Controls whether values are rendered inside the state regions. Auto will render
values if there is sufficient space.

**Align values**

Controls value alignment inside state regions.

**Row height**

Controls space between rows. 1 = no space = 0.5 = 50% space.

**Line width**

Controls the line width of state regions.

**Fill opacity**

Controls the opacity of state regions.

## Value mappings

To assign colors to boolean or string values, use [Configure value mappings](v9-panels-configure-value-mappings.md "v9-panels-configure-value-mappings.md").

## Time series data with thresholds

The panel can be used with time series data as well. In this case, the thresholds
are used to turn the time series into discrete colored state regions.

## Legend options

When the legend option is enabled, it can show either the value mappings or the
threshold brackets. To show the value mappings in the legend, it’s important that
the Color scheme option under Standard options is set to Single color or Classic
palette. To see the threshold brackets in the legend, set the Color scheme to From
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
