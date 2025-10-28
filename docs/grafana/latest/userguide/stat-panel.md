# Stat panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The stat panel shows a one large stat value with an optional graph sparkline. You can
control the background or value color by using thresholds.

By default, the stat panel shows one of the following displays:

- Only the value for a single series or field.
- Both the value and name for multiple series or fields.
  You can use the **Text mode** option to control whether the text is
  displayed or not.

## Data and field options

Stat visualizations allow you to apply the following options:

- [Transformations](panel-transformations.md "panel-transformations.md").
- [Field options and overrides](field-options-overrides.md "field-options-overrides.md").
- [Thresholds](thresholds.md "thresholds.md").

## Automatic layout

adjustment

The panel automatically adjusts the layout depending on available width and
height in the dashboard. It automatically hides the graph (sparkline) if the panel
becomes too small.

## Display options

Use the following options to refine your visualization:

- Show – Choose how Amazon Managed Grafana displays
  your data.
  - Calculate – Show a calculated
    value based on all rows.
    - Calculation – Select a
      calculation to apply. For information about available
      calculations, see [Calculations list](list-of-calculations.md "list-of-calculations.md").

  - All values – Show a separate
    stat for each row.
    - Limit – Specify the
      maximum number of rows to display.

- Fields – Select a field name or a field
  type (including **All fields** or **Numeric
  fields**) to include in this panel.
- Value – Select a reducer function that
  Amazon Managed Grafana will use to reduce many fields to a single value. Choose the
  **Value** list to see functions and brief descriptions.
- Orientation – Choose a stacking
  direction.
  - Auto – Amazon Managed Grafana selects what
    it thinks is the best orientation.
  - Horizontal – Bars stretch
    horizontally, left to right.
  - Vertical – Bars stretch
    vertically, top to bottom.

- Text mode – You can use the
  **Text mode** option to control what text the panel
  displays. If only the name and color are important, and the value is not,
  change the **Text mode** to **Name**. The
  value is still used to determine color and is displayed in a tooltip.
  - Auto – If the data contains
    multiple series or fields, show both the name and the value.
  - Value – Show only the value,
    never the name. The name is displayed in tooltip.
  - Value and name – Always show
    the value and the name.
  - Name – Show the name instead of
    the value. The value is displayed in the tooltip.
  - None – Show nothing (empty).
    The name and the value are displayed in the tooltip.

- Color mode – Choose a color mode.
  - Value – Colors only the value
    and graph area.
  - Background – Colors the
    background as well.

- Graph mode – Choose a graph mode.
  - None – Hides the graph and
    shows only the value.
  - Area – Shows the area graph
    below the value. This option requires that your query returns a time
    column.

- Alignment mode – Choose an alignment
  mode.
  - Auto – If only a single value
    is shown (no repeat), the value is centered. If multiple series or
    rows are shown, the value is left-aligned.
  - Center – Stat value is
    centered.
