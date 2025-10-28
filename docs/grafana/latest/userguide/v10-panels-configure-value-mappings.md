# Configure value mappings

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

In addition to field overrides, value mapping is a technique that you can use to
change how data appears in a visualization.

Values mappings bypass the unit formatting set in the [Standard options](v10-panels-configure-standard-options.md "v10-panels-configure-standard-options.md") of the panel
editor, like color or number of decimal places displayed. When value mappings are
present in a panel, Grafana displays a summary of them in the **Value
mappings** section of the panel editor.

**Supported visualizations**

- Bar chart
- Bar gauge
- Candlestick
- Canvas
- Gauge
- Geomap
- Histogram
- Pie chart
- Stat
- State timeline
- Status history
- Table
- Time series
- Trend

## Types of value mappings

Grafana supports the following value mapping types:

- **Value** – Maps specific values to a text and a
  color. For example, you can configure a value mapping so that all
  instances of the value `10` appear as `Perfection!`
  rather than the number. Use a **Value** mapping when you
  want to format a single value.
- **Range** – Maps numerical ranges to text and a
  color. For example, if a value is within a certain range, you can configure
  a range value mapping to display `Low` or `High`
  rather than the number. Use **Range** mapping when you
  want to formate multiple continuous values.
- **Regex** – Maps regular expressions to text and
  a color. For example, if a value is `www.example.com`, you can
  configure a regex value mapping so that Grafana displays `www`
  and truncates the domain. Use the **Regex** mapping when
  you want to format the text and color of a regular expression value.
- **Special** – Maps special values like
  `Null`, `NaN` (not a number), and Boolean values
  like `true` and `false` to a text and color. For
  example, you can configure a special value mapping so that
  `null` values appear as `N/A`. Use the
  **Special** mappiong when you want to format uncommon,
  Boolean, or empty value.

## Adding a value mapping

You can add value mappings to your panels.

###### To add a value mapping

1. Navigate to the panel you want to update.
2. Hover over any part of the panel to display a menu at the top right
   corner of the panel.
3. From the menu, choose **Edit**.
4. In the **Value mappings** section, choose
   **Add value mappings**.
5. Choose **Add a new mapping**, and then select one of
   the following:
   - **Value** – Enter a single value to
     match.
   - **Range** – Enter the beginning and
     ending values of a range to match.
   - **Regex** – Enter a regular expression
     pattern to match.
   - **Special** – Choose a special value to
     match.

6. (Optional) Enter display text.
7. (Optional) Set the color.
8. Choose **Update** to save the value mapping.

After you've added a mapping, the **Edit value mappings**
button replaces the **Add value mappings** button. Choose the
edit button to add or update mappings.
