# Logs panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The logs panel visualization shows log lines from data sources that support logs,
such as Elastic, Influx, and Loki. Typically, you would use this panel next to a graph
panel to display the log output of a related process.

The logs panel shows the result of queries that were entered on the
**Query** tab. The results of multiple queries are merged and
sorted by time. You can scroll inside the panel if the data source returns more lines
than can be displayed.

To limit the number of lines rendered, you can use the **Max data
points** setting in the **Query options**. If it is not
set, the data source will usually enforce a default limit.

## Display options

Use the following settings to refine your visualization:

- Time – Show or hide the time column.
  This is the timestamp associated with the log line as reported from the data
  source.
- Unique labels – Show or hide the unique
  labels column, which shows only non-common labels.
- Wrap lines – Toggle line wrapping.
- Order – Display results in descending
  or ascending time order. The default is **Descending**,
  showing the newest logs first. Set to **Ascending** to show
  the oldest log lines first.
