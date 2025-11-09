# Configure standard options

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The data model used in Grafana is a columnar-oriented table structure that unifies
both time series and table query results. Each column within this structure is called
a _field_. A field can represent a single time series or table
column.

Field options allow you to change how the data is displayed in your visualizations.
Options and overrides that you apply do not change the data, they change how Grafana
displays the data. When you change an option, it is applied to all fields, meaning all
series or columns. For example, if you change the unit to percentage, then all fields
with numeric values are displayed in percentages.

A complete list of field formatting options is included later in this topic.

###### Note

You can apply standard options to most built-in Grafana panels. Some older
panels and community panels that have not updated to the new panel and data model
will be missing either all or some of these field options.

###### To configure standard options

1. Open a dashboard. Hover over any part of the panel to display the actions
   menu at the top right corner of the dashboard.
2. From the actions menu, choose **Edit**.
3. In the panel display options pane, locate the **Standard
   options** section.
4. Select the standard options you want to apply.
5. To preview your change, select outside of the field option box you are
   editing or press **Enter**.
   **Standard options definitions**

This section explains all available standard options.

You can apply standard options to most built-in Grafana panels. Some older panels and
community panels that have not updated to the new panel and data model will be missing
either all or some of these field options.

Most field options will not affect the visualization until you click outside of the
field option box you are editing or press **Enter**.

###### Note

Grafana Labs is constantly working to add and expand options for all
visualization, so all options might not be available for all visualizations.

## Unit

Lets you choose what unit a field should use. Choose the
**Unit** field, then drill down until you find the unit you
want. The unit you select is applied to all fields except time.

### Custom units

You can use the unit dropdown to also specify custom units, custom prefix or
suffix and date time formats.

To select a custom unit enter the unit and select the last **Custom:
xxx** option in the dropdown.

- **suffix:<suffix>** for a custom unit that
  should go after the value.
- **prefix:<prefix>** for a custom unit that
  should go before the value.
- **time:<format>** For custom date time
  formats, type for example `time:YYYY-MM-DD`. See [format](https://momentjs.com/docs/#/displaying/ "https://momentjs.com/docs/#/displaying/") in
  the _Moment.js Documentation_ for the format
  syntax and options.
- **si:<base scale><unit characters>**
  for custom SI units. For example: `si: mF`. This is a
  bit more advanced as you can specify both a unit and the source
  data scale. So if your source data is represented as milli (thousands
  of) something prefix the unit with that SI scale character.
- **count:<unit>** for a custom count
  unit.
- **currency:<unit>** for custom a currency
  unit.

You can also paste a native emoji in the unit picker and pick it as a custom
unit.

### String units

Grafana can sometimes be too aggressive in parsing strings and displaying
them as numbers. To configure Grafana to show the original string value,
create a field override and add a unit property with the
**String** unit.

### Scale units

By default, Grafana automatically scales the unit based on the magnitude
of the value. For example, if you have a value of 0.14 kW, Grafana will
display it as 140 W. Another example is that 3000 kW will be displayed as
three MW. If you want to disable this behavior, you can turn off the
**Scale units** switch.

## Min

Lets you set the minimum value used in percentage threshold calculations. Leave
blank to automatically calculate the minimum.

## Max

Lets you set the maximum value used in percentage threshold calculations. Leave
blank to automatically calculate the maximum.

## Field min/max

By default the calculated min and max will be based on the minimum and maximum,
in all series and fields. Turning field min/max on will calculate the min or max
on each field individually, based on the minimum or maximum of that field.

## Decimals

Specify the number of decimals Grafana includes in the rendered value. If you
leave this field blank, Grafana automatically truncates the number of decimals
based on the value. For example 1.1234 will display as 1.12 and 100.456 will
display as 100.

To display all decimals, set the unit to **String**.

## Display name

Lets you set the display title of all fields. You can use [variables](v10-dash-variables.md "v10-dash-variables.md") in the field title.

When multiple stats, fields, or series are shown, this field controls the title
in each stat. You can use expressions like **${\_\_field.name}** to
use only the series name or the field name in the title.

Given a field with a name of `Temp`, and labels of
`{"Loc"="PBI", "Sensor"="3"}`:

| Expression syntax            | Example                 | Renders to                     | Explanation                                                                                                                                                                                                                 |
| ---------------------------- | ----------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `${__field.displayName}`     | Same as syntax          | `Temp {Loc="PBI", Sensor="3"}` | Displays the field name, and labels in `{}`<br>if they are present. If there is only one label key in the response,<br>then for the label portion, Grafana displays the value of the label<br>without the enclosing braces. |
| `${__field.name}`            | Same as syntax          | `Temp`                         | Displays the name of the field (without labels).                                                                                                                                                                            |
| `${__field.labels}`          | Same as syntax          | `Loc="PBI", Sensor="3"`        | Displays the labels without the name.                                                                                                                                                                                       |
| `${__field.labels.`X`}`      | `${__field.labels.Loc}` | `PBI`                          | Displays the value of the specified label key.                                                                                                                                                                              |
| `${__field.labels.__values}` | Same as Syntax          | `PBI, 3`                       | Displays the values of the labels separated by a comma (without<br>label keys).                                                                                                                                             |

If the value is an empty string after rendering the expression for a particular
field, then the default display method is used.

## Color scheme

The color options and their effect on the visualization depends on the
visualization you are working with. Some visualizations have different color
options.

You can specify a single color, or select a continuous (gradient) color scheme,
based on a value. Continuous color interpolates a color using the percentage of a
value relative to min and max.

Select one of the following palettes:

| Color mode                           | Description                                                                                                                                                    |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Single color**                     | Specify a single color, useful in an override rule                                                                                                             |
| **Shades of a color**                | Selects shades of a single color, useful in an override rule                                                                                                   |
| **From thresholds**                  | Informs Grafana to take the color from the matching threshold                                                                                                  |
| **Classic palette**                  | Grafana will assign color by looking up a color in a palette by<br>series index. Useful for Graphs and pie charts and other categorical<br>data visualizations |
| **Classic palette (by series name)** | Grafana will assign color based on the name of the series.<br>Useful when the series names to be vsiualized depend on the<br>available data.                   |
| **Green-Yellow-Red (by value)**      | Continuous color scheme                                                                                                                                        |
| **Red-Yellow-Green (by value)**      | Continuous color scheme                                                                                                                                        |
| **Blue-Yellow-Red (by value)**       | Continuous color scheme                                                                                                                                        |
| **Yellow-Red (by value)**            | Continuous color scheme                                                                                                                                        |
| **Blue-Purple (by value)**           | Continuous color scheme                                                                                                                                        |
| **Yellow-Blue (by value)**           | Continuous color scheme                                                                                                                                        |
| **Blues (by value)**                 | Continuous color scheme (panel background to blue)                                                                                                             |
| **Reds (by value)**                  | Continuous color scheme (panel background color to red)                                                                                                        |
| **Greens (by value)**                | Continuous color scheme (panel background color to green)                                                                                                      |
| **Purple (by value)**                | Continuous color scheme (panel background color to purple)                                                                                                     |

## No value

Enter what Grafana should display if the field value is empty or null. The
default value is a hyphen (-).
