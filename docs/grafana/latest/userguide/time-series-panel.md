# Time series panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The time series panel can render a time series as a line, a path of dots, or a series
of bars. This type of graph is versatile enough to display almost any time-series data.

###### Note

You can migrate Graph panel visualizations to Time series visualizations. To
migrate, on the **Panel** tab, choose **Time series
visualization**. Grafana transfers all applicable settings.

Time series visualizations enable you to apply the following options:

- [Transformations](panel-transformations.md "panel-transformations.md")
- [Field options and overrides](field-options-overrides.md "field-options-overrides.md")
- [Thresholds](thresholds.md "thresholds.md")
  You can also use field options to create different types of graphs or adjust your
  axes.

Use these settings to refine your visualization.

## Tooltip mode

When you hover your cursor over the graph, Grafana can display tooltips. Choose
how tooltips behave:

- Single – The hover tooltip shows only
  the series that you are hovering over.
- All – The hover tooltip shows all the
  series in the graph. Grafana highlights the series that you are hovering
  over in bold in the series list in the tooltip.
- Hidden – Do not display the tooltip.

## Legend mode and placement

Choose how the legend appears.

- List – Displays the legend as a list.
  This is the default.
- Table – Displays the legend as a table.
- Hidden – Hides the legend.

Choose where to display the legend.

- Bottom – Below the graph.
- Right – To the right of the graph.

## Legend calculations

Choose which calculations to show in the legend. For more information, see [Calculations list](list-of-calculations.md "list-of-calculations.md").
