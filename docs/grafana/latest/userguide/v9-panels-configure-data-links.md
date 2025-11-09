# Configure data links

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can use data link variables or data links to create links between panels.

## Data link variables

You can use variables in data links to refer to series fields, labels, and values.
For more information about data links, see [Data links](#v9-panels-data-links "#v9-panels-data-links").

To see a list of available variables, type **$** in the data link
**URL** field to see a list of variables that you can
use.

###### Note

These variables changed in 6.4, so if you have an older version of Grafana, then
use the version picker to select docs for an older version of Grafana.

You can also use template variables in your data links URLs, see [Adding and managing dashboard variables](v9-dash-variables.md "v9-dash-variables.md").

## Time range panel

variables

These variables allow you to include the current time range in the data link URL.

- **\_\_url_time_range** - current dashboard’s time range
  (i.e. **?from=now-6h&to=now**)
- **$\_\_from and $\_\_to** - For more information, see [Global variables](v9-dash-variable-add.md#v9-dash-variable-add-global "v9-dash-variable-add.md#v9-dash-variable-add-global").

## Series variables

Series specific variables are available under **\_\_series**
namespace:

- **\_\_series.name** - series name to the URL

## Field variables

Field-specific variables are available under **\_\_field** namespace:

- **\_\_field.name** - the name of the field
- **\_\_field.labels.<LABEL>** - label’s value to the URL. If
  your label contains dots, then use
  **\_\_field.labels["<LABEL>"]** syntax.

## Value variables

Value-specific variables are available under **\_\_value** namespace:

- **\_\_value.time** - value’s timestamp (Unix ms epoch) to the URL
  (i.e. **?time=1560268814105**)
- **\_\_value.raw** - raw value
- **\_\_value.numeric** - numeric representation of a value
- **\_\_value.text** - text representation of a value
- **\_\_value.calc** - calculation name if the value is result of
  calculation

## Template variables

When linking to another dashboard that uses template variables, select variable
values for whoever clicks the link.

**${var-myvar:queryparam}** - where **var-myvar** is
the name of the template variable that matches one in the current dashboard that you
want to use.

| Variable state           | Result in the created URL             |
| ------------------------ | ------------------------------------- |
| selected one value       | **var-myvar=value1**                  |
| selected multiple values | **var-myvar=value1&var-myvar=value2** |
| selected **All**         | **var-myvar=All**                     |

If you want to add all of the current dashboard’s variables to the URL, then use
**${\_\_all_variables}**.

## Data links

Data links allow you to provide more granular context to your links. You can create
links that include the series name or even the value under the cursor. For example, if
your visualization showed four servers, you could add a data link to one or two of them.

The link itself is accessible in different ways depending on the visualization. For
the Graph you need to click on a data point or line, for a panel like Stat, Gauge, or
Bar Gauge you can click anywhere on the visualization to open the context menu.

You can use variables in data links to send people to a detailed dashboard with
preserved data filters. For example, you could use variables to specify a time range,
series, and variable selection. For more information, see [Data link variables](#v9-panels-data-link-variables "#v9-panels-data-link-variables").

### Typeahead suggestions

When creating or updating a data link, press Cmd+Space or Ctrl+Space on your
keyboard to open the typeahead suggestions to more easily add variables to your URL.

### Add a data link

1. Hover your cursor over the panel that you want to add a link to and then
   press **e**. Or click the dropdown arrow next to the panel
   title and then click **Edit**.
2. On the Field tab, scroll down to the Data links section.
3. Expand Data links and then click **Add
   link**.
4. Enter a **Title**. **Title** is a human-readable label for the link that will be
   displayed in the UI.
5. Enter the **URL** you want to link to.

You can even add one of the template variables defined in the dashboard.
Click in the **URL** field and then type
**$** or press Ctrl+Space or Cmd+Space to see a list of
available variables. By adding template variables to your panel link, the
link sends the user to the right context, with the relevant variables
already set. For more information, see [Data link variables](#v9-panels-data-link-variables "#v9-panels-data-link-variables"). 6. If you want the link to open in a new tab, then select **Open in a new tab**. 7. Click **Save** to save changes and close the
window. 8. Click **Save** in the upper right to save
your changes to the dashboard.

### Update a data link

1. On the Field tab, find the link that you want to make changes to.
2. Click the Edit (pencil) icon to open the Edit link window.
3. Make any necessary changes.
4. Click **Save** to save changes and close the
   window.
5. Click **Save** in the upper right to save
   your changes to the dashboard.

### Delete a data link

1. On the Field tab, find the link that you want to delete.
2. Click the **X** icon next to the link you
   want to delete.
3. Click **Save** in the upper right to save
   your changes to the dashboard.
