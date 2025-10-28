# Recorded queries

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

You can see trends over time by taking a snapshot of a data point on a set interval using
recorded queries. This can give you insight into historic trends.

For the plugins that do not return time series, it might be useful to plot historical
data. For example, you might want to query **ServiceNow** to see a history
of request response times but it can only return current point-in-time metrics.

## How recorded queries work

Recorded queries only work with backend data source plugins. For more information,
refer to [Backend data source plugin](https://grafana.com/tutorials/build-a-data-source-backend-plugin/ "https://grafana.com/tutorials/build-a-data-source-backend-plugin/"). You can record three types of queries:

- single row and column - A query that returns a single row and column.
- row count - A query that returns meaningful rows to be counted.
- expression - Any expression. To learn more about creating and using
  expressions, see [Expressions](https://grafana.com/docs/grafana/next/panels-visualizations/query-transform-data/expression-queries/ "https://grafana.com/docs/grafana/next/panels-visualizations/query-transform-data/expression-queries/").

After a recorded query is created or enabled, it immediately creates a snapshot and
continues to create snapshots at the set interval. The recorded query stops taking
snapshots when it is disabled, deleted, or when Grafana is not running. Data points are
gathered in the backend by running the recorded query and forwarding each result to a
remote write enabled Prometheus instance.

###### Note

You must configure a Prometheus data source and associate it with a Remote write
target before recorded queries can be used.

## Create a recorded query

To create a recorded query, complete the following steps:

1. Find or create a query you want to record on a dashboard in an edit panel. The
   query must only return one row and column. If it returns more, you can still
   record the number of results returned using the _count_ option. The query’s data source must be a backend data
   source. Expressions can be used to aggregate data from a time series query. To
   learn more about creating and using expressions, refer to [Expressions](https://grafana.com/docs/grafana/next/panels-visualizations/query-transform-data/expression-queries/ "https://grafana.com/docs/grafana/next/panels-visualizations/query-transform-data/expression-queries/").
2. Choose the **record query** menu located in the query
   editor.
3. Enter recorded query information. All fields are required unless otherwise
   indicated.
   - Name - Name of the recorded query.
   - Description - (optional) Describe the recorded query as you want it to
     appear in the recorded query list.
   - Interval - The interval at which the snapshot will be taken. The
     interval starts when you create the recorded query and stops if you
     pause or delete the recorded query. For more information on pausing and
     deleting recorded queries, refer to [Managing recorded queries](https://grafana.com/docs/grafana/latest/enterprise/recorded-queries/#manage-recorded-queries "https://grafana.com/docs/grafana/latest/enterprise/recorded-queries/#manage-recorded-queries").
   - Range - The relative time range of the query. If you select a range of
     30m and an interval of 1h the query will take a snapshot every hour of
     the past 30 minutes.
   - Count query results - If you want to count the rows returned from your
     query toggle this option on. If this option is off, your query must
     return one row with one value.

4. Test your recorded query by choosing the test recorded query button.
5. Choose **Start recording query**.

## Adding a recorded query

You can add existing recorded queries to panels in a dashboard. For each recorded
query that you add, a Prometheus query is created:
`generated_recorded_query_name{id="generated_id", name="recorded query
 name"}`. The created query from Prometheus returns all the recorded query’s
gathered snapshots.

1. Navigate to a panel in a dashboard where you wish to add a recorded
   query.
2. Choose the **+ Recorded query** menu.
3. If you want to filter recorded queries by data source, select a data source
   from the filter by data source drop down menu.
4. Choose **Add** menu on your recorded query to add it to the
   panel.

After adding your recorded query to the panel, the panel data source will become
`-- Mixed --`. Your recorded query is represented by a
`Prometheus` query with a name label matching your recorded query name.
Refer to [Prometheus](https://grafana.com/docs/grafana/latest/datasources/prometheus/ "https://grafana.com/docs/grafana/latest/datasources/prometheus/") to learn more about the Prometheus data source.

If after adding a recorded query, a query with a `-- Mixed --` data source
instead of Prometheus data source appears, this could mean that a `Prometheus` remote write target was not set up for recorded queries. Refer to [Remote write target](https://grafana.com/docs/grafana/latest/enterprise/recorded-queries/#remote-write-target "https://grafana.com/docs/grafana/latest/enterprise/recorded-queries/#remote-write-target") to set up a remote write point.

## Using a recorded query

To use a recorded query, create one and add it to a dashboard. After that, it can be
managed in **Preferences** from the **Recorded
queries** tab.

## Managing recorded queries

Recorded queries can be paused or activated and deleted from the Recorded queries tab
in Preferences. Deleting a recorded query will remove it from Grafana, but the
information that was gathered in Prometheus will still be there. Pausing a recorded
query will no longer gather new data points until it is resumed.

## Remote write target

The remote write target is the **Prometheus** data source that
recorded query data points are written to. You will need a Prometheus with remote write
enabled and you will need to create a data source for this Prometheus.

To edit the remote write target choose **Edit Remote Write Target**
in the console menu on the **Recorded Queries** tab in
**Preferences**. Select the **Prometheus** data
source that has remote write enabled and enter the remote write path.
