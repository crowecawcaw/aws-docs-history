# Linking

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

You can use links to navigate between commonly used dashboards or to connect others to
your visualizations. Links let you create shortcuts to other dashboards, panels, and even
external websites.

Amazon Managed Grafana supports dashboard links, panel links, and data links. Dashboard links are
displayed at the top of the dashboard. Panel links are accessible by choosing an icon on the
top-left corner of the panel.

## Which link should you use?

Start by examining how you’re currently navigating between dashboards. If you’re
often jumping between a set of dashboards and struggling to find the same context in
each, links can help optimize your workflow.

The next step is to figure out which link type is right for your workflow. Although
all the link types in Grafana are used to create shortcuts to other dashboards or
external websites, they work in different contexts.

- To add links that relate to most or all of the panels in the dashboard, use
  [Dashboard links](dashboard-links.md "dashboard-links.md").
- To drill down into specific panels, use [Panel links](panel-links.md "panel-links.md").
- To link to external sites, you can use either a dashboard link or a panel
  link.
- To drill down into a specific series, or even a single measurement, use [Data links](data-links.md "data-links.md").

## Controlling time range using the

URL

You can control the time range of a panel or dashboard by providing the following
query parameters in the dashboard URL:

- `from` defines lower limit of the time range, specified in ms epoch.
- `to` defines upper limit of the time range, specified in ms epoch.
- `time` and `time.window` define a time range from
  `time-time.window/2` to `time+time.window/2`. Both
  parameters should be specified in milliseconds. For example,
  `?time=1500000000000&time.window=10000` will result in a
  10-second time range from 1499999995000 to 1500000005000

## Data link variables

You can use variables in data links to see series fields, labels, and values. For
more information about data links, see [Data links](data-links.md "data-links.md").

To see a list of available variables, enter **$** in the
data link **URL** field.

You can also use template variables in your data links URLs. For more information,
see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

### Time range panel variables

You can use the following variables to include the current time range in the data
link URL:

- `__url_time_range` – The current dashboard’s time range;
  for example, `?from=now-6h&to=now`
- `$__from and $__to` – For more information, see [Global
  variables]({{< relref
  "../variables/variable-types/global-variables.md#\_\_from-and-\_\_to"
  > }}).

### Series variables

Series-specific variables are available under the `__series`
namespace:

- `__series.name` – Adds the series name to the URL
- `__series.labels.<LABEL>` – Adds the label’s value to
  the URL. If your label contains dots, use
  `__series.labels["<LABEL>"]` syntax.

### Field variables

Field-specific variables are available under the `__field` namespace:

- `__field.name` – The name of the field

### Value variables

Value-specific variables are available under the `__value` namespace:

- `__value.time` – The value’s timestamp (Unix ms epoch) to
  the URL; for example, `?time=1560268814105`
- `__value.raw` – The raw value
- `__value.numeric` – The numeric representation of a value
- `__value.text` – The text representation of a value
- `__value.calc` – The calculation name if the value is
  result of calculation

### Template variables

When linking to another dashboard that uses template variables, select variable
values for whoever chooses the link.

Use `var-myvar=${myvar}`, where `myvar` is a name of the
template variable that matches one in the current dashboard that you want to use.

To add all of the current dashboard’s variables to the URL, use
`__all_variables`.
