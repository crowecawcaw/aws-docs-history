# Query management in Explore

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

To help with debugging queries, Explore allows you to investigate query requests and
responses, as well as query statistics, via the Query inspector. This functionality is
similar to the panel inspector tasks [Inspect query performance](v9-panels-panel-inspector.md#v9-panels-query-performance "v9-panels-panel-inspector.md#v9-panels-query-performance") and [Inspect query request and response data](v9-panels-panel-inspector.md#v9-panels-query-request-response "v9-panels-panel-inspector.md#v9-panels-query-request-response").

## Query history

Query history is a list of queries that you used in Explore. The history is stored
in the Grafana database and it is not shared with other users. The retention period
for queries in history is two weeks. Queries older than two weeks are automatically
deleted. To open and interact with your history, select the **Query
history** button in Explore.

###### Note

Starred (favorited) queries are not subject to the
two weeks retention period and they are not deleted.

**View query history**

Query history lets you view the history of your querying. For each individual
query, you can:

- Run a query.
- Create and/or edit a comment.
- Copy a query to the clipboard.
- Copy a shortened link with the query to the clipboard.
- Star (favorite) a query.

**Manage favorite queries**

All queries that have been starred in the Query history tab are displayed in
the Starred list. This allows you to access your favorite queries faster and
to reuse these queries without typing them from scratch.

**Sorting query history**

By default, query history shows you the most recent queries. You can sort your
history by date or by data source name in ascending or descending order.

###### To sort your query history

1. Select the **Sort queries by**
   field.
2. Select one of the following options:
   - Newest first
   - Oldest first

**Filtering query history**

You can filter your query history in Query history and Starred tab to a
specific data source.

###### Filtering history to a data source

1. Select the **Filter queries for specific
   data source(s)** field.
2. Select the data source for which you would like to filter your
   history. You can select multiple data sources.

In the **Query history** tab it is also possible to
filter queries by date using the slider:

- Use the vertical slider to filter queries by date.
- Adjust the start date by dragging the top handle.
- Adjust the end date by dragging the top handle.

**Searching in query history**

You can search in your history across queries and your comments. Search is
possible for queries in the Query history tab and Starred tab.

###### To search in query history

1. Select the **Search queries** field.
2. Enter the term you are searching for into search field.

**Query history settings**

You can customize the query history in the Settings tab. Options are described
in the table below.

| Setting                       | Default value     |
| ----------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Change the default active tab | Query history tab | ###### Note Query history settings are global, and applied to both panels in split mode. ## Prometheus-specific Features Explore features a custom querying experience for Prometheus. When a query is run, it actually runs two queries, a normal Prometheus query for the graph and an _Instant Query_ for the table. An Instant Query returns the last value for each time series which shows a good summary of the data shown in the graph. **Metrics explorer** On the left side of the query field, choose **Metrics** to open the Metric Explorer. This shows a hierarchical menu with metrics grouped by their prefix. For example, all Alertmanager metrics are grouped under the `alertmanager` prefix. This is a good starting point if you just want to explore which metrics are available. **Query field** The Query field supports autocomplete for metric names and functions, comparable to the standard Prometheus query editor. You can press the Enter key to create a new line and Shift+Enter to run a query. The autocomplete menu can be triggered by pressing Ctrl+Space. The Autocomplete menu contains a new History section with a list of recently run queries. Suggestions can appear under the query field - select on them to update your query with the suggested change. <br>• For counters (monotonically increasing metrics), a rate function will be suggested. <br>• For buckets, a histogram function will be suggested. <br>• For recording rules, possible to expand the rules. **Table filters** Select the filter button in the **label** column of a Table panel to add filters to the query expression. You can add filters for multiple queries as well - the filter is added for all the queries. |
