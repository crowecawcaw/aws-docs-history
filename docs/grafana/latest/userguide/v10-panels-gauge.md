# Gauge

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Gauges are single-value visualizations that can repeat a gauge for every series, column
or row.

![An image showing an example of a gauge visualization in Grafana.](/images/grafana/latest/userguide/images/viz/gauge_example.png)

## Value options

Use the following options to refine how your visualization displays the
value:

**Show**

Choose how Grafana displays your data.

_Calculate_

Show a calculated value based on all rows.

- **Calculation** – Select a reducer
  function that Grafana will use to reduce
  many fields to a single value. For a list of available
  calculations, refer to [Calculation types](v10-panels-calculation-types.md "v10-panels-calculation-types.md").
- **Fields** – Select the fields
  to display in the panel.

_All values_

Show a separate stat for every row. If you select this option, then you
can also limit the number of rows to display.

- **Limit** – The maximum number
  of rows to display. Default is 5,000.
- **Fields** – Select the fields
  to display in the panel.

## Gauge

Adjust how the gauge is displayed.

**Orientation**

Choose a stacking direction.

- **Auto** – Gauges display in rows
  and columns.
- **Horizontal** – Gauges display top
  to bottom.
- **Vertical** – Gauges display left
  to right.

**Show threshold labels**

Controls if threshold values are shown.

**Show threshold markers**

Controls if a threshold band is shown outside the inner gauge value
band.

**Gauge size**

Choose a guage size mode

- **Auto** – Grafana determines the
  best gauge size.
- **Manual** – Manually configure the
  gauge size.

**Min width**

Set the minimum width of vertically-oriented gauges.

If you set a minimum width, the x-axis scrollbar is automatically displayed when
there is a large amount of data.

###### Note

This option only applies when gauge size is set to manual.

**Min height**

Se the minimum height of horizontally-oriented gauges.

If you set a minimum height, the y-axis scrollbar is automatically displayed when
there is a large amount of data.

###### Note

This option only applies when gauge size is set to manual.

**Neutral**

Set the starting value from which every gauge will be filled.

## Text size

Adjust the sizes of the gauge text.

- **Title** – Enter a numeric
  value for the gauge title size.
- **Value** – Enter a numeric
  value for the gauge value size.
