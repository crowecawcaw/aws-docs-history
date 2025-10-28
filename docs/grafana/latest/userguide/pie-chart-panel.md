# Pie chart panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The pie chart displays reduced series, or values in a series, from one or more
queries, as they relate to each other, as slices of a pie. The arc length, area, and
central angle of a slice are all proportional to the slices value, as it relates to the
sum of all values. This type of chart is best used when you want a quick comparison of a
small set of values in an aesthetically pleasing form.

Pie chart visualizations allow you to apply the following options:

- [Transformations](panel-transformations.md "panel-transformations.md").
- [Field options and overrides](field-options-overrides.md "field-options-overrides.md").
- [Thresholds](thresholds.md "thresholds.md").

## Options

You can use the following options to refine your visualization.

- Show – Choose how much information to
  show. **Calculate** reduces each value to a single value
  per series. **All values** displays every value from a
  single series.
- Calculation – Select a calculation to
  reduce each series when **Calculate** has been selected.
  For information about available calculations, see [Calculations list](list-of-calculations.md "list-of-calculations.md").
- Limit – When displaying every value
  from a single series, this limits the number of values displayed.
- Fields – Select which fields to display
  in the visualization.
  - **Numeric fields** – All fields
    with numeric values.
  - **All fields** – All fields
    that are not removed by transformations.
  - **Time** – All fields with time
    values.

## Labels

Select labels to display on the pie chart. You can select more than one.

- Name – The series or field name.
- Percent – The percentage of the whole.
- Value – The raw numerical value.

Labels are displayed in white over the body of the chart. You might need to select
darker chart colors to make them more visible. Long names or numbers might be
clipped.

## Legend placement and values

Choose where to display the legend.

- Bottom – Below the chart.
- Right – To the right of the chart.

You can select more than one value to display in the legend.
**Percent** is the percentage of the whole and
**Value** is the raw numerical value.
