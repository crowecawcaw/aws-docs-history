# Query management in Explore

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can manage the queries that you have created in Explore, including a history of
queries that you have run, and queries that you have starred.

## Query history

Query history is a list of queries that you used in Explore. The history is stored
in the Grafana database and it is not shared with other users. The retention period
for queries in history is two weeks. Queries older than two weeks are automatically
deleted. To open and interact with your history, select the **Query
history** button in Explore.

###### Note

Starred (favorited) queries are not subject to the
two weeks retention period and they are not deleted.

## View query history

Query history lets you view the history of your querying. For each individual
query, you can:

- Run the query.
- Create and/or edit a comment.
- Copy a query to the clipboard.
- Copy a shortened link with the query to the clipboard.
- Star (favorite) a query.

## Manage favorite queries

All queries that have been starred in the Query history tab are displayed in
the Starred tab. This allows you to access your favorite queries faster and
to reuse these queries without typing them from scratch.

## Sorting query history

By default, query history shows you the most recent queries. You can sort your
history by date or by data source name in ascending or descending order.

###### To sort your query history

1. Select the **Sort queries by**
   field.
2. Select one of the following options:
   - **Newest first**
   - **Oldest first**

## Filtering query history

You can filter your query history in Query history and Starred tab to a
specific data source.

###### To filter history to a data source

1. Select the **Filter queries for specific
   data source(s)** field.
2. Select the data source for which you would like to filter your
   history. You can select multiple data sources.

###### Note

Queries ran using the Mixed data source will appear only when filtering for
Mixed, and not when filtering by their individual data sources.

In the **Query history** tab it is also possible to
filter queries by date using the slider:

- Use the vertical slider to filter queries by date.
- Adjust the start date by dragging the bottom handle.
- Adjust the end date by dragging the top handle.

## Searching in query history

You can search in your history across queries and your comments. Search is
possible for queries in the Query history tab and Starred tab.

###### To search in query history

1. Select the **Search queries** field.
2. Enter the term you are searching for into search field.

## Query history settings

You can customize the query history in the Settings tab. Options are described
in the following table.

| Setting                       | Default value     |
| ----------------------------- | ----------------- |
| Change the default active tab | Query history tab |

###### Note

Query history settings are global,
and applied to both panels in split mode.
