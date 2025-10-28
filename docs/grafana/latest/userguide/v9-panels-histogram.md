# Histogram panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The histogram visualization calculates the distribution of values and presents them
as a bar chart. The Y-axis and the height of each bar represent the count of values that
fall into each bracket while the X-axis represents the value range.

Histogram visualization supports time series and any table results with one or more
numerical fields.

## Supported formats

Histogram visualization supports time series and any table results with one
or more numerical fields.

## Display options

Use these options to refine your visualizations:

**Bucket size**

The size of the buckets. Leave this empty for automatic bucket sizing (~10% of the
full range).

**Bucket offset**

If the first bucket should not start at zero. A non-zero offset shifts the
aggregation window. For example, 5-sized buckets that are 0–5, 5–10,
10–15 with a default 0 offset would become 2–7, 7–12,
12–17 with an offset of 2; offsets of 0, 5, or 10, in this case, would
effectively do nothing. Typically, this option would be used with an explicitly
defined bucket size rather than automatic. For this setting to affect, the offset
amount should be greater than 0 and less than the bucket size; values outside this
range will have the same effect as values within this range.

**Combine series**

This will merge all series and fields into a combined histogram.

**Line width** controls line width of the
bars.

**Fill opacity** controls the fill opacity of the
bars.

**Gradient mode** sets the mode of the gradient fill.
Fill gradient is based on the line color. To change the color, use the standard
color scheme field option. Gradient appearance is influenced by the Fill opacity
setting.

- None – No gradient fill, this is the
  default setting.
- Opacity – Transparency of the gradient
  is calculated based on the values on the Y-axis. Opacity of the fill is
  increasing with the values on the Y-axis.
- Hue – Gradient color is generated based
  on the hue of the line color.

Tooltip mode When you hover your cursor over the
graph, Grafana can display tooltips. Choose how tooltips behave:

- Single – The hover tooltip shows only
  the series that you are hovering over.
- All – The hover tooltip shows all the
  series in the visualization. Grafana highlights the series that you are
  hovering over in bold in the series list in the tooltip.
- Hidden – Do not display the tooltip.

###### Note

Use an override to hide individual series from the tooltip.

## Legend options

When the legend option is enabled, it can show either the value mappings or the
threshold brackets. To show the value mappings in the legend, it’s important that
the Color scheme option under standard options is set to Single color or Classic
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

**Legend Values**

Choose which of the standard calculations to show in the legend. You can have more
than one. For more information, see [Calculation types](v9-panels-calculation-types.md "v9-panels-calculation-types.md").

**Legend calculations**

Choose which calculations to show in the legend. You can select more than
one.
