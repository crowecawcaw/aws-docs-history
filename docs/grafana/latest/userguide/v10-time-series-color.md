# Color options

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

By default, the graph uses the standard [Color scheme](v10-panels-configure-standard-options.md#v10-panels-standard-options-color-scheme "v10-panels-configure-standard-options.md#v10-panels-standard-options-color-scheme") option to
assign series colors. You can also use the legend to open the color picker by
selecting the legend series color icon. Setting color this way automatically creates
an override rule that set’s a specific color for a specific series.

The following are additional options that you can use to override series color
defaults.

## Classic palette

The most common setup is to use the **Classic palette** for
graphs. This scheme automatically assigns a color for each field or series based on
its order. If the order of a field changes in your query, the color also changes.
You can manually configure a color for a specific field using an override
rule.

## Single color

Use this mode to specify a color. You can also select the colored line icon
next to each series in the Legend to open the color picker. This automatically
creates a new override that sets the color scheme to single color and the
selected color.

## By value color schemes

If you select a by value color scheme like **From thresholds (by
value)** or **Green-Yellow-Red (by value)**, the
**Color series by** option appears. This option controls which
value (Last, Min, Max) to use to assign the series its color.

## Scheme gradient mode

The **Gradient mode** option located under the **Graph
styles** has a mode named **Scheme**. When you enable
**Scheme**, the line or bar receives a gradient color defined
from the selected **Color scheme**.

**From thresholds**

If the **Color scheme** is set to **From thresholds (by
value)** and **Gradient mode** is set to
**Scheme**, then the line or bar color changes as they cross
the defined thresholds. You will see only the exact colors chosen in the
scheme.

**Gradient color schemes**

Using a gradient color scheme _without_ setting
the **Gradient mode** to **Scheme**, means that
the colors chosen will form a gradient between the colors chosen, as the values in
the series move between the thresholds set.
