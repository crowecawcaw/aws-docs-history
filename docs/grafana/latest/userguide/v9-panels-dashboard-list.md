# Dashboard list

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The dashboard list visualization allows you to display dynamic links to other
dashboards. The list can be configured to use starred dashboards, recently viewed
dashboards, a search query, and dashboard tags.

On each dashboard load, this panel queries the dashboard list, always providing the
most up-to-date results.

**Options**

Use these options to refine your visualization.

- **Starred** – Display starred
  dashboards in alphabetical order.
- **Recently viewed** – Display
  recently viewed dashboards in alphabetical order.
- **Search** – Display dashboards
  by search query or tags. You must enter at least one value in
  **Query** or **Tags**. For the
  **Query** and **Tags** fields,
  variable interpolation is supported, for example, `$my_var`
  or `${my_var}`.
- **Show headings** – The chosen
  list selection (Starred, Recently viewed, Search) is shown as a
  heading.
- **Max items** – Sets the maximum
  number of items to list per section. For example, if
  you left this at the default value of 10 and displayed Starred and
  Recently viewed dashboards, then the panel would display up to 20 total
  dashboards, ten in each section.
  **Search**

These options only apply if the **Search** option is
selected.

- **Query** – Enter the query you
  want to search by. Queries are case-insensitive,
  and partial values are accepted.
- **Folder** – Select the dashboard folders
  that you want to display.
- **Tags** – Here is where you enter your
  tags you want to search by. Existing tags will not appear as you type, and they
  _are_ case sensitive.

###### Note

When multiple tags and strings appear, the dashboard list displays those
matching _all_ conditions.
