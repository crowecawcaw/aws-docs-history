# Axis options

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Options under the axis category change how the x- and y-axes are rendered. Some
options do not take effect until you click outside of the field option box you are
editing. You can also press `Enter`.

## Time zone

Set the desired time zones to display along the x-axis.

## Placement

Select the placement of the Y-axis. The options are:

- **Auto** – Automatically assigns the y-axis
  to the series. When there are two or more series with different units,
  Grafana assigns the left axis to the first unit, and the right axis
  to the units that follow.
- **Left** – Display all y-axes on the
  left side.
- **Right** – Display all y-axes on the
  right side.
- **Hidden** – Hide all axes.

To selectively hide axes, [add
a field override](v10-panels-configure-overrides.md "v10-panels-configure-overrides.md") that targets specific fields.

## Label

Set a y-axis text label. If you have more than one y-axis, then you can assign
different labels using an override.

## Width

Set a fixed width of the axis. By default, Grafana dynamically calculates the
width of an axis.

By setting the width of the axis, data with different axes types can share the
same display proportions. This setting makes it easier for you to compare more than
one graph’s worth of data because the axes are not shifted or stretched within
visual proximity to each other.

## Show grid lines

Set the axis grid line visibility.

- **Auto** – Automatically show grid lines
  based on the density of the data.
- **On** – Always show grid lines.
- **Off** – Never show grid lines.

## Color

Set the color of the axis.

- **Text** – Set the color based on theme
  text color.
- **Series** – Set the color based on the
  series color.

## Show border

Set the axis border visibility.

## Scale

Set how the y-axis values scale.

- **Linear** – Divides the scale into equal
  parts.
- **Logarithmic** – Use a logarithmic scale.
  When you select this option, a list appears for you to choose a binary
  (base 2) or common (base 10) logarithmic scale.
- **Symlog** – Use a symmetrical logarithmic
  scale. When you select this option, a list appears for you to choose a
  binary (base 2) or common (base 10) logarithmic scale. The linear
  threshold option allows you to set the threshold at which the scale
  changes from linear to logarithmic.

## Centered zero

Sets the y-axis to be centered on zero.

## Soft min and soft max

Set a **Soft min** or **soft max** option
for better control of y-axis limits. By default, Grafana sets the range for
the y-axis automatically based on the dataset.

Soft min and soft max settings can prevent small variations in the data from
being magnified when it's mostly flat. In contrast, hard min and max values
help prevent obscuring useful detail in the data by clipping intermittent spikes
past a specific point.

To define hard limits of the y-axis, set standard min/max options. For
more information, refer to [Configure standard options](v10-panels-configure-standard-options.md "v10-panels-configure-standard-options.md").

## Transform

Use this option to transform the series values without affecting the values
shown in the tooltip, context menus, or legend. You have two transform
options:

- **Negative Y transform** – Flip the
  results to negative values on the Y axis.
- **Constant** – Show the first value as
  a constant line.

###### Note

The transform option is only available as an override.

## Display multiple y-axes

There are some cases where you want to display multiple y-axes. For example,
if you have a dataset showing both temperature and humidity over time, you
could show two y-axes with different units for these two series.

To display multiple y-axes, [add a field override](v10-panels-configure-overrides.md#v10-panels-overrides-add-a-field "v10-panels-configure-overrides.md#v10-panels-overrides-add-a-field"). Follow the steps as many times as required to
add as many y-axes as you need.
