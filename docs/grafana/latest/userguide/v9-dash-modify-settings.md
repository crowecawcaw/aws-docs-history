# Modifying dashboard settings

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The dashboard settings page enables you to:

- Edit general dashboard properties, including time settings.
- Add annotation queries.
- Add dashboard variables.
- Add links.
- View the dashboard JSON model
  To access the dashboard setting page:

1. Open a dashboard in edit mode.
2. Click **Dashboard settings** (gear icon)
   located at the top of the page.
   **Modifying dashboard time settings**

Adjust dashboard time settings when you want to change the dashboard timezone, the
local browser time, and specify auto-refresh time intervals.

###### To modify dashboard time settings

1. On the **Dashboard** settings page, select
   **General**.
2. Navigate to the **Time Options**
   section.
3. Specify time settings according to the following descriptions.
4. Timezone specifies the local time zone of the service or system that you
   are monitoring. This can be helpful when monitoring a system or service that
   operates across several time zones.
   - Grafana uses the _default_ selected
     time zone for the user profile, team, or organization. If no time
     zone is specified for the user profile, a team the user is a member
     of, or the organization, then Grafana uses the local browser
     time.
   - The time zone configured for the viewing user browser, the
     _local browser time_, is used.
     This is usually the same time zone as set on the computer.
   - Use standard [ISO 8601 time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"), including UTC.

- **Auto-refresh** customizes the options
  displayed for relative time and the auto-refresh options Entries are comma
  separated and accept any valid time unit.
- **Now delay** overrides the `now`
  time by entering a time delay. Use this option to accommodate known delays
  in data aggregation to avoid null values.
- **Hide time picker** removes the Grafana time
  picker display.

###### Note

To have time controls, your data must include a time column. See the
documentation for your specific [data source](AMG-data-sources.md "AMG-data-sources.md")
for more information about including a time column.

**Adding an annotation query**

An annotation query is a query that queries for events. These events can be
visualized in graphs across the dashboard as vertical lines along with a small icon
you can hover over to see the event information.

###### To add n annotation query

1. On the **Dashboard settings** page, select
   **Annotations**.
2. Select **Add annotation query**.
3. Enter a name and select a data source.
4. Complete the rest of the form to build a query and annotation.
   The query editor UI changes based on the data source that you select. see the
   [Data source](AMG-data-sources.md "AMG-data-sources.md") documentation for details on
   how to construct a query.

**Adding a variable**

Variables enable you to create more interactive and dynamic dashboards. Instead of
hard-coding things like server, application, and sensor names in your metric
queries, you can use variables in their place. Variables are displayed as dropdown
lists at the top of the dashboard. These dropdowns make it easy to change the data
being displayed in your dashboard.

For more information about variables, see [Variables](v9-dash-variables.md "v9-dash-variables.md").

1. On the **Dashboard settings** page, click
   **Variable** in the left side section menu
   and then the **Add variable** button.
2. In the **General** section, the the name of
   the variable. This is the name that you will later use in queries.
3. Select a variable **Type**.

###### Note

The variable type that you select impacts which fields that you
populate on the page. 4. Define the variable and click **Update**.
**Adding a link**

Dashboard links enable you to place links to other dashboards and websites
directly below the dashboard header. Links provide for easy navigation to other,
related dashboards and content.

1. On the **Dashboard settings** page, click
   **Links** in the left side section menu and
   then the **Add link** button.
2. Enter title and and in the **Type** field,
   select **Dashboard** or **Link**.
3. To add a dashboard link, add an optional tag, select any of the dashboard
   link Options, and click **Apply**.

###### Note

Tags are useful creating a dynamic dropdown of dashboards that all
have a specific tag. 4. To add a link, add a URL and tooltip text that appears when the user
hovers over the link, select an icon that appears next to the link, and
select any of the dashboard link options.
**View dashboard JSON model**

A dashboard in Grafana is represented by a JSON object, which stores metadata of
its dashboard. Dashboard metadata includes dashboard properties, metadata from
panels, template variables, panel queries, and so on.

To view a dashboard JSON model, on the **Dashboard
settings** page, click **JSON**.

For more information about the JSON fields, see [JSON fields](v9-dash-dashboard-json-model.md "v9-dash-dashboard-json-model.md").
