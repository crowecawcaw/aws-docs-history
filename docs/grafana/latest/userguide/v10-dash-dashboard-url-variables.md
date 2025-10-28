# Dashboard URL variables

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Grafana can apply variable values passed as query parameters in dashboard URLs.
For more information, see [Manage
dashboard links](v10-dash-manage-dashboard-links.md "v10-dash-manage-dashboard-links.md") and [Templates and
variables](v10-dash-variables.md "v10-dash-variables.md").

**Passing variables as query parameters**

Grafana interprets query string parameters prefixed with `var-` as
variables in the given dashboard.

For example, in this URL:

```
https://${your-domain}/path/to/your/dashboard?var-example=value
```

The query parameter `var-example=value` represents the dashboard
variable example with a value of `value`.

**Passing multiple values for a variable**

To pass multiple values, repeat the variable parameter once for each value.

```
https://${your-domain}/path/to/your/dashboard?var-example=value1&var-example=value2
```

Grafana interprets `var-example=value1&var-example=value2` as the
dashboard variable example with two values: `value1` and
`value2`.

**Adding variables to dashboard links**

Grafana can add variables to dashboard links when you generate them from a
dashboard’s settings. For more information and steps to add variables, see [Manage dashboard links](v10-dash-manage-dashboard-links.md "v10-dash-manage-dashboard-links.md").

**Passing ad hoc filters**

Ad hoc filters apply key or value filters to all metric queries that use a
specified data source. For more information, see [Ad hoc filters](v10-dash-variable-add.md#v10-dash-variable-add-adhoc "v10-dash-variable-add.md#v10-dash-variable-add-adhoc").

To pass an ad hoc filter as a query parameter, use the variable syntax to pass the
ad hoc filter variable, and also provide the key, the operator as the value, and the
value as a pipe-separated list.

For example, in this URL:

`https://${your-domain}/path/to/your/dashboard?var-adhoc=example_key|=|example_value`

The query parameter `var-adhoc=key|=|value` applies the ad hoc filter
configured as the adhoc dashboard variable using the `example_key` key,
the `=` operator, and the `example_value` value.

###### Note

When sharing URLs with ad hoc filters, remember to encode the URL. In the
above example, replace the pipes (`|`) with `%7C` and the
equality operator (`=`) with `%3D`.

**Controlling time range using the URL**

To set a dashboard’s time range, use the `from`, `to`,
`time`, and `time.window` query parameters. Because these
are not variables, they do not require the `var-` prefix.
