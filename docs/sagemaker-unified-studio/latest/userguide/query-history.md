# Review query history

The query history tool displays past queries that you have run. To navigate to the Query
history page, choose the **Query history** icon from the side navigation of the
query editor. Select a data source to view query results from that source.

Queries are sorted so that the most recent queries are listed first. Each query contains the
following information:

- **Execution ID**. This is a unique ID for the query that you ran at a
  specific time.
- **Status**. This displays the status of a query. The following status
  types can be displayed:
  - **Completed**. This means the query was successfully executed and has
    completed running. You can view results for it.
  - **Failed**. A query can fail for a number of reasons. To see more
    details about the query and troubleshoot it, choose the execution ID of the query you want to
    see details for.
  - **Canceled**. A query is canceled if you choose the Stop button on the
    Query editor page before the query finishes running.
  - **Running**. The query editor might show this status if you are
    querying a large dataset. After some time, this status will be updated when the query is
    complete.

- **Duration**. This shows how long it took for the query to finish
  running.
- **SQL**. This shows a preview of the SQL you used to run the query. To
  view the complete SQL, choose the execution ID of a query to see details for it.
- **Start time**. This displays the time and date that the query was
  started. Queries outside of the specified time range at the top of the page are not
  displayed.
- **Engine**. This specifies the engine that was used to perform the
  query.

## Filtering the query history

You can filter query history results by data source, status, and time range. By default,
the query history page displays queries of all status types from the past 24 hours.

To display queries from a different data source, choose Data source and select the data
source you want to see queries from.

To display queries with a certain status, such as Cancelled or Running, choose Status and
then choose the type of status that you want to display. You can also choose All to view queries
of all status types.

To view queries from a different time frame, complete the following steps:

1. Choose **Time range**.
2. Select the time range you want to see queries from.
3. (Optional) If you choose a custom date range, select the time zone you want it in.
4. Choose **Apply**.

## Reviewing additional details

To see more details about a query you have run, select the execution ID of the query you
want to see details for. A side window then opens and displays additional details about the
query, including a display of the SQL that was used to run the query. The details displayed are
different depending on the data source of the query. For instance, in a query for
Amazon Athena you can view AWS S3 encryption information and query stats that show a
visual representation of the time it took to run the query.

To view the full SQL and results of the query, choose **Open in a new
tab**. This opens the query in the query editor tool.
