# Thresholds

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Thresholds set the color of either the value text or the background depending on
conditions that you define.

You can define thresholds one of two ways:

- **Absolute** thresholds are defined based on a
  number; for example, 80 on a scale of 1–150.
- **Percentage** thresholds are defined relative to
  minimum or maximum; for example, 80 percent.
  You can apply thresholds to the following visualizations:

- [Bar gauge panel](alert-panel-bar-gauge-panel.md "alert-panel-bar-gauge-panel.md")
- [Gauge panel](gauge-panel.md "gauge-panel.md")
- [Graph panel](graph-panel.md "graph-panel.md")
- [Stat panel](stat-panel.md "stat-panel.md")
- [Table panel](table-panel.md "table-panel.md")

## Default thresholds

On visualizations that support it, Amazon Managed Grafana sets the following default threshold
value: 80 = red; Base = green; Mode = Absolute.

The **Base** value represents minus infinity. It is
generally the _good_ color.

## Adding a threshold

You can add as many thresholds to a panel as you want. The Grafana workspace
automatically sorts thresholds from highest value to lowest.

###### Note

These instructions apply only to the stat, gauge, bar gauge, and table
visualizations.

1. Choose the panel that you want to add a threshold to.
2. Choose the **Field** tab.
3. Choose **Add threshold**.

Amazon Managed Grafana adds a threshold with suggested numerical and color values. 4. Accept the recommendations or edit the new threshold.

    * Edit color – Choose the color
     dot that you want to change, and then select a new color.
    * Edit number – Choose the number
     that you want to change, and then enter a new number.
    * Thresholds mode – Choose the
     mode to change it for all thresholds on this panel.

5. Choose **Save** to save the changes in the
   dashboard.

## Adding a threshold to a graph

panel

In the graph panel visualization, you can use thresholds to add arbitrary lines
or sections to the graph to make it easier to see when the graph crosses a
particular threshold.

1. Choose the graph panel that you want to add a threshold to.
2. On the **Panel** tab, choose **Thresholds**.
3. Choose **Add threshold**.
4. Fill in as many fields as you want. Only the **T1** fields are required.
   - T1 – Both values are required
     to display a threshold.
     - lt or gt – Select **lt** for
       less than or **gt** for greater than to
       indicate what the threshold applies to.
     - Value – Enter a
       threshold value. The Grafana workspace draws a threshold
       line along the y-axis at that value.

   - Color – Choose a condition that
     corresponds to a color, or define your own color.
     - custom – You define the
       fill color and line color.
     - critical – Fill and
       line color are red.
     - warning – Fill and line
       color are yellow.
     - ok – Fill and line
       color are green.

   - Fill – Choose whether the
     threshold fill is displayed.
   - Line – Choose whether the
     threshold line is displayed.
   - Y-Axis – Choose **left** or **right**.

5. Choose **Save** to save the changes in the dashboard.

## Deleting a threshold

1. Choose the panel that you want to remove a threshold from.
2. Choose the **Field** tab. (Or, for a graph panel, choose
   the **Panel** tab.)
3. Choose the trash can icon next to the threshold that you want to remove.
4. Choose **Save** to save the changes in the dashboard.
