# Gauge panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Gauge is a single-value visualization that can repeat a gauge for every series, column
or row.

**Value options**

Use the following options to refine how your visualization displays the
value:

**Show**

Choose how Grafana displays your data.

**Calculate**

Show a calculated value based on all rows.

- **Calculation** – Select a reducer
  function that Grafana will use to reduce
  many fields to a single value. For a list of available
  calculations, refer to [Calculation types](v9-panels-calculation-types.md "v9-panels-calculation-types.md").
- **Fields** – Select the fields
  to display in the panel.
  **All values**

Show a separate stat for every row. If you select this option, then you
can also limit the number of rows to display.

- **Limit** – The maximum number
  of rows to display. Default is 5,000.
- **Fields** – Select the fields
  to display in the panel.
  **Gauge**

Adjust how the gauge is displayed.

- **Show threshold labels** –
  Controls if threshold values are shown.
- **Show threshold markers** –
  Controls if a threshold band is shown outside the inner gauge value
  band.
  **Text size**

Adjust the sizes of the gauge text.

- **Title** – Enter a numeric
  value for the gauge title size.
- **Value** – Enter a numeric
  value for the gauge value size.
