# Inspector in Explore

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The inspector helps you understand and troubleshoot your queries. You can inspect the
raw data, export that data to a comma-separated values (CSV) file, export log results
in TXT format, and view query requests.

## Inspector UI

The inspector has the following tabs:

- **Stats tab** – Shows how long
  your query takes and how much it returns.
- **Query tab** – Shows you the
  requests to the server sent when Grafana queries the data
  source.
- **JSON tab** – Allows you to
  view and copy the data JSON and data frame structure JSON.
- **Data tab** – Shows the raw
  data returned by the query.
- **Error tab** – Shows the
  error. Only visible when query returns error.

## Inspector tasks

You can perform a variety of tasks in the Explore inspector.

**Open the Inspector**

After you run the query you would like to inspect, select the
**Inspector** button.

The inspector pane opens on the bottom of the screen.

**Inspect raw query results**

You can view raw query results, that is the data returned by the query in a
table.

In the **Inspector** tab, click the
**Data** tab.

For multiple queries or for queries multiple nodes, there are additional
options.

- **Show data frame:** Select the
  result set data you want to view.
- **Series joined by time:** View the raw data from
  all of your queries at once, one result set per column. You can click
  a column heading to sort the data.

**Download raw query results as CSV**

Grafana generates a CSV file in your default browser download location. You can
open it in the viewer of your choice.

1. In the **Inspector** tab, get raw query results by
   following the instructions above.
2. Refine the query settings until you can see the raw data that you want
   to export.
3. Choose **Download CSV**.

In order to download a CSV file specifically formatted for Excel, expand
**Data options** and then turn on the **Download
for Excel** toggle before you select the
**Download CSV** option.

**Download log results as TXT**

You can generate a TXT file of the logs you are currently viewing, by selecting
**Download logs** in the **Inspector**tab.

**Download trace results**

Based on the data source type, Grafana generates a JSON file for the trace
results in one of the supported formats: Jaeger, Zipkin, or OTLP formats.

1. Open the Inspector.
2. Inspect the log query results. Refine the results until you see the raw
   logs that you want to export.
3. Choose **Download logs**.

**Inspect query performance**

The **Stats** tab displays statistics that tell you how
long your query takes, how many queries you send, and the number of rows
returned. This information can help you troubleshoot your queries, especially
if any of the numbers are unexpectedly high or low.

Statistics are displayed in read-only format.

**View JSON model**

You can explore and export data as well as data frame JSON models.

###### To view the JSON model

1. In the Inspector panel, click the **JSON** tab.
2. From the **Select source** dropdown, choose one
   of the following options:
   - **Data** – Displays a JSON object
     representing the data that was returned to Explore.
   - **DataFrame structure** – Displays the
     raw result set.

3. You can expand or collapse portions of the JSON to view separate
   sections. You can also select the **Copy to
   clipboard** option to copy JSON body and paste it into
   another application.

**View raw request and response to data
source**

As you are working with Explore and the Inspector tab, you can view the
raw request and response data that you are generating with a query. In the
Inspector, select the **Query** tab and choose
**Refresh** to see the raw data.

Grafana sends the query to the server and displays the result. You can drill
down on specific portions of the query, expand or collapse all of it, or copy
the data to the clipboard to use in other applications.
