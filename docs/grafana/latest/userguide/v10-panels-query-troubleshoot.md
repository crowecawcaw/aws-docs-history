# Troubleshoot queries

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

This page provides information to solve common dashboard problems.

**I get different results when I rearrange my
functions**

Function order is very important. Just like in math, the order that you place your
functions can affect the result.

**Inspect your query request and response**

The most common problems are related to the query and response from your data
source. Even if it looks like a bug or visualization issue in Grafana, it is almost
always a problem with the data source query or the data source response. Start by
inspecting your panel query and response.

For more information, refer to [Inspect
request and response data](v10-panels-panel-inspector.md "v10-panels-panel-inspector.md").

**My query is slow**

How many data points is your query returning? A query that returns lots of data
points will be slow. Try this:

- In **Query options**, limit the **Max data
  points** returned.
- In **Query options**, increase the **Min
  interval** time.
- In your query, use a `group by` function.
