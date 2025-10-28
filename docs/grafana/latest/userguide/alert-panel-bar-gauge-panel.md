# Bar gauge panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The bar gauge simplifies your data by reducing every field to a single value. You
choose how Amazon Managed Grafana calculates the reduction.

This panel can show one or more bar gauges depending on how many series, rows, or
columns your query returns.

## Data and field options

With Bar gauge visualizations, you can apply the following options:

- [Transformations](panel-transformations.md "panel-transformations.md")
- [Field options and overrides](field-options-overrides.md "field-options-overrides.md")
- [Thresholds](thresholds.md "thresholds.md")

## Display options

Use the following options to refine your visualization:

- Show – Choose how Amazon Managed Grafana displays
  your data.
  - Calculate – Show a calculated
    value based on all rows. For a list of available calculations, see
    [Calculations list](list-of-calculations.md "list-of-calculations.md").
  - All values – Show a separate
    stat for every row. If you select this option, you can also select a
    **Limit**, or the maximum number of rows to
    display.

- Value – Select a reducer function that
  Amazon Managed Grafana will use to reduce many fields to a single value. Choose the
  **Value** list to see functions and brief descriptions.
- Orientation – Choose a stacking
  direction.
  - Auto – Amazon Managed Grafana selects what
    the orientation that it thinks fits best.
  - Horizontal – Bars stretch
    horizontally, left to right.
  - Vertical – Bars stretch
    vertically, top to bottom.

- Display mode – Choose a display mode.
  - Gradient – Choose a threshold
    level to define a gradient.
  - Retro LCD – Display the gauge
    split into small cells that are lit or unlit.
  - Basic – Use a single color
    based on the matching threshold.

- Show unfilled area – Select this option
  if you want to render the unfilled region of the bars as dark gray. This
  option is not available for the Retro LCD display mode.
