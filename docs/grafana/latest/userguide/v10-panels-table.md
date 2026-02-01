# Table

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Tables are very flexible, supporting multiple modes for time series and for tables,
annotation, and raw JSON data. This visualization also provides date formatting, value
formatting, and coloring options.

![An image showing an example of a table visualization in Grafana.](/images/grafana/latest/userguide/images/viz/table_example.png)

###### Note

Annotations and alerts are not supported in tables.

## Sort column

Choose a column title to change the sort order from default to descending to
ascending. Each time you select the column, the sort order changes to the next
option in the cycle. You can sort on multiple columns by holding the
`shift` key when selecting additional columns.

## Table options

**Show header**

Show or hide column names imported from your data source.

## Column width

By default, Grafana automatically calculates the column width based on the table
size and the minimum column width. This field option can override the setting and
define the width for all columns in pixels.

For example, if you enter `100`, all the columns will be set to 100
pixels wide (the change takes place when you exit the field).

## Minimum column width

By default, the minimum width of the table column is 150 pixels. This field option
can override that default and will define the new minimum column width for the table
panel in pixels.

For example, if you set the minimum to `75`, all the columns will
scale to no smaller than 75 pixels wide.

For small-screen devices, such as smartphones or tablets, you can reduce the
default `150` pixel value to `50` to allow table based panels
to render correctly in dashboards.

## Column alignment

Choose how Grafana should align cell contents.

- Auto (default)
- Left
- Center
- Right

## Cell type

By default, Grafana automatically chooses display settings. You can override the
settings by choosing one of the following options to set the default for all fields.
Additional configuration is available for some cell types.

###### Note

If you set these in the **Field** tab, then the type will
apply to all fields, including the time field. You can set them in the
**Override** tab to apply the change to one or more
fields.

**Color text**

If thresholds are set, then the field text is displayed in the appropriate
threshold color.

**Color background (gradient or solid)**

If thresholds are set, then the field background is displayed in the appropriate
threshold color.

**Gauge**

Cells can be displayed as a graphical gauge, with several different presentation
types.

- _Basic_ – The basic mode will show a simple
  gauge with the threshold levels defining the color of gauge.
- _Gradient_ – The threshold levels define a
  gradient.
- _LCD_ – The gauge is split up in small cells
  that are lit or unlit.

Additionally, labels displayed alongside the gauges can be set to be colored by
value, match the theme text color, or be hidden.

- **Value color**
- **Text color**
- **Hidden**

**JSON view**

Shows value formatted as code. If a value is an object the JSON view allowing
browsing the JSON object will appear on hover.

**Sparkline**

Shows values rendered as a sparkline. Requires [time series to table](v10-panels-xform-functions.md#v10-panels-xform-funcs-series "v10-panels-xform-functions.md#v10-panels-xform-funcs-series") data
transform.

## Cell value inspect

Enables value inspection from table cell. The raw value is presented in a modal
window.

###### Note

Cell value inspection is only available when cell display mode is set to Auto,
Color text, Color background, or JSON View.

## Column filter

You can temporarily change how column data is displayed. For example, you can
order values from highest to lowest or hide specific values. For more information,
see [Filter table columns](#v10-panels-table-filter "#v10-panels-table-filter").

## Pagination

Use this option to enable or disable pagination. It is a front-end option that
does not affect queries. When enabled, the page size automatically adjusts to the
height of the table.

## Filter table columns

If you turn on the **Column filter**, then you can filter table
options.

###### To turn on column filtering

1. In Grafana, navigate to the dashboard with the table with the columns that
   you want to filter.
2. On the table panel you want to filter, open the panel editor.
3. Choose the **Field** tab.
4. In **Table** options, turn on the **Column
   filter** option.

A filter (funnel) icon appears next to each column title.

**Filter column values**

To filter column values, choose the filter (funnel) icon next to a column title.
Grafana displays the filter options for that column.

Choose the check box next to the values that you want to display. Enter text in
the search field at the top to show those values in the display so that you can
select them rather than scroll to find them.

Select from several operators to display column values:

- **Contains** – Matches a regex pattern (operator
  by default).
- **Expression** – Evaluates a Boolean expression.
  The character `$` represents the column value in the expression
  (for example, `$ >= 10 ≈& $ <= 12`).
- **Comparison operators** – You can use the
  typical comparison operators: `=`, `!=`,
  `<`, `<=`, `>`,
  `>=`.

Choose the checkbox above the **Ok** and
**Cancel** buttons to add or remove all displayed values from the
filter.

**Clear column filters**

Columns with filters applied have a blue funnel displayed next to the
title.

To remove the filter, choose the blue funnel icon and then select **Clear
filter**.

## Table footer

You can use the table footer to show [calculations](v10-panels-calculation-types.md "v10-panels-calculation-types.md") on fields.

After you enable the table footer, you can select the
**Calculation**, and then the **Fields** that
you want to calculate.

The system applies the calculation to all numeric fields if you do not select a
field.

**Count rows**

If you want to show the number of rows in the dataset instead of the number of
values in the selected fields, select the **Count** calculation and
enable **Count rows**.
