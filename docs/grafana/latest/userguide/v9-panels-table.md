# Table panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The table panel visualization is very flexible, supporting multiple modes for time
series and for tables, annotation, and raw JSON data. This panel also provides date
formatting, value formatting, and coloring options.

## Sort column

Click a column title to change the sort order from default to descending to
ascending. Each time you click, the sort order changes to the next option in the
cycle. You can only sort by one column at a time.

## Table options

**Show header**

Show or hide column names imported from your data source.

## Column width

By default, Grafana automatically calculates the column width based on the table
size and the minimum column width. This field option can override the setting and
define the width for all columns in pixels.

For example, if you enter `100` in the field, then when you click
outside the field, all the columns will be set to 100 pixels wide.

## Minimum column width

By default, the minimum width of the table column is 150 pixels. This field option
can override that default and will define the new minimum column width for the table
panel in pixels.

For example, if you enter `75` in the field, then when you click
outside the field, all the columns will scale to no smaller than 75 pixels
wide.

For small-screen devices, such as smartphones or tablets, reduce the default
`150` pixel value to `50` to allow table based panels to
render correctly in dashboards.

## Column alignment

Choose how Grafana should align cell contents:

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

**Basic**

The basic mode will show a simple gauge with the threshold levels defining the
color of gauge.

**Gradient**

The threshold levels define a gradient.

**LCD**

The gauge is split up in small cells that are lit or unlit.

**JSON view**

Shows value formatted as code. If a value is an object the JSON view allowing
browsing the JSON object will appear on hover.

## Cell value inspect

Enables value inspection from table cell. The raw value is presented in a modal
window.

###### Note

Cell value inspection is only available when cell display mode is set to Auto,
Color text, Color background or JSON View.

## Column filter

You can temporarily change how column data is displayed. For example, you can
order values from highest to lowest or hide specific values. For more information,
refer to [Filter table columns](#v9-panels-table-filter "#v9-panels-table-filter"),
below.

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

A filter icon appears next to each column title.

**Filter column values**

To filter column values, choose the filter (funnel) icon next to a column title.
Grafana displays the filter options for that column.

Choose the check box next to the values that you want to display. Enter text in
the search field at the top to show those values in the display so that you can
select them rather than scroll to find them.

**Clear column filters**

Columns with filters applied have a blue funnel displayed next to the
title.

To remove the filter, choose the blue funnel icon and then select Clear
filter.

## Table footer

You can use the table footer to show [calculations](v9-panels-calculation-types.md "v9-panels-calculation-types.md") on fields.

After you enable the table footer, you can select the
**Calculation**, and then the **Fields** that
you want to calculate.

The system applies the calculation to all numeric fields if you do not select a
field.

**Count rows**

If you want to show the number of rows in the dataset instead of the number of
values in the selected fields, select the **Count** calculation and
enable **Count rows**.
