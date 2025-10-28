# Configure a legend

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

A panel includes a legend that you can use to interpret data displayed in a visualization.
Each legend option adds context and clarity to the data illustrated in a
visualization.

## Isolating series data in a visualization

Visualizations can often be visually complex, and include many data series. You can
simplify the view by removing series data from the visualization, which isolates the
data you want to see. Grafana automatically creates a new override in the
**Override** tab.

When you apply your changes, the visualization changes appear to all users of the
panel.

###### To isolate series data in a visualization

1. Open the panel.
2. In the legend, select the label of the series you want to isolate.

The system removes from view all other series data. 3. To incrementally add series data to an isolated series, press the
**Ctrl** or **Command** key and select the label of the series you want to
add. 4. To revert back to the default view that includes all data, click any
series label twice. 5. To save your changes so that they appear to all viewers of the panel,
select **Apply**.

This topic currently applies to the following visualizations:

- [Bar chart](v9-panels-bar-chart.md "v9-panels-bar-chart.md")
- [Histogram](v9-panels-histogram.md "v9-panels-histogram.md")
- [Pie chart](v9-panels-piechart.md "v9-panels-piechart.md")
- [State timeline](v9-panels-state-timeline.md "v9-panels-state-timeline.md")
- [Status history](v9-panels-status-history.md "v9-panels-status-history.md")
- [Time series](v9-panels-time-series.md "v9-panels-time-series.md")

## Adding values to a legend

As way to add more context to a visualization, you can add series data values to a
legend. You can add as many values as you’d like; after you apply your changes, you can
horizontally scroll the legend to see all values.

###### To add values to a legend

1. Edit a panel.
2. In the panel display options pane, locate the **Legend**
   section.
3. In the **Legend values** field, select the
   values you want to appear in the legend.
4. Choose **Apply** to save your changes are
   navigate back to the dashboard.

## Changing a series color

By default, Grafana specifies the color of your series data, which you can
change.

###### To change a series color

1. Edit a panel.
2. In the legend, select the color bar associated with the series.
3. Select a pre-set color or a custom color from the color palette.
4. Choose **Apply** to save your changes are
   navigate back to the dashboard.

## Sort series

You can change legend mode to **Table** and choose [Calculation types](v9-panels-calculation-types.md "v9-panels-calculation-types.md")
to be displayed in the legend. Select the calculation name
header in the legend table to sort the values in the table in ascending or descending
order.

The sort order affects the positions of the bars in the Bar chart panel as well as the
order of stacked series in the Time series and Bar chart panels.

###### Note

This feature is only supported in these
panels: Bar chart, Histogram, Time series, XY Chart.
