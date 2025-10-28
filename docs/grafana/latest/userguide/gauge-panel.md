# Gauge panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

**Gauge** is a single-value panel that can repeat a gauge for every
series, column, or row.

## Data and field options

Gauge visualizations allow you to apply the following options:

- [Transformations](panel-transformations.md "panel-transformations.md")
- [Field options and overrides](field-options-overrides.md "field-options-overrides.md")
- [Thresholds](thresholds.md "thresholds.md")

## Display options

To refine your visualization, use the following options:

- Show – Choose how Amazon Managed Grafana displays
  your data.
  - Calculate – Show a calculated
    **Value** based on all rows. For a list of
    available calculations, see [Calculations list](list-of-calculations.md "list-of-calculations.md").
  - All values – Show a separate
    stat for every row. If you select this option, you can also select a
    **Limit**, or the maximum number of rows to
    display.

- Orientation – Choose a stacking
  direction.
  - Auto – Amazon Managed Grafana selects what
    it thinks is the best orientation.
  - Horizontal – Bars stretch
    horizontally, left to right.
  - Vertical – Bars stretch
    vertically, top to bottom.

- Show threshold labels – Choose whether
  to show threshold values.
- Show threshold markers – Choose whether
  to show a threshold band outside the inner gauge value band.
