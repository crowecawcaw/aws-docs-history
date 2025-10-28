# Configure thresholds

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

This section includes information about using thresholds in your visualizations. You’ll
learn about thresholds and their defaults, how to add or delete a threshold, and adding a
threshold to a legacy panel.

## About thresholds

A threshold is a value that you specify for a metric that is visually reflected in a
dashboard when the threshold value is met or exceeded.

Thresholds provide one method for you to conditionally style and color your
visualizations based on query results. You can apply thresholds to most, but not all,
visualizations. For more information about visualizations, refer to [Visualization panels](v9-panels.md "v9-panels.md").

You can use thresholds to:

- Color grid lines or grid ares areas in the [Time-series visualization](v9-panels-time-series.md "v9-panels-time-series.md")
- Color lines in the [Time-series
  visualization](v9-panels-time-series.md "v9-panels-time-series.md")
- Color the background or value text in the [Stat
  visualization](v9-panels-stat.md "v9-panels-stat.md")
- Color the gauge and threshold markers in the [Gauge visualization](v9-panels-gauge.md "v9-panels-gauge.md")
- Color markers in the [Geomap
  visualization](v9-panels-geomap.md "v9-panels-geomap.md")
- Color cell text or background in the [Table
  visualization](v9-panels-table.md "v9-panels-table.md")
- Define regions and region colors in the [State timeline visualization](v9-panels-state-timeline.md "v9-panels-state-timeline.md")

There are two types of thresholds:

- **Absolute** thresholds are defined by a number.
  For example, 80 on a scale of 1 to 150.
- **Percentage** thresholds are defined relative to
  minimum or maximum. For example, 80 percent.

### Default thresholds

On visualizations that support it, Grafana sets default threshold values of:

- 80 = red
- Base = green
- Mode = Absolute

The **Base** value represents minus infinity. It
is generally the "good" color.

## Add or delete a threshold

You can add as many thresholds to a panel as you want. Grafana automatically sorts
thresholds values from highest to lowest.

Delete a threshold when it is no longer relevant to your business operations. When
you delete a threshold, the system removes the threshold from all visualizations that
include the threshold.

1. To add a threshold:
   1. Edit the panel to which you want to add a threshold.
   2. In the options side pane, locate the **Thresholds** section and click **+
      Add threshold**.
   3. Select a threshold color, number, and mode. Threshold mode applies to
      all thresholds on this panel.
   4. For a time-series panel, select a **Show
      thresholds** option.

2. To delete a threshold, navigate to the panel that contains the threshold and
   click the trash icon next to the threshold you want to remove.

## Add a threshold to a legacy graph

panel

In the Graph panel visualization, thresholds enable you to add lines or sections to a
graph to make it easier to recognize when the graph crosses a threshold.

1. Navigate to the graph panel to which you want to add a threshold.
2. On the **Panel** tab, click **Thresholds**.
3. Click **Add threshold**.
4. Complete the following fields:
   - **T1 -** Both values are required to
     display a threshold.
     - **lt** or **gt** - Select **lt** for less than or **gt** for greater than to indicate what the
       threshold applies to.
     - **Value -** Enter a threshold
       value. Grafana draws a threshold line along the Y-axis at that
       value.

   - **Color -** Choose a condition that
     corresponds to a color, or define your own color.
     - **custom -** You define the fill
       color and line color.
     - **critical -** Fill and line
       color are red.
     - **warning -** Fill and line color
       are yellow.
     - **ok -** Fill and line color are
       green.

   - **Fill -** Controls whether the threshold
     fill is displayed.
   - **Line -** Controls whether the threshold
     line is displayed.
   - **Y-Axis -** Choose **left** or **right**.

5. Click **Save** to save the changes in the
   dashboard.
