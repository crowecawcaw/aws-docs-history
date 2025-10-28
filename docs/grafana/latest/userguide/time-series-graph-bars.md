# Graph time series as bars

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

This section explains how to use Time series field options to visualize time
series data as bars and illustrates what the options do.

###### Create the panel

1. Create a panel, selecting the **Time series**
   visualization. For more information, see [Adding a panel](add-a-panel-to-a-dashboard.md "add-a-panel-to-a-dashboard.md").
2. In the **Panel editor**, choose
   **Field**.
3. In **Style**, choose **Bars**.

## Style the bars

There are a variety of options for styling the bars.

- **Bar alignment** – Set the
  position of the bar relative to a data point. The choices are
  **Before**, **Center**, and
  **After**.
- **Line width** – Set the thickness
  of the bar outlines between 0 and 10 pixels.
- **Fill opacity** – Set the opacity
  of the bar fill, from 0 to 100 percent.
- **Gradient mode** – Set the mode
  of the gradient fill. Fill gradient is based on the line color. To
  change the color, use the standard color scheme field option.

Gradient appearance is influenced by the setting for **Fill
opacity**.

The choices for gradient fill are **None**,
**Opacity**, and **Hue**. With
**Opacity**, Transparency of the gradient is
calculated based on the values on the y-axis. Opacity of the fill is
increasing with the values on the y-axis. With **Hue**,
the gradient color is generated based on the hue of the line
color.

- **Show points** – Choose when the
  points should be shown on the graph. The choices are
  **Auto**, **Always** and
  **Never**.
