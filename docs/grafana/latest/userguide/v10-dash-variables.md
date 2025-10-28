# Variables

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

A variable is a placeholder for a value. You can use variables in metric queries and
in panel titles. So when you change the value, using the dropdown at the top of the
dashboard, your panel’s metric queries will change to reflect the new value.

Variables allow you to create more interactive and dynamic dashboards. Instead of
hard-coding things like server, application, and sensor names in your metric queries,
you can use variables in their place. Variables are displayed as dropdown lists at the
top of the dashboard. These dropdowns make it easy to change the data being displayed in
your dashboard.

These can be especially useful for administrators who want to allow Grafana viewers to
quickly adjust visualizations but do not want to give them full editing permissions.
Grafana Viewers can use variables.

Variables and templates also allow you to single-source dashboards. If you have
multiple identical data sources or servers, you can make one dashboard and use variables
to change what you are viewing. This simplifies maintenance and upkeep
enormously.

**Templates**

A template is any query that contains a variable. For example, if you were
administering a dashboard to monitor several servers, you could make a dashboard for
each server, or you could create one dashboard and use panels with template queries,
such as the following.

```
wmi_system_threads{instance=~"$server"}
```

Variable values are always synced to the URL using the syntax
var-<varname>=value.

**Examples**

Variables are listed in dropdown lists across the top of the screen. Select different
variables to see how the visualizations change.

To see variable settings, navigate to **Dashboard Settings >
Variables**. Click a variable in the list to see its
settings.

Variables can be used in titles, descriptions, text panels, and queries. Queries with
text that starts with `$` are templates. Not all panels will have template
queries.

**Variable best practices**

- Variable dropdown lists are displayed in the order they are listed in the
  variable list in **Dashboard settings**.
- Put the variables that you will change often at the top, so they will be shown
  first (far left on the dashboard).
- Variables preselect the topmost value in the dropdown list by default. If
  you want to choose an empty value instead, change the variable settings, as
  follows:
  1.  Select the **Include All Option** checkbox.
  2.  In the **Custom all value** field, enter the
      value `+`.

###### Topics

- [Add and manage variables](v10-dash-variable-add.md "v10-dash-variable-add.md")
- [Inspect Variables](v10-dash-variable-add-inspect.md "v10-dash-variable-add-inspect.md")
- [Variable syntax](v10-dash-variable-syntax.md "v10-dash-variable-syntax.md")
