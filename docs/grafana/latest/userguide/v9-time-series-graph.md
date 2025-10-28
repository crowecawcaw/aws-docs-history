# Graph style options

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

**Graph style**

Use this option to define how to display your time series data. You can use
overrides to combine multiple styles in the same graph. There are three style
options. Some of the other style options only apply to certain graph styles.

- **Lines** – Display the time series as
  a line on a graph.
- **Bars** – Display the time series as
  a series of bars on a graph, one for each data point.
- **Points** – Display the time series
  as dots on a graph, one for each data point.
  **Bar alignment**

For bar graphs, , sets the position of the bar, relative to where the point would
be drawn on the graph. Because a bar has a width, it can be placed before, after, or
centered on the point. The choices for this option are **Before**,
**Center**, or **After**.

**Line width**

Sets the thickness of the line for Line graphs, or the thickness of the outline
for each bar in a bar graph.

**Fill opacity**

Sets the opacity of a fill color. Fills are used, for example, to show the area
under the line in a line graph, or as the color of bars in a bar graph.

**Gradient mode**

Gradient mode specifies the gradient fill, which is based on the series color. To
change the color, use the standard color scheme field option. For more information,
see [Color scheme](v9-panels-configure-standard-options.md#v9-panels-standard-options-color-scheme "v9-panels-configure-standard-options.md#v9-panels-standard-options-color-scheme"). The gradient mode
options are:

- **None** – No gradient fill.
- **Opacity** – An opacity gradient
  where the opacity of the fill increases as the Y-axis values
  increase.
- **Hue** – A gradient that is based on
  the hue of the series color.
- **Scheme** – A color gradient defined
  by your color scheme. This setting can be used by the fill and the line. For
  more information, see [Color options](v9-time-series-color.md "v9-time-series-color.md").
  The gradient appearance is also modified by the **Fill opacity**
  setting.

**Show points**

You can configure your visualization to add points to line or bar graphs. You can
choose **Always**, **Never**, or
**Auto**. When using **Auto**, Grafana
determines whether to show points based on the density of the data. If the density
of the data is low enough, points are shown.

**Point size**

Sets the size of drawn points, from 1 to 40 pixels in diameter.

**Line interpolation**

Choose how Grafana interpolates the series line. The choices are
**Linear**, **Smooth**, **Step
before**, and **Step after**.

**Line style**

Set the style of the line. To change the color, use the standard color scheme
field option.

Line style appearance is influenced by the settings for **Line
width** and **Fill opacity**.

The choices for line style are **Solid**,
**Dash**, and **Dots**.

**Connect null values**

Choose how null values (gaps in the data) appear on the graph. Null values can be
connected to form a continuous line or, optionally, set a threshold above which gaps
in the data should no longer be connected. You can choose to
**Never** connect data points with gaps,
**Always** connect data points with gaps, or set a
**Threshold** at which gaps in the data should no longer be
connected.

**Stack series**

_Stacking_ allows Grafana to display series on
top of each other. Be cautious when using stacking in the visualization as it can
easily create misleading graphs. To read more about why stacking might not be the
best approach, refer to [The Issue with Stacking](https://www.data-to-viz.com/caveat/stacking.html "https://www.data-to-viz.com/caveat/stacking.html").

The options for stacking are:

- **Off** – Turns off series
  stacking.
- **Normal** – Stacks series on top of
  each other.
- **100%** – Stack by percentage, where
  all series together add up to 100%.
  **Stack series in groups**

You can override the stacking behavior to stack series in groups. For more
information about creating an override, see [Configure field overrides](v9-panels-configure-overrides.md "v9-panels-configure-overrides.md"). When creating the override,
give the name of the stacking group you want the series to be part of.

**Fill below to**

The **Fill below to** option fills the area between two series.
This options is only available as a series or field override. Using this option you
can fill the area between two series, rather than from the series line down to 0.
For example, if you had two series called _Max_ and
_Min_, you could select the **Max** series and override it to **Fill below
to** the **Min** series.. This would fill
only the area between the two series lines.
