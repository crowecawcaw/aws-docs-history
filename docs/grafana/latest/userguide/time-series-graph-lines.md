# Graph time series as lines

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

This section explains how to use Time series field options to visualize time
series data as lines and illustrates what the options do.

###### Create the panel

1. Create a panel, selecting the **Time series**
   visualization. For more information, see [Adding a panel](add-a-panel-to-a-dashboard.md "add-a-panel-to-a-dashboard.md").
2. In the **Panel editor**, choose
   **Field**.
3. In **Style**, choose **Lines**.

## Style the lines

There are a variety of options for styling the lines.

- **Line interpolation** – Choose
  how Grafana interpolates the series line. The choices are
  **Linear**, **Smooth**,
  **Step before**, and **Step
  after**.
- **Line width** – Set the line
  thickness between 0 and 10 pixels.
- **Fill opacity** – Set the opacity
  of the series fill, from 0 to 100 percent.
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

- **Line style** – Set the style of
  the line. To change the color, use the standard color scheme field
  option.

Line style appearance is influenced by the settings for **Line
width** and **Fill opacity**.

The choices for line style are **Solid**,
**Dash**, and **Dots**.

- **Null values** – Choose how gaps
  in the data are displayed. Null values can be connected to form a
  continuous line or, optionally, set a threshold above which gaps in the
  data should no longer be connected. You can choose to
  **Never** connect data points with gaps,
  **Always** connect data points with gaps, or set a
  **Threshold** at which gaps in the data should no
  longer be connected.
- **Show points** – Choose when the
  points should be shown on the graph. The choices are
  **Auto**, **Always**, and
  **Never**.

## Fill below to

This option is available only in the overrides tab.

###### To fill the area between two series

1. Select the fields to fill below.
2. In **Add override property**, choose **Fill
   below to**.
3. Select the series that you want the fill to stop at.
