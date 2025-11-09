# Field options and overrides

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

This section explains what field options and field overrides in Amazon Managed Grafana are and how
to use them.

The data model used in Grafana workspaces, the data frame, is a columnar-oriented
table structure that unifies both time series and table query results. Each column
within this structure is called a _field_. A field can represent a
single time series or table column.

Field options allow you to change how the data is displayed in your visualizations.
Options and overrides that you apply do not change the data, they change how Amazon Managed Grafana
displays the data.

## Field options

_Field options_, both standard and custom, can be found on the
**Field** tab in the panel editor. Changes that are made on
this tab apply to all fields (that is, series and columns). For example, if you
change the unit to percentage, all fields with numeric values are displayed in
percentages. Learn how to apply a field option in [Configure all fields](#configure-all-fields "#configure-all-fields").

## Field overrides

_Field overrides_ can be added on the
**Overrides** tab in the panel editor. There you can add the
same options as you find on the **Field** tab, but they are applied
only to specific fields. Learn how to apply an override in [Configure specific fields](#configure-specific-fields "#configure-specific-fields").

## Available field options and

overrides

Field option types are common to both field options and field overrides. The only
difference is whether the change will apply to all fields (applied on the
**Field** tab) or to a subset of fields (applied on the
**Overrides** tab).

- [Standard field options](#standard-field-options "#standard-field-options") apply to all panel
  visualizations that allow transformations.
- [Table field options](table-panel.md#table-field-options "table-panel.md#table-field-options")
  apply only to table panel visualizations.

### Configure all fields

To change how all fields display data, you can change an option on the
**Field** tab. On the **Overrides** tab,
you can then override the field options for specific fields. For more
information, see [Configure specific fields](#configure-specific-fields "#configure-specific-fields").

For example, you can change the number of decimal places shown in all fields
by changing the **Decimals** option. For more
information about options, see [Standard field options](#standard-field-options "#standard-field-options") and [Table field options](table-panel.md#table-field-options "table-panel.md#table-field-options").

#### Change a field option

You can change as many options as you want to.

###### To change a field option

1. Choose the panel that you want to edit, choose the panel title,
   and then choose **Edit**.
2. Choose the **Field** tab.
3. Find the option that you want to change. You can define the
   following:
   - [Standard field options](#standard-field-options "#standard-field-options"), which apply to
     all panel visualizations that allow transformations.
   - [Table field options](table-panel.md#table-field-options "table-panel.md#table-field-options"), which only apply
     to table panel visualizations.

4. Add options by adding values in the fields. To return options to
   default values, delete the white text in the fields.
5. When you have finished making edits to the dashboard, choose
   **Save**.

#### Field option example

Let’s assume that the result set is a data frame that consists of two
fields: time and temperature.

| time                | temperature |
| ------------------- | ----------- |
| 2020-01-02 03:04:00 | 45.0        |
| 2020-01-02 03:05:00 | 47.0        |
| 2020-01-02 03:06:00 | 48.0        |

Each field (column) of this structure can have field options applied in a
way that alter the way its values are displayed. For example, you can set
the Unit to Temperature > Celsius, resulting in the following table.

| time                | temperature |
| ------------------- | ----------- |
| 2020-01-02 03:04:00 | 45.0 °C     |
| 2020-01-02 03:05:00 | 47.0 °C     |
| 2020-01-02 03:06:00 | 48.0 °C     |

The decimal place doesn’t mean anything in this case. You can change the
Decimals from `auto` to zero (`0`), resulting in the
following table.

| time                | temperature |
| ------------------- | ----------- |
| 2020-01-02 03:04:00 | 45 °C       |
| 2020-01-02 03:05:00 | 47 °C       |
| 2020-01-02 03:06:00 | 48 °C       |

### Configure specific fields

You can use overrides to change the settings for one or more fields. Field
options for overrides are exactly the same as the field options that are
available in a particular visualization. The only difference is that you choose
which fields to apply them to.

For example, you can change the number of decimal places shown in all numeric
fields or columns by changing the **Decimals**
option for **Fields with type** that matches
**Numeric**. For more information about
options, see [Standard field options](#standard-field-options "#standard-field-options"), which apply to all panel
visualizations that allow transformations, and [Table field options](table-panel.md#table-field-options "table-panel.md#table-field-options"), which
apply only to table panel visualizations.

#### Add a field override

You can override as many field options as you want to.

###### To add a field override

1. Choose the panel that you want to edit, choose the panel title,
   and then choose **Edit**.
2. Choose the **Overrides** tab.
3. Choose **Add an override for**.
4. Select the fields to which you want to apply an override rule.
   - Fields with name – Use
     this to select a field from the list of all available
     fields. Properties that you add to a rule with this selector
     are applied only to this single field.
   - Fields with name matching
     regex – Use this to specify fields to
     override with a regular expression. Properties that you add
     to a rule by using this selector are applied to all fields
     where the field names match the regex.
   - Fields with type – Use
     this to select fields by type, such as string, numeric, and
     so on. Properties that you add to a rule with this selector
     are applied to all fields that match the selected type.

5. Choose **Add override property**.
6. Select the field option that you want to apply.
7. Enter options by adding values in the fields. To return options
   to default values, delete the white text in the fields.
8. Continue to add overrides to this field by choosing **Add
   override property**, or you can choose **Add
   override** and select a different field to add
   overrides to.
9. When finished, choose **Save**.

#### Delete a field override

1. Choose
   the Overrides tab that contains the override that you want to
   delete.
2. Choose the trash can icon next to the override.

#### Field override example

Let’s assume that our result set is a data frame that consists of four
fields: time, high temp, low temp, and humidity.

| time                | high temp | low temp | humidity |
| ------------------- | --------- | -------- | -------- |
| 2020-01-02 03:04:00 | 45.0      | 30.0     | 67       |
| 2020-01-02 03:05:00 | 47.0      | 34.0     | 68       |
| 2020-01-02 03:06:00 | 48.0      | 31.0     | 68       |

Let’s apply the field options from the [Field option example](#field-option-example "#field-option-example") to
apply the Celsius unit and get rid of the decimal place. This results in the
following table.

| time                | high temp | low temp | humidity |
| ------------------- | --------- | -------- | -------- |
| 2020-01-02 03:04:00 | 45 °C     | 30 °C    | 67 °C    |
| 2020-01-02 03:05:00 | 47 °C     | 34 °C    | 68 °C    |
| 2020-01-02 03:06:00 | 48 °C     | 31 °C    | 68 °C    |

The temperature fields look good, but the humidity is nonsensical. You
can fix this by applying a field option override to the humidity field and
changing the unit to Misc > percent (0-100). This results in a table that
makes a lot more sense.

| time                | high temp | low temp | humidity |
| ------------------- | --------- | -------- | -------- |
| 2020-01-02 03:04:00 | 45 °C     | 30 °C    | 67%      |
| 2020-01-02 03:05:00 | 47 °C     | 34 °C    | 68%      |
| 2020-01-02 03:06:00 | 48 °C     | 31 °C    | 68%      |

### Standard field options

This section explains the available field options. They are listed in
alphabetical order.

You can apply standard field options to most built-in Grafana workspace
panels. Some older panels and community panels that have not updated to the new
panel and data model will be missing either all or some of these field options.

Most field options will not affect the visualization until you choose outside
of the field option box you are editing or press Enter.

For more information about applying these options, see the following
sections:

- [Configure all fields](#configure-all-fields "#configure-all-fields")
- [Configure specific fields](#configure-specific-fields "#configure-specific-fields")

#### Decimals

This option sets the number of decimals to include when rendering a
value. Leave empty for Amazon Managed Grafana to use the number of decimals provided by
the data source.

To change this setting, enter a number in the field.

#### Data links

This option controls the URL to which a value or visualization links. For
more information and instructions, see [Data links](data-links.md "data-links.md").

#### Display name

This option sets the display title of all fields. You can use variables
in the field title. For more information about templating and template
variables, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

When multiple stats, fields, or series are shown, this field controls the
title in each stat. You can use expressions such as
`${__field.name}` to use only the series name or the field
name in the title.

Given a field with a name of Temp, and labels of
{"Loc"="PBI",
"Sensor"="3"}

| Expression syntax            | Example                 | Renders to                        | Explanation                                                                                                                                                                                                                               |
| ---------------------------- | ----------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `${__field.displayName}`     | Same as syntax          | `Temp {Loc="PBI",<br>Sensor="3"}` | Displays the field name and labels in `{}` if<br>they are present. If there is only one label key in the<br>response, then for the label portion, Amazon Managed Grafana displays the<br>value of the label without the enclosing braces. |
| `${__field.name}`            | Same as syntax          | `Temp`                            | Displays the name of the field (without labels).                                                                                                                                                                                          |
| `${__field.labels}`          | Same as syntax          | `Loc="PBI", Sensor="3"`           | Displays the labels without the name.                                                                                                                                                                                                     |
| `${__field.labels.X}`        | `${__field.labels.Loc}` | `PBI`                             | Displays the value of the specified label key.                                                                                                                                                                                            |
| `${__field.labels.__values}` | Same as Syntax          | `PBI, 3`                          | Displays the values of the labels separated by a comma<br>(without label keys).                                                                                                                                                           |

If the value is an empty string after rendering the expression for a
particular field, the default display method is used.

#### Max

This option sets the maximum value used in percentage threshold
calculations. For automatic calculation based on all series and fields,
leave this setting blank.

#### Min

This option sets the minimum value used in percentage threshold
calculations. For automatic calculation based on all series and fields,
leave this setting blank.

#### No value

Enter what Amazon Managed Grafana should display if the field value is empty or null.

#### Unit

This option specifies the unit that a field should use. Choose the
**Unit** field, then drill down until you find the unit
that you want. The unit that you select is applied to all fields except
time.

##### Custom units

You can also use the unit dropdown list to specify custom units,
custom prefix or suffix, and date/time formats.

To select a custom unit, enter the unit and select the last
`Custom: xxx` option in the dropdown list.

- `suffix:<suffix>` for custom unit that should
  go after value.
- `time:<format>` for custom date/time formats;
  for example, `time:YYYY-MM-DD`. For the format syntax
  and options, see [Display](https://momentjs.com/docs/#/displaying/ "https://momentjs.com/docs/#/displaying/").
- `si:<base scale><unit characters>` for
  custom SI units; for example, `si: mF`. This option
  is a bit more advanced because you can specify both a unit and
  the source data scale. For example, if your source data is
  represented as milli (thousands of) unit, prefix the unit with
  that SI scale character.
- `count:<unit>` for a custom count unit.
- `currency:<unit>` for custom a currency unit.

You can also paste a native emoji in the unit picker and pick it as a
custom unit.

##### String units

Amazon Managed Grafana can sometimes parse strings and show them as numbers. To
make Amazon Managed Grafana show the original string, create a field override and add
a unit property with the `string` unit.

#### Color scheme

The field color option defines how Amazon Managed Grafana colors series or fields.
There are multiple modes here that work differently, and their utility
depends largely on the currently selected visualization.

Continuous color modes use the percentage of a value relative to min and
max to interpolate a color.

- Single color – Specific color
  set by using the color picker. This is most useful from an override
  rule.
- From thresholds – Color derived
  from the matching threshold. This is useful for gauges, stat, and
  table visualizations.

##### Color by series

Amazon Managed Grafana includes color schemes that define color by series. This is
useful for graphs and pie charts, for example.

##### Color by value

Amazon Managed Grafana also includes continuous (gradient) color schemes. This is
useful for visualizations that color individual values; for example,
stat panels and the table panel.

#### Thresholds

You can use thresholds to change the color of a field based on the value.
For more information and instructions, see [Thresholds](thresholds.md "thresholds.md").

#### Value mapping

You can use this option to set rules that translate a field value or
range of values into explicit text. You can add more than one value mapping.

- Mapping type – Choose an
  option.
  - Value – Enter a value.
    If the field value is greater than or equal to the value,
    the **Text** is displayed.
  - From and To – Enter a range. If the
    field value is between or equal to the values in the range,
    the **Text** is displayed.

- Text – Text that is displayed
  if the conditions are met in a field. This field accepts variables.
