# Configure value mappings

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

In addition to field overrides, value mapping is a technique that you can use to change
the visual treatment of data that appears in a visualization.

Values mapped via value mappings bypass the unit formatting. This means that a text value
mapped to a numerical value is not formatted using the configured unit.

If value mappings are present in a panel, then Grafana displays a summary in the side
pane of the panel editor.

## Types of value mappings

Grafana supports the following value mappings:

- **Value:** Maps text values to a color or different
  display text. For example, you can configure a value mapping so that all
  instances of the value **10** appear as **Perfection!** rather than the number.
- **Range:** Maps numerical ranges to a display text
  and color. For example, if a value is within a certain range, you can configure
  a range value mapping to display **Low** or
  **High** rather than the number.
- **Regex:** Maps regular expressions to replacement
  text and a color. For example, if a value is
  **www.example.com**, you can configure a regex value
  mapping so that Grafana displays **www** and
  truncates the domain.
- **Special** Maps special values like
  **Null**, **NaN** (not a number), and
  boolean values like **true** and **false** to
  a display text and color. For example, you can configure a special value mapping
  so that **null** values appear as **N/A**.

You can also use the dots on the left to drag and reorder value mappings in the list.

## Map a value

Map a value when you want to format a single value.

1. Open a panel for which you want to map a value.
2. In panel display options, locate the **Value
   mappings** section and click **Add value
   mappings**.
3. Click **Add a new mapping** and then select
   **Value**.
4. Enter the value for Grafana to match.
5. (Optional) Enter display text.
6. (Optional) Set the color.
7. Click **Update** to save the value mapping.

## Map a range

Map a range of values when you want to format multiple, continuous values.

1. Edit the panel for which you want to map a range of values.
2. In panel display options, in the **Value
   mappings** section, click **Add value
   mappings**.
3. Click **Add a new mapping** and then select
   **Range**.
4. Enter the beginning and ending values in the range for Grafana to match.
5. (Optional) Enter display text.
6. (Optional) Set the color.
7. Click **Update** to save the value mapping.

## Map a regular

expression

Map a regular expression when you want to format the text and color of a regular
expression value.

1. Edit the panel for which you want to map a regular expression.
2. In the **Value mappings** section of the
   panel display options, click **Add value
   mappings**.
3. Click **Add a new mapping** and then select
   **Regex**.
4. Enter the regular expression pattern for Grafana to match.
5. (Optional) Enter display text.
6. (Optional) Set the color.
7. Click **Update** to save the value mapping.

## Map a special

value

Map a special value when you want to format uncommon, boolean, or empty values.

1. Edit the panel for which you want to map a special value.
2. In panel display options, locate the **Value
   mappings** section and click **Add value
   mappings**.
3. Click **Add a new mapping** and then select
   **Special**.
4. Select the special value for Grafana to match.
5. (Optional) Enter display text.
6. (Optional) Set the color.
7. Click **Update** to save the value mapping.

## Edit a value mapping

You can change a value mapping at any time.

1. Edit the panel that contains the value mapping you want to edit.
2. In the panel display options, in the **Value
   mappings** section, click **Edit value
   mappings**.
3. Make the changes and click **Update**.
