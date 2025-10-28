# Configure data links

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Data links allow you to provide more granular context to your links. You can create
links that include the series name or even the value under the cursor. For example, if
your visualization shows four servers, you can add a datalink to one or two of them.
You can also link panels using data links.

The link itself is accessible in different ways depending on the visualization. For
the time series visualization, for example, you choose a data point or line. For large
area visualizations, like stat, gauge, or bar gauge, you can choose anywhere on the
visualization to open the context menu.

If there is only one data link in the visualization, choosing anywhere on the
visualization opens the link rather than the context menu.

**Supported visualizations**

- Bar chart
- Bar gauge
- Candlestick
- Canvas
- Gauge
- Geomap
- Heatmap
- Histogram
- Pie chart
- Stat
- State timeline
- Status history
- Table
- Time series
- Trend

## Data link variables

Variables in data links let you send people to a detailed dashboard with
preserved data filters. For example, you could use variable to specify a label,
time range, series, or variable selection.

To see a list of available variables, type `$` in the data link
**URL** field.

You can also use template variables in your data links URLs, see [Variables](v10-dash-variables.md "v10-dash-variables.md").

### Time range panel

variables

These variables allow you to include the current time range in the data link URL.

- `__url_time_range` – current dashboard’s time range
  (i.e. `?from=now-6h&to=now`)
- `$__from` – For more information, see [Global variables](v10-dash-variable-add.md#v10-dash-variable-add-global "v10-dash-variable-add.md#v10-dash-variable-add-global").
- `$__to` – For more information, see [Global variables](v10-dash-variable-add.md#v10-dash-variable-add-global "v10-dash-variable-add.md#v10-dash-variable-add-global").

### Series variables

Series specific variables are available under `__series`
namespace:

- `__series.name` – series name to the URL

### Field variables

Field-specific variables are available under `__field` namespace:

- `__field.name` – the name of the field
- `__field.labels.<LABEL>` – label’s value to the URL. If
  your label contains dots, then use
  `__field.labels["<LABEL>"]` syntax.

### Value variables

Value-specific variables are available under `__value` namespace:

- `__value.time` – value’s timestamp (Unix ms epoch)
  to the URL (i.e. `?time=1560268814105`)
- `__value.raw` – raw value
- `__value.numeric` – numeric representation of a value
- `__value.text` – text representation of a value
- `__value.calc` – calculation name if the value is
  result of calculation

Using value-specific variable in data links can show different result
depending on the set option of Tooltip mode.

### Data variables

To access values from other fields use:

- `__data.fields[i]` – Value of field `i`
  (on the same row).
- `__data.fields["NameOfField"]` – Value of field
  using name instead of index.
- `__data.fields[i].labels.cluster` – Access the
  labels of another field.

### Template variables

When linking to another dashboard that uses template variables, select variable
values for whoever clicks the link.

`${var-myvar:queryparam}` – where `var-myvar`
is the name of the template variable that matches one in the current
dashboard that you want to use.

| Variable state           | Result in the created URL           |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| selected one value       | `var-myvar=value1`                  |
| selected multiple values | `var-myvar=value1&var-myvar=value2` |
| selected `All`           | `var-myvar=All`                     | If you want to add all of the current dashboard’s variables to the URL, then use `${__all_variables}`. ## Adding a data link You can add data links to your panels. 1. Navigate to the panel to which you want to add the data link. 2. Hover over the panel to display the menu icon in the upper-right corner. 3. From the menu, choose **Edit** to open the panel editor. 4. In the **Panel edit** pane, scroll down to the **Data links** section and expand it. 5. Choose **Add link**. 6. In the dialog box that opens, enter a **Title**. This is a human-readable label for the link, which will be displayed in the UI. 7. Enter the **URL** or variable you want to link to. To add a data link variable, select the **URL** field and then enter `$` or press Ctrl+Space or Cmd+Space to see a list of available variables. 8. If you want the link to open in a new tab, then select **Open in a new tab**. 9. Choose **Save** to save changes and close the dialog box. 10. Save your changes to the dashboard. |
