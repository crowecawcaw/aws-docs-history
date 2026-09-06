

# Table panel
<a name="table-panel"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 8.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).

The table panel supports multiple modes for time series and for tables, annotation, and raw JSON data. This panel also provides date formatting, value formatting, and coloring options.

## Data and field options
<a name="data-and-field-options"></a>

With table visualizations you can apply the following options:
+  [Transformations](panel-transformations.md).
+  [Field options and overrides](field-options-overrides.md).
+  [Thresholds](thresholds.md).

## Display options
<a name="display-options"></a>
+  **Show header** – Show or hide column names imported from your data source.
+  **Sort ascending/descending** – Choose a column title to change the sort order from the default to descending to ascending. Each time you choose, the sort order changes to the next option in the cycle. You can sort by only one column at a time.
+  [Table field options](#table-field-options) – Change field options such as column width, alignment, and cell display mode.
+  [Filter table columns](#filter-table-columns) – Temporarily change how column data is displayed. For example, you can order values from highest to lowest or hide specific values.

## Annotation support
<a name="annotation-support"></a>

Annotations are not currently supported in the new table panel.

## Table field options
<a name="table-field-options"></a>

This section explains all available table field options. The options are listed in the same order as in Amazon Managed Grafana. Options listed in this topic apply only to table panel visualizations.

Most field options will not affect the visualization until you choose outside of the field option box that you are editing or press Enter.

For more information about applying these options, see [Configure all fields](field-options-overrides.md#configure-all-fields) and [Configure specific fields](field-options-overrides.md#configure-specific-fields).

### Column alignment
<a name="column-alignment"></a>

Choose how Amazon Managed Grafana should align cell contents:
+ Auto (default)
+ Left
+ Center
+ Right

### Column width
<a name="column-width"></a>

By default, Amazon Managed Grafana automatically calculates the column width based on the cell contents. In this field option, you can override the setting and define the width for all columns in pixels.

For example, if you enter `100` in the field, all the columns will be set to 100 pixels wide when you choose outside the field.

### Cell display mode
<a name="cell-display-mode"></a>

By default, Amazon Managed Grafana automatically chooses display settings. You can override the settings by choosing one of the following options to change all fields.

**Note**  
If you set these in the **Field** tab, the display modes apply to all fields, including the time field. Many options work best if you set them in the **Override** tab.

#### Color text
<a name="color-text"></a>

If thresholds are set, the field text is displayed in the appropriate threshold color.

#### Color background
<a name="color-background"></a>

If thresholds are set, the field background is displayed in the appropriate threshold color.

#### Gradient gauge
<a name="gradient-gauge"></a>

The threshold levels define a gradient.

#### LCD gauge
<a name="lcd-gauge"></a>

The gauge is split up in small cells that are lit or unlit.

#### JSON view
<a name="json-view"></a>

The value is shown formatted as code. If a value is an object, the JSON view that enables you to browse the JSON object appears when you pause on the value.

### Column filter
<a name="column-filter"></a>

## Filter table columns
<a name="filter-table-columns"></a>

If you turn on the **Column filter** in table options, you can filter table options. For more information, see [Table field options](#table-field-options).

### Turn on column filtering
<a name="turn-on-column-filtering"></a>

1. In Amazon Managed Grafana, choose the dashboard that shows the table with the columns that you want to filter.

1. On the table panel that you want to filter, [Opening the panel editor](AMG-panel-editor.md#open-the-panel-editor).

1. Choose the **Field** tab.

1. In **Table** options, turn on the **Column filter** option.

A filter icon appears next to each column title.

### Filter column values
<a name="filter-column-values"></a>

To filter column values, choose the filter (funnel) icon next to a column title. The Grafana workspace displays the filter options for that column.

Select the check boxes next to the values that you want to display. Enter text in the search field at the top to show those values in the display so that you can select them rather than scroll to find them.

### Clear column filters
<a name="clear-column-filters"></a>

Columns with filters applied have a blue funnel displayed next to the title.

To remove the filter, choose the blue funnel icon, and then choose **Clear filter**.