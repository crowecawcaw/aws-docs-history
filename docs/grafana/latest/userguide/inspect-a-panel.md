# Inspect a panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The panel inspector helps you understand and troubleshoot your panels. You can
inspect the raw data for any Grafana workspace panel, export that data to a
comma-separated values (CSV) file, view query requests, and export panel and data JSON.

## Panel inspector UI

The panel inspector displays **Inspect:
<NameOfPanelBeingInspected>** at the top of the pane. Choose the
arrow in the upper right corner to expand or reduce the pane.

The panel inspector consists of four tabs:

- Data tab – Shows the raw data returned
  by the query with transformations applied. Field options, such as overrides
  and value mappings, are not applied by default.
- Stats tab – Shows how long your query
  takes and how much it returns.
- JSON tab – Allows you to view and copy
  the panel JSON, panel data JSON, and data frame structure JSON. This is
  useful if you are provisioning or administering Amazon Managed Grafana.
- Query tab – Shows you the requests to
  the server sent when Amazon Managed Grafana queries the data source.

###### Note

Not all panel types include all four tabs. For example, dashboard list panels
do not have raw data to inspect, so they do not display the Stats, Data, or
Query tabs.

## Panel inspector tasks

In the panel inspector, you can inspect panels, inspect and download raw query
results, inspect query performance, view panel JSON models, and view the raw request
and response to the data source.

### Open the panel inspector

You can inspect any panel that you can view.

1. In the Grafana workspace console, choose the dashboard that contains
   the panel that you want to inspect.
2. Choose the title of the panel that you want to inspect, and then
   choose **Inspect**. Or pause over the panel title, and
   then press **i**.

The panel inspector pane opens on the right side of the screen.

### Inspect raw query results

View raw query results in a table. These are the data returned by the query
with transformations applied and before the panel applies field options or field
option overrides.

1. Open the panel inspector, and then choose the
   **Data** tab. Or in the panel menu, choose
   **Inspect**, **Data**.
2. If your panel contains multiple queries or queries multiple nodes,
   you have additional options.

- Select result – Choose which result
  set data you want to view.
- **Transform data**

      + Join by time – View raw
       data from all your queries at the same time, with one result set
       per column. Choose a column heading to reorder the data.

  View raw query results in a table with field options and option
  overrides applied.

      1. Open the **Data** tab in the panel
       inspector.
      2. Above the table, choose on **Data display
       options**.
      3. Choose the **Apply field
       configuration** toggle button.

### Download raw query results

as a CSV file

Amazon Managed Grafana generates a CSV file in your default browser download location. You
can open it in the viewer of your choice.

1. Open the panel inspector.
2. Inspect the raw query results as described above. Adjust settings
   until you see the raw data that you want to export.
3. Choose **Download CSV**.

To download a CSV file formatted for Excel, expand the **Data
options** panel and turn on the **Download for
Excel** option before you choose **Download CSV**.

### Inspect query performance

The **Stats** tab displays statistics that tell you how long
your query takes, how many queries you send, and the number of rows returned.
This information can help you troubleshoot your queries, especially if any of
the numbers are unexpectedly high or low.

1. Open the panel inspector.
2. Choose the **Stats** tab.

Statistics are displayed in read-only format.

### View panel JSON models

Explore and export panel, panel data, and data frame JSON models.

1. Open the panel inspector, and then choose the
   **JSON** tab. Or, in the panel menu, choose
   **Inspect**, **Panel JSON**.
2. In **Select source**, choose one of the following
   options:
   - Panel JSON – Displays a
     JSON object representing the panel.
   - Panel data – Displays a
     JSON object representing the data that was passed to the panel.
   - DataFrame structure –
     Displays the raw result set with your transformations, field
     configuration, and overrides applied.

3. You can expand or collapse portions of the JSON to explore it, or you
   can choose **Copy to clipboard** and paste the JSON in
   another application.

### View raw request

and response to data source

1. Open the panel inspector, and then choose the
   **Query** tab. Or, in the panel menu, choose
   **Inspect**, **Query**.
2. Choose **Refresh**.

Amazon Managed Grafana sends a query to the server to collect information, and then it
displays the result. You can drill down on specific portions of the query,
expand or collapse all of it, or copy the data to the clipboard to use in other
applications.
