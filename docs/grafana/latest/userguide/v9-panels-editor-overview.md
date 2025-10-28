# Panel editor overview

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

This section describes the areas of the Grafana panel editor.

- Panel header: The header section lists the dashboard in which the panel appears
  and the following controls:
  - **Dashboard settings (gear) icon:** Click to
    access the dashboard settings.
  - **Discard:** Discards changes you have made to
    the panel since you last saved the dashboard.
  - **Save:** Saves changes you made to the panel.
  - **Apply:** Applies changes you made and closes
    the panel editor, returning you to the dashboard. You will have to save the
    dashboard to persist the applied changes.

- Visualization preview: The visualization preview section contains the following
  options:
  - **Table view:** Convert any visualization to a
    table so you can see the data. Table views are helpful for troubleshooting.
    This view only contains the raw data. It does not include transformations
    you might have applied to the data or the formatting options available in
    the [Table](v9-panels-table.md "v9-panels-table.md") visualization.
  - **Fill:** The visualization preview fills the
    available space. If you change the width of the side pane or height of the
    bottom pane the visualization changes to fill the available space.
  - **Actual:** The visualization preview will have
    the exact size as the size on the dashboard. If not enough space is
    available, the visualization will scale down preserving the aspect ratio.
  - **Time range controls:**
    **Default** is either the browser local
    timezone or the timezone selected at a higher level.

- Data section: The data section contains tabs where you enter queries, transform
  your data, and create alert rules (if applicable).
  - **Query tab:** Select your data source and
    enter queries here.
  - **Transform tab:** Apply data transformations.
  - **Alert tab:** Write alert rules.

- Panel display options: The display options section contains tabs where you
  configure almost every aspect of your data visualization.

## Open the panel inspect drawer

The inspect drawer helps you understand and troubleshoot your panels. You can view
the raw data for any panel, export that data to a comma-separated values (CSV) file,
view query requests, and export panel and data JSON.

The panel inspector consists of the following options:

- The panel inspect drawer displays opens a drawer on the right side. Click the
  arrow in the upper right corner to expand or reduce the drawer pane.
- **Data tab -** Shows the raw data returned by the
  query with transformations applied. Field options such as overrides and value
  mappings are not applied by default.
- **Stats tab -** Shows how long your query takes and
  how much it returns.
- **JSON tab -** Allows you to view and copy the
  panel JSON, panel data JSON, and data frame structure JSON. This is useful if
  you are provisioning or administering Grafana.
- **Query tab -** Shows you the requests to the
  server sent when Grafana queries the data source.
- **Error tab -** Shows the error. Only visible when
  query returns error.
