# Modifying dashboard settings

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The dashboard settings page enables you to:

- Edit general dashboard properties, including time settings.
- Add annotation queries.
- Add dashboard variables.
- Add links.
- View the dashboard JSON model

###### To access the dashboard setting page

1. Open a dashboard in edit mode.
2. Click **Dashboard settings** (gear icon)
   located at the top of the page.
   **Modifying dashboard time settings**

Adjust dashboard time settings when you want to change the dashboard timezone, the
local browser time, and specify auto-refresh time intervals.

###### To modify dashboard time settings

1. On the **Dashboard** settings page, select
   **General**.
2. Navigate to the **Time Options** section.
3. Specify time settings according to the following descriptions.
4. - **Timezone** – Specify the
     local time zone of the service or system that you are monitoring.
     This can be helpful when monitoring a system or service that
     operates across several time zones.
     - **Default** – Grafana uses
       the default selected time zone
       for the user profile, team, or organization. If no time zone is
       specified for the user profile, a team the user is a member of, or
       the organization, then Grafana uses the local browser time.
     - **Local browser time** – The
       time zone configured for the viewing user browser is used. This is
       usually the same time zone as set on the computer.
     - Use standard [ISO 8601 time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"), including UTC.

   - **Auto-refresh** – Customize
     the options displayed for relative time and the auto-refresh
     options. Entries are comma separated and accept any valid time
     unit.
   - **Now delay** – Override the
     `now` time by entering a time delay. Use this option to
     accommodate known delays in data aggregation to avoid null
     values.
   - **Hide time picker** – Selecting
     this option if you do not want the dashboard to display the time
     picker.

###### Note

To have time controls, your data must include a time column. See the
documentation for your specific [data
source](AMG-data-sources.md "AMG-data-sources.md") for more information about including a time column.

**Adding an annotation query**

An annotation query is a query that queries for events. These events can be
visualized in graphs across the dashboard as vertical lines along with a small icon
you can hover over to see the event information.

###### To add an annotation query

1. On the **Dashboard settings** page, select
   **Annotations**.
2. Select **Add annotation query**.
3. Enter a name and select a data source.
4. Complete the rest of the form to build a query and annotation.
   The query editor UI changes based on the data source that you select. see the
   [Data source](AMG-data-sources.md "AMG-data-sources.md") documentation for details on
   how to construct a query. Or, for data source plugins that you install from the
   [Find plugins with the plugin catalog](grafana-plugins.md#plugin-catalog "grafana-plugins.md#plugin-catalog"), you can use the
   [documentation
   on the Grafana Labs website](https://grafana.com/docs/grafana/v10.3/datasources/ "https://grafana.com/docs/grafana/v10.3/datasources/").

**Adding a variable**

Variables enable you to create more interactive and dynamic dashboards. Instead of
hard-coding things like server, application, and sensor names in your metric
queries, you can use variables in their place. Variables are displayed as dropdown
lists at the top of the dashboard. These dropdowns make it easy to change the data
being displayed in your dashboard.

For more information about variables, see [Variables](v10-dash-variables.md "v10-dash-variables.md").

###### To add a variable

1. On the **Dashboard settings** page, click
   **Variable** in the left side section menu
   and then the **Add variable** button.
2. In the **General** section, add the name of
   the variable. This is the name that you will later use in queries.
3. Select a variable **Type**.

###### Note

The variable type that you select impacts which fields that you
populate on the page. 4. Define the variable and click **Update**.
**Adding a link**

Dashboard links enable you to place links to other dashboards and websites
directly below the dashboard header. Links provide for easy navigation to other,
related dashboards and content.

###### To add a link

1. On the **Dashboard settings** page, choose
   **Links** from the left side section menu and
   then the **Add link** button.
2. Enter a title and in the **Type** field,
   select **Dashboard** or **Link**.
3. To add a dashboard link, add an optional tag, select any of the dashboard
   link Options, and click **Apply**.

###### Note

Using tags creates a dynamic dropdown of dashboards that all
have a specific tag. 4. To add a web link, add a URL and tooltip text that appears when the user
hovers over the link, select an icon that appears next to the link, and
select any of the dashboard link options.
**View dashboard JSON model**

A dashboard in Grafana is represented by a JSON object, which stores the
metadata of a dashboard. Dashboard metadata includes dashboard properties,
metadata from panels, template variables, panel queries, and so on. The
JSON metadata defines the dashboard.

To view a dashboard JSON model, on the **Dashboard
settings** page, click **JSON**.

For more information about the JSON fields, see [JSON fields](v10-dash-dashboard-json-model.md "v10-dash-dashboard-json-model.md").
