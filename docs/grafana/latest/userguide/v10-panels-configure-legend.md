# Configure a legend

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

A panel includes a legend that you can use to interpret data displayed in a
visualization. Each legend option adds context and clarity to the data illustrated
in a visualization.

Legends are supported for the following visualizations:

- [Bar chart](v10-panels-bar-chart.md "v10-panels-bar-chart.md")
- [Candlestick](v10-panels-candlestick.md "v10-panels-candlestick.md")
- [Histogram](v10-panels-histogram.md "v10-panels-histogram.md")
- [Pie chart](v10-panels-piechart.md "v10-panels-piechart.md")
- [State timeline](v10-panels-state-timeline.md "v10-panels-state-timeline.md")
- [Status history](v10-panels-status-history.md "v10-panels-status-history.md")
- [Time series](v10-panels-time-series.md "v10-panels-time-series.md")
- [Trend](v10-panels-trend.md "v10-panels-trend.md")
  [Geomaps](v10-panels-geomap.md "v10-panels-geomap.md") and
  [Heatmaps](v10-panels-heatmap.md "v10-panels-heatmap.md") also have legends, but they
  only provide the choice to display or not display a legend, and don't support other
  legend options.

## Legend options

You can find the following options under the **Legend**
section in the panel edit pane.

###### Note

Not all of the options listed apply to all visualizations with legends.

**Visibility**

Set whether the legend is displayed or not. Use the switch to toggle a legend
on or off.

**Mode**

Set the format in which the legend is displayed. Choose from:

- **List**
- **Table**

When you format a legend as a table, other information about the legend, such as
associated values or where it's located in the visualization, might be displayed
as well.

**Placement**

Set where on the visualization a legend is displayed. Choose from:

- **Bottom**
- **Right**

**Width**

If you set the legend placement to **Right**, the
**Width** option becomes available. Leave the field empty to
allow Grafana to automatically set the legend width, or enter a vale in the
field.

**Values**

You can add more context to a visualization by adding series data values or
[calculations](v10-panels-calculation-types.md "v10-panels-calculation-types.md") to a legend.
You can add as many values as you like. After you apply your changes, you can
scroll the legend to see all values.

## Changing a series color

By default, Grafana sets the color of your series data, but you can change them
through the panel legend.

###### To change a series color

1. Navigate to the panel you want to update.
2. In the legend, select the color bar associated with the series.
3. Select a pre-set color in the **Colors** tab or set a
   custom color in the **Custom** tab, using the picker or
   RGB values.
4. Save the dashboard.

## Isolating series data in a visualization

Visualizations can often be visually complex, and include many data series. You
can simplify the view by removing series data from the visualization through the
legend, which isolates the data you want to see. When you do this, Grafana
automatically creates a new override in the **Override**
tab.

###### To isolate series data in a visualization

1. Navigate to the panel you want to update.
2. In the legend, select the label of the series you want to isolate.

The system removes from view all other series data. 3. To incrementally add series data back to an isolated series, press the
**Ctrl** or **Command** key and select the label of the series you want to
add. 4. To save your changes so that they appear to all viewers of the panel,
save the dashboard.

To revert back to the default view that includes all data, click any
series label twice.

## Sorting series

When you format a legend as a table and add values to it, you can sort the
series in the table by those values.

###### To sort series

1. Navigate to the panel you want to update.
2. Hover over any part of the panel you want to work on to display the
   menu on the top right corner of the panel.
3. From the menu, choose **Edit**.
4. Scroll to the **Legend** section of the panel edit
   pane.
5. Under **Values**, select the value or calculation that
   you want to show.

The legend now displays values. 6. Choose the calculation name header in the legend table to sort the
values in the table in ascending or descending order.

###### Note

This feature is only supported in these
panels: bar chart, histogram, time series.
