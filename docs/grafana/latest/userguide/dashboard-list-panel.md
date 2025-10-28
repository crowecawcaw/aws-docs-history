# Dashboard list panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The dashboard list panel displays dynamic links to other dashboards. The list can be
configured to use starred dashboards, recently viewed dashboards, a search query, and
dashboard tags.

On each dashboard load, this panel queries the dashboard list, always providing the
most up-to-date results.

## Options

Use the following options to refine your visualization:

- Starred – Display starred dashboards in
  alphabetical order.
- Recently viewed – Display recently
  viewed dashboards in alphabetical order.
- Search – Display dashboards by search
  query or tags. This option requires you to enter at least one value in
  **Query** or **Tags**.
- Show headings – Show the chosen list
  selection (Starred, Recently viewed, Search) as a heading.
- Max items – Set the maximum number of
  items to list per section. For example, at the default value of 10, if
  choose to display starred and recently viewed dashboards, the panel displays
  up to 20 total dashboards, 10 in each section.

### Search

The following options apply only if the **Search** option is selected.

- Query – Enter the query that you
  want to search. Queries are not case sensitive, and partial values are
  accepted.
- Folder – Select the dashboard
  folders that you want to display.
- Tags – Enter the tags that you want
  to search. Note that existing tags will not appear as you type, and tags
  _are_ case sensitive.

###### Note

When multiple tags and strings appear, the dashboard list displays those
matching _all_ conditions.
