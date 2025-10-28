# Searching Dashboards in Grafana version 10

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can search for dashboards by dashboard name and by panel title. When you search
for dashboards, the system returns all dashboards available within the Grafana instance,
even if you do not have permission to view the contents of the dashboard.

## Search dashboards using dashboard name

Enter any part of the dashboard name in the search bar. The search returns
results for any partial string match in real-time, as you type.

Dashboard search is:

- Real-time
- _Not_ case sensitive
- Functional across stored and file based dashboards.

###### Tip

You can use your keyboard arrow keys to
navigate the results and press `Enter` to open
the selected dashboard.

## Search dashboards using panel title

You can search for a dashboard by the title of a panel that appears in a
dashboard. If a panel’s title matches your search query, the dashboard appears in
the search results.

## Filter dashboard search results by tags

Tags are a great way to organize your dashboards, especially as the number of
dashboards grow. You can add and manage tags in dashboard
**Settings**.

When you select multiple tags, Grafana shows dashboards that include all selected
tags.

To filter dashboard search result by a tag, complete one of the following
steps:

- To filter dashboard search results by tag, choose a tag that appears in
  the right column of the search results.

You can continue filtering by choosing additional tags.

- To see a list of all available tags, click the **Filter by
  tags** dropdown menu and select a tag.

All tags will be shown, and when you select a tag, the dashboard
search will be instantly filtered.

###### Tip

When using only a keyboard, press the `tab` key and navigate to the
**Filter by tag** dropdown menu, press the down arrow key to
activate the menu and locate a tag, and press `Enter` to select the
tag.

## Command palette

You can use the command palette to do the following:

- Search for and open dashboards and folders.
- Create dashboards and alert rules.
- Locate pages within Grafana.
- Change the theme to dark or light.

Top open the command palette, enter `ctrl+k` (`cmd+k` in
MacOS). You can also select the search input in the Grafana navigation bar.

###### Note

To go to the previous step, press `backspace` with the command
palette empty.
